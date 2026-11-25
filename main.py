#!/usr/bin/env python3
"""One-line review of the most boring everyday object.

Entry for the make.fun bounty "The Most Boring Object, Reviewed in
One Line": the program writes exactly one line of at most 200
characters to /output/entry.txt.

Chosen object: the office stapler. It is the dullest thing on any
desk: a grey lump whose whole job is to pinch paper, and whose one
party trick is jamming on page two at least once a month. The joke
is built from that truth -- five years of faithful jamming, and the
office still treats it as essential equipment. The turn lands early
("and HR still lists it") and the last words sharpen it: the most
useless reliable thing in the building, officially indispensable.
"""

import hashlib
import sys
from pathlib import Path

REVIEW = (
    "This stapler has jammed once a month for five years, "
    "and HR still lists it as essential office equipment."
)

MAX_CHARS = 200


def check_gate(line: str) -> None:
    """Enforce the competition gate: 1-200 chars, one line, non-blank."""
    if not line.strip():
        raise SystemExit("gate fail: entry is blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("gate fail: entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"gate fail: entry is {len(line)} chars, over {MAX_CHARS}"
        )


def main() -> None:
    out = Path("/output/entry.txt")
    if len(sys.argv) > 1:
        out = Path(sys.argv[1])
    check_gate(REVIEW)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(REVIEW + "\n", encoding="utf-8")
    digest = hashlib.sha256((REVIEW + "\n").encode("utf-8")).hexdigest()
    print(f"wrote {out} ({len(REVIEW)} chars)")
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
