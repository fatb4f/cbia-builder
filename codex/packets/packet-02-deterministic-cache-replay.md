---
packet_id: packet-02-deterministic-cache-replay
packet_number: 2
title: Deterministic cache / replay
status: planned
priority: P0
authoritative: true
date: 2026-01-10

depends_on:
  - packet-01-authoritative-driver
  - packet-01_1-orchestration-tightening
  - packet-01_1a-control-map-gate

applies_to:
  pipeline: cbia-builder
  phases:
    - control-kernel
    - gen
    - check
    - repair
    - promote

constraints:
  deterministic: true
  content_addressed: true
  replay_must_emit_evidence: true
---

# Packet 2 — Deterministic cache / replay

## Goal
Add a deterministic, content-addressed **cache + replay** layer so repeated runs with identical admissible inputs can skip execution while still producing full audit evidence.

## Non-Goals
- No change to Control Kernel authority or OPA policy semantics.
- No weakening of hash/evidence requirements.
- No changes to packet ordering or phase names.

## Scope
Cache applies to **phase-level outputs** (at minimum GEN; optionally CHECK/REPAIR where applicable), keyed by a deterministic cache key derived from authoritative inputs.

## Required Deliverables

### A) Cache key schema (authoritative)
Implement a single deterministic cache key that includes, at minimum:
- authority ledger hash
- policy bundle hash (OPA bundle input)
- pre_gen_capsule hash
- inputs manifest hash (resolved dependency closure)
- phase identifier (GEN/CHECK/REPAIR/etc.)
- tool version(s) affecting outputs (runner version, generator version)

Deliver as:
- `execution/cache/cache_key.schema.json` (or equivalent location under `execution/` or `control/`)
- `execution/cache/README.md` explaining the key components and stability rules

### B) Cache storage layout
Define a deterministic on-disk layout, e.g.:
- `execution/cache/<cache_key>/`
  - cached artifacts (phase outputs)
  - `cache.meta.json` (what was cached, sizes, hashes, creation inputs)
  - `opa/decision.json`, `opa/explain.json`, `opa/bundle.hash` (if applicable to the cached phase)

### C) Runner integration (authoritative driver)
Modify the authoritative runner (e.g. `tools/run_pipeline.py`) to:
1. compute cache key **after** Control Kernel admission
2. check cache presence
3. on hit: perform deterministic replay by materializing cached artifacts into the expected run outputs
4. always emit ledger evidence for replay:
   - record cache hit, cache key, and hashes
   - link to the authority/policy/pre_gen capsule hashes
   - re-emit (or copy) OPA decision/explain artifacts as required evidence

### D) Invariants (must be enforced)
- Cache hit MUST NOT bypass Control Kernel gating.
- Cache hit MUST NOT bypass OPA decision requirements.
- Cache hit MUST still produce:
  - execution ledger entry
  - artifact hashes recorded
  - OPA decision/explain artifacts (either replayed copies or re-evaluated with memoization in Packet 3)

### E) Tests
Add minimal deterministic tests:
- same inputs → cache hit → byte-identical outputs
- altered authority ledger or policy bundle → cache miss
- altered pre_gen_capsule → cache miss

## Acceptance Criteria
- A second identical run produces a cache hit and completes without regeneration of phase outputs.
- Replay produces full evidence artifacts and ledger linkage.
- Any change in authoritative inputs forces a cache miss.
- Determinism verified: cache key stable and ordering stable.

## Suggested Issue Template
Title: `Packet 2: Deterministic cache / replay`
Labels: `control`, `packet`, `P0`, `determinism`, `cache`
Branch: `packet/cache-replay-<issue#>`
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

