---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 8 min
---

# OCI Generative AI Professional Scenarios

---

## Scenario 1: Choosing the customization approach

**Scenario**: An insurer wants an assistant that answers questions about its policy documents. The documents are updated monthly, answers must cite the source clause, and the team has no ML engineers.

**Solution Pattern**:
- **RAG**, not fine-tuning
- Monthly updates make fine-tuning wrong on its own: fine-tuned knowledge is frozen at training time, so every update would require retraining
- Citation requires knowing which source text produced the answer, which RAG provides and fine-tuning cannot
- No ML engineers points away from a training pipeline
- Implementation: chunk the policy documents, embed them, store in **AI Vector Search** or another vector store, retrieve on each question, and instruct the model to answer only from the retrieved clauses and cite them

**Common Distractors**:
- Fine-tuning on the policy corpus (frozen knowledge, no citations, retraining every month)
- Putting all documents in the prompt (exceeds the context window and costs enormously)
- Pre-training a model (never the answer at this scale)

**Key Takeaway**: Changing knowledge, plus a citation requirement, is definitive for RAG. Fine-tuning is for behavior, not for facts that change.

---

## Scenario 2: On-demand or dedicated cluster

**Scenario**: A team has fine-tuned a model on their support ticket history to match their house tone. They now want to serve it to a production application with steady traffic and a latency commitment.

**Solution Pattern**:
- A **dedicated AI cluster** is **required**, not optional. Custom fine-tuned models can only be hosted on a dedicated cluster; on-demand inference serves base models only
- Fine-tuning itself also required a cluster
- Size the cluster by required throughput; dedicated capacity is what makes a latency commitment possible
- Hosting and fine-tuning clusters are distinct, so plan for both if retraining is ongoing
- Billing is by reserved cluster unit hours rather than per request, so it is only economical above a certain steady volume

**Common Distractors**:
- On-demand inference (cannot serve a custom model at all)
- A larger base model with better prompting (a reasonable alternative design, but it does not answer how to serve the model they already fine-tuned)
- Deploying through OCI Data Science (possible for a self-managed model, but not how OCI Generative AI custom models are served)

**Key Takeaway**: Fine-tuning and custom model hosting both require a dedicated AI cluster. This is a hard constraint and a reliable exam question.

---

## Scenario 3: Answers are wrong even though the data exists

**Scenario**: A RAG chatbot over technical documentation gives confidently wrong answers. The information is definitely in the corpus. The team increased the number of retrieved chunks from 3 to 20 and it got worse.

**Solution Pattern**:
- Diagnose in order. **Log the retrieved chunks** and check whether the correct one is present at all
- If it is **not retrieved**, the problem is retrieval: chunk size may be too large (imprecise embeddings) or too small (missing context), the embedding model may be a poor fit for technical vocabulary, or the query wording may differ from the document wording. Hybrid search combining keyword and semantic matching often fixes the last case
- If it **is retrieved but ignored**, retrieving 20 chunks is likely the cause: the relevant chunk is buried, and models attend less to the middle of a long context. Reduce the count and consider reranking so the best chunk appears first
- Strengthen the prompt: instruct the model to answer only from the context and to say when the context lacks the answer
- Require citations so wrong answers are detectable

**Common Distractors**:
- Increasing chunk count further (the change that already made it worse)
- Raising temperature (increases variety, not correctness)
- Fine-tuning the model (the data exists; this is a retrieval problem)

**Key Takeaway**: Poor RAG answers are usually retrieval failures. More retrieved chunks is often worse, not better. Log the retrieved context before changing anything else.

---

## Scenario 4: Reproducible output

**Scenario**: A team uses an LLM to extract structured fields from contracts. Running the same document twice produces slightly different values, which breaks their downstream reconciliation.

**Solution Pattern**:
- Set **temperature to 0** for near-deterministic decoding
- Avoid top-p and top-k sampling settings that reintroduce randomness
- Use **structured output** or a strict schema and validate the response, rejecting anything that does not conform
- Add **stop sequences** so generation terminates predictably
- Note the honest caveat: even at temperature 0, output is not guaranteed identical across model versions or infrastructure, so validation belongs in the pipeline regardless

**Common Distractors**:
- Lowering top-k only (helps, but temperature is the primary control)
- Fine-tuning for consistency (expensive answer to a decoding parameter problem)
- Retrying until two runs agree (masks the issue and doubles the cost)

**Key Takeaway**: Temperature 0 is the first answer for determinism, with schema validation as the safety net. Extraction tasks should never run at a high temperature.

---

## Scenario 5: Cost control

**Scenario**: A customer support assistant's inference bill has tripled. Investigation shows every request includes the full conversation history plus 15 retrieved chunks, and the system prompt is 2,000 tokens.

**Solution Pattern**:
- **Reduce retrieved chunks** from 15 to a smaller number, which usually improves quality as well as cost
- **Trim conversation memory**: summarize older turns rather than resending them verbatim, or use a windowed memory that keeps only recent turns
- **Shorten the system prompt**, moving reference material into retrieval rather than sending it on every request
- **Cap max tokens** on the response
- Consider a **smaller model** for classification or routing steps, reserving the larger model for generation
- Measure tokens per request as an ongoing metric rather than discovering the problem in the bill

**Common Distractors**:
- Moving to a dedicated cluster (predictable cost, not necessarily lower, and only economical above a steady volume)
- Caching whole responses (helps for repeated identical questions, which is rarely the bulk of support traffic)
- Reducing traffic (not a technical answer)

**Key Takeaway**: LLM cost is driven by tokens in and out. The largest levers are retrieved context size, conversation history handling, and system prompt length, in that order.

---

## Scenario 6: Multi-tenant retrieval

**Scenario**: A SaaS company builds one assistant serving many customer organizations, each with its own documents in a shared vector store. During testing, a user from one organization receives an answer containing another organization's content.

**Solution Pattern**:
- **Filter by tenant in the vector query**, not after retrieval. Every chunk must carry a tenant identifier in its metadata, and every query must constrain on it
- Better still, use **separate namespaces, collections, or indexes** per tenant so cross-tenant retrieval is structurally impossible
- Enforce authorization on the **end user's identity**, resolved server-side from the session, not from anything the model or the request body supplies
- Treat the vector store as a primary datastore for classification purposes: encrypt, restrict network access, and audit reads. Embeddings are not anonymized, and source text can be substantially reconstructed from them
- Add a test for this case to the evaluation suite so it cannot regress

**Common Distractors**:
- Instructing the model in the system prompt not to reveal other tenants' data (a prompt is not an access control)
- Post-filtering results after the model has seen them (the data already entered the context)
- Separate models per tenant (enormously expensive, and it does not address the retrieval boundary)

**Key Takeaway**: Multi-tenant retrieval must be enforced in the query, on the end user's identity. This is the most common serious security defect in production RAG systems, and it is a retrieval authorization bug rather than a model problem.

---

## Related

- [Practice plan](./practice-plan.md)
- [Strategy](./strategy.md)
- [Notes](./notes/)
- [AI security](../../../resources/ai-security/) - the engineering-depth treatment of scenario 6
- [Practice questions](../../../resources/practice-questions/oracle-oci-generative-ai-professional.md)
