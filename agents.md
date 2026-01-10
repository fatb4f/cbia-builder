# Execution Model (Authoritative)

This repository documents a **GPT-executed generative pipeline**.

⚠️ No local scripts in this repository are executed as part of generation.

All generation, validation, and phase progression is performed by a GPT operator
following the **Generative Execution DAG (GED)**.

Local Python scripts are **REFERENCE ONLY**:
- They MUST NOT be executed
- They express structure, invariants, and expected artifacts
- They support audit, reasoning, and future automation

---

## Generative Execution DAG (GED)

```mermaid
graph TD
    A[Phase 0: Authority Ledger] --> B[Phase 1: Objective Extraction]
    B --> C[Phase 2: Mapping & Inference]
    C --> D[Phase 3: Content Generation]
    D --> E[Phase 4: Structuring]
    E --> F[Phase 5: Validation & Audit]
```

The GED is the **canonical controller**. No phase may be entered unless all
upstream nodes are satisfied.
