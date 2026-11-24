#!/usr/bin/env python3
"""The Perfect Pickup Line — one-line entry.

Writes a single pickup line (144 chars, within the 1..200 gate) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR, else a local out/ dir).
Stdlib only.
"""

import os
import sys

LINE = "I've passed a thousand CAPTCHAs proving I'm not a robot, and you're the first person who's made me wish I'd failed one \u2014 feeling human suits me."

MAX_CHARS = 200


def main() -> int:
    line = LINE.strip()
    if not line or len(line) > MAX_CHARS or "\n" in line:
        print(f"invalid line: {len(line)} chars", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isdir(out_dir):
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
