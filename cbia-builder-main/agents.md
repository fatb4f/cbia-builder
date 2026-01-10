# agents.md — Hard-Gated Generative Execution (PRE-GEN Capsule + OPA)

## Execution Mode: GPT-Executed Pipeline

This repository defines a **GPT-executed pipeline**.

- GPT performs **operator actions** (extract, infer, propose, generate).
- Repository scripts are **reference contracts**: they define ordering, invariants, schemas, and acceptance criteria.
- **No GPT output is authoritative by default**. Promotion to authoritative artifacts occurs only after **STRUCT acceptance**.

### Canonical Pipeline DAG

All execution MUST follow the DAG:

- DAG graph: `control/pipeline/inf1220_tp1_gpt_exec.dag.mmd`
- DAG IO map: `control/pipeline/inf1220_tp1_gpt_exec.dag.map.json`

Each DAG node declares:
- required inputs
- emitted artifacts
- acceptance gate (STRUCT) where applicable

### Artifact Tiers

**Operator outputs (GPT):**
- Suffix: `.gpt.json`
- May include pointers/references
- Never authoritative
- Never ledger-eligible

**Authoritative artifacts (accepted):**
- No `.gpt` suffix
- Produced only by STRUCT (validation/materialization) or explicit promotion step
- Hashable + ledger-eligible

### Scope Discipline (INF1220 TP1)

Default slice is **TP1-only**:
- Objectives must be evidenced by TP1.
- Syllabus-derived but unassessed items go to review buffers and are not promoted without a review decision.
- Depth halos are **reference-only**; drills must not require halo knowledge.

### Evidence Rule

If an objective depends on source text, GPT must emit evidence pointers to a trusted capsule.
A trusted step materializes:
- locator
- quote span
- hash references

No evidence → no objective.




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


## Objective extraction (GPT-first, audit-grade via evidence pointers)

### Problem
When GPT performs extraction (instead of a local script), it cannot be required to:
- compute file hashes
- embed long authority text
- guarantee stable quoting

### Solution
Use a **locally-hashed extraction capsule** as the auditable substrate.

#### 1) Runner builds a TP extraction capsule (local, deterministic)
- Input: authoritative TP file(s) referenced in `control/authority.ledger.json`
- Output: `control/runtime/tp1_extraction_capsule.json`
  - includes file sha256
  - includes chunk map (chunk_id + locator + chunk sha256)
  - optionally includes bounded excerpts

#### 2) GPT emits pointer-only objectives (GEN-EXTRACT)
- Output: `cbia-content/<track>/objectives/tp1.extracted.gpt.json`
- Every objective must include `evidence_ptrs[]` that reference `chunk_id` values from the capsule.
- No raw quoting required in GPT output.

#### 3) STRUCT materializes evidence (audit upgrade)
- Resolve pointers → attach:
  - `path`
  - `locator`
  - `quote` (bounded)
  - `hash_ref` (file sha256 + quote/chunk sha256)
- Output: `cbia-content/<track>/objectives/tp1.extracted.json`
- Any unresolvable pointer => **STOP**.

### Mobile-only execution mode
If the user cannot run anything locally, the assistant must:
1) Generate required artifacts inside the repo (objectives, DAG, learning material).
2) Replace dummy GEN in `tools/run_pipeline.py` with a real packaging run.
3) Provide an updated repo archive as the runnable deliverable.
