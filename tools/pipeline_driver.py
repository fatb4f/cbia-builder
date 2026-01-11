#!/usr/bin/env python3
"""Authoritative pipeline driver for cbia-builder."""

import datetime
import hashlib
import json
import os
import shutil
import sys
from typing import Any, Dict, List, Tuple

ROOT = os.path.dirname(os.path.dirname(__file__))

PHASE_ORDER = ["PRE_GEN", "GEN", "CHECK", "REPAIR", "PROMOTE"]
CACHE_SCHEMA_VERSION = "0.1.0"


def _read_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _write_json(path: str, obj: Any) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _sha256_json(obj: Any) -> str:
    blob = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return _sha256_bytes(blob.encode("utf-8"))


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_dir(path: str) -> str:
    items: List[Tuple[str, str]] = []
    for root, _, files in os.walk(path):
        for fn in sorted(files):
            p = os.path.join(root, fn)
            rel = os.path.relpath(p, path)
            items.append((rel, sha256_file(p)))
    blob = json.dumps(items, sort_keys=True).encode("utf-8")
    return _sha256_bytes(blob)


def now_utc() -> str:
    return datetime.datetime.utcnow().isoformat() + "Z"


def _sha256_path_if_exists(path: str) -> str:
    if os.path.exists(path) and os.path.isfile(path):
        return sha256_file(path)
    if os.path.exists(path) and os.path.isdir(path):
        return sha256_dir(path)
    return ""


def materialize_evidence(
    pre_gen_capsule: Dict[str, Any],
    run_ledger: List[Dict[str, Any]],
    artifact_hashes: Dict[str, str],
) -> Dict[str, Any]:
    dag_path = os.path.join(ROOT, "control/evidence/evidence_dag.json")
    contract_path = os.path.join(ROOT, "control/evidence/evidence.contract.json")

    if not os.path.exists(dag_path) or not os.path.exists(contract_path):
        return {"required": False, "completed": True, "dag_hash": ""}

    contract = _read_json(contract_path)
    required = bool(contract.get("requires_execution_dag", False))

    evidence_root = os.path.join(ROOT, "execution/evidence")
    os.makedirs(evidence_root, exist_ok=True)

    checks = {
        "pre_gen_capsule_present": pre_gen_capsule is not None,
        "run_ledger_nonempty": bool(run_ledger),
        "artifact_hashes_nonempty": bool(artifact_hashes),
        "opa_outputs_present": os.path.exists(os.path.join(ROOT, "opa/decision.json"))
        and os.path.exists(os.path.join(ROOT, "opa/explain.json")),
    }

    mat_ledger = {
        "phase": "EVIDENCE",
        "timestamp": now_utc(),
        "policy_bundle_hash": pre_gen_capsule.get("policy_bundle_hash"),
        "pre_gen_capsule_hash": _sha256_bytes(
            json.dumps(pre_gen_capsule, sort_keys=True).encode("utf-8")
        ),
        "opa_decision_hash": _sha256_path_if_exists(os.path.join(ROOT, "opa/decision.json")),
        "opa_explain_hash": _sha256_path_if_exists(os.path.join(ROOT, "opa/explain.json")),
        "run_ledger_hash": _sha256_bytes(
            json.dumps(run_ledger, sort_keys=True).encode("utf-8")
        ),
        "artifact_hashes_hash": _sha256_bytes(
            json.dumps(artifact_hashes, sort_keys=True).encode("utf-8")
        ),
        "evidence_dag_hash": sha256_file(dag_path),
    }

    manifest = {
        "schema_version": "0.1.0",
        "inputs": {
            "control/evidence/evidence_dag.json": mat_ledger["evidence_dag_hash"],
            "control/evidence/evidence.contract.json": sha256_file(contract_path),
            "control/runtime/pre_gen_capsule.json": mat_ledger["pre_gen_capsule_hash"],
            "opa/decision.json": mat_ledger["opa_decision_hash"],
            "opa/explain.json": mat_ledger["opa_explain_hash"],
        },
        "outputs": {
            "execution/evidence/materialization.ledger.json": _sha256_bytes(
                json.dumps(mat_ledger, sort_keys=True).encode("utf-8")
            ),
            "execution/evidence/checks.json": _sha256_bytes(
                json.dumps(checks, sort_keys=True).encode("utf-8")
            ),
        },
    }

    _write_json(os.path.join(evidence_root, "materialization.ledger.json"), mat_ledger)
    _write_json(os.path.join(evidence_root, "checks.json"), checks)
    _write_json(os.path.join(evidence_root, "bundle.manifest.json"), manifest)

    completed = all(checks.values()) if required else True
    return {"required": required, "completed": completed, "dag_hash": mat_ledger["evidence_dag_hash"]}


