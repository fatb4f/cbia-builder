package control.inference
default allow := false

valid(o) {
  o.type == "authoritative"
} else {
  o.type == "derived"
} else {
  o.type == "inferred"
  o.justification != ""
  count(o.constraints) > 0
  o.inference_depth <= input.inference_policy.max_depth
}

allow {
  every o in input.objectives {
    valid(o)
  }
}