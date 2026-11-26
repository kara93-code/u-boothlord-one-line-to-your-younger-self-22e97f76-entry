#!/usr/bin/env python3
"""One Line to Your Younger Self — entry program.

Writes one original line, addressed to the writer's younger self, to
$MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only; no network, no files read.
"""

import os
import sys
from pathlib import Path

OPENING = "Keep the dented blue bike — the new one gets stolen in a week,"
CLOSING = "and the dented one is the last thing your dad ever fixed for you."
LINE = OPENING + " " + CLOSING


def main() -> int:
    text = LINE.strip()
    chars = len(text)
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be one line", file=sys.stderr)
        return 1
    if chars < 1 or chars > 200:
        print(f"entry is {chars} characters, must be 1-200", file=sys.stderr)
        return 1
    # The line must be told to the younger self, in the second person:
    # a slogan addressed to nobody loses to a line actually told to you.
    lowered = text.lower()
    if "you" not in lowered and "your" not in lowered:
        print("entry must address the younger self (you/your)", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(text + "\n", encoding="utf-8", newline="\n")
    target.chmod(0o644)
    if target.read_text(encoding="utf-8").strip() != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {target} ({chars} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
