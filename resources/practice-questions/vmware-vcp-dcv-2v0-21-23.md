---
last-updated: 2026-08-09
difficulty: advanced
---

# VMware Certified Professional - Data Center Virtualization (VCP-DCV 2V0-21.23) - Practice Questions

15 questions on vSphere 8 administration: ESXi and vCenter, virtual machines, networking with standard and distributed switches, storage, resource management, and availability with HA and DRS.

> **Cert page:** [exams/vmware/vcp-dcv-2v0-21-23/](../../exams/vmware/vcp-dcv-2v0-21-23/)

---

### Question 1
**Scenario:** What is the relationship between ESXi and vCenter Server?

A. They are the same product
B. ESXi is the hypervisor running on physical hosts; vCenter is the central management plane for many ESXi hosts and their features
C. vCenter is a hypervisor
D. ESXi manages vCenter

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** ESXi runs the VMs; vCenter is what enables the cluster-level features - vMotion, HA, DRS - that require coordination across hosts. A host can run standalone, but the advanced features need vCenter.
</details>

---

### Question 2
**Scenario:** A running VM must move to another host with no downtime.

A. Power it off and migrate
B. vMotion, which migrates a running VM's compute state between hosts while it keeps running
C. Clone it
D. Storage vMotion only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** vMotion moves the live memory and execution state; Storage vMotion moves the disk files between datastores. The prerequisites are examinable: compatible CPUs or EVC, shared visibility of the VM, and a vMotion-enabled network.
</details>

---

### Question 3
**Scenario:** Which feature restarts VMs on surviving hosts after a host failure?

A. DRS
B. vSphere HA, which restarts the failed host's VMs on other hosts in the cluster
C. vMotion
D. Fault Tolerance

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** HA is recovery, not prevention: there is a brief outage while VMs restart elsewhere. Fault Tolerance is the zero-downtime alternative, running a shadow VM in lockstep, at the cost of much higher overhead and tight limits.
</details>

---

### Question 4
**Scenario:** Which feature balances VM load across hosts automatically?

A. HA
B. DRS, which uses vMotion to distribute VMs according to resource use and configured automation level
C. Storage DRS only
D. vMotion alone

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** DRS makes placement and balancing decisions; at the fully automated level it acts without prompting. Storage DRS is the datastore-cluster equivalent, balancing capacity and I/O across datastores.
</details>

---

### Question 5
**Scenario:** A distributed switch is preferred over standard switches in a large cluster.

A. They are equivalent
B. A vSphere Distributed Switch is configured once at vCenter and spans all hosts, giving consistent configuration and advanced features that per-host standard switches lack
C. Standard switches span hosts
D. Distributed switches are per host

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Standard switches are configured per host, so a mismatch between hosts breaks vMotion networking. The distributed switch centralizes it and adds features like network I/O control and port mirroring, which is why it is the choice at scale.
</details>

---

### Question 6
**Scenario:** Which storage protocol presents block storage to ESXi over an IP network?

A. NFS
B. iSCSI, presenting LUNs formatted with VMFS over TCP/IP
C. Fibre Channel only
D. SMB

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** iSCSI and Fibre Channel are block protocols carrying VMFS; NFS is file-level and mounted directly without VMFS. Knowing which protocol yields VMFS versus a direct mount matters for how multipathing and datastore features behave.
</details>

---

### Question 7
**Scenario:** Which VMware storage technology aggregates local host disks into a shared datastore?

A. VMFS on a SAN
B. vSAN, which pools local storage across cluster hosts into a single datastore governed by storage policies
C. NFS
D. Raw device mapping

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** vSAN is the hyperconverged option, removing the external array and using host-local disks. Storage Policy Based Management is central: policies such as failures-to-tolerate determine how data is placed and protected, rather than manual LUN design.
</details>

---

### Question 8
**Scenario:** A VM needs guaranteed access to a minimum amount of CPU or memory.

