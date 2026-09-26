# Making AI write better

Findings on the question "has anyone found out how to make AI write better?": prompting, style guidance, fine-tuning, preference optimisation, critique-and-revise loops, evaluation, and the known failure modes. Findings only; no kit design, no catalogue entries, no recommendations here. The user asked for one file; this repo's convention is a conclusion plus one note per source, so the citations below link to the notes in `sources/`, and each note carries the primary URL.

## Short answer

Partly. There is measured evidence that the flat, samey, cliched quality of default LLM prose is real, has identifiable causes, and can be reduced. The evidence that works best is narrow, and most of what people actually do (prompt tips) has the weakest evidence.

- Strongest positive result: fine-tuning on one author's complete works made a frontier model's imitation preferred by expert and general readers over expert human writers ([Chakrabarty et al.](sources/chakrabarty-fine-tuning-author-style.md)). One study, abstract-level read, prompting alone lost to humans in the same study.
- Well supported failure mode: preference tuning (RLHF, DPO) reduces diversity and drives word overuse ([Kirk et al.](sources/kirk-rlhf-generalisation-diversity.md), [Padmakumar and He](sources/padmakumar-he-writing-with-lms-diversity.md), [Juzek and Ward](sources/juzek-ward-word-overuse-alignment.md)); models also resemble each other, not only themselves ([Artificial Hivemind](sources/artificial-hivemind-homogeneity.md)).
- Methods that address it (verbalized sampling, deviation-aware DPO, Antislop) report large gains, but are each from one group, mostly with abstract-level support, and some authors run the benchmark that scores them.
- Prompt advice from vendors (examples, roles, defining the anti-pattern) is consistent across vendors but comes with no measurements. The one persona study tested factual questions, not prose.
- Evaluation is the weak link: LLM judges are biased (length, position, familiarity) and one study found LLM judges did not correlate with experts on creative writing. Most writing benchmarks are LLM-judged and few report validation against human readers.

## How to read the evidence

Nearly every arXiv source below was read through a page-to-Markdown tool that summarises with a small model, on the abstract page only. Claims are therefore abstract-level, and numbers should be rechecked in the papers before reliance. The vendor guides are first-party documentation and self-report; none of them contains data. Two 2026 arXiv items surfaced in search results (2608.23705 on limits of automatic creativity evaluation, and 2606.19544 on judge validity) were not read; the first PDF could not be parsed, so they are not relied on.

## Prompting

- Examples. Anthropic calls examples "one of the most reliable ways" to steer tone, format and structure and recommends 3-5, diverse enough not to induce unintended patterns ([Anthropic](sources/anthropic-prompting-best-practices-writing.md)). Google says to "always include few-shot examples" ([Google](sources/google-gemini-prompting-strategies.md)); OpenAI says to show diverse inputs ([OpenAI](sources/openai-prompt-engineering-guide.md)). Support: three vendors agree, no measurement of writing quality.
- Examples for imitating a person. An EMNLP 2025 study of over 40,000 generations found in-context imitation works on formal text (news, email) and fails on informal writing (blogs, forums), and that the number of examples matters ([Wang et al.](sources/catch-me-if-you-can-style-imitation.md)). This is measured, and it is a limit on what pasted samples achieve.
- Style guidance and naming the anti-pattern. Anthropic's Fable 5.1 guide says to define the failure ("mannered prose") in a prompt, or simply ask to remove it, and says to prefer the positive instruction over "do not" ([Fable 5.1](sources/anthropic-prompting-fable-5-1-writing-density.md), [best practices](sources/anthropic-prompting-best-practices-writing.md)). Vendor recommendation for its own model, unmeasured. Whether a style guide pasted into context improves human-judged quality was not found in a primary study.
- Personas. The one large test found personas in system prompts did not improve accuracy over no persona ([Zheng et al.](sources/persona-prompts-do-not-improve.md)). It tested factual questions, so it neither supports nor refutes persona use for voice. Vendor guides still recommend roles for tone.
- Sampling-style prompts. Verbalized Sampling (ask for several responses with probabilities) reports 1.6-2.1x diversity on poems, stories and jokes, with more gain on stronger models ([Zhang et al.](sources/verbalized-sampling-mode-collapse.md)). Training-free and cheap; it targets diversity, not per-piece quality; single group, abstract-level.

## Fine-tuning and preference optimisation

