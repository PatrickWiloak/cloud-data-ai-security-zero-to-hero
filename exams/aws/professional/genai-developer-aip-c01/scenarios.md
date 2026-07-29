---
last-updated: 2026-07-29
---

# AWS Certified Generative AI Developer - Professional (AIP-C01) - Exam Scenarios

> Eight worked scenarios in AIP-C01 style. These are illustrative, written for this repo, not real exam questions. AIP-C01 scenarios are long: they establish the model, the data, a latency or cost budget, and a compliance constraint before asking anything. The clause that decides the answer is often a single phrase near the end.

## How to use this

1. Read the scenario and commit to an answer before reading the analysis.
2. For every option, say out loud why it is right or wrong. "Feels right" does not transfer to the exam.
3. The takeaway is the principle to carry into the next question of that shape.

---

## Scenario 1 - Retrieval quality, not model quality (Domain 1: 31%)

A legal team uses a Bedrock Knowledge Base over 40,000 contract PDFs to answer questions
about clause language. Answers are fluent but frequently cite the wrong contract, and
often truncate mid-clause. The team has already switched from Claude Haiku to Claude
Sonnet with no improvement. Latency and cost are acceptable. They need accurate citations.

Which change is most likely to fix this?

A. Switch to a larger foundation model and raise the temperature.
B. Reduce chunk size, add chunk overlap, and attach contract-ID metadata for filtering at query time.
C. Fine-tune the model on the contract corpus.
D. Increase the number of retrieved results from 5 to 50 and let the model sort it out.

**Answer: B.**

The symptom is a retrieval failure wearing a generation costume. Wrong-contract citations
mean the retriever is returning chunks from the wrong document, which metadata filtering
fixes directly. Truncated clauses mean chunks are splitting mid-clause, which smaller
chunks with overlap fix.

- **A** is wrong twice: model size does not fix retrieval, and raising temperature makes
  citation accuracy worse, not better.
- **C** is the classic distractor. Fine-tuning teaches style and format, not a
  frequently-changing document set, and it destroys citability.
- **D** floods the context window with mostly-irrelevant chunks. Precision drops and cost
  rises. More retrieval is not better retrieval.

**Takeaway:** when a RAG system is fluent but wrong, suspect chunking, embeddings, and
metadata before you touch the model.

---

## Scenario 2 - The fine-tuning decision (Domain 1: 31%)

A bank wants an assistant that replies in the bank's specific regulatory tone, using a
fixed disclosure format, over a product catalog that changes weekly. Prompt engineering
gets the format right about 70% of the time. Compliance requires the disclosure wording
to be exact every time.

What should the team implement?

A. Fine-tune on the product catalog so the model memorizes current products.
B. Fine-tune for tone and disclosure format, and use RAG for the product catalog.
C. Use RAG for both tone and catalog by retrieving example responses.
D. Put the entire catalog and a style guide in the system prompt on every call.

**Answer: B.**

This scenario deliberately contains both signals. Tone and a fixed output format are
stable behavioral properties, which is what fine-tuning is for. A weekly-changing
catalog is exactly what fine-tuning handles badly and RAG handles well. The correct
architecture uses each for what it is good at.

- **A** would require retraining every week and still would not guarantee format.
- **C** can nudge tone through few-shot examples but will not reach "exact every time."
- **D** is expensive on every call, and long system prompts degrade instruction-following.

**Takeaway:** RAG and fine-tuning are not competitors. Stable behavior, fine-tune.
Changing knowledge, retrieve.

---

## Scenario 3 - Blocking a model, not blocking content (Domain 3: 20%)

A platform team hosts a shared Bedrock account. The data science team may call any model.
The customer-support team must be prevented from invoking any Anthropic model above
Haiku, for cost reasons. An engineer proposes configuring Bedrock Guardrails.

Is that correct, and what should be done?

A. Yes, configure a Guardrail denying the other models.
B. No. Use an IAM identity-based policy that denies `bedrock:InvokeModel` on the specific model ARNs for that team's role.
C. No. Use a Guardrail with a denied-topics policy covering expensive requests.
D. Yes, and additionally enable model invocation logging.

**Answer: B.**

Guardrails filter *what is said*, in either direction: content categories, denied topics,
PII, word filters. They have no concept of which principal is calling. Restricting who may
invoke which model is an authorization question, so it belongs in IAM, scoped to the model
ARN.

- **A** and **D** both misuse Guardrails for access control. Logging is good practice but
  is detective, not preventive.
- **C** confuses topic filtering with model selection entirely.

**Takeaway:** Guardrails govern content. IAM governs access. Exam questions that describe
a *team* or *role* being restricted are IAM questions.

---

## Scenario 4 - Provisioned Throughput or not (Domain 4: 12%)

A retailer runs a product-description generator. Traffic is bursty: near zero most of the
week, then roughly 40,000 requests over six hours every Monday during catalog refresh.
Finance wants the lowest total cost. Latency during the burst may degrade gracefully.

Which approach is most cost-effective?

A. Purchase Provisioned Throughput sized for the Monday peak.
B. Use On-Demand invocation, and use batch inference for the Monday catalog refresh.
C. Purchase Provisioned Throughput sized for average weekly volume.
D. Provision a SageMaker real-time endpoint with autoscaling.

**Answer: B.**

Provisioned Throughput bills for committed capacity whether or not you use it, so buying
for a six-hour weekly peak means paying for idle capacity the other 162 hours. The
workload is also asynchronous by nature: catalog descriptions do not need interactive
latency, which is precisely what batch inference is for and it is cheaper per token.

- **A** is the trap for people who pattern-match "high volume" to Provisioned Throughput
  without checking the duty cycle.
