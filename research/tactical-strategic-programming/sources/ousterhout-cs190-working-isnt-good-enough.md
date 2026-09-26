---
source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=working
source_date: 2018
researched: 2026-09-26
---

# Ousterhout, CS190 lecture "Working Isn't Good Enough" (Stanford, Winter 2018)

Primary source: the author's own course page, the class the book grew out of. Re-read 2026-09-26: fetched raw with curl (HTTP 200), stripped to text, read in full (the page is a short outline, about 30 lines). Earlier version came from a summariser; all quotes below match the page.

- Tactical programming: "goal is to get the next feature or bug fix working"; a few shortcuts and kludges are accepted if they deliver speed. Page states the result as "Results in bad design, high complexity". The outline also lists "Tactical tornadoes" as a bullet without elaboration.
- Strategic programming: the "primary goal is to produce a great design", asking how easy the code is to evolve. Achieved through "continual small investments".
- Investment level: "as much as you can afford", with "10-20% overhead?" as the figure (also written with a question mark, so a tentative guess). Claimed to "pay for themselves relatively quickly (6-12 months?)". The question mark is in the source, so the payback figure is a guess by the author, not a measurement.
- The page opens: programs evolve continuously (cannot design whole system at once, cannot get the design right first time, requirements change). For the class: "zero tolerance for complexity".
- Core principle: "Working isn't good enough."
- The split is about the programmer's stance toward design and complexity over time. It is not a split by level of abstraction or by who does the work.
