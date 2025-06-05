#!/usr/bin/env python3
"""Update PROFILE.md with a random message."""
import random
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
PROMPTS = ROOT / "prompts.txt"
PROFILE = ROOT / "PROFILE.md"

def main() -> None:
    lines = [line.strip() for line in PROMPTS.read_text().splitlines() if line.strip()]
    if not lines:
        raise SystemExit("No prompts found in prompts.txt")
    message = random.choice(lines)
    PROFILE.write_text(f"{message}\n\nUpdated {datetime.utcnow().isoformat()} UTC\n")

if __name__ == "__main__":
    main()
