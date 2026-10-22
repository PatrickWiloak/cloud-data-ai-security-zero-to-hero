---
last-updated: 2026-10-22
difficulty: intermediate
---

# Azure Network Engineer Associate (AZ-700) - Practice Questions

30 questions for AZ-700 prep. Questions 16-30 follow the skills measured as of July 27, 2026: core networking infrastructure (25-30%), connectivity services (20-25%), application delivery (15-20%), network security (15-20%), and private access to Azure services (10-15%).

> **Cert page:** [exams/azure/az-700/](../../exams/azure/az-700/)

---

### Question 1
**Scenario:** Two virtual networks are peered. A VM in VNet A cannot reach a VM in VNet B, and peering status shows Connected on both sides.

A. Peering is not transitive; check that the reverse peering exists and that no NSG rule or route table blocks
B. Peering requires a VPN gateway
C. VNets in the same region cannot peer, so a Connected status only means the two VNets see each other's metadata but not data traffic
D. Peering only supports IPv6

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Connected peering gives connectivity, so the failure is almost always an NSG rule, a user-defined route sending traffic to a virtual appliance, or an overlapping address space. Peering is bidirectional and must be configured from both VNets, and it is not transitive: A-B and B-C does not give A-C without a hub route or a gateway.
</details>

---

### Question 2
**Scenario:** A subnet must send all internet-bound traffic through a network virtual appliance.

A. A user-defined route for `0.0.0.0/0` with next hop type Virtual appliance, on the subnet
B. Azure Firewall Manager policy alone, applied to the subnet without making any route table changes
C. Service endpoints
D. A Network Security Group with a deny rule for internet destinations, which forces traffic to use the appliance

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** UDRs override Azure's system routes, and a default route to a virtual appliance is the standard forced tunneling pattern. NSGs filter traffic but never redirect it. Remember the appliance's own NIC needs IP forwarding enabled, or the packets are dropped.
</details>

---

### Question 3
**Scenario:** A storage account must be reachable privately from a VNet, with a private IP in that VNet, and not over the public endpoint.

A. Service endpoint
B. VNet peering
C. Private endpoint with a private DNS zone
D. NAT gateway

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A private endpoint places a NIC with a private IP into your subnet and maps it to the PaaS resource. The part people miss is DNS: without the `privatelink` private DNS zone linked to the VNet, the name still resolves to the public IP. Service endpoints keep the public IP and merely restrict access by VNet.
</details>

---

### Question 4
**Scenario:** Outbound internet access from a subnet must use a stable, predictable set of source IPs and avoid SNAT port exhaustion.

A. An internal load balancer
B. A public IP on each VM
C. A NAT gateway associated with the subnet
D. Default outbound access, which gives each VM a fixed address from a pool dedicated to your subscription

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** NAT gateway gives a large SNAT port pool with far better scaling than load balancer outbound rules or default outbound access, and it pins egress to the public IPs or prefix you attach. Per-VM public IPs work but multiply cost and attack surface. Default outbound access is being retired and uses unpredictable addresses.
</details>

---

### Question 5
**Scenario:** An HTTPS web app needs path-based routing, WAF, and TLS termination.

A. Traffic Manager
B. Azure Load Balancer
C. Application Gateway with the WAF SKU
D. NAT gateway

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Application Gateway is the regional layer 7 load balancer, and the WAF SKU adds OWASP rule protection. Azure Load Balancer is layer 4 and cannot read paths. Traffic Manager is DNS-based global routing with no data path at all, so it cannot terminate TLS.
</details>

---

### Question 6
**Scenario:** Global HTTP traffic must be routed to the closest healthy regional backend with edge caching.

A. Azure Front Door
B. Azure Load Balancer Standard, a layer 4 service with no HTTP awareness
C. Application Gateway, a regional layer 7 service deployed into one VNet
D. ExpressRoute, a private connection between on-premises networks and Azure

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Front Door is the global layer 7 entry point with anycast, edge caching, WAF, and health-based origin selection. Application Gateway is regional. Standard Load Balancer is regional layer 4. ExpressRoute is private connectivity to Azure, not internet-facing distribution.
</details>

---

### Question 7
**Scenario:** ExpressRoute must carry traffic to Azure PaaS services, such as Azure Storage, through their public endpoints over the private connection, not the internet.

