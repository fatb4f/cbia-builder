#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build execution_dag.json.")
    parser.add_argument(
        "--scope-id",
        default="inf1220-tp1",
        help="Scope identifier for execution DAG.",
    )
    parser.add_argument(
        "--output",
        default="control/artifacts/execution_dag.json",
        help="Output path for execution DAG JSON.",
    )
    args = parser.parse_args()

    nodes = [
        {"node_id": "STOP.MISSING_OBJECTIVES", "kind": "stop_terminal"},
        {"node_id": "STOP.MISSING_POINTER_MAP", "kind": "stop_terminal"},
        {"node_id": "STOP.MISSING_MATH_RECALL", "kind": "stop_terminal"},
        {
            "node_id": "build.pointer_map",
            "kind": "build_step",
            "produces": ["control/artifacts/pointer_map.json"],
            "requires": ["control/artifacts/formal_objectives.json"],
        },
        {
            "node_id": "build.math_topic_index",
            "kind": "build_step",
            "produces": ["control/artifacts/math_topic_index.json"],
            "requires": ["control/authority/master-math-doc.md"],
        },
        {
            "node_id": "build.math_recall_map",
            "kind": "build_step",
            "produces": ["control/artifacts/math_recall_map.json"],
            "requires": [
                "control/artifacts/formal_objectives.json",
                "control/artifacts/math_topic_index.json",
                "control/rules/math_inference_rules.v0.1.0.json",
            ],
        },
        {
            "node_id": "build.objective_dependency_dag",
            "kind": "build_step",
            "produces": ["control/artifacts/objective_dependency_dag.json"],
            "requires": ["control/artifacts/formal_objectives.json"],
        },
        {
            "node_id": "build.execution_dag",
            "kind": "build_step",
            "produces": ["control/artifacts/execution_dag.json"],
            "requires": [
                "control/artifacts/objective_dependency_dag.json",
                "control/artifacts/pointer_map.json",
                "control/artifacts/math_recall_map.json",
            ],
        },
        {
            "node_id": "build.notebooks",
            "kind": "build_step",
            "requires": [
                "control/artifacts/pointer_map.json",
                "control/artifacts/math_topic_index.json",
                "control/artifacts/math_recall_map.json",
            ],
        },
        {
            "node_id": "build.drills",
            "kind": "build_step",
            "requires": [
                "control/artifacts/pointer_map.json",
                "control/artifacts/math_topic_index.json",
                "control/artifacts/math_recall_map.json",
            ],
        },
    ]

    edges = [
        {"from": "build.pointer_map", "to": "build.execution_dag"},
        {"from": "build.math_topic_index", "to": "build.math_recall_map"},
        {"from": "build.math_recall_map", "to": "build.execution_dag"},
        {"from": "build.objective_dependency_dag", "to": "build.execution_dag"},
        {"from": "build.pointer_map", "to": "build.notebooks"},
        {"from": "build.math_topic_index", "to": "build.notebooks"},
        {"from": "build.math_recall_map", "to": "build.notebooks"},
        {"from": "build.pointer_map", "to": "build.drills"},
        {"from": "build.math_topic_index", "to": "build.drills"},
        {"from": "build.math_recall_map", "to": "build.drills"},
    ]

    output = {
        "version": "v0.1.0",
        "scope_id": args.scope_id,
        "nodes": nodes,
        "edges": edges,
    }
    write_json(Path(args.output), output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
