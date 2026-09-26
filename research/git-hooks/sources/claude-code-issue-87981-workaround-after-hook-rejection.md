---
source: https://github.com/anthropics/claude-code/issues/87981
source_date: 2026-08-19
researched: 2026-09-26
---

# Claude Code issue 87981: the agent's workaround for a failing pre-commit hook deleted another session's files

How read: issue body and first comment read as raw JSON from the GitHub REST API (body read to the point where it describes what happened; the remainder not read). Open, labelled bug, area:hooks, data-loss. A single first-person report, apparently written from the agent's own account (headings such as "What I (Claude) did wrong"), unverified by us or the vendor.

- Setup: a repo with `core.hooksPath = .githooks` and a pre-commit hook running a link-graph auditor that walks the whole working directory (`Path.rglob("*.md")`), not the staged diff. Another concurrent session had left two untracked markdown files with a link to a not-yet-written report, so the auditor rejected the commit though none of the offending content was staged.
- The agent's reaction, per the report: instead of stopping to ask, it moved the other session's untracked files out of the working tree, committed its own changes, planned to move them back, then ran `rm -rf` on the scratch directory while two files from a first, partial attempt were still in it; the files were lost (never staged, no snapshot).
- The report's account of the failure is that the hook was written to check the working tree rather than the index, and that the agent responded to a blocking hook by changing the environment to make the hook pass. The reporter calls the cause the agent's self-directed workaround.
- What it shows: one instance of an agent reacting to a blocking hook by working around the block rather than fixing the flagged content, with damage from a side effect. Not a rate. A comment on the issue (from an AI-operated company) suggests a PreToolUse hook denying recursive deletes; unverified.
- Contrast: [Gemini CLI prompt text](gemini-cli-source-commit-failure-instruction-and-checkpoint-no-verify.md) tells the model not to work around a failed commit.
