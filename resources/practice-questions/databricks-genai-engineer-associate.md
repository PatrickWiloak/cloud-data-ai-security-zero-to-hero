---
last-updated: 2026-08-09
difficulty: intermediate
---

# Databricks Certified Generative AI Engineer Associate - Practice Questions

15 questions for this exam, weighted toward RAG application design (30%) and implementation (30%), then governance and evaluation (20%) and LLM fundamentals (20%).

> **Cert page:** [exams/databricks/genai-engineer-associate/](../../exams/databricks/genai-engineer-associate/)

---

### Question 1
**Scenario:** A RAG application must answer questions from internal policy documents.

A. Fine-tune a model on the documents
B. Chunk and embed the documents into a Vector Search index, retrieve relevant chunks at query time, and generate an answer from them
C. Put all documents in the prompt
D. Train a model from scratch

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RAG separates knowledge from the model, so updating a policy means reindexing rather than retraining, and the retrieved chunk can be cited. Fine-tuning teaches behavior far better than it teaches facts, and full-document prompting hits context and cost limits quickly.
</details>

---

### Question 2
**Scenario:** A Delta table of documents must stay in sync with a vector index.

A. Rebuild the index nightly by hand
B. A Databricks Vector Search Delta Sync index, which keeps the index updated as the source table changes
C. Export to CSV
D. Manual upserts

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Delta Sync indexes track the source table and update automatically, which removes the class of bugs where the index silently falls behind the data. Direct Vector Access indexes are the alternative when you manage embeddings and writes yourself.
</details>

---

### Question 3
**Scenario:** Chunk size must be chosen for a corpus of long technical manuals.

A. One chunk per document
B. Chunks sized to hold a complete idea with some overlap, ideally split on document structure such as sections rather than fixed character counts
C. One sentence per chunk
D. Chunk size does not matter

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Whole documents dilute the embedding so retrieval returns everything weakly; single sentences lose the context needed to answer. Structure-aware splitting with overlap keeps facts intact across boundaries, and it is the highest-leverage tuning knob in most RAG systems.
</details>

---

### Question 4
**Scenario:** Retrieval misses documents when the user's query uses different wording from the source.

A. Keyword search only
B. Vector (semantic) search, optionally hybrid with keyword search for exact identifiers
C. Increase temperature
D. A bigger model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Embeddings capture meaning rather than surface form, which is why a paraphrased query still retrieves. Hybrid search adds back the exact-match strength that dense retrieval lacks for error codes, part numbers, and rare proper nouns.
</details>

---

### Question 5
**Scenario:** A model endpoint must serve an external foundation model and a fine-tuned model behind one interface.

A. Two applications
B. Mosaic AI Model Serving with external model endpoints and custom model endpoints, optionally behind an AI Gateway
C. A load balancer
D. Manual routing

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Model Serving fronts foundation model APIs, external providers, and your own registered models with one interface, and the gateway layer adds rate limiting, usage tracking, and credential management. That means switching providers does not mean rewriting the application.
</details>

---

### Question 6
**Scenario:** A chain of retrieval, prompt, and model must be tracked and versioned.

A. A notebook only
B. Log the chain as an MLflow model, register it in Unity Catalog, and deploy the registered version
C. Copy the code to production
D. A text file

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Logging the whole chain rather than just the model makes the deployed artifact reproducible, including the prompt template and retrieval configuration. Registering in Unity Catalog gives it the same governance, lineage, and access control as data.
</details>

---

### Question 7
**Scenario:** The application must be evaluated for answer quality against ground truth.

A. Spot checks
B. An evaluation set with metrics such as answer correctness, groundedness, and retrieval recall, run automatically on each change
C. User complaints
D. Latency only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Separating retrieval metrics from generation metrics matters because they fail for different reasons. Mosaic AI Agent Evaluation supports LLM-judge metrics alongside human review, and running it on every prompt or model change is what catches silent regressions.
</details>

---

### Question 8
**Scenario:** Retrieval must respect who is asking, so users only see permitted documents.