A. A site-to-site VPN gateway running over the public internet to reach those services
B. Private peering only, with the PaaS services reached through their public endpoints
C. Public peering, which is the current option for reaching Azure PaaS public IPs and needs no route filters
D. Microsoft peering, with route filters selecting the service communities

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Private peering reaches VNets by private IP address. Microsoft peering reaches Azure PaaS services and Microsoft 365 on public IP addresses, and no routes are advertised until a route filter selects the BGP service communities. Public peering is no longer offered on new circuits. If the PaaS services are reached through private endpoints in a VNet instead, private peering carries that traffic.

**Key Concept:** [ExpressRoute circuits and peering](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-circuit-peerings)
</details>

---

### Question 8
**Scenario:** A hub-and-spoke topology needs spokes to reach on-premises through the hub's VPN gateway.

A. Deploy a VPN gateway in each spoke VNet, with a separate site-to-site connection to the on-premises device, instead of using the hub's gateway
B. Use service endpoints
C. Enable "Use remote gateways" on the spoke peering and "Allow gateway transit" on the hub peering
D. Enable IP forwarding on the NICs of all spoke VMs, so that each one can relay traffic on to the hub gateway

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Gateway transit is the pair of peering settings that lets spokes use the hub's gateway. Both sides must be set, and a spoke can use only one remote gateway. Deploying a gateway per spoke works but multiplies cost and complexity, which defeats the point of a hub.
</details>

---

### Question 9
**Scenario:** BGP is configured on a site-to-site VPN and on-premises advertises `0.0.0.0/0`. What is the effect on Azure VMs?

A. Only DNS resolution is affected, because BGP routes apply to name lookups alone
B. Forced tunneling: internet-bound VM traffic is sent to on-premises
C. The tunnel drops
D. No effect, because Azure system routes always take precedence over any route learned from BGP

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A default route learned over BGP overrides Azure's system default to the internet, so egress hairpins through on-premises. Some organizations want exactly this for inspection; others discover it accidentally when connectivity to Azure services breaks. Effective routes on the NIC are the fastest way to confirm.
</details>

---

### Question 10
**Scenario:** You need to see, for a specific VM NIC, which route Azure will actually use for a destination.

A. Azure Advisor, which lists the effective route table of each NIC along with recommendations
B. The activity log, which records the control plane operations performed on each resource
C. Service Health, which reports Azure platform incidents that affect your subscription
D. Network Watcher Effective routes and IP flow verify

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Effective routes merges system routes, UDRs, BGP-learned routes, and peering, which is the only reliable view when several sources conflict. IP flow verify answers "would this specific packet be allowed" and names the NSG rule that decided. Advisor, activity logs, and Service Health do not evaluate the data path.
</details>

---

### Question 11
**Scenario:** An NSG on a subnet and another on the NIC both apply. How is inbound traffic evaluated?

A. Only the NIC NSG applies, because the NSG closest to the VM replaces the subnet NSG entirely for that VM
B. The subnet NSG is evaluated first for inbound, then the NIC NSG; each one must allow the traffic
C. The rules are merged
D. The most permissive rule wins, so an allow in either NSG is enough to let the traffic through to the VM

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** For inbound, the subnet NSG is processed then the NIC NSG, and both must allow. For outbound the order reverses. Since there is no merge and no permissive override, a deny in either place wins, which is why layered NSGs are a common cause of "the rule is right but it still fails."
</details>

---

### Question 12
**Scenario:** DNS resolution is needed for private endpoints across many VNets from an on-premises resolver.

A. Public Azure DNS zones
B. Azure DNS Private Resolver with an inbound endpoint, plus private DNS zones linked to the VNets
C. Custom DNS on every VNet pointing to 8.8.8.8, with conditional forwarders for the privatelink zones added on each VNet
D. A hosts file on each VM

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Private DNS zones are not reachable from on-premises by themselves. The Private Resolver's inbound endpoint gives on-premises a private IP to forward queries to, and the outbound endpoint plus forwarding rulesets handle the reverse direction. Public resolvers cannot see privatelink records.
</details>

---

### Question 13
**Scenario:** Virtual WAN is chosen over a manually built hub. What is the main benefit?

A. It provides layer 7 WAF and path-based routing for every branch, replacing Application Gateway entirely
B. Lower per-GB cost always
C. It removes the need for NSGs
D. Managed hubs with automated any-to-any branch, VNet, and user connectivity and built-in routing

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Virtual WAN's value is managed transit: Microsoft runs the hub routing, VPN and ExpressRoute gateways, and scale-out, so you configure connections rather than route tables. Cost is not automatically lower. Security controls and WAF are still separate services you attach.
</details>

