---
source: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
source_date: 2025-07-10
researched: 2026-09-26
---

# Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity (METR)

How read this time: full post fetched with curl and converted to text; read in full except the figures and the full paper (linked from the page), which were not read. All numbers below were correct. New: the page now carries a banner "These results are out of date", pointing to the early-2026 continuation.

Primary: randomized controlled trial by METR.

- Design: 16 experienced developers from large open-source repositories (averaging 22k+ stars and 1M+ lines of code) they had contributed to for years; 246 real issues (bug fixes, features, refactors; about two hours each) randomly assigned to allow or disallow AI. Tools were "primarily Cursor Pro with Claude 3.5/3.7 Sonnet". Developers screen-recorded and self-reported implementation time; paid $150/hour.
- Result: "they take 19% longer to complete issues". Developers expected AI to speed them up by 24% and, after the slowdown, still believed AI had sped them up by 20%.
- Quality: METR says they "submitted similar quality PRs with and without AI".
- METR's own list of claims it does not make: it does not claim AI does not speed up most developers, that developers or repositories are representative, that AI will not speed up developers in the same setting in future, or that there are no better ways to use current AI. It notes that Cursor may not use optimal prompting or scaffolding, and that learning effects over hundreds of hours may matter (its developers used Cursor for a few dozen hours). It also suggests AI capabilities may be lower in settings with very high quality standards or many implicit requirements.
- Bearing on the split: contradicts a strong form of "AI is good at tactical work" for this setting (issues in familiar, high-standard repositories) and shows self-reports are unreliable. Small sample, early tools, and the page itself now says the results are out of date; see the metr-2026-uplift-design-update note.
