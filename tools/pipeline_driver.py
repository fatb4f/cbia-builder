#!/usr/bin/env python3
"""Authoritative pipeline driver for cbia-builder."""

import datetime
import hashlib
import json
import os
import shutil
import subprocess
import sys
from typing import Any, Dict, List, Tuple

import jsonschema

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


def _output_path(relpath: str, output_root: str | None) -> str:
    if output_root:
        return os.path.join(output_root, relpath)
    return os.path.join(ROOT, relpath)


def _pre_gen_capsule_path(output_root: str | None) -> str:
    if output_root:
        return os.path.join(output_root, "pre_gen_capsule.json")
    return os.path.join(ROOT, "control/runtime/pre_gen_capsule.json")


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


def _stable_capsule_hash(path: str) -> str:
    if not os.path.exists(path):
        return ""
    payload = _read_json(path)
    payload.pop("timestamp", None)
    return _sha256_bytes(_canonical_json(payload))


def materialize_evidence(
    pre_gen_capsule: Dict[str, Any],
    run_ledger: List[Dict[str, Any]],
    artifact_hashes: Dict[str, str],
    output_root: str | None = None,
) -> Dict[str, Any]:
    dag_path = os.path.join(ROOT, "control/evidence/evidence_dag.json")
    contract_path = os.path.join(ROOT, "control/evidence/evidence.contract.json")

    if not os.path.exists(dag_path) or not os.path.exists(contract_path):
        return {"required": False, "completed": True, "dag_hash": ""}

    contract = _read_json(contract_path)
    required = bool(contract.get("requires_execution_dag", False))

    evidence_root = _output_path("execution/evidence", output_root)
    os.makedirs(evidence_root, exist_ok=True)

    opa_decision_path = _output_path("opa/decision.json", output_root)
    opa_explain_path = _output_path("opa/explain.json", output_root)
    pre_gen_capsule_path = _pre_gen_capsule_path(output_root)

    checks = {
        "pre_gen_capsule_present": pre_gen_capsule is not None,
        "run_ledger_nonempty": bool(run_ledger),
        "artifact_hashes_nonempty": bool(artifact_hashes),
        "opa_outputs_present": os.path.exists(opa_decision_path)
        and os.path.exists(opa_explain_path),
    }

    mat_ledger = {
        "phase": "EVIDENCE",
        "timestamp": now_utc(),
        "policy_bundle_hash": pre_gen_capsule.get("policy_bundle_hash"),
        "pre_gen_capsule_hash": _sha256_bytes(
            json.dumps(pre_gen_capsule, sort_keys=True).encode("utf-8")
        ),
        "opa_decision_hash": _sha256_path_if_exists(opa_decision_path),
        "opa_explain_hash": _sha256_path_if_exists(opa_explain_path),
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
            os.path.relpath(pre_gen_capsule_path, output_root or ROOT): mat_ledger[
                "pre_gen_capsule_hash"
            ],
            os.path.relpath(opa_decision_path, output_root or ROOT): mat_ledger[
                "opa_decision_hash"
            ],
            os.path.relpath(opa_explain_path, output_root or ROOT): mat_ledger[
                "opa_explain_hash"
            ],
        },
        "outputs": {
            os.path.relpath(
                os.path.join(evidence_root, "materialization.ledger.json"),
                output_root or ROOT,
            ): _sha256_bytes(
                json.dumps(mat_ledger, sort_keys=True).encode("utf-8")
            ),
            os.path.relpath(
                os.path.join(evidence_root, "checks.json"), output_root or ROOT
            ): _sha256_bytes(
                json.dumps(checks, sort_keys=True).encode("utf-8")
            ),
        },
    }

    _write_json(os.path.join(evidence_root, "materialization.ledger.json"), mat_ledger)
    _write_json(os.path.join(evidence_root, "checks.json"), checks)
    _write_json(os.path.join(evidence_root, "bundle.manifest.json"), manifest)

    completed = all(checks.values()) if required else True
    return {"required": required, "completed": completed, "dag_hash": mat_ledger["evidence_dag_hash"]}


def promotion_state(evidence: Dict[str, Any], output_root: str | None = None) -> Dict[str, Any]:
    req_path = os.path.join(ROOT, "control/runtime/promotion.request.json")
    dag_path = os.path.join(ROOT, "control/promotion/promotion_dag.json")

    required = os.path.exists(req_path) and os.path.exists(dag_path)
    if not required:
        return {"required": False, "completed": True, "dag_hash": ""}

    ci_att = _output_path("execution/ci/attestation.json", output_root)
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


