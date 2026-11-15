import subprocess
import sys

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GAME_DIR = Path.home() / "Games" / "DungeonsII"
BUILD_DIR = ROOT / "scripts" / "build_ipa_from_nsp.py"

print(f"Repository located at: {ROOT}")

def main():
    if not GAME_DIR.is_dir():
        print("Game directory not found!")
        return 1

    if not BUILD_DIR.is_file():
        print("Builder script not found!")
        return 1

    print("Ready to build!")
    return 0

command = [
    sys.executable,
    str(BUILD_DIR),
    str(GAME_DIR)
]

result = subprocess.run(command)
result.returncode

if __name__ == "__main__":
    sys.exit(main())

