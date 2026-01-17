#!/usr/bin/env python3
import argparse
import hashlib
import json
import sys
from pathlib import Path

from jsonschema import Draft7Validator


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def sha256_for_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_json(path: Path, schema_path: Path) -> list[str]:
    schema = load_json(schema_path)
    data = load_json(path)
    validator = Draft7Validator(schema)
    return [error.message for error in validator.iter_errors(data)]


def main() -> int:
    parser = argparse.ArgumentParser(description="Build validation_report.json.")
    parser.add_argument(
        "--output",
        default="control/artifacts/validation_report.json",
        help="Output path for validation report.",
    )
    args = parser.parse_args()

    artifact_schema_map = {
        "control/artifacts/formal_objectives.json": "control/schemas/formal_objectives.schema.json",
        "control/artifacts/pointer_map.json": "control/schemas/pointer_map.schema.json",
        "control/artifacts/math_topic_index.json": "control/schemas/math_topic_index.schema.json",
        "control/artifacts/math_recall_map.json": "control/schemas/math_recall_map.schema.json",
        "control/artifacts/objective_dependency_dag.json": "control/schemas/objective_dependency_dag.schema.json",
        "control/artifacts/execution_dag.json": "control/schemas/execution_dag.schema.json",
    }

    artifacts = []
    has_failure = False
    for artifact_path_str, schema_path_str in artifact_schema_map.items():
        artifact_path = Path(artifact_path_str)
        schema_path = Path(schema_path_str)
        errors = []
        if not artifact_path.exists():
            errors.append("missing artifact")
        else:
            errors.extend(validate_json(artifact_path, schema_path))
        valid = len(errors) == 0
        if not valid:
            has_failure = True
        artifacts.append(
            {
                "path": artifact_path_str,
                "sha256": sha256_for_path(artifact_path) if artifact_path.exists() else "",
                "schema": schema_path_str,
                "valid": valid,
                "errors": errors,
            }
        )

    report = {"version": "v0.1.0", "artifacts": artifacts}
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2, sort_keys=False) + "\n", encoding="utf-8")

    report_schema = Path("control/schemas/validation_report.schema.json")
    report_errors = validate_json(output_path, report_schema)
    if report_errors:
        for error in report_errors:
            print(f"validation_report.json: {error}", file=sys.stderr)
        has_failure = True

    return 1 if has_failure else 0


if __name__ == "__main__":
    raise SystemExit(main())