---

### Question 14
**Scenario:** Traffic between two spokes must be inspected by Azure Firewall in the hub.

A. Peer the spokes directly, since peering forces all spoke traffic through the hub firewall for inspection
B. UDRs in each spoke pointing the other spoke's prefix at the firewall's private IP
C. Rely on NSGs on each spoke subnet to inspect the traffic and block unwanted flows between the spokes
D. Enable service endpoints on both spoke subnets so that the traffic between them is routed through the firewall

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Without a route, spoke-to-spoke traffic through peering goes directly and never touches the firewall. Explicit UDRs force the hairpin through the hub, and the firewall needs rules permitting the flow. Direct peering makes the bypass worse rather than better.
</details>

---

### Question 15
**Scenario:** You must capture packet-level evidence of a connectivity problem on a running VM.

A. Network Watcher packet capture
B. NSG flow logs
C. Connection Monitor
D. Azure Monitor metrics

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Packet capture writes a capture file from the VM extension for the depth you need to see handshakes and resets. Flow logs record allow and deny decisions per flow, which is excellent for "was it blocked" but not for payload or TCP state. Connection Monitor does synthetic reachability testing over time.
</details>

---

### Question 16
**Scenario:** An engineer creates a /29 subnet in an Azure VNet for a small appliance cluster. How many addresses can be assigned to resources?

A. 8, because Azure lets every address in the range be assigned
B. 3
C. 6, because only the network and broadcast addresses are reserved as in a typical on-premises subnet
D. 5, because Azure reserves the first and last address and one for the gateway

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Azure reserves five addresses in every subnet: the network address, the next three (default gateway and two for Azure DNS), and the last address. A /29 has 8 addresses, so 3 are usable. Treating all 8 as usable ignores the reservations. Six usable addresses is the on-premises rule, which reserves only two. Five usable addresses assumes only three reservations, but Azure reserves five.
</details>

---

### Question 17
**Scenario:** A platform service that injects resources into a customer VNet requires a subnet dedicated to it, and other resources must not be placed there.

A. Attach a NAT gateway to the subnet so only that service can send outbound traffic from it
B. Create a service endpoint on the subnet for the platform service
C. Apply an NSG to the subnet that denies all inbound traffic from other subnets in the VNet
D. Delegate the subnet to the service

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Subnet delegation hands a subnet to a specific Azure service, which can then create its resources there and apply its own policies, and the subnet is reserved for it. A NAT gateway controls outbound source IPs, not who can use the subnet. A service endpoint optimizes routing to a PaaS service's public endpoint and does not reserve the subnet. An NSG filters traffic but does not stop other resources being deployed in the subnet.
</details>

---

### Question 18
**Scenario:** A third-party SD-WAN appliance in a hub VNet must exchange routes dynamically with Azure so that spoke VNets learn on-premises prefixes without hand-maintained route tables.

A. Deploy Azure Route Server and peer it with the appliance over BGP
B. Create a user-defined route in every spoke pointing each on-premises prefix to the appliance
C. Enable gateway transit on the hub peering without any gateway or Route Server in the hub VNet
D. Use Azure DNS Private Resolver to forward the prefixes

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Azure Route Server speaks BGP with network virtual appliances and programs the learned routes into the VNet and its peered spokes, so routes stay current without manual tables. UDRs in every spoke work but must be maintained by hand. Gateway transit shares a VPN or ExpressRoute gateway, and with no gateway or Route Server there is nothing to share. DNS Private Resolver handles name resolution, not routing.
</details>

---

### Question 19
**Scenario:** An organization has 60 VNets across subscriptions and wants to define hub-and-spoke connectivity once and have peerings created and kept consistent automatically.

A. Script VNet peerings with a scheduled runbook that checks each pair nightly and recreates missing ones
B. Deploy a VPN gateway in every VNet and connect them all with VNet-to-VNet connections
C. Use Azure Virtual Network Manager with a connectivity configuration and network groups
D. Use Azure Front Door

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Azure Virtual Network Manager applies connectivity configurations, such as hub-and-spoke or mesh, to network groups that can be defined dynamically, and keeps the peerings in place across subscriptions. A scheduled script works but is custom code to own and leaves gaps between runs. VPN gateways in every VNet add cost and throughput limits for no benefit over peering. Front Door is an application delivery service, not VNet connectivity.
</details>

---

