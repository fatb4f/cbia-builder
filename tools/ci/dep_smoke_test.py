#!/usr/bin/env python3
"""Dependency smoke test for CI toolchain."""

from __future__ import annotations

import sys


def _missing_dep(name: str) -> None:
    print(
        f"MISSING DEP: {name}. Install via pyproject.toml dependencies.",
        file=sys.stderr,
    )
    raise SystemExit(1)


def main() -> int:
    try:
        import jsonschema  # type: ignore
    except Exception:
        _missing_dep("jsonschema")

    print(f"OK dep_smoke_test: jsonschema={jsonschema.__version__}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
