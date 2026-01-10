# CBIA Build Ledger (v0.2 skeleton)

This repo is a **single-source, auditable build ledger** for CBIA generation.

It hosts two flavors:
- `cbia-contentless/` — ramps driven by **constraints**
- `cbia-content/` — course instances driven by **syllabus**

All stages are committed:
- `constraints/` or `syllabus/` (inputs)
- `schemas/` (generated)
- `material/` (generated)
- `manifests/stage.json` (provenance)

Tooling is kept under `tooling/` and `scripts/` (no global schemas/material at repo root).

Date: 2026-01-04
