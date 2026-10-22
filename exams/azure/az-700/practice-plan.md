---
last-updated: 2026-10-22
---

# AZ-700 - 8-Week Practice Plan

This plan follows the five skill areas measured as of July 27, 2026, in the order that makes them easiest to learn: core networking first, because everything else builds on it. It assumes 1-2 hours of reading plus 1-2 hours of hands-on lab per day.

Networking labs in Azure can be expensive (VPN gateways, Azure Firewall, Application Gateway). Tear everything down at the end of each session.

| Week | Skill area | Weight | Note |
|---|---|---|---|
| 1-2 | 1. Core networking infrastructure | 25-30% | [01](./notes/01-core-networking-infrastructure.md) |
| 3-4 | 2. Connectivity services | 20-25% | [02](./notes/02-connectivity-services.md) |
| 5 | 3. Application delivery services | 15-20% | [03](./notes/03-application-delivery-services.md) |
| 6 | 4. Private access to Azure services | 10-15% | [04](./notes/04-private-access-to-azure-services.md) |
| 7 | 5. Network security services | 15-20% | [05](./notes/05-network-security-services.md) |
| 8 | Practice exams and review | - | [fact-sheet](./fact-sheet.md), [scenarios](./scenarios.md) |

---

## Lab setup

- [ ] Activate an Azure free account ($200 credit) or Visual Studio subscription credits
- [ ] Set budget alerts at $50, $100 and $150
- [ ] Create a resource group named `learn-az700`
- [ ] Practise tearing it down at the end of each session: `az group delete --name learn-az700`

---

## Week 1 - Core networking: addressing and name resolution

- [ ] Read [notes/01-core-networking-infrastructure.md](./notes/01-core-networking-infrastructure.md), sections 1 and 2
- [ ] Lab: design an address plan for a hub and two spokes in two regions with no overlaps; create the VNets and subnets, including `GatewaySubnet`, `AzureFirewallSubnet` and `AzureBastionSubnet`
- [ ] Lab: delegate a subnet to App Service and integrate a web app with it
- [ ] Lab: create a public IP prefix and derive two public IPs from it
- [ ] Lab: private DNS zone with auto-registration linked to one VNet and resolution-only links to another
- [ ] Lab: Azure DNS Private Resolver with an inbound endpoint and an outbound endpoint plus a forwarding ruleset

### Self-check
- [ ] Can I name the minimum size of every named subnet?
- [ ] Can I explain inbound versus outbound endpoints of Private Resolver?

---

## Week 2 - Core networking: connectivity, routing and monitoring

- [ ] Read [notes/01-core-networking-infrastructure.md](./notes/01-core-networking-infrastructure.md), sections 3 and 4
- [ ] Lab: peer hub and spokes; test that spoke-to-spoke fails (non-transitive)
- [ ] Lab: Azure Virtual Network Manager with a dynamic network group (tag-based) and a hub-and-spoke configuration; deploy it and watch the peerings appear
- [ ] Lab: route table with `0.0.0.0/0` to a Linux VM acting as an NVA; enable IP forwarding and check effective routes and Next hop
- [ ] Lab: NAT Gateway on a private subnet; confirm the egress IP
- [ ] Lab: Connection monitor between two VMs; IP flow verify and NSG diagnostics on a blocked flow
- [ ] Read: Route Server, DDoS protection tiers, Defender for Cloud Secure Score network recommendations, attack path analysis and Cloud Security Explorer

### Self-check
- [ ] Can I predict which route wins when a UDR and a BGP route overlap?
- [ ] Do I know when to pick Route Server, NAT Gateway or AVNM?

---

## Week 3 - Connectivity services: VPN

- [ ] Read [notes/02-connectivity-services.md](./notes/02-connectivity-services.md), sections 1 and 2
- [ ] Lab: deploy a VPN gateway with an AZ SKU (this takes 30-45 minutes, so plan around it)
- [ ] Lab: simulate on-premises with a second VNet and its own gateway (or strongSwan on a Linux VM); build site-to-site with BGP
- [ ] Lab: apply a custom IPsec/IKE policy and break it on purpose to see the failure in VPN troubleshoot
- [ ] Lab: point-to-site with OpenVPN and Microsoft Entra ID authentication using the Azure VPN Client
- [ ] Read: Always On VPN, Azure Network Adapter, Azure Extended Network

### Self-check
- [ ] Can I pick a VPN SKU from tunnel, user and throughput numbers?
- [ ] Do I know which authentication method works with which tunnel type?

