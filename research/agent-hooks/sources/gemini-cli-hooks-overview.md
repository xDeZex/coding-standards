---
source: https://geminicli.com/docs/hooks/
source_date: 2026-04-13
researched: 2026-09-26
---

# Gemini CLI hooks: overview, events, exit codes, security

Read in full as raw page text (curl and html.parser). The page says "Last updated: Apr 13, 2026" and carries a banner: "Unpaid tier and Google One users: Gemini CLI was replaced by Antigravity CLI on June 18th, 2026", so it may be superseded for some users (not checked). The reference page is covered in the sibling note [gemini-cli-hooks](../../hooks-as-test-gate/sources/gemini-cli-hooks.md).

- Definition: "Hooks are scripts or programs that Gemini CLI executes at specific points in the agentic loop, allowing you to intercept and customize behavior without modifying the CLI's source code." "Hooks run synchronously as part of the agent loop ... Gemini CLI waits for all matching hooks to complete before continuing."
- Listed purposes: add context, validate actions, enforce policies, log interactions, optimize behavior (filter tools, adjust model parameters).
- Events and stated impact: SessionStart (inject context), SessionEnd (advisory), BeforeAgent (block turn or add context), AfterAgent (retry or halt), BeforeModel (block, mock, swap model), AfterModel (block or redact), BeforeToolSelection (filter tools), BeforeTool (block or rewrite), AfterTool (block result or add context, "run tests"), PreCompress (advisory), Notification (advisory).
- Strict JSON rule: stdout must be only the final JSON object; "The CLI will default to 'Allow' and treat the entire output as a systemMessage" if stdout has extra text.
- Exit codes: 0 parsed as JSON; 2 "Critical Block", the action is aborted and stderr is the reason; any other code "Warning ... Non-fatal failure ... the interaction proceeds using original parameters."
- Config layers (highest to lowest precedence): project `.gemini/settings.json`, user, system `/etc/gemini-cli/settings.json`, extensions. Only `command` type is supported. Default timeout 60000 ms. Hooks run with a sanitized environment (sic; the best-practices page says redaction is off by default).
- Security: "Hooks execute arbitrary code with your user privileges." Project hooks are fingerprinted by name and command: if a command changes (for example via `git pull`), it is treated as a new untrusted hook and the user is warned before it runs. Management commands: `/hooks enable-all`, `/hooks disable-all`, per-hook enable and disable.
