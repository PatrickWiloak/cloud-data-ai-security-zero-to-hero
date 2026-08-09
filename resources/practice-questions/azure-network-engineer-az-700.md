---
last-updated: 2026-08-09
difficulty: intermediate
---

# Azure Network Engineer Associate (AZ-700) - Practice Questions

15 questions for AZ-700 prep, weighted toward routing (25-30%) and core networking infrastructure (20-25%), then private access, monitoring, and hybrid connectivity.

> **Cert page:** [exams/azure/az-700/](../../exams/azure/az-700/)

---

### Question 1
**Scenario:** Two virtual networks are peered. A VM in VNet A cannot reach a VM in VNet B, and peering status shows Connected on both sides.

A. Peering is not transitive; check that both peerings exist and that NSGs or a route table are not blocking
B. Peering requires a VPN gateway
C. VNets in the same region cannot peer
D. Peering only supports IPv6

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Connected peering gives connectivity, so the failure is almost always an NSG rule, a user-defined route sending traffic to a virtual appliance, or an overlapping address space. Peering is bidirectional and must be configured from both VNets, and it is not transitive: A-B and B-C does not give A-C without a hub route or a gateway.
</details>

---

### Question 2
**Scenario:** A subnet must send all internet-bound traffic through a network virtual appliance.

A. A Network Security Group with a deny rule
B. A user-defined route with address prefix `0.0.0.0/0` and next hop type Virtual appliance, associated with the subnet
C. Azure Firewall Manager policy alone
D. Service endpoints

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** UDRs override Azure's system routes, and a default route to a virtual appliance is the standard forced tunneling pattern. NSGs filter traffic but never redirect it. Remember the appliance's own NIC needs IP forwarding enabled, or the packets are dropped.
</details>

---

### Question 3
**Scenario:** A storage account must be reachable privately from a VNet, with a private IP in that VNet, and not over the public endpoint.

A. Service endpoint
B. Private endpoint with a private DNS zone
C. NAT gateway
D. VNet peering

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A private endpoint places a NIC with a private IP into your subnet and maps it to the PaaS resource. The part people miss is DNS: without the `privatelink` private DNS zone linked to the VNet, the name still resolves to the public IP. Service endpoints keep the public IP and merely restrict access by VNet.
</details>

---

### Question 4
**Scenario:** Outbound internet access from a subnet must use a stable, predictable set of source IPs and avoid SNAT port exhaustion.

A. A NAT gateway associated with the subnet
B. A public IP on each VM
C. Default outbound access
D. An internal load balancer

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** NAT gateway gives a large SNAT port pool with far better scaling than load balancer outbound rules or default outbound access, and it pins egress to the public IPs or prefix you attach. Per-VM public IPs work but multiply cost and attack surface. Default outbound access is being retired and uses unpredictable addresses.
</details>

---

### Question 5
**Scenario:** An HTTPS web app needs path-based routing, WAF, and TLS termination.

A. Azure Load Balancer
B. Application Gateway with the WAF SKU
C. Traffic Manager
D. NAT gateway

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Application Gateway is the regional layer 7 load balancer, and the WAF SKU adds OWASP rule protection. Azure Load Balancer is layer 4 and cannot read paths. Traffic Manager is DNS-based global routing with no data path at all, so it cannot terminate TLS.
</details>

---

### Question 6
**Scenario:** Global HTTP traffic must be routed to the closest healthy regional backend with edge caching.

A. Azure Front Door
B. Application Gateway
C. Azure Load Balancer Standard
D. ExpressRoute

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Front Door is the global layer 7 entry point with anycast, edge caching, WAF, and health-based origin selection. Application Gateway is regional. Standard Load Balancer is regional layer 4. ExpressRoute is private connectivity to Azure, not internet-facing distribution.
</details>

---

### Question 7
**Scenario:** ExpressRoute must carry traffic to Azure PaaS services over the private connection, not the internet.

A. Private peering only
B. Microsoft peering, with route filters selecting the service communities
C. Public peering
D. A site-to-site VPN

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Private peering reaches VNets. Microsoft peering reaches public Microsoft services such as Azure Storage and Microsoft 365, and a route filter is required to select which BGP communities are advertised. Public peering is the deprecated predecessor to Microsoft peering.
</details>

---

### Question 8
**Scenario:** A hub-and-spoke topology needs spokes to reach on-premises through the hub's VPN gateway.

