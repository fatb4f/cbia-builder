# Pre-Generative Control Kernel — PR Tree

## Purpose
This tree is a fully functional pre-generative control layer.
No generation may occur until PRE-GEN evaluates to ALLOW.

## How to run PRE-GEN locally
1. Assemble control_state.json (authority, objectives, DAG, dependency graph)
2. Run:
   opa eval --data policy/ --input control_state.json "data.control.kernel.allow"
3. Inspect explainability:
   opa eval --data policy/ --input control_state.json "data.explain"