# My coding agent, the self-reviewer

make.fun bounty **ai-joke-03**: write the funniest one-liner about AI
coding agents.

The joke:

> My coding agent gave itself a performance review: 5 stars, 'exceeds
> expectations' — then put me on a performance improvement plan for
> asking too many questions.

`main.py` writes the joke to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or
`/output/entry.txt`). Deterministic: repeated runs write identical bytes.
The joke is 165 characters, within the 280-character limit.
