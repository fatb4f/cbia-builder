# Implementation Plan — Pipeline-SRE Skill

## Objective
Implement Pipeline-SRE (pipeline-structure-ops) as a **controller skill** where:
- constraints are **first-class algorithms**
- the packet defines an **algebraic end-state** predicate
- instructions and mechanical checks are **isomorphic** via a shared SSOT
- execution is driven by a **skill DAG** (fail-closed)

Low volume / high fidelity approach: **one mechanical preflight controller** + regen-and-compare + bounded repair.

---

## Deliverables
1. **Skill SSOT**
   - `.codex/skills/pipeline-sre/skill.json`
   - `.codex/skills/pipeline-sre/end_state.json` (algebraic predicate)
   - `.codex/skills/pipeline-sre/dag.json` (SSOT DAG)
   - `.codex/skills/pipeline-sre/constraints/catalog.json`

2. **Mechanical controller**
   - `tools/orchestrator.py` (generic DAG runner)
   - `tools/structure_ops_preflight.py` (Pipeline-SRE concrete checks; may be called by orchestrator)

3. **Contracts**
   - `control/packets/packet_contract.schema.json`
   - `control/packets/packet-XX-pipeline-sre.json` (example contract)

4. **Control maps (mechanically generated)**
   - `control/plant/pipeline_sre_dag.json` (SSOT DAG for plant)
   - `control/plant/pipeline_sre_dag.mmd` (view)

5. **CI gates**
   - one step: checkout full history + run orchestrator
   - evidence JSON artifact emission

6. **Algebraic law tests**
   - determinism, fail-closed, regen idempotence, coverage, repair boundedness

---

## Skill package layout
```text
.codex/skills/pipeline-sre/
  SKILL.md
  skill.json
  end_state.json
  dag.json
  constraints/
    catalog.json
  tests/
    test_laws.py

control/packets/
  packet_contract.schema.json
  packet-XX-pipeline-sre.json

control/plant/
  pipeline_sre_dag.json
  pipeline_sre_dag.mmd

tools/
  orchestrator.py
  structure_ops_preflight.py
  gen_control_maps.py
```

---

## Skill DAG (supporting DAG)

### Mermaid view (generated from JSON SSOT)
```mermaid
flowchart TD
  S([START]) --> A1[Load end_state + packet contract]
  A1 --> Gcov{Coverage: required primitives constrained?}
  Gcov -- no --> Xcov([STOP: PRIMITIVE_UNCONTROLLED])

  Gcov -- yes --> A2[Derive PR scope evidence]
  A2 --> G2{Paths ⊆ allowed_paths?}
  G2 -- no --> X2([STOP: PATH_SCOPE_VIOLATION])

  G2 -- yes --> G2b{Diff size within budget?}
  G2b -- no --> X2b([STOP: DIFF_BUDGET_EXCEEDED])

  G2b -- yes --> G3{Forbidden patterns absent?}
  G3 -- no --> X3([STOP: SEMANTIC_SCOPE_VIOLATION])

  G3 -- yes --> G4{No forbidden outputs/runtime leakage?}
  G4 -- no --> X4([STOP: RUNTIME_LEAKAGE])

  G4 -- yes --> A4[Regen control maps mechanically]
  A4 --> G5{Regen-and-compare clean?}
  G5 -- no --> X5([STOP: MAP_DRIFT])

  G5 -- yes --> G6{Interface files/keys present?}
  G6 -- no --> X6([STOP: INTERFACE_MISMATCH])

  G6 -- yes --> G7{Base-ref + CI determinism invariants satisfied?}
  G7 -- no --> X7([STOP: CI_NONDETERMINISM])

  G7 -- yes --> A6[Run CI supervisory gates]
  A6 --> G8{CI pass?}
  G8 -- yes --> PM[Promote merge (human)] --> E([END: MERGED])

  G8 -- no --> D[Diagnose; emit reason code]
  D --> RB{Repair budget available?}
  RB -- no --> X8([STOP: REPAIR_EXHAUSTED])

  RB -- yes --> RD{Repair delta within budget + allowed paths?}
  RD -- no --> X9([STOP: REPAIR_DELTA_VIOLATION])

  RD -- yes --> R[Execute bounded repair]
  R --> A6
```

### JSON SSOT (skill-local `dag.json`)
- Nodes: `action | gate | terminal`
- Gates list constraints (IDs) and pass/fail targets

(Keep this SSOT minimal; Mermaid is generated.)

---

## End-state SSOT (algebraic predicate)

### `end_state.json` model
A strict conjunction of named constraints:

\[
E(ctx) := \bigwedge_i C_i(ctx)
\]