### Question 20
**Scenario:** A VNet needs several site-to-site VPN connections to different branches plus point-to-site connections for remote staff on the same gateway.

A. A policy-based VPN gateway
B. A local network gateway with no virtual network gateway, which handles both connection types
C. An ExpressRoute gateway, which supports site-to-site and point-to-site connections natively
D. A route-based VPN gateway

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Route-based VPN gateways support multiple site-to-site tunnels, point-to-site, and BGP, so one gateway can serve branches and remote users. Policy-based gateways are limited to one site-to-site tunnel and do not support point-to-site. A local network gateway only represents the on-premises side; it cannot terminate tunnels on its own. ExpressRoute gateways carry ExpressRoute circuits, not VPN connections.
</details>

---

### Question 21
**Scenario:** Remote staff must connect with point-to-site VPN and sign in with their Microsoft Entra ID accounts and MFA.

A. Use the IKEv2 tunnel type with certificate authentication only
B. Use the OpenVPN tunnel type with Microsoft Entra ID authentication
C. Use the SSTP tunnel type with RADIUS shared secrets stored on each client device
D. Use a site-to-site connection from each user's home router

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Microsoft Entra ID authentication for point-to-site requires the OpenVPN protocol, and it allows Conditional Access and MFA through the Azure VPN Client. IKEv2 with certificates authenticates the device certificate, not the Entra ID account. SSTP with RADIUS can work with other directories but is not native Entra ID sign-in. Site-to-site from home routers is unmanageable and does not authenticate individual users.
</details>

---

### Question 22
**Scenario:** Two on-premises data centers each have their own ExpressRoute circuit to Azure. The company wants them to talk to each other over the Microsoft backbone.

A. Enable ExpressRoute Global Reach between the two circuits
B. Peer the two ExpressRoute gateways with VNet peering so the data centers can share routes
C. Turn on FastPath on both circuits
D. Build a site-to-site VPN from each data center to the internet and route through it

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Global Reach links two ExpressRoute circuits so the on-premises sites behind them exchange traffic over Microsoft's backbone. VNet peering connects VNets, not circuits, and does not pass on-premises to on-premises traffic. FastPath sends traffic from the gateway straight to VMs, improving data path performance, but does not connect circuits. A VPN over the internet is a different path and does not use the backbone.
</details>

---

### Question 23
**Scenario:** A pair of VMs runs a TCP-based database listener inside a VNet. Clients in the same and peered VNets need one private IP that fails over between the VMs. HTTP features are not needed.

A. A public Standard Load Balancer with an inbound NAT rule for the database port
B. Azure Application Gateway with a TCP listener and URL-based routing to the two VMs
C. An internal Standard Load Balancer with a health probe on the listener port
D. Azure Traffic Manager with priority routing

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** An internal Standard Load Balancer gives a private frontend IP and sends layer 4 traffic only to backends that pass the health probe, which suits a non-HTTP listener. A public load balancer exposes the service to the internet. Application Gateway is built for HTTP and HTTPS, and URL-based routing does not apply to a database protocol. Traffic Manager works through DNS and is meant for global endpoints, not a private IP in one VNet.
</details>

---

### Question 24
**Scenario:** A non-HTTP service runs in two regions. Clients should be sent to the primary region and only to the secondary if the primary's endpoint fails health checks.

A. Azure Front Door with weighted routing between the two regional endpoints
B. A cross-region load balancer in Basic tier with session persistence to the primary region
C. Two NSG rules that allow traffic to the primary and deny it to the secondary until a failure
D. Azure Traffic Manager with the priority routing method

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Traffic Manager answers DNS queries with the highest-priority healthy endpoint, so it fails over to the secondary only when the primary is unhealthy, and it works for any protocol. Front Door only handles HTTP and HTTPS. The cross-region load balancer is a Standard SKU feature, and session persistence is not failover. NSG rules filter traffic and cannot react to health checks.
</details>

---

### Question 25
**Scenario:** An App Service origin behind Azure Front Door must not be reachable over the public internet at all, only through Front Door.

A. Restrict the origin's access to the Front Door service tag, and leave its public endpoint enabled for health checks
B. Use Front Door Premium with Private Link to the origin and disable the origin's public access
C. Put the origin behind a second Front Door profile in a different region
D. Turn on Front Door caching for every path

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Front Door Premium can connect to supported origins through Private Link, so the origin's public access can be turned off and only Front Door reaches it privately. Service tag restrictions with header checks are a valid hardening step, but the endpoint stays public, which fails "not reachable at all". A second profile adds nothing to origin exposure. Caching reduces origin load but does not change who can reach it.
</details>

