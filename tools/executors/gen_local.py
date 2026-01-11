#!/usr/bin/env python3
"""Reference GEN executor (local, deterministic)."""

import json
import os
import sys
from typing import Any, Dict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

sys.path.insert(0, ROOT)

from tools import pipeline_driver


def _read_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _write_json(path: str, obj: Any) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def _artifact_record(path: str) -> Dict[str, Any]:
    data = open(path, "rb").read()
    return {
        "path": os.path.relpath(path, os.getcwd()),
        "hash": pipeline_driver.sha256_file(path),
        "bytes": len(data),
    }


def main(argv: list[str] | None = None) -> int:
    args = argv or sys.argv[1:]
    if not args:
        raise SystemExit("usage: gen_local.py <executor_input.json>")

    bundle = _read_json(args[0])
    phase_config = bundle["phase_config"]
    outputs = phase_config["outputs"]
    outputs_manifest = os.path.join(os.getcwd(), outputs["outputs_manifest"])
    report_path = os.path.join(os.getcwd(), outputs["execution_report"])

    payload = {
        "schema_version": "0.1.0",
        "phase": "GEN",
        "input_hashes": pipeline_driver._phase_inputs(
            bundle["pre_gen_capsule"], os.getcwd()
        ),
    }
    _write_json(outputs_manifest, payload)

    report = {
        "schema_version": "0.1.0",
        "phase": "GEN",
        "artifacts": [
            _artifact_record(outputs_manifest),
        ],
        "tool_versions": {"executor": "gen_local@0.1.0"},
    }
    _write_json(report_path, report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
