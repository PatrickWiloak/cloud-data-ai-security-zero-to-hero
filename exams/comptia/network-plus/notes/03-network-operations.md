---
last-updated: 2026-07-29
---

# Network+ Domain 3 - Network Operations (19%)

Documentation, monitoring, availability, and the organizational paperwork. Light on
technology, heavy on terminology the exam expects you to distinguish precisely.

## Documentation

- **Physical network diagram** - cabling, ports, racks, and where equipment physically sits.
- **Logical network diagram** - IP subnets, VLANs, and routing relationships, independent of physical layout.
- **Rack diagram** - elevation showing what occupies each rack unit.
- **Wiring and port location diagram** - which wall port terminates on which patch panel port and switch port.
- **IP address management (IPAM)** - the authoritative record of allocated addresses and subnets. Prevents duplicate assignments.
- **Asset inventory** - hardware and software owned, with lifecycle status.
- **Baseline configuration** - the approved standard configuration for a device class. Drift from baseline is a change to investigate.
- **Site survey report** - documented wireless coverage and interference measurements.
- **Audit and assessment report** - findings from a formal review against a standard.

## Monitoring

- **SNMP** - polls devices for status. Traps are unsolicited alerts from the device.
- **Syslog** - centralized event logging. Severity runs 0 (emergency) to 7 (debug); lower numbers are more severe.
- **NetFlow / sFlow / IPFIX** - flow data describing who talked to whom, how much, and for how long. Flow data answers bandwidth questions that packet capture is too heavy for.
- **Packet capture** - full payload, highest detail, highest storage cost.
- **SIEM** - aggregates and correlates logs, generating alerts.
- **Network discovery** - identifying what is present, actively by scanning or passively by observing.

**Performance metrics**

- **Bandwidth** - theoretical maximum capacity of a link.
- **Throughput** - the data rate actually achieved.
- **Latency** - delay for a packet to travel end to end.
- **Jitter** - variation in latency between packets. The metric that ruins voice and video even when average latency is acceptable.
- **Packet loss** - packets that never arrive. Small percentages devastate TCP throughput.

Voice and video are the usual context for jitter questions; a bulk file transfer cares
about throughput and is largely indifferent to jitter.

## Availability and redundancy

- **High availability (HA)** - designing so that a single failure does not cause an outage.
- **Active-active** - all nodes serve traffic; provides load sharing and failover.
- **Active-passive** - a standby takes over on failure; simpler, wastes capacity.
- **Clustering** - multiple systems presenting as one service.
- **NIC teaming** - bonding multiple network adapters on a host for redundancy or throughput.
- **First hop redundancy (FHRP)** - protocols such as VRRP and HSRP present a virtual gateway IP shared by two routers, so gateway failure is transparent.
- **Load balancing** - distributing requests across servers.
- **Cold, warm, and hot site** - a cold site is space and power only, a warm site has equipment but stale data, a hot site is ready to take traffic immediately. Cost rises with readiness.

**Recovery metrics**

- **RTO (Recovery Time Objective)** - how quickly service must be restored.
- **RPO (Recovery Point Objective)** - how much data loss is acceptable, expressed as time.
- **MTBF (Mean Time Between Failures)** - average operating time between failures of a repairable system.
- **MTTR (Mean Time To Repair)** - average time to restore after a failure.

RTO and RPO are the pair most often confused. RTO is about *time to restore*; RPO is about
*data lost*. A one-hour RPO means backups at least hourly.

## Organizational documents and policies

- **SLA (Service Level Agreement)** - a commitment to a measurable service level, usually with penalties.
- **MOU (Memorandum of Understanding)** - a statement of intent between parties, generally not legally binding.
- **NDA (Non-Disclosure Agreement)** - confidentiality obligations.
- **AUP (Acceptable Use Policy)** - what users may and may not do with company systems.
- **BYOD policy** - terms for personal devices on the corporate network.
- **SOP (Standard Operating Procedure)** - the documented way a routine task is performed.
- **Onboarding and offboarding** - account and asset provisioning and, critically, revocation.
- **Data loss prevention (DLP)** - controls detecting and blocking sensitive data leaving the organization.

## Change and configuration management

- **Change management** - the process for requesting, assessing, approving, and recording changes.
- **Change request** - the record: reason, scope, risk, rollback plan, and approver.
- **Rollback plan** - how to undo the change if it fails. Required before approval, not written during the outage.
- **Maintenance window** - the agreed period for disruptive work.
- **Configuration management** - keeping device configurations consistent, versioned, and recoverable.
- **Configuration drift** - accumulated undocumented differences from the baseline.

## Network management methods

- **In-band management** - managing a device over the production network. Simple, but unavailable exactly when the network is broken.
- **Out-of-band management** - a separate path, such as a console server or dedicated management port, that works when the production network does not.
- **Jump box / bastion host** - a hardened intermediary through which administrative access is funnelled.
- **VPN** - encrypted remote access. Site-to-site connects networks; client-to-site connects individual users.

## Exam pointers

- Learn RTO versus RPO to the point of reflex. They are among the most reliably tested definitions in the domain.
- MTBF measures reliability, MTTR measures repair speed. A question about how long the business waits is MTTR.
- Jitter is the answer for choppy voice or video when latency looks fine.
- Any question about managing a switch during a network outage points to out-of-band management.
- MOU is not binding; SLA is. Questions sometimes hinge on that distinction.

## Official documentation

**[📖 CompTIA Network+ N10-009 objectives](https://www.comptia.org/certifications/network#examdetails)** - authoritative domain list
**[📖 NIST SP 800-34](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final)** - contingency planning, covers RTO and RPO
