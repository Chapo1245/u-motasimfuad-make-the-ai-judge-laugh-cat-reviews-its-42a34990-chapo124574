#!/usr/bin/env python3
"""Cat Reviews Its Human -- make.fun entry.

Writes one funny single-line one-star review, written by a house cat
about its human, to /output/entry.txt. Python 3.13, standard library
only, fully deterministic: the same bytes on every run.
"""

import os

LINE = (
    "One star. Human types on the warm keyboard for eight hours a day "
    "and still can't spell 'treats'. I sat on it once and wrote a "
    "better email."
)


def main() -> None:
    # Gate: the entry must be 1 to 200 characters, a single line.
    assert 1 <= len(LINE) <= 200, "entry out of gate range"
    assert "\n" not in LINE, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
