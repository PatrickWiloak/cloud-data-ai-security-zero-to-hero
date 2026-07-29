---
last-updated: 2026-07-29
---

# AWS Certified Generative AI Developer - Professional (AIP-C01) - Practice Plan

An 8-week plan assuming 6-8 hours a week. Compress to 5 weeks if you already build
production GenAI applications on Bedrock daily; stretch to 12 if Bedrock is new to you.

This is a Professional-tier exam. It assumes you can already write application code, call
APIs, and reason about IAM. If those are shaky, spend two weeks on
[AWS Certified AI Practitioner](../../foundational/ai-practitioner-aif-c01/) first, which
is background rather than a prerequisite.

**Prerequisites worth having**

- Comfortable with Python and the AWS SDK
- Working IAM knowledge: identity vs resource policies, least privilege
- Some exposure to vector search concepts (see [embeddings and vector search](../../../../learn/concepts/embeddings-and-vector-search.md))

---

## Week 1 - Foundation models and the Bedrock surface

Goal: know what the platform offers before deciding how to use it.

- [ ] Read [fact-sheet.md](fact-sheet.md) end to end. Note the domain weights.
- [ ] Read [notes/01-foundation-models-data-compliance.md](notes/01-foundation-models-data-compliance.md)
- [ ] Read [notes/bedrock-platform-deep-dive.md](notes/bedrock-platform-deep-dive.md), the single most-tested service surface
- [ ] Hands-on: invoke three different foundation models on the same prompt via the Bedrock API. Compare output, latency, and cost per 1K tokens
- [ ] Write down, in your own words, when you would pick each model family

**Checkpoint:** you can explain model selection in terms of capability, latency, and cost
without looking anything up.

---

## Week 2 - Prompt engineering and management

- [ ] Read [notes/prompt-engineering-and-management.md](notes/prompt-engineering-and-management.md)
- [ ] Read the concept page on [prompt engineering](../../../../learn/concepts/prompt-engineering.md)
- [ ] Hands-on: take a task that fails with a naive prompt and fix it with structure, few-shot examples, and explicit output format
- [ ] Hands-on: version two prompts and compare them on the same 10 inputs
- [ ] Note where prompt engineering stops being enough. That boundary is tested

**Checkpoint:** you can articulate the prompt engineering / RAG / fine-tuning decision and
name the constraint that selects each.

---

## Week 3 - RAG architecture, part 1

The largest single topic on the exam.

- [ ] Read [notes/rag-architecture-deep-dive.md](notes/rag-architecture-deep-dive.md)
- [ ] Read [rag-explained](../../../../learn/concepts/rag-explained.md) and [fine-tuning vs RAG](../../../../learn/concepts/fine-tuning-vs-rag.md)
- [ ] Hands-on: build a Knowledge Base over a document set you know well
- [ ] Deliberately break it: oversized chunks, no overlap, no metadata. Observe how the failure *looks* from the answer side

**Checkpoint:** given a bad answer, you can tell whether the fault is retrieval or
generation.

---

## Week 4 - RAG architecture, part 2, and data management

- [ ] Compare vector store options and their trade-offs. See [vector database comparison](../../../../resources/service-comparison-vector-databases.md) and [the decision matrix](../../../../resources/decision-matrix-vector-database.md)
- [ ] Hands-on: add metadata filtering and measure the precision improvement on 10 questions
- [ ] Study data handling: where prompts and completions are stored and logged, and what that means for regulated data
- [ ] Re-read the compliance half of [notes/01-foundation-models-data-compliance.md](notes/01-foundation-models-data-compliance.md)

**Checkpoint:** you can design a RAG pipeline for a regulated workload and justify each
component.

---

## Week 5 - Implementation, integration, and agents

- [ ] Read [notes/02-implementation-integration.md](notes/02-implementation-integration.md)
- [ ] Read [notes/agentic-ai-systems.md](notes/agentic-ai-systems.md)
- [ ] Read the concept pages on [tool use](../../../../learn/concepts/tool-use-and-function-calling.md) and [agentic loops](../../../../learn/concepts/agentic-loops.md)
- [ ] Hands-on: build an agent with two action groups whose purposes are genuinely close. Watch it misroute, then fix it purely by rewriting descriptions
- [ ] Hands-on: add a third action group that calls an external API

**Checkpoint:** you can debug tool selection without reaching for a bigger model.

---

## Week 6 - Safety, security, and governance

- [ ] Read [notes/03-ai-safety-security-governance.md](notes/03-ai-safety-security-governance.md)
- [ ] Read [guardrails and safety](../../../../learn/concepts/guardrails-and-safety.md)
- [ ] Hands-on: configure a Guardrail with PII filters on both input and output, and confirm both directions actually block
- [ ] Hands-on: write an IAM policy that permits one model and denies another for a specific role. Test it
- [ ] Practise stating the difference between a Guardrail control and an IAM control in one sentence

**Checkpoint:** you never confuse content filtering with access control. This is worth
several marks.

---

## Week 7 - Optimisation, testing, and validation

- [ ] Read [notes/04-operational-efficiency-optimization.md](notes/04-operational-efficiency-optimization.md)
- [ ] Read [notes/05-testing-validation-troubleshooting.md](notes/05-testing-validation-troubleshooting.md)
- [ ] Read [evals for LLMs](../../../../learn/concepts/evals-for-llms.md) and [prompt caching](../../../../learn/concepts/prompt-caching.md)
- [ ] Hands-on: build a small evaluation set (20 questions with known-good sources) and score two configurations against it
- [ ] Work through the cost model: On-Demand vs Provisioned Throughput vs batch, for three different duty cycles
- [ ] Hands-on: measure the latency difference streaming makes to time-to-first-token

**Checkpoint:** you can decide On-Demand / Provisioned / batch from a described duty cycle,
and you can describe a defensible evaluation.

---

## Week 8 - Consolidation and exam readiness

- [ ] Work all of [scenarios.md](scenarios.md). For each, write why every distractor fails
- [ ] Read [strategy.md](strategy.md) and internalise the trap list
- [ ] Skim [notes/aws-services-mapping.md](notes/aws-services-mapping.md) as a reverse index: capability to service
- [ ] Re-read [notes/bedrock-platform-deep-dive.md](notes/bedrock-platform-deep-dive.md) and [notes/rag-architecture-deep-dive.md](notes/rag-architecture-deep-dive.md)
- [ ] Take a timed practice run. Hold to 2.4 minutes per question
- [ ] Review every miss and classify it: knowledge gap, misread, or timing

**Do not** start new material in the final three days. Consolidate.

---

## Ongoing habits

- Keep a running list of every question you get wrong and the *reason*. Patterns show up fast.
- Any time you read "least operational overhead" or "most cost-effective," stop and note which one it is. The exam turns on that distinction constantly.
- Build things. This exam rewards people who have actually shipped a RAG pipeline and debugged an agent over people who have only read about them.

## Related material in this repo

- [Build a RAG pipeline](../../../../resources/hands-on-projects/build-rag-pipeline.md)
- [Set up an eval harness](../../../../resources/hands-on-projects/set-up-eval-harness.md)
- [Build a Claude agent with MCP](../../../../resources/hands-on-projects/build-claude-agent-with-mcp.md)
- [AI/ML pipeline architecture pattern](../../../../resources/architecture-patterns/ai-ml-pipeline.md)
- [GenAI platform comparison](../../../../resources/service-comparison-genai-platforms.md)