---

### Question 26
**Scenario:** VMs in a subnet use a service endpoint for Azure Storage. Security wants them to reach only the company's two storage accounts, not any storage account in Azure.

A. Apply a service endpoint policy to the subnet that allows only those two accounts
B. Remove the service endpoint and add an NSG rule allowing the Storage service tag in every region
C. Add a user-defined route sending storage traffic to the internet
D. Enable soft delete on both storage accounts

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Service endpoint policies filter service endpoint traffic to specific Azure Storage accounts, which blocks data exfiltration to other accounts. The Storage service tag covers every storage account in the region, so it does not narrow anything. A UDR to the internet removes the service endpoint path and adds no filtering. Soft delete protects data from deletion and has no effect on network access.
</details>

---

### Question 27
**Scenario:** After creating a private endpoint for a storage account, VMs in the VNet still resolve the account's name to its public IP.

A. Restart the storage account so it picks up the new private endpoint and updates public DNS
B. Assign a public IP to the private endpoint's network interface
C. Link the `privatelink.blob.core.windows.net` private DNS zone, with the endpoint's record, to the VNet
D. Add the private IP to every VM's hosts file

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Private endpoint name resolution relies on a private DNS zone for the `privatelink` subdomain holding the endpoint's A record, linked to the VNets that query it, so the public name resolves to the private IP. Storage accounts are not restarted, and public DNS should keep returning the public address for outside clients. Private endpoints do not take public IPs. Hosts files work but do not scale and break when IPs change.
</details>

---

### Question 28
**Scenario:** NSG rules must allow port 443 from load balancer health probes to all web VMs, and new web VMs should be covered without editing IP addresses in rules.

A. List each web VM's private IP in the rule and update it whenever a VM is added or removed
B. Create one NSG per VM and copy the same rules to each one with a script that runs at deployment
C. Use a service endpoint for the web tier so the NSG matches the web VMs automatically
D. Put the web VMs' NICs in an application security group and use it as the rule's destination

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Application security groups let NSG rules target a group of NICs by role, so adding a VM to the group applies the rule with no IP changes. Listing IPs is brittle and needs edits for every change. Per-VM NSGs multiply the rule sets to keep in sync. Service endpoints route traffic to PaaS services and are not a way to group VMs in rules.
</details>

---

### Question 29
**Scenario:** A hub firewall must inspect encrypted outbound HTTPS traffic for threats and apply signature-based intrusion detection and prevention.

A. Azure Firewall Premium with TLS inspection and IDPS enabled
B. Azure Firewall Basic with threat intelligence set to alert only for outbound HTTPS traffic
C. NSG flow logs analysed in Log Analytics after the traffic has passed
D. Azure DDoS Network Protection on the hub VNet

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Azure Firewall Premium adds TLS inspection, which decrypts and re-encrypts traffic, and signature-based IDPS, which is exactly the requirement. Basic offers threat intelligence alerts but not TLS inspection or IDPS. Flow logs record traffic metadata after the fact and inspect nothing. DDoS protection defends against volumetric attacks, not threats inside encrypted sessions.
</details>

---

### Question 30
**Scenario:** A new WAF policy on Application Gateway is about to protect a busy app. The team worries managed rules will block legitimate requests.

A. Disable all managed rule sets and rely on custom rules written by the team over time
B. Start in detection mode, review the logs, add exclusions, then switch to prevention mode
C. Put the WAF in prevention mode on day one and roll back if users complain about blocks
D. Use NSG rules instead of WAF

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Detection mode logs what would be blocked without blocking it, so the team can tune exclusions against real traffic before enforcing prevention mode. Disabling managed rules drops most of the protection. Going straight to prevention risks blocking real users before tuning. NSGs filter by IP, port and protocol, not by HTTP content, so they cannot replace a WAF.
</details>

---

## Where to go deeper

- [AZ-700 cert page](../../exams/azure/az-700/) - notes, practice plan, strategy
- [AZ-104 practice questions](./azure-administrator-az-104.md) - the prerequisite skill set
- [VPC explained](../../learn/concepts/vpc-explained.md) - cloud networking fundamentals
- [Networking topic index](../../topics/networking.md) - cross-cloud comparisons
- **[📖 AZ-700 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-700)** - official skills outline
