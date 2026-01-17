import json
import subprocess
import sys
from pathlib import Path

import pytest
from jsonschema import Draft7Validator


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate(schema_path: Path, json_path: Path) -> list[str]:
    schema = load_json(schema_path)
    data = load_json(json_path)
    validator = Draft7Validator(schema)
    return [error.message for error in validator.iter_errors(data)]


@pytest.fixture(scope="session", autouse=True)
def run_preflight_once():
    subprocess.run([sys.executable, "tools/run_content_gen_refactor_preflight.py"], check=True)


def test_example_dags_validate():
    examples = [
        (
            Path("control/examples/objective_dependency_dag.example.json"),
            Path("control/schemas/objective_dependency_dag.schema.json"),
        ),
        (
            Path("control/examples/execution_dag.example.json"),
            Path("control/schemas/execution_dag.schema.json"),
        ),
    ]
    for example_path, schema_path in examples:
        errors = validate(schema_path, example_path)
        assert not errors, f"{example_path} failed validation: {errors}"


def test_preflight_outputs_validate():
    artifact_schema_map = {
        "control/artifacts/formal_objectives.json": "control/schemas/formal_objectives.schema.json",
        "control/artifacts/pointer_map.json": "control/schemas/pointer_map.schema.json",
        "control/artifacts/math_topic_index.json": "control/schemas/math_topic_index.schema.json",
        "control/artifacts/math_recall_map.json": "control/schemas/math_recall_map.schema.json",
        "control/artifacts/objective_dependency_dag.json": "control/schemas/objective_dependency_dag.schema.json",
        "control/artifacts/execution_dag.json": "control/schemas/execution_dag.schema.json",
        "control/artifacts/validation_report.json": "control/schemas/validation_report.schema.json",
    }
    for artifact_path, schema_path in artifact_schema_map.items():
        errors = validate(Path(schema_path), Path(artifact_path))
        assert not errors, f"{artifact_path} failed validation: {errors}"


def test_math_recall_inference_evidence():
    recall_map = load_json(Path("control/artifacts/math_recall_map.json"))
    has_recall = False
    for mapping in recall_map.get("mappings", []):
        for recall in mapping.get("math_recalls", []):
            has_recall = True
            assert recall.get("recall_only") is True
            evidence = recall.get("evidence", [])
            assert evidence, "math recall missing evidence"
    assert has_recall, "math recall inference produced no recalls"
