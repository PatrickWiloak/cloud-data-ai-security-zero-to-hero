---
last-updated: 2026-10-22
---

# Google Cloud Professional Cloud Network Engineer Practice Plan

## 10-Week Plan Mapped to the Current Exam Guide

The plan follows the six sections of the current exam guide. Time is weighted by section weight: the two biggest sections (Section 1 at ~21% and Section 2 at ~20%) get two weeks each, and the remaining sections a week or more, with labs throughout and a final review fortnight. Budget about 8-10 hours a week (weekday evenings for reading, one longer weekend block for labs). Use a sandbox project with billing alerts, and tear labs down the same day: Interconnect cannot be practiced for real, but HA VPN between two VPCs, load balancers, Cloud NAT, NCC VPC spokes and Cloud Armor all can.

| Week | Exam section | Weight | Note |
|------|--------------|--------|------|
| 1-2 | 1. Designing and planning a Google Cloud VPC network | ~21% | [01-designing-planning-vpc-network.md](notes/01-designing-planning-vpc-network.md) |
| 3-4 | 2. Implementing a VPC network | ~20% | [02-implementing-vpc-network.md](notes/02-implementing-vpc-network.md) |
| 5 | 3. Configuring managed network services | ~16% | [03-managed-network-services.md](notes/03-managed-network-services.md) |
| 6 | 4. Configuring and implementing hybrid and multicloud network interconnectivity | ~16% | [04-hybrid-multicloud-interconnectivity.md](notes/04-hybrid-multicloud-interconnectivity.md) |
| 7 | 5. Managing, monitoring, and troubleshooting network operations | ~14% | [05-network-operations-monitoring-troubleshooting.md](notes/05-network-operations-monitoring-troubleshooting.md) |
| 8 | 6. Configuring, implementing and managing a cloud network security solution | ~13% | [06-network-security.md](notes/06-network-security.md) |
| 9-10 | Review, practice exams, weak areas | - | [fact-sheet.md](fact-sheet.md), [strategy.md](strategy.md), [scenarios.md](scenarios.md) |

---

## Week 1: Section 1, architecture and VPC design (tasks 1.1-1.2)

**Read:** [Section 1 note](notes/01-designing-planning-vpc-network.md), tasks 1.1 and 1.2.

- [ ] Premium vs Standard Tier: which load balancers need Premium, and why
- [ ] HA/DR building blocks: zonal, regional and global resources; global load balancer failover
- [ ] DNS topology: public, private, forwarding, peering zones; hub DNS VPC
- [ ] Load balancer selection: walk the four questions for ten made-up requirements
- [ ] IAM roles: networkAdmin vs securityAdmin vs xpnAdmin vs networkUser vs loadBalancerServiceUser
- [ ] Managed-service connectivity: private services access vs PSC vs Direct VPC egress vs Serverless VPC Access
- [ ] VPC count and type: custom mode, Shared VPC, peering vs NCC vs PSC
- [ ] IPAM: subnet sizing and expansion, IPv6 ULA and GUA, BYOIP, PUPI, internal ranges, Private NAT
- [ ] MTU: 1,460 default, 1,300-8,896 range; jumbo frame trade-offs
- [ ] NVA insertion: multi-NIC, IP forwarding, ILB next hop, policy-based routes
- [ ] **Lab:** design (on paper) a two-environment Shared VPC with a full IP plan including GKE Pod ranges, PSA range and proxy-only subnets

## Week 2: Section 1, hybrid, multicloud and GKE design (tasks 1.3-1.4)

**Read:** [Section 1 note](notes/01-designing-planning-vpc-network.md), tasks 1.3 and 1.4.

- [ ] Hybrid options table: HA VPN, Classic VPN, Dedicated, Partner, SD-WAN via NCC
- [ ] Cross-Cloud Interconnect: supported clouds, port speeds, SLA shapes
- [ ] Direct Peering vs Verified Peering Provider (public Google services, no VPC access, no SLA)
- [ ] 99.9% vs 99.99% Interconnect topologies; global dynamic routing requirement
- [ ] Reaching many VPCs from on-premises: Shared VPC, hub peering with custom routes, NCC
- [ ] Private access to Google APIs and Gemini Enterprise Agent Platform (formerly Vertex AI) from on-premises: PGA VIPs and PSC endpoints
- [ ] Hybrid DNS: inbound policy, forwarding zones, `35.199.192.0/19`, cross-project binding, DNS peering
- [ ] MTU for VLAN attachments and VPN; MACsec vs HA VPN over Interconnect
- [ ] GKE: private nodes, DNS-based endpoint vs IP endpoints, authorized networks, Pod range math, PUPI, IPv6, Gateway vs Ingress vs Service LB
- [ ] **Lab:** size Pod, Service and node ranges for a 300-node cluster at 110 and at 32 Pods per node

## Week 3: Section 2, VPCs and routing (tasks 2.1-2.2)

