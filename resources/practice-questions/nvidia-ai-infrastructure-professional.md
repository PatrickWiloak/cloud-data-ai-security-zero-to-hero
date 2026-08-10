---
last-updated: 2026-08-09
difficulty: advanced
---

# NVIDIA Certified Professional - AI Infrastructure (NCP-AII) - Practice Questions

15 questions for NCP-AII prep, evenly weighted across DGX and GPU hardware, cluster design and networking, Kubernetes and GPU orchestration, job scheduling, and performance tuning (20% each).

> **Cert page:** [exams/nvidia/ai-infrastructure-professional/](../../exams/nvidia/ai-infrastructure-professional/)

---

### Question 1
**Scenario:** A DGX system's eight GPUs must communicate at full bandwidth for tensor-parallel training.

A. PCIe switching
B. NVLink with NVSwitch providing all-to-all GPU bandwidth within the node
C. InfiniBand
D. Ethernet

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** NVSwitch gives every GPU full-bandwidth access to every other GPU in the chassis, which is what makes intra-node tensor parallelism viable. InfiniBand is the inter-node fabric. PCIe is an order of magnitude slower and would make tensor parallelism a bottleneck rather than a technique.
</details>

---

### Question 2
**Scenario:** A multi-node training cluster is being designed for 64 nodes with 8 GPUs each.

A. A single top-of-rack switch
B. A rail-optimized fat-tree InfiniBand fabric with non-blocking bandwidth and one NIC per GPU rail
C. Standard 10 GbE
D. Wireless

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Collective operations at this scale need non-blocking bisection bandwidth, and rail-optimized designs put each GPU's traffic on its own rail so all-reduce traffic does not contend. A single switch cannot supply the port count, and commodity Ethernet without RDMA leaves the GPUs waiting on the network.
</details>

---

### Question 3
**Scenario:** What does GPUDirect RDMA enable?

A. Direct memory transfer between GPU memory and the network adapter, bypassing host memory
B. Faster local disk access
C. GPU virtualization
D. Display streaming

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Removing the host bounce buffer cuts latency and CPU overhead for inter-node GPU communication, which is what makes NCCL collectives scale. GPUDirect Storage is the sibling technology that does the same for NVMe reads into GPU memory.
</details>

---

### Question 4
**Scenario:** RoCE is used instead of InfiniBand. What must be configured for it to perform?

A. Nothing special
B. Lossless Ethernet: PFC for flow control and ECN for congestion notification, configured consistently end to end
C. Jumbo frames only
D. A separate VLAN only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RDMA assumes a lossless fabric, so priority flow control and explicit congestion notification must be enabled and tuned on every switch and NIC in the path. A single misconfigured hop causes packet loss that collapses RoCE throughput, which is why RoCE deployments fail in the middle rather than at the edges.
</details>

---

### Question 5
**Scenario:** A Slurm cluster must guarantee that all ranks of a distributed job start together.

A. Gang scheduling, so the job runs only when all requested nodes are simultaneously available
B. First-come-first-served per node
C. Backfill only
D. Preemption

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A distributed training job with some ranks running and others queued deadlocks at the first collective and burns the allocated GPUs doing nothing. Gang scheduling is the requirement; backfill is a complementary technique for filling gaps with small jobs.
</details>

---

### Question 6
**Scenario:** Storage must feed 512 GPUs reading a large image dataset.

A. A single NFS server
B. A parallel filesystem or high-throughput object store sized for aggregate bandwidth, with local NVMe caching on nodes
C. Local disk only
D. A cloud bucket over the internet

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** GPU clusters starve on storage long before they starve on compute, and aggregate read bandwidth is the number to size against. Node-local NVMe caching for repeated epochs is the standard multiplier. A single NFS head becomes the bottleneck well before this scale.
</details>

---

### Question 7
**Scenario:** MIG is enabled on a node in a Kubernetes cluster. How do workloads request a slice?

A. They request `nvidia.com/gpu`
B. They request the specific MIG profile resource advertised by the device plugin, such as `nvidia.com/mig-1g.10gb`
C. MIG is not supported in Kubernetes
D. They request CPU only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** In the mixed strategy the device plugin advertises each MIG profile as a distinct resource name, so pods request the slice size they need. The single strategy presents uniform slices as `nvidia.com/gpu` instead. Choosing the strategy is a cluster-level decision that affects every manifest.
</details>

---

### Question 8
**Scenario:** Training throughput is well below the theoretical FLOPS of the hardware.

