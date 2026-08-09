---
last-updated: 2026-08-09
difficulty: advanced
---

# Google Cloud Professional Machine Learning Engineer - Practice Questions

15 questions for the Professional ML Engineer exam, covering problem framing, data and model development on Vertex AI, pipeline automation, serving, and monitoring.

> **Cert page:** [exams/gcp/machine-learning-engineer/](../../exams/gcp/machine-learning-engineer/)

---

### Question 1
**Scenario:** A business wants to "use AI to improve retention." What is the first engineering step?

A. Choose a model architecture
B. Frame it as an ML problem: define the prediction target, the decision it informs, the label source, and the success metric tied to a business outcome
C. Collect more data
D. Provision GPUs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The exam consistently rewards framing before building. A churn model is useless unless someone acts on the score, so the decision and intervention define the label window, the prediction horizon, and the metric. Skipping this produces a technically fine model nobody uses.
</details>

---

### Question 2
**Scenario:** Features must be shared consistently between training and online serving.

A. Recompute them in each system
B. Vertex AI Feature Store, serving the same feature values offline for training and online for inference
C. A spreadsheet
D. Cache in the application

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A feature store exists to remove training-serving skew by making one definition the source for both paths, and it provides point-in-time correct historical retrieval so training does not accidentally use future values. Recomputing in two systems guarantees eventual divergence.
</details>

---

### Question 3
**Scenario:** Which Vertex AI capability trains a model with no code on tabular data?

A. AutoML
B. Custom training with a container
C. Vertex AI Workbench
D. Model Garden

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** AutoML handles feature engineering, architecture search, and tuning for tabular, image, text, and video tasks. Custom training is the escape hatch when you need your own code, and Model Garden is the catalog of pretrained and foundation models.
</details>

---

### Question 4
**Scenario:** A training job needs to run reproducibly with data prep, training, evaluation, and conditional deployment.

A. A notebook run manually
B. Vertex AI Pipelines (Kubeflow Pipelines or TFX) with components and a conditional deploy step
C. A shell script on a VM
D. Cloud Functions

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Pipelines give a versioned DAG with artifact lineage and caching, and the conditional step turns the evaluation into an enforced gate. Notebooks are for exploration; they do not produce the reproducibility or audit trail a production model needs.
</details>

---

### Question 5
**Scenario:** An online prediction endpoint must serve two model versions with traffic split.

A. Two endpoints
B. One endpoint with multiple deployed models and a traffic split percentage
C. A load balancer in front of two services
D. Batch prediction

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Vertex AI endpoints support several deployed models with a traffic split, so canary rollout and rollback are configuration changes rather than client changes. Each deployed model has its own machine type and autoscaling settings.
</details>

---

### Question 6
**Scenario:** Predictions are needed for 100 million rows overnight.

A. Online prediction
B. Batch prediction reading from BigQuery or Cloud Storage and writing results back
C. One request per row
D. A Cloud Function per row

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Batch prediction parallelizes across workers and avoids paying per-request overhead 100 million times. Online endpoints are for latency-sensitive single predictions, and using them for bulk scoring is both slow and disproportionately expensive.
</details>

---

### Question 7
**Scenario:** A deployed model's inputs are drifting from the training distribution.

A. Nothing can be detected
B. Vertex AI Model Monitoring, comparing serving inputs against a training baseline and alerting on skew and drift
C. Cloud Monitoring CPU metrics
D. Manual sampling

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Model Monitoring distinguishes training-serving skew (serving data differs from training data) from prediction drift (serving data changes over time), and alerts per feature. Infrastructure metrics show a perfectly healthy endpoint serving increasingly wrong answers.
</details>

---

### Question 8
**Scenario:** A model must explain individual predictions for a regulated decision.

A. Vertex Explainable AI with feature attributions (integrated gradients, sampled Shapley, or XRAI)
B. The training loss
C. Model size
D. The confusion matrix

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Explainable AI attributes a specific prediction to input features, which is what an adverse-decision explanation requires. The method depends on the model type: gradient-based for differentiable models, sampled Shapley for non-differentiable ones.
</details>

