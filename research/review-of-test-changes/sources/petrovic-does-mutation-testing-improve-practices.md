---
source: https://arxiv.org/abs/2103.07189
source_date: 2021-03
researched: 2026-09-26
---

# Does mutation testing improve testing practices? (Petrovic, Ivankovic, Fraser, Just, ICSE 2021)

Primary source: peer-reviewed study of Google's mutation testing in code review; abstract only.

- Analysed about 15 million mutants.
- Finding: "developers using mutation testing write more tests, and actively improve their test suites with high quality tests such that fewer mutants remain."
- Analysis of real high-priority faults showed a correlation between mutants and real bugs; applying mutation testing to the changes that introduced them would have surfaced live mutants able to prevent the bugs.
- Weakness for our question: it shows a mutation signal changes human authors' behaviour and relates to real faults; it does not test mutation score as a guard against tests being weakened, and the developers were not adversarial or agents.
