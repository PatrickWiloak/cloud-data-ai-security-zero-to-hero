# 09 - Stakeholder Communication and Lifecycle Management

Domain 5 of CCAR-P (14%). Professional-level architects do not just design systems; they get them funded, launched, adopted, and maintained. This domain tests whether you can translate agentic architecture into business language, run a disciplined rollout, and manage the model lifecycle after launch. Engineers underestimate this domain; at 14% it carries the same weight as Governance and more than Context Engineering.

---

## Translating Architecture for Executives and Clients

### The Altitude Rule

Executives do not need to know what a cache breakpoint is. They need to know what the system does, what it costs, what can go wrong, and what you are doing about it. Translate every technical decision into one of four business dimensions:

- **Value** - what outcome improves, by how much
- **Cost** - what it costs to run, per outcome
- **Risk** - what can go wrong, likelihood, blast radius, mitigation
- **Time** - when it ships, what phases, what gates

### Translation Examples

| Technical decision | Executive framing |
|---|---|
| "Single-agent tool loop instead of multi-agent" | "Simpler design: 40% cheaper per request and easier to debug, same quality on our tests" |
| "Prompt caching on the static prefix" | "Repeat questions cost about a tenth as much to serve" |
| "Haiku triage in front of Sonnet" | "Simple requests go to a cheaper model automatically; average cost drops without quality loss" |
| "Regression gate in CI" | "No change reaches customers unless it scores at least as well as what is live today" |
| "Human approval on refunds" | "The system drafts, a person approves; it cannot move money alone" |

### Communicating Uncertainty Honestly

Claude is probabilistic. Say so up front, in concrete terms:

- Give ranges, not point estimates: "resolves 70-80% of tickets without escalation" beats "resolves tickets"
- Name the failure modes: wrong answers stated confidently, occasional refusals of valid requests, degraded quality on out-of-distribution inputs
- Explain the safety nets in the same breath: evals, human escalation, monitoring
- Never promise determinism. A stakeholder surprised by nondeterminism in month two is a trust problem you created in month zero.

---

## Cost and ROI Framing

### Cost-Per-Outcome, Not Tokens

Nobody budgets in tokens. Convert:

1. Model the token cost per typical interaction (input + cached + output + thinking)
2. Multiply to cost per business outcome (per ticket resolved, per document processed, per lead qualified)
3. Compare against the current cost of that outcome (human handle time, vendor fees, opportunity cost)
4. State the margin of error and what drives it (conversation length, escalation rate)

### The ROI Conversation

- **Direct savings** - handle-time reduction, deflection rate, throughput per head
- **Revenue effects** - faster response, longer coverage hours, higher conversion
- **Cost of the system** - inference, engineering, evaluation, ongoing operations (not just the API bill)
- **Sensitivity** - which assumption breaks the case first; usually adoption rate or escalation rate

Present a pilot-verified number over a projected one whenever possible. "In the 4-week pilot the agent resolved 62% of tier-1 tickets at $0.11 each" ends arguments that projections start.

---

## Rollout Phasing: Pilot to Production

### The Standard Ladder

1. **Internal dogfood** - employees only; goal is finding embarrassing failures cheaply
2. **Closed pilot** - a small, friendly customer cohort; goal is measuring real quality, cost, and escalation rates
3. **Limited GA** - a percentage of traffic or a segment; goal is validating at scale under monitoring
4. **General availability** - full traffic, with rollback still rehearsed

Each promotion passes an evaluation gate (below). Each phase has an owner, entry criteria, exit criteria, and a rollback plan. Skipping straight to GA is the most common rollout failure the exam will test.

### Evaluation Gates for Go/No-Go

A gate is a pre-agreed set of thresholds measured on evidence, decided before emotions and sunk costs accumulate:

- **Quality** - eval score at or above baseline; task success rate at or above the phase target
- **Safety** - red-team suite pass; violation and false-refusal rates within bounds
- **Cost** - cost per outcome within budget at observed usage patterns
- **Operations** - alerting live, runbook written, on-call named, rollback tested

Write the thresholds down before the phase starts. A go/no-go meeting that invents its criteria in the room is theater.

---

## Model Version Lifecycle Management

### Deprecations Are a Certainty

Model versions retire. Anthropic publishes deprecation notices with migration windows; Bedrock and Vertex retire region-scoped IDs on their own schedules. Lifecycle management is not optional at Professional level.

