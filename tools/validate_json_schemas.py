#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft7Validator


def load_json(path: Path):
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        raise SystemExit(f"Missing JSON file: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}")


def validate_pair(json_path: Path, schema_path: Path) -> list[str]:
    schema = load_json(schema_path)
    data = load_json(json_path)
    validator = Draft7Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    return [f"{json_path}: {error.message}" for error in errors]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate JSON files against schemas.")
    parser.add_argument(
        "--pair",
        dest="pairs",
        action="append",
        nargs=2,
        metavar=("JSON", "SCHEMA"),
        help="JSON file and schema file to validate.",
    )
    args = parser.parse_args()

    if not args.pairs:
        parser.error("At least one --pair JSON SCHEMA is required.")

    all_errors: list[str] = []
    for json_path_str, schema_path_str in args.pairs:
        json_path = Path(json_path_str)
        schema_path = Path(schema_path_str)
        all_errors.extend(validate_pair(json_path, schema_path))

    if all_errors:
        for error in all_errors:
            print(error, file=sys.stderr)
        return 1

    print("All JSON files validated successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
