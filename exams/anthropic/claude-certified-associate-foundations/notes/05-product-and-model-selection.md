---
last-updated: 2026-08-11
---

# Domain 5 - Product and Model Selection (12%)

## Overview

This domain tests whether you can match a business need to the right Claude product, plan, and model. Scenarios describe a person, a task, and constraints (cost, speed, quality, collaboration, governance), and ask what they should use. No configuration detail is required - that is Domain 6 - just sound selection judgment.

---

## The Claude Product Family

### Claude.ai chat

The general-purpose assistant in the browser, desktop, and mobile apps. Handles drafting, analysis, Q&A, document upload, image understanding, web search, and computation via the analysis tool. The default surface for one-off tasks.

### Projects

Persistent workspaces inside Claude.ai. A Project carries:

- **Custom instructions** applied to every chat in the Project
- **Knowledge files** available to every chat in the Project
- On Team/Enterprise plans, **sharing** with teammates

Select a Project whenever the scenario mentions recurring work, a consistent workstream, repeated context-pasting, or a team needing the same setup.

### Artifacts

The dedicated side-panel where Claude creates and iterates on substantial outputs: documents, reports, code snippets, diagrams, and small interactive pages. Select Artifacts when the scenario centers on producing and refining a deliverable, or something the user wants to view, edit iteratively, or share as a standalone piece.

### Claude in Slack and other integrations

Claude embedded where work already happens: Slack (summarize threads, draft replies, answer questions in-channel), browser extension, and desktop-app conveniences. Select an integration when the scenario's friction is "the information and the conversation live in another tool and people copy-paste".

### Connectors

Connections from Claude to live sources - drives, documents, and business tools - so Claude works from current data rather than uploads. Select connectors when the scenario stresses "always current" information or repeated re-uploading of changing files. Governance note: organizations control which connectors are enabled (Domain 3/6 overlap).

### Claude Code

Anthropic's agentic command-line tool for software engineering: it reads codebases, edits files, runs commands. For the CCAO-F you need concept-level awareness only: it targets developers, and it is the answer when a scenario is about engineering teams automating coding work - and the wrong answer for a business analyst's document workflow.

### The API and developer platform

Building Claude into products and automated pipelines is developer territory (the Developer Foundations cert). For this exam, recognize the boundary: when a scenario needs fully automated, high-volume, system-to-system processing, that is an API/engineering conversation to bring to a technical team - not a chat workflow.

---

## Product Selection Cheat Table

| Scenario signal | Best fit |
|---|---|
| One-off question or draft | Claude.ai chat |
| Same workflow every week, same background docs | Project |
| Team should share one setup and context | Shared Project (Team/Enterprise) |
| Building and refining a document or mini-app | Artifacts |
| Work and discussion live in Slack | Claude in Slack |
| Needs live files/systems, uploads keep going stale | Connectors |
| Engineering team automating code tasks | Claude Code |
| Automated pipeline, no human in the chat | API (refer to developers) |

---

## The Model Family

Claude models come in three tiers. Exact version names change; the tier logic is what the exam tests.

| Tier | Character | Best for |
|---|---|---|
| Opus | Most capable, deepest reasoning, slowest, highest cost | Complex analysis, long multi-step reasoning, hardest writing tasks where quality dominates |
| Sonnet | Balanced capability, speed, and cost | The default for most everyday business work |
| Haiku | Fastest and cheapest, lighter capability | High-volume simple tasks: classification, short summaries, quick extraction |

**[📖 Models Overview](https://docs.anthropic.com/en/docs/about-claude/models)** - the current model family, capabilities, and comparisons

### Selection heuristics

1. **Default to the balanced tier.** Most tasks do not need the flagship, and the balanced model is faster and cheaper.
2. **Step up when quality dominates** - dense analysis, high-stakes deliverables, tasks the balanced model handles poorly after good prompting.
3. **Step down when volume and speed dominate** - hundreds of short, similar, simple items.
4. **Prompt quality beats model choice** for most quality problems. "Switch to a bigger model" is rarely the first fix (Domain 7 overlap): if the prompt lacks context, Opus will produce a better-written wrong answer.
5. **Extended thinking** - Claude's option to reason longer before answering. Turn it on for genuinely hard problems; it costs time, so it is not a default for quick tasks.

### Exam trap

"Always use the most capable model" is a distractor. So is "the cheap model for everything". The correct answers match the tier to the described task, and often mention trying a better prompt before a bigger model.

---

## Plans

| Plan | Audience | Selection signals |
|---|---|---|
| Free | Individuals trying Claude | Light, occasional use; tight usage limits |
| Pro | Individual power users | Daily individual use, higher limits, full features for one person |
| Team | Small-to-mid teams | Shared billing, shared Projects and collaboration, commercial data terms |
| Enterprise | Larger organizations | Everything in Team plus admin controls, SSO-style access management, enhanced security and governance capabilities |

Selection logic the exam uses:

- **Individual experimenting** → Free or Pro.
- **A team collaborating on client work** → Team at minimum; the data terms and shared Projects are the point.
- **An organization with compliance requirements, central user management, or audit needs** → Enterprise.
- The governance rule from Domain 3 shows up here: client-confidential work on a personal Free/Pro account is a wrong answer even though it is technically possible.

---

## Putting It Together: Selection Scenarios

**"A consultant answers similar RFP questions every week from a library of past responses."**
Project (recurring workflow + standing knowledge files) on a Team/Enterprise plan (client data), balanced model. Artifacts for assembling each response document.

**"A support lead wants 300 short customer emails per day categorized and given draft replies, no human typing prompts."**
That is an automated pipeline: refer to the engineering team for an API solution, likely on the fast/cheap model tier. A chat product is the wrong shape.

**"A partner needs a one-time deep analysis of a 100-page market study for a board presentation."**
Claude.ai chat with the document uploaded; the most capable model tier (possibly with extended thinking) since quality dominates and volume is one; output drafted as an Artifact; every figure verified before the board sees it (Domain 1).

**"A project team living in Slack keeps copy-pasting thread summaries into Claude."**
Claude in Slack.

---

## Key Takeaways

1. Match the surface to the work pattern: chat for one-offs, Projects for recurring work, Artifacts for deliverables, integrations for in-tool work, connectors for live data.
2. Claude Code is for developers; the API is for automated pipelines - know the boundary and hand off.
3. Model tiers: balanced by default, up for quality-dominant tasks, down for volume-dominant simple tasks.
4. Better prompting usually beats a bigger model as the first fix.
5. Plans are a governance choice as much as a feature choice: business data on business plans.

**[📖 Claude.ai](https://claude.com)** - current plans and features
**[📖 Claude Help Center](https://support.claude.com)** - product documentation for each feature