**[📖 Anthropic model deprecations](https://docs.anthropic.com/en/docs/about-claude/model-deprecations)** - current deprecation status and dates.

### Pinning vs Auto-Upgrading

- **Pin** production to a dated model snapshot. Behavior changes between versions; an unreviewed upgrade is an unreviewed behavior change to your product.
- **Auto-upgrade aliases** (latest-style IDs) are acceptable for internal tools and experiments, never for gated production paths.
- Treat a model upgrade exactly like a code release: eval comparison, shadow traffic where feasible, phased rollout, rollback plan.

### Migration Playbook

1. Inventory which systems use the deprecating version (your model risk inventory, note 08, gives you this for free)
2. Run the full eval suite on the successor model; diff quality, cost, latency, and safety
3. Update prompts where the new model's behavior shifted; newer models often need less scaffolding
4. Phase in via weighted routing or feature flags; monitor cohort metrics
5. Keep the old version configured for rollback until after the deprecation cutoff planning allows
6. Update documentation and the model inventory; notify stakeholders of any user-visible behavior change

### Communicating Model Changes

Model upgrades can change tone, verbosity, and edge-case behavior even when eval scores improve. Tell customer-facing teams before their users tell them. A one-page "what changed, what to expect, who to contact" note prevents a support fire.

---

## Documentation and Runbooks

Deliverables a Professional architect ships alongside the system:

- **Architecture decision records (ADRs)** - what was chosen, what was rejected, why; the future team inherits your reasoning, not just your code
- **Runbook** - alert-by-alert response procedures: quality drift, cost spike, provider outage, guardrail trip, model deprecation notice
- **System card / model use documentation** - purpose, data flows, limitations, evaluation evidence; doubles as EU AI Act and procurement documentation
- **Escalation matrix** - who is paged for what, and who can authorize a rollback or kill switch
- **Change log** - every prompt, model, and tool change with its eval delta

If only the person who built it can operate it, the project is not done.

---

## Training and Enablement

Adoption fails without enablement, and the ROI case dies with adoption.

- **End users** - what the assistant can and cannot do, how to phrase requests, how to escalate; short and example-driven
- **Support and operations teams** - how to read traces, common failure signatures, when to page engineering
- **Reviewers (human-in-the-loop)** - what they are approving, what to look for, how their decisions are logged
- **Leadership** - the dashboard: quality trend, cost per outcome, adoption, incident count

Plan enablement as a project workstream with owners and dates, not as an email on launch day.

---

## Post-Launch Review Loops

Launch is the midpoint, not the finish.

- **Weekly (early life)** - quality metrics, escalation rate, cost per outcome, top failure categories; feed real failures back into the eval set
- **Monthly** - stakeholder review against the original ROI case; adoption and satisfaction trends
- **Quarterly** - model version review (anything deprecating?), risk re-tiering, guardrail effectiveness (both violation and false-refusal rates), and a decision: invest, maintain, or retire
- **Incident-driven** - every user-visible failure gets a lightweight postmortem; recurring patterns become eval cases and runbook entries

The loop that matters most: production failures become eval cases. That single habit turns incidents into a permanently rising quality floor.

---

## Handling Common Stakeholder Objections

You will face the same objections on every engagement. Have the answers ready:

- **"Can it be 100% accurate?"** No system is, including the human process it replaces. Reframe to the comparison that matters: current human error rate vs the agent's measured rate plus its escalation safety net.
- **"What if it says something embarrassing?"** Walk through the layered guardrails, the false-refusal tradeoff, and the incident process. Offer the pilot phase as the place embarrassing failures get found cheaply.
- **"Why is this so expensive to build if the API is cheap?"** The API call is the smallest cost. Evaluation, integration, governance, and enablement are the engineering; they are also what separates a demo from a product.
- **"Can we just use the newest model automatically?"** Explain pinning: version changes are behavior changes, and behavior changes go through the gate.
- **"Why do we still need people in the loop?"** Because some actions are irreversible and some risk is not worth automating. The human gate is a feature the auditors and customers will ask for by name.

Answering these calmly, with pilot data, is the skill Domain 5 measures.

---

## Communication Artifacts Checklist

The artifacts a Professional architect produces per engagement, and their audiences:

| Artifact | Audience | Cadence |
|---|---|---|
| Executive brief (value, cost, risk, timeline) | Sponsors | Per phase gate |
| Go/no-go gate definition | Sponsors + engineering | Before each phase |
| ADRs | Engineering, future maintainers | Per major decision |
| Runbook + escalation matrix | Operations, on-call | Living document |
| System card / model use documentation | Compliance, procurement, regulators | Per release |
| Migration plan | Engineering + stakeholders | Per deprecation notice |
| Metrics dashboard | Leadership | Continuous |
| Enablement materials | End users, support, reviewers | Before each rollout phase |

If asked on the exam which document serves which audience, the pattern is: sponsors get outcomes and gates, engineers get decisions and procedures, compliance gets data flows and evidence, users get capabilities and escape hatches.

---

## Exam Focus

Expect scenarios like:

- "The CFO asks what the agent costs" - cost per business outcome with pilot-verified numbers, not token math
- "A new model version is announced; production pins an old one" - eval comparison, phased migration, rollback held; never silent auto-upgrade
- "The pilot missed its quality target but the sponsor wants to launch" - the pre-agreed gate holds; report evidence, propose a remediation phase
- "Users are surprised the assistant sometimes refuses valid requests" - an expectation-setting and enablement failure; fix communication and measure false refusals
- "What documents does the operations team need" - runbook, escalation matrix, trace-reading guide
- "How do you keep quality improving after launch" - failures feed the eval set; scheduled review loops with owners
