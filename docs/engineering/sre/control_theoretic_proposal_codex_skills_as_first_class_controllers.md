# Control-Theoretic Solution Proposal

## Purpose
Model the Codex-agent “skills architecture” so that **constraints are first-class algorithms embedded within execution logic**, not advisory prose. Codex operates as a bounded **actuator**; a deterministic **supervisory controller** decides admissibility and promotion.

## Scope
This proposal applies to cbia-builder with explicit **cross-scope separation**:
- **Scope A**: Runtime learning-content generation (content DAG + OPA supervisory gating).
- **Scope B**: Pipeline-SRE / pipeline-structure-ops (repo structure + control-map + CI hardening).

Primary target in this document: **Scope B** (Pipeline-SRE), using **low volume / high fidelity** mechanical constraints.

---

## System model (control-theoretic framing)

### Plant
The plant is the **repository state transition** induced by edits/commits:
- State: `x` = `(working tree, index, HEAD, diff(base_ref..HEAD), CI outcomes, generated maps, evidence)`
- Inputs: `u` = `(mechanical actions, Codex edits)`
- Outputs: `y` = `(observables extracted from x: diff stats, file touches, drift, required keys, etc.)`

### Controller layers
1. **Supervisory Controller (SC)** — deterministic orchestrator executing a skill DAG.
2. **Constraint Algorithms (Cᵢ)** — first-class gates mapping `Context → Decision + Evidence`.
3. **Actuator (Codex)** — applies bounded edits only when SC permits.

### Observer
The observer computes `Context` (a structured bundle of observables) from repo state:
- `ctx = observe(x; base_ref, contract, env)`
- Observation is mechanical, explicit, and evidence-producing.

---

## Core abstraction: Constraint-as-Algorithm

Define each constraint as a pure(ish) function over explicit observables:

\[
C_i : \text{Context} \rightarrow (allow \in \{0,1\},\ reason,\ evidence)
\]

**Fail-closed rule**: any missing observable, runtime error, or unparseable input yields `allow=0`.

### End-state predicate (algebraic)
A packet/skill defines the intended end state as a conjunction:

\[
E(ctx) := \bigwedge_{i=1}^{n} C_i(ctx)
\]

A run is admissible iff `E(ctx)=true`.

This makes “what we want” **mathematically explicit** and mechanically checkable.

---

## Primitives (degrees of freedom) as a first-class control surface
Each skill explicitly declares the **primitives constrained** (coverage gate):

- P0 Contract content
- P1 Diff surface (paths)
- P2 Diff size budget
- P3 Semantic surface
- P4 Write surface (outputs)
- P5 Runtime evidence leakage
- P6 Control-map regeneration drift
- P7 Interface literals (files/keys)
- P8 CI determinism invariants
- P9 CI outcomes
- P10 Repair loop budget
- P11 Repair delta budget
- P12 PR metadata hooks
- P13 Base ref / merge-base invariants
- P14 Network/side effects

**Coverage invariant** (skill-level):

\[
Required(scope) \subseteq \bigcup_i Primitives(C_i)
\]

If violated → DENY with `PRIMITIVE_UNCONTROLLED`.

---

## Isomorphism: Instruction ↔ Mechanical Check (by construction)

### Problem
“Instruction documents” drift from what the checker enforces.

### Solution
Define a single SSOT for end-state constraints (DSL), then:
- **Render** the instruction to Codex from the SSOT.
- **Evaluate** the mechanical checker from the same SSOT.

**Isomorphism definition (operational)**
- *Syntactic*: instruction references the same constraint IDs and parameters as the SSOT.
- *Semantic*: every normative statement in the instruction has a corresponding constraint in SSOT.

**Enforcement**
- Include `end_state_spec_hash` in the instruction section and verify it during checks.
- Lint: no “English-only constraints.”

---

## Skill architecture as embedded control logic

### Skill package model
A “skill” is a **controller package**:
- SSOT DAG (`dag.json`) defining allowed node transitions.
- End-state constraint spec (`end_state.json`) listing `Cᵢ` and parameters.
- Constraint catalog mapping IDs → implementations (mechanical Python / scoped OPA).
- Orchestrator entrypoint executing DAG + emitting evidence.

### Execution law
Codex cannot bypass gates because:
- Orchestrator chooses the next node based solely on constraint outcomes.
- Promotion is downstream of explicit `ALLOW` decisions + evidence integrity.

---

## Algebraic tests (laws) for constraints (low volume / high fidelity)
Test constraints by **properties**, not examples.

### Required laws for Pipeline-SRE (structure-ops)
1. **Determinism**
   - Same `ContextHash` → same `(DecisionHash, EvidenceHash)`.
2. **Fail-closed**
   - Missing required observable → DENY.
3. **Idempotence of regen**
   - `regen(regen(x)) = regen(x)` and `git diff` remains empty after regen.
4. **Coverage**
   - Required primitives for scope ⊆ constrained primitives.
5. **Repair boundedness**
   - `repairs_used > max_repairs` → DENY; repair delta budgets enforced.

These laws make the controller auditable and regression-resistant without high test volume.

---

## Safety: cross-scope contamination prevention

### Separation rule
Pipeline-SRE skills must deny runtime content-gen artifacts:
- `forbidden_outputs` deny-list (e.g., `control/runtime/**`, `execution/**`, `opa/**`, `cbia-content/**`)

### Supervisory safety interlocks
- Path allow-list + forbidden outputs are enforced before any regen/CI.
- Regen-and-compare denies hand edits to mechanically generated artifacts.

---

## Acceptance criteria (proposal-level)
1. Constraints exist as **named algorithms** with structured evidence output.
2. Every skill packet has:
   - explicit primitives constrained
   - SSOT end-state predicate
   - DAG-executed orchestration (fail-closed)
3. Instruction ↔ check isomorphism is mechanically enforced.
4. Pipeline-SRE achieves low volume / high fidelity via a single preflight controller plus regen-and-compare.

---

## Consequences (what improves)
- Fewer ambiguous “ball throws” because the admissible state space is explicit.
- Stronger auditability: every gate produces evidence with reason codes.
- Drift prevention: SSOT predicate drives both instruction and check.
- Predictable repairs: bounded repair loop with delta budgets.

