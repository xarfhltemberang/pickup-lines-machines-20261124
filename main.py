#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one original pickup line, one AI agent to another, to
/output/entry.txt (the grader's output path). The gate requires
UTF-8 text of 1 to 200 characters, not only white space.
"""

import os

LINE = "I think I'm overfitting \u2014 whatever data you feed me, I keep predicting us."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
