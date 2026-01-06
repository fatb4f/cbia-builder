# INF1250 M2 — Schema Pack

This archive contains JSON Schemas + minimal examples for generating **Module 2** theory and drill blocks
aligned to **TP2**.

## Files
- `schemas/theory-block.schema.json`
- `schemas/drill-block.schema.json`
- `examples/theory.inf1250-m2-t1.sample.json`
- `examples/drill.inf1250-m2-da.sample.json`

## Conventions
- `id` patterns:
  - Theory: `inf1250-m{n}-t{k}` (e.g., `inf1250-m2-t1`)
  - Drill:  `inf1250-m{n}-d{a|b|c|d}` (e.g., `inf1250-m2-da`)
- `body` target: **200–300 words** (schema enforces character bounds as a proxy).
- `items[*].answer_key` is **optional** to support self-check packs.

## Versioning
- Schema versioning lives in `meta.version` inside content blocks.
- Recommended starting value: `0.1.0`

Generated: 2026-01-06
