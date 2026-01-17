#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build pointer_map.json from formal objectives.")
    parser.add_argument(
        "--objectives",
        default="control/artifacts/formal_objectives.json",
        help="Path to formal objectives JSON.",
    )
    parser.add_argument(
        "--output",
        default="control/artifacts/pointer_map.json",
        help="Output path for pointer map JSON.",
    )
    args = parser.parse_args()

    objectives = load_json(Path(args.objectives))
    mappings = []
    for objective in objectives.get("objectives", []):
        pointer_refs = [
            {"source": ref["source"], "anchor": ref["anchor"], "role": "clarify"}
            for ref in objective.get("authority_refs", [])
        ]
        if not pointer_refs:
            raise SystemExit(f"Objective {objective.get('objective_id')} missing authority refs")
        mappings.append({"objective_id": objective["objective_id"], "pointer_refs": pointer_refs})

    output = {
        "version": objectives.get("version", "v0.1.0"),
        "scope_id": objectives.get("scope_id", "unknown"),
        "mappings": mappings,
    }
    write_json(Path(args.output), output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
