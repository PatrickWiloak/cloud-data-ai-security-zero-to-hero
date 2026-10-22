---
last-updated: 2026-10-22
---

# Microsoft Certified: Azure Network Engineer Associate (AZ-700)

## Overview

The Azure Network Engineer Associate certification validates the ability to plan, implement and manage Azure networking: core VNet infrastructure (IP addressing, DNS, routing and monitoring), hybrid connectivity (VPN, ExpressRoute, Virtual WAN), application delivery (Load Balancer, Traffic Manager, Application Gateway, Front Door), private access to PaaS services (Private Link, service endpoints) and network security (NSGs, Azure Firewall, WAF).

This guide follows the skills measured **as of July 27, 2026**. That revision made minor changes to the IP addressing, monitoring and NSG skills (Microsoft's change log lists them). Older versions of this page used a retired outline (hybrid networking, routing, "secure and monitor networks"); the topics are mostly the same, but they now sit under different headings and weights, so plan your time from the table below.

This is the canonical Azure-networking specialty for network engineers, cloud architects, and security professionals working with Azure-hosted workloads.

---

## Quick Reference

| Detail | Info |
|---|---|
| **Exam Code** | AZ-700 |
| **Full Name** | Microsoft Certified: Azure Network Engineer Associate |
| **Provider** | Microsoft |
| **Format** | Multiple choice, multiple response, drag-and-drop, case studies |
| **Duration** | 100 minutes |
| **Cost** | $165 USD |
| **Validity** | 1 year (renewable for free annually via Microsoft Learn) |
| **Passing Score** | 700 / 1000 |

**[📖 Official AZ-700 page](https://learn.microsoft.com/credentials/certifications/azure-network-engineer-associate/)** - registration and certification details
**[📖 AZ-700 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-700)** - the skills measured as of July 27, 2026, with the change log

---

## Exam Domains

Skills measured as of July 27, 2026:

| # | Skill area | Weight | Note |
|---|---|---|---|
| 1 | Design and implement core networking infrastructure | 25-30% | [01](notes/01-core-networking-infrastructure.md) |
| 2 | Design, implement, and manage connectivity services | 20-25% | [02](notes/02-connectivity-services.md) |
| 3 | Design and implement application delivery services | 15-20% | [03](notes/03-application-delivery-services.md) |
| 4 | Design and implement private access to Azure services | 10-15% | [04](notes/04-private-access-to-azure-services.md) |
| 5 | Design and implement Azure network security services | 15-20% | [05](notes/05-network-security-services.md) |

Core networking infrastructure now carries routing (UDRs, Route Server, NAT Gateway, Virtual Network Manager) and network monitoring (Network Watcher, DDoS, Defender for Cloud), so it is the domain to study first and longest.

---

## Study Materials in This Guide

| File | Description |
|---|---|
| [fact-sheet.md](fact-sheet.md) | High-yield facts per skill area, with Microsoft Learn links |
| [strategy.md](strategy.md) | Time allocation by weight, traps and tactics |
| [practice-plan.md](practice-plan.md) | 8-week study plan mapped to the five skill areas |
| [scenarios.md](scenarios.md) | 12 exam-style scenarios |
| [notes/01-core-networking-infrastructure.md](notes/01-core-networking-infrastructure.md) | IP addressing, public IPs and BYOIP, DNS and Private Resolver, peering, AVNM, UDRs, Route Server, NAT Gateway, Network Watcher, DDoS, Defender for Cloud |
| [notes/02-connectivity-services.md](notes/02-connectivity-services.md) | Site-to-site and point-to-site VPN, Extended Network, ExpressRoute, Virtual WAN |
| [notes/03-application-delivery-services.md](notes/03-application-delivery-services.md) | Load Balancer (regional, cross-region, Gateway), Traffic Manager, Application Gateway, Front Door |
| [notes/04-private-access-to-azure-services.md](notes/04-private-access-to-azure-services.md) | Private endpoints, private DNS integration, Private Link service, service endpoints and policies |
| [notes/05-network-security-services.md](notes/05-network-security-services.md) | NSGs, ASGs, Bastion, virtual network flow logs, AVNM security admin rules, Azure Firewall and Firewall Manager, WAF |
| [Practice questions](../../../resources/practice-questions/azure-network-engineer-az-700.md) | 30 questions with explanations |

---

## Recommended Study Time

| Background | Estimated Prep Time |
|---|---|
| Azure admin (AZ-104) + networking experience | 4-6 weeks |
| AZ-104 only, light networking | 6-8 weeks |
| New to Azure | 12+ weeks; consider AZ-104 first |

---

## Hands-on Setup

- Azure free account ($200 credit, 30 days) or Visual Studio subscription credits
- Build out: 2 VNets in different regions, peer them, deploy a VPN gateway (AZ SKU), attach Azure Firewall, add Application Gateway WAF_v2, configure a private endpoint to Azure SQL Database with a private DNS zone, and turn on virtual network flow logs
- Each lab session, tear down to control cost (Azure networking can run $$$)

---

## Companion Materials

- **[AZ-104 Azure Administrator](../az-104/)** - prerequisite-level Azure knowledge
- **[Hybrid Connectivity Deep Dive](../../../resources/networking-deep-dives/hybrid-connectivity.md)**
- **[Multi-Cloud Networking](../../../resources/networking-deep-dives/multi-cloud-networking.md)**
- **[Cisco CCNA](../../cisco/ccna-200-301/)** - foundational networking concepts
- **[AWS Advanced Networking ANS-C01](../../aws/specialty/advanced-networking-ans-c01/)** - AWS counterpart
