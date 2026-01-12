# cbia-builder — Control-Closure Checklist (Content-Gen Readiness)

**Target date:** 2026-01-13 (INF1250 + INF1220 start)

## Objective
Close the remaining control loop so learning-content generation is:
- **Scope-bound** (course/module/TP explicitly selected; no implicit defaults)
- **OPA-gated** (supervisory allow/deny is authoritative and reproducible)
- **Mechanically checked** (schemas + invariants + normalization)
- **Repair-bounded** (explicit diffs only, budgeted)
- **Promote-gated** (no promotion without evidence + hashes)

This checklist is organized as **packets** (each packet is a PR-sized, deterministic change). Each packet defines:
- `packet_id`
- end-state predicate `E(ctx)` (high-level)
- high-level requirements
- required artifacts
- acceptance checks (mechanical)

---

# Packet 00 — Baseline Evidence Snapshot

## packet_id
`packet-00-baseline-evidence-snapshot`

## End-state predicate
`E0(ctx) = baseline.exists ∧ baseline.is_replayable ∧ baseline.is_scope_annotated`

## High-level requirements
1. Capture current `main` **plant state** as immutable baseline evidence.
2. Record scope classification for the last successful runs (content-gen vs pipeline-sre).
3. Ensure evidence is sufficient to reproduce: inputs → decision → outputs hash set.

## Required artifacts
- `execution/baselines/packet-00/`
  - `plant.snapshot.json` (hashes of control maps + key control files)
  - `runs.snapshot.json` (last N run manifests + decisions)
  - `scope.classification.json` (per run: scope + rationale)

## Acceptance checks
- A single script generates snapshots deterministically.
- Hashes are computed and stored; rerun yields identical results on same ref.

---

# Packet 01 — Scope Binding: Run Profile SSOT

## packet_id
`packet-01-run-profile-ssot`

## End-state predicate
`E1(ctx) = run_profile.required ∧ run_profile.valid ∧ scope_paths.resolved ∧ no_implicit_defaults`

## High-level requirements
1. Introduce **one** SSOT for selecting scope (course/module/TP) per run.
2. The pipeline driver must refuse to run without an explicit scope selection.
3. The selected scope must resolve to **canonical paths**:
   - objectives inputs
   - dependency graph inputs (if used)
   - output root(s)

## Required artifacts
- `control/runtime/run_profile.schema.json`
- `control/runtime/run_profile.example.json`
- `control/runtime/run_profile.json` (optional local default, but runner must accept explicit override)

## Acceptance checks
- Runner fails with a clear reason if run_profile is missing/invalid.
- Runner emits resolved paths into PRE_GEN capsule.

---

# Packet 02 — OPA Input Materialization: Views-as-Generated

## packet_id
`packet-02-opa-input-materialization`

## End-state predicate
`E2(ctx) = opa_inputs.generated ∧ opa_inputs.hash_bound ∧ opa_gate_reproducible`

## High-level requirements
1. Decide SSOT strategy (low volume, high fidelity):
   - **Option A (preferred):** Generate repo-root **views** (`objectives.json`, `dependency.graph.json`) from `cbia-content/<course>/objectives/*` per run profile.
   - **Option B:** Stop using repo-root views; instead build OPA input bundle from scope-resolved paths.
2. The OPA input bundle must be:
   - fully materialized from explicit inputs
   - hashed
   - reproducible

## Required artifacts
- `tools/materialize_opa_inputs.py` (single entrypoint)
- Output (generated; no-hand-edit rule enforced by CI):
  - `opa/input.json`
  - `opa/bundle.hash`
  - (if using views) `objectives.json`, `dependency.graph.json`

## Acceptance checks
- `tools/materialize_opa_inputs.py` produces identical `opa/input.json` for same ref + run_profile.
- CI denies merge if generated artifacts differ from regen.

---

# Packet 03 — PRE_GEN Capsule Isomorphism: Schema ↔ Emission

## packet_id
`packet-03-pre-gen-capsule-isomorphism`

## End-state predicate
`E3(ctx) = capsule.validates ∧ capsule.complete ∧ capsule.hash_bound`

## High-level requirements
1. PRE_GEN capsule emission must **validate** against `pre_gen_capsule.schema.json`.
2. No `additionalProperties` mismatches.
3. Capsule must include:
   - resolved scope
   - executor identity (`gen_executor`) (either add to schema or stop emitting)
   - input hashes (authority ledger hash, policy bundle hash, objectives hash)

## Required artifacts
- Updated `control/runtime/pre_gen_capsule.schema.json` (or updated emission)
- `tools/validate_capsule.py`

## Acceptance checks
- Runner fails hard if capsule validation fails.
- Capsule hash recorded in `execution/ledger/run.manifest.json`.

---

# Packet 04 — OPA as Authoritative Gate (Not Mirror-Only)

## packet_id
`packet-04-opa-authoritative-gate`

## End-state predicate
`E4(ctx) = opa_decision.authoritative ∧ explain.emitted ∧ deny_blocks_execution`

