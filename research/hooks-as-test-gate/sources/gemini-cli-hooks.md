---
source: https://geminicli.com/docs/hooks/reference/
source_date: undated
researched: 2026-09-26
---

# Gemini CLI hooks (AfterAgent retry, BeforeTool block)

Re-read 2026-09-26 as raw HTML fetched with curl (redirects followed), stripped to text with a python html.parser script; the reference page and the overview page https://geminicli.com/docs/hooks/ were both read in full and quotes checked against that text; no WebFetch used. First-party vendor docs. The banner at the top of both pages reads "Unpaid tier and Google One users: Gemini CLI was replaced by Antigravity CLI on June 18th, 2026. To learn more, see our blog post." (confirmed in the raw text; the blog post was not opened), so this tool's documentation may be superseded; its status for paid users was not checked.

- Hooks are configured in settings.json (merged, highest precedence first: project .gemini/settings.json, user ~/.gemini/settings.json, system /etc/gemini-cli/settings.json). Definition: `matcher` (regex for tool events, exact string for lifecycle events), `sequential`, and a `hooks` array of `{type: "command", command, name, timeout, description}`. "timeout: Execution timeout in milliseconds (default: 60000)." Only type "command" is supported.
- Exit codes: "0: Success. stdout is parsed as JSON. Preferred for all logic. 2: System Block. The action is blocked; stderr is used as the rejection reason. Other: Warning. A non-fatal failure occurred; the CLI continues with a warning." "Silence is Mandatory": stdout must carry only the final JSON.
- BeforeTool: `decision: "deny"` (alias "block") prevents the tool; exit 2 also blocks, stderr as reason.
- AfterAgent ("Fires once per turn after the model generates its final response. Primary use case is response validation and automatic retries."): input includes `prompt`, `prompt_response`, and `stop_hook_active` ("Indicates if this hook is already running as part of a retry sequence"). Output `decision: "deny"` "rejects the response and forces a retry"; `reason` "is sent to the agent as a new prompt to request a correction"; `continue: false` stops the session without retrying. "Exit Code 2 (Retry): Rejects the response and triggers an automatic retry turn using stderr as the feedback prompt." This is Gemini's equivalent of a keep-working-until-green Stop hook.
- No retry cap: searching both full pages for retry, limit, max and loop found none; the only guard offered is `stop_hook_active`. Absence on the page, not proof the code has none.
- The overview event table lists AfterTool ("After a tool executes", impact "Block Result / Context") with the common use "Process results, run tests, hide results"; it gives no git-commit-gating recipe.

Unverified: retry limit in code; whether hooks apply in Antigravity CLI.
