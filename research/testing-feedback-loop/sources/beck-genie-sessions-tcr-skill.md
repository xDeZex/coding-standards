---
source: https://newsletter.kentbeck.com/p/genie-sessions-tcr-skill
source_date: 2026-04-01
researched: 2026-09-26
---

# Kent Beck, "Genie Sessions: TCR Skill"

Reading method: the post is a recording of a live, unscripted coding video, not an article. The static page shows only a caption; the full ~50-minute transcript was retrieved via the post's API JSON (`/api/v1/posts/<slug>`), which links to a signed CDN URL for an auto-generated (WhisperX-style, word-level) transcription.json. Read in full from that transcript.

- Author Kent Beck, 1 April 2026, live video on his "Tidy First?" newsletter (Substack).
- Setup: a live, unscripted "genie session." Beck defines TCR: "test and commit or revert, which is this crazy but fun programming workflow where you make changes, you run the test, if the test fail you revert hard, you're back to square one, and if they pass then you do a commit." He pairs it with a second idea he's exploring live: agent skills. Quoted rule as implemented: "run tests after each micro change, commit only on green, discard the change on red, use when the user mentions TCR."
- He built a skill in Cursor (not Claude Code or Codex — his stated reason was budget: "I still have some money on cursor and Claude's behaving badly for me right now") that forces TCR on every message in the repo, then had the agent implement a left-leaning red-black tree in Python one micro-test at a time: empty get, put+get, BST insert/lookup, rotations, invariant checks, then delete (single-node, two-node, larger stress runs).
- **Result, in his words**: "So I think we've done enough. The skill works. That part is clear... We can get the genie to follow a TCR style. It does real TCR in the sense of having a big goal and then working on little pieces that are... monotonically increasing towards that eventual goal."
- **A named weakness**: TCR reverts the whole change on a failing test, including a correctly-written test paired with a wrong implementation. "What if you get the test right, but the implementation wrong, poof, even your test is gonna disappear... it's a thing I don't like about TCR."
- **Left untested**: he never pushed the task hard enough to see the failure mode he was actually curious about. "We haven't gotten it to a point where maybe it gets frustrated trying to follow a TCR style... What happens if it just gets stuck? Don't know yet."
- **An open, unresolved worry**: whether a stuck agent would stop writing tests rather than keep reverting — "are we going to find it just not writing tests, it's just gonna plow ahead with an implementation that may or may not be correct and not have tests." He floats requiring a coverage percentage as a guard, while noting he otherwise thinks coverage targets are "a terrible way to think about managing software development quality" — floated, not tried.
- Scope and confidence: one person, one session, one data structure, no comparison run without TCR, self-reported and informal ("just figuring stuff out live"). Positive but qualified first impression, not a track record.
- The skill and code were pushed live to a GitHub repo he calls "kentbeck/tcr-skill" in the recording; not independently confirmed or read here (see lead).
