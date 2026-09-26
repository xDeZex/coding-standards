---
source: https://github.com/anthropics/claude-code/issues/96891
source_date: 2026-09-24
researched: 2026-09-26
---

# anthropics/claude-code issue 96891: a blocked UserPromptSubmit prompt is still echoed and written to the transcript

Practitioner bug report by one user, body read in full as raw JSON from the GitHub API; no comments. Open when read, Claude Code 2.1.281 (also 2.1.266), Windows. Not reproduced by us.

- Report: when a UserPromptSubmit hook blocks a prompt (exit 2 or `{"decision":"block"}`), the prompt text is still shown in the terminal under "Original prompt:" and is written to the session JSONL twice: a `queue-operation` enqueue record written before the hook runs, and a system record embedding the block notice with the raw prompt. The reporter verified the blocked prompt did not reach the model (a later question about a unique marker returned "No").
- The reference's exit-code table says exit 2 on UserPromptSubmit "Blocks prompt processing and erases the prompt". The reporter says organizations "are building data-handling controls on that sentence" and that the JSON form behaves identically, "So there is no hook-side mitigation."
- Why it matters here: the verdict was correct and the model never saw the prompt, but the hook did not remove the data from local storage. A hook that blocks acts on what the model receives, not on every copy the harness keeps. Frequency and vendor response unknown.
