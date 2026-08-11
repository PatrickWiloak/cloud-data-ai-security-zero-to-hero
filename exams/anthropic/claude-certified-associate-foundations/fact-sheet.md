---
last-updated: 2026-08-11
---

# CCAO-F - Fact Sheet

## Quick Reference

| Detail | Info |
|---|---|
| Exam Code | CCAO-F |
| Full Name | Claude Certified Associate - Foundations |
| Provider | Anthropic |
| Duration | 120 minutes |
| Questions | 60 multiple-choice and multiple-response |
| Passing Score | 720 / 1000 |
| Cost | $99 USD |
| Delivery | Pearson VUE - online proctored or test center |
| Validity | 12 months |
| Level | Foundational |
| Prerequisites | None |
| Released | July 2026 |
| Registration | Anthropic Partner Academy (requires free Claude Partner Network membership, company email) |
| Badge | Digital badge via Credly by Pearson |
| Renewal | Free non-proctored Partner Academy assessment if renewed on time |
| Retakes | 14 days after attempt 1, 30 days after attempt 2, 90 days after attempt 3; max 4 attempts per rolling 12 months |
| Reschedule | Up to 24 hours before the appointment |

---

## Domain Weights

Official blueprint v1.0, effective July 2026:

| Domain | Weight | Key Focus |
|---|---|---|
| 1. Output Evaluation and Validation | 21% | Verifying, fact-checking, and improving Claude's outputs |
| 2. Workflow Integration and Solution Design | 16% | Fitting Claude into real business workflows |
| 3. Governance, Risk, and Responsible Use | 15% | Data handling, confidentiality, disclosure, appropriate use |
| 4. Prompting and Task Execution | 14% | Clear instructions, context, iteration, task framing |
| 5. Product and Model Selection | 12% | Choosing the right Claude product, plan, and model |
| 6. Configuration and Knowledge Management | 12% | Projects, custom instructions, knowledge bases, connectors |
| 7. Troubleshooting and Optimization | 10% | Diagnosing weak outputs and fixing them |

---

## Official Documentation Links

### Product Documentation (Claude.ai)

