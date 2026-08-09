---
last-updated: 2026-08-09
difficulty: advanced
---

# NVIDIA Certified Professional - Networking (NCP-NET) - Practice Questions

15 questions for NCP-NET prep, weighted toward InfiniBand (25%), Spectrum Ethernet (20%), RDMA and RoCE (20%), and UFM fabric management (20%).

> **Cert page:** [exams/nvidia/networking-professional/](../../exams/nvidia/networking-professional/)

---

### Question 1
**Scenario:** Which component assigns LIDs and computes routing tables in an InfiniBand fabric?

A. The subnet manager
B. The DHCP server
C. BGP
D. The spine switch

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** InfiniBand is a managed fabric: the subnet manager discovers the topology, assigns local identifiers, and programs forwarding tables. It can run on a switch or a host, and a fabric with no active subnet manager does not pass traffic at all, which is the first thing to check on a dead fabric.
</details>

---

### Question 2
**Scenario:** What does RDMA provide that TCP/IP sockets do not?

A. Encryption
B. Direct memory-to-memory transfer with kernel bypass and near-zero CPU involvement
C. Higher MTU
D. Routing

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RDMA writes into remote memory without the receiving CPU copying buffers through the kernel, which removes both latency and CPU overhead. That is why it matters at scale: with sockets, the CPUs become the bottleneck of a collective operation long before the wire does.
</details>

---

### Question 3
**Scenario:** RoCEv2 is deployed and throughput collapses under load with high retransmission counts.

A. Increase MTU only
B. The fabric is not lossless: verify PFC is configured on the correct priority end to end, and that ECN marking and DCQCN are tuned
C. Replace the NICs
D. Disable RDMA

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RoCE assumes losslessness, and go-back-N recovery makes even small loss rates catastrophic for throughput. PFC must be consistent on every hop for the priority carrying RoCE traffic, and ECN with DCQCN handles congestion before PFC pause frames start causing head-of-line blocking.
</details>

---

### Question 4
**Scenario:** A rail-optimized topology is chosen for a GPU cluster. What does that mean?

A. All GPUs share one NIC
B. Each GPU is associated with its own NIC and switch plane, so same-rank traffic across nodes stays within one rail
C. Switches are stacked physically
D. Only one switch is used

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Collectives such as all-reduce exchange between corresponding ranks across nodes, so putting each rank on its own rail keeps that traffic on a dedicated plane and avoids cross-rail contention. It also localizes failure: a rail outage degrades rather than halts the fabric.
</details>

---

### Question 5
**Scenario:** Which topology provides non-blocking bandwidth between any pair of endpoints at scale?

A. A ring
B. A fat-tree (Clos) with full bisection bandwidth
C. A single switch chain
D. A star with oversubscription

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A fat-tree provisions enough uplink capacity at each tier that any permutation of traffic can be carried, which is what all-to-all collectives demand. Oversubscribed designs are cheaper and fine for general datacenter traffic but throttle synchronized training.
</details>

---

### Question 6
**Scenario:** GPUDirect RDMA must work between nodes.

A. Only a driver update is needed
B. The NIC and GPU must share a PCIe path with peer-to-peer support, the correct drivers must be loaded, and the topology should place them under the same PCIe switch or root complex
C. It works automatically over any network
D. It requires Ethernet only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Peer-to-peer DMA depends on PCIe topology, so a NIC and GPU on different root complexes may fall back to staging through host memory and lose most of the benefit. `nvidia-smi topo -m` shows the affinity matrix, which is how you verify the pairing before blaming the fabric.
</details>

---

### Question 7
**Scenario:** Which tool monitors InfiniBand fabric health, congestion, and cable errors?

A. NVIDIA UFM
B. DCGM
C. Prometheus alone
D. `nvidia-smi`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** UFM provides subnet management, real-time telemetry, congestion analysis, and cable and port diagnostics across the fabric, with alerting on error counter thresholds. DCGM and `nvidia-smi` see GPUs, not the network between them.
</details>

---

### Question 8
**Scenario:** Symbol errors are rising on one InfiniBand port.

