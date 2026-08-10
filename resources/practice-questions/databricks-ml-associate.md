---
last-updated: 2026-08-09
difficulty: intermediate
---

# Databricks Certified Machine Learning Associate - Practice Questions

15 questions for the ML Associate exam, weighted toward ML workloads on Databricks (29%) and the ML workflow (29%), then Spark ML (17%), deep learning (13%), and scaling (12%).

> **Cert page:** [exams/databricks/ml-associate/](../../exams/databricks/ml-associate/)

---

### Question 1
**Scenario:** An experiment's parameters, metrics, and model artifact must be recorded automatically.

A. Manual notes
B. MLflow autologging, or explicit `mlflow.log_param` and `log_metric` calls within a run
C. Print statements
D. A spreadsheet

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Autologging captures parameters, metrics, and the model for supported libraries with one line, which means tracking happens by default rather than when someone remembers. Runs are then comparable in the experiment UI without any bookkeeping discipline.
</details>

---

### Question 2
**Scenario:** A model must be promoted from development to production with a clear lifecycle.

A. Copy the file
B. Register the model in Unity Catalog with model versions and aliases such as `champion`, and grant access through the catalog
C. Email the pickle
D. Rename the artifact

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The registry keeps lineage back to the producing run and makes promotion an explicit, auditable action. Aliases replaced the older named stages, so applications reference `@champion` and a promotion is an alias move rather than a redeployment.
</details>

---

### Question 3
**Scenario:** Hyperparameters must be tuned in parallel across a cluster.

A. A sequential loop
B. Hyperopt with `SparkTrials`, or Optuna, distributing trials across workers
C. Manual tuning
D. One configuration

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Distributing trials uses the cluster you are already paying for, and Tree-structured Parzen Estimator search converges faster than grid search by conditioning on previous results. Each trial also logs to MLflow automatically, which keeps the search auditable.
</details>

---

### Question 4
**Scenario:** Features used in training must match those used at inference.

A. Recompute in both places
B. Databricks Feature Store (Feature Engineering in Unity Catalog), which serves the same definitions offline and online
C. A shared spreadsheet
D. Copy the code

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The feature store removes training-serving skew by making one definition authoritative, and it supports point-in-time joins so training does not accidentally use values that were not available at prediction time. Copied code diverges as soon as someone fixes a bug in one place.
</details>

---

### Question 5
**Scenario:** A scikit-learn model must be trained on data too large for one machine.

A. Sample the data
B. Use Spark ML for distributed training, or distribute single-node training across the cluster with `applyInPandas` for per-group models
C. Buy a bigger driver
D. It cannot be done

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Spark ML implements distributed versions of common algorithms. The per-group pattern is the other common case: thousands of small models, one per store or customer segment, each fitting comfortably on one worker and trained in parallel.
</details>

---

### Question 6
**Scenario:** A Spark ML pipeline includes indexing, assembling, and a classifier.

A. Run each step manually
B. A `Pipeline` of stages, fit once, producing a `PipelineModel` that applies the same transformations at inference
C. Separate notebooks
D. SQL only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Wrapping the transformations and the estimator into one pipeline means the fitted preprocessing travels with the model, so serving cannot accidentally apply different encoding. This is the Spark ML answer to training-serving skew.
</details>

---

### Question 7
**Scenario:** A classification model on imbalanced data reports 98% accuracy.

A. Ship it
B. Evaluate with precision, recall, F1, and area under the precision-recall curve, and consider class weights or resampling
C. Increase the training epochs
D. Add features

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** With 2% positives, predicting the majority class always scores 98%. Precision and recall on the minority class expose that immediately, and resampling should be applied only to the training split so the evaluation stays honest.
</details>

---

### Question 8
**Scenario:** A deep learning model must train on multiple GPUs.

