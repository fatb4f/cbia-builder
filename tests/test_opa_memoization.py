import json
import os
import sys
from typing import Any, Dict, List

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import tools.pipeline_driver as pipeline_driver


def _write_json(path: str, obj: Any) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def _read_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _authority_ledger() -> Dict[str, Any]:
    return {
        "frozen": True,
        "authority_set": [
            {
                "authority_id": "AUTH-1",
                "hash": {"value": "hash-1"},
                "source": {"locator": "file://authority"},
            }
        ],
    }


def _pre_gen_capsule() -> Dict[str, Any]:
    return {
        "schema_version": "0.1.0",
        "kernel_decision": "ALLOW",
        "control_state_hash": "control-hash",
        "policy_bundle_hash": "policy-hash",
        "authority_set_hashes": {"AUTH-1": "hash-1"},
        "timestamp": "2026-01-10T00:00:00Z",
    }


def _run_ledger(policy_bundle_hash: str) -> List[Dict[str, Any]]:
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
            "timestamp": "2026-01-10T00:00:00Z",
        }
    ]


def test_opa_memoization_hit(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(pipeline_driver, "ROOT", str(tmp_path))

    _write_json(tmp_path / "control/authority.ledger.json", _authority_ledger())

    pre_gen_capsule = _pre_gen_capsule()
    run_ledger = _run_ledger(pre_gen_capsule["policy_bundle_hash"])
    artifact_hashes: Dict[str, str] = {}

    pipeline_driver.opa_gate(pre_gen_capsule, run_ledger, artifact_hashes)

    bundle_hash = _read_json(tmp_path / "opa/bundle.hash")["opa_input_bundle_hash"]
    memo_root = tmp_path / "opa/memo" / bundle_hash

    assert (memo_root / "decision.json").exists()
    assert (memo_root / "explain.json").exists()

    memo_decision = {"result": [{"expressions": [{"value": True}]}]}
    memo_explain = {"explain": ["memo-hit"], "allow": True}
    _write_json(memo_root / "decision.json", memo_decision)
    _write_json(memo_root / "explain.json", memo_explain)

    pipeline_driver.opa_gate(pre_gen_capsule, run_ledger, artifact_hashes)

    decision = _read_json(tmp_path / "opa/decision.json")
    explain = _read_json(tmp_path / "opa/explain.json")

    assert decision == memo_decision
    assert explain == memo_explain