## High-level requirements
1. Replace/upgrade “python mirror gate” so **OPA decision is authoritative**.
2. Require emission of:
   - `opa/decision.json`
   - `opa/explain.json`
   - `opa/bundle.hash`
3. Deny must stop the run before GEN.

## Required artifacts
- `tools/opa_eval.py` (wrapper) or integrate into existing driver
- `execution/ledger/opa.decision.manifest.json` (optional, but recommended)

## Acceptance checks
- Toggling a known-deny condition causes deterministic deny.
- Allow causes deterministic allow with explain output.

---

# Packet 05 — CHECK Phase: Mechanical Schema + Invariants + Normalization

## packet_id
`packet-05-check-phase-mechanical`

## End-state predicate
`E5(ctx) = outputs.schema_valid ∧ outputs.normalized ∧ invariants.pass ∧ evidence.emitted`

## High-level requirements
1. Implement CHECK as a **mechanical** phase (no GPT).
2. CHECK must validate:
   - content-block schemas (per artifact kind)
   - manifest schemas
   - path allow-list + forbidden outputs
   - objective→authority closure for generated artifacts
   - deterministic normalization (canonical ordering, formatting, stable keys)

## Required artifacts
- `tools/check_phase.py`
- `execution/ledger/check.report.json` (machine-readable)

## Acceptance checks
- Any schema violation fails the run.
- Normalization is deterministic (regen yields same canonical form).

---

# Packet 06 — REPAIR Phase: Bounded, Explicit Diffs Only

## packet_id
`packet-06-repair-phase-bounded`

## End-state predicate
`E6(ctx) = repair.optional ∧ repair.budgeted ∧ repair.delta_measured ∧ post_repair_check_passes`

## High-level requirements
1. REPAIR is only entered if CHECK fails.
2. Repair inputs are restricted to explicit diffs:
   - the failing files
   - machine error report
   - allowed transformations (enum)
3. Enforce budgets:
   - max changed lines
   - max files touched
   - max commits in repair loop

## Required artifacts
- `control/runtime/repair_policy.schema.json`
- `control/runtime/repair_policy.example.json`
- `tools/repair_orchestrator.py` (driver; can call external executor)
- `execution/ledger/repair.report.json`

## Acceptance checks
- Repair loop stops deterministically when budgets exceeded.
- Post-repair CHECK must pass before PROMOTE.

---

# Packet 07 — PROMOTE Phase: Evidence + Hashes Required

## packet_id
`packet-07-promote-phase-evidence`

## End-state predicate
`E7(ctx) = promote.requires(check.pass ∧ hashes.recorded ∧ closure.proven ∧ allow.decision) ∧ promote.emits_manifest`

## High-level requirements
1. PROMOTE cannot occur unless:
   - OPA allow is present
   - CHECK pass report is present
   - artifact hashes are recorded
   - objective→authority closure is proven
2. PROMOTE emits a single promotion manifest linking:
   - capsule hash
   - opa bundle/decision hashes
   - outputs hashes
   - scope

## Required artifacts
- `tools/promote_phase.py`
- `execution/ledger/promotion.manifest.json`

## Acceptance checks
- Promotion fails if any required evidence is missing.
- Promotion manifest is deterministic and complete.

---

# Packet 08 — INF1250 Bootstrap: Authority + Objectives + First Controlled Deliverable

## packet_id
`packet-08-inf1250-bootstrap`

## End-state predicate
`E8(ctx) = inf1250.authority_defined ∧ inf1250.objectives.present ∧ inf1250.first_artifact.generated ∧ check.pass ∧ promote.pass`

## High-level requirements
1. Add INF1250 authority sources (feuille de route, syllabus refs, TP statements) to the authority ledger.
2. Generate/ingest INF1250 objectives for the first target slice (minimum viable set).
3. Produce **one** controlled learning artifact (e.g., M2 theory block pack) under full pipeline.

## Required artifacts
- `control/authority.ledger.json` updated with INF1250 authority entries
- `cbia-content/inf1250/objectives/` populated
- `cbia-content/inf1250/material/<slice>/` first artifact(s)
- promotion manifest + evidence ledger

## Acceptance checks
- OPA allow + CHECK pass + PROMOTE pass for INF1250 slice.
- Outputs are schema-valid and linked to authority.

---

# Minimal “tomorrow morning” subset (if time is tight)

If you need a smallest safe set to run content-gen immediately:
- Packet 01 (run profile SSOT)
- Packet 03 (capsule isomorphism)
- Packet 05 (CHECK mechanical)
- Packet 08 (INF1250 bootstrap)

Rationale: this makes scope explicit, prevents silent schema drift, and ensures generated outputs are mechanically validated.

---

# Notes on low-volume/high-fidelity constraints
- Prefer **one** preflight/controller script for each scope:
  - content-gen controller
  - pipeline-sre controller
- Prefer SSOT JSON inputs → deterministic rendering → regen-and-compare in CI.
- Avoid adding new “choice points” unless the policy explicitly enumerates them.

