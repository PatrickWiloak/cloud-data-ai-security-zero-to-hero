---
last-updated: 2026-08-11
difficulty: advanced
---

# Claude Certified Architect - Professional (CCAR-P)

Official certification guide for the Claude Certified Architect - Professional exam (CCAR-P), released by Anthropic in July 2026. This is the senior tier above [Claude Certified Architect - Foundations](../claude-certified-architect-foundations/) (CCAR-F). It validates your ability to design, integrate, evaluate, govern, and operate large-scale production systems on top of Claude.

## Exam Overview

| Detail | Info |
|---|---|
| **Exam Code** | CCAR-P |
| **Duration** | 120 minutes |
| **Questions** | 63 multiple-choice and multiple-response |
| **Passing Score** | 720 / 1000 |
| **Cost** | $175 USD |
| **Delivery** | Pearson VUE - online proctored or test center |
| **Validity** | 12 months |
| **Level** | Professional |
| **Prerequisites** | None; CCAR-F recommended first |

Anthropic recommends, but does not require, passing CCAR-F before sitting CCAR-P. The exam targets AI engineers, solutions architects, staff-level software engineers, and platform leads who already ship Claude-powered products. It is not a beginner exam.

---

## Exam Domains (Blueprint v1.0, effective July 2026)

| # | Domain | Weight |
|---|---|---|
| 1 | Integration | 19% |
| 2 | Solution Design and Architecture | 17% |
| 3 | Evaluation, Testing and Optimization | 16% |
| 4 | Governance, Safety and Risk Management | 14% |
| 5 | Stakeholder Communication and Lifecycle Management | 14% |
| 6 | Claude Models, Prompting and Context Engineering | 13% |
| 7 | Developer Productivity and Operational Enablement | 7% |

### Domain Summaries

**1 - Integration (19%).** Connecting Claude to the systems around it: tool design, MCP servers and transports, first-party tools (code execution, computer use, web search, memory), the Agent SDK, streaming clients, and deployment through Amazon Bedrock and Google Cloud Vertex AI as well as the first-party API.

**2 - Solution Design and Architecture (17%).** Choosing the right architecture under cost, latency, and compliance constraints: single-agent tool loops vs orchestrator-worker vs planner-executor, RAG at scale, multi-tenant design, reliability patterns, and enterprise deployment topology (private networking, data residency).

**3 - Evaluation, Testing and Optimization (16%).** Eval harnesses, LLM-as-judge design and calibration, regression gates, tracing and observability, and the cost/latency toolkit: prompt caching economics, Batch API, model routing, and thinking-budget tuning.

**4 - Governance, Safety and Risk Management (14%).** Usage policies, data privacy and retention (including zero data retention), guardrails and content moderation layers, prompt injection and jailbreak risk management, audit logging, compliance mapping (SOC 2, GDPR, HIPAA), and human-in-the-loop design for high-stakes actions.

**5 - Stakeholder Communication and Lifecycle Management (14%).** Translating architecture decisions for executives and clients, cost and ROI framing, expectation setting on model behavior, rollout phasing from pilot to production, model version lifecycle (deprecations, migrations, pinning), evaluation gates for go/no-go decisions, and documentation, training, and post-launch review.

**6 - Claude Models, Prompting and Context Engineering (13%).** Model tier selection (Opus, Sonnet, Haiku), extended thinking and interleaved thinking, context window economics, the memory tool, summarization and compaction, and contextual retrieval.

**7 - Developer Productivity and Operational Enablement (7%).** Claude Code and Agent SDK workflows for teams, skills and hooks, shared MCP infrastructure, internal enablement, and operational runbooks.

---

## Registration and Logistics

