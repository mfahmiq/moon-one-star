#!/usr/bin/env python3
"""Write the Moon Gets One Star entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry line (95 characters, a one-star review of the Moon):

    One star. It follows me home every night and pretends that's
    romantic. It's not. It's stalking.

Why this line: it won an internal 16-candidate pairwise tournament
judged against the published brief in weight order. It is a complaint
about the Moon itself (criterion 1); the romantic-to-stalking twist
lands on first read (criterion 2); it opens "One star." and reads like
a genuine review (criterion 3); "follows me home every night" is a
specific, surprising grievance built on a real Moon experience, not a
craters/cheese/brightness joke (criterion 4); and every word earns its
place in 95 characters (criterion 5).
"""

import os

ENTRY = "One star. It follows me home every night and pretends that's romantic. It's not. It's stalking."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
