---
last-updated: 2026-07-29
---

# AWS Certified Generative AI Developer - Professional (AIP-C01) - Exam Strategy

> Cert-specific tactics. General study advice lives in [study-strategies.md](../../../../resources/study-strategies.md). This page is what is different about AIP-C01.

## Format reminder

- 85 questions total, 65 scored and 10 unscored, 205 minutes
- Pass mark 750 / 1000 scaled
- Multiple choice (1 of 4) and multiple response (2+ of 5+)
- Compensatory scoring: you pass on the overall score, not domain by domain
- Multiple-response questions are all-or-nothing. Partial selections score zero

## Time management math

205 minutes across 85 questions is about **2.4 minutes per question**. GenAI scenarios
tend to be long, because they have to establish the model, the data, the latency budget,
and the compliance constraint before asking anything.

- Short service-recall questions (~20): 60-90 seconds
- Medium architecture scenarios (~45): 2-3 minutes
- Long multi-constraint scenarios (~20): 4-5 minutes

Aim to be at question 30 by minute 70 and question 60 by minute 145, leaving roughly
40 minutes for flagged items and review. **Answer every question.** There is no guessing
penalty, so a flagged guess always beats a blank.

## The top traps for this exam

1. **RAG versus fine-tuning versus prompt engineering.** The most common decision on the
   exam. The deciding constraint is usually in the last sentence. Knowledge that changes
   frequently or must be cited points to RAG. Consistent tone, format, or a domain
   vocabulary the base model lacks points to fine-tuning. Behaviour achievable with better
   instructions points to prompt engineering. Cost and latency budgets break ties.

2. **"Least operational overhead" versus "lowest cost."** These select different answers,
   exactly as on SAP-C02. Bedrock managed features (Knowledge Bases, Agents, Guardrails)
   usually win on overhead; a self-managed vector store on OpenSearch or pgvector can win
   on cost at scale. Read which criterion the question actually states.

3. **Guardrails are not the same as IAM.** Bedrock Guardrails filter content and block
   topics. They do not control who can invoke a model. Questions that describe preventing
   a team from calling a specific model want IAM policies or resource-based policy, not
   Guardrails.

4. **Knowledge Bases does not mean you skip chunking decisions.** Managed ingestion still
   exposes chunking strategy, embedding model choice, and metadata filtering. Questions
   about poor retrieval quality usually resolve to chunk size, overlap, or a missing
   metadata filter, not to swapping the foundation model.

5. **Provisioned Throughput versus On-Demand.** Provisioned Throughput buys committed
   capacity for predictable high volume and is the answer when the scenario stresses
   consistent throughput or guaranteed capacity. It is the wrong answer for spiky or
   low-volume workloads, where On-Demand is cheaper.

6. **Agents introduce failure modes that look like model problems.** When a scenario
   describes an agent calling the wrong tool or looping, the fix is usually the action
   group schema, the tool description, or the orchestration prompt, not a larger model.

7. **Evaluation questions want a method, not a vibe.** If a question asks how to know
   whether a change helped, the answer involves a held-out dataset and a defined metric,
   often LLM-as-a-judge with human spot checks, not "test it in the console."

## Domain weighting and where to spend effort

| Domain | Weight | Effort note |
|--------|-------:|-------------|
| 1. Foundation model integration, data management, compliance | 31% | Largest domain. RAG design and data handling dominate |
| 2. Implementation and integration | 26% | Agents, action groups, API integration patterns |
| 3. AI safety, security, and governance | 20% | Guardrails, IAM, PII handling, model access control |
| 4. Operational efficiency and optimisation | 12% | Caching, batching, model selection for cost and latency |
| 5. Testing, validation, troubleshooting | 11% | Evaluation methodology, debugging retrieval and agents |

Domains 1 and 2 are 57% of the exam between them. If time is short, make sure RAG
architecture and agent implementation are solid before polishing the smaller domains.

## Question triage

Read the **last sentence first** on long scenarios. It carries the decision criterion
(cost, latency, overhead, compliance) and often makes two of the four options obviously
wrong before you have read the setup.

For multiple-response questions, count the required selections and treat each option as an
independent true or false claim. Because scoring is all-or-nothing, a careful pass over
five options beats a fast guess.

Flag and move on after 90 seconds of no progress. GenAI scenarios reward a second read
with a clear head more than most exams, because the constraint you missed is usually a
single clause.

## The week before

- Re-read [bedrock-platform-deep-dive.md](notes/bedrock-platform-deep-dive.md) and
  [rag-architecture-deep-dive.md](notes/rag-architecture-deep-dive.md). Between them they
  cover the majority of the tested surface.
- Work [scenarios.md](scenarios.md) and write down why each distractor fails, not just
  which answer is right.
- Skim [aws-services-mapping.md](notes/aws-services-mapping.md) as a last-mile check that
  you can name the service for each capability.
- Do not start new material in the final three days. Consolidate instead.

## Exam day

Standard logistics are in the [exam-day checklist](../../../../resources/exam-day-checklist.md).
Two AIP-C01-specific notes:

- The exam is Professional-tier length. Take the offered break if you are at a testing
  centre, and pace hydration accordingly for online proctoring where you cannot leave.
- Expect several questions that feel like they have two right answers. They do. One is
  merely correct, the other is the AWS-recommended pattern under the stated constraint.
  Pick the recommended pattern.