---

## Week 4 - Connectivity services: ExpressRoute and Virtual WAN

- [ ] Read [notes/02-connectivity-services.md](./notes/02-connectivity-services.md), sections 3 and 4
- [ ] ExpressRoute cannot be fully built in a personal lab (it needs a provider). Read the docs end to end and use the Microsoft Learn exercises
- [ ] Write one-paragraph answers: four connectivity models; Local versus Standard versus Premium; private versus Microsoft peering; Global Reach, FastPath and Direct; MACsec versus IPsec; BFD
- [ ] Lab: Virtual WAN Standard with two hubs, two connected VNets and a VPN site; inspect the default route table, association and propagation
- [ ] Read: routing intent and partner NVAs in the hub

---

## Week 5 - Application delivery services

- [ ] Read [notes/03-application-delivery-services.md](./notes/03-application-delivery-services.md)
- [ ] Lab: Standard Load Balancer with two VMs, a health probe, a load balancing rule, an inbound NAT rule and an outbound rule
- [ ] Lab: internal load balancer with HA ports in front of two NVA VMs
- [ ] Lab: Application Gateway WAF_v2 with autoscale, two multi-site listeners, a path-based rule, a custom probe, a Key Vault certificate and a rewrite set that removes the `Server` header
- [ ] Lab: Front Door Standard with two origins in different regions; test failover with priority, then split traffic with weight; add a rule set redirect and purge the cache
- [ ] Lab: Traffic Manager with priority routing and then a nested performance profile

### Self-check
- [ ] Can I pick the right service for any delivery requirement in under 30 seconds?
- [ ] Can I list three causes of an Application Gateway 502?

---

## Week 6 - Private access to Azure services

- [ ] Read [notes/04-private-access-to-azure-services.md](./notes/04-private-access-to-azure-services.md)
- [ ] Lab: storage account with private endpoints for `blob` and `dfs`; integrate with private DNS zones; disable public access; test from a VM and from outside
- [ ] Lab: enable private endpoint network policies on the subnet and route endpoint traffic through the NVA from week 2
- [ ] Lab: resolve the private endpoint from a "simulated on-premises" VNet through the Private Resolver inbound endpoint
- [ ] Lab: service endpoint for `Microsoft.Storage` with a VNet rule, then a service endpoint policy that allows only one storage account
- [ ] Lab: Private Link service behind a Standard internal load balancer, consumed from another VNet

---

## Week 7 - Network security services

- [ ] Read [notes/05-network-security-services.md](./notes/05-network-security-services.md)
- [ ] Lab: NSGs on subnet and NIC with ASGs for web, app and db tiers; verify with IP flow verify
- [ ] Lab: Azure Bastion with the required NSG rules on `AzureBastionSubnet`
- [ ] Lab: virtual network flow logs with traffic analytics; read raw tuples and find a denied flow
- [ ] Lab: AVNM security admin rule that denies inbound SSH from the internet; show that a local NSG allow cannot override it
- [ ] Lab: Azure Firewall Standard in the hub with a parent and child Firewall Policy, a DNAT rule, a network rule and an application rule using an FQDN tag; force spoke traffic through it
- [ ] Read: Firewall Premium (TLS inspection, IDPS), secured virtual hub
- [ ] Lab: WAF policy in detection mode on the Application Gateway from week 5, add an exclusion, then switch to prevention; add a rate-limit custom rule

---

## Week 8 - Practice exams and review

- [ ] Re-read [fact-sheet.md](./fact-sheet.md) cover to cover
- [ ] Work through [scenarios.md](./scenarios.md) and the [practice questions](../../../resources/practice-questions/azure-network-engineer-az-700.md)
- [ ] Take the free Microsoft Learn AZ-700 practice assessment
- [ ] Re-read the notes for any skill area that scores below 75%
- [ ] Score 80%+ twice before scheduling

---

## Stop signals (you're ready)

- [ ] You can sketch a hub-and-spoke with VPN or ExpressRoute, Azure Firewall, forced tunneling, Private Resolver and a private endpoint to Storage from memory
- [ ] You can predict route selection for overlapping UDR, BGP and system routes
- [ ] You can pick the right delivery service for any prompt
- [ ] You know private endpoint versus service endpoint trade-offs and the DNS steps
- [ ] You can troubleshoot connectivity with Network Watcher tools and flow logs
- [ ] You score 80%+ on practice exams twice in a row
