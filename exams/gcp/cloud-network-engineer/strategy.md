---
last-updated: 2026-10-22
---

# GCP Professional Cloud Network Engineer (PCNE) - Exam Strategy

## Format reminder

- 2 hours, 50-60 multiple choice and multiple select questions
- Passing score is not published; aim to be comfortably above 80% on practice tests
- Questions are scenario-heavy: a company, a constraint or two, and four plausible options

## Time allocation by section weight

With about 55 questions in 120 minutes you have roughly 2 minutes per question. Plan to finish a first pass in about 105 minutes and keep 15 minutes to revisit flagged questions. Expected question counts below are estimates from the published weights, not official numbers.

| Section | Weight | Approx. questions (of 55) | First-pass minutes |
|---------|--------|---------------------------|--------------------|
| 1. Designing and planning a Google Cloud VPC network | ~21% | 11-12 | 22 |
| 2. Implementing a VPC network | ~20% | 11 | 21 |
| 3. Configuring managed network services | ~16% | 9 | 17 |
| 4. Configuring and implementing hybrid and multicloud network interconnectivity | ~16% | 9 | 17 |
| 5. Managing, monitoring, and troubleshooting network operations | ~14% | 8 | 15 |
| 6. Configuring, implementing and managing a cloud network security solution | ~13% | 7 | 14 |

Questions are not grouped by section on the exam, so use the table to decide **study** time and to sanity-check your pace (about 30 questions done at the one-hour mark).

## Per-section tactics

**Section 1 - Design (~21%).** Underline the hard constraints before reading options: SLA, bandwidth, encryption, overlap, "central team", "no public IPs", "global users". Then eliminate any option that breaks one. Know the decision tables cold: tier, load balancer, peering vs NCC vs Shared VPC vs PSC, hybrid option, 99.9% vs 99.99% topology. GKE IP math (default `/24` per node for 110 Pods) shows up as "cluster cannot add nodes". [Note](notes/01-designing-planning-vpc-network.md)

**Section 2 - Implementation (~20%).** Questions test the step that was missed: the second side of a peering, custom route export, the service agent's `networkUser` role, the default internet gateway route for Private Google Access, global dynamic routing, the `DEFAULT_ROUTING` exception in a PBR, Dataplane V2 only at cluster creation. When two options both "work", pick the one that is least privilege and least operational effort. [Note](notes/02-implementing-vpc-network.md)

**Section 3 - Managed services (~16%).** For load balancers, decide internal/external, L7/L4, proxy/passthrough, global/regional in that order. Remember the health check ranges, proxy-only subnets, global access, and that UDP means passthrough. For CDN, invalidation is on the URL map and versioned URLs beat invalidation. For DNS, separate forwarding zones, server policies, peering zones and cross-project binding. [Note](notes/03-managed-network-services.md)

**Section 4 - Hybrid (~16%).** Memorize the SLA topologies, the Partner ASN 16550 rule, Layer 2 vs Layer 3 partner responsibilities, HA VPN's two-interface requirement, BFD limits (Interconnect only), custom advertisement uses, and when standard best path selection matters. Transitivity questions are the most common trap. [Note](notes/04-hybrid-multicloud-interconnectivity.md)

**Section 5 - Operations (~14%).** Map each symptom to a tool: Connectivity Tests for "is the path configured", `routers get-status` for BGP, flow logs for "did traffic flow", firewall logs for "which rule", Packet Mirroring for payload, Network Analyzer for proactive misconfiguration and IP exhaustion, Performance Dashboard for "is it Google or me". Remember which logs are off by default. [Note](notes/05-network-operations-monitoring-troubleshooting.md)

**Section 6 - Security (~13%).** Place each control on the path: Cloud Armor at the edge (edge policy before CDN cache), Cloud NGFW at the VM, Secure Web Proxy and Cloud NAT for egress, NSI or NGFW Enterprise for inspection. Know the firewall evaluation order, secure tags vs network tags, NGFW tier features and Cloud NAT port math. [Note](notes/06-network-security.md)

## Top traps

1. **Shared VPC vs VPC Network Peering vs Network Connectivity Center vs PSC**:
   - Shared VPC: one VPC owned by a host project, used by service projects
   - Peering: two independent VPCs, non-transitive, no overlap
   - NCC: hub with VPC and hybrid spokes, transitive, mesh or star (fixed at creation)
   - PSC: publish or consume one service, overlap allowed
