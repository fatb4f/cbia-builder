# INF1250 Workbench (v0.1.0)

Operational layer for INF1250 using:
- Jupyter / IPython kernel
- DuckDB
- Jupytext Markdown notebooks (canonical source)
- A minimal Python lens (`inf1250_lens`) to enforce 3P and ACS framing (stubs only in v0.1.0)

This workbench contains no curriculum content.
It exists solely as an execution and evidence surface for TP work.

---

## Layout

notebooks/
- Jupytext .md notebooks (canonical)
- m2/00-m2-workpad.md
- tp2/00-tp2-workpad.md

src/inf1250_lens/
- Python lens package
- API signatures frozen
- All functions are stubs in v0.1.0

sql/fixtures/
- Optional SQL snippets / fixtures

data/
- Local DuckDB file target
- Database artifacts must not be committed

docs/
- Workbench documentation

---

## Setup (minimal)

From workbench/inf1250/:

Commands:
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .

---

## Kernel registration (optional)

Commands:
python -m ipykernel install --user --name inf1250-workbench --display-name "INF1250 Workbench"

---

## Running notebooks

Commands:
jupytext --sync notebooks/**/*.md
jupyter lab

---

## Same-kernel REPL (preferred)

Command:
jupyter console --existing

Preferred over ptpython for attaching to a live notebook kernel.

---

## 3P + ACS discipline (per exercise)

Each workpad includes fixed sections.

3P:
- Computation:
- Inference:
- Control:

ACS:
- Plant:
- Controller:
- Sensors:
- Actuators:
- Constraints:
- Feedback rule:

In v0.1.0 these are templates only.

---

## Versioning

- The workbench is versioned independently from course content.
- v0.1.0 provides:
  - Stable directory layout
  - Frozen API signatures
  - No functional lens implementation