**Read:** [Section 2 note](notes/02-implementing-vpc-network.md), tasks 2.1 and 2.2.

- [ ] Create custom VPCs, subnets with secondary ranges, a proxy-only subnet and a dual-stack subnet
- [ ] Private services access range and connection; export custom routes
- [ ] Peer two VPCs both ways; exchange custom routes; test non-transitivity with a third VPC
- [ ] Shared VPC: enable host, attach service project, subnet-level networkUser, service agent roles
- [ ] Private Google Access, restricted VIP DNS zone and route, a PSC endpoint for Google APIs
- [ ] Expand a subnet range
- [ ] VPC Service Controls perimeter in dry-run, read the violations
- [ ] Routing: subnet vs static vs dynamic vs PBR order; tag-scoped routes; regional vs global dynamic routing
- [ ] Internal passthrough NLB as next hop for two appliance VMs
- [ ] **Lab:** build hub and spoke with peering, an appliance pair behind an ILB next hop, and a policy-based route with a `DEFAULT_ROUTING` exception

## Week 4: Section 2, NCC and GKE (tasks 2.3-2.4)

**Read:** [Section 2 note](notes/02-implementing-vpc-network.md), tasks 2.3 and 2.4.

- [ ] NCC spoke types: VPC, hybrid, router appliance, producer VPC
- [ ] Mesh vs star hub; spoke acceptance; export include/exclude ranges
- [ ] Private NAT for an overlapping spoke; PSC connection propagation and its Private NAT caveat
- [ ] Hub route tables and spoke state for troubleshooting
- [ ] GKE: VPC-native cluster in Shared VPC, private nodes, DNS-based endpoint, authorized networks
- [ ] Dataplane V2 and network policies; ip-masq-agent nonMasqueradeCIDRs
- [ ] Additional Pod ranges at cluster and node pool level
- [ ] Cloud DNS for GKE scopes and NodeLocal DNSCache
- [ ] **Lab:** NCC star hub with three VPC spokes (one center, two edge) and confirm edge-to-edge is blocked; then a Dataplane V2 cluster with a deny-all plus allow NetworkPolicy

## Week 5: Section 3, managed network services

**Read:** [Section 3 note](notes/03-managed-network-services.md).

- [ ] Load balancer family and old-to-new name mapping
- [ ] Anatomy: forwarding rule, target proxy, URL map, backend service, backends; load balancing schemes
- [ ] Balancing modes, capacity scaler, session affinity, health check ranges, global access, failover backends
- [ ] NEG types: zonal, serverless, internet, hybrid, PSC
- [ ] GKE: Service LoadBalancer, Ingress classes, Gateway classes, container-native LB
- [ ] Traffic splitting, mirroring, URL rewrite, redirects
- [ ] Cloud CDN origins, cache modes, cache keys, signed URLs, invalidation rules, internet NEGs and S3 origins
- [ ] Cloud DNS zones, migration steps, routing policies with health checks, DNSSEC and the DS record, forwarding and server policies, split horizon, cross-project binding, DNS peering, ExternalDNS
- [ ] **Lab:** global external Application LB with two regional MIGs, a backend bucket with CDN, a 90/10 traffic split, and a Cloud DNS failover policy in a private zone

## Week 6: Section 4, hybrid and multicloud interconnectivity

**Read:** [Section 4 note](notes/04-hybrid-multicloud-interconnectivity.md).

- [ ] Dedicated Interconnect flow (LOA-CFA, VLAN attachments, MTU options)
- [ ] Partner Interconnect flow (ASN 16550, pairing key, Layer 2 vs Layer 3)
- [ ] Cross-Cloud Interconnect build steps
- [ ] HA VPN over Cloud Interconnect (encrypted attachments, two Cloud Routers)
- [ ] 99.9% and 99.99% topologies, memorized
- [ ] HA VPN to on-premises and gateway-to-gateway between VPCs; Classic VPN route-based vs policy-based
- [ ] Cloud Router: ASNs, link-local IPs, MED, MD5, BFD timers, custom advertisements, custom learned routes, legacy vs standard best path selection
- [ ] NCC hybrid spokes, site-to-site data transfer, router appliances, transitivity table
- [ ] **Lab:** HA VPN between two VPCs (four tunnels if you like), custom advertisement of a peered range, MED-based primary/backup, then add both as NCC spokes

## Week 7: Section 5, operations, monitoring and troubleshooting

**Read:** [Section 5 note](notes/05-network-operations-monitoring-troubleshooting.md).

