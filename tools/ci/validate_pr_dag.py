#!/usr/bin/env python3
"""PR DAG + non-regression validator (CI)

This validator is a *supervisory guard* over repository changes.
It does NOT control generation; it prevents regressions in the Control Kernel / OPA gate semantics.

Intended usage (GitHub Actions):
  python tools/ci/validate_pr_dag.py

Inputs:
- the checked-out repository workspace
- (optional) environment variables provided by CI:
    - BASE_REF (preferred base ref)
    - HEAD_REF (preferred head ref)
- (optional) CLI overrides:
    - --base-ref
    - --head-ref
    - --print-resolved-refs
    - --skip-control-map-regen

Hard rules:
- protected files must not be deleted
- assurance policy must define `default allow = false` AND an `allow { ... }` rule
- PR log must exist (docs/pr/PR_LOG.md) to keep GPT-targeted review scope contained
"""

from __future__ import annotations
import argparse, os, re, json, subprocess, sys
from pathlib import Path
from typing import List, Tuple

ROOT = Path(__file__).resolve().parents[2]

def run(cmd: List[str]) -> str:
    p = subprocess.run(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if p.returncode != 0:
        print(p.stdout)
        raise SystemExit(p.returncode)
    return p.stdout.strip()

def rev_parse_ok(ref: str) -> bool:
    p = subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", ref],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    return p.returncode == 0

def _run_no_fail(cmd: List[str]) -> str:
    p = subprocess.run(
        cmd,
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    return p.stdout.strip()

def resolve_head_ref(cli_head: str | None) -> str:
    if cli_head:
        if rev_parse_ok(cli_head):
            return cli_head
        raise SystemExit(f"HEAD_REF does not resolve: {cli_head}")
    head_env = os.environ.get("HEAD_REF")
    if head_env:
        if rev_parse_ok(head_env):
            return head_env
        raise SystemExit(f"HEAD_REF does not resolve: {head_env}")
    return "HEAD"

def resolve_base_ref(cli_base: str | None) -> str:
    if cli_base:
        if rev_parse_ok(cli_base):
            return cli_base
        raise SystemExit(f"BASE_REF does not resolve: {cli_base}")

    base_env = os.environ.get("BASE_REF")
    if base_env:
        if rev_parse_ok(base_env):
            return base_env
        raise SystemExit(f"BASE_REF does not resolve: {base_env}")

    github_base = os.environ.get("GITHUB_BASE_REF")
    if github_base:
        origin_ref = f"origin/{github_base}"
        if rev_parse_ok(origin_ref):
            return origin_ref
        if rev_parse_ok(github_base):
            return github_base

    if rev_parse_ok("origin/main"):
        return "origin/main"
    if rev_parse_ok("main"):
        return "main"
    if rev_parse_ok("master"):
        return "master"

    branches = _run_no_fail(["git", "branch", "-a"])
    remotes = _run_no_fail(["git", "remote", "-v"])
    raise SystemExit(
        "Unable to resolve BASE_REF. Set BASE_REF to a valid ref/SHA.\n"
        f"git branch -a:\n{branches}\n"
        f"git remote -v:\n{remotes}"
    )

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

def regen_control_maps() -> None:
    run([sys.executable, "tools/ci/regen_control_maps.py"])

def check_control_maps_clean() -> None:
    run(
        [
            "git",
            "diff",
            "--exit-code",
            "--",
            "control/plant/plant.mmd",
            "control/plant/execution_dag.json",
        ]
    )

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
    parser = argparse.ArgumentParser(description="Validate PR DAG invariants")
    parser.add_argument("--base-ref", help="Override base ref (takes precedence over env)")
    parser.add_argument("--head-ref", help="Override head ref (takes precedence over env)")
    parser.add_argument(
        "--print-resolved-refs",
        action="store_true",
        help="Print resolved base/head refs and exit",
    )
    parser.add_argument(
        "--skip-control-map-regen",
        action="store_true",
        help="Skip control-map regeneration and diff check",
    )
    args = parser.parse_args()

    contract = load_contract()
    must_exist(contract["pr_log_required"])

    base = resolve_base_ref(args.base_ref)
    head = resolve_head_ref(args.head_ref)

    if args.print_resolved_refs:
        print(f"base={base} head={head}")
        return

    if not args.skip_control_map_regen:
        regen_control_maps()
        check_control_maps_clean()

    _, deleted = git_changed_files(base, head)

    for rel in contract["protected_files"]:
        if rel in deleted:
            raise SystemExit(f"Protected file deleted: {rel}")

    check_assurance_invariants()
    check_runner_not_stub()

    print("PR DAG validation: PASS")

if __name__ == "__main__":
    main()