- Author fine-tuning: see above. It reports detection as AI dropped from 97% to 3% and cost about 81 USD per author ([Chakrabarty et al.](sources/chakrabarty-fine-tuning-author-style.md)). Peer-review status unchecked; the paper is entangled with a copyright argument.
- Diversity-aware post-training: adding a "deviation" term to DPO/ORPO gave an 8B model with human-dataset-level diversity and GPT-4o-level judged quality ([Chung et al.](sources/chung-diverse-creative-writing-post-training.md)).
- Slop-targeted tuning: FTPO reports about 90% slop reduction with benchmarks held, and reports DPO degraded writing ([Antislop](sources/antislop-framework.md)). The lead author also runs EQ-Bench, whose slop score uses a similar concept ([EQ-Bench](sources/eqbench-creative-writing-v3.md)); independent replication was not found.
- RL for writing: Writing-Zero (RL with a generative reward model, claimed resistance to reward hacking, arXiv 2506.00103) and LongWriter (SFT data for long outputs, 2408.07055) surfaced but were read from abstract summaries only in this session and have no source note; treat them as leads, not findings.

## Draft, critique, revise

- Self-Refine reports about 20% absolute average improvement across seven tasks, humans preferring refined output ([Madaan et al.](sources/self-refine.md)). The tasks are mostly not prose quality.
- Counter-evidence for reasoning: models without external feedback often fail to self-correct and can get worse ([Huang et al.](sources/huang-llms-cannot-self-correct-reasoning.md)). Scope is reasoning, not writing.
- For prose specifically, professional writers built a seven-category taxonomy of LLM writing faults and a corpus of expert edits, and found automatic editing promising but experts still preferred human edits ([LAMP](sources/lamp-can-ai-writing-be-salvaged.md)). This suggests a critique step using a fault list has a target, but the primary source read here gives no effect size for it. No study found comparing a revise loop with a single strong prompt on human-judged writing.

## Failure modes

- Mode collapse and homogenisation: across-model similarity exceeds within-model repetition ([Artificial Hivemind](sources/artificial-hivemind-homogeneity.md)); a controlled experiment found InstructGPT-assisted essays became more alike across authors, GPT-3 did not ([Padmakumar and He](sources/padmakumar-he-writing-with-lms-diversity.md)); RLHF lowers diversity versus SFT ([Kirk et al.](sources/kirk-rlhf-generalisation-diversity.md)); one proposed cause is typicality bias in preference data ([Zhang et al.](sources/verbalized-sampling-mode-collapse.md), a hypothesis of that paper).
- Slop and word overuse: some phrases are over 1,000x more frequent than in human text ([Antislop](sources/antislop-framework.md)); overuse was partly traced to RLHF and rater preference, and raters in the authors' replication preferred the overused words ([Juzek and Ward 2025](sources/juzek-ward-word-overuse-alignment.md), [2024](sources/juzek-ward-delve-lexical-overrepresentation.md)). Word bans are narrow: a search-result summary (unverified at its paper) said "delve" fell after being publicised while other markers kept rising.
- Quality gap: LLM stories passed 3-10x fewer expert creativity tests than professional stories, and no model led on writing quality in another study ([Torrance test](sources/torrance-test-art-or-artifice.md), [LAMP](sources/lamp-can-ai-writing-be-salvaged.md)). Both used 2023-2024 models; newer models were not tested there.

## Evaluation

- LLM judges agree with humans over 80% on general chat, but show position, verbosity and self-enhancement bias ([Zheng et al.](sources/mt-bench-llm-as-judge.md)). Length bias is large enough that controlling it moved Arena correlation from 0.94 to 0.98 ([Dubois et al.](sources/length-controlled-alpacaeval.md)). Judges prefer lower-perplexity, more familiar text ([Wataoka et al.](sources/self-preference-bias-perplexity.md)), which can reward the very text readers call slop.
- For creative writing, LLM judges did not positively correlate with expert assessments ([Torrance test](sources/torrance-test-art-or-artifice.md)), and judges, reward models and evaluators align poorly with humans on open-ended prompts ([Hivemind](sources/artificial-hivemind-homogeneity.md)).
- Benchmarks: [WritingBench](sources/writingbench.md) (six domains, 100 subdomains, query-specific LLM criteria, a fine-tuned critic) and [EQ-Bench Creative Writing v3](sources/eqbench-creative-writing-v3.md) (LLM-judged rubric and Elo, plus repetition and slop metrics; self-declared uncontrolled biases including self-bias toward Anthropic models, and no human-validation data found on its About page). The WritingBench critic's agreement with humans was not captured.

## Gaps

- No primary study found that isolates a style guide in context against human-judged prose.
- No study found comparing draft-critique-revise loops with a single well-written prompt on writing quality.
- No independent replication found for verbalized sampling, Antislop or the deviation-based DPO work.
- Findings on 2023-2024 models may not carry to current ones; vendors state that current models write with fewer stock phrases, unmeasured.
