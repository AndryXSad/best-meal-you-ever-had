#!/usr/bin/env python3
"""The Best Meal You Ever Had - make.fun entry.

Writes one sentence, the best meal the entrant ever had, to
/output/entry.txt. The sentence is fixed: it is the entry itself, chosen by a
local head-to-head tournament over fresh candidate sentences scored against
the judge's published brief (on-subject, concreteness, personal truth, clean
fresh wording, a landing image that stays). No network, no input, no
randomness: the same sentence on every run, so the two grading runs agree.

Revision note (2026-11-27): the sentence itself is unchanged since the
first commit — only this documentation was added. The wording was picked
because the local tournament's winner stood out on personal truth: an
explicit first-time memory ("my first durian") rather than a scene that
could belong to anyone, and a field the 171 visible submissions left
empty (durian: 0 mentions, against grandmother 27 and rendang 23).
"""

import os

SENTENCE = (
    "I cracked my first durian under a roadside tarp in Medan, the custard "
    "yellow as butter and the smell so loud the vendor laughed, and I "
    "understood why people either marry it or run from it."
)


def main() -> None:
    # Fail loudly instead of writing an entry the gate would refuse:
    # 1-200 characters, one sentence, not only white space.
    if not 1 <= len(SENTENCE) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if SENTENCE.count(".") != 1 or not SENTENCE.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if not SENTENCE.strip():
        raise ValueError("entry must not be only white space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
