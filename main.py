#!/usr/bin/env python3
"""The Vacuum's Alibi entry for make.fun.

u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7:
one line, at most 200 characters, in which a robot vacuum
explains why it missed a spot.

Writes exactly that one line to /output/entry.txt.
"""

from pathlib import Path

DESTINATION = Path("/output/entry.txt")

# The vacuum's alibi, in its own deadpan voice: its cliff sensor
# misread the spot, it does not do stairs, and its warranty
# draws the line at heroics.
ALIBI = (
    "Cliff sensor flagged the spot as stairs. "
    "I do not vacuum stairs. "
    "My warranty does not cover heroics."
)


def deliver_alibi() -> str:
    """Write the alibi line to the output file and return it."""
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(ALIBI, encoding="utf-8")
    return ALIBI


if __name__ == "__main__":
    print(deliver_alibi())
