---
source: https://github.com/Aider-AI/aider/issues/802
source_date: 2024-07-06
researched: 2026-09-26
---

# Aider issue 802: pre-commit hooks ignored; maintainer answer and a formatting-hook comment

How read: issue body and all comments read as raw JSON from the GitHub REST API. Closed as completed on 2024-07-12 by the maintainer (paul-gauthier); the last comment is from 2025-02-26.

- Reporter (Aider v0.42.0, Claude 3.5 Sonnet) says failing pre-commit hooks (a `.git/hooks/pre-commit` and a `pre-commit` framework config running Jest) "will not prevent Aider from committing". Asks how to make Aider "iterate on a prompt until tests are passing" and wants a failing pre-commit test hook to make Aider stop, correct and go back to the previous commit. Says Aider "can sometimes break a number of tests without realizing it".
- Maintainer reply (2024-07-07): "Yes, aider skips pre-commit hooks by default. You can probably restore them using something like: `aider --test-cmd pre-commit`", explaining `--test-cmd` runs a repo-wide check and "Aider will attempt to fix any issues identified if the command returns a non-zero exit status." So the vendor's answer positions Aider's own test or lint command (an agent-side loop) as the way to get hook-style checks, not the git hook.
- Comment 2025-02-26 (maje91, practitioner): uses `pre-commit` "only for formatting", says requiring tests to pass on every small commit "doesn't really work for me", and that formatter hooks "fix the errors it finds" so they fall in "a different class of tooling than test/lint". After Aider committed without hooks, `pre-commit run --all-files` showed clang-format failing with "files were modified by this hook". Asks for a `--format-cmd`/`--fix-cmd` option. This is a practitioner observation on hooks that rewrite files rather than reject.
- Related: [docs note](aider-git-docs-commit-verify-default.md).
