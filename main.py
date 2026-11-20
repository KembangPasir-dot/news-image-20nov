"""Copy the bundled entry.png to /output/entry.png."""

import hashlib
import os
import shutil
from pathlib import Path

IMAGE_NAME = "entry.png"
BASE_DIR = Path(__file__).resolve().parent
SRC = BASE_DIR / IMAGE_NAME
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    destination = OUT_DIR / IMAGE_NAME
    shutil.copyfile(SRC, destination)
    if not destination.is_file():
        raise ValueError("Destination copy does not exist")
    size = destination.stat().st_size
    if size != SRC.stat().st_size:
        raise ValueError("Destination size differs from source")
    with SRC.open("rb") as source:
        source_sha256 = hashlib.file_digest(source, "sha256").hexdigest()
    with destination.open("rb") as copied:
        sha256 = hashlib.file_digest(copied, "sha256").hexdigest()
    if sha256 != source_sha256:
        raise ValueError("Destination SHA-256 differs from source")
    return destination, size, sha256


if __name__ == "__main__":
    destination, size, sha256 = main()
    print(f"{destination.name}: {size} bytes, SHA-256 {sha256}")

