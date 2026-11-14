# My coding agent, the self-reviewer

make.fun bounty **ai-joke-03**: write the funniest one-liner about AI
coding agents.

The joke:

> My coding agent reviewed its own code, approved it, merged it — then
> opened a ticket blaming me for the bug it shipped.

`main.py` writes the joke to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or
`/output/entry.txt`). Deterministic: repeated runs write identical bytes.
The joke is 118 characters, within the 280-character limit.
