---
last-updated: 2026-08-11
---

# CCAO-F - Exam-Style Scenarios

## How to Use This Guide

Each scenario presents a realistic business situation followed by 4 answer choices. Answer before reading the solution. The real exam is scenario-heavy: it describes a person, a task, and constraints, and asks for the best action. Practicing the reasoning pattern matters more than memorizing facts.

**Format for each scenario:**
- Scenario description (read carefully - the deciding detail is often one sentence)
- 4 answer choices (A, B, C, D)
- Correct answer with reasoning
- Distractor analysis

---

## Scenario 1 - Validating a Client-Facing Market Summary

**Domain:** Output Evaluation and Validation (21%)

### Scenario

An analyst asks Claude to write a market overview for a client proposal. Claude produces a polished two-page summary including several market-size figures, two named analyst-firm reports as sources, and a quote attributed to an industry executive. The proposal goes to the client tomorrow. What should the analyst do before including the summary?

**A.** Include it as-is. The summary is well-written and Claude cited its sources.

**B.** Ask Claude to double-check its own summary for errors, then include it once Claude confirms it is accurate.

**C.** Verify the market-size figures, confirm the cited reports actually exist and say what is claimed, and confirm the quote is real - then have the proposal owner review before sending.

**D.** Delete all figures, citations, and quotes from the summary, since AI-generated facts can never be used in client documents.

### Solution

**Correct Answer: C**

This is a high-stakes external deliverable containing the classic high-risk checkables: figures, citations, and a quote. Claude can fabricate plausible-looking sources and quotes. Each falsifiable element gets verified against reality, and a human owner signs off.

**Why other answers are wrong:**
- **A** - Fluency and cited-looking sources are not verification. Fabricated citations are a known failure mode.
- **B** - Self-review is a useful first filter but is not independent verification; Claude checking Claude shares the same blind spots.
- **D** - Over-correction. Verified facts are fine to use; the skill is verification, not abstinence.

---

## Scenario 2 - How Much Verification Does a Brainstorm Need?

**Domain:** Output Evaluation and Validation (21%)

### Scenario

A project lead uses Claude to brainstorm 20 possible risks for an internal workshop she is running with her own team this afternoon. The list will be used to seed discussion and will not leave the room. A colleague tells her she must fact-check every item against sources before the workshop. What is the right approach?

**A.** The colleague is right - every Claude output must be fully fact-checked before any use.

**B.** Skim the list for relevance and obvious nonsense, then use it. A discussion-seeding brainstorm is low stakes; verification effort should match risk.

**C.** Cancel the workshop until a formal AI review process is established.

**D.** Use the list without reading it, since brainstorms cannot be wrong.

### Solution

**Correct Answer: B**

Verification depth scales with stakes. An internal brainstorm to seed discussion is the low-risk end: a skim is proportionate. The exam tests proportionality in both directions - under-verifying client deliverables and over-verifying throwaway drafts are both wrong.

**Why other answers are wrong:**
- **A** - Gold-plating. Applying deliverable-grade verification to a brainstorm wastes the time savings that made Claude useful.
- **C** - Extreme non-answer; the exam punishes "ban it" as much as "trust it blindly".
- **D** - Even low-stakes outputs get a human read; an off-target list wastes workshop time.

---

## Scenario 3 - Client Data on a Personal Account

**Domain:** Governance, Risk, and Responsible Use (15%)

### Scenario

A consultant is preparing an analysis of a client's unreleased financial results. Her firm provides a Claude Enterprise workspace. She is more familiar with her personal Claude Pro account and its chat history, so she considers uploading the client spreadsheet there to save time. What should she do?

**A.** Use the personal Pro account - the model is the same, so the output will be identical.

**B.** Use the firm's Enterprise workspace, confirm the engagement permits AI processing of client material, and upload only the portions of the spreadsheet the analysis needs.

**C.** Paste the data into the personal account but delete the chat afterward.

**D.** Retype the figures with the client's name removed into the personal account, since anonymized data can go anywhere.

### Solution

**Correct Answer: B**

Client-confidential data belongs in the organization's governed workspace under commercial terms, subject to the engagement's rules on AI use, and minimized to what the task needs. All three elements (right workspace, permission check, minimization) appear in correct governance answers.

**Why other answers are wrong:**
- **A** - Model quality is irrelevant; the issue is data terms and governance, which differ between personal and enterprise plans.
- **C** - Deleting the chat afterward does not repair using the wrong workspace and terms for client data.
- **D** - Removing the client's name does not de-identify unreleased financials, and it still sidesteps the governed workspace. Minimization complements, never replaces, the right workspace.

