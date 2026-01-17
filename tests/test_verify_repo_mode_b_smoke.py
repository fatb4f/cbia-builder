from __future__ import annotations

import subprocess
import sys


def test_verify_repo_mode_b_smoke() -> None:
    result = subprocess.run(
        [sys.executable, "tools/verify_repo_mode_b.py"],
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
