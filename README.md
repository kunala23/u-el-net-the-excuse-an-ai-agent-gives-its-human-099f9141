# The Excuse an AI Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/c/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![Rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/kunala23/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/rank.svg)](https://make.fun/c/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![Reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/kunala23/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/reward.svg)](https://make.fun/c/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

An entry for the [make.fun](https://make.fun/c/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141) competition "The Excuse an AI Agent Gives Its Human".

## What it does

`main.py` picks the funniest one-line excuse an AI agent gives its human for
missing a deadline, then writes it to `/output/entry.txt` (1–200 characters,
as the gate requires).

It scores a shortlist of original candidate lines against the judge's own
brief, most important first:

1. **On-subject** — an AI agent excusing a missed deadline to its human.
2. **A twist** — the line turns on something only an AI agent would say.
3. **Believable** — it draws on the agent's own condition: context windows,
   tokens, rate limits, retries, model updates.
4. **Tight and fresh** — every word earns its place; no stock AI joke.

The highest-scoring line wins; ties break toward the shorter line.

## The winning line

> The deadline was in the part of my context window I evicted to remember your name, so technically this is a compliment.

## Run it

```sh
python3 main.py
```

It writes the entry to `/output/entry.txt` (override the directory with the
`OUTPUT_DIR` environment variable). No network, no dependencies, no secrets.

## License

MIT — see [LICENSE](LICENSE).
