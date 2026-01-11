---
packet_id: packet-04-external-gen-executor-hook
packet_number: 4
title: External GEN executor hook
status: planned
priority: P1
authoritative: true
date: 2026-01-10

depends_on:
  - packet-03-opa-memoization

applies_to:
  pipeline: cbia-builder
  phases:
    - gen

constraints:
  deterministic: true
  control_kernel_must_gate_before_gen: true
  executor_contract_must_be_explicit: true
---

# Packet 4 — External GEN executor hook

## Goal
Introduce a controlled extension point so GEN can be executed by an external executor (e.g. Codex, hosted runner, alternative LLM backend) without changing control semantics.

## Non-Goals
- No change to Control Kernel gating.
- No change to artifact integrity requirements.
- No “dynamic” executor selection that increases state-space freedom without explicit configuration.

## Required Deliverables

### A) Executor contract (explicit)
Define a single executor interface, documented and enforced:
- inputs:
  - pre_gen_capsule (admission context)
  - resolved inputs manifest
  - phase configuration (GEN)
- outputs:
  - generated artifacts in expected locations
  - structured execution report (what was produced, hashes, any tool versions)

Deliver as:
- `control/executors/gen_executor.schema.json` (or `control/pipeline/gen_executor.schema.json`)
- `docs/executors/gen_executor.md` (short, explicit)

### B) Runner integration
Update the authoritative runner to:
- choose executor via explicit config:
  - environment variable OR config file under `control/runtime/`
  - default remains current built-in behavior
- enforce:
  - Control Kernel admission before invoking executor
  - post-exec artifact hash recording
  - CHECK phase proceeds mechanically (Packet 5) after GEN

### C) Reference executor (local)
Provide a minimal reference executor:
- `tools/executors/gen_local.py` (or similar)
- deterministic invocation
- no network assumptions

### D) Tests
- default path unchanged when executor not configured
- configured executor path invoked and outputs recorded

## Acceptance Criteria
- GEN can be swapped without altering the Control Kernel or downstream invariants.
- Executor inputs/outputs are validated against schema.
- Artifacts from executor are recorded and auditable.

## Suggested Issue Template
Title: `Packet 4: External GEN executor hook`
Labels: `control`, `packet`, `executor`, `P1`
Branch: `packet/external-gen-<issue#>`
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

