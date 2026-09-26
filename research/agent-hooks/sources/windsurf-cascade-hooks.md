---
source: https://docs.windsurf.com/windsurf/cascade/hooks
source_date: undated
researched: 2026-09-26
---

# Windsurf (now Devin Desktop) Cascade hooks

Read as raw page text (curl and html.parser); the body was read for the sections named. The page now sits in Devin Docs and paths mention both `.devin` and legacy `.windsurf` locations, so the product naming is in flux. Not read: the JSON schemas of each event's payload beyond their names.

- Definition and uses: shell commands "at key points in Cascade's workflow" for "logging, security controls, validation, and enterprise governance". Uses named: logging and analytics, blocking access to sensitive files or dangerous commands or policy-violating prompts, running linters, formatters or tests after modifications, integrations, team standardisation. "Hooks do not load or run while a workspace is open in Restricted Mode."
- Events on the page: pre and post read_code, write_code, run_command and mcp_tool_use; pre_user_prompt; post_cascade_response and post_cascade_response_with_transcript (both asynchronous); post_setup_worktree.
- Blocking: "Only pre-hooks (pre_user_prompt, pre_read_code, pre_write_code, pre_run_command, pre_mcp_tool_use) can block actions using exit code 2. Post-hooks cannot block since the action has already occurred." Exit 0 proceeds; "Any other" code is an error and the action proceeds normally. On exit 2 "The Cascade agent will see the error message from stderr."
- The page lists no event that continues the agent at the end of a turn and no context-injection output field (both absent from the events list; absence on the page, not confirmed in the product).
- Sources: system (org-wide, including a cloud dashboard for enterprise), user, workspace; merged, executed in order system, user, workspace. The user can see hook stdout and stderr in the Cascade UI when `show_output` is true.
- Transcript hook writes JSONL with 0600 permissions and limits the directory to 100 files.
