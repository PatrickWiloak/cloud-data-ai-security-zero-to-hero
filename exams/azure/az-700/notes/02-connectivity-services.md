---
last-updated: 2026-10-22
---

# 02 - Design, Implement, and Manage Connectivity Services (20-25%)

This domain is about getting traffic between Azure and everything that is not Azure: offices, data centers, remote users and branch networks. The July 27, 2026 outline groups it into four skills: site-to-site VPN, point-to-site VPN, ExpressRoute and Virtual WAN. Expect scenario questions that hand you bandwidth, availability and authentication requirements and ask which SKU, model or setting meets them at the lowest cost or effort.

**[📖 AZ-700 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-700)** - the official skills outline this note follows

---

## 1. Site-to-site VPN

### What it is and the pieces you build

A site-to-site (S2S) VPN is an IPsec/IKE tunnel over the public internet between an on-premises VPN device and an Azure **virtual network gateway** of type VPN. You build three resources:

1. A **virtual network gateway** in the VNet's `GatewaySubnet`, with a Standard SKU public IP (two for active-active). Creating one takes a while, often 30 minutes or more, which is worth knowing for "fastest way" questions.
2. A **local network gateway**, which is Azure's description of the on-premises side: the device's public IP or FQDN, and either the on-premises address prefixes (static routing) or the device's BGP ASN and peer IP (dynamic routing).
3. A **connection** of type site-to-site (IPsec) that joins the two, holding the shared key and, optionally, a custom IPsec/IKE policy.

### Route-based versus policy-based

A **route-based** gateway uses any-to-any traffic selectors and decides what goes into the tunnel from the routing table. It supports IKEv2, BGP, active-active, point-to-site, multiple tunnels and coexistence with ExpressRoute. A **policy-based** gateway uses static traffic selectors (prefix pairs), supports only IKEv1, only one S2S tunnel and no point-to-site, and is available only on the Basic SKU. Choose policy-based only when a legacy on-premises device cannot do anything else. If the device is policy-based but you need route-based features, connect a route-based gateway with **PolicyBasedTrafficSelectors** enabled on the connection.

### Gateway SKUs

Microsoft is consolidating VPN gateway SKUs onto the availability-zone (AZ) SKUs. The non-AZ VpnGw1 to VpnGw5 SKUs are slated for migration and should not be used for new gateways. The current SKUs to choose from are:

| SKU (Generation) | S2S tunnels | P2S IKEv2/OpenVPN connections | Aggregate throughput benchmark |
|---|---|---|---|
| Basic (Gen1) | 10 | not supported (SSTP only, 128) | 100 Mbps |
| VpnGw1AZ (Gen1) | 30 | 250 | 650 Mbps |
| VpnGw2AZ (Gen2) | 30 | 500 | 1.25 Gbps |
| VpnGw3AZ (Gen2) | 30 | 1,000 | 2.5 Gbps |
| VpnGw4AZ (Gen2) | 100 | 5,000 | 5 Gbps |
| VpnGw5AZ (Gen2) | 100 | 10,000 | 10 Gbps |

Selection logic: Basic is dev/test only (no BGP, no IPv6, no RADIUS, no IKEv2 point-to-site, limited support). For production, size by tunnel count, point-to-site user count and throughput, and remember a single tunnel is far below the aggregate figure. If you need more than 100 tunnels, the documented answer is **Virtual WAN**.

### Designing for high availability

Every VPN gateway is two instances. In the default **active-standby** mode only one serves your tunnel; Microsoft documents a planned failover at about 10 to 15 seconds and an unplanned one at 1 to 3 minutes. **Active-active** runs both instances with their own public IPs, so the on-premises device builds two tunnels and traffic uses both. The strongest design is **dual-redundancy**: active-active in Azure plus two on-premises devices, giving a full mesh of four tunnels, with BGP so failover is automatic. Zone-redundant AZ SKUs protect against a zone failure inside the region on top of that.

### IPsec/IKE policies

By default Azure offers a set of proposals and the device negotiates one. A **custom IPsec/IKE policy** on the connection pins exact algorithms (for example IKEv2 with AES256 and SHA256, DH group 14, IPsec GCMAES256, PFS group 14, and SA lifetimes). Use it when a compliance standard mandates algorithms or when the on-premises device only supports a specific combination. Both sides must match exactly, or phase 1 or phase 2 negotiation fails.

### Diagnosing gateway connectivity

