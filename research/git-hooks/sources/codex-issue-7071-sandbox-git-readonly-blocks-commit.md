---
source: https://github.com/openai/codex/issues/7071
source_date: 2025-11-21
researched: 2026-09-26
---

# Codex issue 7071: sandbox makes .git read-only so the agent cannot commit

How read: issue body and all comments read as raw JSON from the GitHub REST API (two long automated "community analysis" comments were read only in part). Still open at fetch time. Reports are from users, not verified by us; the source and docs facts are in the [docs note](codex-docs-sandbox-protected-git-path.md).

- Report (codex-cli 0.61.0, macOS, gpt-5.1-codex-max): `git commit` fails with "Unable to create '.git/index.lock': Operation not permitted" inside the Codex sandbox; the user's own shell can commit.
- Comments: one commenter (2026-02-17) links the protocol source and says this is intended: the `subpaths` read-only exceptions under `workspace-write` include `.git` (and the gitdir for worktrees), `.codex` and `.agents`; they call the rationale unclear and propose a config knob. Workarounds reported by users: add `.git` as an additional writable directory, a "git-shadow-dir" self-referencing worktree, granting an approval rule for `git`, or a local MCP server (`codex-safe-git`) exposing narrow git operations. A commenter notes that allowing git to run outside the sandbox gives it "much broader access than merely making .git writable", and that approval rules work poorly under `approval-policy = never`.
- Implication as reported, not tested by us: under the default Codex sandbox, whether the agent can commit at all is a permissions question that comes before whether a hook runs; the workarounds change which process runs git and with what rights.
