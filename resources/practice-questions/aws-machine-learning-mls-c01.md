---
last-updated: 2026-08-09
difficulty: advanced
---

# AWS Certified Machine Learning - Specialty (MLS-C01) - Practice Questions

15 questions for MLS-C01 prep, weighted toward modeling (36%), exploratory data analysis (24%), then data engineering and ML implementation and operations (20% each).

MLS-C01 has been superseded for many candidates by the Machine Learning Engineer Associate (MLA-C01). Check which exam is current before booking.

> **Cert page:** [exams/aws/specialty/machine-learning-mls-c01/](../../exams/aws/specialty/machine-learning-mls-c01/)

---

### Question 1
**Scenario:** A binary classifier must catch as many fraudulent transactions as possible, accepting some false alarms.

A. Optimize accuracy
B. Optimize recall, and tune the decision threshold accordingly
C. Optimize precision
D. Optimize training speed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Recall is the fraction of actual fraud you catch, which is what "miss as few as possible" means. Precision is the cost you are choosing to pay in false positives. Accuracy is meaningless at 0.1% fraud, where predicting "not fraud" always scores 99.9%.
</details>

---

### Question 2
**Scenario:** Training accuracy is 99% and validation accuracy is 70%.

A. Underfitting; use a larger model
B. Overfitting; add regularization, dropout, more data, or early stopping
C. The data is corrupt
D. The learning rate is too low

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A large train-validation gap is the definition of overfitting: the model memorized the training set. Regularization, more data, simpler models, and early stopping all attack it. Underfitting shows as poor performance on both sets.
</details>

---

### Question 3
**Scenario:** A categorical feature has 10,000 distinct values.

A. One-hot encode it
B. Use target encoding, hashing, or a learned embedding, depending on the model
C. Drop it
D. Label encode it for a linear model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** One-hot at that cardinality creates a huge sparse matrix. Hashing bounds the dimension, target encoding compresses to a statistic (with care to avoid leakage, using out-of-fold encoding), and embeddings learn a dense representation. Label encoding imposes a false ordinal relationship on a linear model.
</details>

---

### Question 4
**Scenario:** SageMaker must serve a model with variable, spiky traffic and scale to zero between bursts.

A. A real-time endpoint with a fixed instance count
B. Serverless Inference
C. Batch Transform
D. An EC2 instance

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Serverless Inference scales with traffic and to zero, at the cost of cold starts. Real-time endpoints give consistent latency but bill continuously. Asynchronous Inference is the third option, suited to large payloads and long processing where a queue is acceptable.
</details>

---

### Question 5
**Scenario:** Two model versions must be compared on live traffic without risking full exposure.

A. Deploy both behind one endpoint as production variants with weighted traffic, or use a shadow variant
B. Two separate endpoints and manual switching
C. Offline evaluation only
D. Deploy the new one fully

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Production variants split traffic by weight behind a single endpoint, so rollback is a weight change. Shadow testing sends a copy of traffic to the new variant without returning its responses, which measures behavior with zero user risk.
</details>

---

### Question 6
**Scenario:** A dataset is highly imbalanced at 100:1.

A. Do nothing
B. Combine approaches: resampling (SMOTE or undersampling), class weights, and evaluation with precision-recall rather than accuracy
C. Collect more of the majority class
D. Use a bigger model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Imbalance affects both training and evaluation, so it needs handling in both places. Apply resampling only to the training split, never to validation or test, or your measured performance will be optimistic and wrong.
</details>

---

### Question 7
**Scenario:** Hyperparameter tuning must find good values efficiently on an expensive training job.

A. Grid search
B. SageMaker automatic model tuning with Bayesian search and early stopping
C. Random guessing
D. Manual tuning

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Bayesian optimization uses the results of previous trials to choose the next configuration, which finds good values in far fewer runs than grid search on an expensive objective. Early stopping kills unpromising trials, which is where the remaining savings come from.
</details>

---

### Question 8
**Scenario:** Feature values computed at training time differ from those computed at inference time.

