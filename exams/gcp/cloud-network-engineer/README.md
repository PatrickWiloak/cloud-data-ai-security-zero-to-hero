---
last-updated: 2026-10-22
---

# Google Cloud Professional Cloud Network Engineer Certification

## Exam Overview

The Professional Cloud Network Engineer certification validates that you can design, implement and manage Google Cloud network infrastructure: VPC networks, routing, load balancing, Cloud NAT and Cloud DNS; hybrid and multicloud connectivity with Cloud Interconnect and Cloud VPN; operations with Google Cloud Observability and Network Intelligence Center; and network security with Cloud NGFW, VPC firewall rules, Secure Web Proxy, VPC Service Controls and Google Cloud Armor.

**Exam Name:** Professional Cloud Network Engineer
**Duration:** 2 hours
**Questions:** 50-60
**Format:** Multiple choice and multiple select
**Passing Score:** Not published
**Cost:** $200 USD (plus tax where applicable)
**Languages:** English, Japanese
**Validity:** 2 years (recertify in the final 60 days)
**Delivery:** Online proctored or onsite at a test center
**Prerequisites:** None required; recommended 3+ years of industry experience including 1+ year designing and managing solutions on Google Cloud

The current exam guide (PDF dated April 2026 by its file name) organizes the exam into six sections.

## Exam Domains

| Section | Weight |
|---------|--------|
| 1. Designing and planning a Google Cloud VPC network | ~21% |
| 2. Implementing a VPC network | ~20% |
| 3. Configuring managed network services | ~16% |
| 4. Configuring and implementing hybrid and multicloud network interconnectivity | ~16% |
| 5. Managing, monitoring, and troubleshooting network operations | ~14% |
| 6. Configuring, implementing and managing a cloud network security solution | ~13% |

### What each section covers

- **Section 1** - Network tiers, HA/DR, DNS topology, load balancer choice, GKE planning, IAM roles, managed-service connectivity, quotas; VPC type and count, interconnection (peering, NCC mesh/star, PSC), IPAM (IPv6, BYOIP, PUPI, Private NAT), MTU, appliance insertion; hybrid and multicloud design (Interconnect, Cross-Cloud Interconnect, VPN, SD-WAN, Direct Peering vs Verified Peering Provider, hybrid DNS, MACsec, HA VPN over Interconnect); GKE design.
- **Section 2** - Building VPCs, subnets, firewall rules or policies, private services access, peering, Shared VPC and its IAM, Private Google Access, subnet expansion, VPC Service Controls; static, dynamic and policy-based routing, ILB next hop, custom route exchange; Network Connectivity Center spokes, topologies, Private NAT, PSC propagation, CIDR filters; GKE networking (VPC-native, Shared VPC, private control plane, DNS-based endpoint, Dataplane V2, IP masquerade, network policy, additional Pod ranges, DNS).
- **Section 3** - Load balancer selection and configuration, backends and NEGs, GKE Gateway and Ingress, traffic management; Cloud CDN origins including internet NEGs and third-party storage, invalidation; Cloud DNS zones, migration, routing policies, DNSSEC, forwarding and server policies, split horizon, cross-project binding, DNS peering, external-dns for GKE.
- **Section 4** - Dedicated, Partner (Layer 2 vs Layer 3) and Cross-Cloud Interconnect, HA VPN over Interconnect, 99.9% and 99.99% SLA topologies; HA VPN and Classic VPN; Cloud Router BGP attributes, BFD, custom advertised and learned routes, legacy vs standard best path selection; NCC hybrid spokes, site-to-site data transfer, router appliances, transitivity.
- **Section 5** - Logging and metrics for VPN, Cloud Router, VPC-SC, NGFW, flow logs, DNS, NAT, NCC, Interconnect, load balancers and Cloud Armor; draining traffic; troubleshooting VPN, Interconnect and BGP; flow logs, firewall logs and Packet Mirroring; Network Topology, Connectivity Tests, Performance Dashboard, Firewall Insights, Network Analyzer and Flow Analyzer.
- **Section 6** - Cloud Armor edge and backend policies, WAF, Adaptive Protection and advanced network DDoS, rate limiting, bot management, Google Threat Intelligence; Cloud NGFW strategy, hierarchical evaluation, Enterprise L7 inspection, migration from VPC firewall rules, rule criteria, logging, secure tags, Essentials/Standard/Enterprise tiers; public Cloud NAT addressing and port allocation, Secure Web Proxy; multi-NIC NVAs, ILB next hop, policy-based routes, out-of-band Network Security Integration and Packet Mirroring.