def promotion_state(evidence: Dict[str, Any]) -> Dict[str, Any]:
    req_path = os.path.join(ROOT, "control/runtime/promotion.request.json")
    dag_path = os.path.join(ROOT, "control/promotion/promotion_dag.json")

    required = os.path.exists(req_path) and os.path.exists(dag_path)
    if not required:
        return {"required": False, "completed": True, "dag_hash": ""}

    ci_att = os.path.join(ROOT, "execution/ci/attestation.json")
    completed = bool(evidence.get("completed")) and os.path.exists(ci_att)

    return {"required": True, "completed": completed, "dag_hash": sha256_file(dag_path)}


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
        }
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
    explain: List[str] = []

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
        ledger_hashes = {
            a["authority_id"]: a["hash"]["value"] for a in ledger.get("authority_set", [])
        }
        if capsule_hashes != ledger_hashes:
            explain.append("auth_immutable: FAIL (capsule hashes != ledger hashes)")
            return False, explain
        explain.append("auth_immutable: PASS")
    except Exception as e:
        explain.append(f"auth_immutable: ERROR ({e})")
        return False, explain

    authority_ids = {a["authority_id"] for a in input_bundle["authority_ledger"].get("authority_set", [])}
    used = set()
    for entry in input_bundle.get("run_ledger", []):
        for aid in entry.get("authority_ids", []):
            used.add(aid)
    if not used.issubset(authority_ids):
        explain.append("closed_world_authority: FAIL (used authority id not in ledger)")
        return False, explain
    explain.append("closed_world_authority: PASS")

    objectives = input_bundle.get("objectives", [])
    obj_to_auth = {o.get("id"): (o.get("source", {}) or {}).get("authority_id", "") for o in objectives}
    for entry in input_bundle.get("run_ledger", []):
        if entry.get("artifact_id"):
            for oid in entry.get("objective_ids", []):
                if not obj_to_auth.get(oid):
                    explain.append(f"dependency_closure: FAIL (objective {oid} has no authority_id)")
                    return False, explain
    explain.append("dependency_closure: PASS")

    for obj in objectives:
        if obj.get("type") == "inferred":
            if not obj.get("justification") or not obj.get("constraints"):
                explain.append(
                    f"inference_compliance: FAIL (inferred objective {obj.get('id')} missing justification/constraints)"
                )
                return False, explain
    explain.append("inference_compliance: PASS")

    phases = [entry.get("phase") for entry in input_bundle.get("run_ledger", [])]
    idx = [PHASE_ORDER.index(p) for p in phases if p in PHASE_ORDER]
    if idx != sorted(idx):
        explain.append("phase_admissibility: FAIL (phase order not monotone)")
        return False, explain
    explain.append("phase_admissibility: PASS")

    artifact_hashes = input_bundle.get("artifact_hashes", {})
    for entry in input_bundle.get("run_ledger", []):
        ap = entry.get("artifact_path", "")
        if ap:
            if artifact_hashes.get(ap) != entry.get("hash"):
                explain.append(f"artifact_integrity: FAIL (hash mismatch for {ap})")
                return False, explain
    explain.append("artifact_integrity: PASS")

    run_ledger = input_bundle.get("run_ledger", [])
    if not run_ledger:
        explain.append("deterministic_replay: FAIL (run_ledger empty)")
        return False, explain
    if input_bundle["pre_gen_capsule"].get("policy_bundle_hash") != run_ledger[0].get(
        "policy_bundle_hash"
    ):
        explain.append("deterministic_replay: FAIL (policy bundle hash mismatch)")
        return False, explain
    explain.append("deterministic_replay: PASS")

    ev = input_bundle.get("evidence", {}) or {}
    if ev.get("required"):
        if not ev.get("completed"):
            explain.append("evidence_materialized: FAIL (evidence required but not completed)")
            return False, explain
        explain.append("evidence_materialized: PASS")
    else:
        explain.append("evidence_materialized: SKIP")

    pr = input_bundle.get("promotion", {}) or {}
    if pr.get("required"):
        if not pr.get("completed"):
            explain.append("promotion_admissible: FAIL (promotion required but not completed)")
            return False, explain
        explain.append("promotion_admissible: PASS")
    else:
        explain.append("promotion_admissible: SKIP")

    return True, explain


