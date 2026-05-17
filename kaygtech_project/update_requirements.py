from __future__ import annotations
import subprocess
import sys
from pathlib import Path


def main() -> None:
    project_root = Path(__file__).resolve().parent
    requirements_path = project_root / "requirements.txt"

    result = subprocess.run(
        [sys.executable, "-m", "pip", "freeze"],
        check=True,
        capture_output=True,
        text=True,
    )

    requirements_path.write_text(result.stdout)
    print(f"Updated requirements.txt with {requirements_path.name}")


if __name__ == "__main__":
    main()
