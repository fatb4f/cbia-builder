#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path


def run_step(label: str, args: list[str]) -> None:
    result = subprocess.run(args, check=False)
    if result.returncode != 0:
        raise RuntimeError(f"Step failed: {label}")


def main() -> int:
    python = sys.executable
    try:
        run_step(
            "build_math_topic_index",
            [python, "tools/build_math_topic_index.py"],
        )
        run_step(
            "infer_math_recalls",
            [python, "tools/infer_math_recalls.py"],
        )
        run_step(
            "build_pointer_map",
            [python, "tools/build_pointer_map.py"],
        )
        run_step(
            "build_objective_dependency_dag",
            [python, "tools/build_objective_dependency_dag.py"],
        )

        scope_id = "inf1220-tp1"
        formal_objectives = Path("control/artifacts/formal_objectives.json")
        if formal_objectives.exists():
            payload = json.loads(formal_objectives.read_text(encoding="utf-8"))
            scope_id = payload.get("scope_id", scope_id)

        run_step(
            "build_execution_dag",
            [python, "tools/build_execution_dag.py", "--scope-id", scope_id],
        )
        run_step(
            "build_validation_report",
            [python, "tools/build_validation_report.py"],
        )
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
