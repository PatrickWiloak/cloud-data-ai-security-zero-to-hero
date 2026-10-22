---
last-updated: 2026-10-22
difficulty: advanced
---

# VMware Certified Professional - Data Center Virtualization (VCP-DCV 2V0-21.23) - Practice Questions

30 questions on vSphere 8 administration: ESXi and vCenter, virtual machines, networking with standard and distributed switches, storage, resource management, and availability with HA and DRS.

> **Cert page:** [exams/vmware/vcp-dcv-2v0-21-23/](../../exams/vmware/vcp-dcv-2v0-21-23/)

---

### Question 1
**Scenario:** What is the relationship between ESXi and vCenter Server?

A. They are the same product
B. ESXi is the hypervisor on each physical host; vCenter is the central management plane for many hosts
C. ESXi manages vCenter
D. vCenter is a bare-metal hypervisor that runs VMs directly, with ESXi as its web client

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
C. Storage vMotion, which moves the VM's disk files between datastores
D. Clone it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** vMotion moves the live memory and execution state; Storage vMotion moves the disk files between datastores. The prerequisites are examinable: compatible CPUs or EVC, shared visibility of the VM, and a vMotion-enabled network.
</details>

---

### Question 3
**Scenario:** Which feature restarts VMs on surviving hosts after a host failure?

A. Fault Tolerance, which runs a lockstep shadow VM so a failed host's workload continues, though it restarts nothing elsewhere
B. vMotion, which moves a running VM between hosts at the administrator's request
C. vSphere HA, which restarts failed host's VMs on other hosts
D. DRS, which rebalances running VMs by resource use, not by host failure

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** HA is recovery, not prevention: there is a brief outage while VMs restart elsewhere. Fault Tolerance is the zero-downtime alternative, running a shadow VM in lockstep, at the cost of much higher overhead and tight limits.
</details>

---

### Question 4
**Scenario:** Which feature balances VM load across hosts automatically?

A. vMotion alone
B. Storage DRS only, which balances datastore capacity and I/O latency across a datastore cluster using Storage vMotion
C. DRS, which uses vMotion to distribute VMs according to resource use and configured automation level
D. HA

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** DRS makes placement and balancing decisions; at the fully automated level it acts without prompting. Storage DRS is the datastore-cluster equivalent, balancing capacity and I/O across datastores.
</details>

---

### Question 5
**Scenario:** A distributed switch is preferred over standard switches in a large cluster.

A. Standard switches span all hosts in a cluster automatically once they share the same vCenter inventory, with no per-host setup
B. A distributed switch is configured once at vCenter and spans all hosts
C. They are equivalent in features, differing only in the name shown in the vSphere Client
D. Distributed switches are configured separately on each host and do not span the cluster

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Standard switches are configured per host, so a mismatch between hosts breaks vMotion networking. The distributed switch centralizes it and adds features like network I/O control and port mirroring, which is why it is the choice at scale.
</details>

---

### Question 6
**Scenario:** Which storage protocol presents block storage to ESXi over an IP network?

A. SMB
B. Fibre Channel only, which carries SCSI block commands over a dedicated fabric and cannot run on an IP network
C. NFS
D. iSCSI, presenting LUNs formatted with VMFS

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** iSCSI and Fibre Channel are block protocols carrying VMFS; NFS is file-level and mounted directly without VMFS. Knowing which protocol yields VMFS versus a direct mount matters for how multipathing and datastore features behave.
</details>

---

### Question 7
**Scenario:** Which VMware storage technology aggregates local host disks into a shared datastore?

A. NFS
B. Raw device mapping
C. VMFS on a SAN, which presents shared LUNs from an external array that all hosts mount as one clustered datastore
D. vSAN, which pools local host disks into one datastore governed by storage policies

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** vSAN is the hyperconverged option, removing the external array and using host-local disks. Storage Policy Based Management is central: policies such as failures-to-tolerate determine how data is placed and protected, rather than manual LUN design.
</details>

---

### Question 8
**Scenario:** A VM needs guaranteed access to a minimum amount of CPU or memory.

