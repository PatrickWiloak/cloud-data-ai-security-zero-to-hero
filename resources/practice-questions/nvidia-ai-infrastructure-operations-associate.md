---
last-updated: 2026-08-09
difficulty: intermediate
---

# NVIDIA Certified Associate - AI Infrastructure Operations (NCA-AIIO) - Practice Questions

15 questions for NCA-AIIO prep, weighted toward GPU fundamentals and monitoring (25%) and container and runtime management (25%), then Kubernetes GPU operations (20%).

> **Cert page:** [exams/nvidia/ai-infrastructure-operations-associate/](../../exams/nvidia/ai-infrastructure-operations-associate/)

---

### Question 1
**Scenario:** You need current GPU utilization, memory use, temperature, and the processes using each GPU on a node.

A. `nvidia-smi`
B. `top`
C. `df -h`
D. `lspci`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `nvidia-smi` is the first tool for any GPU question: utilization, memory, power, temperature, ECC state, and the compute processes attached to each device. `nvidia-smi -l 1` loops it, and `dmon` gives a compact time series. `lspci` only confirms the card is present on the bus.
</details>

---

### Question 2
**Scenario:** Fleet-wide GPU health metrics must be exported to Prometheus with alerting.

A. NVIDIA DCGM with the DCGM exporter
B. `nvidia-smi` in a cron job
C. Node exporter alone
D. Grafana alone

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** DCGM is the managed monitoring layer for GPUs, providing health checks, diagnostics, and profiling metrics, and the DCGM exporter presents them to Prometheus. Node exporter has no GPU visibility, and Grafana visualizes data it is given rather than collecting it.
</details>

---

### Question 3
**Scenario:** A container must access the host's GPUs.

A. Install drivers inside the container
B. Use the NVIDIA Container Toolkit so the runtime injects the driver libraries and devices
C. Run the container as privileged with no other change
D. Mount `/dev` manually

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The toolkit's runtime hook exposes the devices and mounts the matching driver user-space libraries from the host, which is why the container ships CUDA runtime but not the driver. Installing a driver in the image would conflict with the host kernel module version.
</details>

---

### Question 4
**Scenario:** A CUDA application fails with a driver and runtime version mismatch.

A. Reinstall the application
B. The container's CUDA runtime requires a newer driver than the host provides; upgrade the host driver or use an image built for the installed driver
C. Reboot
D. Increase GPU memory

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The compatibility rule is that the driver must be at least as new as the CUDA runtime, and newer drivers support older runtimes. CUDA forward compatibility packages relax this on data center GPUs. Checking the driver version against the image's CUDA version is the fast diagnosis.
</details>

---

### Question 5
**Scenario:** Kubernetes must schedule pods onto GPU nodes and advertise GPU resources automatically.

A. The NVIDIA GPU Operator, which manages drivers, container toolkit, device plugin, and DCGM exporter
B. A DaemonSet running `nvidia-smi`
C. A node label only
D. The CNI plugin

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The GPU Operator installs and lifecycle-manages the whole GPU software stack on nodes, including the device plugin that advertises `nvidia.com/gpu` as a schedulable resource. Labeling alone tells the scheduler nothing about capacity.
</details>

---

### Question 6
**Scenario:** One A100 should be shared by several small inference workloads with hardware-level isolation.

A. Multi-Instance GPU (MIG), partitioning the GPU into isolated instances
B. Time-slicing
C. MPS
D. Running them sequentially

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** MIG partitions the GPU into instances with dedicated SMs, cache, and memory bandwidth, giving fault and performance isolation. Time-slicing shares the whole GPU by interleaving contexts with no memory isolation, and MPS allows concurrent kernels from multiple processes without hard isolation.
</details>

---

### Question 7
**Scenario:** A pod requests `nvidia.com/gpu: 1` and stays Pending.

A. Check for schedulable GPU nodes, whether the device plugin is running and advertising capacity, and whether taints or tolerations block placement
B. Increase the pod's memory
C. Restart the API server
D. Rebuild the image

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `kubectl describe node` shows whether `nvidia.com/gpu` appears under Capacity and Allocatable, which immediately separates "no GPU nodes" from "plugin not running" from "all GPUs already allocated." GPU nodes are also frequently tainted so that only GPU workloads land on them.
</details>

---

### Question 8
**Scenario:** What does NVLink provide compared with PCIe?

