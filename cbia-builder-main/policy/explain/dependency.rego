package explain.dependency
deny[reason] {
  a := input.artifacts[_]
  not reaches_authority(a.id)
  reason := {
    "controller": "dependency",
    "rule_id": "DCC-ORPHAN",
    "summary": "Artifact does not trace to authority",
    "path": [a.id]
  }
}

reaches_authority(x) {
  e := input.edges[_]
  e.from == x
  input.nodes[e.to].type == "authority"
} else {
  e := input.edges[_]
  e.from == x
  reaches_authority(e.to)
}