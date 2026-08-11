---
last-updated: 2026-08-11
---

# Domain 4 - Prompting and Task Execution (14%)

## Overview

This domain covers getting good work out of Claude: framing tasks clearly, providing the right context, structuring prompts, and iterating in conversation. The exam tests it at a business-user level - no API parameters, no XML tag trivia - but the underlying principles are the same ones in Anthropic's official prompting guidance.

The single most important idea: **Claude cannot read your mind.** Almost every weak output traces back to missing context or an underspecified task. Treat prompting as delegation to a very capable new colleague who knows nothing about your situation until you tell them.

**[📖 Prompt Engineering Overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)** - Anthropic's official guide; written for the API but the techniques transfer directly to Claude.ai chat

---

## The Anatomy of a Strong Prompt

A reliable skeleton for work tasks:

1. **Role and audience** - who Claude should act as, and who the output is for.
2. **Task** - one clear sentence stating what to produce.
3. **Context** - background, source material, and anything Claude needs to know.
4. **Constraints** - length, tone, what to include, what to leave out.
5. **Format** - the exact output shape: table, email, one-pager, bullet brief.
6. **Example** - optionally, a sample of what good looks like.

### Weak vs strong

Weak:

> Write something about our Q3 results for the team.

Strong:

> You are helping a sales director write an internal update. Using the attached Q3 summary, write a 200-word email to the sales team: one short paragraph on overall performance, three bullets on wins, one sentence on the Q4 focus. Upbeat but honest tone; do not mention the churn figures, those are covered separately.

Every improvement is information, not magic wording: audience, source, length, structure, tone, exclusions.

---

## Core Techniques

### Be specific and direct

State exactly what you want. "Summarize this" invites Claude to guess length and focus; "Summarize this in 5 bullets focused on financial risks" does not. Numbers beat adjectives: "3 options", "under 150 words", "a 10-row table".

### Provide context and source material

Claude does dramatically better working from your actual documents than from general knowledge. Upload the report, paste the thread, attach the data. Also say *why* you need it - "this is for a skeptical CFO" changes the output usefully.

### Assign a role

"You are an experienced management consultant reviewing a junior analyst's deck" sets expertise level, tone, and perspective in one line. Roles are especially useful for review tasks and audience-tailored rewriting.

### Show examples (few-shot)

One or two examples of the desired output outperform paragraphs of description. Pasting last month's well-received status report and asking for this month's in the same style is the highest-leverage formatting technique there is.

### Ask for reasoning first

For analysis and judgment tasks, ask Claude to think through the problem before answering: "First list the key factors and how you weigh them, then give your recommendation." Visible reasoning improves the answer and gives you something to evaluate (Domain 1).

### Break large tasks into steps

One giant prompt asking for a complete 20-page proposal produces mush. Better: outline first, agree the outline, then draft section by section, then a consistency pass. You steer at each checkpoint, which is faster than repairing a monolith.

### Tell Claude what to do when it doesn't know

Add: "If the document does not contain the answer, say so rather than guessing." This one sentence meaningfully reduces fabricated answers on document tasks.

---

## Iterating in Conversation

The first response is round one. Skilled users improve outputs in the same chat with targeted feedback rather than starting over:

| Feedback style | Example |
|---|---|
| Directional | "Make it half the length and lead with the recommendation" |
| Corrective | "The date in paragraph 2 is wrong - the launch was in March, not May" |
| Additive | "Add a section on risks; here are the two I already know about" |
| Comparative | "Version 1's tone was better; keep that tone with version 2's structure" |

Why in-conversation iteration usually beats a fresh prompt: Claude retains all the context you have built up. Start fresh when the conversation has become long and confused, or when you want an uncontaminated second opinion (see Domain 7).

Also useful: ask for variants. "Give me three versions of this opening: formal, conversational, and blunt" - then pick and refine.

---

## Task Execution Across Claude's Capabilities

Business-level awareness of what Claude can work with:

- **Documents** - upload PDFs, Word docs, spreadsheets, slides; Claude reads and works over them. Long documents work, but focused inputs get more focused attention.
- **Images** - screenshots, whiteboard photos, charts. Claude can read, describe, and extract from them.
- **Data and the analysis tool** - for real computation over uploaded data (sums, trends, charts), the analysis tool runs actual code. Prefer it over asking for arithmetic in prose.
- **Web search** - for current information, ask Claude to search and cite sources; then verify the load-bearing ones.
- **Artifacts** - ask for the output "as a document/artifact" when you want a deliverable to iterate on beside the chat.
- **Voice and mobile** - the same prompting principles apply in every Claude app.

Knowing which capability a task needs is itself an exam topic (overlapping Domain 5): a question about "this quarter's competitor pricing" needs web search; "totals across this 5,000-row export" needs the analysis tool.

---

## Common Prompting Mistakes

1. **No audience** - output pitched at the wrong level. Always name the reader.
2. **No format** - you get an essay when you wanted a table.
3. **Buried intent** - three paragraphs of background, no clear ask. Put the task up front.
4. **Assumed knowledge** - referring to "the Henderson account" that Claude has never heard of. Paste the background or use a Project that holds it.
5. **Compound mega-prompts** - five unrelated asks in one message; some get dropped. Split them.
6. **Vague revision requests** - "make it better" forces Claude to guess what you dislike. Say what is wrong.
7. **Arguing instead of restating** - if Claude misunderstood, do not debate; restate the task more precisely.

---

## Prompts as Team Assets

An associate-level user turns good prompts into shared capability (links to Domains 2 and 6):

- **Prompt templates** - a fill-in-the-blanks version of a proven prompt, stored where the team works.
- **Project instructions** - the durable parts of a prompt (role, style, process, format rules) moved into a Project so nobody retypes them.
- **Worked examples in project knowledge** - the "what good looks like" samples stored once, applied to every chat in the Project.

A good test: could a new team member produce an acceptable draft on day one using the Project and template alone? If yes, the prompting knowledge has been institutionalized.

---

## Worked Example

Task: turn a messy 40-minute meeting transcript into minutes and actions.

A strong prompt:

> You are preparing minutes for a project steering meeting. From the attached transcript, produce: (1) a 5-sentence summary of decisions made, (2) a table of action items with columns Owner, Action, Due date - only include actions explicitly agreed in the meeting, (3) a short list of open questions deferred to next time. Use only the transcript; if an owner or date was not stated, write "not specified" rather than guessing. Format as a document I can share with attendees.

Then iterate: "Action 3's owner was Priya, not Paul - correct it", and validate by scanning the transcript for the decisions listed (Domain 1).

---

## Key Takeaways

1. Prompting is delegation: role, task, context, constraints, format, example.
2. Specificity and real source material beat clever wording every time.
3. Examples are the strongest formatting tool; reasoning-first improves analysis.
4. Break big tasks into steps with human checkpoints between them.
5. Iterate with targeted feedback in-conversation; restate rather than argue.
6. "Say so if you don't know" belongs in every document-grounded prompt.
7. Durable prompt knowledge belongs in Projects and templates, not in one person's head.
