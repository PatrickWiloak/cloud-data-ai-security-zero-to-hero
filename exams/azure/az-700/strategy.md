---
last-updated: 2026-10-22
---

# Azure Network Engineer Associate (AZ-700) - Exam Strategy

## Format reminder

- About 40-60 questions in 100 minutes (Microsoft does not publish a fixed count)
- Pass mark: 700 / 1000
- Multiple choice, multiple response, drag-and-drop and case studies
- AZ-104 level Azure administration is the practical prerequisite
- Skills measured as of July 27, 2026: five skill areas, listed below

**[📖 AZ-700 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-700)** - always check the "skills measured as of" date before you book

---

## Allocate study time by weight

The weights are ranges, so use the midpoint to plan. Over an 8-week plan of roughly 80 hours, that works out as follows.

| Skill area | Weight | Share of study time | Hours (of ~80) | Note |
|---|---|---|---|---|
| 1. Core networking infrastructure | 25-30% | ~28% | 22 | [01](notes/01-core-networking-infrastructure.md) |
| 2. Connectivity services | 20-25% | ~23% | 18 | [02](notes/02-connectivity-services.md) |
| 3. Application delivery services | 15-20% | ~17% | 14 | [03](notes/03-application-delivery-services.md) |
| 4. Private access to Azure services | 10-15% | ~12% | 10 | [04](notes/04-private-access-to-azure-services.md) |
| 5. Network security services | 15-20% | ~17% | 14 | [05](notes/05-network-security-services.md) |
| Practice exams and review | - | - | the rest | [scenarios](scenarios.md) |

Two adjustments to the raw numbers. First, study **core networking first and longest**: it now contains addressing, DNS, routing and monitoring, and the other four areas assume you know them. Second, give private access a little more than its 10-15% suggests, because private endpoint DNS questions also show up under core networking (name resolution) and security (network policies).

---

## How each skill area is tested

### 1. Core networking infrastructure

Expect subnet sizing and naming (`GatewaySubnet`, `AzureFirewallSubnet`, `AzureBastionSubnet`, `RouteServerSubnet`), DNS designs (private zones, links, auto-registration, Private Resolver inbound versus outbound), and routing puzzles. For routing puzzles, apply the rule in order: longest prefix match, then UDR over BGP over system routes. Many "traffic bypasses the firewall" questions are a more specific BGP route that the UDR did not cover, or a missing route on the return path. Know NAT Gateway, Route Server and Virtual Network Manager well enough to pick them from a requirement. Read the new monitoring skills carefully: DDoS protection tiers and the three Defender for Cloud features (Secure Score recommendations, attack path analysis, Cloud Security Explorer) are easy points if you know which does what.

### 2. Connectivity services

These are selection questions with numbers in them. Know which VPN gateway SKU meets a tunnel count, user count or throughput, and that new gateways use the AZ SKUs. Know route-based versus policy-based, the three P2S tunnel types and which authentication works with which (Entra ID needs OpenVPN). For ExpressRoute, know the four connectivity models, Local versus Standard versus Premium, private versus Microsoft peering (route filter required), and Global Reach versus FastPath versus Direct. For Virtual WAN, know Basic versus Standard and how association and propagation shape routing.

### 3. Application delivery services

Decide layer (4 or 7) and scope (regional or global) before reading the options. Then expect configuration questions: an Application Gateway returning 502 (probes), a multi-site listener not matching, end-to-end TLS failing (untrusted backend certificate), Front Door caching with query strings, or origin priority versus weight.

### 4. Private access to Azure services

Almost always private endpoint versus service endpoint, plus DNS. If the requirement says on-premises, no public endpoint, or one specific resource, the answer is a private endpoint. If it says cheapest or simplest and VNet-only, a service endpoint can be right. "Prevent copying data to other storage accounts" over service endpoints means service endpoint policies.

### 5. Network security services

Read NSG rule tables slowly: priority, direction, and whether the source is a service tag or an ASG. Know the evaluation order (subnet then NIC inbound, NIC then subnet outbound), Azure Firewall rule processing (DNAT, network, application), which features need Firewall Premium, and the WAF rollout from detection to prevention. Flow logs now mean **virtual network flow logs**.

---

## Top traps

1. **Peering, Virtual WAN and Global Reach** solve different problems: VNet-to-VNet, managed any-to-any transit, and on-premises-to-on-premises through ExpressRoute.
2. **VPN Gateway SKUs**: Basic is dev/test only; non-AZ SKUs are being migrated; size by tunnels, P2S users and throughput.
3. **ExpressRoute public peering** no longer exists; Microsoft peering replaced it and needs a route filter.
4. **Traffic Manager never sees the traffic**; Front Door proxies it.
5. **Service endpoint is not private access to the resource**; the resource keeps its public endpoint.
6. **Private endpoint network policies** are off by default, so NSGs and UDRs ignore that traffic until enabled.
7. **NAT Gateway** wins over load balancer outbound rules and instance public IPs.
8. **AVNM security admin rules** run before NSGs; Always Allow skips them.
9. **Front Door Premium** is required for managed WAF rules, bot protection and Private Link origins.
10. **Retired or retiring options** are distractors: Basic Load Balancer, Basic public IP, Application Gateway v1, NSG flow log creation, Front Door classic.

---

## Time management

100 minutes for about 50 questions is about 2 minutes each. Case studies take longer, so bank time on short items. Aim to be halfway at minute 45, flag anything that needs a diagram drawn, and keep 10 minutes for review. Once you leave a case study section you may not be able to return to it, so finish its questions first.

## When stuck

1. **Identify the layer**: TCP and UDP ports point to Load Balancer or NSGs; host names, paths and headers point to Application Gateway, Front Door or WAF.
2. **Identify the scope**: one region or global, one VNet or many, Azure only or hybrid.
3. **Prefer the managed, current answer**: Private Resolver over DNS forwarder VMs, NAT Gateway over default outbound, Virtual WAN for many branches, private endpoints for private PaaS.
4. **Eliminate retired features** listed in trap 10.

## Day-of logistics

Online or test center through Pearson VUE. Online needs a clean desk, a webcam and a system check beforehand. You can request an extra 30 minutes if the exam is not offered in your first language.

## After

**Pass:** the certification is valid for one year; renew free with the online assessment on Microsoft Learn in the six months before expiry.

**Fail:** the score report shows performance per skill area. Most misses cluster in core networking (routing and DNS) and connectivity services (SKU selection, ExpressRoute peering and resiliency). Rebuild those labs before retaking.

---

## AZ-700 patterns

- "Multi-region transit at scale with many branches" = Virtual WAN Standard
- "Spokes reach on-premises through the hub gateway" = gateway transit on peering
- "On-premises to Azure, private, predictable" = ExpressRoute private peering
- "On-premises to Microsoft 365 or public PaaS over ExpressRoute" = Microsoft peering with a route filter
- "Global L7 with WAF" = Front Door
- "Regional L7 with WAF" = Application Gateway WAF_v2
- "Global L4 with one IP" = cross-region Load Balancer
- "Hybrid DNS" = Azure DNS Private Resolver
- "SNAT exhaustion" = NAT Gateway
- "Centralized connectivity and guardrails for many VNets" = Azure Virtual Network Manager
- "BGP between NVAs and the VNet" = Route Server
- "RDP or SSH without public IPs" = Azure Bastion
- "DDoS protection on a few public IPs" = DDoS IP Protection; "on whole VNets with rapid response" = DDoS Network Protection
- "Which attack paths reach my database?" = Defender for Cloud attack path analysis
