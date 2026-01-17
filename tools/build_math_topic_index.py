#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


ANCHOR_PATTERN = re.compile(r"^#+\s+(.+?)(?:\s+\{#([A-Za-z0-9._:-]+)\})?\s*$")


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n", encoding="utf-8")


def parse_anchors(doc_path: Path) -> dict[str, str]:
    anchors: dict[str, str] = {}
    for line in doc_path.read_text(encoding="utf-8").splitlines():
        match = ANCHOR_PATTERN.match(line.strip())
        if match and match.group(2):
            title = match.group(1).strip()
            anchor = match.group(2).strip()
            anchors[anchor] = title
    return anchors


def slugify(anchor: str) -> str:
    slug = re.sub(r"[^a-z0-9._:-]+", ".", anchor.lower())
    slug = re.sub(r"\.{2,}", ".", slug).strip(".")
    return slug or anchor.lower()


def keywords_from_title(title: str) -> list[str]:
    tokens = re.findall(r"[A-Za-z0-9]+", title.lower())
    return tokens or [title.lower()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Build math_topic_index.json from master math doc.")
    parser.add_argument(
        "--master-doc",
        default="control/authority/master-math-doc.md",
        help="Path to sanitized master math doc.",
    )
    parser.add_argument(
        "--seed",
        default="control/rules/math_topic_index.seed.json",
        help="Path to math topic seed JSON.",
    )
    parser.add_argument(
        "--output",
        default="control/artifacts/math_topic_index.json",
        help="Output path for math_topic_index.json.",
    )
    args = parser.parse_args()

    master_doc = Path(args.master_doc)
    seed_path = Path(args.seed)
    output_path = Path(args.output)

    anchors = parse_anchors(master_doc)
    if not anchors:
        raise SystemExit(f"No anchored headings found in {master_doc}")

    seed = load_json(seed_path)
    seed_topics = seed.get("topics", [])
    anchor_set = {anchor.lstrip("#") for anchor in anchors.keys()}

    for topic in seed_topics:
        ref_anchor = topic["source_ref"]["anchor"].lstrip("#")
        if ref_anchor not in anchor_set:
            raise SystemExit(f"Seed topic anchor missing in master doc: {ref_anchor}")

    seed_anchor_lookup = {topic["source_ref"]["anchor"].lstrip("#"): topic for topic in seed_topics}
    extra_topics = []
    for anchor, title in sorted(anchors.items()):
        if anchor in seed_anchor_lookup:
            continue
        extra_topics.append(
            {
                "math_topic_id": slugify(anchor),
                "title": title,
                "keywords": keywords_from_title(title),
                "source_ref": {"source": seed["source"], "anchor": f"#{anchor}"},
            }
        )

    output = {
        "version": seed["version"],
        "source": seed["source"],
        "topics": [*seed_topics, *extra_topics],
    }
    write_json(output_path, output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
