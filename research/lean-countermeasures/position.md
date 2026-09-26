# Countermeasures in lean

Findings on what lean means by "countermeasure" and what follows for a kit that maps catalogue entries to ways of making them take effect. Findings only; no kit design and no catalogue entries here.

Evidence quality: the A3 chapter by Shook ([source](sources/lei-shook-a3-chapter.md)) and Rother's handbook ([source](sources/rother-improvement-kata-handbook-pdca.md)) were read directly. LEI lexicon pages and Lean Post articles were read through a fetch summary. Ohno's and Shingo's own books were not read; Ohno is reached through [LEI's 5 whys article](sources/lei-five-whys.md) and Shingo through a [third-party tutorial quoting him](sources/mistakeproofing-shingo-tutorial.md). The [kenji repo](sources/kenji-repo.md) is a practitioner application, not a lean authority.

## What a countermeasure is

A countermeasure is a change proposed to act on an identified cause of a gap between current and target condition, and held as a hypothesis to be checked, not as a final answer. LEI's lexicon contrasts it with a "solution": "unlike 'solutions' that infer a permanent fix, a countermeasure encourages continuous improvement" ([source](sources/lei-value-stream-improvement-lexicon.md)). In the A3 it is the step between analysis of root cause and plan, and it comes with a check: "How will you know if your countermeasures work?" ([source](sources/lei-shook-a3-chapter.md)). Shook describes the recommended countermeasure as often "a simple trial or small experiment" ([source](sources/lei-shook-a3-discovery-post.md)).

## Countermeasure versus fix versus rule

- Fix or solution: implies the problem is closed. A countermeasure stays open until its effect is checked and may be replaced. This is the lean-owned distinction; the sources give no stronger definition than the LEI sentence above.
- Rule: a rule is one possible form a countermeasure takes, and a rule is not a countermeasure until it is tied to a cause and checked. Graban's warning fits: a proposed solution ("We should implement checklists!") prompts "Do we really understand the problem first?" ([source](sources/lei-graban-standardization-countermeasure.md)). Kenji's glossary lists "rule" and "fix" as terms to avoid, and defines a countermeasure as "small, reversible" ([source](sources/kenji-repo.md)); the smallness and reversibility are Kenji's wording, not found in the lean sources read.
- Countermeasures also include short-term containment. Ballé names two aims of immediate countermeasures: protect the customer and return to normal conditions, for example a temporary 100% check ([source](sources/lei-balle-problem-solving.md)). Root-cause countermeasures come after, for recurring problems.

## How a countermeasure is chosen against a root cause

- Sequence: clarify problem, grasp situation, set target, find root cause, then develop countermeasures ([source](sources/lei-balle-problem-solving.md)). The countermeasure is attached to the root cause, not the first-level symptom ([5 whys example](sources/lei-five-whys.md)). The A3 template asks how the countermeasures "affect the root cause".
- Choosing among alternatives is an explicit A3 step ("How will you decide which countermeasures to propose?") and needs agreement from those concerned ([source](sources/lei-shook-a3-chapter.md)). The read sources do not give the selection criteria. A search summary mentioned an evaluation matrix (effectiveness, feasibility, cost, impact, risk); that was not verified in a primary source.
- Rother's improvement kata differs: the unit is an obstacle in the way of a target condition, not a root cause of a past problem, and the step is an experiment with a stated expectation. He warns against "disconnected countermeasures" and shotgun changes, and prefers one change at a time so cause and effect can be seen ([source](sources/rother-improvement-kata-handbook-pdca.md)). Two lean traditions therefore coexist: A3 (analyse cause, select countermeasure) and kata (iterate on obstacles toward a target). Kenji uses the kata frame.

## How the effect is checked

- Check is part of the countermeasure, not an afterthought. LEI: PDCA proposes a change, implements it, measures results, takes appropriate action ([source](sources/lei-lexicon-pdca.md)). Rother frames each cycle as a prediction ("what you expect"), the step, measured evidence, then comparison of actual to expectation ([source](sources/rother-improvement-kata-handbook-pdca.md)).
- Checking needs a measurable target and a stated expectation before the change is made. Kenji encodes this as a criterion checkable "without interpretation" and a check window, with an append-only experiment log including failures ([source](sources/kenji-repo.md)).
- Failure of a countermeasure is information, not proof the target is wrong. Kenji's ADR-0004 separates the goal from the attempts so a failed countermeasure does not reset the work ([source](sources/kenji-repo.md)); the lean sources agree in spirit (adjust and iterate) but do not say this in those words.
- Both results and the process of getting them are evaluated (Ballé step 7).

