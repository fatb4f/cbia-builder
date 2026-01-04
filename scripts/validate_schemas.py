from __future__ import annotations

import argparse
from pathlib import Path

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True, help="Project root, e.g. cbia-content/mqt1001")
    args = ap.parse_args()

    root = Path(args.project)
    if not root.exists():
        print(f"missing project: {root}")
        return 2

    schemas = root / "schemas"
    mf = root / "manifests" / "stage.json"

    if not schemas.exists():
        print(f"missing: {schemas}")
        return 2
    if not mf.exists():
        print(f"missing: {mf}")
        return 2

    # Minimal: ensure schemas dir has something beyond README when generated
    files = [p for p in schemas.rglob("*") if p.is_file() and p.name != "README.md"]
    if not files:
        print("note: schemas contains no generated files yet (OK for early stage)")
    else:
        print(f"ok: schemas contains {len(files)} file(s)")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