A. Enable "Use remote gateways" on the spoke peering and "Allow gateway transit" on the hub peering
B. Deploy a VPN gateway in each spoke
C. Use service endpoints
D. Enable IP forwarding on the spoke VMs

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Gateway transit is the pair of peering settings that lets spokes use the hub's gateway. Both sides must be set, and a spoke can use only one remote gateway. Deploying a gateway per spoke works but multiplies cost and complexity, which defeats the point of a hub.
</details>

---

### Question 9
**Scenario:** BGP is configured on a site-to-site VPN and on-premises advertises `0.0.0.0/0`. What is the effect on Azure VMs?

A. No effect
B. Forced tunneling: internet-bound VM traffic is sent to on-premises
C. The tunnel drops
D. Only DNS is affected

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A default route learned over BGP overrides Azure's system default to the internet, so egress hairpins through on-premises. Some organizations want exactly this for inspection; others discover it accidentally when connectivity to Azure services breaks. Effective routes on the NIC are the fastest way to confirm.
</details>

---

### Question 10
**Scenario:** You need to see, for a specific VM NIC, which route Azure will actually use for a destination.

A. Network Watcher Effective routes and IP flow verify
B. Azure Advisor
C. The activity log
D. Service Health

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Effective routes merges system routes, UDRs, BGP-learned routes, and peering, which is the only reliable view when several sources conflict. IP flow verify answers "would this specific packet be allowed" and names the NSG rule that decided. Advisor, activity logs, and Service Health do not evaluate the data path.
</details>

---

### Question 11
**Scenario:** An NSG on a subnet and another on the NIC both apply. How is inbound traffic evaluated?

A. Only the NIC NSG applies
B. The subnet NSG is evaluated first for inbound, then the NIC NSG; traffic must be allowed by both
C. The rules are merged
D. The most permissive wins

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** For inbound, the subnet NSG is processed then the NIC NSG, and both must allow. For outbound the order reverses. Since there is no merge and no permissive override, a deny in either place wins, which is why layered NSGs are a common cause of "the rule is right but it still fails."
</details>

---

### Question 12
**Scenario:** DNS resolution is needed for private endpoints across many VNets from an on-premises resolver.

A. Azure DNS Private Resolver with an inbound endpoint, plus private DNS zones linked to the VNets
B. Public Azure DNS zones
C. A hosts file on each VM
D. Custom DNS on every VNet pointing to 8.8.8.8

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Private DNS zones are not reachable from on-premises by themselves. The Private Resolver's inbound endpoint gives on-premises a private IP to forward queries to, and the outbound endpoint plus forwarding rulesets handle the reverse direction. Public resolvers cannot see privatelink records.
</details>

---

### Question 13
**Scenario:** Virtual WAN is chosen over a manually built hub. What is the main benefit?

A. Lower per-GB cost always
B. Managed hubs with automated any-to-any branch, VNet, and user connectivity and built-in routing
C. It removes the need for NSGs
D. It provides layer 7 WAF

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Virtual WAN's value is managed transit: Microsoft runs the hub routing, VPN and ExpressRoute gateways, and scale-out, so you configure connections rather than route tables. Cost is not automatically lower. Security controls and WAF are still separate services you attach.
</details>

---

### Question 14
**Scenario:** Traffic between two spokes must be inspected by Azure Firewall in the hub.

A. Peer the spokes directly
B. UDRs in each spoke sending the other spoke's prefix to the firewall private IP as next hop
C. Rely on NSGs
D. Enable service endpoints

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Without a route, spoke-to-spoke traffic through peering goes directly and never touches the firewall. Explicit UDRs force the hairpin through the hub, and the firewall needs rules permitting the flow. Direct peering makes the bypass worse rather than better.
</details>

---

### Question 15
**Scenario:** You must capture packet-level evidence of a connectivity problem on a running VM.

A. NSG flow logs
B. Network Watcher packet capture
C. Connection Monitor
D. Azure Monitor metrics

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Packet capture writes a capture file from the VM extension for the depth you need to see handshakes and resets. Flow logs record allow and deny decisions per flow, which is excellent for "was it blocked" but not for payload or TCP state. Connection Monitor does synthetic reachability testing over time.
</details>

---

## Where to go deeper

- [AZ-700 cert page](../../exams/azure/az-700/) - notes, practice plan, strategy
- [AZ-104 practice questions](./azure-administrator-az-104.md) - the prerequisite skill set
- [VPC explained](../../learn/concepts/vpc-explained.md) - cloud networking fundamentals
- [Networking topic index](../../topics/networking.md) - cross-cloud comparisons
- **[📖 AZ-700 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-700)** - official skills outline
