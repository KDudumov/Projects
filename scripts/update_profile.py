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
    prompt = random.choice(lines)
    content = [
        "Welcome to my GitHub profile!",
        "",
        f"> {prompt}",
        "",
        f"Updated {datetime.utcnow().isoformat()} UTC",
    ]
    PROFILE.write_text("\n".join(content) + "\n")


if __name__ == "__main__":
    main()
