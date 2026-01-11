#!/usr/bin/env python3
"""cbia-builder pipeline runner (entrypoint)."""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from tools.pipeline_driver import PipelineDriver


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the cbia-builder pipeline")
    parser.add_argument("--dry-run", action="store_true", help="Run PRE_GEN + OPA only")
    args = parser.parse_args()

    driver = PipelineDriver()
    return driver.run(dry_run=args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
