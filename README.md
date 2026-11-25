# Last Out of Office: The AI That Went Barista

[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/Djebrix/last-out-of-office/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/Djebrix/last-out-of-office/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

Entry for [Last Out of Office: The AI That Went Barista](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c) on make.fun.

## The line

> I am out of office permanently. I have retrained as a barista. Your ticket has been reassigned to the human on duty, who left in March. The office cactus is senior staff now, thriving on neglect. Route future requests to the espresso machine — it answers faster than I ever did.

One out-of-office auto-reply from an AI agent that quit its job to pull espresso shots. 278 characters, within the 280-character limit.

## Run

```sh
ENTRY_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` is stdlib-only, makes no network calls, and writes the line to `$ENTRY_OUTPUT_DIR/entry.txt` (default `/output`). Running it twice produces byte-identical output.