def opa_gate(
    pre_gen_capsule: Dict[str, Any],
    run_ledger: List[Dict[str, Any]],
    artifact_hashes: Dict[str, str],
) -> None:
    input_bundle = {
        "pre_gen_capsule": pre_gen_capsule,
        "authority_ledger": _read_json(os.path.join(ROOT, "control/authority.ledger.json")),
        "objectives": _read_json(os.path.join(ROOT, "objectives.json"))
        if os.path.exists(os.path.join(ROOT, "objectives.json"))
        else [],
        "dependency_graph": _read_json(os.path.join(ROOT, "dependency.graph.json"))
        if os.path.exists(os.path.join(ROOT, "dependency.graph.json"))
        else {},
        "execution_dag": _read_json(os.path.join(ROOT, "execution_dag.json"))
        if os.path.exists(os.path.join(ROOT, "execution_dag.json"))
        else {},
        "run_ledger": run_ledger,
        "artifact_hashes": artifact_hashes,
        "evidence": {"required": False, "completed": True, "dag_hash": ""},
        "promotion": {"required": False, "completed": True, "dag_hash": ""},
    }
    _write_json(os.path.join(ROOT, "opa/input.json"), input_bundle)

    allow, explain = assurance_eval(input_bundle)

    decision = {"result": [{"expressions": [{"value": allow}]}]}
    _write_json(os.path.join(ROOT, "opa/decision.json"), decision)
    _write_json(os.path.join(ROOT, "opa/explain.json"), {"explain": explain, "allow": allow})

    evidence = materialize_evidence(pre_gen_capsule, run_ledger, artifact_hashes)
    promotion = promotion_state(evidence)

    input_bundle["evidence"] = evidence
    input_bundle["promotion"] = promotion
    _write_json(os.path.join(ROOT, "opa/input.json"), input_bundle)

    bundle_hash = _sha256_json(input_bundle)
    memo_root = os.path.join(ROOT, "opa/memo", bundle_hash)
    memo_decision = os.path.join(memo_root, "decision.json")
    memo_explain = os.path.join(memo_root, "explain.json")

    if os.path.exists(memo_decision) and os.path.exists(memo_explain):
        shutil.copyfile(memo_decision, os.path.join(ROOT, "opa/decision.json"))
        shutil.copyfile(memo_explain, os.path.join(ROOT, "opa/explain.json"))
        decision2 = _read_json(os.path.join(ROOT, "opa/decision.json"))
        allow2 = (
            decision2.get("result", [{}])[0]
            .get("expressions", [{}])[0]
            .get("value", False)
        )
    else:
        allow2, explain2 = assurance_eval(input_bundle)

        decision2 = {"result": [{"expressions": [{"value": allow2}]}]}
        _write_json(os.path.join(ROOT, "opa/decision.json"), decision2)
        _write_json(os.path.join(ROOT, "opa/explain.json"), {"explain": explain2, "allow": allow2})

        os.makedirs(memo_root, exist_ok=True)
        shutil.copyfile(os.path.join(ROOT, "opa/decision.json"), memo_decision)
        shutil.copyfile(os.path.join(ROOT, "opa/explain.json"), memo_explain)

    _write_json(
        os.path.join(ROOT, "opa/bundle.hash"),
        {
            "opa_input_bundle_hash": bundle_hash,
            "policy_bundle_hash": pre_gen_capsule["policy_bundle_hash"],
        },
    )

    if not allow2:
        sys.exit("OPA gate denied")