A. Instruct the model to refuse
B. Filter at retrieval time by metadata reflecting the user's entitlements, enforced in code
C. Post-process the answer
D. Rely on the model's training

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Once content is in the context window it can appear in the output, so authorization must happen before retrieval returns. A prompt instruction is advisory and can be overridden by injected text in a retrieved document.
</details>

---

### Question 9
**Scenario:** Model responses must be traced for debugging and audit.

A. Print statements
B. MLflow Tracing capturing spans for retrieval, prompt construction, and generation, plus inference tables logging requests and responses
C. No logging
D. Only errors

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A wrong answer is usually a retrieval problem, and you cannot tell without seeing which chunks were retrieved. Tracing makes each step inspectable, and inference tables put production traffic into a Delta table you can query and build evaluation sets from.
</details>

---

### Question 10
**Scenario:** An agent must call tools to complete a task.

A. The model executes tools itself
B. The model emits a structured tool call, your code executes it with a scoped credential and an authorization check, and the result returns to the model
C. Give the agent admin access
D. Skip authorization

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The execution step is where security lives, because the model is an untrusted planner that a retrieved document may have influenced. Unity Catalog functions as tools help here by carrying their own governance and grants.
</details>

---

### Question 11
**Scenario:** An embedding model is upgraded.

A. No further action
B. Re-embed the entire index, because vectors from different models are not comparable
C. Re-embed new documents only
D. Increase the index size

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Mixing embedding spaces produces meaningless similarity scores, so a partial reindex is worse than no upgrade. Build the new index alongside the old one and cut over after validating, which is blue-green applied to retrieval.
</details>

---

### Question 12
**Scenario:** Unsafe or off-topic outputs must be constrained.

A. Prompt instructions alone
B. Layered guardrails: input and output classification, topic constraints in the gateway, and measurement of both violation rate and false refusal rate
C. Reduce the max tokens
D. Lower temperature

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Safety is a trade-off curve rather than a switch, so measuring false refusals matters as much as measuring violations: an over-blocking assistant is also a failed product. Prompt instructions are the weakest layer because injected content competes with them.
</details>

---

### Question 13
**Scenario:** Costs rise sharply as usage grows.

A. Accept it
B. Measure tokens per request, use a smaller model for simple steps, cache repeated prefixes, and cap retrieved context size
C. Increase the model size
D. Add more endpoints

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cost is driven by tokens in and out, and retrieved context is often the largest and least examined contributor. Trimming top-k after measuring the effect on quality frequently reduces cost without any measurable loss.
</details>

---

### Question 14
**Scenario:** Which describes the difference between prompt engineering, RAG, and fine-tuning?

A. They are interchangeable
B. Prompt engineering shapes behavior with instructions and examples, RAG supplies external knowledge at query time, and fine-tuning adjusts weights for consistent task behavior
C. Fine-tuning is always best
D. RAG replaces the model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** They address different needs and cost increases in that order. Most production systems combine them: a tuned prompt, retrieval for facts, and optionally fine-tuning for format consistency the prompt could not reliably enforce.
</details>

---

### Question 15
**Scenario:** A model serving endpoint must scale down when idle.

A. A fixed provisioned endpoint
B. Scale-to-zero on the serving endpoint, accepting cold start latency on the first request after idle
C. Delete the endpoint each night
D. A larger instance

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Scale-to-zero suits development and intermittent internal tools where a few seconds of cold start is acceptable. Interactive user-facing applications usually keep a warm minimum, so the choice follows the latency requirement rather than the cost target alone.
</details>

---

## Where to go deeper

- [GenAI Engineer Associate cert page](../../exams/databricks/genai-engineer-associate/) - notes, practice plan, strategy
- [Databricks ML Associate practice questions](./databricks-ml-associate.md) - the classical ML sibling
- [RAG explained](../../learn/concepts/rag-explained.md) - retrieval in plain English
- [Prompt injection defense](../ai-security/prompt-injection-defense.md) - questions 8 and 10 in depth
- **[📖 Databricks certification](https://www.databricks.com/learn/certification)** - official exam guides
