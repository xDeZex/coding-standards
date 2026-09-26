---
source: https://martinfowler.com/articles/continuousIntegration.html
source_date: undated
researched: 2026-09-26
---

# Martin Fowler, "Continuous Integration": build speed and staged builds

Reading method: fetched through a summarising tool, asked only about build speed and staging; quotes as returned, unverified. The page is a revised article and the fetch gave no date. The repo's [broader note on the article](../../testing-feedback-loop/sources/fowler-continuous-integration.md) covers the rest.

- Speed target: "the XP guideline of a ten minute build", which he says most of his modern projects achieve, because developers integrate often and time saved compounds.
- Staged pipeline: the commit build is what runs when someone pushes to mainline; it runs fast, mostly unit tests with external services doubled. A second-stage build runs tests that hit a real database and end-to-end behaviour, which "might take a couple of hours".
- Local pre-push step: developers update from mainline, resolve conflicts, build locally, and push only if it passes.
- Relevance: this is the placement guidance closest to a hook gate. The fast stage sits at the developer's push and the slow stage behind it. It suggests a hook gate should run only the fast tier. This is our inference; Fowler writes about human teams and CI servers, not agent hooks.
