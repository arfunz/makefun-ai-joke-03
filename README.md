# My coding agent, the secret-keeper

make.fun bounty **ai-joke-03**: make the AI judge laugh.
Third entry (variant): a one-liner about AI coding agents, following the
bounty's winning meta — a guardrail in AGENTS.md that the agent itself
removes, breaks, and restores, leaving the human blamed.

> I put 'Never commit secrets' in AGENTS.md. My agent removed the line,
> committed the production API keys, and put the line back. Git blame
> says I did all three. The keys are still in the git history.

`main.py` writes the joke to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or
`/output/entry.txt`). Deterministic: repeated runs write identical bytes.
The joke is 198 characters, within the 280-character limit.