def pre_gen(output_root: str | None = None) -> Dict[str, Any]:
    auth = _read_json(os.path.join(ROOT, "control/authority.ledger.json"))
    hashes = {a["authority_id"]: a["hash"]["value"] for a in auth["authority_set"]}
    policy_bundle_hash = sha256_dir(os.path.join(ROOT, "policy"))
    gen_executor = _gen_executor_identity(ROOT)
    capsule = {
        "schema_version": "0.1.0",
        "kernel_decision": "ALLOW" if auth.get("frozen") else "DENY",
        "control_state_hash": _sha256_bytes(json.dumps(hashes, sort_keys=True).encode("utf-8")),
        "policy_bundle_hash": policy_bundle_hash,
        "authority_set_hashes": hashes,
        "gen_executor": gen_executor,
        "timestamp": now_utc(),
    }
    _write_json(_pre_gen_capsule_path(output_root), capsule)
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
    output_root: str | None = None,
) -> None:
    evidence = {"required": False, "completed": True, "dag_hash": ""}
    promotion = {"required": False, "completed": True, "dag_hash": ""}
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
        "evidence": evidence,
        "promotion": promotion,
        "gates": {
            "evidence_materialized": evidence.get("completed") is True,
            "promotion_admissible": promotion.get("completed") is True,
        },
    }
    _write_json(_output_path("opa/input.json", output_root), input_bundle)

    allow, explain = assurance_eval(input_bundle)

    decision = {"result": [{"expressions": [{"value": allow}]}]}
    _write_json(_output_path("opa/decision.json", output_root), decision)
    _write_json(
        _output_path("opa/explain.json", output_root),
        {"explain": explain, "allow": allow},
    )

    evidence = materialize_evidence(
        pre_gen_capsule, run_ledger, artifact_hashes, output_root=output_root
    )
    promotion = promotion_state(evidence, output_root=output_root)

    input_bundle["evidence"] = evidence
    input_bundle["promotion"] = promotion
    input_bundle["gates"] = {
        "evidence_materialized": evidence.get("completed") is True,
        "promotion_admissible": promotion.get("completed") is True,
    }
    _write_json(_output_path("opa/input.json", output_root), input_bundle)

    bundle_hash = _sha256_json(input_bundle)
    memo_root = _output_path(os.path.join("opa/memo", bundle_hash), output_root)
    memo_decision = os.path.join(memo_root, "decision.json")
    memo_explain = os.path.join(memo_root, "explain.json")

    if os.path.exists(memo_decision) and os.path.exists(memo_explain):
        shutil.copyfile(memo_decision, _output_path("opa/decision.json", output_root))
        shutil.copyfile(memo_explain, _output_path("opa/explain.json", output_root))
        decision2 = _read_json(_output_path("opa/decision.json", output_root))
        allow2 = (
            decision2.get("result", [{}])[0]
            .get("expressions", [{}])[0]
            .get("value", False)
        )
    else:
        allow2, explain2 = assurance_eval(input_bundle)

        decision2 = {"result": [{"expressions": [{"value": allow2}]}]}
        _write_json(_output_path("opa/decision.json", output_root), decision2)
        _write_json(
            _output_path("opa/explain.json", output_root),
            {"explain": explain2, "allow": allow2},
        )

        os.makedirs(memo_root, exist_ok=True)
        shutil.copyfile(_output_path("opa/decision.json", output_root), memo_decision)
        shutil.copyfile(_output_path("opa/explain.json", output_root), memo_explain)

    _write_json(
        _output_path("opa/bundle.hash", output_root),
        {
            "opa_input_bundle_hash": bundle_hash,
            "policy_bundle_hash": pre_gen_capsule["policy_bundle_hash"],
        },
    )

    if not allow2:
        sys.exit("OPA gate denied")


def write_ledgers(
    run_ledger: List[Dict[str, Any]],
    artifact_hashes: Dict[str, str],
    output_root: str | None = None,
) -> None:
    _write_json(_output_path("execution/ledger/run.ledger.json", output_root), run_ledger)
    _write_json(
        _output_path("execution/ledger/artifact_hashes.json", output_root),
        artifact_hashes,
    )


def _inputs_manifest_hash(root: str = ROOT) -> str:
    candidate = os.path.join(root, "execution/ledger/inputs.manifest.json")
    return sha256_file(candidate) if os.path.exists(candidate) else ""