A. A single GPU only
B. Distributed training with TorchDistributor (or Ray on Databricks), scaling from one node to several
C. CPU training
D. Reduce the model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** TorchDistributor runs PyTorch distributed training on a Databricks cluster, handling process launch and coordination. Start single-node multi-GPU and move to multi-node only when the model or data genuinely requires it, since inter-node communication adds real cost.
</details>

---

### Question 9
**Scenario:** A model must serve real-time predictions with autoscaling.

A. A notebook
B. Mosaic AI Model Serving with a registered model version, scaling on request volume
C. A batch job
D. A cron script

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Model Serving provides an HTTPS endpoint with authentication, autoscaling, and optional scale-to-zero, backed by a registered model version. Batch scoring remains the right answer for high-volume offline work where latency does not matter.
</details>

---

### Question 10
**Scenario:** Data leakage is suspected because validation performance is suspiciously high.

A. Accept the result
B. Check for target leakage: features computed after the label event, identifiers correlated with the target, or preprocessing fitted before the split
C. Increase regularization
D. Use a smaller model

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Fitting a scaler or an encoder on the full dataset before splitting leaks distributional information into validation. The other classic is a feature that only exists because the outcome already happened. Both produce excellent offline numbers and a useless production model.
</details>

---

### Question 11
**Scenario:** Model training must be reproducible months later.

A. Save the notebook
B. Log the model with its signature and environment, pin the cluster runtime version, and version the input data (Delta table version or a snapshot)
C. Remember the settings
D. Save only the metrics

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Code, data, and environment all have to be pinned. Delta time travel supplies the data version, MLflow captures the conda or pip environment and model signature, and the runtime version pins the libraries the notebook assumed.
</details>

---

### Question 12
**Scenario:** A batch scoring job must run nightly on new data.

A. Manual runs
B. A scheduled Databricks job loading the registered model and writing predictions to a Delta table
C. A notebook someone opens
D. Real-time serving for all rows

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Batch scoring through `mlflow.pyfunc.spark_udf` parallelizes across the cluster and writes results transactionally. Pushing millions of rows through a real-time endpoint pays per-request overhead for every record.
</details>

---

### Question 13
**Scenario:** Two models must be compared on the same evaluation data.

A. Run them at different times
B. Log both as MLflow runs in one experiment with the same metrics, and compare in the run comparison UI
C. Compare file sizes
D. Ask the team

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Comparison requires the same metric names on the same data, which is exactly what an experiment groups. Logging the evaluation dataset version alongside the metrics is what makes the comparison defensible later.
</details>

---

### Question 14
**Scenario:** AutoML is used on a tabular dataset.

A. It replaces the data scientist
B. It produces baseline models plus generated notebooks showing the code, which serve as a starting point for refinement
C. It only reports metrics
D. It cannot be inspected

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The generated notebook is the distinguishing feature: nothing is hidden, so you can see the preprocessing and modeling choices and take over from there. What AutoML cannot do is tell you the label is wrong or the problem is badly framed.
</details>

---

### Question 15
**Scenario:** A cluster for ML work must have the right libraries.

A. Install packages in every notebook
B. Use the Databricks Runtime for Machine Learning, which includes common ML libraries and GPU support
C. Build from scratch
D. Use the standard runtime

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The ML runtime ships with tested versions of scikit-learn, PyTorch, TensorFlow, XGBoost, MLflow, and CUDA where applicable. Installing ad hoc on the standard runtime produces version conflicts and cluster start times that grow with every added package.
</details>

---

## Where to go deeper

- [ML Associate cert page](../../exams/databricks/ml-associate/) - notes, practice plan, strategy
- [ML Professional practice questions](./databricks-ml-professional.md) - the next level up
- [Data Engineer Associate practice questions](./databricks-data-engineer-associate.md) - the data platform beneath
- [AI/ML systems topic index](../../topics/ai-ml-systems.md) - MLOps across the repo
- **[📖 Databricks certification](https://www.databricks.com/learn/certification)** - official exam guides
