#!/usr/bin/env python3
import argparse
import hashlib
import json
import sys
from pathlib import Path


def sha256_for_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="Compute sha256 hashes for files.")
    parser.add_argument("paths", nargs="+", help="File paths to hash.")
    parser.add_argument("--output", help="Optional output path for JSON results.")
    args = parser.parse_args()

    results = []
    for path_str in args.paths:
        path = Path(path_str)
        if not path.exists():
            print(f"Missing file: {path}", file=sys.stderr)
            return 1
        results.append({"path": str(path), "sha256": sha256_for_path(path)})

    output = json.dumps(results, indent=2, sort_keys=True)
    if args.output:
        Path(args.output).write_text(output + "\n", encoding="utf-8")
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
