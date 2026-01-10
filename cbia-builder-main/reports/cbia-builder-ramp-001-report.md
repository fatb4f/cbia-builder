# CBIA Builder Extraction + Validation Report — ramp-001 (v0.2)

## 1) Extracted builder-owned elements
- Project created at: `cbia-contentless/ramp-001/`
- Constraints: `constraints/ssot-input/` + `constraints/index.md`
- Schemas: `schemas/{course,content_block,references}.schema.json`
- Material: `material/index.md` + `material/modules/*` (normalized)

## 2) Schema + defined-content validation (jsonschema)
- ✅ `course.json`: ok
- ✅ `references.json`: ok
- ✅ `content/co-01-python-core-for-operators-drill.json`: ok
- ✅ `content/co-01-python-core-for-operators-theory.json`: ok
- ✅ `content/co-02-typed-boundary-contracts-drill.json`: ok
- ✅ `content/co-02-typed-boundary-contracts-theory.json`: ok
- ✅ `content/co-03-pydantic-contract-layer-drill.json`: ok
- ✅ `content/co-03-pydantic-contract-layer-theory.json`: ok
- ✅ `content/co-04-repo-structure-and-import-discipline-drill.json`: ok
- ✅ `content/co-04-repo-structure-and-import-discipline-theory.json`: ok
- ✅ `content/co-05-cli-orchestration-with-typer-drill.json`: ok
- ✅ `content/co-05-cli-orchestration-with-typer-theory.json`: ok
- ✅ `content/co-06-content-generation-layer-drill.json`: ok
- ✅ `content/co-06-content-generation-layer-theory.json`: ok
- ✅ `content/co-07-verification-and-tooling-drill.json`: ok
- ✅ `content/co-07-verification-and-tooling-theory.json`: ok

Total jsonschema errors: **0**

## 3) Learning material validation
- ✅ `material/index.md`
- ✅ `modules/co-01-python-core-for-operators`
- ✅ `modules/co-02-typed-boundary-contracts`
- ✅ `modules/co-03-pydantic-contract-layer`
- ✅ `modules/co-04-repo-structure-and-import-discipline`
- ✅ `modules/co-05-cli-orchestration-with-typer`
- ✅ `modules/co-06-content-generation-layer`
- ✅ `modules/co-07-verification-and-tooling`

## 4) Content-data modifications applied
- Removed `material/_dist_snapshot/` after normalization (keeps builder tree clean).
- Merged `co-05-cli-orchestration-with-typer/{DRILLS_1,THEORY_1}.md` into `{DRILLS,THEORY}.md`.
- Generated missing `co-06-content-generation-layer/{THEORY,DRILLS}.md` from `constraints/ssot-input/content/*.json`.

## 5) cbia-builder compliance artifacts generated
- `constraints/index.md`
- `schemas/*.schema.json`
- `material/index.md` (from dist `INDEX.md`)
- `manifests/stage.json` (material stage + hashes)
