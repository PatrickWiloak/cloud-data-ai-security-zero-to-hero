---
last-updated: 2026-08-11
---

# Domain 3 - Governance, Risk, and Responsible Use (15%)

## Overview

This domain tests judgment about data, policy, and responsibility when using Claude in a business context. It is not a legal exam; it tests whether you can spot the risk in a scenario and choose the option that protects the client, the data, and your organization while still getting the work done.

Two framing rules cover most questions:

1. **The strictest applicable rule wins** - Anthropic's usage policies, your company's AI policy, and the client's contract all apply at once. If any of them forbids something, it is forbidden.
2. **When the data situation is unclear, stop and ask** - the exam never rewards "paste it in and hope".

---

## Data Handling: The Core Risk

### Whose data is it?

Before putting anything into Claude, classify what you are holding:

| Data type | Examples | Handling |
|---|---|---|
| Public | Published reports, public web content | Generally fine |
| Internal | Your company's plans, drafts, internal metrics | Per your company's AI policy, on a company-governed plan |
| Client-confidential | Client documents, deal terms, unreleased results | Only under the client's agreed terms, on an appropriately governed plan |
| Personal data | Names with HR, health, financial details; anything identifying individuals | Minimize, redact, and follow privacy policy and law |
| Regulated | Health records, card data, classified material | Usually out of bounds without explicit approved arrangements |

### Plans and terms matter

Consumer plans and commercial plans (Team, Enterprise) carry different data-handling terms, and Enterprise adds admin controls: user management, audit-relevant controls, and organization-wide settings. The recurring exam pattern: an employee uses a **personal** Claude account for **client** data. That is the wrong setup regardless of how good the output is - business use of business or client data belongs in the organization's governed workspace under its terms.

You do not need to memorize legal terms. You need the reflex: *check which plan and terms cover the workspace before the data goes in.*

### Data minimization and redaction

Even in an approved workspace, share only what the task needs:

- Summarizing a contract's payment terms does not require the whole data room.
- Analyzing interview feedback rarely requires candidate names - replace them with "Candidate A/B".
- Strip identifiers, account numbers, and health or financial details that are not load-bearing for the task.

Minimization is almost always part of the correct answer in data scenarios; it reduces the blast radius of any mistake.

---

## Responsible Use of Outputs

### Accountability

The human who uses the output is accountable for it. "Claude wrote it" is never a defense for an error, a biased decision, or an IP problem. This principle from Domain 1 is also a governance principle: organizations should make ownership explicit - every AI-assisted deliverable has a named human owner who reviewed it.

### Disclosure

Whether and how to disclose AI assistance depends on:

- **Client contract** - some engagements require disclosure or prohibit AI use for certain work products. Check the contract or ask the engagement lead.
- **Company policy** - many organizations set disclosure rules for external content.
- **Context norms** - academic, journalistic, and regulatory contexts often have explicit rules.

The exam-safe position: know the applicable policy, follow it, and never misrepresent AI-assisted work as something it is not when disclosure is required.

### Bias and fairness

AI outputs can reflect biases from training data or from the prompt itself. This matters most when outputs feed decisions about people:

- Screening or ranking candidates, performance summaries, credit or eligibility assessments.
- The correct pattern: extra human scrutiny, structured criteria defined by humans, and Claude in a drafting/summarizing role rather than a deciding role.
- Some jurisdictions regulate automated decision-making about people; that is another reason the human decision point is not optional.

### Intellectual property

- Treat Claude's output as material your organization is responsible for publishing.
- Check that quotes and close paraphrases are attributed to their sources.
- Follow your company's guidance on using AI output in trademarked, patented, or contractually sensitive material.

---

## Appropriate Use and Refusals

Anthropic's usage policies prohibit harmful uses (deception, harassment, illegal activity, and similar categories). Company policies typically add restrictions (e.g., no AI on certain client engagements, no personal-account use for work).

Two exam-relevant behaviors:

1. **Refusals are a feature.** If Claude declines something that is genuinely against policy, the correct response is to accept it, not to rephrase deceptively until it complies. If the task is legitimate and the refusal is a misunderstanding, clarify your intent and context honestly - that is fine and often works.
2. **Do not launder prohibited tasks.** Splitting a prohibited task into innocent-looking pieces, or misdescribing the purpose, is a policy violation even if it technically produces output.

---

## Governance for Teams

An associate-level professional is expected to help a team use Claude safely, not just themselves:

- **Written AI usage policy** - what data classes may be used, on which plan, for which tasks; who approves exceptions.
- **Approved workspace** - work happens in the organization's Team/Enterprise workspace, not personal accounts. Admins manage access centrally.
- **Training** - people get the basics of prompting, validation, and data rules before heavy use.
- **Review gates** - defined in the workflow (Domain 2): what needs human review, what needs expert review.
- **Auditability** - for regulated or high-stakes work, keep a record: what was AI-assisted, what sources were used, who verified it. Enterprise-grade plans support organizational oversight; the team supplies the habit.
- **Incident path** - people know what to do if data goes somewhere it should not have (report it, do not hide it). Speed of reporting is what limits damage.

### Shadow AI

If the official path is too locked down, people quietly use personal accounts - which is the worst governance outcome because it is invisible. The mature answer in these scenarios is to provide a governed, capable official option plus clear rules, not to ban and look away.

---

## A Practical Pre-flight Checklist

Before a Claude task involving non-public data, a business user should be able to answer:

1. Whose data is this, and how sensitive is it?
2. Am I in the right workspace (organization plan, not personal) for this data?
3. Does the client contract or company policy restrict AI use for this task?
4. Have I minimized - removed data the task does not need?
5. Who reviews the output before it is used, and does this deliverable require disclosure?

If any answer is "I don't know", the correct next step is to find out, not to proceed.

---

## Worked Example

Scenario: a consultant wants Claude to summarize a client's unreleased quarterly financials for an internal steering meeting. She has a personal Pro account and her firm has an Enterprise workspace.

Correct handling:

1. Use the firm's Enterprise workspace, never the personal account, for client-confidential data.
2. Confirm the engagement terms permit AI processing of client material; if unclear, ask the engagement lead.
3. Minimize: upload the financials package sections needed for the summary, not the entire data room.
4. Ground and verify: ask for a cited summary, check every figure against the source (Domain 1).
5. Label the summary as AI-assisted per firm policy, with the consultant as accountable reviewer.

Every step maps to a question the exam can ask independently.

---

## Key Takeaways

1. Strictest rule wins: Anthropic policy, company policy, and client contract all apply simultaneously.
2. Client and company data belongs in the organization's governed workspace, never personal accounts.
3. Minimize and redact - share only what the task needs.
4. Humans own outputs and decisions; Claude never carries accountability, especially in decisions about people.
5. Follow disclosure rules; never evade a legitimate refusal.
6. Good team governance is an enabling policy plus a governed workspace plus training plus review gates - not a ban.

**[📖 Claude Help Center](https://support.claude.com)** - plan features and product documentation
**[📖 Claude.ai](https://claude.com)** - plan comparison, including Team and Enterprise capabilities
