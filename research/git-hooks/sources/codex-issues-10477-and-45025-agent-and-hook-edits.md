---
source: https://github.com/openai/codex/issues/10477
source_date: 2026-02-03
researched: 2026-09-26
---

# Codex issues 10477 and 45025: refusing to mention --no-verify, and rewriting a hook shebang

How read: both issues (bodies and comments) read as raw JSON from the GitHub REST API. Both open at fetch time. User reports, unverified.

- #10477 (2026-02-03, bniladridas): Codex "refused mentions of --no-verify even when non-executing", saying it must follow repo rules. The reporter adds that the repo's AGENTS.md has an explicit rule prohibiting `--no-verify` and that Codex seems to treat a mention as a hard violation of that rule. Shows an instruction-file rule against skipping hooks being followed strictly, in this case over-broadly. One user, one repo, no other reproduction seen.
- #45025 (2026-09-12, MRJHP): a `codex exec --json` background task (run through a Claude Code plugin, Windows 11 Git Bash, `--sandbox workspace-write`) was asked to add a block to an existing pre-commit-framework `pre-commit` hook right after the shebang and leave everything else; after the edit line 1 had changed from `#!/usr/bin/env bash` to `#!/bin/sh`, in 2 of 7 repositories. No transcript offered. Shows agents can edit hook files they are asked to edit, and can change them unintentionally; it says nothing about agents disabling hooks on purpose.
- The agent's ability to write to `.git/hooks` in the Codex sandbox is separate: see the [docs note](codex-docs-sandbox-protected-git-path.md).
