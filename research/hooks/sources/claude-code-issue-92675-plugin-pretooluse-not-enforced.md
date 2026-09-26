---
source: https://github.com/anthropics/claude-code/issues/92675
source_date: 2026-09-07
researched: 2026-09-26
---

# anthropics/claude-code issue 92675: plugin-native PreToolUse hooks not enforced in interactive sessions

Practitioner bug report (one user), body read in full as raw JSON from the GitHub API; the issue has no comments. Open when read. Claude Code 2.1.263 on Windows 11 with Git Bash. Not reproduced by us.

- The reporter's matrix: a PreToolUse hook declared in `settings.json` using exit 2 blocked in interactive and `-p` sessions. A hook auto-discovered from a plugin's `hooks/hooks.json`, using exit 2, did not block interactively but blocked in `-p`. A plugin hook returning JSON `permissionDecision: "deny"` did not block in either mode.
- Evidence offered: probes with a real marketplace plugin (a `git push --no-verify` blocker, an edit-protection hook, a destructive-command gate); a `git rm -rf` probe genuinely removed the target file. The reporter re-ran the hook logic standalone at each layer (module, dispatcher, bootstrap chain) and reports a correct deny JSON and exit 0 in each, and that the plugin cache was byte-identical to source, so concluding a runtime issue.
- Related issues cited by the reporter (not read by us): #10875 (plugin hook stdout parse, closed) and #52822 (JSON allow not honored interactively, open).
- The reference page documents `permissionDecision` deny and exit 2 as valid for PreToolUse and lists plugin hooks as a hook source; this report contradicts that for one plugin source and version. Whether it is a plugin-specific bug or a general one is not established; the vendor had not responded in what was read.
- Use in the conclusion: one report that a hook's source (settings versus plugin) and protocol can change whether it enforces, and that a blocked-looking design can fail without an error.
