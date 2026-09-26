---
source: https://docs.github.com/en/copilot/reference/hooks-configuration
source_date: undated
researched: 2026-09-26
---

# GitHub Copilot hooks reference: CLI versus cloud agent, policy hooks, event effects

Read as raw page text (curl and html.parser). Not via WebFetch. Exit codes, timeouts and agentStop are in the sibling note [github-copilot-hooks](../../hooks-as-test-gate/sources/github-copilot-hooks.md). This page covers two surfaces, Copilot CLI and Copilot cloud agent.

- Sources loaded in order: policy files, user, project, plugins; all entries for an event run. Policy hooks are machine-wide files (`/etc/github-copilot/policy.d/*.json`, a Windows path and a registry key), "cannot be disabled by disableAllHooks and are available regardless of folder trust state"; on POSIX they must be owned by root and not group- or world-writable. "Policy hooks are not supported under Copilot cloud agent." A repository `settings.json` can set `disableAllHooks` to skip every non-policy hook in CLI sessions.
- Cloud agent: hooks run in an ephemeral Linux sandbox; only `bash` (or `command`) entries are honoured; the only hook configuration present by default is `.github/hooks/*.json` in the cloned repo; the sandbox "does not ship with user-level hook files". Outbound network is restricted by the agent firewall, so an HTTP hook to another host needs an admin allow rule. Files hooks write are discarded when the job ends. Notification hooks do not fire in the cloud agent. preToolUse "ask" is treated as deny "because no user is available". Prompt hooks ("auto-submit text as if the user typed it", only on sessionStart) "may not fire" in cloud agent.
- Event effects from the events table: agentStop and subagentStop can block and force continuation; preToolUse can allow, deny or modify; postToolUse "can modify the tool result or inject additional context for the model"; postToolUseFailure can add recovery guidance; sessionStart and notification "can inject additionalContext"; errorOccurred, preCompact and sessionEnd have no output processed; subagentStart cannot block but can prepend context to the subagent prompt. The notification hook is "fire-and-forget: never blocks the session".
- userPromptSubmitted: `modifiedPrompt` "is only honored by SDK programmatic hooks. Command and HTTP config-file userPromptSubmitted hooks have their output dropped, including modifiedPrompt." The same runtime split applies to preToolUse: a lighter hooks runtime for hosted or steering cloud agent sessions ignores some fields.
- Failure handling: for most events non-zero exits and timeouts are "logged and skipped". preToolUse command hooks fail closed on exit 2, a crash or any non-timeout non-zero exit, "but timeouts always fail-open — a slow or unreachable hook must not silently block tool calls or work, even when the hook was deployed by an administrator as policy." Two or more JSON objects on stdout concatenate into invalid JSON and are ignored ("emit exactly one final decision object"). A malformed hook item in a `.github/hooks/*.json` file is dropped and logged while sibling hooks load; inline settings hooks are strict.
- Hook output is bounded at 10 MiB per invocation. Progress lines (`{"type":"progress"}`) are display-only.
- The page also describes a VS Code compatible PascalCase format; that variant was not read further.
