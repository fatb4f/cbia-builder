#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n", encoding="utf-8")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def keyword_hits(text: str, keywords: list[str]) -> int:
    hits = 0
    lowered = normalize_text(text)
    for keyword in keywords:
        if keyword.lower() in lowered:
            hits += 1
    return hits


def resolve_formal_objectives(path: Path) -> dict:
    if path.exists():
        return load_json(path)
    canonical = Path("cbia-content/inf1220/objectives/tp1.extracted.json")
    if not canonical.exists():
        raise SystemExit("formal_objectives.json missing and canonical objectives not found")
    source = load_json(canonical)
    objectives = []
    for item in source.get("objectives", []):
        evidence = item.get("evidence", [])
        authority_refs = [
            {"source": entry["path"], "anchor": entry["locator"]}
            for entry in evidence
            if "path" in entry and "locator" in entry
        ]
        if not authority_refs:
            raise SystemExit(f"Objective {item.get('objective_id')} missing authority refs")
        objectives.append(
            {
                "objective_id": item["objective_id"],
                "title": item["statement"],
                "capability": item["statement"],
                "authority_refs": authority_refs,
            }
        )
    payload = {"version": "v0.1.0", "scope_id": "inf1220-tp1", "objectives": objectives}
    write_json(path, payload)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Infer math recall map from objectives.")
    parser.add_argument(
        "--objectives",
        default="control/artifacts/formal_objectives.json",
        help="Path to formal objectives JSON.",
    )
    parser.add_argument(
        "--topic-index",
        default="control/artifacts/math_topic_index.json",
        help="Path to math topic index JSON.",
    )
    parser.add_argument(
        "--rules",
        default="control/rules/math_inference_rules.v0.1.0.json",
        help="Path to math inference rules JSON.",
    )
    parser.add_argument(
        "--output",
        default="control/artifacts/math_recall_map.json",
        help="Output path for math recall map.",
    )
    args = parser.parse_args()

    objectives_path = Path(args.objectives)
    topic_index = load_json(Path(args.topic_index))
    rules = load_json(Path(args.rules))
    objectives = resolve_formal_objectives(objectives_path)

    topic_by_id = {topic["math_topic_id"]: topic for topic in topic_index.get("topics", [])}
    mappings = []
    for objective in objectives.get("objectives", []):
        text = " ".join([objective.get("title", ""), objective.get("capability", "")])
        objective_anchors = {
            ref["anchor"].lstrip("#") for ref in objective.get("authority_refs", []) if "anchor" in ref
        }
        recalls = []
        for rule in rules.get("rules", []):
            topic = topic_by_id.get(rule["math_topic_id"])
            if not topic:
                continue
            hits = keyword_hits(text, rule.get("keywords", []))
            if hits < rule.get("min_hits", 1):
                continue
            evidence = []
            if topic["source_ref"]["anchor"].lstrip("#") in objective_anchors:
                evidence.append(
                    {
                        "kind": "pointer_anchor",
                        "ref": {
                            "source": topic["source_ref"]["source"],
                            "anchor": topic["source_ref"]["anchor"],
                        },
                    }
                )
            evidence.append(
                {
                    "kind": "lexical_match",
                    "ref": {
                        "source": topic["source_ref"]["source"],
                        "anchor": topic["source_ref"]["anchor"],
                    },
                }
            )
            has_pointer_anchor = any(entry["kind"] == "pointer_anchor" for entry in evidence)
            confidence = float(rule.get("confidence", 0.0))
            if not has_pointer_anchor and hits == rule.get("min_hits", 1):
                confidence = max(0.0, confidence - 0.1)
            recalls.append(
                {
                    "math_topic_id": rule["math_topic_id"],
                    "recall_only": True,
                    "confidence": confidence,
                    "evidence": evidence,
                }
            )
        mappings.append({"objective_id": objective["objective_id"], "math_recalls": recalls})

    output = {"version": "v0.1.0", "scope_id": objectives.get("scope_id", "unknown"), "mappings": mappings}
    write_json(Path(args.output), output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
