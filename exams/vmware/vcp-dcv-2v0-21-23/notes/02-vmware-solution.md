---
last-updated: 2026-07-29
---

# VCP-DCV Section 2 - The VMware Solution

vCenter, clustering services, vSAN, and the features that turn a set of hosts into a
managed platform.

## vCenter Server

- **vCenter Server Appliance (VCSA)** - the Photon OS-based appliance. The Windows version is discontinued, so VCSA is the only deployment form.
- **vCenter Single Sign-On (SSO)** - the authentication service issuing tokens for vSphere components.
- **vCenter Single Sign-On domain** - `vsphere.local` by default, distinct from your Active Directory domain. Confusing the two is a common error.
- **Enhanced Linked Mode** - multiple vCenter Servers sharing roles, permissions, licenses, tags, and policies, and manageable from one client view.
- **vCenter High Availability (VCHA)** - active, passive, and witness nodes protecting vCenter itself.
- **vCenter backup** - file-based backup to FTP, SFTP, HTTP, HTTPS, SMB, or NFS. This is the supported protection mechanism and is examined.

## Authentication and permissions

- **Identity source** - Active Directory over LDAP, OpenLDAP, or an external identity provider for federated authentication.
- **Permission model** - a permission is the combination of a **user or group**, a **role**, and an **object**, with an option to propagate to children.
- **Role** - a named set of privileges. Sample roles include Administrator, Read-only, and No access, plus sample roles for common jobs.
- **Propagation** - permissions applied to a parent object flow to children when propagate is enabled.
- **Effective permissions** - where multiple permissions apply, user permissions on an object override group permissions on that object, and permissions set on a child object override those inherited from a parent.

Global permissions apply across all inventory hierarchies, including in Enhanced Linked
Mode.

## Clusters and their services

- **Cluster** - the container on which HA, DRS, and vSAN are enabled.

**vSphere HA**

- **Purpose** - restart VMs after host, guest OS, or (with configuration) datastore failure. Downtime occurs; it is a restart, not continuity.
- **Master and subordinate hosts** - one host is elected master and monitors the others.
- **Heartbeat** - network heartbeats, with **datastore heartbeating** as a secondary channel to distinguish a failed host from an isolated one.
- **Host isolation** - a host that cannot reach the network but is still running. **Isolation response** options are leave powered on, power off, or shut down.
- **Admission control** - reserves capacity so that failover can actually succeed. Policies: cluster resource percentage, slot policy, or dedicated failover hosts. Disabling admission control allows more VMs but may leave insufficient capacity to restart them.
- **VM restart priority and dependencies** - ordering for restarts.
- **Proactive HA** - evacuates VMs from hosts a hardware vendor reports as degrading, before failure.
- **VM Component Protection (VMCP)** - responds to storage failures, specifically permanent device loss (PDL) and all-paths-down (APD).

**vSphere DRS**

- **Automation levels** - manual, partially automated (initial placement only), fully automated (placement and ongoing migration).
- **Migration threshold** - how aggressively DRS balances.
- **Affinity rules** - keep VMs together (affinity) or apart (anti-affinity), and VM-to-host rules with "should" (soft, best effort) or "must" (hard, enforced) semantics.
- **Predictive DRS** - uses vRealize/Aria Operations forecasting.

Anti-affinity separates VMs that must not fail together, such as two domain controllers.
"Must" rules are enforced even at the cost of availability, which is a real trade-off the
exam probes.

## Migration technologies

- **vMotion** - live compute migration. Requires shared visibility of the VM files or uses the migration network to copy them, plus a VMkernel adapter enabled for vMotion, and compatible CPUs (see EVC).
- **Storage vMotion** - live migration of VM files between datastores.
- **Cross-host and cross-datastore migration** - both compute and storage at once.
- **Cross vCenter vMotion** - between vCenter instances.
- **Long-distance vMotion** - supported up to defined round-trip latency limits.
- **Cold migration** - the VM is powered off; the fewest requirements.

## vSAN

- **vSAN** - hyperconverged storage pooling local host devices into a single datastore, enabled at cluster level.
- **Disk group** - one cache device plus one or more capacity devices, in the original architecture. Newer Express Storage Architecture (ESA) uses a single-tier pool.
- **Storage policy-based management (SPBM)** - policies specify availability and performance requirements per VM or per disk, and vSAN places data to satisfy them.
- **Failures to tolerate (FTT)** - how many host failures the data survives. FTT=1 with RAID-1 mirroring needs 3 hosts; RAID-5 erasure coding needs 4; RAID-6 needs 6.
- **Witness** - a component providing quorum, and a dedicated witness host or appliance in stretched and two-node clusters.
- **Stretched cluster** - a cluster split across two sites with a witness at a third.
- **Deduplication and compression** - space efficiency, available on all-flash configurations.

FTT drives the host count. Questions giving a required FTT and asking for minimum hosts
are common.

## Content and lifecycle

- **Content Library** - a repository of templates, ISOs, and scripts, which can be published and subscribed to across sites and vCenters.
- **VM template** - a non-runnable master image for deploying VMs.
- **Clone versus template** - a clone is a copy made now; a template is a master intended for repeated deployment.
- **Guest customization specification** - applies hostname, network settings, and domain join during deployment.
- **vSphere Lifecycle Manager (vLCM)** - manages ESXi images and firmware for a cluster using a desired-state image, replacing the older baseline approach from Update Manager.

## Exam pointers

- HA restarts, FT continues, DRS balances. Do not mix them up.
- Admission control exists to guarantee failover capacity; disabling it risks failed restarts.
- Datastore heartbeating distinguishes host failure from network isolation.
- FTT and the RAID type determine the minimum vSAN host count.
- vCenter is protected by file-based backup and optionally VCHA.
- Permissions: user overrides group on the same object; child overrides inherited parent.
- vLCM uses desired-state images; Update Manager baselines are the legacy approach.

## Official documentation

**[📖 vSphere availability](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere.html)** - HA, FT, and DRS reference
**[📖 vSAN documentation](https://techdocs.broadcom.com/us/en/vmware-cis/vsan.html)** - architecture and policies
**[📖 vCenter Server installation and setup](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere.html)** - VCSA deployment
