#!/usr/bin/env python3
import random
from pathlib import Path

def main():
    repo_root = Path(__file__).resolve().parent.parent
    prompts_file = Path(__file__).resolve().parent / 'prompts.txt'
    profile_file = repo_root / 'PROFILE.md'

    prompts = [line.strip() for line in prompts_file.read_text().splitlines() if line.strip()]
    prompt = random.choice(prompts)

    content = [
        'Welcome to my GitHub profile!',
        '',
        f'> {prompt}',
    ]
    profile_file.write_text('\n'.join(content) + '\n')

if __name__ == '__main__':
    main()