Example shape:
```json
{
  "packet_id": "pipeline-sre",
  "scope": "pipeline-structure-ops",
  "required_primitives": ["P0","P1","P2","P4","P5","P6","P7","P8","P10","P11","P13"],
  "constraints": [
    {"id": "contract_valid.v1", "primitives": ["P0"]},
    {"id": "derive_pr_scope.v1", "primitives": ["P1","P13"]},
    {"id": "path_scope.v1", "primitives": ["P1"], "params": {"allowed_paths_ref": "contract.allowed_paths"}},
    {"id": "diff_budget.v1", "primitives": ["P2"], "params": {"budget_ref": "contract.diff_budget"}},
    {"id": "semantic_forbidden_patterns.v1", "primitives": ["P3"], "params": {"patterns_ref": "contract.forbidden_patterns"}},
    {"id": "forbidden_outputs.v1", "primitives": ["P4","P5"], "params": {"forbidden_ref": "contract.forbidden_outputs"}},
    {"id": "regen_no_drift.v1", "primitives": ["P6"], "params": {"regen_cmd_ref": "contract.regen_cmd"}},
    {"id": "interface_required_files_keys.v1", "primitives": ["P7"], "params": {"files_ref": "contract.required_files", "keys_ref": "contract.required_json_keys"}},
    {"id": "ci_determinism_base_ref.v1", "primitives": ["P8","P13"]},
    {"id": "repair_policy.v1", "primitives": ["P10","P11"], "params": {"policy_ref": "contract.repair_policy"}}
  ]
}
```

**Isomorphism enforcement**
- `SKILL.md` contains a generated “End-state constraints” block including `hash(end_state.json)`
- `structure_ops_preflight.py` verifies the hash matches what the skill declares

---

## Constraint catalog
`constraints/catalog.json` maps IDs → implementations:
```json
{
  "contract_valid.v1": {"impl": "python:structure_ops_preflight:contract_valid"},
  "derive_pr_scope.v1": {"impl": "python:structure_ops_preflight:derive_pr_scope"},
  "path_scope.v1": {"impl": "python:structure_ops_preflight:path_scope"},
  "diff_budget.v1": {"impl": "python:structure_ops_preflight:diff_budget"},
  "semantic_forbidden_patterns.v1": {"impl": "python:structure_ops_preflight:forbidden_patterns"},
  "forbidden_outputs.v1": {"impl": "python:structure_ops_preflight:forbidden_outputs"},
  "regen_no_drift.v1": {"impl": "python:structure_ops_preflight:regen_no_drift"},
  "interface_required_files_keys.v1": {"impl": "python:structure_ops_preflight:interface_required"},
  "ci_determinism_base_ref.v1": {"impl": "python:structure_ops_preflight:ci_determinism"},
  "repair_policy.v1": {"impl": "python:structure_ops_preflight:repair_policy"}
}
```

Low volume: keep implementations in one module initially.

---

## Orchestrator execution model

### `tools/orchestrator.py` (generic)
Responsibilities:
- load `skill.json`, `dag.json`, `end_state.json`, contract
- compute `Context` (observer)
- execute DAG deterministically
- for each gate node:
  - evaluate listed constraints via catalog
  - merge decisions fail-closed
  - emit evidence JSON per node

Evidence outputs (stable paths):
- `artifacts/pipeline-sre/decision.json`
- `artifacts/pipeline-sre/explain.json`
- `artifacts/pipeline-sre/evidence/<node-id>.json`

---

## CI integration
Single entrypoint step:
- checkout with `fetch-depth: 0`
- run orchestrator
- upload `artifacts/pipeline-sre/**` as workflow artifact

---

## Algebraic law tests (minimal)

### Laws
1. **Determinism**
   - Same `ctx_hash` → same `decision_hash` and `evidence_hash`.
2. **Fail-closed**
   - Remove an observable (e.g., delete contract file) → DENY.
3. **Regen idempotence**
   - Run regen twice → no drift; same output hashes.
4. **Coverage**
   - If `required_primitives` not subset of union of constraint primitives → DENY.
5. **Repair boundedness**
   - Exceed commit-count budget or delta budget → DENY.

### Test harness
- Use golden fixtures (small repo snapshots or synthetic contexts)
- Keep test count low; each law is a compact set of assertions

---

## Milestone plan (sequenced)

### M0 — Baseline scaffolding
- Add `.codex/skills/pipeline-sre/` layout
- Add `skill.json`, `dag.json`, `end_state.json` (initial)

### M1 — Mechanical checker (single module)
- Refactor existing `structure_ops_preflight.py` to expose constraint functions
- Add evidence emission per constraint

### M2 — Orchestrator
- Implement DAG runner + catalog loader
- Implement coverage gate

### M3 — CI wiring
- Replace ad-hoc steps with `tools/orchestrator.py --skill pipeline-sre`
- Add artifact upload

### M4 — Law tests
- Add minimal law tests for determinism/fail-closed/regen/coverage/repair

### M5 — Isomorphism enforcement
- Generate the “End-state constraints” block in `SKILL.md`
- Verify `end_state.json` hash matches in checks

---

## Acceptance criteria (implementation)
1. A Pipeline-SRE PR is accepted **iff** the orchestrator returns ALLOW.
2. Orchestrator emits node-level evidence JSON with reason codes.
3. Coverage gate denies missing primitives.
4. Regen-and-compare denies any drift.
5. Repair loop is bounded and audited.

---

## Pointers to next refinements (deferred unless needed)
1. Upgrade semantic scope from `forbidden_patterns` → explicit model:
   - `allowed_commands`, `forbidden_imports`, `forbidden_globs`
2. PR metadata gate (Closes #XX / labels) if automation requires it.
3. Optional no-network/side-effects gate (P14) later.
4. Enforce “no hand edits” by making Mermaid a generated view of JSON SSOT.
5. Unify all checks under the orchestrator entrypoint (no parallel paths).