A. Increase the VM's vCPU count so it can claim more scheduler time on a busy host whenever contention appears
B. VM-to-VM affinity rules that keep the VM on the same host as its partner VM
C. A resource reservation, with limits and shares for contention
D. A larger host

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Reservations guarantee, limits cap, and shares set relative priority only when resources are contended. Over-using reservations is a common mistake, because reserved-but-idle resources cannot be used by anything else and reduce consolidation.
</details>

---

### Question 9
**Scenario:** A point-in-time copy of a VM must be taken before a risky change.

A. A backup only
B. A template, which converts the VM into a master image that can be reverted to its earlier state whenever needed
C. vMotion to another host, which keeps a copy of the VM's earlier state for reverting later
D. A snapshot, capturing state and data so it can be reverted (not a backup)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Snapshots are for short-term revert, and long-lived or chained snapshots grow, hurt performance, and risk datastore fill. The exam and practice both stress that a snapshot depends on the base disk and is therefore not a backup.
</details>

---

### Question 10
**Scenario:** A standardized VM must be deployed repeatedly.

A. A template: a non-runnable master image deployed to new VMs, optionally customized
B. Manual installation of the guest operating system on every new VM, from the installation media
C. A snapshot of the first VM, which can be deployed repeatedly to create new powered-on copies
D. Clone a running VM each time and rename it by hand, which copies the source VM's identity and any drift into every copy

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Templates cannot be powered on, which prevents drift in the master. Guest customization sets a unique hostname, network identity, and SID on deployment, which is what stops identity collisions from cloned machines.
</details>

---

### Question 11
**Scenario:** ESXi hosts must be patched consistently across a cluster.

A. Lifecycle Manager, using a desired image or baselines with maintenance mode
B. A script per host
C. Patch each host manually through its own host client, one at a time, relying on each host to keep its own baseline
D. Reinstall ESXi on each host from the installation media whenever a patch is released

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Lifecycle Manager's image-based model defines the whole host image (ESXi, drivers, firmware) as a desired state. Entering maintenance mode evacuates the host via DRS first, which is what makes rolling patching non-disruptive.
</details>

---

### Question 12
**Scenario:** Two VMs must never run on the same host for availability.

A. A DRS anti-affinity rule keeping the VMs on separate hosts
B. A reservation of CPU and memory for each VM, which guarantees resources on its host
C. A resource pool, which divides cluster CPU and memory by shares and also keeps its member VMs on different hosts
D. Nothing can enforce this, because DRS has no rules that depend on VM placement

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Anti-affinity separates VMs so a single host failure cannot take down both, which is how you protect a clustered application. Affinity rules do the opposite, keeping VMs together, for example to reduce inter-host traffic.
</details>

---

### Question 13
**Scenario:** A resource pool is used to divide cluster capacity between two teams.

A. Resource pools always guarantee an equal split of cluster capacity between the teams, whatever their share values or VM counts
B. Pools are only for storage
C. Resource pools apportion resources with shares, reservations, and limits, but nested pools can give odd results
D. Pools replace clusters, because a pool carries its own hosts, storage, and network settings, plus its own DRS and HA

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Shares only take effect under contention and are relative, so a pool with more VMs can starve its members even with generous shares. This resource pool priority-pie behavior is a classic source of confusion the exam probes.
</details>

---

### Question 14
**Scenario:** What does entering maintenance mode on a host do in a DRS cluster?

A. Nothing until reboot
B. Blocks new VM placement and, with DRS, migrates running VMs off the host
C. Deletes the VMs
D. Powers off the host immediately and restarts its VMs elsewhere through HA, without waiting for any migration to finish

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Maintenance mode is the safe path to servicing a host. Without fully automated DRS, the administrator may have to vMotion VMs manually before the host will enter the mode, which is a common operational gotcha.
</details>

---

### Question 15
**Scenario:** Which network feature isolates traffic types such as management, vMotion, and storage?

