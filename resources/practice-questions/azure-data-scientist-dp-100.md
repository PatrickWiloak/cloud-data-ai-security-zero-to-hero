---
last-updated: 2026-08-09
difficulty: intermediate
---

# Azure Data Scientist Associate (DP-100) - Practice Questions

15 questions for DP-100 prep, weighted toward exploring data and training models (35-40%), with design and preparation, deployment preparation, and deploy and retrain at 20-25% each.

> **Cert page:** [exams/azure/dp-100/](../../exams/azure/dp-100/)

---

### Question 1
**Scenario:** A training job needs a GPU for four hours a week and nothing the rest of the time.

A. An always-on Compute Instance
B. A Compute Cluster with minimum nodes 0 and a GPU VM size
C. A Kubernetes online endpoint
D. Serverless Spark

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Compute clusters scale to zero when idle, so you pay only for the hours the job runs, and they scale out for parallel runs. A compute instance is a personal development box that bills while running. Online endpoints are for inference. Serverless Spark suits distributed data processing rather than single-node GPU training.
</details>

---

### Question 2
**Scenario:** A model is trained with an experiment tracked in Azure Machine Learning. What is the correct order before serving traffic?

A. Deploy, then register, then evaluate
B. Evaluate, register the model in the workspace registry, then deploy to an endpoint
C. Register, deploy, then train
D. Deploy directly from the run output

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Registration gives the artifact a name, version, and lineage back to the run, which is what makes rollback and audit possible. Deploying straight from run output leaves you without a versioned reference. Evaluation before registration prevents promoting a model that underperforms the incumbent.
</details>

---

### Question 3
**Scenario:** You need low-latency real-time predictions with autoscaling and no cluster management.

A. Batch endpoint
B. Managed online endpoint
C. A scheduled pipeline job
D. A compute instance running a notebook

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Managed online endpoints handle the compute, TLS, authentication, and blue-green deployment slots for you. Batch endpoints are asynchronous and optimized for throughput over large inputs. A pipeline job is scheduled work, and a notebook is not a production serving surface.
</details>

---

### Question 4
**Scenario:** A new model version should take 10% of live traffic before full rollout.

A. Create a second endpoint
B. Add a second deployment under the same online endpoint and set traffic allocation to 90/10
C. Retrain with 10% of data
D. Use a batch endpoint

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** An online endpoint can host multiple deployments and split traffic by percentage, which is exactly a canary. Callers keep using one URL, so rollback is a traffic change rather than a client change. A second endpoint would require clients to know about it.
</details>

---

### Question 5
**Scenario:** Training data lives in an Azure Data Lake Storage Gen2 account and must be referenced without credentials in code.

A. Hard-code a SAS token
B. Register a datastore with identity-based access and use a data asset that points at it
C. Copy the data into the notebook
D. Make the container public

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A datastore holds the connection, and identity-based access uses the workspace or user managed identity so no secret lives in code. Data assets add versioning on top. Hard-coded SAS tokens leak through notebooks and git history, and public containers are a data exposure.
</details>

---

### Question 6
**Scenario:** You want the best model over a search space of learning rates and batch sizes, stopping unpromising runs early.

A. A single training run
B. A sweep job with a sampling method and an early termination policy such as bandit or median stopping
C. AutoML featurization only
D. Manual grid search in a notebook

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Sweep jobs define the search space, the sampling strategy (random, grid, or Bayesian), the primary metric to optimize, and a termination policy that kills runs falling behind. That last part is where most of the compute savings come from. Manual search wastes budget and is not reproducible.
</details>

---

### Question 7
**Scenario:** A classification model must be explained to a regulator: which features drove a given prediction?

A. The confusion matrix
B. The Responsible AI dashboard with feature importance, including per-prediction explanations
C. The ROC curve
D. The learning rate schedule

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The Responsible AI dashboard bundles interpretability (global and local feature importance), error analysis, fairness assessment, and counterfactuals. A confusion matrix and ROC curve describe aggregate performance, not the reasoning behind an individual decision.
</details>

---

### Question 8
**Scenario:** A dataset has 5% positive cases and the model reports 95% accuracy.