def write_ledgers(run_ledger: List[Dict[str, Any]], artifact_hashes: Dict[str, str]) -> None:
    _write_json(os.path.join(ROOT, "execution/ledger/run.ledger.json"), run_ledger)
    _write_json(os.path.join(ROOT, "execution/ledger/artifact_hashes.json"), artifact_hashes)


def _inputs_manifest_hash(root: str = ROOT) -> str:
    candidate = os.path.join(root, "execution/ledger/inputs.manifest.json")
    return sha256_file(candidate) if os.path.exists(candidate) else ""


def _phase_inputs(pre_gen_capsule: Dict[str, Any], root: str = ROOT) -> Dict[str, str]:
    return {
        "authority_ledger": sha256_file(os.path.join(root, "control/authority.ledger.json")),
        "policy_bundle": pre_gen_capsule.get("policy_bundle_hash", ""),
        "pre_gen_capsule": _sha256_path_if_exists(
            os.path.join(root, "control/runtime/pre_gen_capsule.json")
        ),
        "inputs_manifest": _inputs_manifest_hash(root),
    }


def _phase_outputs() -> Dict[str, str]:
    return {
        "opa_decision": _sha256_path_if_exists(os.path.join(ROOT, "opa/decision.json")),
        "opa_explain": _sha256_path_if_exists(os.path.join(ROOT, "opa/explain.json")),
        "opa_bundle_hash": _sha256_path_if_exists(os.path.join(ROOT, "opa/bundle.hash")),
    }


def _canonical_json(payload: Any) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode(
        "utf-8"
    )


def _runner_version_hash() -> str:
    components = {
        "tools/pipeline_driver.py": sha256_file(os.path.join(ROOT, "tools/pipeline_driver.py")),
        "tools/run_pipeline.py": sha256_file(os.path.join(ROOT, "tools/run_pipeline.py")),
    }
    return _sha256_bytes(_canonical_json(components))


def _next_ledger_entry_id(run_ledger: List[Dict[str, Any]]) -> str:
    return f"LEDGER-{len(run_ledger) + 1:04d}"


def _gen_outputs_path(root: str = ROOT) -> str:
    return os.path.join(root, "execution/gen/outputs.json")


def _gen_phase(pre_gen_capsule: Dict[str, Any], root: str = ROOT) -> List[str]:
    payload = {
        "schema_version": "0.1.0",
        "phase": "GEN",
        "input_hashes": _phase_inputs(pre_gen_capsule, root),
    }
    output_path = _gen_outputs_path(root)
    _write_json(output_path, payload)
    return [output_path]


