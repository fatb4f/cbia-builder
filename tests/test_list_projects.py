from pathlib import Path
import subprocess
import sys

def test_list_projects_runs():
    root = Path(__file__).resolve().parents[1]
    p = subprocess.run([sys.executable, str(root / "scripts" / "list_projects.py")], capture_output=True, text=True)
    assert p.returncode == 0
    assert "cbia-content" in p.stdout