A. Training-serving skew: use a feature store or shared transformation code so both paths compute features identically
B. Increase model size
C. Retrain more often
D. Ignore it

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Skew produces a model that performs well offline and badly in production, and it is one of the most common causes of that gap. SageMaker Feature Store, or at minimum a single shared transformation library, removes the possibility of the two paths diverging.
</details>

---

### Question 9
**Scenario:** Which SageMaker capability detects data drift on a deployed endpoint?

A. Model Monitor with a baseline from the training data
B. CloudWatch alarms on CPU
C. Batch Transform
D. Clarify only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Model Monitor captures endpoint traffic, compares statistics against a baseline, and reports violations for data quality, model quality, bias drift, and feature attribution drift. Clarify computes bias and explainability, and its outputs feed two of those monitor types.
</details>

---

### Question 10
**Scenario:** A time series must be split for validation.

A. Random shuffle split
B. Chronological split, training on earlier data and validating on later, with no future information in the features
C. Stratified split
D. K-fold with shuffling

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Random splitting on time series lets the model see the future, which produces excellent validation scores and a useless model. Chronological splitting and rolling-origin cross-validation preserve the causal order, and lag features must be computed with the same care.
</details>

---

### Question 11
**Scenario:** Large training data lives in S3 and the job spends most of its time downloading.

A. Use Pipe mode or FastFile mode to stream from S3, or use FSx for Lustre for repeated access
B. Use a bigger instance
C. Compress with gzip only
D. Reduce the dataset

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** File mode copies the whole dataset before training starts, which dominates the wall clock for large data. Streaming modes overlap download with compute, and FSx for Lustre is the right answer when many jobs repeatedly read the same dataset.
</details>

---

### Question 12
**Scenario:** A model must explain individual predictions to satisfy a regulator.

A. SageMaker Clarify with SHAP values for feature attribution
B. The confusion matrix
C. Training loss curves
D. Model size

<details>
<summary>Answer</summary>

<!-- -->

**Correct: A**

**Why:** SHAP attributes a prediction to its input features in a locally accurate way, which is what "why did this application get declined" requires. Aggregate performance metrics describe the model overall and say nothing about an individual decision.
</details>

---

### Question 13
**Scenario:** Which algorithm suits anomaly detection on streaming numeric data?

A. Random Cut Forest
B. XGBoost
C. Linear Learner
D. Seq2Seq

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Random Cut Forest is the built-in unsupervised anomaly detection algorithm and is available both in SageMaker and in Kinesis Data Analytics for streaming. The supervised algorithms need labeled anomalies, which is precisely what you usually lack.
</details>

---

### Question 14
**Scenario:** Training must use spot capacity without losing progress on interruption.

A. Managed spot training with checkpointing to S3
B. On-demand only
C. Restart from scratch on interruption
D. Reserved instances

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Managed spot training can cut costs substantially, and checkpointing is what makes interruption survivable: the job resumes from the last checkpoint rather than the beginning. Without checkpoints, a long job on spot is a gamble that gets worse the longer it runs.
</details>

---

### Question 15
**Scenario:** An ML pipeline must run data prep, training, evaluation, and conditional registration.

A. A shell script
B. SageMaker Pipelines with steps and a condition step gating model registration on the evaluation metric
C. Manual steps
D. A single notebook

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Pipelines gives a versioned DAG with lineage tracking and caching, and the condition step is what turns "we evaluated it" into an enforced quality gate. Notebooks are for exploration; they do not give reproducibility or auditability.
</details>

---

## Where to go deeper

- [MLS-C01 cert page](../../exams/aws/specialty/machine-learning-mls-c01/) - notes, practice plan, strategy
- [ML Engineer Associate practice questions](./aws-ml-engineer-associate.md) - the current-generation exam
- [DP-100 practice questions](./azure-data-scientist-dp-100.md) - the Azure counterpart
- [AI/ML systems topic index](../../topics/ai-ml-systems.md) - MLOps across the repo
- **[📖 AWS Certification](https://aws.amazon.com/certification/)** - official exam guides
