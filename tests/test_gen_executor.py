from __future__ import annotations

import json
import os
import shutil
import sys
from pathlib import Path

import jsonschema
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import tools.pipeline_driver as pipeline_driver
from tools.pipeline_driver import _gen_phase


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
    return capsule


def _copy_schema(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    schema_src = repo_root / "control" / "executors" / "gen_executor.schema.json"
    (tmp_path / "control" / "executors").mkdir(parents=True, exist_ok=True)
    shutil.copy(schema_src, tmp_path / "control" / "executors" / "gen_executor.schema.json")


def _write_executor_script(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")


def test_gen_phase_default_executor(tmp_path: Path) -> None:
    capsule = _setup_root(tmp_path)
    _copy_schema(tmp_path)

    phase_outputs = _gen_phase(capsule, str(tmp_path))

    output_path = tmp_path / "execution" / "gen" / "outputs.json"
    assert phase_outputs == [str(output_path)]
    payload = json.loads(output_path.read_text(encoding="utf-8"))
    assert payload["phase"] == "GEN"
    assert payload["schema_version"] == "0.1.0"


def test_schema_validation_rejects_invalid_config(tmp_path: Path) -> None:
    capsule = _setup_root(tmp_path)
    _copy_schema(tmp_path)

    invalid = {"kind": "external"}
    _write_json(tmp_path / "control" / "runtime" / "gen_executor.json", invalid)

    with pytest.raises(jsonschema.ValidationError):
        _gen_phase(capsule, str(tmp_path))


def test_external_executor_invoked_writes_output(tmp_path: Path) -> None:
    capsule = _setup_root(tmp_path)
    _copy_schema(tmp_path)

    script = tmp_path / "tools" / "executors" / "fake_exec.py"
    _write_executor_script(
        script,
        """
import json
import sys

with open(sys.argv[1], "r", encoding="utf-8") as f:
    bundle = json.load(f)
outputs = bundle["phase_config"]["outputs"]
outputs_manifest = outputs["outputs_manifest"]
report_path = outputs["execution_report"]

payload = {"schema_version": "0.1.0", "phase": "GEN", "input_hashes": {}}
with open(outputs_manifest, "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2, sort_keys=True)

report = {
    "schema_version": "0.1.0",
    "phase": "GEN",
    "artifacts": [
        {"path": outputs_manifest, "hash": "hash", "bytes": 1}
    ],
    "tool_versions": {"executor": "fake"},
}
with open(report_path, "w", encoding="utf-8") as f:
    json.dump(report, f, indent=2, sort_keys=True)
""",
    )

    config = {
        "kind": "external",
        "version": "test-1",
        "command": [sys.executable, str(script)],
        "phase_config": {
            "phase": "GEN",
            "outputs": {
                "outputs_manifest": "execution/gen/outputs.json",
                "execution_report": "execution/gen/executor.report.json",
            },
        },
    }
    _write_json(tmp_path / "control" / "runtime" / "gen_executor.json", config)

    phase_outputs = _gen_phase(capsule, str(tmp_path))

    outputs_manifest = tmp_path / "execution" / "gen" / "outputs.json"
    report_path = tmp_path / "execution" / "gen" / "executor.report.json"

    assert outputs_manifest.exists()
    assert report_path.exists()
    assert outputs_manifest in [Path(p) for p in phase_outputs]
    assert report_path in [Path(p) for p in phase_outputs]

    report = json.loads(report_path.read_text(encoding="utf-8"))
    artifacts = {artifact["path"] for artifact in report["artifacts"]}
    assert "execution/gen/outputs.json" in artifacts


def test_external_executor_nonzero_exit_blocks_and_captures_logs(tmp_path: Path) -> None:
    capsule = _setup_root(tmp_path)
    _copy_schema(tmp_path)

    script = tmp_path / "tools" / "executors" / "fail_exec.py"
    _write_executor_script(
        script,
        """
import sys
sys.stderr.write("boom")
sys.exit(2)
""",
    )

    config = {
        "kind": "external",
        "version": "test-2",
        "command": [sys.executable, str(script)],
    }
    _write_json(tmp_path / "control" / "runtime" / "gen_executor.json", config)

    with pytest.raises(RuntimeError) as excinfo:
        _gen_phase(capsule, str(tmp_path))

    assert "boom" in str(excinfo.value)


def test_executor_version_recorded_in_capsule(tmp_path: Path, monkeypatch) -> None:
    _setup_root(tmp_path)
    _copy_schema(tmp_path)

    config = {
        "kind": "external",
        "version": "capsule-1",
        "command": [sys.executable, "-c", "print('ok')"],
    }
    _write_json(tmp_path / "control" / "runtime" / "gen_executor.json", config)

    monkeypatch.setattr(pipeline_driver, "ROOT", str(tmp_path))

    capsule = pipeline_driver.pre_gen()

    assert capsule["gen_executor"]["version"] == "capsule-1"
    assert capsule["gen_executor"]["kind"] == "external"
