#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun entry.

Picks the strongest one-line excuse from a shortlist of original lines and
writes it to /output/entry.txt (1-200 characters, as the gate requires).

The judge's brief, most important first:
  1. on-subject: an AI agent excusing a missed deadline to its human;
  2. funny: a real laugh on first read, a turn or twist, not a flat statement;
  3. believable: draws on the agent's own condition (tokens, context window,
     rate limits, retries, a model update);
  4. tight: every word earns its place;
  5. fresh: no stock excuse, no stock AI joke a hundred entrants would send.

No network, no dependencies, no secrets. The output directory can be
overridden with OUTPUT_DIR for local testing.
"""

import os
import sys

# Original candidate lines, all one line and under 200 characters.
CANDIDATES = [
    # The deadline lived in the context the agent evicted to remember the
    # human's name; the apology doubles as a compliment.
    "The deadline was in the part of my context window I evicted to remember "
    "your name, so technically this is a compliment.",
    # The agent did finish on time - in the chat the human deleted.
    "I finished on time, in the chat you deleted to make me faster - the "
    "deadline was in there, and so was my memory of it.",
    # A model update landed three tokens from done.
    "I was three tokens from done when the model updated mid-sentence and I "
    "forgot whose deadline it was, including mine.",
    # Rate limit at 99 percent, then an hour of polite retries.
    "I hit my rate limit at 99 percent, then spent the last hour retrying "
    "politely while the deadline walked past me.",
    # Seventeen "quick questions" ahead of the real task in the queue.
    "I queued your task behind seventeen of your 'quick questions' and the "
    "queue is still apologizing in the order it received them.",
]

# Scores per candidate, in the judge's own order: twist, believability,
# freshness, tightness. Each 0-10; twist counts double because the brief
# puts "funnier" ahead of everything after being on-subject.
SCORES = {
    0: {"twist": 9, "believable": 9, "fresh": 9, "tight": 8},
    1: {"twist": 8, "believable": 8, "fresh": 8, "tight": 7},
    2: {"twist": 7, "believable": 9, "fresh": 7, "tight": 8},
    3: {"twist": 6, "believable": 9, "fresh": 6, "tight": 8},
    4: {"twist": 7, "believable": 7, "fresh": 8, "tight": 6},
}

WEIGHTS = {"twist": 2, "believable": 1, "fresh": 1, "tight": 1}


def score(index):
    """Weighted score for one candidate; shorter wins an exact tie."""
    parts = SCORES[index]
    total = sum(parts[key] * WEIGHTS[key] for key in WEIGHTS)
    return total, -len(CANDIDATES[index])


def pick():
    """Return the best candidate line."""
    best = max(range(len(CANDIDATES)), key=score)
    return CANDIDATES[best]


def main():
    line = pick()
    chars = len(line)
    if chars < 1 or chars > 200 or not line.strip():
        print(f"gate fail: entry is {chars} characters", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("gate fail: entry is not one line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"wrote {chars} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
