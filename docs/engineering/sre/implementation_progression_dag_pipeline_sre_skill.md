# Implementation Progression DAG — Pipeline-SRE Skill

This DAG models the **implementation progression** for the Pipeline-SRE skill, aligned to the plan milestones **M0–M5**, plus deferred refinement branches.

---

## Mermaid view

```mermaid
flowchart TD
  S([START]) --> M0[M0: Baseline scaffolding]
  M0 --> G0{G0: Skill SSOT present?}
  G0 -- no --> X0([STOP: M0_INCOMPLETE])

  G0 -- yes --> M1[M1: Mechanical constraint implementations]
  M1 --> G1{G1: Constraints executable + evidence JSON?}
  G1 -- no --> X1([STOP: M1_INCOMPLETE])

  G1 -- yes --> M2[M2: Orchestrator (DAG runner + catalog + coverage gate)]
  M2 --> G2{G2: DAG execution deterministic + fail-closed?}
  G2 -- no --> X2([STOP: M2_INCOMPLETE])

  G2 -- yes --> M3[M3: CI wiring (single entrypoint + artifacts)]
  M3 --> G3{G3: CI runs orchestrator with fetch-depth 0?}
  G3 -- no --> X3([STOP: M3_INCOMPLETE])

  G3 -- yes --> M4[M4: Algebraic law tests]
  M4 --> G4{G4: Laws enforced in CI?}
  G4 -- no --> X4([STOP: M4_INCOMPLETE])

  G4 -- yes --> M5[M5: Isomorphism enforcement]
  M5 --> G5{G5: end_state hash verified + SKILL.md block generated?}
  G5 -- no --> X5([STOP: M5_INCOMPLETE])

  G5 -- yes --> E([END: PIPELINE-SRE SKILL OPERATIONAL])

  %% Deferred refinements (optional branches)
  E --> R1[R1: Semantic scope model upgrade]
  E --> R2[R2: PR metadata gate]
  E --> R3[R3: No-network / side-effects gate]
  E --> R4[R4: Mermaid generated from JSON SSOT]
  E --> R5[R5: Unify all checks under orchestrator]

  R1 --> ER1([END: SEMANTIC_MODEL_UPGRADED])
  R2 --> ER2([END: PR_METADATA_ENFORCED])
  R3 --> ER3([END: NO_NETWORK_ENFORCED])
  R4 --> ER4([END: NO_HAND_EDITS_ENFORCED])
  R5 --> ER5([END: SINGLE_ENTRYPOINT_ENFORCED])
```

---

## Node definitions (what “done” means)

### M0 — Baseline scaffolding
**Artifacts**
- `.codex/skills/pipeline-sre/{skill.json, dag.json, end_state.json, constraints/catalog.json}`
- `control/packets/{packet_contract.schema.json, packet-XX-pipeline-sre.json}`
- `control/plant/pipeline_sre_dag.{json,mmd}` (if plant map is in-scope now)

**Gate G0**
- Files exist, parse as JSON, and satisfy minimal required keys.

### M1 — Mechanical constraint implementations
**Artifacts**
- `tools/structure_ops_preflight.py` exposes constraint functions and emits evidence

**Gate G1**
- Each constraint ID in `constraints/catalog.json` resolves to an executable function.
- Evidence JSON schema is stable and reason codes are emitted.

### M2 — Orchestrator
**Artifacts**
- `tools/orchestrator.py` loads skill SSOT and runs `dag.json`
- Coverage gate: `required_primitives ⊆ ⋃ primitives(Cᵢ)`

**Gate G2**
- Deterministic evaluation for fixed input bundle.
- Fail-closed merge: any error/missing observable ⇒ DENY.
- Emits `artifacts/pipeline-sre/{decision,explain}.json` + per-node evidence.

### M3 — CI wiring
**Artifacts**
- Workflow step calling `python tools/orchestrator.py --skill pipeline-sre ...`
- Evidence artifacts uploaded

**Gate G3**
- `actions/checkout` uses `fetch-depth: 0`
- CI passes on a known-good baseline and denies on known-bad fixture.

### M4 — Algebraic law tests
**Artifacts**
- `.codex/skills/pipeline-sre/tests/test_laws.py`

**Gate G4**
- Laws enforced in CI:
  - determinism
  - fail-closed
  - regen idempotence
  - coverage
  - repair boundedness

### M5 — Isomorphism enforcement
**Artifacts**
- `SKILL.md` includes a generated “End-state constraints (SSOT)” block
- End-state hash is recorded and verified during preflight/orchestrator run

**Gate G5**
- Any drift between instruction block and `end_state.json` hash ⇒ DENY

---

## JSON SSOT (implementation progression)

This JSON is an SSOT representation of the progression DAG above (useful for rendering diagrams and for mechanical checklist enforcement).