**[📖 Claude Help Center](https://support.claude.com)** - official product documentation for Claude.ai, Projects, Artifacts, plans, and integrations

**[📖 Claude.ai](https://claude.com)** - product home: plans, features, and the Claude apps

**[📖 Claude Partner Network](https://claude.com/partners)** - free membership required to register for partner certifications

### Developer Documentation (concept-level reading for this exam)

**[📖 Anthropic Documentation Home](https://docs.anthropic.com)** - documentation portal; the prompting guides apply to Claude.ai use as much as API use

**[📖 Models Overview](https://docs.anthropic.com/en/docs/about-claude/models)** - the Claude model family (Opus, Sonnet, Haiku), capabilities and trade-offs

**[📖 Prompt Engineering Overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)** - the official prompting guide; the techniques transfer directly to Claude.ai chat

### Training and Certification

**[📖 Anthropic Partner Academy](https://anthropic-partners.skilljar.com/page/partner-certifications)** - certification catalog, free official prep courses, and exam registration

**[📖 Pearson VUE - Anthropic](https://www.pearsonvue.com/us/en/anthropic.html)** - exam scheduling, test-center lookup, online-proctoring requirements

---

## Domain 1 - Output Evaluation and Validation (21%)

### Key Facts

- **Outputs are drafts** - Claude's output is a starting point to review, not a finished deliverable. The exam's biggest domain tests this mindset.
- **Hallucination** - Claude can state incorrect information fluently and confidently. Fluency is not accuracy.
- **Verify by risk** - the depth of verification should match the stakes. A brainstorm needs a skim; a client deliverable or a number in a report needs source checking.
- **Check the checkables** - names, dates, figures, quotes, citations, and URLs are the highest-risk elements. Verify them against source material.
- **Grounding** - giving Claude the source documents and asking it to answer only from them reduces (but does not eliminate) fabrication.
- **Ask for citations** - when Claude works from provided documents, ask it to quote or cite the passage supporting each claim, then spot-check the quotes.
- **Self-review has limits** - asking Claude to check its own work catches some errors, but is not independent verification.
- **Human accountability** - the person who ships the deliverable owns its accuracy, not the tool.

### Practical Validation Techniques

1. Ask Claude to list its assumptions and confidence level for key claims.
2. Ask "what would make this wrong?" to surface weak points.
3. Re-run the task with a rephrased prompt and compare answers; divergence flags uncertainty.
4. Paste source material and ask Claude to verify its earlier answer against it.
5. For math and data summaries, spot-check a sample of figures by hand or with the analysis tool.
6. For anything customer-facing, legal, financial, or medical: human expert review before shipping.

---

## Domain 2 - Workflow Integration and Solution Design (16%)

### Key Facts

- **Start from the task, not the tool** - identify the workflow step where Claude adds value (drafting, summarizing, extracting, transforming, reviewing), then design around it.
- **Human-in-the-loop** - high-stakes steps keep a human decision point; Claude accelerates, the human approves.
- **Good fit tasks** - first drafts, summarization, meeting notes, research synthesis, rewriting for audience, data extraction, brainstorming, review checklists.
- **Poor fit tasks** - final authority on facts, decisions requiring accountability, tasks needing real-time data Claude does not have access to, precise calculations without the analysis tool.
- **Projects for repeat work** - recurring workflows belong in a Project with standing instructions and reference files, not re-explained in every chat.
- **Artifacts for deliverables** - documents, reports, and simple interactive pages Claude builds in a side panel you can iterate on.
- **Integrations** - Claude for Slack, browser extension, desktop apps, and connectors bring Claude to where the work happens instead of copy-pasting.
- **Pilot before rollout** - test a Claude-assisted workflow on a small scale, measure quality and time saved, then expand.

---

## Domain 3 - Governance, Risk, and Responsible Use (15%)

### Key Facts

- **Know your plan's data terms** - consumer and commercial plans have different data-handling terms. Client and company data belongs in an appropriately governed plan (Team/Enterprise), under your organization's policy.
- **Confidentiality first** - do not paste client-confidential, regulated, or personal data into any AI tool outside the terms your organization and client have agreed to.
- **Data minimization** - share the minimum needed for the task; redact names, identifiers, and sensitive fields when they are not needed.
- **Disclosure** - follow your organization's and client's rules on disclosing AI assistance in deliverables.
- **Bias awareness** - review outputs used in decisions about people (hiring, performance, credit) with extra care; AI output can reflect bias in training data or prompts.
- **IP and attribution** - treat Claude's output as your organization's responsibility; check that quoted or closely paraphrased content is attributed.
- **Usage policy** - Anthropic's usage policies prohibit certain uses; company AI policies typically add more. The stricter rule wins.
- **Auditability** - for regulated work, keep a record of what was AI-assisted and how it was verified.

### Decision Rule

Before pasting anything into Claude, ask: whose data is this, what plan and terms cover this workspace, and would the data owner be comfortable with this use? If any answer is unclear, stop and ask.

---

## Domain 4 - Prompting and Task Execution (14%)

### Key Facts

- **Be clear and specific** - state the task, the audience, the format, the length, and the constraints. Vague prompts produce generic output.
- **Give context** - background, source material, and examples matter more than clever wording.
- **Show, don't describe** - one or two examples of the desired output (few-shot) beat a paragraph describing it.
- **Assign a role** - "You are a management consultant preparing a board summary" steers tone and depth.
- **Break big tasks down** - outline first, then draft sections; or extract first, then analyze. Stepwise beats one giant prompt.
- **Iterate in conversation** - treat the first response as round one. Give specific feedback ("shorter, more formal, lead with the recommendation") instead of starting over.
- **Ask Claude to think first** - for complex analysis, asking for reasoning or a plan before the answer improves quality.
- **Specify the output format** - table, bullet list, email, one-pager. Claude follows format instructions well.

### A Reliable Prompt Skeleton

1. Role and audience
2. Task, in one clear sentence
3. Context and source material
4. Constraints (length, tone, what to exclude)
5. Output format
6. Example of the desired output (optional but powerful)

---

## Domain 5 - Product and Model Selection (12%)

### Key Facts

- **Claude.ai chat** - general-purpose assistant: drafting, analysis, Q&A, file upload, web search, analysis tool.
- **Projects** - persistent workspaces with custom instructions and knowledge files; for recurring workstreams and shared team context.
- **Artifacts** - dedicated output panel for documents, code, and interactive content that you iterate on beside the chat.
- **Claude Code** - Anthropic's agentic command-line tool for software work. Know what it is and that it targets developers; you will not be tested on using it.
- **Claude in Slack and other integrations** - Claude embedded in the tools where teams already work.
- **Model family** - Opus (most capable, deep reasoning), Sonnet (balanced default for most work), Haiku (fastest and cheapest, high-volume simple tasks).
- **Model choice heuristic** - default to the balanced model; step up for complex multi-step analysis where quality dominates; step down for speed and volume on simple tasks.
- **Plans** - Free, Pro, Team, and Enterprise differ in usage limits, features, collaboration, and admin/governance controls. Business use of business data belongs on business plans.

---

## Domain 6 - Configuration and Knowledge Management (12%)

### Key Facts

- **Project instructions** - standing instructions attached to a Project apply to every chat in it; the right home for role, style, and process guidance you would otherwise repeat.
- **Project knowledge** - files uploaded to a Project are available to all chats in it; keep them current and curated, not a dumping ground.
- **Personal preferences/custom instructions** - account-level style preferences apply across chats.
- **Garbage in, garbage out** - outdated or contradictory knowledge files produce confidently wrong answers; assign an owner and refresh cadence.
- **Scope knowledge tightly** - a Project per workstream or client with only its own material beats one giant Project mixing everything.
- **Connectors** - integrations that let Claude reach live sources (drives, docs, tools) so answers use current data instead of stale uploads; enabled per organization policy.
- **Sharing** - Team/Enterprise Projects can be shared so a whole team benefits from one well-configured setup.
- **Context limits** - Claude reads a lot but not unlimited amounts; enormous knowledge bases dilute focus. Curate.

---

## Domain 7 - Troubleshooting and Optimization (10%)

### Key Facts

- **Diagnose before re-prompting** - identify the failure type: wrong facts, wrong format, wrong tone, wrong scope, refused task, or lost context.
- **Wrong facts** - ground with source documents and ask for citations; verify externally.
- **Wrong format or tone** - add explicit format instructions and an example; state the audience.
- **Wrong scope** - the prompt was ambiguous; state what to include and exclude.
- **Generic output** - add context and constraints; generic prompts get generic answers.
- **Long-chat drift** - very long conversations lose earlier detail; summarize the state and start a fresh chat, or move standing context into a Project.
- **Refusals** - rephrase to clarify legitimate intent and context; do not try to trick the model. If the task is genuinely against policy, the refusal is the correct outcome.
- **Inconsistent results across runs** - normal model behavior; pin down format and criteria in the prompt, or template the task in a Project.
- **Optimization** - the highest-leverage fixes are usually better context and clearer instructions, not a different model.

---

## Exam Tips

### High-Frequency Topics

1. Matching verification depth to output risk (Domain 1 is 21% - the biggest)
2. Which product feature fits a scenario: chat vs Project vs Artifact vs integration
3. Data-confidentiality judgment calls (what can be pasted where, and under which plan)
4. Fixing a weak output: what change to make first
5. Opus vs Sonnet vs Haiku trade-offs in plain business terms
6. Project instructions vs project knowledge vs personal preferences
7. When a human must stay in the loop
8. Prompt improvement: identifying what is missing from a vague prompt

### Common Exam Traps

1. **"Claude said it, so it's done"** - always the wrong answer. Verification steps beat blind trust.
2. **Over-verification** - the exam also punishes gold-plating; a brainstorm does not need a fact-check audit. Match effort to stakes.
3. **Re-prompting from scratch** - iterating with specific feedback usually beats starting over.
4. **Biggest model always** - "use the most capable model" is wrong when the scenario stresses speed, volume, or cost on a simple task.
5. **Pasting client data into a personal account** - governance questions often hide the plan/terms detail in the scenario.
6. **Tricking refusals** - any option that reworks a prompt to evade a policy refusal is wrong.
7. **One giant Project** - scoped Projects per workstream beat a single catch-all.
8. **Multiple-response questions** - read how many answers are required; partial selections score as wrong.

### Answer Selection Strategy

1. Read the full scenario; the deciding constraint is often in the last sentence.
2. Identify the domain being tested.
3. Eliminate the extremes first: "trust the output fully" and "never use AI for this" are both usually wrong.
4. Prefer answers that combine a practical Claude workflow with a proportionate human check.
5. On governance questions, when in doubt, choose the more protective option that still gets the work done.
