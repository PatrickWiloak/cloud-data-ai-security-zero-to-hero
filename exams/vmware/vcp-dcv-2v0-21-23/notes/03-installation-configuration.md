---
last-updated: 2026-07-29
---

# VCP-DCV Section 3 - Installation, Configuration, and Setup

Deploying ESXi and vCenter, then configuring networking and storage.

## ESXi installation

- **Hardware requirements** - a supported 64-bit x86 CPU with hardware virtualisation enabled in firmware, the minimum RAM for the release, and a supported boot device. Always verify against the **VMware Compatibility Guide**; unsupported hardware is the first thing to check in a failed-install scenario.
- **Interactive installation** - from ISO via ILO/iDRAC virtual media or USB.
- **Scripted installation** - a **kickstart** file (`ks.cfg`) supplied by boot option, for repeatable deployment at scale.
- **Auto Deploy** - PXE-boots stateless hosts from an image profile held by vCenter. Suits large, uniform estates.
- **Boot device** - USB and SD cards are deprecated for the OSData partition in current releases; persistent local storage is expected.
- **DCUI (Direct Console User Interface)** - the console interface for initial configuration: management IP, hostname, DNS, root password, and restart of management agents.
- **Lockdown mode** - restricts direct host access so administration goes through vCenter. Normal lockdown permits DCUI access for defined users; strict lockdown disables the DCUI entirely, which can lock you out if vCenter is unavailable.

## vCenter Server deployment

- **Two-stage deployment** - stage 1 deploys the appliance OVA, stage 2 configures SSO and services.
- **Deployment size** - tiny through x-large, chosen by host and VM count. Undersizing causes performance problems that look like other faults.
- **Target** - deployed onto an ESXi host or an existing vCenter.
- **SSO domain** - create a new one or join an existing for Enhanced Linked Mode.
- **DNS** - forward and reverse records must exist and resolve correctly *before* deployment. DNS misconfiguration is the leading cause of failed vCenter deployments and is a reliable exam answer.
- **NTP** - time synchronisation is required; certificate validation and SSO token exchange fail with skew.

## Networking configuration

**Standard switch**

- Created per host, with port groups for VM traffic and VMkernel adapters for host traffic.
- **VMkernel adapter services** - management, vMotion, Fault Tolerance logging, vSAN, provisioning, and NFS/iSCSI.
- **VLAN tagging modes** - **EST** (external switch tagging, VLAN 0), **VST** (virtual switch tagging, the common choice, a VLAN ID on the port group), and **VGT** (virtual guest tagging, VLAN 4095, the guest handles tags).

**Distributed switch**

- Created in vCenter, hosts added as members, with **uplink port groups** mapping physical NICs.
- **Distributed port group** - policy applied consistently across all member hosts.
- **Features** - private VLANs, NetFlow, port mirroring, LACP, Network I/O Control, and health check.
- **Rollback and recovery** - vSphere reverts a network change that disconnects a host from vCenter, which is why VDS misconfiguration is usually recoverable.

**Policies (set on switch or port group; port group overrides switch)**

- **Security** - promiscuous mode, MAC address changes, and forged transmits. All should be Reject unless a specific need exists, such as a nested lab or an IDS appliance.
- **Teaming and failover** - load balancing method (originating virtual port, source MAC hash, IP hash, or physical NIC load on VDS), network failure detection, notify switches, and failback.
- **IP hash** requires a correctly configured static EtherChannel or LACP on the physical switch. Choosing IP hash without switch-side configuration breaks connectivity, and that mismatch is examined.
- **Traffic shaping** - average bandwidth, peak bandwidth, and burst size. Egress only on VSS; ingress and egress on VDS.

## Storage configuration

- **iSCSI** - software adapter, dependent hardware adapter, or independent hardware adapter. Configure targets (static or dynamic discovery), CHAP authentication, and port binding for multipathing.
- **Fibre Channel and FCoE** - zoning and LUN masking are done on the fabric and array.
- **NFS** - mount an export; NFS 4.1 supports multipathing and Kerberos, NFS 3 does not.
- **Multipathing (PSA/NMP)** - path selection policies are **Fixed**, **Most Recently Used (MRU)**, and **Round Robin**. Round Robin is the common default for active/active arrays.
- **Datastore creation** - VMFS6 on a LUN, or mounting NFS.
- **Datastore cluster** - a group of datastores managed by Storage DRS.
- **Storage I/O Control (SIOC)** - datastore-wide fairness under contention using shares and limits.

## VM creation and configuration

- **Virtual hardware version** - determines available features; upgrading requires a supported ESXi version and a power cycle.
- **Virtual disk controllers** - LSI Logic, and **PVSCSI** (paravirtual) for high-I/O workloads. **NVMe** controllers for very high performance.
- **Network adapters** - **VMXNET3** is the paravirtual default and requires VMware Tools. E1000e is emulated and used when drivers are unavailable during installation.
- **CPU and memory hot add** - allows increases while powered on, enabled per VM in advance, with guest OS support required.
- **VM options** - boot options, firmware (BIOS or EFI), and advanced parameters.
- **OVF and OVA** - open virtualisation packaging for import and export.

Choosing paravirtual devices (VMXNET3, PVSCSI) gives better performance but depends on
VMware Tools being installed, which is the trade-off the exam tests.

## Exam pointers

- Verify hardware against the VMware Compatibility Guide first in installation problems.
- DNS forward and reverse records must exist before vCenter deployment.
- VST (a VLAN ID on the port group) is the normal tagging mode; VGT uses VLAN 4095.
- Security policies should be Reject unless a documented exception applies.
- IP hash load balancing requires matching physical switch configuration.
- VMXNET3 and PVSCSI need VMware Tools.
- Strict lockdown mode disables DCUI access entirely.

## Official documentation

**[📖 vSphere installation and setup](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere.html)** - ESXi and vCenter deployment
**[📖 vSphere networking](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere.html)** - switches, port groups, policies
**[📖 VMware Compatibility Guide](https://compatibilityguide.broadcom.com/)** - supported hardware
