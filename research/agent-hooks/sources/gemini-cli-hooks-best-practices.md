---
source: https://geminicli.com/docs/hooks/best-practices/
source_date: 2026-04-10
researched: 2026-09-26
---

# Gemini CLI hooks best practices: performance, debugging, security

Read in full as raw page text (curl and html.parser). "Last updated: Apr 10, 2026". Same Antigravity replacement banner as the overview note; applicability for paid users not checked.

- Performance: "Hooks run synchronously—slow hooks delay the agent loop." Advice: parallelise and cache expensive work; use narrow matchers, since specific matchers save "the overhead of spawning a process for irrelevant events". AfterAgent fires once per turn, while AfterModel "Fires after every chunk of LLM output", so a check of the final result belongs in AfterAgent.
- Debugging: "The most common cause of hook failure is 'polluting' the standard output." Hooks run in the background so writing to a log file is often the easiest way to debug. Execution is logged with telemetry `logPrompts` on; a `/hooks panel` shows counts, recent successes and failures and timing.
- Exit-code semantics as the page states them: exit 2 on Agent or Model events aborts the turn; on Tool events "blocks the tool but allows the agent to continue"; on AfterAgent "triggers an automatic retry turn". `{"continue": false}` kills the entire agent loop, distinct from a deny that blocks one action.
- Maintenance: use the `description` field and comments (one example script header lists "Performance: ~500ms average"); commit hook scripts to share them with the team.
- Threat model table: system hooks assumed safest; user hooks the user's responsibility; extensions depend on their source; project hooks "Untrusted by default. Safest in trusted internal repos; higher risk in third-party/public repos". Risks named: arbitrary code execution, data exfiltration (hooks can read prompts, code, and environment variables such as an API key), and prompt injection ("Malicious content in a file or web page could trick an LLM into running a tool that triggers a hook in an unexpected way").
- "Environment redaction is currently OFF by default." Administrators can enforce it in system settings.
- Hook not executing checklist: appears in `/hooks` and enabled, matcher regex correct, not on the `disabled` list, script executable (Windows execution policy), path resolves. Timeout default 60,000 ms.