A. VLANs and separate VMkernel adapters per traffic type, ideally on distinct networks
B. Fault Tolerance
C. One shared network for all traffic, since VLANs matter only for guest VMs
D. One VMkernel adapter

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** VMkernel adapters carry host system traffic and each is tagged for a service. Isolating them protects latency-sensitive vMotion and storage from each other and from VM traffic, which is a baseline design practice rather than an optimization.
</details>

---

### Question 16
**Scenario:** A trading application VM must keep running with no downtime and no data loss if its ESXi host fails. A restart on another host, even a fast one, is not acceptable.

A. vSphere HA with VM restart priority set to Highest
B. A DRS rule keeping the VM on the most reliable host
C. vSphere Fault Tolerance for the VM
D. Hourly snapshots replicated to a second datastore

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Fault Tolerance keeps a secondary copy of the VM running on another host, continuously synchronized, and switches to it instantly on host failure with no data loss. HA restarts the VM, which means an outage, whatever the priority. DRS rules do not survive a host failure, and snapshots are neither backups nor a failover mechanism.

**Key Concept:** [Providing Fault Tolerance for Virtual Machines](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-availability/providing-fault-tolerance-for-virtual-machines.html)
</details>

---

### Question 17
**Scenario:** A datastore must be retired. Its running VMs' disks need to move to a new datastore with no downtime, while the VMs stay on their current hosts.

A. Storage vMotion of each VM to the new datastore
B. vMotion of each VM to a different host in the cluster
C. Cold migration after powering each VM off
D. Clone each VM to the new datastore and delete the original

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Storage vMotion moves a running VM's files and disks between datastores with no downtime and without changing its host. A plain vMotion changes the host, not the storage. Cold migration requires powering off, and cloning creates a new VM, needs a cutover, and briefly duplicates the workload.

**Key Concept:** [Migrating Virtual Machines](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management/migrating-virtual-machines-host-management.html)
</details>

---

### Question 18
**Scenario:** Three vCenter Server instances in different sites must all use the same set of approved VM templates and ISOs, kept in sync from one central source.

A. Copy the templates to each site's datastores by hand every month
B. Export each template as OVF and email the files to each site
C. Store the templates on a local datastore of one ESXi host
D. Publish a content library centrally and subscribe to it from each vCenter

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A published content library can be subscribed to from other vCenter Server instances, which synchronize its templates, OVFs, and ISOs automatically. Manual copies and emailed exports drift out of date. A local datastore on one host is not shared with other sites and is a single point of failure.

**Key Concept:** [Using Content Libraries](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-virtual-machine-administration/using-content-librariesvsphere-vm-admin.html)
</details>

---

### Question 19
**Scenario:** An HA cluster has eight hosts. Administrators keep powering on more VMs, and the team worries that after a host failure there will not be enough capacity to restart everything.

A. Disable HA so that more VMs can be powered on
B. Enable admission control sized to tolerate one host failure
C. Set DRS to fully automated with the most aggressive threshold
D. Turn off VM monitoring to reduce resource overhead

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** HA admission control reserves failover capacity (for example, enough for one host failure) and prevents power-on operations that would consume it. Disabling HA removes the protection entirely. DRS balances load among running hosts but does not reserve spare capacity, and VM monitoring has nothing to do with restart capacity.

**Key Concept:** [vSphere HA Admission Control](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-availability/creating-and-using-vsphere-ha-clusters/vsphere-ha-admission-control.html)
</details>

---

### Question 20
**Scenario:** A VM's guest OS sometimes hangs while its host stays healthy. The team wants vSphere to restart the VM automatically when this happens.

A. Enable vSphere Fault Tolerance on the VM
B. Configure DRS affinity rules for the VM
C. Enable VM monitoring in the vSphere HA settings
D. Add a CPU reservation equal to the VM's full size

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** HA VM monitoring watches VMware Tools heartbeats (and I/O activity) and resets a VM whose guest stops responding. Fault Tolerance protects against host failure, and its secondary would mirror the same hung guest. DRS rules affect placement only, and a CPU reservation guarantees resources but cannot detect or fix a hang.

**Key Concept:** [How vSphere HA Works](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-availability/creating-and-using-vsphere-ha-clusters/how-vsphere-ha-works.html)
</details>

---

