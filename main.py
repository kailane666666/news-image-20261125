"""Ship the news image: copy entry.png into the output directory."""

from os import environ
from pathlib import Path
import hashlib
import sys

SOURCE = Path(__file__).resolve().parent / "entry.png"
TARGET_DIR = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = TARGET_DIR / "entry.png"
CHUNK = 1 << 16


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            block = f.read(CHUNK)
            if not block:
                break
            h.update(block)
    return h.hexdigest()


TARGET_DIR.mkdir(parents=True, exist_ok=True)
TARGET.write_bytes(SOURCE.read_bytes())
if digest(SOURCE) != digest(TARGET):
    print("copy failed: output differs from entry.png", file=sys.stderr)
    sys.exit(1)