- [ ] Which logs are on by default and which must be enabled (flow logs, firewall logging, NAT, DNS, LB)
- [ ] Metrics and alerts for VPN, Interconnect, Cloud Router, load balancers, Cloud Armor, Cloud NAT
- [ ] Draining with connection draining, capacity scaler and traffic splitting
- [ ] VPN, Interconnect and BGP troubleshooting tables
- [ ] Flow logs vs firewall logs vs Packet Mirroring
- [ ] Network Intelligence Center: Network Topology, Connectivity Tests, Performance Dashboard, Firewall Insights, Network Analyzer, Flow Analyzer
- [ ] **Lab:** break things on purpose (remove the health check firewall rule, mismatch a BGP ASN, delete a route) and diagnose each with a Connectivity Test, logs and `get-status`

## Week 8: Section 6, network security

**Read:** [Section 6 note](notes/06-network-security.md).

- [ ] Cloud Armor policy types (backend, edge, network edge), actions, default rule, preview mode
- [ ] WAF rule sets and sensitivity levels; tuning
- [ ] Adaptive Protection, advanced network DDoS, Cloud Armor tiers
- [ ] Rate limiting (throttle vs rate-based ban, enforce-on keys), bot management, Google Threat Intelligence
- [ ] Firewall evaluation order across hierarchical, VPC rules, global and regional policies; enforcement order setting
- [ ] Secure tags vs network tags vs service accounts; NGFW Essentials, Standard, Enterprise
- [ ] NGFW Enterprise endpoints, security profiles, TLS inspection; migration tool
- [ ] Cloud NAT IP allocation, static vs dynamic ports, sizing math; Secure Web Proxy rules and modes
- [ ] Multi-NIC NVAs, ILB next hop with symmetric hashing, PBR, Network Security Integration, Packet Mirroring
- [ ] **Lab:** Cloud Armor policy with an SQLi rule in preview, a rate-based ban on `/login`, and a geo rule; a global network firewall policy using secure tags; Cloud NAT with manual IPs and DPA; a Packet Mirroring policy to a tcpdump collector

## Weeks 9-10: Review and practice exams

- [ ] Re-read every note's **Exam traps** and **Key terms** sections
- [ ] Work through [scenarios.md](scenarios.md) and explain why each wrong option is wrong
- [ ] Take the official practice exam (see [README](README.md)) and a second practice test; log every miss by section
- [ ] Spend the remaining days on the two weakest sections, prioritizing Sections 1 and 2 by weight
- [ ] Review [strategy.md](strategy.md) for time management and elimination tactics
- [ ] Day before: logistics (ID, remote proctoring check, quiet room) and light review of the [fact sheet](fact-sheet.md)

## gcloud practice set

```bash
# VPC, subnets, expansion
gcloud compute networks create VPC --subnet-mode=custom --bgp-routing-mode=global
gcloud compute networks subnets create SUBNET --network=VPC --region=REGION --range=CIDR
gcloud compute networks subnets expand-ip-range SUBNET --region=REGION --prefix-length=22

# Firewall policies and effective rules
gcloud compute network-firewall-policies create POLICY --global
gcloud compute instances network-interfaces get-effective-firewalls VM --zone=ZONE

# Load balancing
gcloud compute backend-services create BES --global --load-balancing-scheme=EXTERNAL_MANAGED --protocol=HTTP
gcloud compute url-maps create MAP --default-service=BES --global

# HA VPN and Cloud Router
gcloud compute vpn-gateways create GW --network=VPC --region=REGION
gcloud compute routers create ROUTER --network=VPC --region=REGION --asn=65001
gcloud compute routers get-status ROUTER --region=REGION

# NCC
gcloud network-connectivity hubs create HUB --preset-topology=mesh
gcloud network-connectivity spokes linked-vpc-network create SPOKE --hub=HUB --vpc-network=VPC_URI --global

# Diagnostics
gcloud network-management connectivity-tests create TEST --source-instance=VM_URI --destination-ip-address=IP --protocol=TCP --destination-port=443
```

## Study resources

- **[📖 Professional Cloud Network Engineer exam page](https://cloud.google.com/learn/certification/cloud-network-engineer)** - exam guide, logistics and practice questions
- **[📖 Best practices for VPC design](https://cloud.google.com/architecture/best-practices-vpc-design)** - Google's design guidance
- **[📖 Hybrid and multicloud secure networking patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns)** - reference architectures
- **[📖 VPC documentation](https://cloud.google.com/vpc/docs)** - networks, routes, firewalls
- **[📖 Cloud Load Balancing documentation](https://cloud.google.com/load-balancing/docs)** - every load balancer type

**👉 [Complete GCP Study Resources Guide](../../../.templates/resources-gcp.md)**

## Success metrics

- [ ] **Week 2:** can choose tier, load balancer, interconnection model and IP plan for any scenario without notes
- [ ] **Week 4:** has built Shared VPC, peering, NCC and a private GKE cluster
- [ ] **Week 6:** can recite the 99.99% Interconnect topology and the Cloud Router knobs
- [ ] **Week 8:** has built Cloud Armor, firewall policies with secure tags, Cloud NAT and Packet Mirroring
- [ ] **Week 10:** scoring comfortably above 80% on practice exams, with no section clearly weaker than the rest
