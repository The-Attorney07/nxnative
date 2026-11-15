import subprocess
import sys

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GAME_DIR = Path.home() / "Games" / "DungeonsII"
BUILD_DIR = ROOT / "Scripts" / "build_ipa_from_nsp.py"

print(f"Repository located at: {ROOT}")

if GAME_DIR.is_dir():
    print(f"Game directory found at: {GAME_DIR}")
else:
    print(f"Game directory not found at: {GAME_DIR}")

if BUILD_DIR.is_file():
    print(f"Build script found at: {BUILD_DIR}")
else:
    print(f"Build script not found at: {BUILD_DIR}")