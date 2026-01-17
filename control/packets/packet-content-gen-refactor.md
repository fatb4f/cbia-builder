# Packet: content-gen workflow refactor (objectives + inferred math recalls + pointer maps + split DAGs)

## Purpose
Refactor the content-gen workflow so it produces and validates the following canonical artifacts:

- formal_objectives.json (SSOT: extracted objectives)
- pointer_map.json (objective -> pointer anchors; referential only)
- math_topic_index.json (derived from master math doc)
- math_recall_map.json (inferred: objective -> math topics, recall-only, with evidence)
- objective_dependency_dag.json (authoritative; objectives-only prerequisite graph)
- execution_dag.json (derived; build/execution plan including notebook/drill steps)

## Hard constraints (must hold)
1) NO syllabus regeneration or paraphrase. Syllabus is immutable authority.
2) formal_objectives.json is the SSOT for intent (capabilities), not pedagogy.
3) math_recall_map.json MUST be derived by cross-referencing:
   - formal_objectives.json (objective text + refs)
   - master math doc (sanitized)
   - inference rules: control/rules/math_inference_rules.v0.1.0.json
   - topic seed: control/rules/math_topic_index.seed.json (extend deterministically if needed)
4) objective_dependency_dag.json must contain ONLY objective nodes and prerequisite edges.
5) execution_dag.json may include notebooks/drills/build steps but must be derived and MUST gate
   notebooks/drills behind pointer_map + math_topic_index + math_recall_map creation.
6) All produced JSON artifacts must validate against control/schemas/*.schema.json

## Outputs (required paths)
- control/artifacts/formal_objectives.json
- control/artifacts/pointer_map.json
- control/artifacts/math_topic_index.json
- control/artifacts/math_recall_map.json
- control/artifacts/objective_dependency_dag.json
- control/artifacts/execution_dag.json
- control/artifacts/validation_report.json

## Acceptance criteria
- math_recall_map is reproducible from (objectives + master math doc + rules).
- objective_dependency_dag is acyclic, closed, and objective-only.
- execution_dag includes explicit stage ordering and STOP terminals on missing/invalid artifacts.
- validation_report.json records schema pass/fail + sha256 hashes of all artifacts.
