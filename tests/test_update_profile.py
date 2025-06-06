import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'update_profile.py'


def test_update_profile(tmp_path):
    prompts = 'Test content\nLine 2'
    (tmp_path / 'prompts.txt').write_text(prompts)
    subprocess.run([sys.executable, str(SCRIPT)], cwd=tmp_path, check=True)
    result = (tmp_path / 'PROFILE.md').read_text()
    assert result == prompts
