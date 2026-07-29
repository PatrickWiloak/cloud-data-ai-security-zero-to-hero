---
last-updated: 2026-07-29
---

# VCP-DCV Section 5 - Troubleshooting and Repairing

Diagnosing the common failures, and knowing which log to read.

## Method

1. Establish scope: one VM, one host, one cluster, or everything.
2. Check recent change. Most faults follow a change.
3. Check dependencies bottom-up: physical, storage, network, host, VM.
4. Read the relevant log rather than guessing.
5. Verify the fix and document it.

## Logs worth knowing

| Log | Location | Contains |
|---|---|---|
| `vmkernel.log` | `/var/log/` | VMkernel, storage, and device events |
| `hostd.log` | `/var/log/` | Host management agent, most host-side operations |
| `vpxa.log` | `/var/log/` | vCenter agent on the host |
| `vobd.log` | `/var/log/` | Observed events and alarms |
| `vmware.log` | VM's datastore folder | Per-VM events, in the VM directory itself |
| `vpxd.log` | vCenter appliance | vCenter server operations |

The per-VM `vmware.log` living beside the VM's files, not in `/var/log`, is a detail worth
remembering.

- **Syslog forwarding** - ESXi logs should be sent to a central collector, because local logs are limited and may be lost.
- **vm-support / vc-support** - diagnostic bundle collection.

## Host problems

- **Host disconnected from vCenter** - check network to the management VMkernel, then restart the management agents from the DCUI or with `services.sh restart`. The VMs keep running while the host is disconnected; disconnection is a management-plane problem, not a workload outage.
- **Host not responding versus disconnected** - "not responding" means vCenter lost contact unexpectedly; "disconnected" means an administrator removed it.
- **PSOD (purple screen of death)** - a VMkernel panic. Record the screen, collect the core dump, and check hardware and driver compatibility. Usually hardware, firmware, or a driver fault.
- **Host isolation** - the host is running but cannot reach the isolation address. HA applies the configured isolation response.
- **Time drift** - breaks certificate validation and SSO. Check NTP.

## VM problems

- **VM will not power on** - common causes: insufficient host resources, a reservation that cannot be satisfied, a locked file from an ungraceful shutdown or an existing lock by another host, a missing or corrupt `.vmdk`, or a full datastore.
- **Locked file** - shown as "unable to access file since it is locked." Identify the host holding the lock and release it.
- **VM performance poor** - check %RDY, ballooning, swapping, and storage latency, in that order.
- **VMware Tools not running** - breaks graceful shutdown, time sync, quiescing, and paravirtual drivers.
- **Snapshot consolidation needed** - a warning that delta disks remain after a failed snapshot removal. Consolidate promptly; delta chains degrade performance and consume space.
- **Full datastore** - a very common root cause, frequently caused by thin disks growing or by forgotten snapshots.

## Storage problems

- **APD (All Paths Down)** - the host has lost all paths to a device but the array has not said the device is gone. The host keeps retrying, hoping it returns.
- **PDL (Permanent Device Loss)** - the array has explicitly signaled the device is gone permanently.
- **VMCP (VM Component Protection)** - configures HA's response to APD and PDL conditions, including restarting affected VMs elsewhere.
- **Path thrashing** - two hosts alternately claiming ownership of a LUN on an active/passive array, usually caused by a wrong path selection policy.
- **High DAVG** - array or fabric latency, escalate to the storage team.
- **High KAVG** - host queuing, check queue depth and multipathing.
- **Datastore full** - clear snapshots, expand the datastore, or Storage vMotion VMs away.

APD is temporary and retried; PDL is permanent and declared by the array. That distinction
is directly examined.

## Network problems

- **VM has no connectivity** - check port group VLAN ID, uplink assignment, physical switch trunking, and teaming policy in that order.
- **VLAN mismatch** - the most common cause. The port group VLAN must match the physical switch configuration.
- **IP hash without EtherChannel** - configured teaming that the physical switch does not match, producing intermittent or total loss.
- **vMotion fails** - check the vMotion-enabled VMkernel adapter on both hosts, IP connectivity between them, MTU consistency if jumbo frames are used, and CPU compatibility (EVC).
- **MTU mismatch** - jumbo frames configured on some elements but not all; large frames silently dropped while small pings succeed.

## Cluster problems

- **HA configuration error** - often DNS resolution, management network redundancy warnings, or insufficient heartbeat datastores.
- **Insufficient failover resources** - admission control preventing a power-on because the cluster could not guarantee restart capacity.
- **DRS not balancing** - check the automation level, migration threshold, and whether "must" affinity rules are constraining placement.
- **vSAN health warnings** - use the built-in vSAN health checks; component and object status indicate whether policy compliance is met.

## Backup and restore

- **vCenter file-based backup and restore** - the supported path for vCenter recovery.
- **VM backup** - via vStorage APIs for Data Protection (VADP) using a backup product with changed block tracking. Snapshots are a mechanism inside this, not a backup themselves.
- **Changed Block Tracking (CBT)** - lets backup software copy only changed blocks.

## Exam pointers

- `vmware.log` is in the VM's folder on the datastore; host logs are in `/var/log`.
- A disconnected host does not stop its VMs; restart management agents.
- APD is transient, PDL is permanent and array-declared.
- A locked file usually follows an ungraceful shutdown or a host still holding the lock.
- vMotion failures: VMkernel service enabled, network reachability, MTU, and CPU compatibility.
- Snapshots are not backups, and unconsolidated deltas cause both performance and space problems.

## Official documentation

**[📖 vSphere troubleshooting](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere.html)** - diagnostic procedures
**[📖 ESXi log file locations](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere.html)** - log reference
**[📖 Broadcom support knowledge base](https://knowledge.broadcom.com/)** - specific error resolution