## Study Materials

| File | What it is |
|------|------------|
| [notes/01-designing-planning-vpc-network.md](notes/01-designing-planning-vpc-network.md) | Section 1: designing and planning a Google Cloud VPC network |
| [notes/02-implementing-vpc-network.md](notes/02-implementing-vpc-network.md) | Section 2: implementing a VPC network (VPCs, routing, NCC, GKE) |
| [notes/03-managed-network-services.md](notes/03-managed-network-services.md) | Section 3: load balancing, Cloud CDN, Cloud DNS |
| [notes/04-hybrid-multicloud-interconnectivity.md](notes/04-hybrid-multicloud-interconnectivity.md) | Section 4: Interconnect, VPN, Cloud Router, NCC for hybrid |
| [notes/05-network-operations-monitoring-troubleshooting.md](notes/05-network-operations-monitoring-troubleshooting.md) | Section 5: logging, monitoring, troubleshooting, Network Intelligence Center |
| [notes/06-network-security.md](notes/06-network-security.md) | Section 6: Cloud Armor, Cloud NGFW, Cloud NAT, Secure Web Proxy, appliances and Packet Mirroring |
| [fact-sheet.md](fact-sheet.md) | Exam facts, high-yield facts per section, and vendor documentation links |
| [strategy.md](strategy.md) | Time allocation by section weight, per-section tactics, common traps |
| [practice-plan.md](practice-plan.md) | 10-week plan mapped to the six sections, with labs |
| [scenarios.md](scenarios.md) | Worked scenario questions with explanations |

## How to use this guide

1. Read the notes in order; Sections 1 and 2 together are about 41% of the exam and underpin the rest.
2. Do the labs in the [practice plan](practice-plan.md) in a sandbox project; HA VPN between two VPCs, load balancers, NCC VPC spokes, Cloud NAT, Cloud Armor and Packet Mirroring can all be built cheaply and torn down the same day.
3. Finish each note with its **Exam traps** and **Key terms** sections, then test yourself with [scenarios.md](scenarios.md) and practice exams.
4. Use the [strategy](strategy.md) for pacing and elimination on exam day.

## Official resources

- **[📖 Professional Cloud Network Engineer certification](https://cloud.google.com/learn/certification/cloud-network-engineer)** - registration, exam guide, logistics
- **[📖 Exam guide PDF](https://services.google.com/fh/files/misc/042426_professional_cloud_network_engineer_exam_guide_english.pdf)** - the current six-section outline
- **[📖 Google Cloud Skills Boost](https://www.cloudskillsboost.google/paths)** - official learning paths and hands-on labs
- **[📖 Google Cloud documentation](https://cloud.google.com/docs)** - complete service documentation
- **[📖 Google Cloud Free Program](https://cloud.google.com/free)** - free trial credit and always-free usage for labs

## 📚 Comprehensive Study Resources

**👉 [Complete GCP Study Resources Guide](../../../.templates/resources-gcp.md)**

The guide covers Google Cloud Skills Boost labs, video courses, practice test platforms, the free tier, community forums and gcloud tooling.

## Related certifications

- **Professional Cloud Architect** - broader solution architecture across Google Cloud
- **Professional Cloud Security Engineer** - deeper coverage of IAM, data protection and security operations
- **Associate Cloud Engineer** - a good foundation before this exam if you are new to Google Cloud