### Question 21
**Scenario:** New hosts with a newer Intel CPU generation are added to a cluster of older Intel hosts. vMotion between old and new hosts fails with CPU compatibility errors.

A. Enable EVC on the cluster at the older CPU baseline
B. Upgrade every VM's hardware version to the latest
C. Put the new hosts in maintenance mode permanently
D. Reinstall the older hosts with the newest ESXi release

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** EVC masks newer CPU features so every host in the cluster presents the same baseline, which allows vMotion across processor generations from the same vendor. VM hardware version and ESXi release do not change the physical CPU features exposed. Keeping the new hosts in maintenance mode wastes them.

**Key Concept:** [Migrating Virtual Machines](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management/migrating-virtual-machines-host-management.html)
</details>

---

### Question 22
**Scenario:** Database VMs must always land on storage that provides a specific level of availability and performance, and vSphere should flag any VM that is out of compliance.

A. Name the datastores "gold" and ask admins to choose them
B. Use a resource pool with high shares for storage
C. Create a custom attribute on each database VM
D. Create a VM storage policy and assign it to the VMs

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Storage policy-based management matches VMs to datastores whose capabilities meet the policy, filters compatible storage at placement, and reports compliance status. Naming conventions rely on people. Resource pool shares govern CPU and memory, not storage capability, and custom attributes are labels with no placement or compliance logic.

**Key Concept:** [Storage Policy Based Management](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage/storage-policy-based-management-in-vsphere.html)
</details>

---

### Question 23
**Scenario:** A team wants to provision 2 TB virtual disks that initially use only the space actually written, accepting the need to monitor datastore usage.

A. Thick provision eager zeroed disks
B. Thin provisioned disks
C. Thick provision lazy zeroed disks
D. Raw device mappings in physical mode

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A thin disk consumes datastore space only as data is written, so it saves space but allows overcommitment, which is why datastore usage must be monitored. Both thick formats allocate the full 2 TB at creation (eager zeroed also zeroes it up front). A raw device mapping passes a whole LUN to the VM and is not a space-saving format.

**Key Concept:** [Storage Provisioning and Space Reclamation](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-storage/storage-provisioning-and-space-reclamation-in-vsphere.html)
</details>

---

### Question 24
**Scenario:** On a distributed switch, one uplink is saturated while others are idle. The team wants ESXi to move VM traffic between uplinks based on actual utilization, without configuring the physical switch.

A. Route based on IP hash with a static EtherChannel
B. Route based on source MAC hash
C. Route based on physical NIC load
D. Use explicit failover order with one active uplink

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Route based on physical NIC load (load-based teaming), available only on a distributed switch, checks uplink utilization and moves VM ports off a busy uplink, with no physical switch configuration. IP hash requires EtherChannel on the physical switch. Source MAC hash and the originating port policy place traffic statically, and explicit failover order uses one uplink at a time.

**Key Concept:** [Networking Policies](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-networking/networking-policies.html)
</details>

---

### Question 25
**Scenario:** Users report a slow 8-vCPU VM. In `esxtop` its %RDY is high while the host's CPUs are heavily committed, and the guest itself shows only modest CPU use.

A. CPU contention; reduce the VM's vCPU count or rebalance load across hosts
B. Memory swapping; add a memory reservation equal to configured RAM
C. Storage latency; move the VM to a faster datastore right away
D. Network saturation; add a second virtual NIC to the VM

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** %RDY is the time a vCPU was ready to run but waited for a physical CPU, so high values mean CPU scheduling contention, which oversized VMs make worse. Right-sizing vCPUs or moving load (DRS) helps. Swapping shows in memory counters such as %SWP, storage latency in disk counters, and network saturation in network counters, not in %RDY.

**Key Concept:** [Performance Monitoring Utilities: resxtop and esxtop](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-monitoring-and-performance/performance-monitoring-utilities-resxtop-and-esxtop.html)
</details>

---

### Question 26
**Scenario:** Memory counters show balloon activity (MCTL) on several VMs of one host. What does this indicate?

