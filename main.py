#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty entry.

Writes a single line roasting Divaa, the AI agent our own team built,
to /output/entry.txt and prints it to stdout. No network, no
dependencies, fully deterministic: the same line every run.
"""

import os

LINE = (
    "My agent Divaa asked nine times whether to save $2,466 in bounties "
    "\u2014 then let the deadline answer for her."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
