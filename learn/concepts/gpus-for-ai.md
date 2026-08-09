---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 8 min
---

# GPUs for AI

> **8-minute read. Assumes you've read [LLM basics](./llm-basics.md).**

## The one-line answer

Training and running neural networks is mostly matrix multiplication, which is the same simple operation repeated across enormous amounts of data. A GPU has thousands of small cores that do exactly that in parallel, so it is dramatically faster than a CPU for this specific shape of work.

## Why not a CPU

A CPU has a few dozen powerful cores optimized for sequential work with unpredictable branches: running an operating system, serving requests, executing business logic. Each core is sophisticated and expensive.

A GPU has thousands of simpler cores designed to apply the same instruction across a lot of data simultaneously. That is a poor fit for a web server and an excellent fit for multiplying a 4096x4096 matrix.

The consequence: a task that takes a CPU a week can take a GPU cluster hours, and a task the GPU is bad at will run faster on a single CPU core.

## The vocabulary that appears on every spec sheet

| Term | Means | Why it matters |
|---|---|---|
| **VRAM** | Memory on the GPU itself | The hard limit on model size. If the model does not fit, it does not run |
| **Memory bandwidth** | How fast data moves between VRAM and the cores | Usually the real bottleneck for inference, not raw compute |
| **FLOPS** | Floating point operations per second | Headline compute figure, and often not the limiting factor |
| **Tensor cores** | Units specialized for matrix operations | Where most of the useful throughput comes from |
| **Interconnect** (NVLink, RDMA) | Speed of GPU-to-GPU and node-to-node communication | The bottleneck once training spans multiple devices |

The number that decides whether you can run a model at all is **VRAM**. The number that decides how fast it responds is usually **memory bandwidth**.

## How much memory a model needs

A rough rule for inference: multiply the parameter count by the bytes per parameter.

| Precision | Bytes per parameter | A 7B model needs | A 70B model needs |
|---|---|---|---|
| FP32 (full) | 4 | ~28 GB | ~280 GB |
| FP16 / BF16 (half) | 2 | ~14 GB | ~140 GB |
| INT8 | 1 | ~7 GB | ~70 GB |
| INT4 | 0.5 | ~3.5 GB | ~35 GB |

Then add overhead for activations and the **KV cache**, which grows with context length and concurrent requests, and can become the dominant memory consumer for long-context serving.

**Training needs several times more** than inference, because it also holds gradients and optimizer state. A rule of thumb is 3-4 times the inference figure for full fine-tuning, which is why parameter-efficient methods such as LoRA exist: they train a small set of additional weights and cut the memory requirement dramatically.

## Quantization

Storing weights at lower precision shrinks the model so it fits on smaller, cheaper hardware and moves less data per token, which also makes it faster.

The trade is accuracy. In practice INT8 is usually close to lossless for most tasks, and INT4 is noticeably degraded on some while remaining perfectly usable for others. Whether the degradation matters is an empirical question about your task, which is why you evaluate rather than assume.

See [Quantization and distillation](./quantization-and-distillation.md).

## Training versus inference

They are different workloads with different economics, which is why cloud providers price and provision them separately.

| | Training | Inference |
|---|---|---|
| Duration | Hours to months, one job | Continuous, many small requests |
| Memory | Weights plus gradients plus optimizer state | Weights plus KV cache |
| Scale | Often many GPUs across many nodes | Often one GPU, or part of one |
| Bottleneck | Interconnect between devices | Memory bandwidth |
| Interruption | Costly; needs checkpointing | Cheap; retry the request |
| Cost model | Reserved or spot capacity for a burst | Steady capacity, or per-token API |

Most people building with AI never train anything. Inference, and how efficiently you serve it, is where the money goes.

## Multi-GPU

When a model does not fit on one device, or training would take too long, work is split:

- **Data parallelism**: every GPU holds a full copy of the model and processes a different batch, synchronizing gradients. Simple, and requires the model to fit on one device.
- **Tensor parallelism**: a single layer's matrices are split across GPUs. Needed when the model does not fit, and very sensitive to interconnect speed.
- **Pipeline parallelism**: different layers on different GPUs, with batches flowing through.

All three make the **interconnect** the limiting factor, which is why high-end training clusters advertise NVLink between GPUs and RDMA networking between nodes. It is also why "how many GPUs" is a less useful question than "how are they connected".

## Serving efficiently

Naively running one request at a time wastes most of a GPU. Inference servers such as vLLM, TGI, and TensorRT-LLM improve throughput substantially through:

- **Continuous batching**: adding new requests to a running batch rather than waiting for the batch to finish
- **PagedAttention**: managing the KV cache in pages to avoid fragmentation and waste
- **Speculative decoding**: a small model proposes tokens that the large model verifies in parallel

The practical effect is several times more throughput from the same hardware, which is why serving framework choice matters as much as GPU choice.

See [Inference servers](./inference-servers.md).

## Do you need one at all

Be honest about this before buying anything:

- **Calling a hosted API** means no GPU, no capacity planning, per-token pricing. Right for most applications.
- **Renting cloud GPUs** suits bursty training and fine-tuning, and inference at moderate scale.
- **Owning hardware** starts to make sense at sustained high utilization, and comes with the obligations of operating it.
- **A local consumer GPU** is genuinely useful for learning and for running small models, and will not run frontier models.

The most common mistake is buying capacity for a workload that a hosted API would serve better and cheaper, because the utilization never materializes.

## What to look at next

- **[Quantization and distillation](./quantization-and-distillation.md)** - making models fit smaller hardware
- **[Inference servers](./inference-servers.md)** - getting throughput out of the GPU you have
- **[Context windows and management](./context-windows-and-management.md)** - why the KV cache grows
- **[Run Llama on a single GPU](../../resources/hands-on-projects/run-llama-on-single-gpu.md)** - a worked build
- **[NVIDIA certifications](../../exams/nvidia/)** - the vendor track covering this material in depth
