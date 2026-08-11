---
last-updated: 2026-08-11
---

# Domain 7 - Troubleshooting and Optimization (10%)

## Overview

The smallest domain, but a highly practical one: when Claude's output disappoints, what do you change? The exam presents a weak output and asks for the best next step. The skill being tested is **diagnosis before action** - identifying which kind of failure occurred, then applying the matching fix instead of randomly re-prompting or reflexively blaming the model.

---

## The Diagnostic Mindset

When an output is not right, resist the two reflexes the exam punishes:

1. **"Regenerate and hope"** - re-rolling without changing anything occasionally helps, but is a coin flip, not a method.
2. **"The model is bad, switch models"** - upgrading the model fixes capability problems, which are rare; most failures are information problems, which a bigger model cannot fix. A better model given a vague prompt writes a more eloquent wrong answer.

Instead, classify the failure first. Almost everything falls into one of these buckets:

| Failure type | What you see | Root cause (usually) |
|---|---|---|
| Wrong facts | Incorrect claims, invented details | No source material; asking beyond training data |
| Wrong scope | Answered a different question, missed parts | Ambiguous or compound prompt |
| Wrong format | Essay instead of table, wrong length | Format never specified |
| Wrong tone/depth | Too casual, too technical, too generic | Audience never specified; missing context |
| Lost the thread | Contradicts earlier decisions, forgets constraints | Very long conversation; context drift |
| Refusal | Claude declines the task | Policy line, or a misread of intent |
| Inconsistency | Different answers on repeated runs | Underspecified criteria; natural model variation |

---

## Fixes by Failure Type

### Wrong facts

- **Ground it**: provide the actual documents and instruct "use only these; say so if the answer is not in them".
- **Demand citations** and spot-check them (Domain 1).
- For current events or prices: have Claude use web search, then verify the cited pages.
- For arithmetic and data work: use the analysis tool so the computation runs as code.

### Wrong scope

- Restate the task in one unambiguous sentence; explicitly list what to include and exclude.
- Split compound requests: five asks in one message become five sequential messages.
- If Claude misunderstood, do not argue - restate. "Let me re-frame the task:" and a clean statement beats a debate about what you meant.

### Wrong format

- Specify the format explicitly: "a table with columns X, Y, Z", "under 200 words", "an email".
- Paste an example of the desired output - the strongest format lever available.
- For recurring format needs, put the template in project instructions or knowledge (Domain 6) so the fix is permanent.

### Wrong tone or depth

- Name the audience: "for a non-technical executive", "for the engineering team".
- Give a sample paragraph in the right voice and ask Claude to match it.
- Adjust with directional feedback: "more formal, less hedging, cut the pleasantries".

### Lost the thread (long-chat drift)

Long conversations accumulate contradictions, superseded drafts, and dead ends, and very long ones exceed what Claude can attend to well. Fixes:

- **Summarize and restart**: ask Claude to summarize the current state, decisions, and constraints; carry that summary into a fresh chat.
- **Promote durable context** into a Project so a fresh chat starts warm instead of cold.
- Prevention: one workstream per chat; start new chats at natural task boundaries.

### Refusals

- If the task is legitimate and was misread, clarify honestly: state the real purpose and context ("I am the account owner drafting a renewal notice to my own client..."). This resolves most misunderstanding-refusals.
- If the task actually crosses a policy line, the refusal is correct - accept it. Any answer involving disguising intent or slicing the task to sneak it through is wrong (Domain 3).

### Inconsistency across runs

- Some variation is normal model behavior, not a defect.
- Reduce it by pinning down criteria and format in the prompt: exact rubric, exact structure, worked example.
- For team-repeatable tasks, template the prompt in a Project so every run starts from identical instructions.

---

## The Escalation Ladder

When a first fix does not land, escalate in this order - cheapest and most likely first:

1. **Improve the prompt** - add the missing context, audience, format, or constraint.
2. **Improve the inputs** - supply better source documents; remove stale or contradictory material.
3. **Restructure the task** - break it into steps with a checkpoint after each.
4. **Reset the conversation** - fresh chat, carrying a state summary.
5. **Fix the configuration** - correct project instructions or curate knowledge files if the failure is systematic across chats (Domain 6).
6. **Change capability** - stronger model tier or extended thinking for genuinely hard reasoning; analysis tool for computation; web search for currency.
7. **Reconsider the fit** - some tasks need a human, a specialist tool, or an engineering (API) solution. Recognizing a poor-fit task is a correct answer, not a failure.

The exam frequently asks "what should she try FIRST?" - the answer is nearly always on rungs 1-2, unless the scenario explicitly establishes the prompt and inputs were already good.

---

## Optimization: Making Good Workflows Better

Beyond fixing failures, this domain covers tuning workflows that already work:

- **Reduce iteration count** - if every draft needs the same three corrections, move those corrections into the prompt template or project instructions. The goal is a first draft that needs one review, not four rounds.
- **Front-load context once** - repeated context-pasting is a signal to create a Project (Domain 6).
- **Right-size the model** - a workflow running fine on the balanced tier does not need the flagship; a high-volume simple task may run better and cheaper on the fast tier (Domain 5).
- **Use extended thinking selectively** - it helps hard reasoning tasks and adds latency to easy ones; it is a dial, not a default.
- **Trim the inputs** - focused excerpts often beat dumping entire documents; attention is a budget.
- **Bake in validation** - instructions like "flag any figure you could not find in the source" make outputs partially self-auditing, cutting review time (Domain 1).
- **Measure** - time per deliverable and edits per draft before and after a change tell you whether an "optimization" actually helped (Domain 2).

---

## Worked Example

Scenario: a consultant's Project drafts client emails. Lately, drafts cite an old service price and keep coming out too long despite her asking for brevity each time.

Diagnosis and fix:

1. **Wrong facts, systematic across chats** → configuration, not prompting: the Project's knowledge contains last year's rate card. Remove it, add the current one (rung 5).
2. **Wrong format, recurring** → the "keep it short" correction she types every time belongs in project instructions: "Client emails are 150 words maximum" (permanent fix beats repeated feedback).
3. **Verify the fix** - run the workflow twice; check price and length. Done.

Note what was NOT the answer: switching models, regenerating repeatedly, or abandoning the Project.

---

## Quick Reference: Symptom → First Move

| Symptom | First move |
|---|---|
| Invented facts or citations | Ground in source documents, require citations |
| Ignored half the request | Split the request; one ask per message |
| Wrong output shape | Specify format; give an example |
| Too generic | Add context and audience |
| Contradicts earlier decisions | Summarize state, start fresh chat |
| Same error across whole team/Project | Fix instructions or knowledge, not individual prompts |
| Declined a legitimate task | Clarify intent and context honestly |
| Needs current data | Web search or connector, then verify |
| Math is off | Analysis tool, not prose arithmetic |

---

## Key Takeaways

1. Diagnose the failure type before changing anything; matching fix to failure is the whole domain.
2. Most failures are information problems: better context, sources, and specificity fix them.
3. Escalate cheaply first: prompt → inputs → structure → fresh chat → configuration → capability → task fit.
4. Systematic failures across a team point at configuration (instructions/knowledge), not at individual prompts.
5. Never game a refusal; clarify honestly or accept it.
6. Optimization means fewer iterations and less review time - move recurring corrections into templates and instructions, and measure the difference.

**[📖 Prompt Engineering Overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)** - the official techniques behind most rung-1 fixes
**[📖 Claude Help Center](https://support.claude.com)** - product documentation for Projects, analysis tool, and web search
