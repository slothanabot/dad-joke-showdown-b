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
    # Gate guard: the sealed scorer only accepts UTF-8 text of 1-200
    # characters, not only whitespace, on a single line. Refuse to write
    # anything that fails the gate instead of producing an invalid entry.
    if not JOKE or len(JOKE) > 200 or "\n" in JOKE or not JOKE.strip():
        print(
            "gate guard: joke must be one line of 1-200 non-whitespace "
            "characters",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
