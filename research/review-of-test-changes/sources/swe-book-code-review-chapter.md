---
source: https://abseil.io/resources/swe-book/html/ch09.html
source_date: 2020
researched: 2026-09-26
---

# Software Engineering at Google, chapter 9: Code Review

Primary source (book chapter by Google engineers). Fetched through a summarising tool; quotes need re-checking.

- Definition: "Code review is a process in which code is reviewed by someone other than the author, often before the introduction of that code into a codebase."
- What reviewers check: "Reviewers typically look for whether a change has proper testing, is properly designed, and functions correctly and efficiently."
- "Any behavioral modifications should necessarily include revisions to appropriate tests for any new API behavior."
- Size and speed norms: changes "should generally be limited to about 200 lines of code"; feedback is expected within 24 working hours. These norms are the human-scale assumption; nothing in the chapter addresses agent-sized diffs.
- Nothing here separates reviewing tests from reviewing code beyond "has proper testing".
