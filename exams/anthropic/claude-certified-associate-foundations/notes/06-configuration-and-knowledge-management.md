---
last-updated: 2026-08-11
---

# Domain 6 - Configuration and Knowledge Management (12%)

## Overview

This domain covers setting Claude up so it does good work repeatedly: Projects, custom instructions, knowledge files, personal preferences, and connectors. If Domain 4 is about the prompt you type today, Domain 6 is about the configuration that means you type less tomorrow - and that a whole team gets the same quality.

The organizing idea: **move durable context out of individual prompts and into configuration.** Anything you find yourself retyping belongs in an instruction or a knowledge file.

---

## The Configuration Layers

Claude.ai has several layers of standing context. Know what each is for and how they interact:

| Layer | Scope | Typical content |
|---|---|---|
| Personal preferences (custom instructions) | All your chats | Your role, general style preferences ("concise, no filler"), default formats |
| Project instructions | Every chat in one Project | The workflow: role, process, tone, format rules, do/don't lists for that workstream |
| Project knowledge | Every chat in one Project | Reference files: templates, style guides, past examples, background documents |
| Per-chat prompt | One conversation | The specific task and its inputs |

Precedence intuition: the more specific layer shapes the work most directly. The per-chat prompt states today's task; project instructions carry the standing "how we do this here"; personal preferences carry cross-cutting style. Conflicts between layers produce confused output - which is a configuration bug to fix, not something to work around per-chat.

---

## Projects: Instructions

Project instructions are the highest-leverage configuration feature for business users. Good project instructions read like a briefing for a new team member:

- **Role and purpose** - "You help the Meridian account team produce weekly client status reports."
- **Process** - the steps to follow, what to ask for if inputs are missing.
- **Format rules** - the template to follow, length limits, section order.
- **Tone** - audience and voice, with a line or two of example.
- **Boundaries** - what not to do: "Never include internal cost figures in client-facing drafts."

Practical guidance:

1. Keep instructions focused on the durable rules; per-task detail stays in the chat.
2. Write them from your best prompt: when a prompt works repeatedly, promote its fixed parts into the instructions.
3. Review them when outputs drift or the process changes - instructions rot like documentation does.

---

## Projects: Knowledge

Project knowledge files give every chat in the Project the same source material. What belongs there:

- Templates and exemplary past deliverables ("what good looks like")
- Style guides and glossaries
- Stable background: account summaries, product descriptions, methodology docs
- Reference data the workflow repeatedly needs

What does not belong there:

- **Fast-changing data** - this week's numbers go in the chat (or come via a connector); a stale file in knowledge produces confidently outdated answers.
- **Everything you have** - knowledge is a curated shelf, not an archive. Irrelevant files dilute attention and can surface in answers where they do not belong.
- **Data that violates governance rules** - the Domain 3 rules apply to knowledge files exactly as they apply to pasted text, and knowledge files persist and are shared, which raises the stakes.

### Curation discipline

Treat a Project's knowledge base like a team-owned document set:

1. **An owner** - someone is responsible for what is in there.
2. **A refresh cadence** - dated files get reviewed; superseded versions get removed, not accumulated.
3. **Naming and scope** - one Project per client or workstream, containing only its own material. One giant Project mixing three clients' files is both a quality problem (wrong-context answers) and a confidentiality problem (cross-client leakage into drafts).

The exam's favorite failure mode here: a team's Project gives wrong answers because the knowledge contains an outdated pricing sheet alongside the new one. The fix is curation - remove the stale file - not prompt gymnastics.

---

## Personal Preferences

Account-level custom instructions apply across your chats: who you are, how you like output formatted, standing style rules. Use them for genuinely universal preferences ("I am a UK-based consultant; use British English; be concise"). Keep workflow-specific rules out of personal preferences and in the relevant Project - otherwise every chat drags irrelevant constraints along.

---

## Connectors and Live Knowledge

Uploaded knowledge is a snapshot; connectors are a pipe. A connector lets Claude read from live sources - document drives, wikis, business tools - subject to what the organization has enabled and to the user's own access permissions.

Selection logic:

| Situation | Choice |
|---|---|
| Stable reference material | Upload to project knowledge |
| Frequently changing documents the team keeps re-uploading | Connector to the source |
| One-off document for one task | Attach in the chat |

Governance note (Domain 3 overlap): connectors are enabled and scoped by workspace admins. Claude's access rides on permissions - it should see what the user can see, and no more. "Connect everything" is not a best practice; connect the sources the workflows need.

---

## Team Configuration on Team/Enterprise Plans

Configuration becomes a management tool at team scale:

- **Shared Projects** - one well-built Project (instructions + curated knowledge) raises the floor for the whole team; new members inherit the working setup on day one.
- **Consistency** - shared configuration is how a team gets consistent tone and format across ten authors.
- **Admin controls** (Enterprise) - workspace admins manage membership, enabled features, and connectors centrally; the configuration surface is part of the governance surface.
- **Documentation** - a shared Project deserves a short "how to use this Project" note - itself a good first knowledge file.

The maturity progression worth remembering for scenario questions:

1. Individuals paste context into ad hoc chats (fragile, inconsistent).
2. One person builds a Project with instructions and knowledge (personal leverage).
3. The Project is shared, owned, and curated by the team (institutional capability).

Exam answers favor movement up this ladder.

---

## Configuration Troubleshooting Preview

Configuration problems surface as output problems (full treatment in Domain 7):

| Symptom | Likely configuration cause |
|---|---|
| Answers cite outdated facts | Stale knowledge file still in the Project |
| Output ignores the team template | Template described in chat but not in instructions/knowledge, or instructions too vague |
| Irrelevant material appears in answers | Over-stuffed knowledge base; unrelated files in the Project |
| Inconsistent tone across team members | Rules living in individuals' prompts instead of shared project instructions |
| Contradictory behavior | Personal preferences conflicting with project instructions |

---

## Worked Example

A delivery lead sets up a Project for monthly QBR (quarterly business review) decks:

- **Instructions**: "You help the team draft QBR narratives for client executives. Follow the structure in qbr-template. Tone: direct, evidence-led, no superlatives. Every metric must come from the data provided in the chat - if a number is not provided, mark it TBD rather than estimating. Never include internal margin data."
- **Knowledge**: the QBR template, two exemplary past narratives, the client glossary.
- **Not in knowledge**: monthly metrics (change every month - provided per chat), the client's raw contract (not needed - governance minimization).
- **Shared** with the account team; the lead owns quarterly review of the knowledge files.

The "mark it TBD rather than estimating" instruction is Domain 1 thinking, baked into configuration so every user gets it for free.

---

## Key Takeaways

1. Move durable context out of prompts into configuration: preferences → instructions → knowledge, each at the right scope.
2. Project instructions are a briefing for a new team member: role, process, format, tone, boundaries.
3. Knowledge is curated, owned, and refreshed - stale or excess files cause confidently wrong output.
4. Scope Projects tightly: one workstream or client each.
5. Uploads for stable material, connectors for live material, chat attachments for one-offs.
6. Shared, owned Projects turn individual skill into team capability - the associate-level move.

**[📖 Claude Help Center](https://support.claude.com)** - official documentation for Projects, knowledge, preferences, and connectors