class CacheManager:
    def __init__(self, root: str = ROOT) -> None:
        self.root = root
        self.cache_root = os.path.join(root, "execution/cache")

    def tool_versions(self) -> Dict[str, str]:
        return {
            "runner_version": _runner_version_hash(),
            "generator_version": "unimplemented",
        }

    def cache_key_data(self, phase: str, pre_gen_capsule: Dict[str, Any]) -> Dict[str, Any]:
        inputs_manifest = _inputs_manifest_hash(self.root)
        return {
            "schema_version": CACHE_SCHEMA_VERSION,
            "phase": phase,
            "authority_ledger_hash": sha256_file(
                os.path.join(self.root, "control/authority.ledger.json")
            ),
            "policy_bundle_hash": pre_gen_capsule.get("policy_bundle_hash", ""),
            "pre_gen_capsule_hash": _sha256_path_if_exists(
                os.path.join(self.root, "control/runtime/pre_gen_capsule.json")
            ),
            "inputs_manifest_hash": inputs_manifest,
            "tool_versions": self.tool_versions(),
        }

    def cache_key(self, key_data: Dict[str, Any]) -> str:
        return _sha256_bytes(_canonical_json(key_data))

    def cache_dir(self, cache_key: str) -> str:
        return os.path.join(self.cache_root, cache_key)

    def cache_meta_path(self, cache_key: str) -> str:
        return os.path.join(self.cache_dir(cache_key), "cache.meta.json")

    def has_cache(self, cache_key: str) -> bool:
        return os.path.exists(self.cache_meta_path(cache_key))

    def store(
        self,
        cache_key: str,
        key_data: Dict[str, Any],
        phase_artifacts: List[str],
    ) -> Dict[str, Any]:
        cache_dir = self.cache_dir(cache_key)
        artifacts: List[Dict[str, Any]] = []
        phase_relpaths: List[str] = []
        for path in phase_artifacts:
            rel = os.path.relpath(path, self.root)
            dest = os.path.join(cache_dir, rel)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(path, "rb") as src, open(dest, "wb") as dst:
                data = src.read()
                dst.write(data)
            artifacts.append(
                {
                    "path": rel,
                    "hash": _sha256_bytes(data),
                    "bytes": len(data),
                }
            )
            phase_relpaths.append(rel)

        opa_paths = [
            os.path.join(self.root, "opa/decision.json"),
            os.path.join(self.root, "opa/explain.json"),
            os.path.join(self.root, "opa/bundle.hash"),
        ]
        for path in opa_paths:
            if not os.path.exists(path):
                continue
            rel = os.path.relpath(path, self.root)
            dest = os.path.join(cache_dir, rel)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(path, "rb") as src, open(dest, "wb") as dst:
                data = src.read()
                dst.write(data)
            artifacts.append(
                {
                    "path": rel,
                    "hash": _sha256_bytes(data),
                    "bytes": len(data),
                }
            )

        meta = {
            "schema_version": CACHE_SCHEMA_VERSION,
            "cache_key": cache_key,
            "phase": key_data.get("phase"),
            "key_data": key_data,
            "artifacts": artifacts,
            "phase_artifacts": phase_relpaths,
        }
        _write_json(self.cache_meta_path(cache_key), meta)
        return meta

    def replay(self, cache_key: str) -> List[str]:
        meta = _read_json(self.cache_meta_path(cache_key))
        artifacts = meta.get("artifacts", [])
        phase_relpaths = set(meta.get("phase_artifacts", []))
        replayed: List[str] = []
        for artifact in artifacts:
            rel = artifact.get("path", "")
            if not rel:
                continue
            src = os.path.join(self.cache_dir(cache_key), rel)
            dest = os.path.join(self.root, rel)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(src, "rb") as src_f, open(dest, "wb") as dst_f:
                data = src_f.read()
                dst_f.write(data)
            if rel in phase_relpaths:
                replayed.append(dest)
        return replayed


def write_manifest(entries: List[Dict[str, Any]]) -> str:
    manifest_path = os.path.join(ROOT, "execution/ledger/run.manifest.json")
    _write_json(manifest_path, {"phases": entries})
    return manifest_path


