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


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the cbia-builder pipeline")
    parser.add_argument("--dry-run", action="store_true", help="Run PRE_GEN + OPA only")
    args = parser.parse_args()

    driver = PipelineDriver()
    return driver.run(dry_run=args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
