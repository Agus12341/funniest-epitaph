#!/usr/bin/env python3
"""Write the one-line epitaph to entry.txt in the output folder."""

import os

# Famous last words for a tombstone: picked from five drafts judged
# pairwise on the kit's criteria (epitaph first, then a real laugh, a
# clean twist, reads carved in stone, quotable). "Watch this" is the
# archetypal last-words setup; the payoff is that this time he had an
# audience. The gate checks entry.txt as UTF-8 text of 1 to 150
# characters: this line is 49 code points, 50 with its trailing
# newline (verified by a local run).
TEXT = "He said 'watch this' and, for once, everyone did."


def write_entry(out_dir: str) -> None:
    """Write the epitaph, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
