"""
REFERENCE ONLY — NOT EXECUTED

This file is a reference mirror of the GPT-executed Generative Execution DAG (GED).
It MUST NOT be invoked as a controller or execution entrypoint.
"""

#!/usr/bin/env python3
"""cbia-builder pipeline runner (self-contained)

This runner is designed to be executable in constrained environments (e.g., mobile-driven
workflows where the user cannot run commands locally). It preserves the *audit semantics*
by emitting:
- PRE-GEN capsule
- an OPA-compatible decision + explain payload (implemented as an embedded assurance evaluator)
- a run ledger + artifact hash map

It replaces the previous dummy GEN with a real, TP1-scoped INF1220 material build.
"""

import json, os, hashlib, sys, datetime, shutil
from typing import Any, Dict, List, Tuple

ROOT = os.path.dirname(os.path.dirname(__file__))

PHASE_ORDER = ["PRE_GEN", "OPA_GATE", "GEN", "STRUCT", "SELECT", "FLOW", "EVAL"]

def _read_json(p: str) -> Any:
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def _write_json(p: str, obj: Any) -> None:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)

def _sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def sha256_dir(path: str) -> str:
    """Stable hash over a directory tree (paths + file hashes)."""
    items: List[Tuple[str,str]] = []
    for root, _, files in os.walk(path):
        for fn in sorted(files):
            p = os.path.join(root, fn)
            rel = os.path.relpath(p, path)
            items.append((rel, sha256_file(p)))
    blob = json.dumps(items, sort_keys=True).encode("utf-8")
    return _sha256_bytes(blob)

def now_utc() -> str:
    return datetime.datetime.utcnow().isoformat() + "Z"

def init_ledger(policy_bundle_hash: str) -> List[Dict[str, Any]]:
    return [
        {
            "entry_id": "LEDGER-0001",
            "phase": "PRE_GEN",
            "artifact_id": "",
            "artifact_path": "",
            "hash": "",
            "objective_ids": [],
            "authority_ids": [],
            "policy_bundle_hash": policy_bundle_hash,
            "timestamp": now_utc(),
        },
        {
            "entry_id": "LEDGER-0002",
            "phase": "OPA_GATE",
            "artifact_id": "",
            "artifact_path": "",
            "hash": "",
            "objective_ids": [],
            "authority_ids": [],
            "policy_bundle_hash": policy_bundle_hash,
            "timestamp": now_utc(),
        },
    ]

def pre_gen() -> Dict[str, Any]:
    auth = _read_json(os.path.join(ROOT, "control/authority.ledger.json"))
    hashes = {a["authority_id"]: a["hash"]["value"] for a in auth["authority_set"]}
    policy_bundle_hash = sha256_dir(os.path.join(ROOT, "policy"))
    capsule = {
        "schema_version": "0.1.0",
        "kernel_decision": "ALLOW" if auth.get("frozen") else "DENY",
        "control_state_hash": _sha256_bytes(json.dumps(hashes, sort_keys=True).encode("utf-8")),
        "policy_bundle_hash": policy_bundle_hash,
        "authority_set_hashes": hashes,
        "timestamp": now_utc(),
    }
    _write_json(os.path.join(ROOT, "control/runtime/pre_gen_capsule.json"), capsule)
    if capsule["kernel_decision"] != "ALLOW":
        sys.exit("PRE-GEN denied")
    return capsule