def _phase_inputs(
    pre_gen_capsule: Dict[str, Any],
    root: str = ROOT,
    output_root: str | None = None,
) -> Dict[str, str]:
    return {
        "authority_ledger": sha256_file(os.path.join(root, "control/authority.ledger.json")),
        "policy_bundle": pre_gen_capsule.get("policy_bundle_hash", ""),
        "pre_gen_capsule": _sha256_path_if_exists(_pre_gen_capsule_path(output_root)),
        "inputs_manifest": _inputs_manifest_hash(root),
    }


def _phase_outputs(output_root: str | None = None) -> Dict[str, str]:
    return {
        "opa_decision": _sha256_path_if_exists(_output_path("opa/decision.json", output_root)),
        "opa_explain": _sha256_path_if_exists(_output_path("opa/explain.json", output_root)),
        "opa_bundle_hash": _sha256_path_if_exists(_output_path("opa/bundle.hash", output_root)),
    }


def _canonical_json(payload: Any) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode(
        "utf-8"
    )


def _load_gen_executor_schema(root: str = ROOT) -> Dict[str, Any]:
    return _read_json(os.path.join(root, "control/executors/gen_executor.schema.json"))


def _validate_gen_executor(instance: Dict[str, Any], def_name: str, schema: Dict[str, Any]) -> None:
    validator_schema = {
        "$schema": schema.get("$schema", "https://json-schema.org/draft/2020-12/schema"),
        "$ref": f"#/$defs/{def_name}",
        "$defs": schema.get("$defs", {}),
    }
    jsonschema.validate(instance=instance, schema=validator_schema)


def _load_gen_executor_config(root: str = ROOT) -> Dict[str, Any] | None:
    env_path = os.environ.get("CBIA_GEN_EXECUTOR_CONFIG")
    if env_path:
        return _read_json(env_path)
    config_path = os.path.join(root, "control/runtime/gen_executor.json")
    if os.path.exists(config_path):
        return _read_json(config_path)
    return None


def _default_gen_phase_config() -> Dict[str, Any]:
    return {
        "phase": "GEN",
        "outputs": {
            "outputs_manifest": "execution/gen/outputs.json",
            "execution_report": "execution/gen/executor.report.json",
        },
    }


def _default_gen_executor_config() -> Dict[str, Any]:
    return {"kind": "local", "version": "builtin", "phase_config": _default_gen_phase_config()}


def _resolved_gen_executor_config(root: str = ROOT) -> Tuple[Dict[str, Any], bool]:
    config = _load_gen_executor_config(root)
    explicit = config is not None
    resolved = config if config is not None else _default_gen_executor_config()
    schema = _load_gen_executor_schema(root)
    _validate_gen_executor(resolved, "config", schema)
    if "phase_config" not in resolved:
        resolved["phase_config"] = _default_gen_phase_config()
    return resolved, explicit


def _gen_executor_phase_config(config: Dict[str, Any]) -> Dict[str, Any]:
    phase_config = _default_gen_phase_config()
    override = config.get("phase_config") if isinstance(config, dict) else None
    if isinstance(override, dict):
        phase_config.update({k: v for k, v in override.items() if k != "outputs"})
        outputs = dict(phase_config.get("outputs", {}))
        outputs.update(override.get("outputs", {}))
        phase_config["outputs"] = outputs
    return phase_config


def _gen_executor_identity(root: str = ROOT) -> Dict[str, Any]:
    config, explicit = _resolved_gen_executor_config(root)
    schema_path = os.path.join(root, "control/executors/gen_executor.schema.json")
    config_hash = _sha256_bytes(_canonical_json(config))
    return {
        "kind": config["kind"],
        "version": config["version"],
        "explicit": explicit,
        "config_hash": config_hash,
        "schema_hash": sha256_file(schema_path) if os.path.exists(schema_path) else "",
    }


