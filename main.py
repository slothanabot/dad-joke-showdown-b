#!/usr/bin/env python3
"""Dad Joke Showdown entry (make.fun program/v1).

Writes one original dad joke to ``<MAKEFUN_OUTPUT_DIR>/entry.txt``
(the grader mounts that directory at ``/output``). The joke is a fixed
string literal: no network, no randomness, no input, so every run
produces byte-identical output.
"""

import os
import sys

JOKE = (
    "I told my smart fridge to stop judging my midnight snacks. "
    "It said, 'Dad, I'm not judging, I'm just keeping everything "
    "cool between us.'"
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
