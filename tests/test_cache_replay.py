from __future__ import annotations

import json
from pathlib import Path

from tools.pipeline_driver import CacheManager, _gen_phase


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, sort_keys=True), encoding="utf-8")


def _setup_root(tmp_path: Path) -> dict:
    authority = {
        "frozen": True,
        "authority_set": [
            {"authority_id": "AUTH-1", "hash": {"value": "abc"}, "source": {"locator": "x"}}
        ],
    }
    _write_json(tmp_path / "control" / "authority.ledger.json", authority)
    (tmp_path / "policy").mkdir(parents=True, exist_ok=True)
    (tmp_path / "policy" / "assurance.rego").write_text("package assurance", encoding="utf-8")
    _write_json(tmp_path / "execution" / "ledger" / "inputs.manifest.json", {"inputs": []})
    capsule = {
        "schema_version": "0.1.0",
        "kernel_decision": "ALLOW",
        "control_state_hash": "state",
        "policy_bundle_hash": "policyhash",
        "authority_set_hashes": {"AUTH-1": "abc"},
    }
    _write_json(tmp_path / "control" / "runtime" / "pre_gen_capsule.json", capsule)
    (tmp_path / "opa").mkdir(parents=True, exist_ok=True)
    (tmp_path / "opa" / "decision.json").write_text("{}", encoding="utf-8")
    (tmp_path / "opa" / "explain.json").write_text("{}", encoding="utf-8")
    (tmp_path / "opa" / "bundle.hash").write_text("{}", encoding="utf-8")
    return capsule


def test_cache_hit_replays_identical_outputs(tmp_path: Path) -> None:
    capsule = _setup_root(tmp_path)
    cache_manager = CacheManager(str(tmp_path))

    phase_outputs = _gen_phase(capsule, str(tmp_path))
    key_data = cache_manager.cache_key_data("GEN", capsule)
    cache_key = cache_manager.cache_key(key_data)
    cache_manager.store(cache_key, key_data, phase_outputs)

    output_path = Path(phase_outputs[0])
    original_bytes = output_path.read_bytes()
    output_path.unlink()

    assert cache_manager.has_cache(cache_key)
    replayed = cache_manager.replay(cache_key)
    assert replayed == [str(output_path)]
    assert output_path.read_bytes() == original_bytes


def test_cache_key_changes_on_authority_policy_or_capsule(tmp_path: Path) -> None:
    capsule = _setup_root(tmp_path)
    cache_manager = CacheManager(str(tmp_path))

    key_data = cache_manager.cache_key_data("GEN", capsule)
    base_key = cache_manager.cache_key(key_data)

    authority_path = tmp_path / "control" / "authority.ledger.json"
    authority_payload = json.loads(authority_path.read_text(encoding="utf-8"))
    authority_payload["authority_set"].append(
        {"authority_id": "AUTH-2", "hash": {"value": "def"}, "source": {"locator": "y"}}
    )
    _write_json(authority_path, authority_payload)
    key_after_authority = cache_manager.cache_key(cache_manager.cache_key_data("GEN", capsule))
    assert base_key != key_after_authority

    policy_path = tmp_path / "policy" / "assurance.rego"
    policy_path.write_text("package assurance\n# change", encoding="utf-8")
    key_after_policy = cache_manager.cache_key(cache_manager.cache_key_data("GEN", capsule))
    assert base_key != key_after_policy

    capsule_path = tmp_path / "control" / "runtime" / "pre_gen_capsule.json"
    capsule_payload = json.loads(capsule_path.read_text(encoding="utf-8"))
    capsule_payload["policy_bundle_hash"] = "policyhash2"
    _write_json(capsule_path, capsule_payload)
    key_after_capsule = cache_manager.cache_key(cache_manager.cache_key_data("GEN", capsule))
    assert base_key != key_after_capsule
