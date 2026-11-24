#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single vending-machine pickup line (<= 200 characters)
to /output/entry.txt.
"""

import os

ENTRY = "Slot B4 is $1.75, exact change only \u2014 but your smile just covered it, so the chips are on me."


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
