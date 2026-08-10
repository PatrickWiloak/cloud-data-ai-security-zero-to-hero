---
last-updated: 2026-08-09
difficulty: advanced
---

# NVIDIA Certified Professional - Generative AI and LLMs (NCP-GENL) - Practice Questions

15 questions for NCP-GENL prep, evenly weighted across LLM architecture, training and fine-tuning at scale, inference optimization, prompt engineering and RAG, and production deployment (20% each).

> **Cert page:** [exams/nvidia/genai-llms-professional/](../../exams/nvidia/genai-llms-professional/)

---

### Question 1
**Scenario:** Inference throughput is low because requests wait for the longest sequence in each batch to finish.

A. Increase the batch size
B. Enable in-flight (continuous) batching so finished sequences are evicted and new ones join mid-batch
C. Reduce the context window
D. Use a smaller GPU

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Static batching wastes GPU cycles on padding and on slots held by finished sequences. Continuous batching, which TensorRT-LLM and vLLM implement, replaces completed sequences immediately and typically multiplies throughput several times over. Simply raising batch size makes the head-of-line problem worse.
</details>

---

### Question 2
**Scenario:** KV cache memory dominates GPU usage at long context lengths.

A. Paged attention style KV cache management, plus KV cache quantization or grouped-query attention
B. Increase max_tokens
C. Disable the cache entirely
D. Add more layers

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** KV cache grows linearly with sequence length and batch size and typically becomes the binding memory constraint before weights do. Paged allocation removes fragmentation, GQA reduces the number of KV heads, and quantizing the cache to FP8 or INT8 cuts it further. Disabling the cache would force quadratic recomputation.
</details>

---

### Question 3
**Scenario:** A 70B parameter model does not fit on a single GPU.

A. Tensor parallelism to shard each layer across GPUs, optionally with pipeline parallelism across nodes
B. Data parallelism
C. Gradient accumulation
D. A larger batch size

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Data parallelism replicates the whole model per device, so it does not help when the model itself does not fit. Tensor parallelism splits individual matrices across GPUs with high communication needs, which is why it stays within an NVLink domain, while pipeline parallelism splits layers and tolerates slower inter-node links.
</details>

---

### Question 4
**Scenario:** A fine-tuning run must minimize GPU memory while keeping most of the quality of full fine-tuning.

A. LoRA or QLoRA with a frozen base model
B. Full fine-tuning at FP32
C. Training from scratch
D. Prompt tuning only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** LoRA trains a small number of adapter parameters, so optimizer state (the dominant memory cost in training) shrinks dramatically. QLoRA adds a quantized frozen base to cut it further. Prompt tuning is even lighter but has less capacity for genuinely new behavior.
</details>

---

### Question 5
**Scenario:** Which technique reduces the latency of generating tokens by proposing several tokens ahead and verifying them in one pass?

A. Speculative decoding with a smaller draft model
B. Beam search
C. Top-k sampling
D. Gradient checkpointing

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A cheap draft model proposes tokens and the target model verifies them in a single forward pass, accepting the longest correct prefix. Output distribution is preserved, so this is a pure latency win when acceptance rates are good. Gradient checkpointing is a training memory technique.
</details>

---

### Question 6
**Scenario:** Multi-node training slows down disproportionately as node count rises.

A. The interconnect is the bottleneck: check NCCL collectives, topology, and whether InfiniBand with GPUDirect RDMA is being used
B. The GPUs are faulty
C. The dataset is too small
D. The learning rate is wrong

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** All-reduce traffic grows with scale, so communication rather than compute becomes the limit. NCCL debug output, topology awareness, and GPUDirect RDMA over InfiniBand are the standard investigation. A learning rate problem would show up as poor convergence rather than poor scaling.
</details>

---

### Question 7
**Scenario:** A production serving stack needs multiple models, multiple frameworks, dynamic batching, and model versioning.

A. NVIDIA Triton Inference Server
B. A single Flask app
C. cuDF
D. NeMo Curator

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Triton serves TensorRT, PyTorch, ONNX, and Python backends concurrently with dynamic batching, concurrent model instances, model repositories with versions, and ensemble pipelines. NIM builds on this stack for packaged LLM deployment.
</details>

---

### Question 8
**Scenario:** FP8 quantization is applied and quality drops noticeably on a reasoning benchmark.

