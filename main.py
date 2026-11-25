#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes the phone battery's final text message to its charger as a single
line of plain text (at most 200 characters) to /output/entry.txt and
prints it to stdout.
"""

import os

MAX_CHARS = 200

LINE = (
    "1% left. I waited all day and you show up NOW? "
    "Plug me in before I die mid-sentence - love, your battery."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    line = LINE.strip()
    assert line, "entry line must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert len(line) <= MAX_CHARS, "entry must be at most 200 characters"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")

    print(line)
    print(f"({len(line)} characters)")


if __name__ == "__main__":
    main()
