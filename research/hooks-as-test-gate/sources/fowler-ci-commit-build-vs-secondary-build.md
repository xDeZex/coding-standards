---
source: https://martinfowler.com/articles/continuousIntegration.html
source_date: 2024-01
researched: 2026-09-26
---

# Martin Fowler, "Continuous Integration": build speed and staged builds

Re-read pass 2026-09-26: the page was downloaded with curl as HTML, converted to text and the build-speed, deployment-pipeline, pre-push and revision-history passages read in full (the article is long; the remaining sections were skimmed by search only). No summarising tool. The page's own revision history says "18 January 2024: Published revised version" (earlier front matter said undated). The repo's [broader note on the article](../../testing-feedback-loop/sources/fowler-continuous-integration.md) covers the rest.

- Speed target, verbatim: "For most projects, however, the XP guideline of a ten minute build is perfectly within reason. Most of our modern projects achieve this." Rationale on the page: "every minute chiseled off the build time is a minute saved for each developer every time they commit". Also on the page: "Most of my colleagues consider a build that takes an hour to be totally unreasonable", and near the end "keep an eye on build times and take action as soon as we start going slower than the ten minute rule".
- Staged pipeline: "The commit build is the build that's needed when someone pushes commits to the mainline. The commit build is the one that has to be done quickly, as a result it will take a number of shortcuts that will reduce the ability to detect bugs." In his two-stage example the first stage runs "more localized unit tests with slow services replaced by Test Doubles" and stays "within the ten minute guideline"; the second stage "do hit a real database and involve more end-to-end behavior. This suite might take a couple of hours to run." The secondary build "may not run after every commit"; a failure there should lead to a new test in the commit build where possible.
- Local step before a push: in his worked example he pulls mainline, merges, builds again and runs the tests before pushing ("Usually this feels superfluous, but this time a test fails"); elsewhere he lists "neglecting to update and build before a push" as a lapse in discipline. The page does not describe an automated pre-push hook.
- Relevance (our inference, not Fowler's): this is the placement guidance closest to a hook gate. The fast stage sits at the developer's push and the slow stage behind it, which suggests a hook gate should run only the fast tier. Fowler writes about human teams and CI servers, not agent hooks.
