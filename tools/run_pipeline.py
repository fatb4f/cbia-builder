#!/usr/bin/env python3
"""cbia-builder pipeline runner (entrypoint)."""

import argparse
import os
import sys
from typing import Any, Dict

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from tools import pipeline_driver
from tools.pipeline_driver import PipelineDriver


def assurance_eval(input_bundle: Dict[str, Any]) -> Dict[str, Any]:
    """Regression guard requires this symbol."""
    allow, explain = pipeline_driver.assurance_eval(input_bundle)
    decision = {"result": [{"expressions": [{"value": allow}]}]}
    return {
        "allow": allow,
        "decision": decision,
        "explain": {"explain": explain, "allow": allow},
    }


def opa_gate(
    pre_gen_capsule: Dict[str, Any],
    run_ledger: list[Dict[str, Any]],
    artifact_hashes: Dict[str, str],
) -> None:
    """Regression guard requires this symbol. Writes opa/decision.json."""
    pipeline_driver.opa_gate(pre_gen_capsule, run_ledger, artifact_hashes)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the cbia-builder pipeline")
    parser.add_argument("--dry-run", action="store_true", help="Run PRE_GEN + OPA only")
    parser.add_argument(
        "--out-dir",
        help="Output directory for dry-run artifacts (default: execution/tmp/latest)",
    )
    args = parser.parse_args()

    driver = PipelineDriver()
    out_dir = args.out_dir
    if args.dry_run and not out_dir:
        out_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "execution", "tmp", "latest"
        )
    return driver.run(dry_run=args.dry_run, out_dir=out_dir)


if __name__ == "__main__":
    raise SystemExit(main())