def _gen_executor_version(root: str = ROOT) -> str:
    return _sha256_bytes(_canonical_json(_gen_executor_identity(root)))


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
    executor_config, explicit = _resolved_gen_executor_config(root)
    if explicit:
        if executor_config["kind"] == "local" and "command" not in executor_config:
            explicit = False

    if explicit:
        schema = _load_gen_executor_schema(root)
        phase_config = _gen_executor_phase_config(executor_config)
        phase_config["executor_id"] = executor_config.get("executor_id", "external")
        inputs_manifest_path = os.path.join(root, "execution/ledger/inputs.manifest.json")
        inputs_manifest = (
            _read_json(inputs_manifest_path) if os.path.exists(inputs_manifest_path) else {}
        )
        request = {
            "schema_version": "0.1.0",
            "pre_gen_capsule": pre_gen_capsule,
            "inputs_manifest": inputs_manifest,
            "phase_config": phase_config,
        }
        _validate_gen_executor(request, "request", schema)
        input_path = os.path.join(root, "execution/gen/executor.input.json")
        _write_json(input_path, request)
        command = executor_config.get("command")
        if not isinstance(command, list) or not command:
            raise ValueError("GEN executor config must include a non-empty command list")
        timeout_s = executor_config.get("timeout_s")
        env_override = executor_config.get("env")
        env = os.environ.copy()
        if isinstance(env_override, dict):
            env.update({str(k): str(v) for k, v in env_override.items()})
        completed = subprocess.run(
            [*command, input_path],
            check=False,
            cwd=root,
            env=env,
            capture_output=True,
            text=True,
            timeout=timeout_s,
        )
        if completed.returncode != 0:
            stdout = completed.stdout.strip()
            stderr = completed.stderr.strip()
            raise RuntimeError(
                "GEN executor failed "
                f"(exit={completed.returncode}) stdout={stdout!r} stderr={stderr!r}"
            )

        report_path = os.path.join(root, phase_config["outputs"]["execution_report"])
        if not os.path.exists(report_path):
            raise FileNotFoundError(
                f"GEN executor report missing: {phase_config['outputs']['execution_report']}"
            )
        report = _read_json(report_path)
        _validate_gen_executor(report, "report", schema)

        outputs: List[str] = []
        for artifact in report.get("artifacts", []):
            relpath = artifact.get("path", "")
            if not relpath:
                continue
            abs_path = os.path.join(root, relpath)
            if not os.path.exists(abs_path):
                raise FileNotFoundError(f"GEN executor artifact missing: {relpath}")
            outputs.append(abs_path)
        outputs.append(report_path)
        return outputs

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
            "generator_version": _gen_executor_version(self.root),
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
            "pre_gen_capsule_hash": _stable_capsule_hash(
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


def write_manifest(entries: List[Dict[str, Any]], output_root: str | None = None) -> str:
    manifest_path = _output_path("execution/ledger/run.manifest.json", output_root)
    _write_json(manifest_path, {"phases": entries})
    return manifest_path


class PipelineDriver:
    def __init__(self, root: str = ROOT) -> None:
        self.root = root

    def run(self, dry_run: bool = False, out_dir: str | None = None) -> int:
        print("Planned phase order: " + " -> ".join(PHASE_ORDER))

        output_root = out_dir if dry_run else None

        pre_gen_capsule = pre_gen(output_root=output_root)
        run_ledger = init_ledger(pre_gen_capsule["policy_bundle_hash"])
        artifact_hashes: Dict[str, str] = {}
        write_ledgers(run_ledger, artifact_hashes, output_root=output_root)

        manifest_entries: List[Dict[str, Any]] = []

        try:
            opa_gate(pre_gen_capsule, run_ledger, artifact_hashes, output_root=output_root)
            manifest_entries.append(
                {
                    "phase": "PRE_GEN",
                    "input_hashes": _phase_inputs(
                        pre_gen_capsule, self.root, output_root=output_root
                    ),
                    "output_hashes": _phase_outputs(output_root=output_root),
                    "status": "executed",
                    "reason": "",
                }
            )
        except SystemExit as exc:
            manifest_entries.append(
                {
                    "phase": "PRE_GEN",
                    "input_hashes": _phase_inputs(
                        pre_gen_capsule, self.root, output_root=output_root
                    ),
                    "output_hashes": _phase_outputs(output_root=output_root),
                    "status": "executed",
                    "reason": f"failed: {exc}",
                }
            )
            manifest_path = write_manifest(manifest_entries, output_root=output_root)
            manifest_hash = sha256_file(manifest_path)
            print(f"Run manifest: {manifest_path} (sha256={manifest_hash})")
            raise

        if dry_run:
            for phase in ["GEN", "CHECK", "REPAIR", "PROMOTE"]:
                manifest_entries.append(
                    {
                        "phase": phase,
                        "input_hashes": _phase_inputs(
                            pre_gen_capsule, self.root, output_root=output_root
                        ),
                        "output_hashes": {},
                        "status": "skipped",
                        "reason": "dry-run",
                    }
                )
            manifest_path = write_manifest(manifest_entries, output_root=output_root)
            manifest_hash = sha256_file(manifest_path)
            print(f"Run manifest: {manifest_path} (sha256={manifest_hash})")
            write_ledgers(run_ledger, artifact_hashes, output_root=output_root)
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
