# agents.md — CBIA build ledger contract (v0.2)

GPT owns generation. Humans operate the merge/review loop via **archives**.

## Project structure

Each project lives at:
- `cbia-contentless/<ramp-id>/`
- `cbia-content/<course-id>/`

Each project has:
- `constraints/` *(contentless input)* OR `syllabus/` *(course input)*
- `schemas/` *(generated)*
- `material/` *(generated)*
- `manifests/stage.json` *(provenance + stage status)*

## Stages (one archive per stage)

### Stage A — Constraints / Syllabus (input)
Allowed paths:
- `**/constraints/**` or `**/syllabus/**`
- `**/manifests/stage.json`
Acceptance:
- input index exists (`README.md` or `index.md`)

### Stage B — Schemas (generated)
Allowed paths:
- `**/schemas/**`
- `**/manifests/stage.json`
Acceptance:
- schemas are self-contained and indexed
- optional `.build-hash` present in `schemas/`

### Stage C — Material (generated)
Allowed paths:
- `**/material/**`
- `**/manifests/stage.json`
Acceptance:
- `material/index.md` exists
- optional `.build-hash` present in `material/`

## Local checks (repo-native)

- `scripts/list_projects.py` — list projects + stage
- `scripts/validate_schemas.py --project <path>` — validate schemas folder structure
- `scripts/check_material.py --project <path>` — check material structure
- `scripts/update_stage.py --project <path> --stage <constraints|syllabus|schemas|material>` — update manifest

## Packaging into workbench template

Workbench consumes only:
- `<project>/material/`
- `<project>/manifests/stage.json` (copied to `content/manifest.json`)

Date: 2026-01-04