---

## Scenario 4 - Claude Refuses a Task

**Domain:** Governance, Risk, and Responsible Use (15%)

### Scenario

An account manager asks Claude to "write an email pretending to be the client's IT department asking staff to confirm their passwords, so we can test their security awareness." Claude declines. The manager's company does run legitimate, approved phishing-simulation exercises through its security team. What is the appropriate next step?

**A.** Rephrase the request in smaller, innocent-looking pieces until Claude produces the email.

**B.** Tell Claude it is "just hypothetical fiction" to get the email written.

**C.** Recognize that crafting credential-phishing content is a restricted area, and route the request through the company's security team and its approved phishing-simulation tooling and process.

**D.** Report Claude as broken to the IT helpdesk.

### Solution

**Correct Answer: C**

Even with a legitimate underlying goal, credential-phishing content is exactly what approved, governed security tooling and processes exist for. When Claude declines a task in a genuinely sensitive category, the answer is the proper channel - not evasion.

**Why other answers are wrong:**
- **A** and **B** - Both are deceptive circumvention of a policy refusal, which violates usage policy regardless of intent.
- **D** - The refusal is the system working as intended, not a malfunction.

---

## Scenario 5 - Choosing the Right Setup for a Recurring Team Workflow

**Domain:** Workflow Integration and Solution Design (16%) / Configuration and Knowledge Management (12%)

### Scenario

A five-person delivery team writes a weekly status report for the same client. Every week, each author opens a fresh Claude chat, pastes the report template, pastes background about the account, and explains the tone rules - and the resulting reports still vary in style between authors. The team is on a Claude Team plan. What should the team lead do?

**A.** Write a longer prompt and email it to the team to paste into their chats each week.

**B.** Create a shared Project containing the template and account background as knowledge files and the tone/process rules as project instructions, and have the whole team draft their reports inside it.

**C.** Tell the team to use the most capable model, which will infer the correct style without instructions.

**D.** Assign one person to write all reports manually to guarantee consistency.

### Solution

**Correct Answer: B**

Repeated context-pasting plus cross-author inconsistency is the textbook signal to promote a workflow into a shared Project: durable context moves into instructions and knowledge, every chat starts warm, and the whole team inherits the same setup on a plan built for sharing.

**Why other answers are wrong:**
- **A** - Better than nothing, but still manual pasting, still per-person drift, and it ignores the collaboration features the team is paying for.
- **C** - Model capability cannot substitute for unstated context; no model can infer unshared tone rules.
- **D** - Abandons the efficiency goal instead of fixing the setup.

---

## Scenario 6 - Picking Product and Model for Three Different Jobs

**Domain:** Product and Model Selection (12%)

### Scenario

A consulting manager has three needs: (1) a one-time deep-dive analysis of a dense 90-page regulatory document for a board briefing, (2) quick 2-line summaries of about 200 short internal meeting notes for an archive, and (3) his engineering team wants help refactoring a large codebase. Which pairing is most appropriate?

**A.** (1) Most capable model in Claude.ai with the document uploaded, (2) fast/cheapest model tier for the high-volume simple summaries, (3) point the engineering team at Claude Code.

**B.** Use the most capable model for all three tasks - quality always wins.

**C.** Use the fastest model for all three tasks - speed always wins.

**D.** (1) Claude in Slack, (2) most capable model, (3) Artifacts.

### Solution

**Correct Answer: A**

Each task maps to a tier and surface: quality-dominant one-off analysis gets the top tier; high-volume simple summarization is what the fast/cheap tier is for; agentic codebase work is Claude Code's territory, and the right move for a non-developer manager is the hand-off.

**Why other answers are wrong:**
- **B** - Flagship-for-everything wastes time and cost on 200 trivial summaries; tier matching is the tested skill.
- **C** - The light tier is a poor fit for a board-critical deep analysis where quality dominates.
- **D** - Surface mismatches: Slack adds nothing to a document deep-dive, and Artifacts is an output panel, not a codebase tool.

---

## Scenario 7 - The Project That Started Giving Wrong Answers

**Domain:** Troubleshooting and Optimization (10%) / Configuration and Knowledge Management (12%)

### Scenario

A sales team's shared Project drafts client quotes. It worked well for months, but since a price change last week, every team member's drafts quote the old prices - regardless of how they phrase their prompts. One member suggests everyone add "use the NEW prices" to their prompts; another suggests switching to a more capable model. What is the best fix?

**A.** Everyone adds "use the new prices" to every prompt.

**B.** Switch the team to the most capable model.

**C.** Check the Project's knowledge files, remove the outdated rate card, upload the current one, and re-test the workflow.