A. Ignore them if throughput looks fine
B. Investigate the physical layer: reseat or replace the cable or transceiver, check the port counters on both ends, and isolate the link if errors persist
C. Reboot the switch
D. Reduce the link speed permanently

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Rising symbol and link-downed counters are the classic signature of a marginal cable or optic, and a degraded link silently slows every collective that crosses it. Reducing speed masks the fault rather than fixing it, and one bad link can pace an entire training job.
</details>

---

### Question 9
**Scenario:** SHARP is enabled on the fabric. What does it do?

A. Encrypts traffic
B. Performs in-network aggregation of collective operations in the switches, reducing data movement and latency
C. Compresses packets
D. Provides routing

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Scalable Hierarchical Aggregation and Reduction Protocol offloads reduction operations to the switch hierarchy, so partial sums are combined in the network rather than every value traversing to every endpoint. It measurably shortens all-reduce time at scale.
</details>

---

### Question 10
**Scenario:** Adaptive routing is enabled in an InfiniBand fabric.

A. Packets always follow the shortest static path
B. Traffic is dynamically distributed across alternative paths based on congestion, improving utilization in a fat-tree
C. It disables the subnet manager
D. It applies only to Ethernet

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Static routing can create hotspots when several flows hash to the same path. Adaptive routing spreads them, which matters for the bursty synchronized patterns of distributed training. Applications must tolerate potential out-of-order delivery, which InfiniBand transport handles.
</details>

---

### Question 11
**Scenario:** Spectrum switches are managed with Cumulus Linux. What is the operational model?

A. A proprietary CLI only
B. A Linux-based network operating system where standard tooling, automation, and NVUE or Linux commands configure the switch
C. Manual cabling only
D. Windows-based management

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cumulus treats the switch as a Linux host, so configuration management tools and the same automation practices used for servers apply. That is the operational argument for it: one toolchain across compute and network rather than two.
</details>

---

### Question 12
**Scenario:** A DPU (BlueField) is deployed in the cluster. What is its purpose?

A. Additional GPU compute
B. Offloading networking, storage, and security functions from the host CPU onto the network adapter, with its own cores and isolation
C. A display adapter
D. A storage array

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A DPU runs infrastructure services (virtual switching, encryption, storage virtualization, telemetry) on the adapter, freeing host cores for application work and creating a control boundary the tenant OS cannot reach. That isolation property is why it appears in multi-tenant AI cloud designs.
</details>

---

### Question 13
**Scenario:** Congestion control must prevent one heavy flow starving others on a RoCE fabric.

A. Nothing is needed
B. ECN marking with DCQCN, tuned thresholds, and PFC as a last-resort backstop rather than the primary mechanism
C. PFC alone
D. Larger buffers only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** ECN signals congestion early so senders slow down gradually, while PFC pauses entire priority classes and can spread congestion backward through the fabric, causing head-of-line blocking and in bad cases pause storms. Correct designs rely on ECN and treat PFC as the safety net.
</details>

---

### Question 14
**Scenario:** A new cluster must be validated before production.

A. Ping tests
B. Fabric verification: link speed and width on every port, error counter baselines, point-to-point bandwidth and latency tests, and full-scale NCCL all-reduce benchmarks
C. Visual inspection
D. Trust the installer

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Ping proves reachability and nothing about bandwidth. A link that negotiated a lower width, one bad optic, or a missing PFC configuration will pass ping and destroy training performance, so measure per-link and then measure the collective that the cluster exists to run.
</details>

---

### Question 15
**Scenario:** Choosing between InfiniBand and Ethernet for a new AI fabric.

A. Ethernet is always better
B. InfiniBand offers lossless transport, adaptive routing, and SHARP natively; Ethernet with RoCE can be competitive but requires careful lossless configuration and brings existing operational familiarity
C. InfiniBand cannot scale
D. They are identical

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The honest comparison is about built-in guarantees versus operational familiarity and ecosystem. InfiniBand gets lossless behavior and in-network aggregation by design; RoCE gets there with configuration discipline across every hop, which is where deployments most often go wrong.
</details>

---

## Where to go deeper

- [NCP-NET cert page](../../exams/nvidia/networking-professional/) - notes, practice plan, strategy
- [NCP-AII practice questions](./nvidia-ai-infrastructure-professional.md) - cluster design in context
- [Networking topic index](../../topics/networking.md) - cross-cloud networking
- **[📖 NVIDIA training and certification](https://www.nvidia.com/en-us/training/)** - official exam pages
