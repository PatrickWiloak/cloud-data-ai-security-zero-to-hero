---
last-updated: 2026-08-11
---

# Domain 2 - Workflow Integration and Solution Design (16%)

## Overview

The second-largest domain tests whether you can take Claude out of the demo and into real work. It covers identifying where Claude fits in a business workflow, designing the human-plus-Claude process around it, choosing the right product surface for the job, and rolling it out sensibly.

The core skill: **start from the task, not from the tool.** The exam punishes answers that bolt Claude onto everything, and rewards answers that pick the workflow step where Claude genuinely helps and keep humans where they must stay.

---

## Where Claude Adds Value

Claude is strongest at language-shaped work: reading, writing, restructuring, and reasoning over text (and images, documents, and data).

### High-value task types

| Task type | Examples |
|---|---|
| First drafts | Emails, proposals, status reports, job descriptions, briefs |
| Summarization | Meeting transcripts, long reports, email threads, research papers |
| Synthesis | Combining several documents into one view; comparing options |
| Transformation | Rewriting for a new audience, translating tone, converting formats |
| Extraction | Pulling names, dates, action items, terms from documents |
| Review | Checking a draft against a checklist, style guide, or rubric |
| Brainstorming | Options, risks, objections, names, agendas, test cases |
| Data exploration | Uploading a spreadsheet and asking questions, with the analysis tool doing the actual computation |

### Poor-fit tasks

- **Final authority on facts** - Claude drafts and checks, humans confirm (Domain 1).
- **Accountable decisions** - hiring, firing, pricing approval, legal sign-off. Claude can prepare the analysis; a person decides.
- **Real-time or proprietary data Claude cannot see** - unless a connector or upload provides it, Claude does not know your pipeline, inventory, or this morning's numbers.
- **High-precision arithmetic in prose** - use the analysis tool (real code execution) or a spreadsheet, not mental math in a chat response.
- **Tasks where the terms or policy forbid AI use** - some client contracts and regulated processes do. Check first (Domain 3).

---

## Designing the Human-plus-Claude Workflow

A well-designed Claude workflow answers four questions:

1. **Which step does Claude do?** Be surgical. In a proposal workflow, maybe Claude drafts the background section and tailors boilerplate, while pricing stays human.
2. **What does Claude need as input?** Templates, past examples, source documents, style guides. Feeding these in (or storing them in a Project) is most of the quality difference.
3. **Where is the human checkpoint?** Every workflow that produces something external or high-stakes has an explicit review gate. "Claude drafts, human edits and approves" is the default pattern.
4. **How does the output leave Claude?** Copy into the document system, export an Artifact, or deliver through an integration. A workflow that ends with "and then someone retypes it" is badly designed.

### Human-in-the-loop patterns

| Pattern | When |
|---|---|
| Claude drafts, human approves | External communications, deliverables |
| Human drafts, Claude reviews | Quality checks against a rubric or style guide |
| Claude triages, human handles exceptions | High-volume sorting, classification, first-pass responses |
| Claude and human alternate | Complex analysis: Claude proposes, human steers, repeatedly |

The exam frequently asks which pattern fits a scenario. Look at the stakes and the volume: high stakes pushes approval gates in; high volume with low stakes pushes toward triage patterns.

---

## Choosing the Product Surface

Solution design includes picking where the workflow lives (overlaps with Domain 5):

- **Ad hoc chat** - one-off tasks. If you notice the same chat being repeated weekly, that is a signal to promote it.
- **Project** - the home for any recurring workflow: standing instructions (how we write status reports), knowledge files (the template, last quarter's examples, the style guide), and shared access for the team on Team/Enterprise plans.
- **Artifacts** - when the output is a document, a formatted report, or a small interactive tool that you iterate on. The Artifact panel keeps the deliverable separate from the conversation about it.
- **Claude in Slack / integrations** - when the work already happens in another tool and copy-paste is the friction. Summarizing a channel discussion, drafting a reply where the thread lives.
- **Connectors** - when the workflow depends on live files or systems (a drive folder, a ticketing tool). Connectors let Claude read current data rather than stale uploads.
- **Claude Code** - conceptually: the developer-focused agentic tool. If a scenario involves a software team automating engineering work, that is Claude Code territory; a business analyst writing a client summary does not need it.

---

## Repeatability: From One-off to Process

The exam rewards recognizing when to invest in repeatability.

Signals that a task should become a standing workflow:

- The same kind of request happens weekly or more often.
- Multiple people do it and quality varies between them.
- You keep pasting the same background material into new chats.

The promotion path:

1. **Template the prompt** - turn the good prompt into a fill-in-the-blanks template with the fixed parts written once.
2. **Create a Project** - move the standing instructions and reference files into project instructions and project knowledge.
3. **Share it** - on team plans, share the Project so everyone runs the same process with the same context.
4. **Document the checkpoint** - write down what the human reviewer checks before output ships.

This turns individual prompt skill into team capability, which is exactly what a consultant or delivery lead is expected to do.

---

## Piloting and Rollout

For introducing Claude into a team or client workflow, the exam favors a measured rollout:

1. **Pick one workflow** with clear pain, low-to-medium risk, and a measurable outcome (time per report, backlog cleared).
2. **Baseline it** - know what the process costs today.
3. **Pilot with a small group** - a few users, a few weeks, with the review gates designed in from the start.
4. **Measure quality and time** - did outputs pass review? How much editing did drafts need? What time was saved?
5. **Fix the setup, then expand** - improve project instructions and knowledge based on pilot feedback before scaling to the wider team.
6. **Train and govern as you scale** - people need the prompting and validation basics (Domains 4 and 1) and the data rules (Domain 3), not just a license.

Distractor answers in rollout scenarios usually look like: "roll out to everyone immediately", "no measurement", or "ban it until perfect". The correct shape is pilot, measure, improve, expand.

---

## Measuring Success

Reasonable metrics for a Claude-assisted workflow:

- **Time** - hours per deliverable, turnaround time, backlog size.
- **Quality** - review pass rate, edits required per draft, error escapes.
- **Adoption** - who uses the workflow, and whether usage sticks after week one.
- **Risk** - verification steps completed, incidents (e.g., data pasted where it should not be).

If a metric cannot be named, the "solution" is a demo, not a solution. Exam scenarios about proving value expect a before/after comparison on a named metric.

---

## Worked Example

Scenario: a consulting team spends 3 hours per week each turning raw meeting notes into formatted client status reports.

Solution design:

1. **Step selection** - Claude drafts the report from the notes; the engagement lead reviews and sends. Pricing/commercial lines stay human-entered.
2. **Project setup** - a Project per client with: instructions describing the report format and tone, the report template, and two exemplary past reports as knowledge files.
3. **Process** - paste or upload the week's notes, ask for a draft in the template, iterate once for tone, lead reviews facts (names, dates, commitments) against the notes, then sends.
4. **Pilot** - two consultants for three weeks; measure drafting time and edits needed.
5. **Result** - the workflow is shared to the team as a Project; a one-page guide documents the review checklist.

---

## Key Takeaways

1. Start from the workflow step, not the tool; be surgical about what Claude does.
2. Default pattern: Claude drafts, human reviews and approves - stakes decide how heavy the gate is.
3. Recurring tasks belong in Projects with instructions and knowledge, not re-explained chats.
4. Choose the surface deliberately: chat, Project, Artifact, integration, connector.
5. Pilot, measure with a named metric, improve, then expand - never big-bang.
6. Turning a personal prompt into a shared, governed team workflow is the core associate-level skill.

**[📖 Claude Help Center](https://support.claude.com)** - product documentation for Projects, Artifacts, and integrations
