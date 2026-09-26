---
source: https://github.com/anthropics/claude-code/issues/34692
source_date: 2026-03-15
researched: 2026-09-26
---

# anthropics/claude-code issue 34692: hooks do not fire for subagent tool calls (contested in comments)

Practitioner bug report, read as raw JSON from the GitHub API: the body in full and the first six comments (of ten). Version 2.1.76, Linux. Closed as `not_planned` by the github-actions bot for inactivity on 2026-05-30, later locked; no Anthropic staff comment among the comments read.

- Report: PreToolUse and PostToolUse hooks in `~/.claude/settings.json` fire for main-session tool calls but not for tool calls made by subagents spawned with the Agent tool; the reporter's `git commit` counter stayed at zero while subagents committed. "There is no warning or indication that hooks are being skipped." Workaround the reporter used: query the systems of record (`git log`, Jira) at checkpoint time instead of trusting hook-maintained state.
- Confirmations in comments (unverified): several users say they see the same on later versions, one on v2.1.89 says PostToolUse works in subagents but PreToolUse blocking does not, one platform reports 66 hooks and bypassed safety hooks in sub-agent context.
- Contradicting evidence in the same thread: a later commenter tested on CLI 2.1.119 (Windows, Git Bash) with a no-op logging hook and `claude -p --include-hook-events`, and reports that both the parent's Agent-tool call and the subagent's own Bash call fired PreToolUse and PostToolUse, with `agent_id` and `agent_type` in the payload.
- The current reference states that hooks "also run inside subagents ... the input carries the agent_id and agent_type" (see the reference note). So the claim is contested: it may have been true at 2.1.76 and fixed, and the reference now says the opposite. What is established is that a hook's coverage of subagents was in doubt for users, and that the thread never received a vendor statement.
- Related issue numbers in the body (#26923 exit 2 and the Task tool; #34240 background agents bypass PreToolUse, closed; #35557 EnterWorktree) were not read.
