#!/usr/bin/env python3
"""Regenerate deterministic control-map artifacts."""

from __future__ import annotations

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

sys.path.insert(0, os.path.join(ROOT, "tools"))

import gen_control_maps  # noqa: E402


def main() -> int:
    gen_control_maps.main()
    print("Regenerated control maps.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