Work from the bottom up:

- Connection status in the portal, and the gateway's tunnel metrics.
- Network Watcher **VPN troubleshoot** on the gateway or the connection, which writes detailed IKE logs to storage.
- Shared key mismatch, mismatched IKE/IPsec proposals, or the wrong public IP in the local network gateway.
- **Overlapping address prefixes** between on-premises and Azure, or prefixes in the local network gateway that do not match what the device sends.
- For BGP: the BGP peer IPs, ASNs, and whether Azure's custom APIPA BGP addresses are used when the device needs link-local peering.
- Resetting the gateway as a last resort.

### Azure Extended Network

Azure Extended Network stretches an on-premises subnet into Azure so you can migrate VMs **without changing their IP addresses**. It uses a pair of Windows Server Azure Edition VMs, one on-premises and one in Azure, that build a VXLAN tunnel between the two sides over your existing VPN or ExpressRoute. It is a migration aid, not a permanent design, and the exam frames it that way: "move VMs to Azure, keep their IPs, finish the re-IP later".

---

## 2. Point-to-site VPN

### Gateway SKU and tunnel types

Point-to-site (P2S) connects individual devices to a VNet through the same VPN gateway. Size the gateway by connection count: SSTP is limited to 128 connections on every SKU, while IKEv2 and OpenVPN scale with the SKU, from 250 on VpnGw1AZ up to 10,000 on VpnGw5AZ. The Basic SKU has no IKEv2 or OpenVPN point-to-site, so it is rarely the right answer.

Three tunnel types:

- **OpenVPN** - TLS over TCP 443 (or UDP), works through most firewalls, runs on Windows, macOS, Linux, iOS and Android, and is the only tunnel type that supports Microsoft Entra ID authentication.
- **IKEv2** - standards-based IPsec, native on Windows and macOS, but uses UDP 500 and 4500, which some networks block.
- **SSTP** - Microsoft's TLS-based protocol, Windows only.

A common choice is "IKEv2 and OpenVPN" so Windows clients use IKEv2 and everyone else uses OpenVPN.

### Authentication methods

- **Certificate** - you upload a root certificate's public key to the gateway and install client certificates signed by it. Revoke by adding thumbprints to the revoked list. Works with all three tunnel types.
- **Microsoft Entra ID** - OpenVPN only, with the Azure VPN Client. Users sign in with Entra credentials, which brings Conditional Access and MFA. This is the usual answer for "users must use their corporate identity with MFA".
- **RADIUS** - the gateway forwards authentication to a RADIUS server you run (on-premises or in Azure), which in turn can check Active Directory, issue certificates or apply third-party MFA. Configure the RADIUS server's IP and secret on the gateway, and make sure the gateway can reach it (on-premises RADIUS needs the S2S tunnel up).

### Client configuration and troubleshooting

After configuring P2S you **download the VPN client profile package** from the gateway. It contains the profile files (for example the XML for the Azure VPN Client, plus native IKEv2 and OpenVPN configurations). Any change to the gateway's P2S settings, such as adding a tunnel type or changing the address pool, means clients must download and import the new profile.

Typical client and authentication failures: the client certificate is missing, expired or not chained to the uploaded root; the root was revoked; the client address pool overlaps the VNet or on-premises; Entra ID tenant, audience or issuer values are wrong in the gateway configuration; or the user's network blocks IKEv2 ports. Routes not reaching the client after adding a peering or a new on-premises prefix also means a fresh profile download is needed.

### Always On VPN and Azure Network Adapter

**Always On VPN** is a Windows client feature that keeps a tunnel up automatically. Azure supports it through a route-based VPN gateway with IKEv2 point-to-site. The **device tunnel** connects before user sign-in (for management and domain logon) and uses machine certificates; the **user tunnel** connects after sign-in. You need to know the Azure-side requirements: a route-based gateway that is not Basic, IKEv2 enabled, and certificate authentication configured with the right root.

**Azure Network Adapter** is a Windows Admin Center feature that connects a single Windows Server to an Azure VNet with a point-to-site connection in a few clicks. It creates (or reuses) a route-based VPN gateway, generates certificates and installs the client. Requirements: Windows Admin Center registered with Azure, a VNet with a gateway subnet, and a gateway SKU that is not Basic.

---

## 3. Azure ExpressRoute

### Connectivity models

ExpressRoute is a private connection between your network and Microsoft that does not traverse the internet. You choose one of four models:

