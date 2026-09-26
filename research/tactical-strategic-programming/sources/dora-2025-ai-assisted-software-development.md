---
source: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
source_date: 2025-09-23
researched: 2026-09-26
---

# 2025 DORA State of AI-assisted Software Development report

How read this time: the launch blog post was fetched with curl and read in full; the dora.dev report landing page was fetched with curl; and the full report PDF (v. 2025.2, about 7,500 lines of extracted text) was downloaded from services.google.com and converted with pdftotext. Read: executive summary, the foreword, the "Exploring AI's relationship to key outcomes" summary, the code quality section and the AI capabilities model list. Other chapters were checked with keyword search only. This pass corrected several claims from the earlier, summariser-based note (marked below).

Vendor-run survey research (Google Cloud / DORA). Survey and qualitative data "from more than 100 hours of qualitative data and survey responses from nearly 5,000 technology professionals" (report); survey conducted between 13 June and 21 July 2025. Self-reported. The report itself says it speaks of "comparisons" rather than causal "effects".

- AI adoption is positively associated with software delivery throughput and product performance ("Unlike last year"), and still associated with higher software delivery instability. Report: "This suggests that while teams are adapting for speed, their underlying systems have not yet evolved to safely manage AI-accelerated development."
- Blog: "Without robust control systems, like strong automated testing, mature version control practices, and fast feedback loops, an increase in change volume leads to instability."
- Corrected: the "loosely coupled architectures see gains, tightly coupled systems see little or no benefit" statement, which the earlier note listed as a survey finding, appears in the blog and in the report's foreword as an Adidas gen-AI pilot case study (teams in loosely coupled architectures with fast feedback loops reported "productivity gains of 20% to 30%, as measured by increases in commits, pull requests, and overall feature-delivery velocity"; teams tightly coupled to ERP systems with slow feedback saw little or no benefit). It is a company anecdote, not a survey result.
- Newly added: the report finds AI adoption associated with higher code quality (the outcome is listed among the positive associations "holding steady since 2024"), and in the survey 59% perceive AI as having improved their code quality, 30% no impact, 10% a negative impact. This is perception, and cuts against the GitClear and preprint findings elsewhere in this topic.
- Headline (landing page and report): "AI's primary role is as an amplifier, magnifying an organization's existing strengths and weaknesses"; "The greatest returns on AI investment come not from the tools themselves, but from a strategic focus on the underlying organizational system: the quality of the internal platform, the clarity of workflows, and the alignment of teams." The word "strategic" here means organisational strategy, not Ousterhout's sense.
- Corrected: the capability model has seven capabilities: clear and communicated AI stance, healthy data ecosystems, AI-accessible internal data, strong version control practices, working in small batches, user-centric focus, quality internal platforms. The earlier note's list ("foundational practices, safety nets", "focus on end users", "internal platform", "clear AI policies") was mixed up with the blog's six-item "where leaders should get started" list.
- Other figures: 90% of respondents use AI at work and over 80% believe it raised their productivity; 30% report little or no trust in AI-generated code; 90% of organisations have adopted platform engineering.
- Bearing on the split: supports the strategic side in the organisational sense (platform, workflow and process determine outcomes). It is survey-based association, not a test of who does tactical work.
