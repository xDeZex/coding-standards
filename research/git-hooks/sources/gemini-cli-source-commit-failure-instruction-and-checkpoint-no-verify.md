---
source: https://github.com/google-gemini/gemini-cli/blob/main/packages/core/src/prompts/snippets.ts
source_date: 2026-09
researched: 2026-09-26
---

# Gemini CLI source: system-prompt commit rules and hook-free checkpoint commits

How read: two source files (packages/core/src/prompts/snippets.ts and packages/core/src/services/gitService.ts) fetched raw from raw.githubusercontent.com main on 2026-09-26 and grepped for commit, hook and no-verify; matches read in context. The GitHub API showed the last change to snippets.ts on 2026-09-08 (source_date is given to the month). This is the main branch, not a pinned release, and is code not documentation.

- snippets.ts, the git section of the prompt: "**NEVER** stage or commit your changes, unless you are explicitly instructed to commit"; when committing, gather `git status`, `git diff HEAD`, `git log -n 3`; do not use `git add .` or `git add -A` unprompted; "After each commit, confirm that it was successful by running `git status`"; "**If a commit fails, never attempt to work around the issues without being asked to do so.**"; "Never push changes to a remote repository without being asked explicitly by the user." The core mandates also say to "Never log, print, or commit secrets".
- No mention of hooks or `--no-verify` in the prompt text matched. The failed-commit instruction covers a hook rejection by implication only.
- gitService.ts: Gemini CLI's checkpointing runs its own commits in a shadow repository (author "Gemini CLI") with `'--no-verify': null`, and its git wrapper sets `allowUnsafeHooksPath: true`. So tool-internal commits skip hooks by construction; these are not the user's repository history as read.
- Codex prompt files read (gpt_5_codex_prompt.md, gpt-5.2-codex_prompt.md, gpt_5_2_prompt.md in codex-rs/core) state only that Codex should not amend a commit or commit or branch unless asked; they say nothing about hooks or a failed commit.
- Related: [Claude Code issue 87981](claude-code-issue-87981-workaround-after-hook-rejection.md), where an agent did work around a rejecting hook.
