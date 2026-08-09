---
last-updated: 2026-08-09
difficulty: intermediate
---

# Google Cloud Generative AI (Self-Directed Track) - Practice Questions

15 questions for the Google Cloud Generative AI study track, covering Gemini models on Vertex AI, grounding and RAG, agents, evaluation, and responsible AI.

This is a self-directed track rather than a Google exam, so these target working knowledge rather than a published objective list.

> **Cert page:** [exams/gcp/genai/](../../exams/gcp/genai/)

---

### Question 1
**Scenario:** Which Google Cloud surface provides access to Gemini and other foundation models with enterprise controls?

A. Vertex AI, including Model Garden and the Gemini API
B. BigQuery only
C. Cloud Functions
D. Compute Engine

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Vertex AI is the managed platform with data residency options, VPC Service Controls support, customer-managed encryption keys, and a commitment that customer prompts are not used to train the foundation models. Those enterprise properties are usually why an organization chooses it over a consumer API.
</details>

---

### Question 2
**Scenario:** Answers must be grounded in the organization's own documents with citations.

A. Fine-tune the model
B. Grounding with Vertex AI Search over your corpus, or a custom RAG pipeline with Vertex AI Vector Search
C. Increase the temperature
D. Use a larger model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Grounding retrieves passages and returns citations, so answers are checkable and update as the documents update. Fine-tuning bakes a snapshot into weights and cannot cite a source, which fails most enterprise requirements on its own.
</details>

---

### Question 3
**Scenario:** A model must return answers grounded in current public web information.

A. Grounding with Google Search
B. A larger context window
C. Higher temperature
D. A longer prompt

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Search grounding attaches retrieved web results to the request and returns supporting links, which covers the "what happened recently" gap that a model's training cutoff creates. It is a separate configuration from private-corpus grounding and the two can be combined.
</details>

---

### Question 4
**Scenario:** Which parameter should be adjusted to make responses more focused and less random?

A. `temperature` toward 0 (and optionally `topP`, but not both aggressively)
B. `maxOutputTokens`
C. `candidateCount`
D. `stopSequences`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Temperature scales sampling randomness and topP truncates the candidate distribution. Tuning both hard at once makes behavior difficult to reason about, so pick one. `maxOutputTokens` bounds length and `stopSequences` ends generation at a marker.
</details>

---

### Question 5
**Scenario:** An application needs the model to call an internal API.

A. Function calling: declare the function schema, let the model emit a structured call, execute it in your code, and return the result
B. Ask the model to describe the API
C. Fine-tune on API responses
D. Paste the API docs in the prompt

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The model never calls anything itself; it emits a structured request that your code decides whether to execute. That gap is the security boundary: authorization must be checked there, against the calling user's rights, not left to the model.
</details>

---

### Question 6
**Scenario:** Gemini's multimodal capability is used to analyze a video.

A. Extract frames manually and describe each
B. Pass the video directly as part of the request, since Gemini accepts video, image, audio, and text natively
C. Convert to text first
D. It is not supported

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Native multimodality means the model reasons over the video with its temporal and audio context rather than over a lossy text summary you produced first. Frame-by-frame preprocessing throws away exactly the information that makes video analysis useful.
</details>

---

### Question 7
**Scenario:** Safety filters block legitimate content in a medical application.

A. Disable all safety settings
B. Tune the configurable harm category thresholds to the levels the use case justifies, and add your own domain-appropriate checks
C. Rewrite prompts to avoid medical terms
D. Switch providers

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Safety settings expose per-category thresholds so you can calibrate to context rather than choosing between all and nothing. Loosening them is a documented decision that should come with compensating controls, not a silent configuration change.
</details>

---

### Question 8
**Scenario:** Cost must be reduced for an application with a long, unchanging preamble on every request.

A. Context caching for the repeated content
B. A larger model
C. More output tokens
D. More replicas

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Context caching stores the processed prefix so repeated requests do not re-pay for it, which suits long system instructions, large documents, or a codebase reused across turns. Model routing to a smaller model for simple requests is the complementary lever.
</details>

---

### Question 9
**Scenario:** Output must conform to a JSON schema every time.

A. Ask for JSON in the prompt
B. Controlled generation with a response schema, then validate the parsed result
C. Parse with regular expressions
D. Retry until it works

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Constraining decoding to a schema eliminates the class of errors where the model wraps JSON in prose or omits a field. Validation afterwards is still worth keeping, because schema-valid output can still be semantically wrong.
</details>

---

### Question 10
**Scenario:** An agent must complete multistep tasks using several tools.

A. A single prompt
B. Vertex AI Agent Builder or an agent framework, with per-tool authorization checked in code and hard limits on loop iterations
C. Chain prompts manually forever
D. A fine-tuned model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Agents need three things the model cannot provide: an execution loop with termination bounds, tools with narrowly scoped credentials, and authorization evaluated against the calling user. Without those, an agent's blast radius is whatever its service account can do.
</details>

---

### Question 11
**Scenario:** A RAG system returns irrelevant passages.

A. Increase temperature
B. Improve chunking, add hybrid search and a reranker, and evaluate retrieval separately from generation
C. Use a larger model
D. Shorten the answers

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Retrieval and generation fail for different reasons, so measure them separately: recall at k tells you whether the right passage was retrieved at all. If it was not, no change to the generation side can recover it.
</details>

---

### Question 12
**Scenario:** Model quality must be measured before and after a change.

A. Manual review
B. The Vertex AI evaluation service with task-appropriate metrics, plus your own dataset representing production traffic
C. Vendor benchmarks
D. Latency only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Public benchmarks say little about your specific distribution. Computation-based metrics and model-based (autorater) evaluation both have a place, and the dataset that matters is one drawn from real requests, including the awkward ones.
</details>

---

### Question 13
**Scenario:** Generated images must be identifiable as AI-generated.

A. A caption asking users to be honest
B. SynthID watermarking, which embeds an imperceptible, detectable marker in generated media
C. A filename convention
D. Metadata only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Watermarking survives common transformations that strip metadata, such as screenshots and re-encoding, which is exactly where filename and EXIF approaches fail. It supports provenance claims rather than relying on downstream honesty.
</details>

---

### Question 14
**Scenario:** Model customization is needed for a specific output style with a few hundred examples.

A. Pretraining
B. Supervised fine-tuning (including parameter-efficient tuning) on the labeled examples
C. RAG
D. A longer prompt only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Style, format, and task-specific behavior are what fine-tuning teaches well, and parameter-efficient methods make it feasible at that data scale. Reach for it after prompt engineering and few-shot examples stop improving results, not before.
</details>

---

### Question 15
**Scenario:** Which describes Google's responsible AI expectation for a launched feature?

A. Accuracy testing alone
B. Assess the use case for harms, evaluate performance across affected groups, apply safety controls, document limitations, and provide a human path for contested outcomes
C. A terms-of-service update
D. Nothing specific

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The pattern is consistent across major providers: identify harms in context, measure disaggregated performance, apply layered controls, be transparent about limits, and keep a human in the loop where the stakes justify it. Aggregate accuracy is the measure that hides the problems.
</details>

---

## Where to go deeper

- [Google Cloud GenAI track page](../../exams/gcp/genai/) - notes, practice plan, strategy
- [Generative AI Leader practice questions](./gcp-generative-ai-leader.md) - the business-level certification
- [Azure GenAI track practice questions](./azure-generative-ai-track.md) - the Azure counterpart
- [Prompt injection defense](../ai-security/prompt-injection-defense.md) - the security side of question 10
- **[📖 Vertex AI generative AI documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)** - primary source
