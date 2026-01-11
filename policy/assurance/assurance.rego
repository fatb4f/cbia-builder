package assurance

default allow = false

################################################################################
# Required inputs:
# input.pre_gen_capsule
# input.authority_ledger
# input.objectives
# input.dependency_graph
# input.execution_dag
# input.run_ledger
# input.artifact_hashes
################################################################################

# --- gates (explicit, required) ---
evidence_materialized := input.gates.evidence_materialized
promotion_admissible := input.gates.promotion_admissible

# ---------- Authority immutability (hash equality) ----------
auth_immutable {
  input.pre_gen_capsule.kernel_decision == "ALLOW"
  input.authority_ledger.frozen == true

  capsule_hashes := input.pre_gen_capsule.authority_set_hashes
  ledger_hashes := {a.authority_id: a.hash.value | a := input.authority_ledger.authority_set}

  capsule_hashes == ledger_hashes
}

# ---------- Closed-world authority ----------
closed_world_authority {
  authority_ids := {a.authority_id | a := input.authority_ledger.authority_set}

  used := {aid |
    e := input.run_ledger[_]
    aid := e.authority_ids[_]
  }

  used ⊆ authority_ids
}

# ---------- Dependency closure: artifact -> objective -> authority ----------
dependency_closure {
  not orphan_artifact
}

orphan_artifact {
  e := input.run_ledger[_]
  e.artifact_id != ""

  some oid
  oid := e.objective_ids[_]

  not objective_traces_to_authority(oid)
}

objective_traces_to_authority(oid) {
  o := input.objectives[_]
  o.id == oid
  a := o.source.authority_id
  a != ""
}

# ---------- Inference compliance ----------
inference_compliance {
  not invalid_inference
}

invalid_inference {
  o := input.objectives[_]
  o.type == "inferred"
  (o.justification == "" or count(o.constraints) == 0)
}

# ---------- Phase admissibility (explicit order) ----------
phase_order := ["PRE_GEN", "OPA_GATE", "GEN", "STRUCT", "SELECT", "FLOW", "EVAL"]

phase_admissibility {
  phases := [e.phase | e := input.run_ledger[_]]
  indices := [indexof(phase_order, p) | p := phases]
  indices == sort(indices)
}

# ---------- Artifact integrity ----------
artifact_integrity {
  not hash_mismatch
}

hash_mismatch {
  e := input.run_ledger[_]
  e.artifact_path != ""
  input.artifact_hashes[e.artifact_path] != e.hash
}

# ---------- Deterministic replay (bounded) ----------
deterministic_replay {
  input.pre_gen_capsule.policy_bundle_hash == input.run_ledger[0].policy_bundle_hash
}

allow {
  evidence_materialized == true
  promotion_admissible == true
  auth_immutable
  closed_world_authority
  dependency_closure
  inference_compliance
  phase_admissibility
  artifact_integrity
  deterministic_replay
}