- **C** would throttle badly during the burst while still paying continuously.
- **D** adds infrastructure management for a workload with no real-time requirement.

**Takeaway:** Provisioned Throughput needs *sustained* predictable volume. Bursty plus
latency-tolerant equals batch.

---

## Scenario 5 - An agent calling the wrong tool (Domain 2: 26%)

A Bedrock Agent has three action groups: `checkOrderStatus`, `cancelOrder`, and
`checkRefundStatus`. Users asking "where is my refund?" are routed to `checkOrderStatus`
about a third of the time. The model is Claude Sonnet. The orchestration prompt is the
default.

What is the most effective fix?

A. Upgrade to a larger model.
B. Sharpen the action group descriptions and parameter descriptions so the refund and order paths are unambiguous.
C. Merge the three action groups into one and branch inside the Lambda.
D. Lower the temperature to 0.

**Answer: B.**

Tool selection is driven by the descriptions the model sees. Two tools whose descriptions
both mention "status" and "order" are genuinely ambiguous, and the model is behaving
reasonably given bad inputs. Rewriting the descriptions to state exactly when each applies
is the direct fix, and costs nothing.

- **A** may reduce the error rate slightly while leaving the ambiguity in place, at higher
  cost per call.
- **C** hides the routing problem inside Lambda and gives up the agent's ability to reason
  about which capability is needed.
- **D** makes selection more deterministic but equally likely to deterministically pick
  the wrong one.

**Takeaway:** agent misrouting is almost always a schema and description problem. Fix the
contract before you change the model.

---

## Scenario 6 - PII on the way in and out (Domain 3: 20%)

A healthcare provider sends clinician notes to a foundation model for summarization. Legal
requires that patient identifiers never reach the model, and that any identifier the model
happens to emit is blocked before reaching the user. Engineering wants minimal custom code.

Which design meets both requirements?

A. A Bedrock Guardrail with PII entity filters configured on both input and output.
B. A Lambda pre-processor using Amazon Comprehend PII detection before invocation.
C. A Guardrail on output only, since the input is trusted internal data.
D. Post-process the response with a regex library for common identifier formats.

**Answer: A.**

Guardrails apply to both the prompt and the completion, which is exactly the two-sided
requirement here, and it is configuration rather than custom code.

- **B** covers only the input half and adds a service and code path to maintain.
- **C** misreads the requirement: legal explicitly said identifiers must not reach the
  model, so input filtering is mandatory.
- **D** is brittle. Regex will miss names and unusual formats, and this is regulated data.

**Takeaway:** when a requirement is stated on both directions of the call, look for the
control that applies to both. Guardrails do.

---

## Scenario 7 - Proving a change helped (Domain 5: 11%)

A team changed its chunking strategy and believes retrieval improved. Their evidence is
that "the three questions we tried look better." Leadership wants defensible evidence
before rolling out to production.

What should the team do?

A. Roll out to 5% of traffic and watch user complaints.
B. Build a held-out evaluation set of representative questions with known-correct source passages, and measure retrieval and answer quality before and after, using LLM-as-a-judge with human spot checks.
C. Ask a larger model whether the new answers are better.
D. Measure average response latency and token cost before and after.

**Answer: B.**

The question asks for defensible evidence of a *quality* change, which requires a fixed
evaluation set and a defined metric so the two configurations are compared on identical
inputs. Judging with a model is acceptable at scale provided humans spot-check the judge.

- **A** is a slow, noisy signal, and ships an unvalidated change to real users first.
- **C** is B without the rigor: no fixed dataset, no ground truth, no human check.
- **D** measures the wrong dimension entirely.

**Takeaway:** evaluation questions want a held-out dataset plus a stated metric. Anecdotes
and latency numbers are not quality evidence.

---

## Scenario 8 - Latency budget forces the architecture (Domain 4: 12%)

A customer-facing chat feature has a hard 2-second p95 budget for first token. The current
design retrieves from a knowledge base, calls a large model, then runs an output Guardrail.
p95 is 4.5 seconds. Answer quality is currently good and must not materially regress.

Which combination best meets the budget?

A. Remove the Guardrail and reduce retrieved chunks to 1.
B. Stream the response, use a smaller model for this path, and cache embeddings and frequent queries.
C. Move to batch inference.
D. Increase Provisioned Throughput.

**Answer: B.**

First-token latency is helped most by streaming, because the user sees output while
generation continues. A smaller model reduces both time-to-first-token and cost, and
caching removes repeated embedding and retrieval work for common questions. Together these
address the budget without gutting quality.

- **A** meets the budget by removing a compliance control and crippling retrieval. Never
  the right trade on a customer-facing path.
- **C** is incompatible with an interactive feature.
- **D** addresses throughput, not per-request latency. Capacity was not the bottleneck.

**Takeaway:** distinguish throughput from latency. Provisioned Throughput fixes "we cannot
serve enough requests," not "each request is too slow."

---

## Patterns worth memorizing

| Symptom in the scenario | Usual answer |
|---|---|
| Fluent but factually wrong or miscited | Retrieval: chunking, embeddings, metadata filters |
| Needs consistent tone or exact format | Fine-tuning |
| Knowledge changes frequently, needs citations | RAG |
| A team or role must be restricted | IAM, not Guardrails |
| Content must be filtered in or out | Guardrails, both directions |
| Sustained predictable high volume | Provisioned Throughput |
| Bursty and latency-tolerant | Batch inference |
| Interactive latency budget | Streaming, smaller model, caching |
| Agent picks the wrong tool | Action group and parameter descriptions |
| "How do we know it improved?" | Held-out eval set with a defined metric |
