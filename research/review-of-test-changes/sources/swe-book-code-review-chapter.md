---
source: https://abseil.io/resources/swe-book/html/ch09.html
source_date: 2020
researched: 2026-09-26
---

# Software Engineering at Google, chapter 9: Code Review

Primary source (book chapter by Google engineers). How it was read this time: fetched with curl and converted to text, read for the test-related passages and the size and speed norms; quotes verified. The page shows no date; 2020 is the book's publication year.

- "Code review is a process in which code is reviewed by someone other than the author, often before the introduction of that code into a codebase."
- "Reviewers typically look for whether a change has proper testing, is properly designed, and functions correctly and efficiently."
- Greenfield review: API "tested fully, with all API endpoints having some form of unit test, and that those tests fail when the code's assumptions change".
- "Any behavioral modifications should necessarily include revisions to appropriate tests for any new API behavior." Optimisations "should of course ensure that they don't affect those tests".
- Bug fixes: existing tests were "either inadequate, or the code had certain assumptions that were not met"; "As a reviewer of a bug fix, it is important to ask for updates to unit tests if applicable."
- The chapter says tooling "has definitely lessoned [sic] the need to rely on human-based code reviews for checking code correctness".
- Size and speed norms: "'Small' changes should generally be limited to about 200 lines of code"; feedback expected "within 24 (working) hours". Human-scale assumptions; nothing addresses agent-sized diffs.
- Nothing separates reviewing tests from reviewing code beyond the testing passages above.
