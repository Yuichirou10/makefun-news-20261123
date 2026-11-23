import os
import shutil
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().with_name("entry.png")
    destination = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.png"))

    os.umask(0o022)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    destination.chmod(0o644)


if __name__ == "__main__":
    main()