- **Cloud Exchange co-location** - you are already in a colocation facility with an exchange; you order a virtual cross-connect.
- **Point-to-point Ethernet** - a provider runs a dedicated Ethernet link from your site to Microsoft.
- **Any-to-any (IPVPN)** - Microsoft becomes another site on your provider's MPLS WAN; good when you already run MPLS.
- **ExpressRoute Direct** - you connect directly to Microsoft's routers at a peering location on dedicated 10 Gbps or 100 Gbps port pairs, with no provider in the middle.

### Circuit SKUs, tiers and billing

A circuit has a **SKU** of Local, Standard or Premium, and a **billing model** of metered (pay per outbound GB) or unlimited.

- **Local** - reaches only the Azure regions close to the peering location, and egress data is included. Cheapest when the workloads sit in that local region.
- **Standard** - reaches all regions in the same geopolitical area.
- **Premium** - reaches regions globally, raises the route limit for private peering (from 4,000 to 10,000 IPv4 prefixes) and allows more VNet links per circuit.

The ExpressRoute **gateway** in your VNet has its own SKUs. The zone-redundant ErGw1Az, ErGw2Az and ErGw3Az, and the newer scalable gateway (ErGwScale) that you size in scale units, are the ones to pick; the older Standard, HighPerformance and UltraPerformance names are legacy. Gateway throughput, not circuit bandwidth, is often the bottleneck in "the circuit is 10 Gbps but we only get 2" questions.

### Peering types

- **Azure private peering** - extends your network to your VNets. Uses private addressing and is what almost every scenario needs.
- **Microsoft peering** - reaches Microsoft public services (Microsoft 365, Dynamics 365, Azure PaaS public endpoints) over the circuit. It requires public IP addresses you own for the BGP session and NAT, and a **route filter** that selects which service communities you want; without a route filter no prefixes are advertised.

Choose private peering only when you just need VNets. Add Microsoft peering only when there is a stated need to reach Microsoft public endpoints privately, because it adds NAT, public addressing and asymmetric routing considerations. Microsoft generally recommends reaching Microsoft 365 over the internet unless a regulation requires otherwise.

Each peering needs two `/30` (or `/126` for IPv6) subnets for the primary and secondary BGP sessions, a VLAN ID and your ASN.

### Connecting VNets and cross-subscription links

You create an ExpressRoute gateway in `GatewaySubnet`, then a **connection** from the gateway to the circuit. To link a VNet in another subscription, the circuit owner creates an **authorization key** and the VNet owner redeems it when creating the connection. Many VNets can link to one circuit; with gateway transit, spokes in a hub-and-spoke use the hub's ExpressRoute gateway.

### Redundancy, cross-region connectivity and disaster recovery

Every circuit has a primary and secondary connection to two Microsoft edge routers. Use both actively, and use two devices on your side. That protects against a device failure but not a peering-location failure. Microsoft's resiliency tiers describe the next steps:

- **Maximum resiliency** - two circuits in two different peering locations, each with redundant connections.
- **High resiliency** - one circuit spread across two peering locations in the same metro (ExpressRoute Metro).
- **Standard resiliency** - a single circuit at one location.

For region-level disaster recovery, link the second region's VNets to circuits in both locations, and use weights and AS path prepending to keep traffic symmetric. A S2S VPN can serve as a low-cost backup path; ExpressRoute routes are preferred over VPN routes for the same prefix.

### Global Reach, FastPath and Direct

- **Global Reach** links two of your ExpressRoute circuits through Microsoft's backbone so two on-premises sites can talk to each other through Microsoft, for example a London office and a New York office that each have a circuit.
- **FastPath** sends traffic from on-premises straight to VMs in the VNet, bypassing the ExpressRoute gateway in the data path, which removes the gateway as a throughput bottleneck. It needs a high-performance gateway SKU (Ultra Performance, ErGw3Az or a scalable gateway with enough units) and has limitations, so read the current list before relying on it for peered VNets or private endpoints.
- **ExpressRoute Direct** gives you the dedicated ports, lets you create several circuits on them, and supports MACsec.

### Route advertisement and encryption

**Route advertisement**: advertise summarized prefixes from on-premises to stay well under the route limits, use **AS path prepending** to influence which circuit Azure prefers for return traffic, and use **connection weight** on the Azure side to prefer one circuit over another for traffic leaving Azure. Avoid advertising a default route unless you mean to force-tunnel everything.

