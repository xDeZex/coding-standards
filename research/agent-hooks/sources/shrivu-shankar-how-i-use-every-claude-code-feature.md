---
source: https://blog.sshh.io/p/how-i-use-every-claude-code-feature
source_date: 2025-11-02
researched: 2026-09-26
---

# Shrivu Shankar, "How I Use Every Claude Code Feature" (hooks section)

Speaker: Shrivu Shankar, an engineer writing the "Shrivu's Substack" blog on Claude Code use in a professional codebase (the page says "a complex enterprise repo"; his employer is not stated in the text I read). Counts as trusted only moderately: named, sustained first-hand writing on real work, widely cited in Claude Code write-ups, but no authored tool or standard. Treat as one practitioner.

How read: raw HTML via curl and html-to-text, whole page; the Hooks section read in full.

- Attitude: "Hooks are huge. I don't use them for hobby projects, but they are critical for steering Claude in a complex enterprise repo. They are the deterministic 'must-do' rules that complement the 'should-do' suggestions in CLAUDE.md."
- Two types used. Block-at-submit: "We have a PreToolUse hook that wraps any Bash(git commit) command. It checks for a /tmp/agent-pre-commit-pass file, which our test script only creates if all tests pass. If the file is missing, the hook blocks the commit, forcing Claude into a 'test-and-fix' loop until the build is green." Hint hooks: "simple, non-blocking hooks that provide 'fire-and-forget' feedback if the agent is doing something suboptimal."
- Against block-at-write: "We intentionally do not use 'block-at-write' hooks (e.g., on Edit or Write). Blocking an agent mid-plan confuses or even 'frustrates' it. It's far more effective to let it finish its work and then check the final, completed result at the commit stage." Takeaway line: "Use hooks to enforce state validation at commit time (block-at-submit). Avoid blocking at write time".
- He also notes sandboxed cloud runs "support all the advanced features like Hooks and MCP".

Unverified: the claim that write-time blocking "frustrates" the agent is the author's experience; no data. The commit-time gate here is a test gate (see the earlier hooks-as-test-gate topic).
