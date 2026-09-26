# Countermeasures in AI coding

Countermeasure is the lean idea, and it fits AI coding well. The harness is the most important part of AI coding, and the harness is a system that can be improved. A countermeasure is how we improve it: a change aimed at a specific problem, held as a hypothesis until we have checked its effect ([LEI lexicon](sources/lei-value-stream-improvement-lexicon.md), [Shook](sources/lei-shook-a3-chapter.md)). In coding it is often a way of making a catalogue entry take effect, such as an AGENTS.md line, a skill, a hook, a test or a CI check, but not always.

## A countermeasure is a change to the system, not a message to the AI

Telling an AI it did something wrong is useless, because it will not remember next session. A prompt the human writes for one session, or a correction when something goes wrong, is not a countermeasure, because it is not a system. It is the same as a Toyota worker working differently instead of updating the standard work, or fixing a problem from the previous station without fixing the cause upstream ([Graban](sources/lei-graban-standardization-countermeasure.md)). A countermeasure lives where the agent meets it every time: an instruction file, a skill, a hook, a check.

Instructions the agent reads while working are the weak kind of countermeasure, since they ask the AI to be careful ([Shingo](sources/mistakeproofing-shingo-tutorial.md)). They are still good when they are specific and used for the right things. Where a deterministic tool can prevent or catch the error, prefer it.

## Record the problem, the countermeasure and the hoped outcome

A ticket that states the problem, the countermeasure and the hoped outcome is a good start, and it is followed up later. Keep it light and do not overspecify. Without a stated outcome and a follow-up, a countermeasure is just a rule ([Rother](sources/rother-improvement-kata-handbook-pdca.md)).

## Check the effect with both metrics and prose

There is a lot going on in AI coding, so cause and effect are hard to see. That makes measuring the effect of a change important. The outcome can be deterministic, prose or both, depending on the problem. Deterministic checks are really good and should be used where possible: CRAP score, tokens used in a session, the time a session takes. AI is also good at checking prose, so some outcomes fit better as prose.

A metric can be gamed. When I added a CRAP check with a max of 6 and 100% coverage, the AI made shallow modules. Raising the max to 10 improved it. So a metric is a proxy, and the human's knowledge of what good code looks like, for example that deep modules are good, is what spots this with a spot check. This is strategic work and the human's role. Stating the goal as both a metric and prose in the ticket is one solution. Which way to do it depends on how you want to work; the CRAP case is one example, not the method.

## The human's role depends on how much the human is involved

AI should write the tickets and do the work, and humans should not be writing this by hand. It should not be left entirely to AI, because humans still have the strategic advantage in seeing when a metric no longer tracks the goal. It would be great if the AI fixed its own problems, and setups that do this exist. It is more advanced, and it depends on how you use AI, how fast you want to go and whether the AI works by itself. A human can watch the AI work all of the time, some of the time or never, and that involvement affects how the countermeasures are set up.

## What this repo does with countermeasures

This repo does not ship countermeasures. A countermeasure is chosen for a specific problem in a specific repo, so a fixed mapping from entry to countermeasure would be a solution, not a countermeasure. This repo describes the different ways of making a countermeasure (skills, hooks, tests and so on) and keeps a list of entries found to be good to have in AI coding.

Adoption starts with a setup where many entries are applied together. An empty repo with no agent instructions, tools or checks produces worse results, and that is known. After the setup, when a repo has a specific problem, a human reading the guide or an AI reading the catalogue looks for a countermeasure for it. This departs from lean's one change at a time, which is sound for improving an existing process but not for starting from nothing.

## Where this does not hold

- The lean sources do not study AI agents. Applying them here is my extension, and the only AI application in the sources is [one practitioner's repo](sources/kenji-repo.md).
- The ordering of prevent, then detect early, then instruct is an analogy from error-proofing, not something shown for AI agents.
- The CRAP example is a single case from my own work.
