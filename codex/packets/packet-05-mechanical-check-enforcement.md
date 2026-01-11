---
packet_id: packet-05-mechanical-check-enforcement
packet_number: 5
title: Mechanical CHECK enforcement (schema + invariants)
status: planned
priority: P0
authoritative: true
date: 2026-01-10

depends_on:
  - packet-04-external-gen-executor-hook

applies_to:
  pipeline: cbia-builder
  phases:
    - check
    - repair

constraints:
  no_llm_discretion_in_check: true
  deterministic: true
  repair_must_be_diff_scoped: true
---

# Packet 5 — Mechanical CHECK enforcement

## Goal
Implement CHECK as a fully mechanical enforcement layer: validate schemas, invariants, normalization, and deterministic formatting. No GPT/LLM decision-making occurs in CHECK.

## Non-Goals
- No selection/ranking logic unless explicitly required by existing pipeline semantics.
- No silent auto-fixes without explicit normalization rules.

## Required Deliverables

### A) CHECK module
Create a deterministic CHECK implementation that:
- validates all generated artifacts against schemas (where schemas exist)
- validates invariants (hash linkage, dependency closure, required fields)
- normalizes outputs deterministically (ordering, whitespace rules where applicable)
- emits a structured report

Deliver as:
- `tools/check_pipeline.py` (or integrated into authoritative runner)
- `execution/check/report.json`
- `execution/check/report.md` (optional, human-readable summary)

### B) Normalization rules (explicit)
Document normalization rules used by CHECK:
- ordering rules (sorted keys)
- path canonicalization
- newline conventions
- stable serialization

Deliver as:
- `control/check/normalization.md` (or `execution/check/README.md`)

### C) REPAIR gate (optional, constrained)
If REPAIR is used:
- REPAIR must be constrained to explicit diffs produced by CHECK
- REPAIR must not invent new files outside an allow-list
- REPAIR must run only after a failed CHECK with a bounded diff capsule

Deliver:
- `control/repair/repair_capsule.schema.json`
- runner support to construct bounded repair capsule

### D) Tests
- invalid artifact fails CHECK with explicit report
- normalization yields byte-stable results across runs

## Acceptance Criteria
- CHECK deterministically accepts or rejects with explainable evidence.
- No LLM is invoked during CHECK.
- If REPAIR exists, it is diff-scoped and bounded.

## Suggested Issue Template
Title: `Packet 5: Mechanical CHECK enforcement`
Labels: `control`, `packet`, `P0`, `check`
Branch: `packet/mech-check-<issue#>`
PR description includes: `Closes #<issue#>`

---

## Codex Execution Prompt (minimal)

Implement this packet exactly as written in this file.

Rules:
- Treat this file as the sole execution contract.
- Do not introduce new pipeline phases unless this packet explicitly adds one (most do not).
- Do not weaken or bypass existing Control Kernel / OPA gating.
- Do not modify unrelated files.
- Deterministic behavior only (no timestamps/UUIDs/randomness/environment-dependent ordering).

Work only on the issue-linked branch/PR. If Codex cannot access the GitHub issue, commit this file into the branch at `control/packets/issue-XX-<packet_id>.md` and point Codex to that path.

