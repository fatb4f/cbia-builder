#!/usr/bin/env python3
"""Deterministic generator for control maps."""

import hashlib
import json
import os
import sys
from typing import Any, Dict, List, Tuple

ROOT = os.path.dirname(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(ROOT, "tools"))
import pipeline_driver  # noqa: E402


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _hash_tree(root: str, exclude_prefixes: Tuple[str, ...] = ()) -> str:
    items: List[Tuple[str, str]] = []
    for base, dirs, files in os.walk(root):
        dirs.sort()
        files.sort()
        for filename in files:
            path = os.path.join(base, filename)
            rel = os.path.relpath(path, ROOT)
            if any(rel.startswith(prefix) for prefix in exclude_prefixes):
                continue
            with open(path, "rb") as handle:
                digest = _sha256_bytes(handle.read())
            items.append((rel, digest))
    blob = json.dumps(items, sort_keys=True).encode("utf-8")
    return _sha256_bytes(blob)


def _write_text(path: str, content: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)


def _write_json(path: str, payload: Any) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False, sort_keys=True)


def _control_inputs_hash() -> str:
    return _hash_tree(
        os.path.join(ROOT, "control"),
        exclude_prefixes=("control/plant/", "control/runtime/"),
    )


def _policy_assurance_hash() -> str:
    return _hash_tree(os.path.join(ROOT, "policy", "assurance"))


def _artifact_paths() -> List[str]:
    return [
        "control/authority.ledger.json",
        "control/runtime/pre_gen_capsule.json",
        "control/plant/plant.mmd",
        "control/plant/execution_dag.json",
        "execution/ledger/run.ledger.json",
        "execution/ledger/artifact_hashes.json",
        "execution/ledger/run.manifest.json",
        "opa/decision.json",
        "opa/explain.json",
        "opa/bundle.hash",
    ]


def render_plant() -> str:
    lines = [
        "flowchart TD",
        "  PRE_GEN[\"Control Kernel (PRE-GEN)\"]",
        "  OPA_DECISION[\"OPA decision\"]",
        "  GEN[\"GEN\"]",
        "  SCHEMA_VALIDATION[\"schema validation\"]",
        "  HASH_RECORDING[\"hash recording\"]",
        "  CHECK[\"CHECK\"]",
        "  REPAIR[\"REPAIR (optional)\"]",
        "  PROMOTE[\"PROMOTE\"]",
        "  PROMOTION_ALLOW[\"promotion allow/deny\"]",
        "  PRE_GEN -->|kernel_decision == ALLOW| OPA_DECISION",
        "  OPA_DECISION -->|allow == true| GEN",
        "  GEN -->|artifacts_emitted| SCHEMA_VALIDATION",
        "  SCHEMA_VALIDATION -->|schemas_valid| HASH_RECORDING",
        "  HASH_RECORDING -->|hashes_recorded| CHECK",
        "  CHECK -->|checks_pass| PROMOTE",
        "  CHECK -->|checks_fail| REPAIR",
        "  REPAIR -->|repairs_applied| CHECK",
        "  PROMOTE -->|promotion_request_present| PROMOTION_ALLOW",
    ]
    return "\n".join(lines) + "\n"