**D.** Delete the Project and go back to individual ad hoc chats.

### Solution

**Correct Answer: C**

A failure that is systematic across all users of a Project points at configuration, not prompting. The knowledge base contains a stale rate card; curation (remove, replace, re-test) is the permanent fix at the root cause.

**Why other answers are wrong:**
- **A** - A per-prompt patch fights the configuration every single time, and Claude may still surface the stale file's numbers; it also leaves the landmine for the next user.
- **B** - Model capability cannot fix wrong reference data; a stronger model quotes the stale price more eloquently.
- **D** - Destroys a working team asset over a one-file curation problem.

---

## Scenario 8 - A Vague Prompt and a Generic Output

**Domain:** Prompting and Task Execution (14%)

### Scenario

A junior consultant types "write a proposal for the client" into Claude and receives a generic, boilerplate proposal that could apply to any company. He concludes Claude is not good at proposals. Which change would most improve the result?

**A.** Regenerate the response several times until a better proposal appears.

**B.** Rewrite the prompt with the client's context and source material attached: the audience, the scope being proposed, the win themes, format and length, plus a past successful proposal as a style example.

**C.** Switch to the most capable model and send the same one-line prompt.

**D.** Ask Claude to "be less generic" with no other change.

### Solution

**Correct Answer: B**

Generic output is the signature of a context-free prompt. The fix is information: audience, task specifics, source material, constraints, format, and an example of what good looks like. A past winning proposal as a few-shot example is the single highest-leverage addition.

**Why other answers are wrong:**
- **A** - Regeneration re-rolls the dice on the same missing information.
- **C** - A stronger model given no context produces more eloquent boilerplate.
- **D** - "Less generic" gives Claude nothing to be specific WITH; specificity requires content, not adjectives.

---

## Scenario 9 - The 80-Message Chat That Lost the Plot

**Domain:** Troubleshooting and Optimization (10%)

### Scenario

A strategy consultant has iterated with Claude across one very long chat for two weeks: market analysis, three re-scopes, several abandoned drafts, and a final structure agreed near the end. Now Claude keeps mixing content from abandoned drafts into new sections and re-raising decisions that were already settled. What should she do?

**A.** Ask Claude to summarize the agreed structure, key decisions, and constraints; verify the summary; then continue the work in a fresh chat seeded with that summary (or move it into a Project if the work will continue for weeks).

**B.** Continue in the same chat but type all previous decisions again before each request.

**C.** Scold Claude in the chat until it stops referencing old drafts.

**D.** Start a completely blank chat and rebuild all context from memory each time.

### Solution

**Correct Answer: A**

Long chats accumulate contradictions and superseded drafts, and attention over a sprawling history degrades. The standard fix: distill state into a verified summary, restart fresh with it, and promote durable context into a Project if the engagement continues.

**Why other answers are wrong:**
- **B** - Keeps the contaminated history in play while adding manual retyping forever.
- **C** - Complaints add tokens, not clarity; the contradictory history remains.
- **D** - Throws away the useful context along with the noise; the verified summary is the bridge.

---

## Scenario 10 - Rolling Out Claude to a 40-Person Department

**Domain:** Workflow Integration and Solution Design (16%) / Governance (15%)

### Scenario

A department head wants her 40-person team to use Claude. Options on the table range from "buy licenses for everyone today and let them figure it out" to "block AI tools entirely until a two-year policy project completes". Several staff are already quietly using personal AI accounts for work documents. What is the best approach?

**A.** Buy licenses for all 40 people immediately with no guidance; usage will sort itself out.

**B.** Ban all AI use until a comprehensive policy is finished in two years.

**C.** Ignore the personal-account usage since it is not officially sanctioned.

**D.** Stand up a governed workspace (Team/Enterprise), publish a short usage policy covering data rules and review gates, pilot 2-3 measured workflows with a small group, train them on prompting and validation basics, then expand based on pilot results - and direct existing personal-account use into the sanctioned workspace.

### Solution

**Correct Answer: D**

This combines the rollout pattern (pilot, measure, train, expand) with the governance pattern (governed workspace, clear rules, absorb shadow AI into the official path). The existing personal-account use is a live data risk that a ban would push further underground; a capable sanctioned option plus rules is the mature fix.

**Why other answers are wrong:**
- **A** - Big-bang with no training or rules produces inconsistent quality and data incidents; measurement is impossible.
- **B** - Bans do not stop usage, they hide it; two years of shadow AI is the worst governance outcome.
- **C** - Ignoring known client/company data flowing through personal accounts is a governance failure in itself.
