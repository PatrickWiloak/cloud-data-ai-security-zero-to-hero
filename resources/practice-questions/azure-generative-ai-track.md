---
last-updated: 2026-08-09
difficulty: intermediate
---

# Azure Generative AI (Self-Directed Track) - Practice Questions

15 questions for the Azure Generative AI study track, weighted toward Azure OpenAI fundamentals (25-30%), prompt engineering (20-25%), and AI Foundry deployment (20-25%), with responsible AI and production integration.

This is a self-directed track rather than a Microsoft exam, so these questions target working knowledge rather than a published objective list.

> **Cert page:** [exams/azure/genai/](../../exams/azure/genai/)

---

### Question 1
**Scenario:** A deployment must guarantee throughput for a latency-sensitive production application.

A. Standard (pay-as-you-go) deployment
B. Provisioned throughput units (PTU)
C. Batch deployment
D. A larger model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** PTU reserves capacity so throughput and latency are predictable rather than shared. Standard deployments are cheaper and elastic but subject to variable latency and 429 responses under load. Batch is the opposite trade: much cheaper, with results delivered asynchronously.
</details>

---

### Question 2
**Scenario:** An application must answer questions from a company's internal documents.

A. Fine-tune the model on the documents
B. Retrieval-augmented generation: index the documents and pass relevant chunks as context
C. Put every document in the system prompt
D. Train a model from scratch

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RAG is the default for factual grounding because content updates without retraining, sources can be cited, and access control can be enforced at retrieval time. Fine-tuning teaches style and format far better than it teaches facts. Stuffing everything into the prompt hits context limits and costs.
</details>

---

### Question 3
**Scenario:** Retrieval quality is poor: relevant passages exist but are not returned.

A. Increase the model's temperature
B. Improve chunking and try hybrid search (keyword plus vector) with semantic reranking
C. Use a larger model
D. Lower the top-k

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Retrieval failures are retrieval problems, not generation problems. Chunk boundaries that split a fact across two chunks, pure vector search missing exact identifiers, and no reranking are the three usual causes. Changing the model cannot recover context it was never given.
</details>

---

### Question 4
**Scenario:** Which parameter makes output more deterministic?

A. Raising temperature
B. Lowering temperature toward 0
C. Raising top_p to 1
D. Increasing max_tokens

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Temperature scales the randomness of token sampling, so near zero is close to greedy decoding. Note that even at temperature 0 output is not strictly guaranteed identical across runs. Adjust temperature or top_p, not both at once, or the interaction becomes hard to reason about.
</details>

---

### Question 5
**Scenario:** An app must return JSON that always matches a defined schema.

A. Ask nicely in the prompt
B. Use structured outputs or JSON mode with a schema, and validate the result before use
C. Parse with a regular expression
D. Lower temperature only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Constrained decoding against a schema removes the class of failures where the model emits prose around the JSON or drops a field. Validation after the fact is still worth keeping, because a schema-valid response can still be semantically wrong.
</details>

---

### Question 6
**Scenario:** Content filtering must be adjusted for a medical application where clinical terms trigger false positives.

A. Disable all filtering
B. Configure content filter severity thresholds per category, and apply for modified filters where the use case justifies it
C. Rewrite the prompts to avoid clinical terms
D. Switch cloud providers

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Azure OpenAI content filters have per-category severity thresholds for hate, sexual, violence, and self-harm, applied to both prompt and completion. Legitimate use cases can request modified configurations through Microsoft's approval process. Avoiding clinical vocabulary would break the application's purpose.
</details>

---

### Question 7
**Scenario:** A retrieval system must not return documents the asking user cannot see.

A. Filter results by the user's identity and group membership at query time, using security trimming on the index
B. Rely on the model to decline
C. Index only public documents
D. Add a system prompt instruction

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Authorization must be enforced in the retrieval layer, in code, before content reaches the context window. A system prompt instruction is a suggestion an injected instruction can compete with, and the model has no reliable way to know who is asking.
</details>

---

### Question 8
**Scenario:** Costs are dominated by a long, unchanging system prompt repeated on every request.

