#!/usr/bin/env python3
"""PR DAG + non-regression validator (CI)

This validator is a *supervisory guard* over repository changes.
It does NOT control generation; it prevents regressions in the Control Kernel / OPA gate semantics.

Intended usage (GitHub Actions):
  python tools/ci/validate_pr_dag.py

Inputs:
- the checked-out repository workspace
- (optional) environment variables provided by CI:
    - BASE_REF (default: origin/main)
    - HEAD_REF (default: HEAD)

Hard rules:
- protected files must not be deleted
- assurance policy must define `default allow = false` AND an `allow { ... }` rule
- PR log must exist (docs/pr/PR_LOG.md) to keep GPT-targeted review scope contained
"""

from __future__ import annotations
import os, re, json, subprocess, sys
from pathlib import Path
from typing import List, Tuple

ROOT = Path(__file__).resolve().parents[2]

def run(cmd: List[str]) -> str:
    p = subprocess.run(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if p.returncode != 0:
        print(p.stdout)
        raise SystemExit(p.returncode)
    return p.stdout.strip()

def git_changed_files(base: str, head: str) -> Tuple[List[str], List[str]]:
    out = run(["git", "diff", "--name-status", f"{base}...{head}"])
    added, deleted = [], []
    for line in out.splitlines():
        if not line.strip():
            continue
        status, path = line.split("\t", 1)
        if status.startswith("A"):
            added.append(path)
        elif status.startswith("D"):
            deleted.append(path)
    return added, deleted

def must_exist(rel: str) -> None:
    p = ROOT / rel
    if not p.exists():
        raise SystemExit(f"Missing required file: {rel}")

def load_contract() -> dict:
    p = ROOT / "control/pr/pr.contract.json"
    must_exist(str(p.relative_to(ROOT)))
    return json.loads(p.read_text(encoding="utf-8"))

def check_assurance_invariants() -> None:
    p = ROOT / "policy/assurance/assurance.rego"
    must_exist(str(p.relative_to(ROOT)))
    txt = p.read_text(encoding="utf-8")
    if "default allow = false" not in txt:
        raise SystemExit("assurance.rego invariant failed: missing `default allow = false`")
    if not re.search(r"\ballow\s*\{", txt):
        raise SystemExit("assurance.rego invariant failed: missing `allow { ... }` rule")
    for key in ["evidence_materialized", "promotion_admissible"]:
        if key not in txt:
            raise SystemExit(f"assurance.rego invariant failed: missing `{key}` gate")

def check_runner_not_stub() -> None:
    p = ROOT / "tools/run_pipeline.py"
    must_exist(str(p.relative_to(ROOT)))
    txt = p.read_text(encoding="utf-8")
    must_have = ["def assurance_eval", "def opa_gate", "pre_gen_capsule", "opa/decision.json"]
    for s in must_have:
        if s not in txt:
            raise SystemExit(f"run_pipeline.py regression guard failed: missing `{s}`")

def main() -> None:
    contract = load_contract()
    must_exist(contract["pr_log_required"])

    base = os.environ.get("BASE_REF", "origin/main")
    head = os.environ.get("HEAD_REF", "HEAD")

    _, deleted = git_changed_files(base, head)

    for rel in contract["protected_files"]:
        if rel in deleted:
            raise SystemExit(f"Protected file deleted: {rel}")

    check_assurance_invariants()
    check_runner_not_stub()

    print("PR DAG validation: PASS")

if __name__ == "__main__":
    main()
