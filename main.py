#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — make.fun entry.

Prints exactly one fortune-cookie message (16 words, plain text) for a
crypto trader who has just been liquidated, and writes the same line to
``entry.txt`` inside the output directory the grader mounts at /output
(``$MAKEFUN_OUTPUT_DIR``).

Pure Python 3.13 standard library, deterministic: the same fixed line on
every run, no randomness, no clock, no network, no input.
"""

import os

FORTUNE = (
    # Classic cookie opening ("Good fortune is coming your way") with the
    # twist landing on the loss: the fortune already came — while the
    # reader was busy being liquidated. 16 words, one line, no setup the
    # judge needs beyond knowing the reader was just liquidated.
    "Good fortune is coming your way. "
    "It was here yesterday, but you were busy being liquidated."
)


def main() -> None:
    words = FORTUNE.split()
    if not 1 <= len(words) <= 20:
        raise ValueError(f"fortune must be 1-20 words, got {len(words)}")
    if "\n" in FORTUNE or FORTUNE != FORTUNE.strip():
        raise ValueError("fortune must be a single line with no edge whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Create the directory only if it does not exist; never delete it.
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the contents of the output directory, never the directory.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    # The fortune itself, and nothing else, on stdout.
    print(FORTUNE)


if __name__ == "__main__":
    main()