A. Higher bandwidth, lower latency GPU-to-GPU interconnect within a node
B. Network connectivity between nodes
C. Storage access
D. Display output

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** NVLink and NVSwitch create a high-bandwidth fabric between GPUs inside a server, which is what makes tensor parallelism practical. Between nodes the equivalent role is played by InfiniBand or high-speed Ethernet with RDMA.
</details>

---

### Question 9
**Scenario:** GPU memory is reported as full but no training job is running.

A. Check for orphaned processes holding memory (`nvidia-smi` process list), and reset the GPU if needed
B. Buy more GPUs
C. Reduce the batch size
D. Reinstall CUDA

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A crashed or zombie process can retain its CUDA context and memory. Identify it in the `nvidia-smi` process list and terminate it; `nvidia-smi --gpu-reset` is the escalation when no process is visible and the device is idle. This is one of the most common day-to-day GPU operations tickets.
</details>

---

### Question 10
**Scenario:** Which registry hosts NVIDIA's optimized containers for frameworks and models?

A. NGC (NVIDIA GPU Cloud) catalog
B. Docker Hub only
C. PyPI
D. Conda-forge

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** NGC provides tuned framework containers, Helm charts, pretrained models, and NIM microservices, versioned against specific CUDA and driver combinations. Using them avoids most of the version-matching problems in question 4.
</details>

---

### Question 11
**Scenario:** ECC errors are reported on a GPU.

A. Ignore them
B. Distinguish correctable from uncorrectable: correctable errors are handled but should be trended, while repeated uncorrectable errors mean the GPU should be drained and the vendor engaged
C. Reformat the node
D. Disable ECC permanently

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Correctable single-bit errors are expected at low rates. Uncorrectable errors corrupt computation and typically require row remapping or hardware replacement, so the operational response is to cordon and drain the node before it silently poisons a training run.
</details>

---

### Question 12
**Scenario:** A training job needs to be scheduled with other jobs on a shared cluster, with queueing and fair share.

A. NVIDIA Base Command or Slurm
B. `docker run`
C. systemd timers
D. cron

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Batch schedulers provide queues, priorities, fair-share accounting, and gang scheduling for multi-node jobs, which is what a shared GPU cluster needs. Running containers directly gives no queueing, so the cluster is allocated first-come-first-served by whoever types fastest.
</details>

---

### Question 13
**Scenario:** GPU utilization is high but the job is slow, and profiling shows most time in host-to-device copies.

A. The data pipeline is the bottleneck: increase dataloader workers, prefetch, use pinned memory, and consider GPUDirect Storage
B. Add more GPUs
C. Increase the learning rate
D. Reduce model size

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A GPU waiting on data is a data pipeline problem, and adding GPUs multiplies the starvation. Pinned memory enables asynchronous transfers, more workers keep the queue full, and GPUDirect Storage bypasses the host bounce buffer entirely for storage reads.
</details>

---

### Question 14
**Scenario:** Driver upgrades must be rolled out to a Kubernetes GPU fleet with minimal disruption.

A. Use the GPU Operator's driver upgrade support with node draining, one node pool at a time, validating before proceeding
B. Upgrade all nodes at once
C. Upgrade only the containers
D. Skip upgrades entirely

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Driver changes require workloads off the node, so cordon, drain, upgrade, validate, uncordon is the sequence, done in waves so a bad driver never takes the fleet. Staying on old drivers eventually blocks newer CUDA runtimes and leaves known bugs in place.
</details>

---

### Question 15
**Scenario:** An escalation must include enough evidence for NVIDIA support.

A. A description of the symptom only
B. `nvidia-bug-report.sh` output, driver and CUDA versions, `nvidia-smi -q` output, DCGM diagnostics, and the reproduction steps
C. A screenshot
D. The application source code

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The bug report script collects driver logs, kernel messages, and configuration in one bundle, and DCGM diagnostics distinguish hardware faults from software issues. Gathering this before escalating typically removes a full round trip.
</details>

---

## Where to go deeper

- [NCA-AIIO cert page](../../exams/nvidia/ai-infrastructure-operations-associate/) - notes, practice plan, strategy
- [NCP-AII practice questions](./nvidia-ai-infrastructure-professional.md) - the professional level above this
- [GPUs for AI](../../learn/concepts/gpus-for-ai.md) - VRAM, FLOPS, and bandwidth in plain English
- [CKA practice questions](./kubernetes-cka.md) - the Kubernetes baseline this assumes
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
