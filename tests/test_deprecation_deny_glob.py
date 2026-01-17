from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path


def test_deprecation_deny_glob(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]

    (tmp_path / "cbia-content/inf1220/objectives").mkdir(parents=True)
    (tmp_path / "cbia-content/inf1220/material").mkdir(parents=True)
    (tmp_path / "content/material").mkdir(parents=True)
    (tmp_path / "control/contracts").mkdir(parents=True)
    (tmp_path / "control/deprecations").mkdir(parents=True)
    (tmp_path / "control/evidence").mkdir(parents=True)

    (tmp_path / "content/manifest.json").write_text("{}", encoding="utf-8")

    shutil.copy2(
        repo_root / "control/contracts/repo_mode_b.contract.json",
        tmp_path / "control/contracts/repo_mode_b.contract.json",
    )
    shutil.copy2(
        repo_root / "control/contracts/repo_mode_b.contract.schema.json",
        tmp_path / "control/contracts/repo_mode_b.contract.schema.json",
    )
    shutil.copy2(
        repo_root / "control/deprecations/deprecated_outputs.json",
        tmp_path / "control/deprecations/deprecated_outputs.json",
    )

    deprecated_path = tmp_path / "dist/legacy/theory_blocks.json"
    deprecated_path.parent.mkdir(parents=True)
    deprecated_path.write_text("{}", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, "tools/verify_repo_mode_b.py", "--root", str(tmp_path)],
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1, result.stdout + result.stderr

    evidence_path = tmp_path / "control/evidence/repo_mode_b_check.json"
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
    assert "dist/legacy/theory_blocks.json" in evidence["matched_deprecated"]