A. Shorten the prompt until quality drops
B. Use prompt caching so the repeated prefix is billed and processed at a reduced rate
C. Use a smaller model only
D. Batch the requests

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Caching a stable prefix is the direct fix and requires the shared content to be at the start of the prompt, which is a real design constraint worth planning for. Batch processing helps for offline workloads but not for interactive latency.
</details>

---

### Question 9
**Scenario:** Which technique gives the model examples of the desired input and output format inside the prompt?

A. Zero-shot prompting
B. Few-shot prompting
C. Fine-tuning
D. Chain of thought

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Few-shot means including exemplars in the prompt, which is the cheapest way to pin down format and edge-case handling. Chain of thought asks the model to reason step by step, which is about the process rather than the format. Fine-tuning moves examples into the weights.
</details>

---

### Question 10
**Scenario:** An agent has a tool that can delete records. What is the minimum responsible design?

A. Trust the model's judgment
B. Scope the tool's credential narrowly, check authorization against the calling user in code, require confirmation for destructive actions, and log every call
C. Add a warning in the system prompt
D. Use a smaller model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The tool boundary is the last non-model control that can refuse, so it must carry the authorization check rather than delegating it to the prompt. Treat the model as an untrusted caller: assume an injected instruction will eventually reach it and design so that the worst outcome is bounded.
</details>

---

### Question 11
**Scenario:** A model deployment must be evaluated before and after a version upgrade.

A. Manual spot checks
B. An evaluation set with defined metrics (groundedness, relevance, fluency, and task-specific accuracy) run against both versions
C. User complaints
D. Latency measurement only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A model upgrade is a behavior change, and without a regression suite you find out from users. Azure AI Foundry evaluation supports both AI-assisted and code-based metrics, and safety evaluations belong in the same suite as quality ones.
</details>

---

### Question 12
**Scenario:** Which Azure service provides the managed development surface for building, evaluating, and deploying generative AI applications?

A. Azure Machine Learning only
B. Azure AI Foundry, with model catalog, prompt flow, evaluation, and deployment
C. Azure Data Factory
D. Azure Functions

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** AI Foundry is the generative AI development hub, including the model catalog across Azure OpenAI and open models, prompt flow for orchestration, evaluations, content safety, and tracing. Azure Machine Learning remains the broader ML platform underneath.
</details>

---

### Question 13
**Scenario:** An embedding model is swapped for a newer one in a live RAG system.

A. Nothing else is needed
B. The entire index must be re-embedded, because vectors from different models are not comparable
C. Only new documents need re-embedding
D. Increase the index size

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Embedding spaces are model-specific, so mixing vectors from two models produces meaningless similarity scores. Plan the reindex, and keep the old index serving until the new one is validated, which is the usual blue-green pattern applied to retrieval.
</details>

---

### Question 14
**Scenario:** Which Microsoft framework should guide the responsible AI review of a new generative feature?

A. The Microsoft Responsible AI Standard, with fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability
B. The Azure Well-Architected Framework alone
C. The Cloud Adoption Framework alone
D. ISO 27001 alone

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Responsible AI Standard names the six principles and requires an impact assessment for the use case. The Well-Architected and Cloud Adoption frameworks are complementary but cover architecture and adoption rather than AI-specific harms, and ISO 27001 is information security management.
</details>

---

### Question 15
**Scenario:** Production monitoring must catch quality degradation over time.

A. Log prompts, completions, latency, token usage, and evaluation scores on sampled traffic, with alerts on drift in those scores
B. Monitor CPU only
C. Wait for support tickets
D. Re-run the launch evaluation once a year

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Generative systems degrade silently as inputs, content, and model versions shift, and infrastructure metrics show nothing. Sampled online evaluation with the same metrics used pre-launch is what turns a quality regression into an alert instead of a complaint.
</details>

---

## Where to go deeper

- [Azure GenAI track page](../../exams/azure/genai/) - notes, practice plan, strategy
- [AI-102 practice questions](./azure-ai-engineer-ai-102.md) - the certification nearest this track
- [Prompt injection defense](../ai-security/prompt-injection-defense.md) - the security side of question 10
- [RAG explained](../../learn/concepts/rag-explained.md) - retrieval in plain English
- **[📖 Azure OpenAI documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)** - primary source