**Encryption**: ExpressRoute is private but not encrypted by default. Two options. **MACsec** encrypts at layer 2 between your edge routers and Microsoft's on ExpressRoute Direct ports, with keys stored in Key Vault. **IPsec over ExpressRoute** builds a site-to-site VPN across the private peering (or through Virtual WAN) so traffic is encrypted end to end to the VNet.

### Bidirectional Forwarding Detection and troubleshooting

BGP's default hold timer means a dead link can take up to three minutes to detect. **Bidirectional Forwarding Detection (BFD)** detects a failure in well under a second and tells BGP to fail over. Microsoft enables BFD on its side for private peering (and Microsoft peering) on newer circuits; you enable it on your customer edge routers.

Troubleshoot in order: circuit provisioning state (Provisioned by the provider) and circuit status (Enabled), then the peering's BGP state, then ARP tables and route tables on the circuit (available in the portal and PowerShell), then the gateway connection, then effective routes on a VM. Common faults: the provider has not provisioned the circuit, VLAN ID or peer subnets mismatch, the route limit was exceeded so the BGP session dropped, or a route filter is missing on Microsoft peering.

---

## 4. Azure Virtual WAN

### SKUs and architecture

Virtual WAN is a Microsoft-managed hub-and-spoke network. You create a Virtual WAN resource, then **virtual hubs** in the regions you use. Each hub is a Microsoft-managed VNet that can hold gateways (S2S VPN, P2S VPN, ExpressRoute), Azure Firewall or partner NVAs, and you connect spoke VNets and branches to it. Hubs in the same Virtual WAN are connected to each other automatically.

There are two SKUs:

- **Basic** - site-to-site VPN only, no transit between hubs.
- **Standard** - everything: ExpressRoute, P2S, VNet-to-VNet transit through the hub, hub-to-hub transit, Azure Firewall and NVAs in the hub. You can upgrade Basic to Standard but not downgrade.

Choose Virtual WAN when there are many branches, multiple regions, or a requirement for any-to-any transit without hand-built UDRs. Choose a self-managed hub VNet when you need full control of the hub (custom NVAs anywhere, unusual routing) and the scale is modest.

### Creating a hub and choosing scale units

A hub needs its own address space (at least `/24`; Microsoft recommends `/23` so there is room for NVAs). Gateways in the hub are sized in **scale units**. As a rule of thumb from the docs: one S2S VPN scale unit is 500 Mbps, one ExpressRoute scale unit is 2 Gbps, and one P2S scale unit is 500 Mbps with a set number of concurrent users. You pick scale units per gateway type based on aggregate branch bandwidth, circuit bandwidth and remote user count, and you can change them later.

### Hub routing

Each hub has a **default route table**. Connections (VNets, VPN sites, ExpressRoute circuits) are **associated** with one route table, which decides where their traffic can go, and **propagate** their routes to one or more route tables, which decides who can reach them. **Labels** group route tables so a connection can propagate to many at once. With these you can build isolation patterns such as "spokes reach shared services and branches, but not each other".

**Routing intent** is the simpler modern way to send traffic through a security appliance in the hub: set an internet traffic policy, a private traffic policy, or both, with Azure Firewall or a supported NVA as the next hop, and the hub programs the routes for you. **Hub routing preference** decides which path wins when the same prefix is learned from ExpressRoute, VPN or both (ExpressRoute, VPN, or shortest AS path).

### Third-party NVAs

You can integrate a partner NVA two ways. **NVA in the hub**: supported SD-WAN or firewall partners deploy managed appliances into the hub itself, and their routes integrate with hub routing. **NVA in a spoke**: you run the appliance in a spoke VNet and peer it with the hub over BGP (hub BGP peering) so the hub learns branch routes from it. The exam phrase "integrate a virtual hub with a third-party NVA for cloud connectivity" points at these two options.

---

## Choosing between connectivity options

| Requirement | Best fit |
|---|---|
| Small office, cost-sensitive, internet acceptable | Site-to-site VPN |
| Predictable bandwidth, low latency, no internet path | ExpressRoute private peering |
| Remote users with Entra ID and MFA | P2S OpenVPN with Microsoft Entra ID authentication |
| ExpressRoute with a cheap backup | ExpressRoute plus S2S VPN coexistence |
| Two offices talking through Microsoft | ExpressRoute Global Reach |
| Encrypt ExpressRoute | MACsec on Direct, or IPsec VPN over private peering |
| More than 100 S2S tunnels, many branches, any-to-any | Virtual WAN Standard |
| Migrate VMs without re-IP | Azure Extended Network |

