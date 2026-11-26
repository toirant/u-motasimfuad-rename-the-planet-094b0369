#!/usr/bin/env python3
"""Rename the Planet — make.fun entry.

Writes one funny line to /output/entry.txt: a new name for Mercury
plus the why, in a single line under 200 characters.
"""

import os

ENTRY = (
    "Mercury is now 'The Intern' \u2014 it crams a whole year "
    "into 88 days and still doesn't get paid."
)


def main() -> None:
    # Gate self-check: the entry must be 1-200 chars, non-whitespace.
    if not (1 <= len(ENTRY) <= 200) or not ENTRY.strip():
        raise SystemExit("entry fails the 1-200 char gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