def build_execution_dag() -> Dict[str, Any]:
    artifact_paths = _artifact_paths()
    artifact_hash = _sha256_bytes(
        json.dumps(artifact_paths, sort_keys=True).encode("utf-8")
    )
    phase_order = ",".join(pipeline_driver.PHASE_ORDER)

    nodes = [
        {
            "gates": ["OPA_DECISION"],
            "id": "PRE_GEN",
            "inputs": [
                "control/authority.ledger.json",
                "policy/assurance",
            ],
            "invariants": [
                "authority_ledger.frozen == true",
                "kernel_decision == ALLOW",
            ],
            "outputs": ["control/runtime/pre_gen_capsule.json"],
            "type": "phase",
        },
        {
            "gates": [],
            "id": "OPA_DECISION",
            "inputs": [
                "control/runtime/pre_gen_capsule.json",
                "control/authority.ledger.json",
                "objectives.json",
                "dependency.graph.json",
                "execution_dag.json",
                "execution/ledger/run.ledger.json",
                "execution/ledger/artifact_hashes.json",
            ],
            "invariants": ["data.assurance.allow == true"],
            "outputs": ["opa/decision.json", "opa/explain.json", "opa/bundle.hash"],
            "type": "gate",
        },
        {
            "gates": ["SCHEMA_VALIDATION", "HASH_RECORDING"],
            "id": "GEN",
            "inputs": ["control/runtime/pre_gen_capsule.json"],
            "invariants": ["opa.allow == true"],
            "outputs": [
                "execution/ledger/run.ledger.json",
                "execution/ledger/artifact_hashes.json",
            ],
            "type": "phase",
        },
        {
            "gates": [],
            "id": "SCHEMA_VALIDATION",
            "inputs": [
                "execution/ledger/run.ledger.json",
                "execution/ledger/artifact_hashes.json",
            ],
            "invariants": ["schemas_valid == true"],
            "outputs": [],
            "type": "gate",
        },
        {
            "gates": [],
            "id": "HASH_RECORDING",
            "inputs": [
                "execution/ledger/run.ledger.json",
                "execution/ledger/artifact_hashes.json",
            ],
            "invariants": ["hashes_recorded == true"],
            "outputs": [],
            "type": "gate",
        },
        {
            "gates": [],
            "id": "CHECK",
            "inputs": [
                "execution/ledger/run.ledger.json",
                "execution/ledger/artifact_hashes.json",
            ],
            "invariants": ["checks_complete == true"],
            "outputs": ["execution/ledger/run.manifest.json"],
            "type": "phase",
        },
        {
            "gates": [],
            "id": "REPAIR",
            "inputs": [
                "execution/ledger/run.ledger.json",
                "execution/ledger/artifact_hashes.json",
            ],
            "invariants": ["repairs_applied == true"],
            "outputs": [],
            "type": "phase",
        },
        {
            "gates": ["PROMOTION_ALLOW"],
            "id": "PROMOTE",
            "inputs": [
                "execution/ledger/run.manifest.json",
                "execution/ledger/run.ledger.json",
            ],
            "invariants": ["promotion_requested == true"],
            "outputs": ["execution/ci/attestation.json"],
            "type": "phase",
        },
        {
            "gates": [],
            "id": "PROMOTION_ALLOW",
            "inputs": [
                "control/runtime/promotion.request.json",
                "execution/ci/attestation.json",
            ],
            "invariants": ["promotion_allowed == true"],
            "outputs": [],
            "type": "gate",
        },
    ]

    edges = [
        {"condition": "kernel_decision == ALLOW", "from": "PRE_GEN", "to": "OPA_DECISION"},
        {"condition": "allow == true", "from": "OPA_DECISION", "to": "GEN"},
        {"condition": "artifacts_emitted", "from": "GEN", "to": "SCHEMA_VALIDATION"},
        {"condition": "schemas_valid", "from": "SCHEMA_VALIDATION", "to": "HASH_RECORDING"},
        {"condition": "hashes_recorded", "from": "HASH_RECORDING", "to": "CHECK"},
        {"condition": "checks_pass", "from": "CHECK", "to": "PROMOTE"},
        {"condition": "checks_fail", "from": "CHECK", "to": "REPAIR"},
        {"condition": "repairs_applied", "from": "REPAIR", "to": "CHECK"},
        {"condition": "promotion_request_present", "from": "PROMOTE", "to": "PROMOTION_ALLOW"},
    ]

    artifacts = [
        {"hash_required": True, "path": path, "role": "control_map"}
        if path.startswith("control/plant/")
        else {"hash_required": True, "path": path, "role": "artifact"}
        for path in artifact_paths
    ]

    return {
        "artifacts": artifacts,
        "determinism": [
            "utf-8",
            "indent=2",
            "sorted_nodes",
            "sorted_edges",
            f"phase_order:{phase_order}",
            f"control_inputs_hash:{_control_inputs_hash()}",
            f"policy_assurance_hash:{_policy_assurance_hash()}",
            f"artifact_paths_hash:{artifact_hash}",
        ],
        "edges": edges,
        "nodes": nodes,
        "opa_inputs": [
            "control/runtime/pre_gen_capsule.json",
            "control/authority.ledger.json",
            "objectives.json",
            "dependency.graph.json",
            "execution_dag.json",
            "execution/ledger/run.ledger.json",
            "execution/ledger/artifact_hashes.json",
            "execution/evidence/materialization.ledger.json",
            "execution/evidence/checks.json",
            "execution/ci/attestation.json",
        ],
        "opa_outputs": [
            "opa/decision.json",
            "opa/explain.json",
            "opa/bundle.hash",
        ],
        "version": "1.0",
    }


def main() -> int:
    plant_path = os.path.join(ROOT, "control", "plant", "plant.mmd")
    dag_path = os.path.join(ROOT, "control", "plant", "execution_dag.json")

    _write_text(plant_path, render_plant())
    _write_json(dag_path, build_execution_dag())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
