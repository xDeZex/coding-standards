---
source: https://code.claude.com/docs/en/best-practices
source_date: undated
researched: 2026-09-26
---

# Best practices for Claude Code (Anthropic docs)

First-party vendor guidance, living document (redirected from anthropic.com/engineering/claude-code-best-practices). Read in full.

- Recommended workflow: Explore, Plan, Implement, Commit. "Separate research and planning from implementation to avoid solving the wrong problem." Plan Mode reads files without changing them; the human can edit the plan before approving.
- Planning is optional: "If you could describe the diff in one sentence, skip the plan." It is most useful when the approach is uncertain, several files change, or the code is unfamiliar. For clear, small changes (typo, log line, rename) "ask Claude to do it directly."
- The human can have Claude interview them and write a spec; "Time spent making the spec precise pays off more than time spent watching the implementation."
- Verification: "Give Claude a way to verify its work." Without a runnable check "you become the verification loop." "The trust-then-verify gap. Claude produces a plausible-looking implementation that doesn't handle edge cases... If you can't verify it, don't ship it."
- Adversarial review by a fresh subagent is advised for unattended work, with a warning that reviewers "will usually report some" gaps and chasing them "leads to over-engineering: extra abstraction layers, defensive code, and tests for cases that can't happen."
- Performance degrades as the context window fills; humans manage context.
- Bearing on the split: the human role described is planning, specifying, verifying and course-correcting, which is strategic-ish, and Claude implements. But the guide treats the code-level output as untrustworthy until checked, and never says the AI is good at tactical work; the emphasis is on verification. Vendor guidance, so not independent evidence of AI capability.
