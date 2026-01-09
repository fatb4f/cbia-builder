
# agents.md — Pre‑Generative Control Kernel (PR)

## Mandatory PRE‑GEN Gate
All execution is blocked until the Control Kernel evaluates to **ALLOW**.

### Controllers
- Authority Controller (OPA)
- Inference Controller (OPA)
- Dependency Closure Controller (OPA)
- Execution DAG Controller

### Decision Surface
Only `data.control.kernel.allow == true` permits entry into GEN.

---

## PRE‑GEN
- Assemble control_state.json
- Evaluate OPA policies
- Emit control.explain.json

## GEN → STRUCT → SELECT → FLOW → EVAL
All phases operate strictly within the admissible state space declared by the Control Kernel.
No phase may introduce new authority, objectives, or dependencies.
