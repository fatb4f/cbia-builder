package explain.authority
deny[reason] {
  count(input.authority_set) == 0
  reason := {
    "controller": "authority",
    "rule_id": "AUTH-EMPTY",
    "summary": "No authority sources declared"
  }
}