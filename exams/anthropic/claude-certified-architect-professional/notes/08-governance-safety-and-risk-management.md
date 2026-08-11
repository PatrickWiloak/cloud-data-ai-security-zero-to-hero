# 08 - Governance, Safety and Risk Management

Domain 4 of CCAR-P (14%). This domain tests whether you can run Claude in an enterprise without creating legal, privacy, or safety exposure. The controls here are part technical (guardrails, logging) and part organizational (policies, review boards, sign-offs). Exam questions frequently give a scenario with a regulatory or risk constraint and ask which control satisfies it. Watch for questions where the correct answer is a process, not a piece of code.

---

## Usage Policies and Acceptable Use

Every Claude deployment inherits two policy layers:

1. **Anthropic's usage policies.** Your application must comply with Anthropic's usage policy regardless of deployment path (first-party, Bedrock, Vertex). High-risk use cases (medical, legal, financial advice to consumers) carry additional requirements such as human review and disclosure.
2. **Your organization's own AI policy.** Enterprises typically layer an internal policy on top: which teams may use which models, which data classifications may enter prompts, which use cases need review board approval.

Architect responsibilities:

- Map each use case against both policy layers before build, not after
- Encode policy in the system, not just in a document: input filters, allowed-tool lists, data classification checks at the boundary
- Establish an escalation path for gray-area use cases

