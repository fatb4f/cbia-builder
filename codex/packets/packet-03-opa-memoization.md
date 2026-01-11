---
packet_id: packet-03-opa-memoization
packet_number: 3
title: OPA memoization (decision caching)
status: planned
priority: P0
authoritative: true
date: 2026-01-10

depends_on:
  - packet-02-deterministic-cache-replay

applies_to:
  pipeline: cbia-builder
  phases:
    - control-kernel

constraints:
  deterministic: true
  must_emit_decision_explain_on_replay: true
---

# Packet 3 — OPA memoization

## Goal
Memoize OPA allow/deny decisions by deterministic **input bundle hash** to reduce redundant OPA execution, while preserving audit evidence and replay determinism.

## Non-Goals
- No changes to OPA policy semantics.
- No “best-effort” caching: memoization must be exact-match only.

## Required Deliverables

### A) Memoization key
Define the memoization key as:
- `opa_input_bundle_hash` (canonical; already produced/available as `opa/bundle.hash` or equivalent)

### B) Memoization storage
Add a deterministic store (filesystem is sufficient), e.g.:
- `opa/memo/<bundle_hash>/decision.json`
- `opa/memo/<bundle_hash>/explain.json`

### C) Runner integration
Update the authoritative runner to:
1. compute OPA input bundle hash deterministically
2. check memo store
3. on hit:
   - copy memoized `decision.json` and `explain.json` into the run’s `opa/` outputs
   - still emit run evidence linking:
     - bundle hash
     - decision hash
     - explain hash
4. on miss:
   - run OPA normally
   - persist outputs into memo store keyed by bundle hash

### D) Invariants
- Memoization must be exact-match only on bundle hash.
- All runs must still produce:
  - `opa/decision.json`
  - `opa/explain.json`
  - `opa/bundle.hash`
- Deny decisions must be memoized identically as allow decisions.

### E) Tests
- same bundle hash → memo hit → identical outputs
- modified bundle contents → different hash → memo miss

## Acceptance Criteria
- OPA execution is skipped on exact-match bundle hash.
- Evidence artifacts are always materialized in the run output.
- Memoization cannot change allow/deny behavior.

## Suggested Issue Template
Title: `Packet 3: OPA memoization`
Labels: `control`, `packet`, `P0`, `opa`
Branch: `packet/opa-memo-<issue#>`
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