class PipelineDriver:
    def __init__(self, root: str = ROOT) -> None:
        self.root = root

    def run(self, dry_run: bool = False) -> int:
        print("Planned phase order: " + " -> ".join(PHASE_ORDER))

        pre_gen_capsule = pre_gen()
        run_ledger = init_ledger(pre_gen_capsule["policy_bundle_hash"])
        artifact_hashes: Dict[str, str] = {}
        write_ledgers(run_ledger, artifact_hashes)

        manifest_entries: List[Dict[str, Any]] = []

        try:
            opa_gate(pre_gen_capsule, run_ledger, artifact_hashes)
            manifest_entries.append(
                {
                    "phase": "PRE_GEN",
                    "input_hashes": _phase_inputs(pre_gen_capsule, self.root),
                    "output_hashes": _phase_outputs(),
                    "status": "executed",
                    "reason": "",
                }
            )
        except SystemExit as exc:
            manifest_entries.append(
                {
                    "phase": "PRE_GEN",
                    "input_hashes": _phase_inputs(pre_gen_capsule, self.root),
                    "output_hashes": _phase_outputs(),
                    "status": "executed",
                    "reason": f"failed: {exc}",
                }
            )
            manifest_path = write_manifest(manifest_entries)
            manifest_hash = sha256_file(manifest_path)
            print(f"Run manifest: {manifest_path} (sha256={manifest_hash})")
            raise

        if dry_run:
            for phase in ["GEN", "CHECK", "REPAIR", "PROMOTE"]:
                manifest_entries.append(
                    {
                        "phase": phase,
                        "input_hashes": _phase_inputs(pre_gen_capsule, self.root),
                        "output_hashes": {},
                        "status": "skipped",
                        "reason": "dry-run",
                    }
                )
            manifest_path = write_manifest(manifest_entries)
            manifest_hash = sha256_file(manifest_path)
            print(f"Run manifest: {manifest_path} (sha256={manifest_hash})")
            write_ledgers(run_ledger, artifact_hashes)
            return 0

        cache_manager = CacheManager(self.root)
        cache_key_data = cache_manager.cache_key_data("GEN", pre_gen_capsule)
        cache_key = cache_manager.cache_key(cache_key_data)
        cache_hit = cache_manager.has_cache(cache_key)
        if cache_hit:
            phase_outputs = cache_manager.replay(cache_key)
            cache_reason = "cache-hit"
        else:
            phase_outputs = _gen_phase(pre_gen_capsule, self.root)
            cache_manager.store(cache_key, cache_key_data, phase_outputs)
            cache_reason = "cache-miss"

        output_hashes: Dict[str, str] = {}
        for path in phase_outputs:
            rel = os.path.relpath(path, self.root)
            output_hashes[rel] = sha256_file(path)
            artifact_hashes[rel] = output_hashes[rel]

        gen_entry = {
            "entry_id": _next_ledger_entry_id(run_ledger),
            "phase": "GEN",
            "artifact_id": "GEN-OUTPUTS",
            "artifact_path": os.path.relpath(phase_outputs[0], self.root) if phase_outputs else "",
            "hash": output_hashes.get(
                os.path.relpath(phase_outputs[0], self.root), ""
            )
            if phase_outputs
            else "",
            "objective_ids": [],
            "authority_ids": [],
            "policy_bundle_hash": pre_gen_capsule["policy_bundle_hash"],
            "timestamp": now_utc(),
            "cache": {"hit": cache_hit, "cache_key": cache_key},
        }
        run_ledger.append(gen_entry)

        manifest_entries.append(
            {
                "phase": "GEN",
                "input_hashes": _phase_inputs(pre_gen_capsule, self.root),
                "output_hashes": output_hashes,
                "status": "executed" if not cache_hit else "replayed",
                "reason": cache_reason,
            }
        )
        manifest_entries.append(
            {
                "phase": "CHECK",
                "input_hashes": _phase_inputs(pre_gen_capsule, self.root),
                "output_hashes": {},
                "status": "skipped",
                "reason": "not implemented",
            }
        )
        manifest_entries.append(
            {
                "phase": "REPAIR",
                "input_hashes": _phase_inputs(pre_gen_capsule, self.root),
                "output_hashes": {},
                "status": "skipped",
                "reason": "not implemented",
            }
        )
        manifest_entries.append(
            {
                "phase": "PROMOTE",
                "input_hashes": _phase_inputs(pre_gen_capsule, self.root),
                "output_hashes": {},
                "status": "skipped",
                "reason": "not implemented",
            }
        )
        manifest_path = write_manifest(manifest_entries)
        manifest_hash = sha256_file(manifest_path)
        print(f"Run manifest: {manifest_path} (sha256={manifest_hash})")
        write_ledgers(run_ledger, artifact_hashes)
        return 0


def main(argv: List[str] | None = None) -> int:
    args = argv or sys.argv[1:]
    dry_run = "--dry-run" in args
    driver = PipelineDriver()
    return driver.run(dry_run=dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
