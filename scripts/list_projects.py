from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def iter_stage_manifests(root: Path):
    for p in root.rglob("manifests/stage.json"):
        yield p

def main() -> int:
    rows = []
    for mf in iter_stage_manifests(ROOT):
        try:
            data = json.loads(mf.read_text(encoding="utf-8"))
            rows.append((data.get("project", str(mf.parent.parent)), data.get("stage", "?"), str(mf)))
        except Exception:
            rows.append((str(mf.parent.parent), "?", str(mf)))

    rows.sort(key=lambda x: x[0])
    if not rows:
        print("no projects found")
        return 1

    w0 = max(len(r[0]) for r in rows)
    w1 = max(len(r[1]) for r in rows)
    for proj, stage, path in rows:
        print(f"{proj.ljust(w0)}  {stage.ljust(w1)}  {path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