## Relation to standard work

- Standardization comes after a successful check: Rother's cycle ends "Standardize and stabilize what works"; Ballé's step 8 is "standardize successful processes" ([Rother](sources/rother-improvement-kata-handbook-pdca.md), [Ballé](sources/lei-balle-problem-solving.md)). Standardized work is then "the object of continuous improvement through kaizen" ([source](sources/lei-lexicon-standardized-work.md)), so it is the baseline the next countermeasure changes.
- Standardization is itself a countermeasure, "never the goal" ([source](sources/lei-graban-standardization-countermeasure.md)). Ballé also treats a standard response to deviation as a countermeasure.
- Standard work defines "normal conditions"; a gap from the standard is what triggers a countermeasure. So standard work is both output and input of countermeasures.
- Kenji's status `standardized` (improvements written into standard work) follows this ordering ([source](sources/kenji-repo.md)). Its ADR-0002 shows the failure mode of stopping before Do: countermeasures recorded but never applied.

## Relation to error-proofing (poka-yoke)

- Poka-yoke is a class of countermeasure aimed at errors, not a synonym for it: "simple and inexpensive devices" that help operators avoid mistakes ([source](sources/lei-lexicon-poka-yoke.md)). The LEI page does not use the word countermeasure; the link is our inference from its function.
- Shingo's distinction, as reported secondhand: an error becomes a defect only if not caught; judgment inspection (sorting) is weakest, informative inspection (feedback such as self-checks) is better, and source inspection (checking conditions before the action, often preventing the work until met) is the aim ([source](sources/mistakeproofing-shingo-tutorial.md)). This gives a strength ordering among countermeasures: prevent the error, then detect it at once, then detect it late.
- Jidoka is the related principle: detect an abnormal condition and stop ([source](sources/lei-lexicon-jidoka.md)).
- Poka-yoke fits mistakes made by a person or process that is otherwise correct; it does not by itself address a wrong standard. Sources do not state this limit; it is our reading.

## Implications for a kit mapping catalogue entries to ways of taking effect

These are findings that constrain the kit, not a design.

1. A catalogue entry is closer to a proposed standard or target condition than to a countermeasure. In lean the countermeasure is the concrete change, chosen for a specific cause in a specific setting. The existing glossary use (a way of making an entry take effect: AGENTS.md line, skill, hook, tool) matches lean loosely; it omits the cause it answers and the check on its effect.
2. Selection depends on the cause. Lean chooses the countermeasure from root cause and context, so one entry can warrant different countermeasures in different repos. A fixed entry-to-countermeasure mapping would sit closer to a solution than a countermeasure, unless it is treated as a default to test.
3. Strength ordering from error-proofing applies: preventing (deterministic tool, hook that blocks) over detecting early over instruction-only guidance. Instruction-file lines resemble asking people to be careful, the weakest class in the Shingo ordering. This is an analogy; no source studies AI agents.
4. Each countermeasure needs an expected effect and a way to check it, or it is a rule. Whatever the kit records should let an adopting repo see what to observe.
5. A countermeasure that works becomes part of standard work (the repo's instruction files, hooks, CI); until then it is an experiment and reversible. Kenji's tool-agnostic history (ADR-0001 to 0002) shows the cost of leaving countermeasures unapplied.
6. Lean also says to work one obstacle at a time and change one thing per experiment, which argues against adopting many entries with their countermeasures in one step. Whether this outweighs the cost of slow adoption is a design question, not settled here.

## Where this does not hold or is unverified

- Ohno's and Shingo's books, Rother's Toyota Kata book and Shook's full Managing to Learn were not read; several LEI pages are undated.
- The term's origin at Toyota (translation of the Japanese taisaku) was not verified.
- The claim that Shook recommends "countermeasure" over "solution" comes from a search summary, not a text read; the LEI lexicon sentence is what is verified.
- Applying these to AI agents is our extension; only the kenji repo does so, and it is one practitioner's work.
