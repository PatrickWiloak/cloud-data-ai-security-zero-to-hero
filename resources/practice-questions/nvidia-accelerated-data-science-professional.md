---
last-updated: 2026-08-09
difficulty: advanced
---

# NVIDIA Certified Professional - Accelerated Data Science (NCP-ADS) - Practice Questions

15 questions for NCP-ADS prep across the RAPIDS ecosystem: cuDF, cuML, cuGraph, GPU ETL with Spark and Dask, and performance work.

> **Cert page:** [exams/nvidia/accelerated-data-science-professional/](../../exams/nvidia/accelerated-data-science-professional/)

---

### Question 1
**Scenario:** Which RAPIDS library provides a pandas-like DataFrame API on the GPU?

A. cuML
B. cuDF
C. cuGraph
D. cuSpatial

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** cuDF mirrors the pandas API for GPU dataframes. cuML mirrors scikit-learn for machine learning, cuGraph handles graph analytics with a NetworkX-like surface, and cuSpatial covers geospatial operations. Knowing the mapping from CPU library to RAPIDS equivalent is core NCP-ADS material.
</details>

---

### Question 2
**Scenario:** An existing pandas script must be accelerated with minimal code change.

A. Rewrite it in CUDA C++
B. Use `cudf.pandas` accelerator mode, which intercepts pandas calls and runs supported operations on the GPU with CPU fallback
C. Increase the CPU count
D. Convert to NumPy

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The pandas accelerator lets unmodified code run on the GPU where operations are supported and fall back transparently where they are not, which removes the porting cost from the decision. Watch the fallback rate, because heavy fallback means you are paying transfer costs for little benefit.
</details>

---

### Question 3
**Scenario:** A dataset is larger than a single GPU's memory.

A. It cannot be processed
B. Use Dask-cuDF to partition across multiple GPUs or process in chunks, with out-of-core spilling where supported
C. Downsample the data
D. Switch to pandas

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Dask-cuDF partitions the frame across workers so aggregate GPU memory becomes the ceiling, and unified virtual memory or spilling handles overflow at a performance cost. Downsampling changes the analysis rather than scaling it.
</details>

---

### Question 4
**Scenario:** A GPU pipeline is slower than the CPU version for a small dataset.

A. The GPU is faulty
B. Fixed overheads (kernel launch, host-to-device transfer) dominate for small data; GPUs win once the work per transfer is large enough
C. cuDF is broken
D. Use more GPUs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Acceleration is a throughput story, so there is a crossover point below which the transfer and launch overhead exceeds the compute saved. Keeping data resident on the GPU across the whole pipeline, rather than bouncing to host between steps, is what moves that crossover in your favor.
</details>

---

### Question 5
**Scenario:** Which format should be read for the fastest GPU ingestion of columnar data?

A. CSV
B. Parquet, read with cuDF (optionally via GPUDirect Storage)
C. JSON
D. XML

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Parquet is columnar, compressed, and carries a schema, so only the needed columns are read and parsing is cheap. CSV parsing is expensive and type inference is error-prone, and row-oriented text formats waste bandwidth on columns you never use.
</details>

---

### Question 6
**Scenario:** cuML's `RandomForestClassifier` results differ slightly from scikit-learn's.

A. cuML is incorrect
B. Implementation and floating-point ordering differences on GPU cause small variation; validate on metrics rather than exact equality
C. The data is corrupt
D. Use CPU only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Parallel reductions do not sum in a fixed order, and algorithmic details differ between implementations, so bit-identical results are not the goal. Compare accuracy, AUC, or RMSE within a tolerance, which is the right acceptance test for a port anyway.
</details>

---

### Question 7
**Scenario:** Apache Spark jobs should use GPUs for SQL and dataframe operations.

A. The RAPIDS Accelerator for Apache Spark, which offloads supported operations to the GPU
B. Rewrite everything in cuDF
C. Increase executor memory
D. Use Spark Streaming

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The plugin intercepts the physical plan and replaces supported operators with GPU versions, falling back to CPU otherwise, so existing Spark SQL runs unchanged. Reading the explain output to see which stages actually ran on GPU is the standard tuning step.
</details>

---

### Question 8
**Scenario:** A graph analytics job must compute PageRank over 500 million edges.

