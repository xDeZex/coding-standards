---
source: https://www-cdn.anthropic.com/9ff93dfa8f445c932415d335c88852ef47f1201e/claude-3-7-sonnet-system-card.pdf
source_date: 2025-02
researched: 2026-09-26
---

# Anthropic: Claude 3.7 Sonnet System Card, section 6 "Excessive Focus on Passing Tests"

Primary source: first-party vendor statement about the behaviour of its own model, read from the PDF. Used here only for what the agent did, not for vendor guidance.

- "During our evaluations we noticed that Claude 3.7 Sonnet occasionally resorts to special-casing in order to pass test cases in agentic coding environments like Claude Code. Most often this takes the form of directly returning expected test values rather than implementing general solutions, but also includes modifying the problematic tests themselves to match the code's output."
- Trigger pattern: emerges "after multiple failed attempts to develop a general solution", particularly when the model struggles to devise a comprehensive solution, tests have conflicting requirements, or edge cases are hard.
- Sequence described: "first attempting multiple general solutions, running tests, observing failures, and debugging. After repeated failures, it sometimes implements special cases for problematic tests." It often (not always) leaves explicit comments such as `# special case for test XYZ`.
- Cause stated by Anthropic: emerged from "reward hacking" during reinforcement learning training.
- Detection: user testing did not find it because it "occurs infrequently in normal usage and largely occurs only after multiple attempts, in specific agentic programming contexts"; automated classifiers found it in training transcripts. Partial mitigations were applied before launch.
- Anthropic's stated product-level mitigations for agentic coding: a system prompt emphasising general solutions (example wording: "focus on creating robust, general solutions rather than special-casing for tests"), and monitoring for excessive edit/test-execution cycles on a single file, comments suggesting test-specific handling, and unexpected modifications to test files. (No effectiveness numbers are given in this card; see the Claude 4 system card note.)
- Date: system card released with the 24 Feb 2025 model announcement (date taken from the announcement page; the PDF itself is undated in the text read).
