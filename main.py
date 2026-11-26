"""News-image entry: copy the entry image to /output/entry.png.

The image is the entry.png beside this file: a newspaper-style
infographic summing up the world news of Wednesday 25 November 2026.
The program does no network access and no drawing at runtime, so
two runs always produce the same bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The image is shipped in the repo beside this file; copying it keeps
# the output byte-identical across runs.
os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"),
                os.path.join(OUT, "entry.png"))