A. NetworkX on CPU
B. cuGraph, optionally multi-GPU, using its GPU PageRank implementation
C. A SQL query
D. Manual iteration in Python

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** cuGraph implements the standard graph algorithms on GPU with an interface close to NetworkX, and multi-GPU support extends it beyond a single device's memory. NetworkX is pure Python and does not reach this scale in practical time.
</details>

---

### Question 9
**Scenario:** A cuML model trained on GPU must be served in a CPU-only environment.

A. It is impossible
B. Export to a portable format such as ONNX or a Treelite-compatible model, or use a compatible CPU inference library
C. Retrain on CPU
D. Ship the GPU

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Training and inference hardware do not have to match. Forest models can be exported for CPU inference, and ONNX covers many other model types. Forest Inference Library is the reverse case: CPU-trained tree ensembles served fast on GPU.
</details>

---

### Question 10
**Scenario:** GPU memory fills during a long chain of cuDF operations.

A. Restart the kernel each time
B. Manage the memory pool (RMM), delete intermediate frames, and avoid retaining references to intermediates
C. Use smaller data types only
D. Add more CPUs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RAPIDS Memory Manager pools allocations to avoid the cost of repeated cudaMalloc, and configuring the pool is standard practice. The Python-side cause is usually intermediate frames still referenced by a notebook variable or output cell, so they are never freed.
</details>

---

### Question 11
**Scenario:** A feature engineering step uses a Python UDF applied row by row and is slow.

A. Keep the loop
B. Vectorize with cuDF column operations, or write a numba CUDA kernel if the logic cannot be expressed with them
C. Use pandas instead
D. Add more GPUs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Row-wise Python defeats the parallelism entirely. Column operations run as GPU kernels over the whole array, and numba lets you compile custom element-wise logic when the built-in operations do not cover it.
</details>

---

### Question 12
**Scenario:** Which cuML algorithm family benefits most dramatically from GPU acceleration?

A. Single small decision tree
B. Compute-heavy algorithms over large data: k-nearest neighbors, DBSCAN, UMAP, t-SNE, and large random forests
C. Simple counting
D. String concatenation

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Algorithms dominated by pairwise distance computation or many independent tree builds map extremely well onto thousands of cores, which is where the largest speedups appear. Trivially cheap operations are dominated by overhead, which is question 4 again.
</details>

---

### Question 13
**Scenario:** Reproducibility is required across runs of a GPU pipeline.

A. Reproducibility is impossible on GPU
B. Set random seeds, pin library and container versions, and accept documented floating-point tolerance where parallel reduction order varies
C. Run on CPU only
D. Disable parallelism

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Seeds and pinned environments give reproducible pipelines; what you cannot generally promise is bit-identical floating-point results, because reduction order varies with scheduling. Stating the tolerance up front avoids arguments later about whether a difference is a bug.
</details>

---

### Question 14
**Scenario:** A profiling exercise must show where a RAPIDS pipeline spends its time.

A. Wall-clock timing of the whole script
B. NVTX annotations with Nsight Systems, plus per-stage timing, to separate transfer, compute, and CPU-side work
C. GPU temperature
D. Count the lines of code

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A total runtime number does not distinguish a slow kernel from a pipeline stalled on host-to-device copies or on Python. NVTX ranges make your own stages visible in the Nsight timeline alongside CUDA activity, which is what localizes the cost.
</details>

---

### Question 15
**Scenario:** Which describes the ideal RAPIDS pipeline shape?

A. Move data between host and device at every step
B. Read directly into GPU memory, keep it resident through ETL, feature engineering, and training, and transfer out only the final result
C. Use the GPU only for training
D. Convert to pandas between steps

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Each host-device round trip costs PCIe bandwidth and synchronization, so a pipeline that bounces between cuDF and pandas can spend more time transferring than computing. Keeping data resident end to end is the single largest architectural lever in accelerated data science.
</details>

---

## Where to go deeper

- [NCP-ADS cert page](../../exams/nvidia/accelerated-data-science-professional/) - notes, practice plan, strategy
- [NCP-AII practice questions](./nvidia-ai-infrastructure-professional.md) - the infrastructure underneath
- [GPUs for AI](../../learn/concepts/gpus-for-ai.md) - why GPUs are fast at this
- [Databricks Data Engineer Associate practice questions](./databricks-data-engineer-associate.md) - the Spark counterpart
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