2. **Load balancer names**: global external Application LB (Premium only), regional external and internal Application LBs, cross-region internal Application LB, external and internal proxy NLBs, external and internal passthrough NLBs. UDP and client-IP preservation mean passthrough.
3. **Cloud Armor tiers**: Standard vs Enterprise (Paygo or Annual; formerly Managed Protection Plus). Full Adaptive Protection, Google Threat Intelligence, named IP lists and advanced network DDoS protection need Enterprise.
4. **Interconnect SLAs**: 99.9% = two connections in one metro, different edge availability domains. 99.99% = four connections across two metros, Cloud Routers in two regions, global dynamic routing. HA VPN gets 99.99% with tunnels on both interfaces.
5. **Private Google Access vs PSC for Google APIs**: PGA is a subnet setting using Google API IPs (or the `private` `199.36.153.8/30` and `restricted` `199.36.153.4/30` VIPs); PSC gives an internal IP of your choosing.
6. **Hybrid DNS**: inbound server policy for on-premises to query Cloud DNS; forwarding zones (source `35.199.192.0/19`) for Cloud to query on-premises; DNS peering for spokes; cross-project binding for central DNS projects.
7. **Firewall layers**: hierarchical (org, folders) -> VPC firewall rules -> global network policy -> regional network policy -> implied rules, by default. Secure tags only in policies; network tags only in VPC rules.
8. **Cloud NAT**: outbound only, regional, on a Cloud Router; 64,512 ports per IP; default 64 ports per VM static; dynamic port allocation and endpoint-independent mapping are mutually exclusive.
9. **VPC Service Controls**: API-level data perimeters, not packet filtering; use dry-run first; pair with `restricted.googleapis.com` or a `vpc-sc` PSC bundle.
10. **Routing**: policy-based routes first, then subnet routes, then longest prefix, then priority, then ECMP; static routes cannot be equal to or inside a subnet range.

## When stuck

1. **Identify the layer**: L3/L4 vs L7, network vs API (VPC-SC).
2. **Identify the scope**: global vs regional vs internal; one VPC vs many; one org vs many.
3. **Prefer managed and least effort**: NCC over manual peering meshes, PSC over self-managed proxies, Cloud NAT over NAT instances, DNS-based GKE endpoint over bastions.
4. **Eliminate legacy or wrong-scope answers**: Classic VPN for a 99.99% requirement, Direct Peering for VPC access, Standard Tier with a global load balancer, peering for transitive routing.
5. **Check least privilege** when options differ only in IAM role or scope (subnet-level `networkUser` beats project-level).

## Day-of logistics

- 120 minutes, about 55 questions; flag and move on rather than burning five minutes on one item.
- Remote proctored or test center; have ID ready and run the system check in advance for online delivery.

## After

- **Pass**: certification is valid for 2 years; recertify in the final 60 days.
- **Fail**: use the per-section feedback to target the weakest sections, starting with whichever of Sections 1 and 2 was weaker because they carry the most weight, and wait out the retake period.

## PCNE pattern cheat list

- "Centralized network for many projects" = Shared VPC
- "Hundreds of VPCs, any-to-any or hub-and-spoke segmentation" = Network Connectivity Center
- "Global L7 with WAF and CDN" = global external Application LB + Cloud Armor + Cloud CDN
- "Non-HTTP TCP, global anycast" = global external proxy Network LB
- "UDP game servers, client IP needed" = external passthrough Network LB
- "Hybrid 99.99% over Interconnect" = four connections, two metros, two regions, global routing
- "Encrypt Interconnect at line rate" = MACsec; "IPsec over Interconnect" = HA VPN over Cloud Interconnect
- "Private API access from VMs" = Private Google Access or a PSC endpoint
- "Data exfiltration prevention for Google APIs" = VPC Service Controls
- "Org-wide firewall guardrails" = hierarchical firewall policy
- "Block egress by domain" = Cloud NGFW Standard FQDN objects; "URL-level egress policy" = Secure Web Proxy
- "Detect and block exploits east-west" = Cloud NGFW Enterprise IPS
- "Outbound-only internet for private VMs" = Cloud NAT
- "DDoS + WAF + geo-blocking" = Cloud Armor (Enterprise for Adaptive Protection and threat intelligence)
- "Find which rule blocks traffic" = Connectivity Tests, then firewall rule logs