A. Increase the VM's vCPU count
B. A resource reservation, guaranteeing a minimum, alongside limits and shares for contention
C. A larger host
D. Affinity rules

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Reservations guarantee, limits cap, and shares set relative priority only when resources are contended. Over-using reservations is a common mistake, because reserved-but-idle resources cannot be used by anything else and reduce consolidation.
</details>

---

### Question 9
**Scenario:** A point-in-time copy of a VM must be taken before a risky change.

A. A clone
B. A snapshot, capturing the VM's state and data so it can be reverted, understanding that snapshots are not backups
C. A template
D. A backup only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Snapshots are for short-term revert, and long-lived or chained snapshots grow, hurt performance, and risk datastore fill. The exam and practice both stress that a snapshot depends on the base disk and is therefore not a backup.
</details>

---

### Question 10
**Scenario:** A standardized VM must be deployed repeatedly.

A. Clone a running VM each time
B. A template, a non-runnable master image deployed to new VMs, optionally customized with a guest customization specification
C. A snapshot
D. Manual installation

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Templates cannot be powered on, which prevents drift in the master. Guest customization sets a unique hostname, network identity, and SID on deployment, which is what stops identity collisions from cloned machines.
</details>

---

### Question 11
**Scenario:** ESXi hosts must be patched consistently across a cluster.

A. Patch each host manually
B. vSphere Lifecycle Manager, using a desired image or baselines to remediate hosts, coordinated with maintenance mode
C. Reinstall ESXi
D. A script per host

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Lifecycle Manager's image-based model defines the whole host image (ESXi, drivers, firmware) as a desired state. Entering maintenance mode evacuates the host via DRS first, which is what makes rolling patching non-disruptive.
</details>

---

### Question 12
**Scenario:** Two VMs must never run on the same host for availability.

A. Nothing can enforce this
B. A DRS anti-affinity rule keeping the VMs on separate hosts
C. A resource pool
D. A reservation

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Anti-affinity separates VMs so a single host failure cannot take down both, which is how you protect a clustered application. Affinity rules do the opposite, keeping VMs together, for example to reduce inter-host traffic.
</details>

---

### Question 13
**Scenario:** A resource pool is used to divide cluster capacity between two teams.

A. Resource pools guarantee equal split always
B. Resource pools apportion cluster resources with shares, reservations, and limits, but misusing nested pools and shares can produce unexpected allocations
C. Pools are only for storage
D. Pools replace clusters

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Shares only take effect under contention and are relative, so a pool with more VMs can starve its members even with generous shares. This resource pool priority-pie behavior is a classic source of confusion the exam probes.
</details>

---

### Question 14
**Scenario:** What does entering maintenance mode on a host do in a DRS cluster?

A. Powers off the host immediately
B. Prevents new VMs being placed and, with DRS, migrates running VMs off the host so it can be serviced
C. Deletes the VMs
D. Nothing until reboot

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Maintenance mode is the safe path to servicing a host. Without fully automated DRS, the administrator may have to vMotion VMs manually before the host will enter the mode, which is a common operational gotcha.
</details>

---

### Question 15
**Scenario:** Which network feature isolates traffic types such as management, vMotion, and storage?

A. A single network for everything
B. VLANs and separate VMkernel adapters per traffic type, ideally on distinct networks, so management, vMotion, and storage do not contend
C. One VMkernel adapter
D. Fault Tolerance

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** VMkernel adapters carry host system traffic and each is tagged for a service. Isolating them protects latency-sensitive vMotion and storage from each other and from VM traffic, which is a baseline design practice rather than an optimization.
</details>

---

## Where to go deeper

- [VCP-DCV cert page](../../exams/vmware/vcp-dcv-2v0-21-23/) - notes, practice plan, strategy
- [Containers vs VMs](../../learn/concepts/containers-vs-vms.md) - where virtualization sits next to containers
- [Disaster recovery patterns](../architecture-patterns/disaster-recovery-patterns.md) - HA and FT in a broader resilience design
- **[📖 VMware certification](https://www.vmware.com/learning/certification.html)** - official exam guide
