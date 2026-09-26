---
source: https://code.claude.com/docs/en/whats-new/2026-w13
source_date: 2026-03
researched: 2026-09-26
---

# Claude Code what's new, week 13: an agent hook scoped to git commit

How read: the section for this page located in the llms-full.txt text file fetched with curl (see the [docs note](claude-code-docs-git-hook-paths-in-permissions-and-sandbox.md)); the "Conditional hooks" passage read in full. The page's exact date was not shown in the text read; the week label 2026-w13 and version v2.1.85 give roughly late March 2026, so source_date is given as 2026-03.

- "Conditional hooks" (v2.1.85): "Hooks can now declare an `if` field using permission rule syntax. Your pre-commit check only spawns for `Bash(git commit *)` instead of every bash call, cutting the process overhead on busy sessions."
- The example wires a PreToolUse agent hook with `"if": "Bash(git commit *)"` to `.claude/hooks/lint-staged.sh`.
- So the vendor's own example of a "pre-commit check" is an agent hook that fires on the agent's `git commit` Bash calls, not a git hook. The page does not compare the two or say when to prefer either, and gives no script body.
