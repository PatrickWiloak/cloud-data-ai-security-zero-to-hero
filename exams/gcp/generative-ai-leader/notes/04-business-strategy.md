---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 9 min
---

# 04 - Business strategies for a successful generative AI solution

Weighted more heavily than a technical reader expects. This is the section that distinguishes the exam from every other AI certification in this repo.

---

## Finding use cases worth doing

Start from the business problem, not the technology.

Good candidates share features:
- A **repetitive task involving language, images, or unstructured content**
- A **measurable outcome**: time saved, cost avoided, revenue enabled, quality improved
- **Tolerance for imperfection**, or a workable human review step
- **Available data**, if grounding or customization is needed

Poor candidates:
- Anything requiring guaranteed correctness with no review, such as an unchecked regulatory filing
- Problems a deterministic system solves better: arithmetic, rules-based routing, exact lookup
- Cases with no measurable outcome, which cannot be justified or evaluated
- Cases where the data does not exist or cannot be used

**Not everything needs generative AI.** The exam includes scenarios where a rules engine, a search index, or a classical ML model is the right answer, and recognizing them is part of what is being tested.

---

## Prioritizing

The standard framing is **value against feasibility**:

| | Low feasibility | High feasibility |
|---|---|---|
| **High value** | Strategic bets: invest deliberately, expect a longer timeline | **Start here.** Quick wins that build credibility |
| **Low value** | Avoid | Only if genuinely trivial |

Early projects should be chosen partly for their **demonstration value**: a visible, quick success builds the organizational appetite that later, harder projects need.

---

## The business case

What a credible case contains:

- The problem, and what it costs today
- The proposed approach, and which rung of the ladder it sits on
- **Expected benefit**, quantified where possible
- **Total cost of ownership**, not just inference
- **Success criteria**, defined before building
- Risks and how they are mitigated
- Who owns it after launch

**Total cost of ownership** components people forget:
- Data preparation, cleaning, and access work, usually the largest hidden cost
- Integration with existing systems
- Evaluation, both initial and ongoing
- Monitoring and incident response
- Model version changes and re-testing
- Change management and training
- Human review capacity, where it is required

Inference cost is usually visible and often not the largest line.

---

## Data readiness

The most common real constraint, and the exam reflects that.

Questions worth asking before committing:
- Does the data exist, and is it accessible?
- Is it accurate, current, and consistent enough?
- Are we permitted to use it, contractually and legally?
- Is it governed: classified, access-controlled, with an owner?
- If we ground on it, will retrieval respect existing permissions?

An organization with poor data governance will find that generative AI **surfaces** the problem rather than solving it. An assistant honors existing permissions, so pre-existing oversharing becomes visible exposure on day one.

---

## Change management and adoption

Deploying a tool is not adoption.

- **Communicate the why**, including honestly addressing job-impact concerns
- **Train** users on effective use, including its limits
- **Redesign the workflow**; bolting AI onto an unchanged process rarely delivers the benefit
- **Identify champions** within teams
- **Collect feedback** and iterate visibly
- **Measure adoption**, not just deployment

Organizational readiness includes skills, governance, and executive sponsorship. A technically successful pilot with no adoption plan is the common failure mode.

---

## Responsible AI

Google's themes, each with a practical control:

| Theme | Means | Control |
|---|---|---|
| **Fairness** | Avoid creating or reinforcing unfair bias | Test outputs across affected groups; diverse evaluation data |
| **Transparency** | People know AI is being used and what it does | Disclosure in the interface; documentation |
| **Explainability** | Decisions can be explained to those affected | Citations, grounding, documented model behavior |
| **Privacy** | Personal data is protected throughout | Minimization, redaction, access control, retention limits |
| **Safety and security** | The system behaves acceptably and resists attack | Safety filters, adversarial testing, secure design |
| **Accountability** | A human is responsible for outcomes | Named owner, human in the loop, audit trail |

Reference frameworks the exam guide names: **Google's AI Principles** and the **Secure AI Framework (SAIF)**.

---

## Risk

| Risk | Shape | Mitigation |
|---|---|---|
| **Hallucination in customer-facing use** | A confident wrong answer given to a customer | Grounding, citations, scope limits, human review for high-stakes replies |
| **Data leakage** | Sensitive data reaching the wrong user or leaving the organization | Retrieval authorization on the end user's identity, DLP, enterprise data controls |
| **Intellectual property** | Uncertainty over generated content and training data provenance | Provider indemnity terms, review process, legal input |
| **Regulatory exposure** | Sector rules and emerging AI regulation | Classify systems by risk, maintain documentation, follow [EU AI Act](../../../../resources/compliance-guides/eu-ai-act.md) and similar regimes |
| **Over-reliance** | Users accepting output without scrutiny | Training, interface design that signals uncertainty, human review |
| **Cost overrun** | Usage growing faster than expected | Budgets, quotas, monitoring, model tiering |
| **Prompt injection and misuse** | Attacker-supplied text changing system behavior | Bounded permissions, output validation, see [AI security](../../../../resources/ai-security/) |

---

## Human in the loop

Where to keep a person in the decision:
- High-stakes decisions: credit, employment, healthcare, legal
- Anything irreversible or outward-facing
- Regulated decisions requiring explanation or appeal
- Any case where the cost of a rare wrong answer exceeds the aggregate benefit of automation

Where full automation is reasonable: low-stakes, high-volume, reversible tasks with good measurement in place.

Recognizing which side of that line a scenario falls on is a repeated exam pattern.

---

## Measuring impact

Define before building, evaluate after:
- **Business metrics**: time saved, cost per case, conversion, resolution rate, customer satisfaction
- **Quality metrics**: accuracy, faithfulness, refusal rate
- **Operational metrics**: latency, availability, cost per request
- **Adoption metrics**: active users, proportion of eligible work handled

Then iterate. Generative AI systems degrade quietly as data, models, and usage change, so evaluation is an ongoing program rather than a launch gate.

---

## Key terms

- **Use case prioritization** - selecting projects by business value against feasibility
- **Total cost of ownership** - the full lifetime cost including data preparation, integration, evaluation, and change management
- **Data readiness** - whether data exists, is accessible, accurate, permitted, and governed enough to use
- **Change management** - the organizational work of training, communication, and workflow redesign that drives adoption
- **Organizational readiness** - the skills, governance, and sponsorship needed for a project to succeed
- **Responsible AI** - the practice of building AI that is fair, transparent, explainable, private, safe, and accountable
- **Google AI Principles** - Google's published commitments governing its AI development and use
- **Secure AI Framework (SAIF)** - Google's conceptual framework for securing AI systems
- **Human in the loop** - requiring human review or approval before a consequential AI output is acted on
- **Over-reliance** - the risk that users accept AI output without appropriate scrutiny
- **Explainability** - the ability to explain an AI-influenced decision to the person it affects
- **Adoption metric** - a measure of how much of the eligible work actually flows through the new capability

---

## Related

- [Notes 01: generative AI fundamentals](./01-genai-fundamentals.md)
- [EU AI Act](../../../../resources/compliance-guides/eu-ai-act.md)
- [NIST AI RMF](../../../../resources/compliance-guides/nist-ai-rmf.md)
- [AI security](../../../../resources/ai-security/)
