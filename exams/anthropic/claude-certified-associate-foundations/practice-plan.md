---
last-updated: 2026-08-11
---

# CCAO-F - Practice Plan

## Overview

A 3-4 week plan for the Claude Certified Associate - Foundations exam. It assumes you already use Claude at least casually at work. If you are brand new to Claude, add a week of daily hands-on use before starting.

**Time commitment:** 1-2 hours per day, 5 days per week. This is a foundational exam about applied judgment; daily hands-on practice with Claude matters more than long reading sessions.

**Before Week 1:**

- [ ] Join the [Claude Partner Network](https://claude.com/partners) (free, company email required)
- [ ] Get access to [Anthropic Partner Academy](https://anthropic-partners.skilljar.com/page/partner-certifications) and locate the CCAO-F prep courses
- [ ] Make sure you have day-to-day access to Claude (ideally on your organization's Team/Enterprise workspace)

---

## Week 1 - Products, Prompting, and Daily Use

**Focus:** Domain 5 (Product and Model Selection - 12%) and Domain 4 (Prompting and Task Execution - 14%)

### Partner Academy

- [ ] Start the official CCAO-F prep course track in Partner Academy
- [ ] Review the official exam guide / blueprint for CCAO-F

### Reading

- [ ] Read [notes/05-product-and-model-selection.md](notes/05-product-and-model-selection.md)
- [ ] Read [notes/04-prompting-and-task-execution.md](notes/04-prompting-and-task-execution.md)
- [ ] Skim the [Prompt Engineering Overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering) - focus on clarity, examples, and role prompting
- [ ] Skim the [Models Overview](https://docs.anthropic.com/en/docs/about-claude/models) for the current model tiers

### Hands-On (use your real work where policy allows)

- [ ] Draft 3 real work documents with Claude using the full prompt skeleton (role, task, context, constraints, format)
- [ ] Take one weak first draft and improve it purely through iterative feedback (no restart)
- [ ] Upload a document and a spreadsheet; try summarization, extraction, and the analysis tool
- [ ] Create one Artifact deliverable and iterate on it 3+ times
- [ ] Try the same task on two model tiers and compare quality, speed, and fit

### Week 1 Self-Check

- [ ] Can you name the right product surface (chat / Project / Artifact / integration / connector) for five different scenarios?
- [ ] Can you explain Opus vs Sonnet vs Haiku trade-offs in one sentence each?
- [ ] Can you list the six parts of a strong prompt from memory?

---

## Week 2 - Evaluation, Validation, and Governance

**Focus:** Domain 1 (Output Evaluation and Validation - 21%) and Domain 3 (Governance, Risk, and Responsible Use - 15%) - together over a third of the exam

### Partner Academy

- [ ] Continue the CCAO-F prep courses (evaluation and responsible-use modules)

### Reading

- [ ] Read [notes/01-output-evaluation-and-validation.md](notes/01-output-evaluation-and-validation.md) - the biggest domain, read it twice
- [ ] Read [notes/03-governance-risk-and-responsible-use.md](notes/03-governance-risk-and-responsible-use.md)
- [ ] Read your own organization's AI usage policy end to end (the exam mindset mirrors real policies)

### Hands-On

- [ ] Ask Claude a question you know the answer to in depth; grade the output and find its weakest claim
- [ ] Upload a source document, ask for a cited summary, and verify every citation against the source
- [ ] Deliberately ask about something after Claude's training cutoff without web search; observe the failure mode, then repeat with web search and verify the cited pages
- [ ] Ask Claude to list its assumptions and confidence on a real analysis task
- [ ] Practice redaction: take a document with names/identifiers and prepare a minimized version for an AI task
- [ ] Write the verification checklist you would apply to a client-facing deliverable

### Week 2 Self-Check

- [ ] Can you match verification depth to four different risk levels?
- [ ] Can you name the high-risk "checkables" from memory?
- [ ] Given a data scenario, can you decide: right workspace, minimization needed, disclosure required?
- [ ] Do you know your retake and renewal rules for this exam? (14/30/90-day waits, 12-month validity, free on-time Partner Academy renewal)

---

## Week 3 - Workflows, Configuration, and Troubleshooting

**Focus:** Domain 2 (Workflow Integration and Solution Design - 16%), Domain 6 (Configuration and Knowledge Management - 12%), Domain 7 (Troubleshooting and Optimization - 10%)

### Partner Academy

- [ ] Finish all remaining CCAO-F prep course modules

### Reading

- [ ] Read [notes/02-workflow-integration-and-solution-design.md](notes/02-workflow-integration-and-solution-design.md)
- [ ] Read [notes/06-configuration-and-knowledge-management.md](notes/06-configuration-and-knowledge-management.md)
- [ ] Read [notes/07-troubleshooting-and-optimization.md](notes/07-troubleshooting-and-optimization.md)

### Hands-On

- [ ] Pick one recurring task from your own work and design the Claude workflow: step, inputs, human checkpoint, output path
- [ ] Build a real Project for it: instructions, template, 2-3 curated knowledge files
- [ ] Run the workflow 3 times through the Project; note the reduction in prompting effort
- [ ] Deliberately break it: add a stale file to knowledge, observe the wrong answer, then fix by curation
- [ ] Take a bad output and walk the escalation ladder: prompt fix, input fix, restructure, fresh chat
- [ ] Practice the long-chat reset: summarize state, restart in a fresh chat

### Week 3 Self-Check

- [ ] Can you name the four human-in-the-loop patterns and when each applies?
- [ ] Instructions vs knowledge vs personal preferences: can you say what goes where?
- [ ] Given a failure symptom, can you name the first move without looking at the table?

---

## Week 4 - Scenarios, Practice Questions, and Exam Prep

**Focus:** All domains - consolidation, gap-filling, logistics

### Practice

- [ ] Work every scenario in [scenarios.md](scenarios.md) - answer before reading the solution
- [ ] Complete the [practice question bank](../../../resources/practice-questions/anthropic-claude-associate-foundations.md) under time pressure (2 minutes per question)
- [ ] Re-read [fact-sheet.md](fact-sheet.md) end to end, including the exam traps
- [ ] Re-read [strategy.md](strategy.md) exam-day tactics
- [ ] Complete any practice assessment offered in the Partner Academy prep courses

### Gap Analysis

- [ ] List your three weakest domains from practice results
- [ ] Re-read the notes file for each weak domain
- [ ] Do one more hands-on exercise per weak domain

### Domain Confidence Check

- [ ] Domain 1 (21%) - I can choose the right validation approach for any stakes level
- [ ] Domain 2 (16%) - I can design a Claude-assisted workflow with the right human checkpoint
- [ ] Domain 3 (15%) - I can make the safe-and-productive call on any data scenario
- [ ] Domain 4 (14%) - I can turn a vague request into a strong prompt and iterate effectively
- [ ] Domain 5 (12%) - I can pick product, plan, and model tier for any scenario
- [ ] Domain 6 (12%) - I can configure a Project (instructions + curated knowledge) for a team
- [ ] Domain 7 (10%) - I can diagnose a failure type and pick the cheapest effective fix

### Exam Logistics

- [ ] Register via [Partner Academy](https://anthropic-partners.skilljar.com/page/partner-certifications) (Claude Partner Network membership + company email required)
- [ ] Schedule at [Pearson VUE](https://www.pearsonvue.com/us/en/anthropic.html) - choose online proctored or a test center
- [ ] If online proctored: run the Pearson VUE system test, prepare a quiet room, clear desk
- [ ] Have government-issued ID ready
- [ ] Remember: reschedule/cancel is allowed up to 24 hours before the appointment
- [ ] Get a full night's sleep before exam day

---

## Progress Summary

| Week | Focus | Status |
|---|---|---|
| Week 1 | Products and Prompting (D5, D4) | [ ] Not Started / [ ] In Progress / [ ] Complete |
| Week 2 | Evaluation and Governance (D1, D3) | [ ] Not Started / [ ] In Progress / [ ] Complete |
| Week 3 | Workflows, Configuration, Troubleshooting (D2, D6, D7) | [ ] Not Started / [ ] In Progress / [ ] Complete |
| Week 4 | Practice and Review (all) | [ ] Not Started / [ ] In Progress / [ ] Complete |

**Exam Date:** ___________
**Result:** ___________
