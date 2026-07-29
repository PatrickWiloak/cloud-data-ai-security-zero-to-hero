---
last-updated: 2026-07-29
---

# VCP-DCV Section 1 - Architectures and Technologies

The vSphere component model, licensing, and the virtualization concepts everything else
builds on.

## The core components

- **ESXi** - the type-1 (bare-metal) hypervisor installed directly on server hardware. It runs virtual machines; it is not an application on top of an operating system.
- **VMkernel** - the ESXi kernel, providing scheduling, memory management, and the network stack for host services.
- **vCenter Server** - the centralized management plane. Features such as vMotion, DRS, and HA are configured and coordinated here.
- **vSphere Client** - the HTML5 browser interface to vCenter.
- **VM (virtual machine)** - an encapsulated set of files: `.vmx` (configuration), `.vmdk` (virtual disk), `.nvram`, plus logs and snapshot files.
- **VMware Tools** - guest-side drivers and utilities. Required for graceful shutdown, time sync, quiescing for backups, and optimal driver performance. Missing Tools is a frequent root cause in troubleshooting scenarios.

Without vCenter, an ESXi host still runs VMs. Almost every advanced feature, however,
requires vCenter, which is why vCenter availability matters so much.

## Inventory structure

- **Datacenter object** - the top-level container; the boundary for vMotion without additional configuration.
- **Cluster** - a group of hosts sharing resources, and the object on which HA and DRS are enabled.
- **Resource pool** - a subdivision of cluster CPU and memory with its own shares, reservations, and limits.
- **Folder** - organizational grouping for VMs, hosts, networks, or datastores.
- **Tags and categories** - metadata for grouping and for storage-policy targeting.

## Virtualization fundamentals

- **Hypervisor type 1** - runs on the hardware directly (ESXi). Type 2 runs on a host OS (Workstation, Fusion).
- **vCPU** - a virtual CPU presented to a guest, scheduled onto physical cores.
- **CPU scheduling and co-stop** - a VM with many vCPUs must wait for enough physical cores to be simultaneously available. Over-provisioning vCPUs *degrades* performance, which is counter-intuitive and therefore examined.
- **Memory overcommitment** - allocating more virtual memory than the host physically has, relying on reclamation techniques.
- **Transparent page sharing (TPS)** - deduplicates identical memory pages. Restricted by default for security reasons in modern releases.
- **Ballooning** - the guest driver (part of VMware Tools) pressures the guest OS to release memory. The preferred reclamation technique because the guest chooses what to give up.
- **Memory compression** - compresses pages rather than swapping.
- **Host swapping** - the last resort, swapping to disk. Worst performance impact.

The reclamation order under pressure is TPS, ballooning, compression, then swapping.
Learn it in that order.

- **Shares, reservations, and limits** - shares set relative priority under contention, a reservation guarantees a minimum, a limit caps the maximum. Limits are the usual cause of a VM performing badly while the host looks idle.

## Storage concepts

- **Datastore** - a storage container for VM files.
- **VMFS** - VMware's clustered file system, allowing multiple hosts to access the same LUN concurrently. VMFS6 is the current version.
- **NFS datastore** - file-level storage; NFS 3 and 4.1 are supported, with 4.1 adding multipathing and Kerberos.
- **vSAN** - aggregates local host disks into a shared datastore, configured per cluster with storage policies.
- **VVols (Virtual Volumes)** - storage-array integration where each virtual disk is an array object, enabling per-VM array services.
- **Raw Device Mapping (RDM)** - a VM accessing a LUN directly. Used for clustering across physical hosts and for very large LUNs.
- **Thin provisioning** - allocates space on demand; risks over-commitment of the datastore.
- **Thick provision lazy zeroed** - space allocated up front, zeroed on first write.
- **Thick provision eager zeroed** - space allocated and zeroed at creation. Required for some clustering features, slowest to create.

## Networking concepts

- **vSphere Standard Switch (VSS)** - configured per host. Simple, but consistency across hosts is manual and error-prone.
- **vSphere Distributed Switch (VDS)** - configured centrally in vCenter and pushed to member hosts. Provides consistency plus advanced features such as NetFlow, port mirroring, LACP, and network I/O control. Requires the appropriate license.
- **Port group** - a policy template for a set of virtual ports, including VLAN, security, and teaming settings.
- **VMkernel adapter** - a host interface carrying management, vMotion, vSAN, or storage traffic.
- **Uplink (vmnic)** - a physical NIC attached to a virtual switch.
- **NIC teaming** - multiple uplinks for redundancy and load distribution.

## Availability and resource features

- **vSphere HA** - restarts VMs on surviving hosts after a host failure. It is a restart, so there is downtime; it is not fault tolerance.
- **vSphere Fault Tolerance (FT)** - runs a shadow VM in lockstep, providing zero-downtime failover, with strict limits on vCPU count and heavy network requirements.
- **DRS (Distributed Resource Scheduler)** - balances VM placement across hosts using vMotion, and makes initial placement decisions.
- **Storage DRS** - balances VMs across datastores in a datastore cluster by space and latency.
- **vMotion** - live migration of a running VM's compute between hosts, with no downtime.
- **Storage vMotion** - live migration of a VM's files between datastores.
- **DPM (Distributed Power Management)** - consolidates VMs and powers down unneeded hosts.
- **EVC (Enhanced vMotion Compatibility)** - masks CPU features to a common baseline so vMotion works across mixed CPU generations within the same vendor. It cannot bridge Intel and AMD.

HA restarts (downtime), FT continues (no downtime). This distinction appears on every
version of this exam.

## Licensing and editions

vSphere is licensed per CPU (with core-count considerations in current models), and
features are gated by edition: Standard, Enterprise Plus, and vSphere with Tanzu or VCF
bundles. Distributed switches, DRS, and Storage DRS require higher editions.

Check current licensing on VMware's site before the exam; licensing detail changes more
often than architecture.

## Exam pointers

- ESXi is type 1, installed on bare metal.
- Memory reclamation order: TPS, ballooning, compression, host swapping.
- Over-allocating vCPUs hurts performance because of co-scheduling.
- A resource *limit* causes poor VM performance even on an idle host.
- HA restarts VMs with downtime; FT provides continuous availability.
- EVC masks CPU features within one vendor; it does not allow Intel-to-AMD migration.
- VDS is centrally managed and license-gated; VSS is per host.

## Official documentation

**[📖 vSphere documentation](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere.html)** - product reference
**[📖 VCP-DCV certification](https://www.broadcom.com/support/education/vmware/certification)** - exam blueprint and requirements
