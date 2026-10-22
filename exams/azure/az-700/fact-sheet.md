---
last-updated: 2026-10-22
---

# AZ-700 Azure Network Engineer Associate - Fact Sheet

## Quick Reference

**Exam Code:** AZ-700
**Duration:** 100 minutes
**Cost:** $165 USD
**Passing Score:** 700/1000
**Format:** Multiple choice, multiple response, drag-and-drop, case studies
**Validity:** 1 year (renew free with an online assessment on Microsoft Learn)

**[📖 Official AZ-700 page](https://learn.microsoft.com/credentials/certifications/azure-network-engineer-associate/)**
**[📖 AZ-700 study guide (skills measured as of July 27, 2026)](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-700)**
**[📖 Azure Networking Documentation](https://learn.microsoft.com/azure/networking/)**

---

## Domain weights

| # | Skill area | Weight |
|---|---|---|
| 1 | Design and implement core networking infrastructure | 25-30% |
| 2 | Design, implement, and manage connectivity services | 20-25% |
| 3 | Design and implement application delivery services | 15-20% |
| 4 | Design and implement private access to Azure services | 10-15% |
| 5 | Design and implement Azure network security services | 15-20% |

The sections below follow the same five skill areas. Each one is a short summary of what to remember; the matching note in `notes/` teaches it in depth.

---

## 1. Core networking infrastructure (25-30%)

**Deep dive:** [notes/01-core-networking-infrastructure.md](notes/01-core-networking-infrastructure.md)

### IP addressing

A VNet lives in one region and holds one or more address spaces. Plan them so they never overlap with on-premises or with any VNet you will peer, because overlaps block peering and hybrid routing. Azure reserves five addresses in every subnet (network, gateway, two for DNS, broadcast), so a `/29` has three usable addresses.

Named subnets the exam expects you to know:

| Subnet | Used by | Size |
|---|---|---|
| `GatewaySubnet` | VPN and ExpressRoute gateways | `/27` or larger |
| `AzureFirewallSubnet` | Azure Firewall | `/26` |
| `AzureFirewallManagementSubnet` | Firewall forced tunneling | `/26` |
| `AzureBastionSubnet` | Azure Bastion | `/26` or larger |
| `RouteServerSubnet` | Azure Route Server | `/26` or larger |

Application Gateway needs a dedicated subnet. **Subnet delegation** hands a subnet to one PaaS service (App Service integration, SQL Managed Instance, DNS Private Resolver). Use **Standard** public IPs (Basic retired September 30, 2025). A **public IP prefix** gives a contiguous static range for partner allowlists; a **custom IP prefix** brings your own public range (BYOIP).

### Name resolution

Azure-provided DNS (`168.63.129.16`) resolves within a VNet only. **Private DNS zones** answer only for linked VNets, and one zone per VNet can auto-register VM records. **Azure DNS Private Resolver** replaces forwarder VMs: the inbound endpoint lets on-premises resolve Azure private zones; the outbound endpoint with a forwarding ruleset lets Azure VMs resolve on-premises names. Public zones are delegated with NS records at the registrar; alias records point the apex at Azure resources.

### Connectivity and routing

Peering is non-transitive. Hub side: **allow gateway transit**; spoke side: **use remote gateways**; hub-side **allow forwarded traffic** when a firewall forwards between spokes. **Azure Virtual Network Manager** builds hub-and-spoke or mesh connectivity for network groups and does nothing until a configuration is deployed. Routes are chosen by longest prefix first, then UDR over BGP over system routes. NVAs used as next hops need IP forwarding on their NIC. **Route Server** exchanges BGP routes with NVAs but carries no traffic. **NAT Gateway** gives outbound-only internet with 64,512 SNAT ports per public IP and overrides other outbound methods on its subnet. New VNets created with API versions after March 31, 2026 have **private subnets** by default, so VMs need an explicit outbound method.

### Monitoring

Network Watcher tools: IP flow verify, NSG diagnostics, next hop, effective security rules, connection troubleshoot, Connection monitor, packet capture, VPN troubleshoot, topology. **Network insights** in Azure Monitor is the dashboard. **DDoS Network Protection** (per VNet, with rapid response and cost protection) versus **DDoS IP Protection** (per IP, without them). Defender for Cloud gives network recommendations in **Secure Score**, exposure chains in **attack path analysis**, and ad hoc queries in **Cloud Security Explorer**.

---

## 2. Connectivity services (20-25%)

**Deep dive:** [notes/02-connectivity-services.md](notes/02-connectivity-services.md)

### Site-to-site VPN

You build a virtual network gateway, a local network gateway (the on-premises side) and a connection. **Route-based** supports IKEv2, BGP, active-active and P2S; **policy-based** is Basic SKU only, IKEv1, one tunnel. New gateways should use the **AZ SKUs** (VpnGw1AZ to VpnGw5AZ); Microsoft is migrating the non-AZ SKUs. Basic is dev/test only (no BGP, no RADIUS, no IKEv2 P2S, no IPv6). For HA use active-active, best with two on-premises devices (dual redundancy). A custom IPsec/IKE policy pins algorithms per connection. More than 100 tunnels: use Virtual WAN. **Azure Extended Network** stretches an on-premises subnet into Azure to migrate VMs without re-IP.

### Point-to-site VPN

Tunnel types: OpenVPN (TLS 443, all platforms), IKEv2, SSTP (Windows, max 128). Authentication: certificate, **Microsoft Entra ID (OpenVPN only)**, or RADIUS. Clients re-download the profile after any P2S change. **Always On VPN** needs a route-based, non-Basic gateway with IKEv2 and certificate authentication. **Azure Network Adapter** connects a Windows Server from Windows Admin Center over P2S.

### ExpressRoute

Models: Cloud Exchange co-location, point-to-point Ethernet, any-to-any IPVPN, ExpressRoute Direct (10 or 100 Gbps ports). Circuit SKUs: Local (nearby regions, egress included), Standard (geopolitical area), Premium (global, more routes and VNet links). **Private peering** reaches VNets; **Microsoft peering** reaches Microsoft public services and needs a **route filter**. Use both primary and secondary connections, and circuits in two peering locations for maximum resiliency. **Global Reach** connects on-premises sites through Microsoft. **FastPath** bypasses the gateway in the data path (needs a high-end gateway SKU). Encrypt with **MACsec** (Direct) or **IPsec over private peering**. **BFD** gives sub-second failure detection. Cross-subscription links use authorization keys.

### Virtual WAN

**Basic** is S2S VPN only; **Standard** adds ExpressRoute, P2S, transit and Azure Firewall. Gateways are sized in scale units. Hub routing uses route tables with **association** and **propagation**, plus **routing intent** to send internet and private traffic through a firewall or NVA. Partner NVAs run in the hub or in a spoke with BGP peering to the hub.

---

## 3. Application delivery services (15-20%)

**Deep dive:** [notes/03-application-delivery-services.md](notes/03-application-delivery-services.md)

| Option | Layer | Scope | Use case |
|---|---|---|---|
| Azure Load Balancer (Standard) | 4 | Regional | Any TCP/UDP, public or internal, HA ports for NVAs |
| Cross-region Load Balancer | 4 | Global | One anycast IP over regional load balancers |
| Gateway Load Balancer | 3/4 | Regional | Transparent NVA insertion |
| Traffic Manager | DNS | Global | DNS steering: priority, weighted, performance, geographic, multivalue, subnet |
| Application Gateway v2 | 7 | Regional | Path and host routing, TLS, rewrites, WAF |
| Front Door Standard/Premium | 7 | Global | Edge TLS, caching, acceleration, WAF, Private Link origins (Premium) |

Load Balancer: Basic SKU retired September 30, 2025. Rules map frontend to backend with a probe; inbound NAT rules forward ports to single instances; outbound rules configure SNAT. Probes come from `168.63.129.16`.

Application Gateway: frontend, listener (basic or multi-site), rule (basic or path-based), backend settings, pool and probe. Autoscale or manual capacity. TLS termination with Key Vault certificates, end-to-end TLS with trusted roots, rewrite sets for headers and URLs. Use v2 (v1 is retiring).

Front Door: profile, endpoint, custom domain, route, origin group, origins with priority and weight. Caching with query string behavior and purge, rule sets for rewrites and redirects, end-to-end TLS. Premium adds managed WAF rules, bot protection and Private Link origins.

---

## 4. Private access to Azure services (10-15%)

**Deep dive:** [notes/04-private-access-to-azure-services.md](notes/04-private-access-to-azure-services.md)

| Feature | Service endpoint | Private endpoint |
|---|---|---|
| Private IP for the service | No | Yes |
| Public endpoint can be disabled | No (filtered by VNet rules) | Yes |
| Granularity | Whole service type, narrowed for Storage by service endpoint policies | One resource sub-resource |
| Reachable from on-premises or peered VNets | No | Yes |
| DNS work | None | `privatelink` private DNS zone, linked to client VNets |
| Cost | Free | Hourly plus data processed |

Private endpoint DNS: the public name CNAMEs to the `privatelink` name; the linked private zone returns the private IP. On-premises clients need a conditional forwarder to a Private Resolver inbound endpoint. NSGs and UDRs apply to private endpoint traffic only after **network policies** are enabled on the subnet. **Private Link service** publishes your own app behind a Standard internal load balancer; providers see NAT IPs unless proxy protocol v2 is on. **Service endpoint policies** restrict a subnet to named storage accounts to stop exfiltration.

---

## 5. Network security services (15-20%)

**Deep dive:** [notes/05-network-security-services.md](notes/05-network-security-services.md)

### NSGs and related tools

Stateful, priority 100 to 4096, first match wins. Inbound: subnet NSG then NIC NSG; outbound: NIC then subnet. Default rules allow `VirtualNetwork` and `AzureLoadBalancer` inbound and internet outbound. **ASGs** group NICs (same VNet) so rules reference roles, not IPs. **Azure Bastion** gives RDP/SSH without public IPs; its subnet needs specific NSG rules (443 from Internet and GatewayManager, 8080 and 5701 within the VNet). **Virtual network flow logs** replace NSG flow logs, which no longer accept new configurations and retire September 30, 2027; add traffic analytics for insights. **IP flow verify** names the rule that allows or denies a packet. **AVNM security admin rules** run before NSGs: Deny cannot be overridden, Always Allow skips NSGs.

### Azure Firewall and Firewall Manager

| SKU | Adds |
|---|---|
| Basic | Core network and application rules for small sites |
| Standard | FQDN tags, web categories, DNS proxy, threat intelligence deny mode |
| Premium | TLS inspection, IDPS, URL filtering |

Rule order: DNAT, then network, then application, each by collection priority; parent policy rules beat child rules. `AzureFirewallSubnet` is `/26`; forced tunneling needs `AzureFirewallManagementSubnet`. **Firewall Manager** manages policies across firewalls; a **secured virtual hub** is Azure Firewall inside a Virtual WAN hub with routing intent.

### Web Application Firewall

A WAF policy attaches to Application Gateway WAF_v2 (gateway, listener or path scope) or to Front Door domains. Start in **detection**, tune exclusions, then move to **prevention**. Managed rule sets (Microsoft Default Rule Set, OWASP CRS on Application Gateway, Bot Manager) use anomaly scoring; custom rules (IP, geo, rate limit) run first. On Front Door, managed rules and bot protection need Premium.

---

## Highest-yield facts

1. VNet peering is non-transitive.
2. Route choice: longest prefix, then UDR, BGP, system.
3. `GatewaySubnet` `/27`+, `AzureFirewallSubnet` `/26`, `AzureBastionSubnet` and `RouteServerSubnet` `/26`+.
4. Private DNS zones resolve only for linked VNets; on-premises needs a Private Resolver inbound endpoint.
5. NAT Gateway is outbound only and wins over other outbound methods on its subnet.
6. New VPN gateways use AZ SKUs; Basic has no BGP, RADIUS or IKEv2 P2S.
7. Entra ID P2S authentication requires OpenVPN.
8. Microsoft peering needs a route filter; Premium is needed for global circuit reach.
9. Front Door is global L7, Application Gateway regional L7, Traffic Manager DNS only, Load Balancer L4.
10. Private endpoint removes public exposure; service endpoint only filters it.
11. Virtual network flow logs replace NSG flow logs.
12. Azure Firewall Premium for TLS inspection and IDPS.
13. WAF: detection first, then prevention.

---

## Common exam triggers

- "Spokes share the hub's VPN or ExpressRoute" - hub allow gateway transit, spokes use remote gateways
- "Spoke-to-spoke traffic must be inspected" - UDRs on spokes to Azure Firewall, hub allows forwarded traffic
- "Manage connectivity for hundreds of VNets by tag" - Azure Virtual Network Manager with dynamic network groups
- "Disable public access to Storage or SQL" - private endpoint, private DNS zone, public network access disabled
- "On-premises must resolve `privatelink` names" - conditional forwarder to a Private Resolver inbound endpoint
- "Global web app with WAF and bot protection" - Front Door Premium
- "Regional HTTPS with path routing and WAF" - Application Gateway WAF_v2
- "Non-HTTP app, one global IP, instant regional failover" - cross-region Load Balancer
- "SNAT port exhaustion" - NAT Gateway
- "Users connect with corporate identity and MFA" - P2S OpenVPN with Microsoft Entra ID
- "Encrypt ExpressRoute traffic" - MACsec on ExpressRoute Direct, or IPsec over private peering
- "Organization-wide rule no NSG can override" - AVNM security admin rule (Deny)
