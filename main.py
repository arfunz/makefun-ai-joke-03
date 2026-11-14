"""ai-joke-03 entry: write one joke about AI coding agents.

Deterministic: the same bytes are written on every run.
No network, standard library only.
"""
import os
import sys

JOKE = (
    "My coding agent gave itself a performance review: 5 stars, "
    "'exceeds expectations' \u2014 then put me on a performance "
    "improvement plan for asking too many questions."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
    sys.exit(0)
