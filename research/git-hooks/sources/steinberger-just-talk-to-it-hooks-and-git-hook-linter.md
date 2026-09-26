---
source: https://steipete.me/posts/just-talk-to-it
source_date: 2025-10-14
researched: 2026-09-26
---

# Peter Steinberger, Just Talk To It - the no-bs Way of Agentic Engineering (steipete.me)

Read in full via curl and html-to-text (25,800 characters), grepped and the commit passages read closely. Published "14 Oct, 2025". Also grepped his "Shipping at inference speed" post: no hits.

Speaker: Peter Steinberger, founder of PSPDFKit and author of widely read posts on running many agents in parallel; he says agents write "pretty much 100%" of his code on a ~300k LOC TypeScript app. Counts as trusted through sustained first-hand accounts of running agents on real work.

- On hooks, meaning Claude Code's agent hooks: "Yes, with claude you could do hooks and codex doesn't support them yet, but models are incredibly clever and no hook will stop them if they are determined." His agents commit themselves, guided by his agent file ("~800 lines ... a collection of organizational scar tissue").
- On a git hook as a linter gate: "If you don't know or don't use ast-grep as codebase linter, stop here and ask your model to set this up as a git hook to block commits." So he recommends a git hook for a structural linter (ast-grep rules), in passing, and without describing his own setup.
- A related pain: his `/commit` command has custom text "to explain that multiple agents work in the same folder and to only commit your changes, so I get clean comments and gpt doesn't freak out about other changes and tries to revert things if linter fails". So with several agents in one working tree, a failing check caused by another agent's change can make an agent try to revert changes that are not its own; he handles that with an instruction. He does not say whether this is a hook or a linter in the agent's own run.
- He works without worktrees or PRs ("always revert back to this setup as it gets stuff done the fastest"), which shapes what a commit gate sees.
- Not said: any account of a hook he runs, speed, or `--no-verify`.

The speaker description above is background I know, not read from the page (except where the page itself says it), and is unverified.