A. Profile with Nsight Systems and Nsight Compute to find whether the job is compute bound, memory bound, communication bound, or input bound
B. Buy newer GPUs
C. Increase the learning rate
D. Reduce the model size

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Utilization percentage does not tell you why. Nsight Systems gives the timeline across CPU, GPU, and communication so you can see gaps, and Nsight Compute drills into individual kernels. Optimizing without profiling usually improves the part that was not the bottleneck.
</details>

---

### Question 9
**Scenario:** Mixed precision training is enabled and loss becomes NaN.

A. Disable mixed precision permanently
B. Use loss scaling (or BF16, which has the same exponent range as FP32) to prevent gradient underflow
C. Lower the batch size
D. Increase the epochs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** FP16 has limited exponent range, so small gradients underflow to zero and large activations overflow. Dynamic loss scaling shifts gradients into representable range. BF16 avoids the problem by trading mantissa bits for exponent range, which is why it is the default on modern hardware.
</details>

---

### Question 10
**Scenario:** A multi-tenant cluster must prevent one team from monopolizing GPUs.

A. Resource quotas per namespace, priority classes, and fair-share or partition limits in the scheduler
B. Trust the teams
C. One large namespace
D. Manual approval for every job

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Quotas cap consumption, priority classes decide who is preempted under contention, and scheduler fair-share prevents one account draining the queue over time. Manual approval does not scale and moves the bottleneck to a human.
</details>

---

### Question 11
**Scenario:** NCCL collectives are unexpectedly slow across nodes.

A. Set `NCCL_DEBUG=INFO` and check the selected transport, topology detection, and whether it fell back from RDMA to sockets
B. Restart the job
C. Reduce the model
D. Add more nodes

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** NCCL logs which transport and rings it chose, and a silent fallback to TCP sockets because RDMA was unavailable is the classic cause of a tenfold slowdown. Environment variables such as `NCCL_IB_HCA` and `NCCL_SOCKET_IFNAME` pin it to the right interfaces.
</details>

---

### Question 12
**Scenario:** Power and cooling must be planned for a rack of DGX systems.

A. Standard office power
B. Plan per-rack power draw and cooling capacity against the systems' rated consumption, including redundancy and possibly liquid cooling
C. Cooling is unnecessary
D. Use fewer GPUs per node

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Dense GPU racks reach power and heat densities that ordinary data center rows cannot support, and this constraint often decides the physical layout before anything else does. Facility limits are the reason many deployments end up with partially populated racks.
</details>

---

### Question 13
**Scenario:** A node's GPU fails mid-training in a 64-node run.

A. Restart from scratch
B. Resume from the most recent checkpoint on healthy nodes, with the failed node cordoned; use frequent checkpointing and elastic training where supported
C. Continue with 63 nodes and no changes
D. Ignore it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** At this scale hardware failure during a long run is expected rather than exceptional, so checkpoint frequency is a design parameter chosen against mean time between failures. Elastic frameworks can reconfigure the world size and continue, which turns a failure into a pause.
</details>

---

### Question 14
**Scenario:** Which tool manages and monitors an InfiniBand fabric?

A. NVIDIA UFM (Unified Fabric Manager)
B. DCGM
C. Nsight
D. NGC

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** UFM handles subnet management, fabric telemetry, congestion analysis, and cable and port health across the InfiniBand network. DCGM covers the GPUs themselves, so a healthy cluster needs both views.
</details>

---

### Question 15
**Scenario:** Benchmarking should validate a new cluster before handing it to users.

A. Run one training job
B. Run standard benchmarks at each layer: single-GPU compute, NCCL all-reduce bandwidth, storage throughput, and an end-to-end MLPerf-style training run
C. Check `nvidia-smi` only
D. Trust the vendor specification

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Layered benchmarking localizes a shortfall: if single-GPU numbers are right but all-reduce is slow, the fabric is at fault, and if both are right but the end-to-end run is slow, look at storage or the data pipeline. A single end-to-end number tells you something is wrong without telling you where.
</details>

---

## Where to go deeper

- [NCP-AII cert page](../../exams/nvidia/ai-infrastructure-professional/) - notes, practice plan, strategy
- [NCA-AIIO practice questions](./nvidia-ai-infrastructure-operations-associate.md) - the associate level below this
- [NCP-NET practice questions](./nvidia-networking-professional.md) - the fabric in depth
- [GPUs for AI](../../learn/concepts/gpus-for-ai.md) - the hardware concepts in plain English
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
