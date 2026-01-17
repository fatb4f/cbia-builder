# content-gen refactor prereqs

These files define the pre-refactor contract surface:

- control/schemas/*.schema.json : schema contracts for required artifacts
- control/rules/* : deterministic seeds + inference rules for math recall inference
- control/examples/* : example DAG shapes (objective-only dependency DAG; derived execution DAG)
- control/packets/packet-content-gen-refactor.md : packet contract describing invariants + outputs

Implementation guidance for the refactor:
- math_recalls are inferred from objectives by cross-referencing master math doc using rules.
- objective_dependency_dag is objective-only; execution DAG is derived and may include build steps.