```json
{
  "dag_id": "cbia-builder.pipeline_sre.implementation_progression",
  "version": "0.1.0",
  "nodes": [
    {"id": "start", "kind": "terminal"},

    {"id": "m0_scaffold", "kind": "milestone"},
    {"id": "g0_skill_ssot_present", "kind": "gate"},
    {"id": "stop_m0_incomplete", "kind": "terminal"},

    {"id": "m1_constraints_impl", "kind": "milestone"},
    {"id": "g1_constraints_executable", "kind": "gate"},
    {"id": "stop_m1_incomplete", "kind": "terminal"},

    {"id": "m2_orchestrator", "kind": "milestone"},
    {"id": "g2_deterministic_failclosed", "kind": "gate"},
    {"id": "stop_m2_incomplete", "kind": "terminal"},

    {"id": "m3_ci_wiring", "kind": "milestone"},
    {"id": "g3_ci_entrypoint", "kind": "gate"},
    {"id": "stop_m3_incomplete", "kind": "terminal"},

    {"id": "m4_law_tests", "kind": "milestone"},
    {"id": "g4_laws_enforced", "kind": "gate"},
    {"id": "stop_m4_incomplete", "kind": "terminal"},

    {"id": "m5_isomorphism", "kind": "milestone"},
    {"id": "g5_hash_verified", "kind": "gate"},
    {"id": "stop_m5_incomplete", "kind": "terminal"},

    {"id": "end_operational", "kind": "terminal"},

    {"id": "r1_semantic_model", "kind": "refinement"},
    {"id": "r2_pr_metadata", "kind": "refinement"},
    {"id": "r3_no_network", "kind": "refinement"},
    {"id": "r4_mermaid_generated", "kind": "refinement"},
    {"id": "r5_single_entrypoint", "kind": "refinement"},

    {"id": "end_semantic_model", "kind": "terminal"},
    {"id": "end_pr_metadata", "kind": "terminal"},
    {"id": "end_no_network", "kind": "terminal"},
    {"id": "end_no_hand_edits", "kind": "terminal"},
    {"id": "end_single_entrypoint", "kind": "terminal"}
  ],
  "edges": [
    {"from": "start", "to": "m0_scaffold"},
    {"from": "m0_scaffold", "to": "g0_skill_ssot_present"},
    {"from": "g0_skill_ssot_present", "to": "stop_m0_incomplete", "condition": "fail"},
    {"from": "g0_skill_ssot_present", "to": "m1_constraints_impl", "condition": "pass"},

    {"from": "m1_constraints_impl", "to": "g1_constraints_executable"},
    {"from": "g1_constraints_executable", "to": "stop_m1_incomplete", "condition": "fail"},
    {"from": "g1_constraints_executable", "to": "m2_orchestrator", "condition": "pass"},

    {"from": "m2_orchestrator", "to": "g2_deterministic_failclosed"},
    {"from": "g2_deterministic_failclosed", "to": "stop_m2_incomplete", "condition": "fail"},
    {"from": "g2_deterministic_failclosed", "to": "m3_ci_wiring", "condition": "pass"},

    {"from": "m3_ci_wiring", "to": "g3_ci_entrypoint"},
    {"from": "g3_ci_entrypoint", "to": "stop_m3_incomplete", "condition": "fail"},
    {"from": "g3_ci_entrypoint", "to": "m4_law_tests", "condition": "pass"},

    {"from": "m4_law_tests", "to": "g4_laws_enforced"},
    {"from": "g4_laws_enforced", "to": "stop_m4_incomplete", "condition": "fail"},
    {"from": "g4_laws_enforced", "to": "m5_isomorphism", "condition": "pass"},

    {"from": "m5_isomorphism", "to": "g5_hash_verified"},
    {"from": "g5_hash_verified", "to": "stop_m5_incomplete", "condition": "fail"},
    {"from": "g5_hash_verified", "to": "end_operational", "condition": "pass"},

    {"from": "end_operational", "to": "r1_semantic_model"},
    {"from": "end_operational", "to": "r2_pr_metadata"},
    {"from": "end_operational", "to": "r3_no_network"},
    {"from": "end_operational", "to": "r4_mermaid_generated"},
    {"from": "end_operational", "to": "r5_single_entrypoint"},

    {"from": "r1_semantic_model", "to": "end_semantic_model"},
    {"from": "r2_pr_metadata", "to": "end_pr_metadata"},
    {"from": "r3_no_network", "to": "end_no_network"},
    {"from": "r4_mermaid_generated", "to": "end_no_hand_edits"},
    {"from": "r5_single_entrypoint", "to": "end_single_entrypoint"}
  ]
}
```

---

## Notes
- This is an **implementation progression DAG** (project plan execution), not the runtime skill DAG.
- If you want to mechanically enforce the progression, this DAG can drive a checklist runner (e.g., a `tools/plan_preflight.py`) that asserts required artifacts exist and that CI wiring matches the plan.