---

## Exam traps

1. Policy-based VPN means Basic SKU, IKEv1, one tunnel. Anything else needs route-based.
2. Basic VPN gateway has no BGP, no IKEv2 or OpenVPN point-to-site, no RADIUS and no IPv6.
3. Entra ID authentication works only with OpenVPN.
4. Clients must re-download the P2S profile after gateway P2S changes or new routes.
5. Microsoft peering advertises nothing until a route filter is attached.
6. Premium is what you need for global reach across geopolitical regions and higher route limits.
7. FastPath bypasses the gateway in the data path but needs a high-end gateway SKU.
8. ExpressRoute is private but not encrypted; MACsec or IPsec adds encryption.
9. Virtual WAN Basic is S2S VPN only; anything with ExpressRoute or transit needs Standard.
10. Gateways live in `GatewaySubnet`; VPN and ExpressRoute coexisting needs a larger subnet.

---

## Key terms

- **Local network gateway** - Azure's record of the on-premises VPN device: its public IP or FQDN, prefixes or BGP settings
- **Route-based VPN** - a VPN gateway type using any-to-any selectors that supports IKEv2, BGP, active-active and point-to-site
- **Policy-based VPN** - a VPN gateway type with static traffic selectors, IKEv1 and a single tunnel, Basic SKU only
- **Active-active gateway** - both VPN gateway instances carry tunnels, each with its own public IP
- **Custom IPsec/IKE policy** - a per-connection setting that pins the encryption, integrity and DH algorithms
- **Azure Extended Network** - stretches an on-premises subnet into Azure over VXLAN so VMs migrate without re-IP
- **OpenVPN tunnel** - a TLS-based point-to-site tunnel and the only type that supports Microsoft Entra ID authentication
- **Azure private peering** - the ExpressRoute peering that connects on-premises to your VNets
- **Microsoft peering** - the ExpressRoute peering to Microsoft public services, which needs a route filter
- **ExpressRoute Premium** - the circuit SKU for global reach across geopolitical regions and higher route limits
- **ExpressRoute Global Reach** - links two ExpressRoute circuits so on-premises sites talk through Microsoft's backbone
- **FastPath** - sends ExpressRoute traffic straight to VMs, bypassing the gateway in the data path
- **MACsec** - layer 2 encryption between your routers and Microsoft's edge on ExpressRoute Direct ports
- **Bidirectional Forwarding Detection** - sub-second link failure detection that speeds up BGP failover
- **Routing intent** - a Virtual WAN hub setting that sends internet and private traffic through Azure Firewall or an NVA

---

## Vendor documentation

- **[📖 VPN Gateway documentation](https://learn.microsoft.com/en-us/azure/vpn-gateway/)** - S2S, P2S and gateway design
- **[📖 About VPN gateway SKUs](https://learn.microsoft.com/en-us/azure/vpn-gateway/about-gateway-skus)** - the current AZ SKUs and limits
- **[📖 Highly available VPN gateway designs](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-highlyavailable)** - active-active and dual redundancy
- **[📖 Custom IPsec/IKE policies](https://learn.microsoft.com/en-us/azure/vpn-gateway/ipsec-ike-policy-howto)** - pinning algorithms on a connection
- **[📖 Point-to-site authentication](https://learn.microsoft.com/en-us/azure/vpn-gateway/point-to-site-about)** - tunnel types and authentication methods
- **[📖 Azure Extended Network](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/azure/azure-extended-network)** - stretch a subnet into Azure
- **[📖 ExpressRoute overview](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction)** - models, peerings and SKUs
- **[📖 ExpressRoute circuits and peering](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-circuit-peerings)** - private and Microsoft peering
- **[📖 About FastPath](https://learn.microsoft.com/en-us/azure/expressroute/about-fastpath)** - requirements and limitations
- **[📖 ExpressRoute encryption](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-about-encryption)** - MACsec and IPsec options
- **[📖 Virtual WAN overview](https://learn.microsoft.com/en-us/azure/virtual-wan/virtual-wan-about)** - SKUs, hubs and connections
- **[📖 Virtual hub routing](https://learn.microsoft.com/en-us/azure/virtual-wan/about-virtual-hub-routing)** - association, propagation, labels and routing intent
