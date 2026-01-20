import os
import sys
from pathlib import Path

def replace_in_file(path: Path, old: str, new: str):
    text = path.read_text()
    path.write_text(text.replace(old, new))

def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/init_service.py <service_name>")
        sys.exit(1)

    service_name = sys.argv[1]
    repo_root = Path(__file__).resolve().parents[1]

    print(f"Initializing service: {service_name}")

    # Files where service name appears
    files_to_update = [
        repo_root / "pyproject.toml",
        repo_root / ".env.example",
        repo_root / "README.md",
    ]

    for file in files_to_update:
        if file.exists():
            replace_in_file(file, "fastapi-service-template", service_name)
            replace_in_file(file, "example-service", service_name)

    # Remove git history
    git_dir = repo_root / ".git"
    if git_dir.exists():
        print("Removing existing git history")
        for root, dirs, files in os.walk(git_dir, topdown=False):
            for name in files:
                os.remove(Path(root) / name)
            for name in dirs:
                os.rmdir(Path(root) / name)
        os.rmdir(git_dir)

    print("Done.")
    print("Next steps:")
    print("  git init")
    print("  cp .env.example .env")
    print("  make install")
    print("  make migrate")
    print("  make dev")

if __name__ == "__main__":
    main()