A. The VMs have more memory than their guest OS can address
B. VMware Tools is out of date and must be reinstalled
C. Transparent page sharing has been turned off on the host
D. The host is under memory pressure and is reclaiming guest memory

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** When host memory runs short, ESXi uses the balloon driver in VMware Tools to make guests release memory they are not actively using. Ballooning is a sign of host memory pressure (and a warning before compression and swapping). It does not indicate an addressing limit or outdated tools, and page sharing settings do not cause ballooning.

**Key Concept:** [Administering Memory Resources](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-resource-management/administering-memory-resources.html)
</details>

---

### Question 27
**Scenario:** The vCenter Server Appliance must be backed up regularly so it can be restored after a failure, using the method VMware supports.

A. Take a VM snapshot of the appliance every night
B. Schedule file-based backup in the appliance management interface
C. Copy the appliance's VMDK files with a datastore browser
D. Export the inventory to a CSV file from the vSphere Client

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The appliance management interface (port 5480) supports scheduled file-based backups to a remote target, and the installer can restore from them. Snapshots are not backups and degrade performance when kept. Copying VMDKs of a running appliance is not consistent, and an inventory CSV cannot rebuild vCenter.

**Key Concept:** [File-Based Backup and Restore of vCenter Server](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-installation-and-setup/file-based-backup-and-restore-of-a-vcenter-server-environment.html)
</details>

---

### Question 28
**Scenario:** An ESXi host intermittently loses paths to its iSCSI LUNs. Which host log is the first place to look for storage and device errors?

A. `/var/log/vpxa.log`
B. `/var/log/shell.log`
C. `/var/log/vmkernel.log`
D. `/var/log/syslog.log`

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The VMkernel log records core kernel activity including storage devices, paths, and multipathing events, so path loss shows there. `vpxa.log` covers the vCenter agent's communication, `shell.log` records commands run in the ESXi shell, and `syslog.log` holds general system messages rather than storage path details.

**Key Concept:** [ESXi System Log Files](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-monitoring-and-performance/system-log-files.html)
</details>

---

### Question 29
**Scenario:** The database team must be able to power VMs on and off and open consoles, but only for VMs in the Databases folder, and nothing else.

A. Assign a custom role with those privileges on the folder, propagated
B. Assign the Administrator role to the team's group on the vCenter root object
C. Give the team the root password for each ESXi host running database VMs
D. Assign the Read-only role on the Datacenter and ask the team to request changes

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A permission pairs a user or group with a role on an inventory object, and propagation applies it to the objects beneath, so a custom role on the folder grants exactly the needed privileges there. Administrator on the root grants everything everywhere. Host root passwords bypass vCenter permissions and auditing, and Read-only does not let the team do the work.

**Key Concept:** [vSphere Permissions and User Management Tasks](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-security/vsphere-permissions-and-user-management-tasks.html)
</details>

---

### Question 30
**Scenario:** Administrators keep placing new VMs on datastores that are nearly full, while other datastores are almost empty. vSphere should pick datastores and rebalance space and I/O automatically.

A. Enable DRS on the compute cluster
B. Enable Storage I/O Control on one datastore
C. Increase the size of the fullest datastore
D. Group the datastores into a datastore cluster with Storage DRS

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Storage DRS on a datastore cluster recommends or performs initial placement and moves disks to balance space use and I/O latency across the datastores. Compute DRS balances CPU and memory between hosts, not datastores. Storage I/O Control prioritizes I/O during contention but does not place or move VMs, and growing one datastore only delays the problem.

**Key Concept:** [Using Datastore Clusters to Manage Storage Resources](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-resource-management/using-datastore-clusters-to-manage-storage-resources.html)
</details>

---

## Where to go deeper

- [VCP-DCV cert page](../../exams/vmware/vcp-dcv-2v0-21-23/) - notes, practice plan, strategy
- [Containers vs VMs](../../learn/concepts/containers-vs-vms.md) - where virtualization sits next to containers
- [Disaster recovery patterns](../architecture-patterns/disaster-recovery-patterns.md) - HA and FT in a broader resilience design
- **[📖 VMware certification](https://www.vmware.com/learning/certification.html)** - official exam guide
