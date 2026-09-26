---
source: https://github.com/anthropics/claude-code/issues/33343
source_date: 2026-03-11
researched: 2026-09-26
---

# anthropics/claude-code issue 33343: PreToolUse hooks and --allowedTools not enforced in headless -p mode

Practitioner bug report, read as raw JSON from the GitHub API: body in full and six comments. Version 2.1.73, Windows 11. Closed `not_planned` by github-actions for inactivity (June 2026), locked in August. No maintainer comment. Not reproduced by us.

- Report: with `claude -p --permission-mode bypassPermissions` (and with `--dangerously-skip-permissions`), the reporter's PreToolUse hook denying reads of certain files "never fires -- the file is read successfully", and `--allowedTools "Glob"` did not stop a Read (a canary file's contents were printed). Cited earlier reports: #20063, #30143, #18093 ("all auto-closed as stale/duplicate without a fix"), not read.
- Reporter's complaint: the docs "do not mention any exceptions for headless -p mode", so "users have no signal that these controls are inactive".
- Comments (unverified): a user with 15+ scheduled `claude -p` jobs says the hooks are bypassed for all headless automation at 2.1.107 and that `--bare` "strips ALL hooks" (a tradeoff, not a fix); a commenter at 2.1.142 reports plugin-registered hooks failing in sandboxed `-p` too, with a flag matrix; a related cluster is named (#36071 `allowedTools: ["*"]` bypasses hooks, #35557 EnterWorktree bypasses PreToolUse, #34240 background agents, closed).
- Contrast with the current docs: the hooks guide now states PreToolUse hooks run in every permission mode and deny "even in bypassPermissions mode or with --dangerously-skip-permissions", and describes `-p` runs treating the folder as trusted so committed hooks run (see the reference note). Issue 92675 reports a `-p` run where exit-2 plugin hooks did block. So this report is old and against a version that predates those statements; whether it still holds is unknown.
