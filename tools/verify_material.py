#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    manifest_path = root / "content" / "manifest.json"
    if not manifest_path.exists():
        print(f"missing: {manifest_path}")
        return 1

    manifest = json.loads(manifest_path.read_text())
    material_root = manifest.get("material_root")
    if not material_root:
        print("missing: manifest.material_root")
        return 1

    material_path = root / material_root
    if not material_path.exists():
        print(f"missing: {material_path}")
        return 1

    print("green")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
