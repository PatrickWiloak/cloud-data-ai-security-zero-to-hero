# Google Cloud Generative AI Leader - Practice Questions

15 questions for Generative AI Leader prep. This is a business certification: expect scenario questions about value, cost, adoption, and responsible AI alongside the technical concepts.

> **Cert page:** [exams/gcp/generative-ai-leader/](../../exams/gcp/generative-ai-leader/)

---

### Question 1
**Scenario:** A retailer wants an assistant that answers customer questions about its current product catalog, which changes weekly.

A. Fine-tune a model on the catalog
B. Ground the model on the catalog data, using retrieval
C. Include the whole catalog in every prompt
D. Train a custom foundation model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Weekly changes make fine-tuning wrong, because fine-tuned knowledge is frozen at training time and would need retraining each week. Grounding updates instantly. Including the whole catalog exceeds practical context and cost limits. The commonest wrong answer on this exam is fine-tuning applied to a knowledge problem.
</details>

---

### Question 2
**Scenario:** An organization wants employees to draft documents and summarize meetings more quickly, with minimal engineering effort.

A. Build a custom application on Vertex AI
B. Adopt Gemini for Google Workspace
C. Fine-tune a model on company documents
D. Deploy an open model with Gemma

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Start at the lowest rung of the ladder. An applied assistant delivers productivity gains with no build at all. Building on the platform is for differentiated experiences, and fine-tuning or self-hosting are further up the cost and effort curve.
</details>

---

### Question 3
**Scenario:** Responses to the same prompt vary too much between runs for an extraction task.

A. Increase top-k
B. Lower the temperature
C. Fine-tune the model
D. Increase the output token limit

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Temperature is the primary control over randomness in token selection, and lowering it makes output near-deterministic. Increasing top-k widens the candidate set, adding variety. Fine-tuning is an expensive answer to a parameter setting.
</details>

---

### Question 4
**Scenario:** A model must check live inventory before answering a customer question.

A. Fine-tune the model on inventory data
B. Grounding with Google Search
C. Function calling, so the model can request that application code query the inventory system
D. Increase the context window

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Live data and actions require function calling. Fine-tuning freezes a snapshot. Search grounding covers public web information, not an internal inventory system. A larger context window does not connect the model to a live system.
</details>

---

### Question 5
**Scenario:** Which Google Cloud product provides grounded search over an organization's own content with generative summaries and citations?

A. NotebookLM
B. Vertex AI Search
C. BigQuery ML
D. Gemma

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Vertex AI Search is the enterprise product for grounded search with summaries and citations. NotebookLM is grounded research over sources an individual supplies. BigQuery ML brings generative functions to data in the warehouse. Gemma is a family of open models.
</details>

---

### Question 6
**Scenario:** A leadership team asks how to decide which generative AI use cases to pursue first.

A. Start with the most technically interesting
B. Prioritize by business value against feasibility, favouring high-value, high-feasibility quick wins with demonstration value
C. Start with the largest department
D. Pursue all candidate use cases in parallel

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Value against feasibility is the standard framing, and early wins should be chosen partly for visibility, because a demonstrated success builds the organizational appetite that later, harder projects require.
</details>

---

### Question 7
**Scenario:** A project to summarize support tickets has stalled. The model works well in demos. What is the most likely cause?

A. The model is not capable enough
B. Data readiness: access, quality, or governance of the ticket data
C. The context window is too small
D. Temperature is set incorrectly

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Data readiness is the most common real constraint on generative AI projects. A model that performs well in a demo and stalls in delivery usually points at data access, quality, or permission problems rather than model capability.
</details>

---

### Question 8
**Scenario:** Which of these is a good candidate for generative AI?

A. Calculating monthly payroll totals exactly
B. Routing tickets according to a fixed set of rules
C. Drafting first-pass responses to customer emails, reviewed by an agent
D. Determining regulatory filing figures with no review

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Good candidates involve unstructured content, have a measurable outcome, and tolerate imperfection through a review step. Exact arithmetic and deterministic rule routing are better solved conventionally. Unreviewed regulatory output requires a guarantee these models cannot give.
</details>

---

### Question 9
**Scenario:** What does grounding primarily mitigate?

A. Latency
B. Cost
C. Hallucination
D. Bias

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Grounding supplies authoritative source text so the model answers from evidence rather than from memory, which is the primary mitigation for confident wrong answers. It also enables citations so a human can verify.
</details>

---

### Question 10
**Scenario:** Which is included in total cost of ownership for a generative AI solution but commonly overlooked?

A. Inference cost
B. Data preparation, evaluation, monitoring, and change management
C. Model licensing
D. Network egress

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Inference is visible and often not the largest line. Data preparation is usually the largest hidden cost, and ongoing evaluation, monitoring, and adoption work continue for the life of the system.
</details>

---

### Question 11
**Scenario:** Which situation calls for keeping a human in the loop?

A. Summarizing internal meeting notes
B. Suggesting draft product descriptions
C. Making a credit decision affecting an applicant
D. Categorizing support tickets by topic

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** High-stakes, regulated decisions affecting individuals require human review and an explainable rationale. The other three are low-stakes, reversible, and reviewable in aggregate.
</details>

---

### Question 12
**Scenario:** Which responsible AI theme does publishing a clear notice that users are interacting with an AI system address?

A. Fairness
B. Transparency
C. Privacy
D. Accountability

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Transparency means people know AI is being used and what it does. Explainability is about explaining a specific decision, accountability is about a human being responsible for outcomes, and fairness concerns equitable outcomes across groups.
</details>

---

### Question 13
**Scenario:** An organization needs to run a model on its own infrastructure, including at the edge, with full control over the weights.

A. Gemini through Vertex AI
B. Gemma open models
C. Vertex AI Search
D. Gemini for Google Cloud

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Gemma is Google's family of open models intended to be run by the user, which is what "own infrastructure" and "control over the weights" require. The others are managed services or applied assistants.
</details>

---

### Question 14
**Scenario:** How should the success of a generative AI deployment be measured?

A. Number of prompts submitted
B. Business outcomes defined before building, plus quality, cost, and adoption metrics
C. Model size
D. Number of features shipped

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Success criteria should be defined before building and measured afterwards, covering business outcome, output quality, operational cost, and how much of the eligible work actually flows through the new capability. Prompt counts and feature counts are activity, not outcome.
</details>

---

### Question 15
**Scenario:** A regulated customer requires that data submitted to a model is not used to train the provider's foundation models, and that inference stays within a specific region.

A. This is not achievable with a managed service
B. Vertex AI enterprise controls: customer data is not used to train Google's foundation models, with regional endpoints and data residency options
C. Only self-hosting an open model satisfies this
D. It depends on the model chosen

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Enterprise data governance, residency, private connectivity, and encryption controls are frequently the deciding factor in business scenarios involving regulated industries, and they are available on the managed platform rather than requiring self-hosting.
</details>

---

## Scoring guide

- **13-15 correct (85%+):** Ready.
- **10-12 correct (65-80%):** Review the adoption ladder and the business strategy material, which is weighted more heavily than a technical reader expects.
- **Below 10:** Read the official exam guide and study guide directly, then re-read [notes 04](../../exams/gcp/generative-ai-leader/notes/04-business-strategy.md).
