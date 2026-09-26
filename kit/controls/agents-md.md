# AGENTS.md

- **What it is:** A Markdown file in the repo that the agent reads at the start of a session, holding instructions for working in that repo.
- **Use when:** the agent needs standing context or constraints it cannot infer from the code, and a reminder before it acts is enough.

The kit has no AGENTS.md template: the file is easy to create and other tools already generate it. This is a guide, in the sense of `CONTEXT.md`: it steers the agent before it acts, and nothing checks that the agent followed it. It is loaded every session, so every line costs attention whether or not it applies.

What belongs in it:

- Standing context the agent cannot infer from the code: build and run commands that are not obvious, conventions the code does not show, constraints and things to avoid, and the reason behind a non-obvious rule.
- Only what a reminder before the agent acts is enough for. If the agent may skip it and the cost is real, use a sensor instead.

What does not:

- Anything the agent can read from the code or config.
- Long or situational instructions. Put those in a skill, which loads only when the task calls for it, and point to it from AGENTS.md if the agent needs a nudge to reach for it.
- A check that must always run. AGENTS.md is advice the agent may not follow; a hook runs regardless of what the agent decided.

The testing case shows the split:

- Explicit instructions for running the tests are better in a skill than in AGENTS.md. This is the author's experience and is not measured: no source compares instruction files, skills and hooks for getting tests run.
- A check that must always run, such as the tests before a commit, goes in a hook. A hook is the guarantee; it complements the agent running tests itself, and does not replace it.

Keep the file short, since the agent's attention thins as it grows. Claude Code suggests under 200 lines for its CLAUDE.md; Codex reads 32 KiB by default. To share one file across tools, Claude Code can import it with `@AGENTS.md` in a CLAUDE.md.

Decided points:

- When an entry is applied through AGENTS.md, write it reworded for the target repo. Leave out ids, links and any other pointer back to this repo, so the file stands alone.
- Create the file if it is missing; otherwise add to the existing one.
