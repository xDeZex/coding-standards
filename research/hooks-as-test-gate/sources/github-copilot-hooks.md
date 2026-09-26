---
source: https://docs.github.com/en/copilot/reference/hooks-configuration
source_date: undated
researched: 2026-09-26
---

# GitHub Copilot hooks (agentStop, preToolUse) for Copilot CLI and cloud agent

Re-read 2026-09-26 as raw HTML fetched with curl (redirects followed), stripped to text with a python html.parser script; the reference page was checked in full for the quotes below and the concept page https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-hooks was read too; no WebFetch used. First-party vendor docs; the reference page title is "GitHub Copilot hooks reference" and the concept path still says coding-agent, so the URLs are likely to move.

- Hooks run custom shell commands at points in an agent's workflow, for Copilot cloud agent on GitHub and Copilot CLI. Defined as JSON at .github/hooks/*.json in the repo (committable), personal hooks at ~/.copilot/hooks/*.json (CLI), or inline in .github/copilot/settings.json; the reference also lists cross-tool .claude/settings.json among sources. Format: `{"version": 1, "hooks": {...}}` with entries `{type: "command", bash | powershell | command (cross-platform fallback), cwd, env, timeoutSec}` (CLI also supports `exec` and `args`). Sources load in order policy, user, project, plugins and are combined. "timeoutSec: Maximum execution time in seconds (default: 30)."
- Events: sessionStart, sessionEnd, userPromptSubmitted, preToolUse, postToolUse, agentStop ("the main agent has finished responding"), subagentStop, errorOccurred and more.
- agentStop / subagentStop decision control: `decision: "block"` "forces another agent turn using reason as the prompt"; "Yes — can block and force continuation." Input `stop_hook_active`: "true when this turn was already forced to continue by a prior block decision from this hook". "Runaway guard. After 8 consecutive block continuations, the CLI overrides the hook and ends the turn anyway." In cloud agent a forced turn "still counts against the job's timeout".
- preToolUse: output `permissionDecision` allow/deny/ask (ask is treated as deny under cloud agent) with `permissionDecisionReason`. Fail behaviour: "Command preToolUse hooks are fail-closed on errors — a crash or non-zero exit (including exit 2) denies the tool call, even if the hook's stdout JSON reports permissionDecision: allow. Command hook timeouts are always fail-open, even for preToolUse" (tool call proceeds).
- Exit-code table: 0 success; 2 "Treated as a warning by default" except for permissionRequest and preToolUse where it denies; other non-zero logged and run continues (fail-open) except preToolUse (fail-closed). For agentStop the only documented route to force continuation is the decision JSON (`decision: "block"`). Exit 2 is documented as "Treated as a warning by default. stderr is surfaced to the user but the run continues", with deny exceptions named only for permissionRequest and preToolUse (and additionalContext for postToolUseFailure); agentStop is not among the exceptions, so per the page exit 2 does not force continuation there (in contrast to Claude Code and Codex). The page has no agentStop-specific exit-code sentence, so this is read from the general table.
- Repository setting can skip all hooks for sessions in that repo (Copilot CLI); policy hooks are unaffected.

Unverified: an explicit agentStop exit-2 statement (inferred from the general table); VS Code Copilot hooks (the reference mentions a "VS Code compatible" config) were not read.
