from __future__ import annotations

import argparse
from pathlib import Path

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True, help="Project root, e.g. cbia-content/mqt1001")
    args = ap.parse_args()

    root = Path(args.project)
    material = root / "material"
    index = material / "index.md"
    mf = root / "manifests" / "stage.json"

    if not root.exists():
        print(f"missing project: {root}")
        return 2
    if not material.exists():
        print(f"missing: {material}")
        return 2
    if not mf.exists():
        print(f"missing: {mf}")
        return 2

    if index.exists():
        print("ok: material/index.md present")
    else:
        print("missing: material/index.md")
        return 2

    md = list(material.rglob("*.md"))
    if len(md) <= 1:
        print("note: only index.md present (OK for early stage)")
    else:
        print(f"ok: {len(md)} markdown files present")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