def assurance_eval(input_bundle: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Embedded evaluator for policy/assurance/assurance.rego intent.

    This is not a full Rego engine. It implements the exact checks used by the current
    assurance.rego in this repo, with one pragmatic constraint: it assumes the runner
    populates PRE_GEN and OPA_GATE ledger entries before GEN so deterministic replay is defined.
    """
    explain: List[str] = []

    # auth_immutable
    try:
        capsule = input_bundle["pre_gen_capsule"]
        ledger = input_bundle["authority_ledger"]
        if capsule.get("kernel_decision") != "ALLOW":
            explain.append("auth_immutable: FAIL (kernel_decision != ALLOW)")
            return False, explain
        if ledger.get("frozen") is not True:
            explain.append("auth_immutable: FAIL (authority_ledger.frozen != true)")
            return False, explain
        capsule_hashes = capsule.get("authority_set_hashes", {})
        ledger_hashes = {a["authority_id"]: a["hash"]["value"] for a in ledger.get("authority_set", [])}
        if capsule_hashes != ledger_hashes:
            explain.append("auth_immutable: FAIL (capsule hashes != ledger hashes)")
            return False, explain
        explain.append("auth_immutable: PASS")
    except Exception as e:
        explain.append(f"auth_immutable: ERROR ({e})")
        return False, explain

    # closed_world_authority
    authority_ids = {a["authority_id"] for a in input_bundle["authority_ledger"].get("authority_set", [])}
    used = set()
    for e in input_bundle.get("run_ledger", []):
        for aid in e.get("authority_ids", []):
            used.add(aid)
    if not used.issubset(authority_ids):
        explain.append("closed_world_authority: FAIL (used authority id not in ledger)")
        return False, explain
    explain.append("closed_world_authority: PASS")

    # dependency_closure: objective -> authority
    objectives = input_bundle.get("objectives", [])
    obj_to_auth = {o.get("id"): (o.get("source", {}) or {}).get("authority_id", "") for o in objectives}
    for e in input_bundle.get("run_ledger", []):
        if e.get("artifact_id"):
            for oid in e.get("objective_ids", []):
                if not obj_to_auth.get(oid):
                    explain.append(f"dependency_closure: FAIL (objective {oid} has no authority_id)")
                    return False, explain
    explain.append("dependency_closure: PASS")

    # inference_compliance (only for type == inferred)
    for o in objectives:
        if o.get("type") == "inferred":
            if not o.get("justification") or not o.get("constraints"):
                explain.append(f"inference_compliance: FAIL (inferred objective {o.get('id')} missing justification/constraints)")
                return False, explain
    explain.append("inference_compliance: PASS")

    # phase admissibility
    phases = [e.get("phase") for e in input_bundle.get("run_ledger", [])]
    idx = [PHASE_ORDER.index(p) for p in phases if p in PHASE_ORDER]
    if idx != sorted(idx):
        explain.append("phase_admissibility: FAIL (phase order not monotone)")
        return False, explain
    explain.append("phase_admissibility: PASS")

    # artifact integrity (only for entries with artifact_path)
    artifact_hashes = input_bundle.get("artifact_hashes", {})
    for e in input_bundle.get("run_ledger", []):
        ap = e.get("artifact_path", "")
        if ap:
            if artifact_hashes.get(ap) != e.get("hash"):
                explain.append(f"artifact_integrity: FAIL (hash mismatch for {ap})")
                return False, explain
    explain.append("artifact_integrity: PASS")

    # deterministic replay: capsule policy hash == first ledger policy hash
    run_ledger = input_bundle.get("run_ledger", [])
    if not run_ledger:
        explain.append("deterministic_replay: FAIL (run_ledger empty)")
        return False, explain
    if input_bundle["pre_gen_capsule"].get("policy_bundle_hash") != run_ledger[0].get("policy_bundle_hash"):
        explain.append("deterministic_replay: FAIL (policy bundle hash mismatch)")
        return False, explain
    explain.append("deterministic_replay: PASS")

    return True, explain

def opa_gate(pre_gen_capsule: Dict[str, Any], run_ledger: List[Dict[str, Any]], artifact_hashes: Dict[str,str]) -> None:
    input_bundle = {
        "pre_gen_capsule": pre_gen_capsule,
        "authority_ledger": _read_json(os.path.join(ROOT, "control/authority.ledger.json")),
        "objectives": _read_json(os.path.join(ROOT, "objectives.json")) if os.path.exists(os.path.join(ROOT, "objectives.json")) else [],
        "dependency_graph": _read_json(os.path.join(ROOT, "dependency.graph.json")) if os.path.exists(os.path.join(ROOT, "dependency.graph.json")) else {},
        "execution_dag": _read_json(os.path.join(ROOT, "execution_dag.json")) if os.path.exists(os.path.join(ROOT, "execution_dag.json")) else {},
        "run_ledger": run_ledger,
        "artifact_hashes": artifact_hashes,
    }
    _write_json(os.path.join(ROOT, "opa/input.json"), input_bundle)

    allow, explain = assurance_eval(input_bundle)

    decision = {
        "result": [
            {"expressions": [{"value": allow}]}
        ]
    }
    _write_json(os.path.join(ROOT, "opa/decision.json"), decision)
    _write_json(os.path.join(ROOT, "opa/explain.json"), {"explain": explain, "allow": allow})

    _write_json(os.path.join(ROOT, "opa/bundle.hash"), {"policy_bundle_hash": pre_gen_capsule["policy_bundle_hash"]})

    if not allow:
        sys.exit("OPA gate denied")

def gen_inf1220_tp1(run_ledger: List[Dict[str, Any]], artifact_hashes: Dict[str,str], policy_bundle_hash: str) -> None:
    """Real GEN: package INF1220 TP1 learning material artifacts."""
    out_root = os.path.join(ROOT, "artifacts/inf1220/tp1")
    os.makedirs(out_root, exist_ok=True)

    inputs = [
        "cbia-content/inf1220/objectives/tp1.extracted.json",
        "cbia-content/inf1220/objectives/objectives.dag.json",
        "cbia-content/inf1220/material/tp1/theory/theory_blocks.json",
        "cbia-content/inf1220/material/tp1/drills/drill_blocks.json",
        "cbia-content/inf1220/material/tp1/flow/learning_flow.json",
        "cbia-content/inf1220/material/tp1/eval/eval_summary.json",
        "cbia-content/inf1220/material/tp1/manifest/material.manifest.json",
    ]

    entry_base = len(run_ledger) + 1
    for i, rel in enumerate(inputs):
        src = os.path.join(ROOT, rel)
        dst_rel = os.path.join("artifacts/inf1220/tp1", os.path.basename(rel))
        dst = os.path.join(ROOT, dst_rel)
        shutil.copyfile(src, dst)
        h = sha256_file(dst)
        artifact_hashes[dst_rel] = h
        run_ledger.append({
            "entry_id": f"LEDGER-{entry_base+i:04d}",
            "phase": "GEN",
            "artifact_id": os.path.basename(rel),
            "artifact_path": dst_rel,
            "hash": h,
            "objective_ids": [
                "INF1220-TP1-O-01",
                "INF1220-TP1-O-02",
                "INF1220-TP1-O-03",
                "INF1220-TP1-O-04",
                "INF1220-TP1-O-05",
            ],
            "authority_ids": ["INF1220-TP1"],
            "policy_bundle_hash": policy_bundle_hash,
            "timestamp": now_utc(),
        })

def write_ledgers(run_ledger: List[Dict[str, Any]], artifact_hashes: Dict[str,str]) -> None:
    _write_json(os.path.join(ROOT, "execution/ledger/run.ledger.json"), run_ledger)
    _write_json(os.path.join(ROOT, "execution/ledger/artifact_hashes.json"), artifact_hashes)

def main() -> None:
    pre = pre_gen()
    policy_bundle_hash = pre["policy_bundle_hash"]

    run_ledger = init_ledger(policy_bundle_hash)
    artifact_hashes: Dict[str,str] = {}
    write_ledgers(run_ledger, artifact_hashes)

    opa_gate(pre, run_ledger, artifact_hashes)

    # GEN
    gen_inf1220_tp1(run_ledger, artifact_hashes, policy_bundle_hash)

    # STRUCT/SELECT/FLOW are no-ops for this packaging run, but we record phase markers
    for phase in ["STRUCT", "SELECT", "FLOW"]:
        run_ledger.append({
            "entry_id": f"LEDGER-{len(run_ledger)+1:04d}",
            "phase": phase,
            "artifact_id": "",
            "artifact_path": "",
            "hash": "",
            "objective_ids": [],
            "authority_ids": [],
            "policy_bundle_hash": policy_bundle_hash,
            "timestamp": now_utc(),
        })

    # EVAL (re-run assurance over final ledger/hash map)
    opa_gate(pre, run_ledger, artifact_hashes)
    run_ledger.append({
        "entry_id": f"LEDGER-{len(run_ledger)+1:04d}",
        "phase": "EVAL",
        "artifact_id": "audit_bundle",
        "artifact_path": "",
        "hash": "",
        "objective_ids": [],
        "authority_ids": [],
        "policy_bundle_hash": policy_bundle_hash,
        "timestamp": now_utc(),
    })

    write_ledgers(run_ledger, artifact_hashes)
    print("Pipeline completed (INF1220 TP1 packaged)")    

if __name__ == "__main__":
    main()