- **Register** through the Anthropic Partner Academy: **[📖 Partner Certifications](https://anthropic-partners.skilljar.com/page/partner-certifications)** - exam registration, blueprints, and free official prep courses.
- Registration requires free membership in the **[📖 Claude Partner Network](https://claude.com/partners)** - sign-up is free and open.
- Exams are delivered by **[📖 Pearson VUE](https://www.pearsonvue.com/us/en/anthropic.html)** - choose online proctored or a test center; reschedule or cancel up to 24 hours before your appointment.
- On passing, you receive a digital badge via Credly by Pearson.

### Renewal and Retakes

- The credential is valid for 12 months.
- Renew on time for free via a non-proctored renewal assessment in Partner Academy. Miss the window and you sit the full exam again.
- Retake policy: 14-day wait after attempt 1, 30 days after attempt 2, 90 days after attempt 3. Maximum 4 attempts per rolling 12 months.

---

## Study Materials in This Guide

Each notes file maps to one or more exam domains:

| Notes File | Primary Domain(s) |
|---|---|
| [notes/01-advanced-claude-architectures.md](notes/01-advanced-claude-architectures.md) | 2 - Solution Design and Architecture |
| [notes/02-claude-agent-sdk-deep-dive.md](notes/02-claude-agent-sdk-deep-dive.md) | 1 - Integration; 7 - Developer Productivity and Operational Enablement |
| [notes/03-extended-thinking-and-context-management.md](notes/03-extended-thinking-and-context-management.md) | 6 - Claude Models, Prompting and Context Engineering |
| [notes/04-tool-use-and-mcp-integration.md](notes/04-tool-use-and-mcp-integration.md) | 1 - Integration |
| [notes/05-evaluation-and-observability.md](notes/05-evaluation-and-observability.md) | 3 - Evaluation, Testing and Optimization |
| [notes/06-cost-latency-optimization-at-scale.md](notes/06-cost-latency-optimization-at-scale.md) | 3 - Evaluation, Testing and Optimization; 2 - Solution Design |
| [notes/07-enterprise-deployment-bedrock-vertex.md](notes/07-enterprise-deployment-bedrock-vertex.md) | 2 - Solution Design and Architecture; 4 - Governance |
| [notes/08-governance-safety-and-risk-management.md](notes/08-governance-safety-and-risk-management.md) | 4 - Governance, Safety and Risk Management |
| [notes/09-stakeholder-communication-and-lifecycle-management.md](notes/09-stakeholder-communication-and-lifecycle-management.md) | 5 - Stakeholder Communication and Lifecycle Management |

Supporting files:

| File | Description |
|---|---|
| [fact-sheet.md](fact-sheet.md) | Quick-reference exam facts, domain weights, high-yield facts |
| [practice-plan.md](practice-plan.md) | 6-week study plan covering all 7 domains |
| [scenarios.md](scenarios.md) | Exam-style scenario questions with explanations |
| [strategy.md](strategy.md) | Exam-day tactics and time management |
| [Practice questions](../../../resources/practice-questions/anthropic-claude-architect-professional.md) | 15-question bank across all domains |

---

## Target Audience

You should already be comfortable with:

- Designing multi-agent and single-agent architectures under cost and latency SLOs
- Integrating Claude with retrieval systems at scale (vector, hybrid, reranked RAG)
- Building and operating MCP servers, tool pipelines, and streaming clients
- Running Claude behind Amazon Bedrock, Google Cloud Vertex AI, or the first-party Anthropic API
- Writing evaluations, tracking regressions, and managing model upgrades
- Reasoning about extended thinking budgets, prompt caching layers, batch economics, and context engineering
- Explaining all of the above to non-technical stakeholders and running a deployment lifecycle

If you are still learning the Messages API or the basics of MCP, start with [CCAR-F](../claude-certified-architect-foundations/) first.

---

## Official Resources

| Resource | URL |
|---|---|
| Partner Academy (registration + prep courses) | https://anthropic-partners.skilljar.com/page/partner-certifications |
| Claude Partner Network | https://claude.com/partners |
| Pearson VUE (Anthropic exams) | https://www.pearsonvue.com/us/en/anthropic.html |
| Anthropic Docs | https://docs.anthropic.com |
| Claude Agent SDK | https://docs.anthropic.com/en/api/agent-sdk/overview |
| Extended Thinking | https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking |
| Prompt Caching | https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching |
| Batch API | https://docs.anthropic.com/en/docs/build-with-claude/batch-processing |
| Files API | https://docs.anthropic.com/en/docs/build-with-claude/files |
| Tool Use | https://docs.anthropic.com/en/docs/build-with-claude/tool-use |
| Computer Use | https://docs.anthropic.com/en/docs/build-with-claude/computer-use |
| Memory Tool | https://docs.anthropic.com/en/docs/build-with-claude/tool-use/memory-tool |
| MCP Spec | https://modelcontextprotocol.io |
| Claude on Bedrock | https://docs.anthropic.com/en/api/claude-on-amazon-bedrock |
| Claude on Vertex | https://docs.anthropic.com/en/api/claude-on-vertex-ai |
| Anthropic Cookbook | https://github.com/anthropics/anthropic-cookbook |

---

## Study Approach

1. Anchor to primary sources. Treat docs.anthropic.com, the Anthropic Cookbook, and the MCP specification as ground truth. Take the free official prep courses in Partner Academy.
2. Build, do not just read. Reproduce the patterns Anthropic emphasizes in its engineering blog posts and cookbook recipes.
3. Track model versions. The exam differentiates Opus, Sonnet, and Haiku tradeoffs. Confirm current model IDs before exam day.
4. Understand the first-party API and the cloud deployments. Bedrock and Vertex quirks (model IDs, regional availability, IAM) matter at this tier.
5. Do not skip the non-coding domains. Governance (14%) and Stakeholder Communication (14%) together outweigh Integration. Engineers most often lose points there.

---

## Suggested Learning Progression

```
CCAR-F (Foundations)   →   CCAR-P (Professional)   (you are here)
```

Companion guides in this repo:

- [Claude Certified Developer - Foundations](../claude-certified-developer-foundations/) - production API/SDK depth
- [Prompt Engineering Specialist](../claude-prompt-engineering-specialist/) - prompt design and evaluation

The Professional material rewards engineers who have felt the pain of a 3am agent loop burning tokens - and fixed it.
