from __future__ import annotations

import argparse
import json
from pathlib import Path
from datetime import date

VALID_STAGES = {"constraints", "syllabus", "schemas", "material"}

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True, help="Project root")
    ap.add_argument("--stage", required=True, help="constraints|syllabus|schemas|material")
    ap.add_argument("--note", default="", help="Optional note to append")
    args = ap.parse_args()

    stage = args.stage
    if stage not in VALID_STAGES:
        print(f"invalid stage: {stage}")
        return 2

    root = Path(args.project)
    mf = root / "manifests" / "stage.json"
    if not mf.exists():
        print(f"missing: {mf}")
        return 2

    data = json.loads(mf.read_text(encoding="utf-8"))
    data["stage"] = stage
    data.setdefault("provenance", {})
    data["provenance"]["generated_on"] = date.today().isoformat()
    if args.note:
        prev = data.get("notes", "")
        data["notes"] = (prev + "\n" if prev else "") + args.note

    mf.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"updated: {mf}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