**[📖 Anthropic Trust Center](https://trust.anthropic.com)** - compliance attestations and policy documentation.

---

## Data Privacy and Retention

### Retention Defaults

By default, API inputs and outputs may be retained short-term for abuse and misuse detection. Anthropic does not train on API customer data by default. Know the difference between:

- **Training use** - whether your data improves future models (off by default for API traffic)
- **Retention** - whether your data is stored at all after the request is served

### Zero Data Retention (ZDR)

ZDR means inputs and outputs are not retained after the response is served. Key facts:

- Contractual arrangement for qualified enterprise customers, not a request-time flag
- Available on the first-party API; verify current Bedrock and Vertex posture separately
- ZDR affects some features: anything that requires server-side persistence (long-lived caches, some batch mechanics) needs review under ZDR

### Bedrock and Vertex Data Handling

- **Bedrock:** prompts and completions are not shared with Anthropic or used to train models; data stays in the AWS region you selected. CloudTrail records the API call, not the prompt body, unless you enable invocation logging (which you control).
- **Vertex:** similar posture on Google's side; data residency follows the regional endpoint, and VPC Service Controls can fence egress.

Design rule: treat the deployment path's data handling as part of your data flow diagram. If your DPA or DPIA says "no PII leaves the EU", the region choice and retention posture are the enforcement mechanism.

### Minimization

The cheapest privacy control is not sending the data:

- Redact or tokenize PII before it enters the prompt where the task allows
- Retrieve only the fields the task needs, not whole records
- Strip identifiers from logs and traces; store prompt hashes rather than raw prompts where full text is not needed

---

## Safety Guardrails and Content Moderation

Production systems layer defenses; no single layer is sufficient.

### The Layered Model

1. **Input layer** - classify incoming requests before the main model sees them. A Haiku-based classifier can flag jailbreak attempts, disallowed topics, or off-policy requests cheaply.
2. **Model layer** - Claude's own training resists harmful requests and refuses appropriately. System prompt constraints narrow behavior further.
3. **Output layer** - classify responses before they reach the user: PII leakage, policy violations, off-brand content.
4. **Action layer** - for agents, the tool boundary is the last control that can refuse. Scope credentials narrowly, validate authorization in code, and require human approval for irreversible actions.
5. **Platform layer** - Bedrock Guardrails or your own moderation service can wrap any of the above with configurable filters.

### Measuring Guardrails

Track two rates, not one:

- **Violation rate** - harmful content that got through
- **False refusal rate** - legitimate requests that were blocked

Optimizing only for violations produces an over-blocking product that fails users a different way. Report both to stakeholders.

### Refusal Handling

Refusals are a feature, not an error. Do not retry refusals as if they were transient failures - repeated retries of a refused request is itself a signal worth alerting on (potential misuse attempt).

---

## Prompt Injection and Jailbreak Risk Management

### The Threat

- **Jailbreak** - the user tries to talk the model out of its constraints
- **Direct prompt injection** - the user embeds instructions that override the system prompt
- **Indirect prompt injection** - untrusted content the agent retrieves (a web page, a document, a tool result) carries instructions aimed at the model

Indirect injection is the dominant risk for agents, because agents ingest content nobody vetted.

### Defense Posture

Assume injection can succeed sometimes. Design so that a successful injection has bounded consequences:

- Wrap untrusted content in explicit XML tags and instruct Claude to treat it as data, not instructions
- Give each tool the narrowest credential that does its job; a compromised read tool must not be able to write
- Check authorization against the calling user in code at the tool boundary, never in the prompt
- Require human confirmation for irreversible or high-impact actions (payments, deletions, external sends)
- Treat model output as untrusted downstream: escape it, validate it, never eval it
- Run a standing red-team suite (jailbreaks, injections, PII probes) on every prompt or model change; injection resistance regresses silently

The exam pattern: any answer that relies solely on "instruct the model to ignore injected instructions" or "filter for suspicious phrases" is a distractor. Correct answers bound consequences at the tool boundary.

---

## Audit Logging

Auditability is a governance requirement, not just a debugging convenience.

### What to Log

Per model call: timestamp, caller identity (user, tenant, service), model ID and version, prompt hash (or full prompt where policy allows), token counts, cost, stop reason, tool calls with arguments and results, and any guardrail decisions (blocked, flagged, approved-by-human).

### Where It Lives

- **First-party API** - your application must emit the audit trail; Anthropic provides request IDs to correlate
- **Bedrock** - CloudTrail records every InvokeModel call natively; enable model invocation logging for payloads if policy requires
- **Vertex** - Cloud Audit Logs record API activity; Cloud Logging for payloads if enabled

### Properties Auditors Expect

- Tamper-evident (write-once storage or append-only stream)
- Survives the agent process dying mid-run
- Retained per your records schedule (often 1-7 years in regulated industries)
- Queryable by incident responders without engineering help

---

## Compliance Mapping

| Framework | What It Means for a Claude Deployment |
|---|---|
| SOC 2 Type II | Anthropic holds this for its service; your system needs its own controls for the application layer |
| GDPR | You are the controller, the model provider is a processor; document lawful basis, retention, data subject rights, and cross-border transfer mechanism |
| HIPAA | Requires a signed BAA; use HIPAA-eligible endpoints (first-party API and Bedrock support BAA coverage); control PHI access and logging on your side |
| ISO 27001 / 42001 | 27001 covers information security management, 42001 covers AI management systems; both appear in enterprise procurement checklists |
| EU AI Act | Claude models are GPAI; as the deployer you carry transparency, documentation, and risk-assessment obligations that scale with the use case |

Compliance questions usually turn on who owns the control: the model provider attests to service-side controls, you own everything from the prompt to the user.

---

## Model Risk Management

Borrowed from financial services (SR 11-7 style thinking) and increasingly expected everywhere:

1. **Inventory** - every deployed model use case has an entry: owner, purpose, model ID, data classification, risk tier
2. **Validation evidence** - eval results, red-team results, and known limitations documented before launch
3. **Risk tiering** - a customer-facing medical triage agent and an internal doc summarizer do not get the same review depth
4. **Ongoing monitoring** - quality drift, safety regression, and cost anomalies alert to a named owner
5. **Review cadence** - periodic re-validation, and mandatory re-review on model version changes
6. **Decommissioning** - retired use cases leave the inventory with a record of why

---

## Human-in-the-Loop for High-Stakes Actions

Not all automation should be autonomous. Decide per action, not per system:

- **Autonomous** - low-impact, reversible actions (draft a reply, summarize a document)
- **Approve-before-execute** - the agent proposes, a human confirms (send the email, issue the refund)
- **Human-performs** - the agent only recommends; a human executes (medical decisions, legal filings)

Design considerations:

- Make the approval surface show what will actually happen (the exact email, the exact amount), not a paraphrase
- Batch approvals fatigue reviewers into rubber-stamping; keep high-stakes approvals rare and meaningful
- Log the approval as part of the audit trail: who approved, what they saw, when
- Agent SDK hooks (pre-tool) are the natural interception point for approval gates

---

## Incident Response for AI Systems

Traditional incident response extends to model-specific incident classes:

| Incident class | Example | First response |
|---|---|---|
| Harmful output reached a user | Policy-violating content served | Preserve the trace, notify per policy, add the case to the red-team suite |
| Prompt injection succeeded | Agent acted on injected instructions | Revoke or rotate the affected tool credentials, replay the trace, tighten the tool boundary |
| Data exposure | PII in a response or a log | Follow the breach process; retention posture determines scope |
| Guardrail outage | Classifier down, requests flowing unchecked | Fail closed for high-risk paths; degrade to human handling |
| Quality collapse | Eval score cliff after a dependency change | Roll back the change; bisect with attribution logging |

Two rules the exam rewards:

1. **Fail closed on high-risk paths.** If the moderation layer is down, a payments agent stops; a doc summarizer may continue. Decide per risk tier in advance, not during the outage.
2. **Every incident feeds the eval set.** The reproduction case becomes a permanent regression test, and the runbook gains an entry.

---

## Evidence for Auditors and Procurement

Enterprise deals and audits ask for the same artifacts repeatedly. Keep them current:

- Provider attestations (SOC 2 report, ISO certificates) pulled from the trust center
- Your DPA chain: who processes what data, where, under which terms
- The model risk inventory with validation evidence per use case
- Red-team results and remediation records
- Data flow diagrams showing where prompts, outputs, and logs live and for how long
- The human-in-the-loop matrix: which actions are autonomous, gated, or human-only

An architect who can produce these in a day closes enterprise deals that otherwise stall for a quarter.

---

## Exam Focus

Expect scenarios like:

- "A regulated customer requires that prompts never persist after the response" - ZDR, contractual, first-party API (verify per path)
- "An agent retrieved a document containing hidden instructions" - bound consequences at the tool boundary; do not rely on filtering
- "Which log satisfies the auditor" - tamper-evident, per-call, with identity and guardrail decisions
- "Who is responsible for GDPR compliance of the application" - you (controller); the provider is a processor
- "A payment agent needs a safety control" - approve-before-execute human gate at the tool boundary
- "How do you keep guardrails from over-blocking" - measure false refusal rate alongside violation rate
