---
source: https://github.com/anthropics/claude-code/issues/88738
source_date: 2026-08-22
researched: 2026-09-26
---

# anthropics/claude-code issue 88738: PreToolUse hook silently stops firing mid-session

Practitioner incident report (one user), read as raw JSON from the GitHub API: the issue body in full and its single comment. Nothing was reproduced by us. Status when read: open, no maintainer comment. Claude Code v2.1.238 per the reporter.

- Reported: in one interactive session a project-scoped PreToolUse hook (a Python script gating writes to protected paths, logging one line per invocation) stopped being invoked at a definite instant and never recovered. A concurrent session in the same project and settings file stayed hooked. "No error was surfaced anywhere, and nothing was written to the hook's stderr file."
- The reporter's table: session `0598abf9`, 52 tool calls, 19 with no hook log line, 100% hooked through 19:32:44 and 0% from 21:43:00 to session end; the other session had 0 and 1 misses. The 19 misses included PowerShell, Bash and Edit calls, among them `git add -A && git commit` and `git push`. The settings file sat on a Google Drive File Stream virtual volume; the hook script on local NTFS.
- The stderr file's mtime predated the outage by seven weeks, from which the reporter concludes "the hook process was not executed at all". Transcript `hookErrors` was empty, described by the reporter as weak evidence because no PreToolUse summary is recorded.
- "This has not been reproduced on demand. No reliable recipe is offered." Conditions observed: a long session (about 5 h 40 min), subagent activity, 130 minutes idle before the first miss (an earlier 124-minute idle did not cause it), a settings file not modified during the session.
- The reporter's questions to the vendor: whether a live session can lose hook registrations, whether the settings file is re-read and how a momentarily unreadable file is handled, whether registration state is inspectable, and whether a session can detect its own hooks are no longer invoked. "The failure is silent by construction: a hook that stops running looks exactly like a hook that has nothing to block."
- The one comment (a different user) generalises: "silence is not a signal", suggests a per-session hook invocation counter and a notice whenever a hook is skipped. It describes an unrelated component that stalled 45 days with green dashboards.
- Evidence strength: single unverified report with a strong measurement method (per-call correlation of transcript and hook log). It shows the failure shape (silent non-invocation) but says nothing about frequency; the vendor has not responded in what was read. The Claude Code reference separately documents that a hook that cannot start "leaves the gate silently disabled" (see the reference note) and that settings edits are picked up by a file watcher which can miss a change (guide note).