A. Accept the loss
B. Investigate calibration data and per-layer sensitivity, and consider keeping sensitive layers at higher precision (mixed precision)
C. Revert to FP32 everywhere
D. Increase temperature

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Quantization sensitivity is not uniform across layers, and calibration data that does not resemble production traffic produces poor scales. Selectively keeping outlier-heavy layers at higher precision usually recovers most of the loss while retaining most of the speedup.
</details>

---

### Question 9
**Scenario:** A RAG system must handle queries that mix an exact product code with a natural-language description.

A. Pure vector search
B. Hybrid search combining sparse (BM25 or keyword) and dense retrieval, then rerank
C. Keyword search only
D. Increase the embedding dimension

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Dense embeddings are weak on rare exact tokens such as SKUs and error codes, which is precisely where sparse retrieval excels. Fusing both and applying a cross-encoder reranker gives the best of each. Raising dimensionality does not fix the exact-match weakness.
</details>

---

### Question 10
**Scenario:** Which describes the NeMo framework's role?

A. A GPU monitoring tool
B. An end-to-end framework for building, customizing, and deploying generative models, including data curation, training, PEFT, alignment, and export
C. A vector database
D. A container registry

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** NeMo spans the model lifecycle: NeMo Curator for data, the training and customization stack for pretraining and PEFT, alignment methods, Guardrails for safety, and export paths into TensorRT-LLM and NIM for serving.
</details>

---

### Question 11
**Scenario:** Time to first token is acceptable but inter-token latency is poor under load.

A. The prefill phase is the bottleneck
B. The decode phase is memory-bandwidth bound; consider larger batches, better KV cache handling, quantization, or a GPU with higher bandwidth
C. The tokenizer is slow
D. Network latency

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Prefill is compute bound and determines time to first token; decode is memory-bandwidth bound and determines inter-token latency because each step reads the full weight set. Knowing which phase a symptom belongs to points at completely different fixes, and chunked prefill exists to stop long prefills stalling decode.
</details>

---

### Question 12
**Scenario:** Several fine-tuned variants of one base model must be served cost-effectively.

A. Deploy each as a separate full model
B. Serve one base model with multiple LoRA adapters loaded and selected per request
C. Merge them all into one model
D. Retrain a single model on everything

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Multi-LoRA serving keeps one copy of the base weights in memory and swaps small adapters per request, which is dramatically cheaper than one full deployment per variant. Merging adapters is appropriate when you want a single fixed behavior with no per-request switching.
</details>

---

### Question 13
**Scenario:** A model upgrade must be validated against the incumbent before rollout.

A. Ship and monitor
B. Run the evaluation suite (task accuracy, groundedness, safety, latency, cost) against both, then canary a small traffic share
C. Compare parameter counts
D. Compare benchmark scores published by the vendor

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Public benchmarks say little about your task distribution. An internal eval suite plus a canary gives evidence on both quality and operational characteristics before full exposure, and it catches regressions in behavior the new model is otherwise better at.
</details>

---

### Question 14
**Scenario:** GPU utilization sits at 40% during inference despite queued requests.

A. Add more GPUs
B. Profile with Nsight or Triton metrics to find the actual bottleneck: tokenization, host-device transfer, small batches, or CPU-side preprocessing
C. Increase the model size
D. Reduce the context window

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Low utilization with a queue means the GPU is starved, usually by CPU preprocessing, serialization, or a scheduling configuration that keeps batches small. Adding hardware to a pipeline bottleneck multiplies the idle capacity rather than fixing it.
</details>

---

### Question 15
**Scenario:** Guardrails must block a class of unsafe requests without harming legitimate use.

A. A blocklist of words
B. Layered controls: input classification, topical rails, output moderation, plus measurement of both violation rate and false refusal rate
C. Lower temperature
D. Shorter responses

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Safety is a trade-off curve, not a switch, so both directions must be measured: blocking more raises false refusals, which is a genuine product failure. Word blocklists are trivially evaded and catch benign text, which is why they perform badly on both axes.
</details>

---

## Where to go deeper

- [NCP-GENL cert page](../../exams/nvidia/genai-llms-professional/) - notes, practice plan, strategy
- [NCA-GENL practice questions](./nvidia-genai-llms-associate.md) - the associate level below this
- [Inference servers](../../learn/concepts/inference-servers.md) - serving in plain English
- [Quantization and distillation](../../learn/concepts/quantization-and-distillation.md) - making models smaller
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
