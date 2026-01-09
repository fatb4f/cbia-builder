package assurance

default allow = false

################################################################################
# Required inputs (assembled by runner):
#
# input.pre_gen_capsule
# input.authority_ledger
# input.objectives
# input.dependency_graph
# input.run_ledger
# input.artifact_hashes
################################################################################

auth_immutable {
  input.pre_gen_capsule.kernel_decision == "ALLOW"
  input.authority_ledger.frozen == true
}

closed_world_authority {
  authority_ids := {a.authority_id | a := input.authority_ledger.authority_set}
  all_refs := {ref |
    entry := input.run_ledger[_]
    ref := entry.authority_ids[_]
  }
  all_refs ⊆ authority_ids
}

dependency_closure {
  not orphan_artifact
}

orphan_artifact {
  entry := input.run_ledger[_]
  entry.artifact_id != ""
  count(entry.objective_ids) == 0
}

inference_compliance {
  not invalid_inference
}

invalid_inference {
  o := input.objectives[_]
  o.type == "inferred"
  o.justification == ""
}

phase_admissibility {
  phases := [e.phase | e := input.run_ledger[_]]
  phases == sort(phases)
}

artifact_integrity {
  not hash_mismatch
}

hash_mismatch {
  e := input.run_ledger[_]
  e.artifact_path != ""
  input.artifact_hashes[e.artifact_path] != e.hash
}

allow {
  auth_immutable
  closed_world_authority
  dependency_closure
  inference_compliance
  phase_admissibility
  artifact_integrity
}