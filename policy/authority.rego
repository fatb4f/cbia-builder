package control.authority
default allow := false
allow {
  count(input.authority_set) > 0
  input.frozen == true
}