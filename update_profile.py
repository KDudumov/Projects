import pathlib

def main():
    prompts_path = pathlib.Path('prompts.txt')
    profile_path = pathlib.Path('PROFILE.md')
    profile_path.write_text(prompts_path.read_text())

if __name__ == '__main__':
    main()
