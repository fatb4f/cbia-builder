# agents.md — Hard-Gated Generative Execution (PRE-GEN Capsule + OPA)

## Hard gates (non-negotiable)
- **GEN is forbidden** unless:
  1) `control/runtime/pre_gen_capsule.json` exists and validates against `control/runtime/pre_gen_capsule.schema.json`, AND
  2) OPA evaluates `data.assurance.allow == true` using `policy/assurance/assurance.rego` (policy bundle identified by `opa/bundle.hash`).

- Authority/objectives/dependency constraints are **read-only** after PRE-GEN.
- Each phase appends to the run ledger (`execution/ledger/run.ledger.json`).

## Required runtime artifacts (must exist before GEN)
- `control/runtime/pre_gen_capsule.json`
- `opa/decision.json`
- `opa/explain.json`
- `opa/bundle.hash`

## Phase 0 — Authority Lock (HARD GATE)
1. Load `control/authority.ledger.json`.
2. Validate schema; assert `frozen == true`.
3. Assert every authority entry has `source.locator` and `hash`.
4. Emit a lock report.

**Stop on failure.**

## Phase 1 — PRE-GEN Control Kernel (HARD GATE)
1. Evaluate the Control Kernel over the authority set and policies.
2. Emit `control/runtime/pre_gen_capsule.json` with:
   - `kernel_decision ∈ {ALLOW,DENY}`
   - `control_state_hash`
   - `policy_bundle_hash`
   - `authority_set_hashes`
   - optional `dependency_graph_hash`, `execution_dag_hash`
3. If `kernel_decision != ALLOW`: **Stop**.

## Phase 2 — OPA Assurance Gate (HARD GATE)
1. Assemble OPA input bundle with:
   - `pre_gen_capsule`
   - `authority_ledger`
   - `objectives`
   - `dependency_graph`
   - `run_ledger` (may be empty initially)
   - `artifact_hashes` (may be empty initially)
2. Evaluate OPA policy package `assurance`.
3. Persist:
   - `opa/decision.json`
   - `opa/explain.json`
   - `opa/bundle.hash`
4. Require: `data.assurance.allow == true`.
   - If false: **Stop** (GEN is forbidden).

## Phase 3 — GEN (execution only)
- Generate candidate artifacts strictly from locked objectives.
- On artifact creation:
  - compute sha256
  - append ledger entry with objective + authority references
  - update artifact hash map

## Phase 4 — STRUCT
- Normalize formats; enforce schemas; attach metadata.
- Append ledger entries + check results.

## Phase 5 — SELECT
- Deterministically prune/accept based on declared criteria.
- Append ledger entries + check results.

## Phase 6 — FLOW
- Package to final layout (dist/bundle).
- Append ledger entries + check results.

## Phase 7 — EVAL (audit bundle)
1. Re-run OPA assurance evaluation over final run state.
2. Emit audit bundle per `assurance/audit_bundle.manifest.json`:
   - capsule
   - decision/explain
   - run ledger + artifact hashes
   - authority ledger
3. Freeze (final manifest + hashes).
