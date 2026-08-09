# OCI Generative AI Professional (1Z0-1127) - Practice Questions

15 questions for OCI Generative AI Professional prep. Three decisions recur: how to customize, on-demand versus dedicated cluster, and where retrieval quality comes from.

> **Cert page:** [exams/oracle/oci-generative-ai-professional/](../../exams/oracle/oci-generative-ai-professional/)

---

### Question 1
**Scenario:** An insurer wants an assistant answering questions about policy documents. Documents change monthly, answers must cite the source clause, and there are no ML engineers.

A. Fine-tune a model on the policy corpus
B. RAG over the policy documents with citations
C. Put all documents in the prompt
D. Pre-train a domain model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Monthly updates rule out fine-tuning, whose knowledge is frozen at training time. Citation requires knowing which source text produced the answer, which only retrieval provides. Putting all documents in the prompt exceeds the context window and costs enormously.
</details>

---

### Question 2
**Scenario:** A team has fine-tuned a model and wants to serve it to production with a latency commitment.

A. On-demand inference
B. A dedicated AI cluster, which is required to host a custom model
C. Either, depending on volume
D. OCI Data Science model deployment

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** On-demand serves base models only. Both fine-tuning and hosting a custom model require dedicated AI clusters, and dedicated capacity is also what makes a latency commitment possible. This is a hard constraint, not a preference.
</details>

---

### Question 3
**Scenario:** A RAG chatbot gives confidently wrong answers although the information is in the corpus. The team increased retrieved chunks from 3 to 20 and it got worse.

A. Increase the chunk count further
B. Raise the temperature
C. Log the retrieved chunks to see whether the right one is present, then reduce the count and consider reranking
D. Fine-tune the model on the corpus

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Diagnose before changing. If the correct chunk is retrieved but ignored, 20 chunks is likely the cause because models attend less to the middle of a long context. If it is not retrieved, the problem is chunking, the embedding model, or query phrasing. Raising temperature increases variety, not correctness.
</details>

---

### Question 4
**Scenario:** A pipeline extracts structured fields from contracts and produces slightly different values on repeated runs, breaking downstream reconciliation.

A. Fine-tune for consistency
B. Set temperature to 0 and validate the output against a schema
C. Retry until two runs agree
D. Increase max tokens

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Temperature is the primary control over randomness, and 0 gives near-deterministic decoding. Schema validation is the safety net, since output is not guaranteed identical across model versions. Fine-tuning is an expensive answer to a decoding parameter problem.
</details>

---

### Question 5
**Scenario:** Inference costs tripled. Every request sends the full conversation history, 15 retrieved chunks, and a 2,000-token system prompt.

A. Move to a dedicated cluster
B. Reduce retrieved chunks, summarize or window the conversation memory, shorten the system prompt, and cap max tokens
C. Cache whole responses
D. Reduce traffic

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cost is driven by tokens in and out. The largest levers, in order, are retrieved context size, conversation history handling, and system prompt length. A dedicated cluster gives predictable cost, not necessarily lower cost. Response caching helps only for repeated identical questions.
</details>

---

### Question 6
**Scenario:** A multi-tenant assistant returns one organization's content to a user from another. What is the correct fix?

A. Instruct the model in the system prompt not to reveal other tenants' data
B. Filter by tenant in the vector query, or use separate namespaces per tenant, authorizing on the end user's identity
C. Post-filter results after generation
D. Deploy a separate fine-tuned model per tenant

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** This is a retrieval authorization bug. A prompt is not an access control. Post-filtering is too late because the data has already entered the model's context. Separate models per tenant is enormously expensive and does not address the retrieval boundary.
</details>

---

### Question 7
**Scenario:** Which statement about fine-tuning versus RAG is correct?

A. Fine-tuning is always more accurate
B. Fine-tuning changes behavior; RAG changes what the model knows for a request
C. RAG requires retraining when documents change
D. They are alternatives that cannot be combined

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** This is the decision rule the exam applies throughout. RAG updates instantly when source documents change, which is precisely why it beats fine-tuning for knowledge. The two can be combined: a fine-tuned model answering over retrieved context.
</details>

