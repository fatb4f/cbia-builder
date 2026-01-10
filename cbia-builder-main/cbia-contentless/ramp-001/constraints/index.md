# ramp-001 — Constraints index

This ramp uses a legacy SSOT-style input snapshot stored at `constraints/ssot-input/`.

## Track
- **id:** python-cbia-contract-pipelines-v1
- **title:** Python CBIA Contract Pipelines v1
- **version:** 0.1.0

## Modules
- `co-01-python-core-for-operators` — Write and refactor small, deterministic pipeline operators with clean module boundaries and safe IO at edges.
- `co-02-typed-boundary-contracts` — Encode stable operator/pipeline contracts using modern typing primitives to reduce ambiguity and enable static checking.
- `co-03-pydantic-contract-layer` — Use Pydantic v2 models as the primary contract layer for validation, parsing, and serialization across pipeline boundaries.
- `co-04-repo-structure-and-import-discipline` — Maintain scalable project structure with explicit boundaries: schemas, operators, pipelines, CLI.
- `co-05-cli-orchestration-with-typer` — Expose pipelines through a deterministic CLI interface that orchestrates validated stages without embedding logic.
- `co-06-content-generation-layer` — Generate Markdown artifacts from validated SSOT models using deterministic templates and stable rendering rules.
- `co-07-verification-and-tooling` — Enforce correctness and stability with ruff, mypy, and pytest; verify contracts and transformations.

## Content blocks

- `co-01-python-core-for-operators-drill.json`
- `co-01-python-core-for-operators-theory.json`
- `co-02-typed-boundary-contracts-drill.json`
- `co-02-typed-boundary-contracts-theory.json`
- `co-03-pydantic-contract-layer-drill.json`
- `co-03-pydantic-contract-layer-theory.json`
- `co-04-repo-structure-and-import-discipline-drill.json`
- `co-04-repo-structure-and-import-discipline-theory.json`
- `co-05-cli-orchestration-with-typer-drill.json`
- `co-05-cli-orchestration-with-typer-theory.json`
- `co-06-content-generation-layer-drill.json`
- `co-06-content-generation-layer-theory.json`
- `co-07-verification-and-tooling-drill.json`
- `co-07-verification-and-tooling-theory.json`
