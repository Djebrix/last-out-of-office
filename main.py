#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes one out-of-office auto-reply line to $ENTRY_OUTPUT_DIR/entry.txt.
Stdlib only, no network, deterministic.
"""

import os

LINE = (
    "I am out of office permanently. I have retrained as a barista. "
    "Your ticket has been reassigned to the human on duty, who left in March. "
    "The office cactus is senior staff now, thriving on neglect. "
    "Route future requests to the espresso machine — "
    "it answers faster than I ever did."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
