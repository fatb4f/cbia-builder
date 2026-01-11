from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import tools.pipeline_driver as pipeline_driver
from tools.pipeline_driver import CacheManager, PipelineDriver, _gen_phase


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, sort_keys=True), encoding="utf-8")


def _copy_schema(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    schema_src = repo_root / "control" / "executors" / "gen_executor.schema.json"
    (tmp_path / "control" / "executors").mkdir(parents=True, exist_ok=True)
    schema_dst = tmp_path / "control" / "executors" / "gen_executor.schema.json"
    schema_dst.write_text(schema_src.read_text(encoding="utf-8"), encoding="utf-8")


def _copy_runner_files(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    tools_root = tmp_path / "tools"
    tools_root.mkdir(parents=True, exist_ok=True)
    (tools_root / "pipeline_driver.py").write_text(
        (repo_root / "tools" / "pipeline_driver.py").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    (tools_root / "run_pipeline.py").write_text(
        (repo_root / "tools" / "run_pipeline.py").read_text(encoding="utf-8"),
        encoding="utf-8",
    )


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
    _copy_schema(tmp_path)
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
    _copy_schema(tmp_path)
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


def test_cache_key_includes_executor_version(tmp_path: Path) -> None:
    capsule = _setup_root(tmp_path)
    _copy_schema(tmp_path)
    cache_manager = CacheManager(str(tmp_path))

    _write_json(
        tmp_path / "control" / "runtime" / "gen_executor.json",
        {"kind": "external", "version": "v1", "command": ["/bin/true"]},
    )
    key_v1 = cache_manager.cache_key(cache_manager.cache_key_data("GEN", capsule))

    _write_json(
        tmp_path / "control" / "runtime" / "gen_executor.json",
        {"kind": "external", "version": "v2", "command": ["/bin/true"]},
    )
    key_v2 = cache_manager.cache_key(cache_manager.cache_key_data("GEN", capsule))

    assert key_v1 != key_v2


def test_cache_replay_skips_external_invocation(tmp_path: Path, monkeypatch) -> None:
    _copy_schema(tmp_path)
    _copy_runner_files(tmp_path)
    _setup_root(tmp_path)

    _write_json(
        tmp_path / "control" / "runtime" / "gen_executor.json",
        {"kind": "external", "version": "v1", "command": ["/bin/true"]},
    )

    monkeypatch.setattr(pipeline_driver, "ROOT", str(tmp_path))

    cache_manager = CacheManager(str(tmp_path))
    capsule = pipeline_driver.pre_gen()

    outputs_path = tmp_path / "execution" / "gen" / "outputs.json"
    _write_json(outputs_path, {"schema_version": "0.1.0", "phase": "GEN", "input_hashes": {}})

    key_data = cache_manager.cache_key_data("GEN", capsule)
    cache_key = cache_manager.cache_key(key_data)
    cache_manager.store(cache_key, key_data, [str(outputs_path)])

    monkeypatch.setattr(pipeline_driver, "_gen_phase", lambda *_args, **_kwargs: pytest.fail("invoked"))

    driver = PipelineDriver(str(tmp_path))
    assert driver.run(dry_run=False, out_dir=None) == 0