---

### Question 9
**Scenario:** Training data in BigQuery must be prepared for a TensorFlow model at scale.

A. Export to CSV and load into pandas
B. Use BigQuery for aggregation and Dataflow (Apache Beam) or TFX components for distributed transformation, writing TFRecords
C. Process row by row in Python
D. Use a single VM

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Pushing aggregation into BigQuery and heavy transformation into Dataflow keeps the work distributed, and TFX Transform has the important property that the same transformation graph is applied at serving time, which prevents skew.
</details>

---

### Question 10
**Scenario:** Hyperparameter tuning must be efficient on an expensive training job.

A. Grid search
B. Vertex AI hyperparameter tuning with Bayesian optimization and early stopping
C. One configuration
D. Random search over the full space with no stopping

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Bayesian search conditions each trial on previous results, so it converges in far fewer runs than grid search when each run is expensive. Early stopping of underperforming trials is where the rest of the savings comes from.
</details>

---

### Question 11
**Scenario:** A team wants a foundation model grounded in their own documents on Google Cloud.

A. Fine-tune from scratch
B. Vertex AI Search and grounding, or a RAG pipeline with an embedding model and Vector Search
C. Paste documents into every prompt
D. Train a new LLM

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Grounding keeps answers tied to retrievable sources with citations and updates as the documents update. Fine-tuning would encode a snapshot of the knowledge into weights, which is both expensive to refresh and impossible to cite.
</details>

---

### Question 12
**Scenario:** A training job must use preemptible or Spot VMs safely.

A. Never checkpoint
B. Checkpoint to Cloud Storage frequently and resume from the last checkpoint after preemption
C. Use only on-demand
D. Restart from scratch each time

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Spot capacity cuts cost substantially, and checkpointing is what converts a preemption from a lost run into a short delay. The checkpoint interval is a trade-off between storage writes and the work you are willing to lose.
</details>

---

### Question 13
**Scenario:** A model must not be trained on personally identifiable information.

A. Trust the data
B. Use Cloud DLP to inspect and de-identify (mask, tokenize, or bucket) before training, and document what was removed
C. Delete the model afterward
D. Encrypt the training job

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Models memorize training data, so PII in the corpus can resurface in outputs and in membership inference attacks. Inspecting and de-identifying before training addresses it at the source, and documenting the transformation is what makes the claim auditable.
</details>

---

### Question 14
**Scenario:** An ML system must retrain automatically when performance drops.

A. Retrain on a fixed schedule regardless
B. Trigger retraining from monitoring signals (drift or degraded outcome metrics) through a pipeline, with an evaluation gate before deployment
C. Retrain manually when someone notices
D. Never retrain

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Event-driven retraining responds to the actual condition rather than the calendar, and the evaluation gate is what prevents automatically deploying a model trained on a bad data batch. Fixed schedules are a reasonable fallback when a good trigger signal does not exist.
</details>

---

### Question 15
**Scenario:** Which best describes the responsible AI step before launching a model that affects people?

A. Check accuracy only
B. Evaluate disaggregated performance across affected groups, document the model's intended use and limitations, and define a human review and appeal path
C. Add a disclaimer
D. Get legal sign-off only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Aggregate accuracy hides subgroup failure, so disaggregated evaluation is the measurement that matters. Model cards document intended use and limits, and a human path handles the cases the model gets wrong, which is the part that determines real-world harm.
</details>

---

## Where to go deeper

- [Professional ML Engineer cert page](../../exams/gcp/machine-learning-engineer/) - notes, practice plan, strategy
- [GCP Data Engineer practice questions](./gcp-data-engineer.md) - the data platform beneath this
- [DP-100 practice questions](./azure-data-scientist-dp-100.md) - the Azure counterpart
- [AI/ML systems topic index](../../topics/ai-ml-systems.md) - MLOps across the repo
- **[📖 Google Cloud certification](https://cloud.google.com/learn/certification)** - official exam guides
