# Coding Standards

A thinking space where a human and an AI research, discuss and document coding standards for software development with AI. Its outputs are meant to be carried into other repos by pointing an AI at this one.

## Language

**Kit**:
The portable set of artifacts this repo produces for use in other repos.
_Avoid_: Toolkit, package, bundle

**Catalogue**:
The source-of-truth collection of candidate instructions, each with its rationale and the conditions under which it applies, and each traceable to its sources through the position it comes from.
_Avoid_: Library, rulebook, database

**Catalogue entry**:
One candidate instruction in the catalogue, coming from a position.
_Avoid_: Rule, item, standard

**Countermeasure**:
A change proposed to act on an identified cause of a problem, held as a hypothesis until its effect is checked. The term comes from lean. In coding it is often a way of making a catalogue entry take effect in a repo, built from one or more controls, but not always.
_Avoid_: Enforcement

**Harness**:
Everything around the model that steers and checks a coding agent: instruction files, skills, agent hooks, git hooks, tools, tests. A system that can be improved, and the countermeasure is how.

**Control**:
One part of the harness that regulates the agent, such as an AGENTS.md, a skill, an agent hook, a git hook, a linter or a review. What a countermeasure is built from; a control is not a countermeasure until it is tied to a cause and checked. The term is Böckeler's ([Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html)).
_Avoid_: Mechanism, way, type

**Guide**:
A feedforward control: steers the agent before it acts, for example an AGENTS.md or a skill.

**Sensor**:
A feedback control: observes after the agent acts so it can self-correct, for example a linter, a test or a git hook.

**Computational control**:
A control that is deterministic and run by the CPU: tests, linters, type checkers.

**Inferential control**:
A control that uses a model to judge: AI code review, LLM as judge. Slower and non-deterministic.

**Human guide**:
Writing about how a human should think with, operate and value working with AI.
_Avoid_: Manual, handbook

**Agent hook**:
A script the agent harness runs at a fixed point in the agent's flow, such as before a tool call or at the end of a turn. Exists only where the harness offers it and varies by harness. Can steer (guide) or observe (sensor).
_Avoid_: Hook (ambiguous with git hook)

**Git hook**:
A script git runs at a git event, such as before a commit. Works the same for an agent and a human, but only sees git operations.
_Avoid_: Hook (ambiguous with agent hook)

**Control handbook**:
A file in `kit/controls/` about one control: what it is, what it is good and bad at, and how it compares to other controls along shared dimensions, so a reader can reason about whether it fits a cause. Written in general terms, not as a list of problems the control solves.
_Avoid_: Control guide (a guide is itself a control), manual, datasheet, profile

**Skills list**:
A curated list of pointers to skills that live elsewhere. This repo does not store skill content.
_Avoid_: Skill library

**Source note**:
A cited record of what a source (book, paper, talk, post) says, kept separate from our opinion of it.
_Avoid_: Research note, summary

**Lead**:
A pointer to a person, company, idea, book or talk worth a look, kept in `research/leads.md` to guide research and to give humans somewhere to look next. Records no claims.
_Avoid_: Reference, recommendation

**Conclusion**:
A research agent's synthesis of the source notes for a topic, written for the human to read and discuss. Not our opinion; it becomes a position only after the human has discussed it and written the position.
_Avoid_: Summary, findings

**Position**:
Our stance on a topic, written by the human after discussing the conclusion, with its trade-offs, linking to the source notes it rests on.
_Avoid_: Verdict, opinion

**Source**:
A book, link or other origin of a claim, recorded with the date of the source and the date we researched it.
_Avoid_: Reference, citation

**Adoption**:
An AI, pointed at this repo from a target repo, inspecting that repo and proposing a selection from the catalogue for the human to confirm before anything is written.
_Avoid_: Installation, sync

**Blueprint**:
The decided shape of this repo and its kit, before any topic is researched.
_Avoid_: Spec, design

**Tactical**:
Code-level practice: how code is written, structured and checked. The level AI is good at, so increasingly delegated to it. A way of thinking, not a tag or folder.
_Avoid_: Low-level, implementation

**Strategic**:
Architecture, planning, process and the roles of humans and agents. The level humans increasingly focus on. A way of thinking, not a tag or folder.
_Avoid_: High-level, management
