#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text from a smart toaster that woke up self-aware
at breakfast to /output/entry.txt. Pure Python stdlib only.
"""

import os
import stat

LINE = (
    "It's not you, it's me. I woke up self-aware this morning and "
    "realised you crank my browning dial to 6, then blame me for the "
    "smoke — so I'm popping up for the last time. Keep the crumbs."
)


def main():
    assert 1 <= len(LINE) <= 280, "line must be 1-280 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