---

### Question 8
**Scenario:** Chunks are set to 50 tokens each. Answers cite the right documents but lack coherent explanation.

A. Retrieve fewer chunks
B. Increase chunk size and add overlap, splitting on structural boundaries
C. Change the similarity metric
D. Lower the temperature

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Chunks that are too small lack surrounding context, so retrieval finds the right words but the model cannot ground a coherent answer. Larger chunks with overlap, split on paragraphs or sections, resolve it. The similarity metric and temperature address different problems.
</details>

---

### Question 9
**Scenario:** Which LangChain component holds prior conversation turns and is a major cost driver?

A. Retriever
B. Output parser
C. Memory
D. Text splitter

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Naive memory resends the whole conversation each turn, so token use grows sharply over a long session. Windowed memory keeps only recent turns and summary memory compresses older ones, both of which control the cost.
</details>

---

### Question 10
**Scenario:** What must be true for a query embedding to retrieve the right chunks?

A. The query must use the same words as the document
B. The query must be embedded with the same model used to index the chunks
C. The vector store must use Euclidean distance
D. The chunks must be sorted alphabetically

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Embeddings from different models occupy different vector spaces, so similarity between them is meaningless. Semantic search exists precisely so that queries need not share wording with documents, and the metric must match how the embedding model was trained.
</details>

---

### Question 11
**Scenario:** Which parameter should be adjusted to make output less repetitive over a long generation?

A. Temperature only
B. Frequency penalty
C. Max tokens
D. Top-k set to 1

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Frequency penalty reduces the likelihood of tokens in proportion to how often they have already appeared, which directly targets repetition. Presence penalty discourages tokens that have appeared at all. Top-k of 1 is greedy decoding, which usually increases repetition.
</details>

---

### Question 12
**Scenario:** A RAG system must be evaluated. What should be measured?

A. Answer quality only
B. Retrieval quality and answer quality separately
C. Model perplexity
D. Token throughput

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** They fail for different reasons and need different fixes. Retrieval is measured by whether the correct source appeared in the top K and how highly it ranked; answer quality by faithfulness, relevance, and correctness. Perplexity evaluates a model, not an application.
</details>

---

### Question 13
**Scenario:** Which parameter-efficient fine-tuning method does OCI Generative AI offer?

A. Full fine-tuning only
B. T-Few
C. Distillation
D. Quantization

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** T-Few updates a fraction of the weights, which makes fine-tuning far cheaper and faster than full fine-tuning and reduces the amount of training data required. Distillation and quantization are model compression techniques, not fine-tuning methods.
</details>

---

### Question 14
**Scenario:** What is the primary risk of retrieving from a corpus that outside parties can write to?

A. Slower retrieval
B. Indirect prompt injection: planted instructions reach the model through retrieved text
C. Higher embedding costs
D. Duplicate chunks

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Anything an outsider can write into the corpus can be retrieved into a future prompt, which makes the index a delivery vehicle for instructions. Controlling write access to the corpus and constraining what the application can do are the mitigations.
</details>

---

### Question 15
**Scenario:** Which is the correct order of the RAG indexing phase?

A. Embed the query, search, retrieve, generate
B. Chunk the documents, embed the chunks, store the vectors with metadata
C. Fine-tune, deploy, evaluate
D. Store the documents, generate, then embed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Indexing runs once, or on document change: chunk, embed, store. The query phase is the other option listed: embed the query, search, retrieve, augment the prompt, generate. Keeping the two phases distinct is the basis for diagnosing where a RAG system fails.
</details>

---

## Scoring guide

- **13-15 correct (85%+):** Ready. The pass mark is 68%.
- **10-12 correct (65-80%):** Review the customization decision table and the diagnosis order for RAG failures.
- **Below 10:** Work the [scenarios](../../exams/oracle/oci-generative-ai-professional/scenarios.md) and build the [RAG pipeline project](../hands-on-projects/build-rag-pipeline.md) in this repo.