A. The model is excellent
B. Accuracy is misleading with imbalance; use precision, recall, F1, or AUC-PR and consider resampling or class weights
C. Increase the learning rate
D. Add more features

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Predicting the majority class every time scores 95% here while catching nothing. Precision and recall on the positive class expose that immediately, and AUC-PR is the more honest summary metric under imbalance than AUC-ROC. Resampling and class weights address the training side.
</details>

---

### Question 9
**Scenario:** Multiple steps (prep, train, evaluate, register) must run in sequence with reusable outputs.

A. One long script
B. A pipeline job composed of components, with outputs passed between steps
C. Separate manual runs
D. A cron job

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Components are versioned, reusable units, and a pipeline wires their inputs and outputs into a DAG that can cache unchanged steps. That caching is the practical payoff: changing only the training step does not force data prep to rerun.
</details>

---

### Question 10
**Scenario:** A deployed model's accuracy degrades over months while the code is unchanged.

A. The endpoint is misconfigured
B. Data drift: the input distribution has moved away from the training distribution, so monitor drift and schedule retraining
C. The model file is corrupt
D. The compute is undersized

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Drift is the normal explanation for silent decay. Azure Machine Learning model monitoring compares production inputs against a baseline and can alert on feature drift and data quality, which is what turns retraining from a guess into a triggered action. Concept drift, where the relationship itself changes, is the related second case.
</details>

---

### Question 11
**Scenario:** An experiment must be reproducible six months later.

A. Note the results in a document
B. Use a registered environment with pinned dependencies, versioned data assets, and logged parameters and metrics per run
C. Keep the compute instance running
D. Save the notebook only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Reproducibility needs three things pinned: code, data, and environment. Registered environments capture the container and package versions, versioned data assets capture the input, and run logging captures parameters and outputs. A saved notebook without the environment usually will not run later.
</details>

---

### Question 12
**Scenario:** AutoML is used for a tabular classification task. What does it not do for you?

A. Feature engineering
B. Model selection
C. Decide whether the business problem is well posed and the label is correct
D. Cross-validation

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** AutoML automates featurization, algorithm selection, hyperparameter search, and validation. What no tool can do is tell you the target is leaking information from the future, that the label definition is wrong, or that the task should not be a classification problem at all. Target leakage is the failure mode that produces suspiciously perfect AutoML results.
</details>

---

### Question 13
**Scenario:** Scoring 50 million rows nightly with no latency requirement.

A. Managed online endpoint
B. Batch endpoint with a compute cluster
C. A single VM script
D. Real-time streaming

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Batch endpoints parallelize scoring across cluster nodes, checkpoint progress, and write outputs to storage, which fits large offline jobs. Sending 50 million rows through a real-time endpoint is slow and expensive because you pay per-request overhead for every record.
</details>

---

### Question 14
**Scenario:** A workspace must not expose data over public endpoints.

A. Managed virtual network isolation for the workspace, private endpoints to the workspace and its dependent storage, key vault, and registry
B. An NSG on the compute subnet only
C. A firewall rule on the storage account only
D. Disabling the studio UI

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The workspace is not one resource: it depends on storage, Key Vault, Container Registry, and Application Insights, and any of those left public is the gap. Managed VNet isolation plus private endpoints across the dependency set is the complete answer.
</details>

---

### Question 15
**Scenario:** A team wants to share a curated model across several workspaces.

A. Copy the file to each workspace
B. Publish it to an Azure Machine Learning registry, which is cross-workspace and cross-region
C. Email the pickle file
D. Store it in a public blob

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Registries hold models, components, environments, and data assets above the workspace level, so one artifact can be promoted across dev, test, and production workspaces with lineage intact. Copying files loses version history, and a pickle in a public blob is both an integrity and a deserialization risk.
</details>

---

## Where to go deeper

- [DP-100 cert page](../../exams/azure/dp-100/) - notes, practice plan, strategy
- [AI-102 practice questions](./azure-ai-engineer-ai-102.md) - the applied AI counterpart
- [Evals for LLMs](../../learn/concepts/evals-for-llms.md) - measuring model quality
- [AI/ML systems topic index](../../topics/ai-ml-systems.md) - MLOps in context
- **[📖 DP-100 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-100)** - official skills outline
