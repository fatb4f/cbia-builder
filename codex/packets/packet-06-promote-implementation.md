---
packet_id: packet-06-promote-implementation
packet_number: 6
title: PROMOTE implementation (OPA-gated)
status: planned
priority: P0
authoritative: true
date: 2026-01-10

depends_on:
  - packet-05-mechanical-check-enforcement

applies_to:
  pipeline: cbia-builder
  phases:
    - promote

constraints:
  opa_gate_required: true
  ledger_commit_required: true
  artifact_hash_linkage_required: true
---

# Packet 6 — PROMOTE implementation

## Goal
Implement a formal PROMOTE step that gates artifact promotion/commit on OPA allow, records immutable evidence, and updates the authoritative ledger in a controlled manner.

## Non-Goals
- No direct writes to authoritative artifacts without promotion protocol.
- No bypass paths for “fast merges.”

## Required Deliverables

### A) Promotion protocol (explicit)
Define a promotion protocol that includes:
- what constitutes a promotable artifact set
- required evidence (OPA decision/explain, hash linkage, CHECK pass report)
- allowed destinations (paths/allow-list)
- commit/ledger update rules

Deliver as:
- `control/promote/promote_protocol.md`
- `control/promote/promote_capsule.schema.json`

### B) PROMOTE implementation
Add a deterministic implementation that:
1. verifies CHECK passed and evidence exists
2. verifies OPA allow for promotion input bundle
3. verifies artifact hashes recorded and linked
4. writes promotion ledger entry
5. performs the controlled write/commit step (or outputs a staged patch if commits are handled externally)

Deliver as:
- `tools/promote.py` (or integrated into authoritative runner)
- `execution/promote/report.json`
- updated ledger artifacts under `execution/ledger/`

### C) CI integration (optional but recommended)
Add a CI gate ensuring promotion invariants are checked on PRs.

### D) Tests
- deny promotion if OPA deny
- deny promotion if hash linkage missing
- accept promotion when all evidence present

## Acceptance Criteria
- Promotion cannot occur without OPA allow and complete evidence chain.
- Promotion emits immutable audit artifacts and ledger linkage.
- No “implicit promotion” via ad-hoc commits.

## Suggested Issue Template
Title: `Packet 6: PROMOTE implementation`
Labels: `control`, `packet`, `P0`, `promote`
Branch: `packet/promote-<issue#>`
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

