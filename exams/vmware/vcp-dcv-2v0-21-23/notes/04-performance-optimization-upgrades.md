---
last-updated: 2026-07-29
---

# VCP-DCV Section 4 - Performance, Optimisation, and Upgrades

Resource management, the metrics that identify a bottleneck, and how to upgrade the stack
in the right order.

## Resource controls

- **Shares** - relative priority, applied only when there is contention. A VM with high shares gets no benefit on an idle host.
- **Reservation** - a guaranteed minimum of CPU (MHz) or memory (MB). Reserved resources are unavailable to others even when idle, and reservations affect HA admission control calculations.
- **Limit** - a hard cap. The VM cannot exceed it even when resources are free. Limits are a frequent cause of unexplained poor performance and should be used sparingly.
- **Resource pool** - applies shares, reservations, and limits to a group of VMs.
- **Expandable reservation** - allows a child pool to borrow unreserved capacity from its parent.

A VM performing badly while the host shows plenty of free capacity almost always means a
limit, or a resource pool with insufficient allocation.

## Key performance metrics

**CPU**

- **%RDY (ready time)** - percentage of time a vCPU was ready to run but waiting for a physical core. Sustained high ready time means CPU contention or too many vCPUs. The primary CPU metric.
- **%CSTP (co-stop)** - time a multi-vCPU VM waited for its vCPUs to be co-scheduled. High co-stop means the VM has too many vCPUs for the host's load.
- **%MLMTD** - time not run because of a configured limit.
- **Usage** - simple utilisation, less diagnostic than ready time.

**Memory**

- **Active memory** - what the guest is actually touching.
- **Consumed** - physical host memory backing the VM.
- **Balloon (vmmemctl)** - memory reclaimed by the balloon driver. Non-zero means the host is under memory pressure.
- **Swap in/out** - host-level swapping. The clearest sign of serious memory over-commitment and the worst for performance.
- **Compressed** - pages compressed rather than swapped.

Ballooning is a warning; host swapping is an emergency.

**Storage**

- **Latency (GAVG)** - total guest-observed latency, made up of **KAVG** (kernel, should be near zero) and **DAVG** (device/array). High DAVG points at the array or fabric; high KAVG points at queuing on the host.
- **Queue depth and QUED** - outstanding I/O waiting.
- **Aborts and resets** - severe storage problems.

Splitting GAVG into KAVG and DAVG is how you decide whether the storage team or the
virtualisation team owns the problem. That reasoning is examined.

**Network**

- **Dropped packets (droppedRx/droppedTx)** - buffer or capacity problems.
- **Usage** - throughput per adapter.

## Tools

- **vSphere Client performance charts** - real-time and historical, with overview and advanced views.
- **esxtop / resxtop** - the live command-line tool on the host. Press `c` for CPU, `m` for memory, `d` for disk adapter, `u` for disk device, `v` for disk VM, `n` for network. This key mapping is worth memorising.
- **vm-support** - collects a diagnostic bundle for VMware support.
- **Aria Operations (formerly vRealize Operations)** - long-term analytics, capacity planning, and right-sizing recommendations.

## Optimisation practice

- **Right-size VMs** - allocate the vCPUs and memory actually needed. Over-allocation harms performance through co-scheduling and NUMA effects.
- **NUMA awareness** - keep a VM's vCPU and memory within a single NUMA node where possible. A VM larger than one node becomes a wide VM and pays a remote-memory penalty.
- **Paravirtual devices** - VMXNET3 and PVSCSI reduce overhead, and require VMware Tools.
- **VMware Tools current** - drivers and balloon driver depend on it.
- **Snapshot hygiene** - snapshots are not backups. They grow, they degrade I/O performance as the delta chain lengthens, and long-lived snapshots are a common cause of both poor performance and full datastores.
- **Storage tiering and Storage DRS** - keep latency within targets.
- **Network I/O Control (NIOC)** - allocates bandwidth by traffic type on a distributed switch.

Snapshots being mistaken for backups is a recurring exam theme, both in performance and in
troubleshooting.

## Upgrades

**Order matters.** Upgrade from the top of the stack down:

1. **vCenter Server** first. A newer ESXi cannot be managed by an older vCenter.
2. **ESXi hosts** next, one at a time, evacuating each with vMotion and maintenance mode.
3. **VMware Tools** in the guests.
4. **Virtual hardware version** last, which requires a VM power cycle.

Doing Tools before hardware version matters: upgrading hardware version first can leave the
guest without drivers.

- **Maintenance mode** - evacuates or requires shutdown of VMs before host work. DRS automates the evacuation in a fully automated cluster.
- **vSphere Lifecycle Manager (vLCM)** - desired-state cluster images covering ESXi, drivers, and firmware, replacing the older baseline model.
- **Pre-upgrade checks** - interoperability matrix, compatibility guide, and configuration backup.
- **Rollback** - ESXi retains the previous image bank, so a failed upgrade can be reverted by pressing Shift+R at boot.

## Exam pointers

- High %RDY means CPU contention; high %CSTP means too many vCPUs.
- Ballooning signals memory pressure; host swapping signals severe over-commitment.
- Split GAVG into KAVG (host queuing) and DAVG (array) to locate a storage bottleneck.
- Upgrade order: vCenter, then ESXi, then VMware Tools, then virtual hardware.
- Snapshots are not backups, and long-lived snapshots degrade performance and consume space.
- Learn the esxtop keys: c, m, d, u, v, n.

## Official documentation

**[📖 vSphere resource management](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere.html)** - shares, reservations, limits, NUMA
**[📖 vSphere upgrade](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere.html)** - supported upgrade sequence
**[📖 VMware product interoperability matrix](https://interopmatrix.broadcom.com/Interoperability)** - version compatibility
