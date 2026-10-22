---
last-updated: 2026-10-22
difficulty: advanced
---

# AWS Certified Advanced Networking - Specialty (ANS-C01) - Practice Questions

30 questions for ANS-C01 prep, weighted toward network design (30%), implementation (26%), security and compliance (24%), and management and operation (20%).

> **Cert page:** [exams/aws/specialty/advanced-networking-ans-c01/](../../exams/aws/specialty/advanced-networking-ans-c01/)

---

### Question 1
**Scenario:** Fifty VPCs across several accounts must communicate with each other and with on-premises, with centralized routing.

A. AWS Transit Gateway with route tables and attachments, shared across accounts through Resource Access Manager, giving centralized routing
B. Full-mesh VPC peering between all fifty VPCs, with route tables in each VPC updated so any VPC reaches any other directly
C. A Site-to-Site VPN per VPC pair, which encrypts traffic between accounts and propagates routes through BGP on each tunnel
D. PrivateLink for everything, with an endpoint service in each VPC and interface endpoints created in every other VPC

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Peering is non-transitive and a 50-VPC mesh needs 1,225 connections, which is unmanageable. Transit Gateway is a hub with attachment-level route tables that give you segmentation, and RAM shares it across accounts. PrivateLink exposes individual services rather than providing general routing.
</details>

---

### Question 2
**Scenario:** Two VPCs have overlapping CIDR blocks and one application in each must talk to the other.

A. PrivateLink to expose just the specific service, or NAT the overlapping ranges through a middlebox appliance
B. Add a more specific route to the remote subnet, so longest prefix match overrides the local route
C. VPC peering, with a route to the remote CIDR in each route table
D. Transit Gateway, with each VPC attached and a route table that forwards traffic between the two overlapping CIDR blocks

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Neither peering nor Transit Gateway supports overlapping CIDRs, because routing becomes ambiguous. PrivateLink sidesteps it entirely by presenting the service on an endpoint in the consumer's address space. Adding a more specific route cannot help, because the local VPC route always wins. Re-addressing a VPC would work but is the most disruptive option.
</details>

---

### Question 3
**Scenario:** A Direct Connect connection must be resilient to a single device or location failure.

A. One connection with a VPN backup only, which restores connectivity but leaves the single location and device as a failure point
B. Two connections at two different Direct Connect locations, ideally with diverse providers, plus BGP failover
C. Two connections on the same router at one location, which survive a cable cut but share the device and site as a failure domain
D. A single 100 Gbps connection, which is plenty of bandwidth but one circuit, device, and location

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Maximum resilience requires separate locations and separate devices, because two circuits into the same router share a failure domain. A VPN backup is a reasonable lower tier but has different bandwidth and latency characteristics, which changes application behavior during failover.
</details>

---

### Question 4
**Scenario:** Traffic from on-premises prefers one Direct Connect path over another.

A. Static routes only, set on the on-premises router and the virtual interface to pin the path
B. BGP attributes: AS path prepending or local preference to influence path selection in each direction
C. Route table priorities in the VPC, where setting a lower number on one target makes AWS prefer that Direct Connect path
D. DNS, by returning different addresses for the on-premises endpoints so clients choose the path

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** AWS uses BGP path selection, so influencing it means using BGP attributes, and each direction is controlled separately: longest prefix match first, then local preference for AWS-to-on-premises, and AS path prepending to influence what AWS prefers. Asymmetric routing is the usual symptom of getting one direction wrong.
</details>

---

### Question 5
**Scenario:** Private DNS resolution is needed between on-premises and a VPC in both directions.

A. Host files on every server and client, each holding the other side's private names
B. A NAT gateway in each VPC, which lets private instances reach on-premises DNS servers through a translated address range
C. Public hosted zones that hold the private records, which hosts on either side can query over the internet
D. Route 53 Resolver inbound and outbound endpoints with conditional forwarding rules for the on-premises domains

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Inbound endpoints give on-premises resolvers an IP in the VPC to query for private zones, and outbound endpoints with rules forward VPC queries for on-premises domains to your resolvers. Both are needed for bidirectional resolution, and forgetting one is the standard hybrid DNS bug.
</details>

---

### Question 6
**Scenario:** All egress to the internet from many VPCs must be inspected centrally.

A. A NAT gateway per VPC, with each VPC's own firewall rules, which provides egress but leaves inspection scattered and uneven
B. Security groups on the instances in every VPC, which filter by port and protocol but cannot inspect traffic content centrally
C. A central inspection VPC with Network Firewall or appliances, reached through Transit Gateway with appliance mode
D. NACLs on each VPC's subnets, which allow or deny by address and port but cannot inspect application traffic or be managed centrally

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Centralized inspection needs traffic steered through a hub, and appliance mode on the Transit Gateway attachment ensures both directions of a flow use the same appliance, which stateful inspection requires. Without appliance mode, asymmetric routing breaks the firewall's state table.
</details>

---

### Question 7
**Scenario:** A Network Load Balancer must preserve the client IP for backends.

A. Use X-Forwarded-For on the NLB, so that backends read the client address from a header added to each request
B. It is impossible, because a layer 4 load balancer always replaces the client address with its own on each connection
C. Use an Application Load Balancer instead, which passes the original client address through to targets unchanged at layer 4
D. Enable proxy protocol v2, or use target type IP or instance where preservation applies

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** NLB operates at layer 4, so there is no HTTP header to add: client IP preservation depends on the target type and setting, and proxy protocol carries the original addresses when preservation is not available. X-Forwarded-For is an ALB (layer 7) mechanism.
</details>

---

### Question 8
**Scenario:** An application must be reachable from another VPC without exposing the whole VPC.

A. Transit Gateway, which connects the two VPCs and lets any resource in one reach any resource in the other that the routes allow
B. PrivateLink: an endpoint service backed by an NLB, consumed by the other VPC through interface endpoints
C. A public ALB with an internet-facing listener, restricted to the other VPC's NAT gateway addresses
D. VPC peering with security group rules limiting access to one app, though routes still exist

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** PrivateLink is unidirectional and service-scoped: the consumer reaches exactly one service and nothing else, with no route between the VPCs. This makes it the right tool for SaaS-style exposure between organizations, and it also works with overlapping CIDRs.
</details>

---

### Question 9
**Scenario:** A packet capture is needed for a production EC2 instance's traffic without touching the instance.

A. VPC Flow Logs, which record metadata but not the packets themselves
B. A tcpdump session on the instance, which captures packets but needs access to the host and adds load to it
C. CloudTrail, which records API calls made in the account but does not capture network traffic from the instance
D. VPC Traffic Mirroring of the instance's network interface to a monitoring appliance

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Traffic Mirroring copies packets, including payload, to a target for analysis with no agent on the source. Flow Logs record metadata about flows (source, destination, ports, action) but not contents, so they answer "was it allowed" rather than "what was in it."
</details>

---

### Question 10
**Scenario:** Global users need low-latency TCP access to regional endpoints with fast failover.

A. Route 53 latency routing alone, which returns the nearest endpoint but relies on resolvers refreshing their cache for failover
B. An internet-facing NLB in one region, which gives a static IP per zone but sends all users to that single region
C. AWS Global Accelerator with static anycast IPs, entering the AWS backbone at the nearest edge and failing over on health checks without DNS caching
D. Amazon CloudFront, which caches and accelerates HTTP content at the edge but is not designed for general TCP traffic

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Global Accelerator gives static anycast addresses, enters the AWS backbone at the nearest edge, and shifts traffic on health checks in seconds without waiting for DNS TTLs. CloudFront is the right answer for cacheable HTTP; DNS-based routing is slower to fail over because resolvers cache.
</details>

---

### Question 11
**Scenario:** IPv6 must be supported for outbound-only connectivity from private subnets.

A. An egress-only internet gateway
B. A NAT instance with source and destination checks disabled, which translates addresses for IPv4 but not for IPv6 traffic
C. A NAT gateway in a public subnet, which provides outbound IPv4 translation but does not handle IPv6 egress
D. An internet gateway with a route for ::/0, which gives outbound IPv6 but also allows connections to be started from outside

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** IPv6 addresses are globally routable, so there is no NAT in the IPv4 sense. The egress-only internet gateway is the stateful device that allows outbound IPv6 and blocks inbound. Using a plain internet gateway would make the instances directly reachable from the internet.
</details>

---

### Question 12
**Scenario:** A VPN over Direct Connect is required so traffic is encrypted end to end.

A. It is not supported, because Direct Connect traffic is already private and cannot be wrapped in an IPsec tunnel
B. Run a Site-to-Site VPN over a Direct Connect public VIF, or use MACsec on supported connections
C. Rely on application TLS only, which protects each session but leaves the rest of the traffic unencrypted
D. Use a private VIF alone, which isolates traffic from the internet but does not add encryption to the connection

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Direct Connect is private but not encrypted by default. Running an IPsec VPN over a public VIF adds encryption at the cost of throughput per tunnel, and MACsec provides layer 2 encryption on supported dedicated connections at line rate. Which one fits depends on the bandwidth requirement.
</details>

---

### Question 13
**Scenario:** Flow Logs show `REJECT` for return traffic to an instance that initiated a connection.

A. A network ACL is blocking the ephemeral port range on the return path, because NACLs are stateless and evaluate each direction on its own
B. A DNS failure, since the instance cannot resolve the remote hostname and so its return packets are rejected at the subnet
C. The security group is wrong because it lacks an inbound rule for the reply, as security groups are stateless for return traffic
D. The route table is wrong, so replies are sent to a gateway that drops them instead of delivering them to the instance

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Security groups are stateful, so a permitted outbound flow returns automatically. NACLs evaluate each direction independently, so the inbound rule must allow the ephemeral port range (typically 1024-65535) for responses. This is the classic asymmetry the exam tests.
</details>

---

### Question 14
**Scenario:** A Transit Gateway must keep production and development traffic separated while both reach a shared services VPC.

A. One route table for everything, with security groups used to separate production from development at each attachment
B. Separate Transit Gateways for production and development, with the shared services VPC attached to only one of them, so the other gateway cannot reach it
C. Separate TGW route tables per segment, with associations and propagations so prod and dev reach shared services but not each other
D. Security groups only, referencing production and development groups, because a Transit Gateway cannot separate traffic between attachments by itself

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Segmentation on a Transit Gateway comes from route table design: which attachments associate to which table, and which routes propagate into it. This is the standard shared-services pattern and it is cheaper and simpler than running multiple gateways.
</details>

---

### Question 15
**Scenario:** DNS queries for an S3 VPC gateway endpoint resolve to public IPs and traffic leaves the VPC.

A. Use a NAT gateway for the subnet, which lets instances reach S3 but sends the traffic through a public path with processing fees
B. Change the VPC's DNS server to a custom resolver that returns private addresses for the S3 endpoint
C. Gateway endpoints work by route table prefix lists; verify the endpoint's route is in the subnet's route table
D. Add an interface endpoint only and remove the gateway endpoint, since gateway endpoints cannot keep S3 traffic private

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Gateway endpoints for S3 and DynamoDB work by injecting a prefix list route, not by changing DNS, so the resolved address stays public while the route keeps traffic inside AWS. Interface endpoints are the DNS-based alternative and are what you need for on-premises access over Direct Connect.
</details>

---

### Question 16
**Scenario:** SD-WAN virtual appliances run in a transit VPC and must exchange routes dynamically with a Transit Gateway, with more throughput per tunnel than an IPsec VPN attachment gives.

A. A Site-to-Site VPN attachment from each appliance, with ECMP enabled across many IPsec tunnels to add bandwidth
B. Static routes on the Transit Gateway route table pointing at the appliance VPC attachment, updated by a Lambda function
C. VPC peering between the appliance VPC and each spoke, with the appliances advertising spoke routes over BGP
D. A Transit Gateway Connect attachment over the VPC attachment, using GRE tunnels with BGP to the appliances

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Transit Gateway Connect is built for SD-WAN appliances: it rides on an existing VPC or Direct Connect transport attachment, uses GRE rather than IPsec, and runs BGP for dynamic routing, with higher bandwidth per tunnel than a VPN. ECMP over many VPN tunnels works but adds IPsec overhead and tunnel sprawl. Static routes maintained by a function are not dynamic routing. Peering is non-transitive and does not exchange routes with BGP.
</details>

---

### Question 17
**Scenario:** A security team wants to stop workloads in a VPC from resolving known malicious and data-exfiltration domains, using a managed threat list.

A. Route 53 Resolver DNS Firewall with an AWS managed domain list rule group associated with the VPC
B. A network ACL denying outbound UDP and TCP port 53 to every IP address outside the VPC CIDR range
C. A security group rule on each instance that blocks outbound traffic to the malicious domains by name
D. GuardDuty findings for DNS activity, which block the query automatically when a domain is flagged

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** DNS Firewall filters queries that go through the Route 53 Resolver and offers AWS managed domain lists for malware and similar threats, with block, alert, or allow actions. Blocking port 53 outward does nothing to queries sent to the VPC resolver, which is the path that matters. Security groups match IPs and prefix lists, not domain names. GuardDuty detects suspicious DNS activity but does not block it on its own.
</details>

---

### Question 18
**Scenario:** Outbound HTTPS from private subnets must be allowed only to an approved list of domains, without decrypting the traffic, using an AWS managed service.

A. A NAT gateway with a security group listing the approved domains as outbound destinations
B. AWS Network Firewall with a stateful domain list rule group that matches the TLS SNI of each connection
C. A gateway VPC endpoint policy that lists the approved domains for all internet-bound HTTPS traffic
D. Route 53 private hosted zones that answer only for the approved domains and return nothing else

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Network Firewall stateful domain list rules inspect the SNI in the TLS handshake (and the Host header for HTTP), so they filter by domain without decryption. NAT gateways have no security groups. Gateway endpoints exist only for S3 and DynamoDB and their policies do not govern general internet traffic. A restrictive DNS setup can be bypassed by connecting straight to an IP address.
</details>

---

### Question 19
**Scenario:** An instance cannot reach a database in another VPC across a Transit Gateway. The engineer wants to find which configuration blocks the path without sending any packets.

A. VPC Flow Logs, filtered on the database IP, to find the rejected packets and the component that dropped them
B. Traffic Mirroring of the instance ENI, with the captures analyzed for TCP resets coming from the database side
C. VPC Reachability Analyzer, which models the path and names the route table, security group, or ACL that blocks it
D. CloudWatch Network Monitor probes from the instance subnet, reporting packet loss and latency toward the database

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Reachability Analyzer performs static configuration analysis between a source and destination, including across Transit Gateways and peering, and identifies the blocking component without sending traffic. Flow Logs need real traffic and show accept or reject but not which rule or route caused it. Traffic Mirroring also needs real packets and shows symptoms, not causes. Network Monitor measures loss and latency on a working path rather than explaining a broken one.
</details>

---

### Question 20
**Scenario:** An auditor requires proof that no database subnet in any VPC of an account has a network path from an internet gateway, and wants it re-checked regularly.

A. AWS Config rules that confirm every database instance uses a security group with no inbound rules from any address
B. A quarterly penetration test from outside AWS, scanning the public IP ranges allocated to the account
C. VPC Reachability Analyzer runs between the internet gateway and every database ENI, repeated one pair at a time
D. Network Access Analyzer with a scope that defines internet gateway to database subnet paths as findings

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Network Access Analyzer evaluates network access scopes, such as "any path from an internet gateway to these resources", across the account and reports every matching path, which suits compliance checks. Reachability Analyzer checks one source and destination at a time and does not scale to "prove none exist". A Config rule on security groups ignores routes and ACLs and so misses real paths. An external scan can miss paths and is not continuous.
</details>

---

### Question 21
**Scenario:** A company has one Direct Connect connection and Transit Gateways in three AWS Regions. On-premises must reach VPCs in all three Regions over that connection.

A. A transit virtual interface to a Direct Connect gateway, associated with all three Transit Gateways
B. A private virtual interface to a virtual private gateway in each Region, one VIF per Region on the connection
C. A public virtual interface, with traffic to the VPCs routed over the public endpoints of each Region
D. A transit virtual interface in the home Region only, with inter-Region peering of the Transit Gateways for the rest

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A Direct Connect gateway is a global resource: one transit VIF to it, associated with Transit Gateways in several Regions, gives on-premises reach to all of them. Private VIFs attach to virtual private gateways per VPC and do not scale to Transit Gateways. A public VIF reaches public service endpoints, not private VPC addresses. Transit Gateway peering does not propagate routes learned from Direct Connect to the peer, so the remote Regions would not be reachable.
</details>

---

### Question 22
**Scenario:** Spoke VPC traffic is sent through firewall appliances in an inspection VPC attached to a Transit Gateway. Return traffic sometimes lands on an appliance in a different Availability Zone and is dropped as asymmetric.

A. Add more appliances in every Availability Zone so that each zone has enough capacity for all the flows
B. Enable appliance mode on the inspection VPC attachment so each flow uses the same zone in both directions
C. Disable cross-zone load balancing on the Transit Gateway so traffic always stays in the zone it started in
D. Replace the Transit Gateway with VPC peering between each spoke VPC and the inspection VPC

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** By default a Transit Gateway keeps traffic in the source Availability Zone, so the two directions of a flow can use different zones and hit different stateful appliances. Appliance mode on the inspection VPC attachment makes the Transit Gateway pick one network interface per flow using a flow hash, keeping both directions on the same appliance. Adding capacity does not fix asymmetry. There is no cross-zone setting on a Transit Gateway. Peering is non-transitive and cannot send spoke-to-spoke traffic through the inspection VPC.
</details>

---

### Question 23
**Scenario:** An Application Load Balancer must sit in private subnets with no public exposure, while users reach the application through Amazon CloudFront.

A. Make the ALB internet-facing and restrict its security group to the CloudFront managed prefix list only
B. Put an NLB with Elastic IPs in front of the ALB and point CloudFront at the NLB's public addresses
C. Use a CloudFront VPC origin that targets the internal ALB, so the ALB needs no public address at all
D. Use AWS Global Accelerator in front of the internal ALB and point CloudFront at the accelerator's IPs

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** CloudFront VPC origins let a distribution reach an internal ALB, NLB, or EC2 instance in private subnets, so the origin has no internet exposure at all. The prefix-list approach is a valid hardening pattern but still leaves the ALB internet-facing, which the requirement rules out. An NLB with Elastic IPs is a public entry point. Global Accelerator would also be a public entry point and adds a hop for no benefit.
</details>

---

### Question 24
**Scenario:** Forty VPCs across many accounts must resolve an on-premises domain. The team wants one set of Resolver outbound endpoints in a central networking account.

A. Create an outbound endpoint and forwarding rule in every VPC, each sending queries straight to on-premises DNS
B. Change each VPC's DHCP options set to use the on-premises DNS servers instead of the Amazon-provided resolver
C. Create a private hosted zone for the on-premises domain and copy its records into Route 53 each night
D. Share the central Resolver forwarding rules through AWS RAM and associate them with each VPC

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Resolver rules can be shared with other accounts through RAM. When a spoke VPC associates a shared rule, its queries for that domain are forwarded through the central outbound endpoint, so there is one set of endpoints to run. Endpoints in every VPC multiply cost and management. Pointing DHCP options at on-premises DNS breaks resolution of private hosted zones and AWS names. Copying records nightly goes stale and is not forwarding.
</details>

---

### Question 25
**Scenario:** Microservices in VPCs owned by different teams and accounts must call each other over HTTP with IAM-based authorization, without managing peering, Transit Gateway routes, or overlapping CIDR conflicts.

A. Amazon VPC Lattice, with services in a service network and auth policies controlling which principals can call them
B. Transit Gateway with a single route table and security groups that reference the calling services by ID
C. VPC peering between every pair of team VPCs, plus IAM roles assumed by each calling service
D. Internet-facing ALBs for each service, with AWS WAF rules that allow only the partner account IP ranges

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** VPC Lattice is an application-layer service network that connects services across VPCs and accounts, works with overlapping CIDRs, and supports IAM auth policies on the service network and service. Transit Gateway and peering both need non-overlapping routing, and security group references do not work across a Transit Gateway. Exposing services publicly and allowlisting IPs is weaker and is not IAM authorization.
</details>

---

### Question 26
**Scenario:** The operations team must continuously measure packet loss and round-trip latency from VPC subnets to on-premises servers over Direct Connect, and alarm when they degrade.

A. Direct Connect ConnectionState metrics in CloudWatch, alarming when the connection reports down
B. Amazon CloudWatch Network Synthetic Monitor probes from the subnets to the on-premises IP addresses
C. VPC Flow Logs with a metric filter that counts rejected records for the on-premises CIDR range
D. Amazon CloudWatch Internet Monitor, configured with the on-premises servers as monitored resources

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Network Synthetic Monitor sends probes from chosen subnets to hybrid destinations and publishes packet loss and latency to CloudWatch, so gradual degradation can raise an alarm. ConnectionState only shows up or down. Flow Log rejects describe policy decisions, not loss or latency. Internet Monitor measures internet performance for users reaching AWS applications, not private hybrid paths.
</details>

---

### Question 27
**Scenario:** Flow Logs on the network interface of a NAT gateway show only the NAT gateway's private IP as the source of outbound traffic. The team needs the original instance addresses.

A. Enable Flow Logs on the internet gateway, which records the original source before translation
B. Use Traffic Mirroring on the NAT gateway, since Flow Logs cannot capture translated traffic at all
C. Create the flow log with a custom format that includes the pkt-srcaddr and pkt-dstaddr fields
D. Query CloudTrail data events for the NAT gateway, which record the translation of each connection

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** In the default format, srcaddr and dstaddr are the interface's view. The pkt-srcaddr and pkt-dstaddr fields, available only in a custom format, record the original packet-level addresses, which reveals the instance behind the NAT gateway. Internet gateways do not produce Flow Logs of their own, NAT gateways cannot be Traffic Mirroring sources, and CloudTrail does not log individual network flows.
</details>

---

### Question 28
**Scenario:** Branch offices worldwide connect to AWS with Site-to-Site VPN over the internet and suffer from inconsistent latency. The team wants the VPN to enter the AWS network close to each branch.

A. Enable acceleration on Site-to-Site VPN connections attached to a Transit Gateway
B. Enable acceleration on the existing VPN connections that terminate on a virtual private gateway
C. Put CloudFront in front of the VPN endpoints so tunnels terminate at the nearest edge location
D. Raise the tunnel MTU and enable ECMP so the existing tunnels carry more traffic at once

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Accelerated Site-to-Site VPN uses AWS Global Accelerator to bring tunnel traffic into the AWS network at the nearest edge location, and it is supported only for VPN connections attached to a Transit Gateway. It cannot be enabled on virtual private gateway connections, and acceleration must be chosen when the connection is created. CloudFront does not carry IPsec. Raising MTU or adding ECMP changes throughput, not the internet path the tunnels take.
</details>

---

### Question 29
**Scenario:** A regulator requires Direct Connect traffic to be encrypted at layer 2 between the customer router and the AWS Direct Connect device, at 100 Gbps.

A. A hosted connection from a partner, with MACsec enabled by the partner on its shared port
B. A Site-to-Site VPN over a public virtual interface, which encrypts all traffic at layer 2 on the link
C. TLS on every application, which encrypts the payload between the router and the AWS device
D. A dedicated connection at a MACsec-capable location, with a MACsec key associated with the connection

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** MACsec provides layer 2 encryption on Direct Connect and is supported on dedicated connections at supported speeds and locations, with a CKN and CAK associated with the connection. Hosted connections do not support MACsec. An IPsec VPN encrypts at layer 3, not layer 2, and TLS is end-to-end application encryption, so neither meets a layer 2 requirement.
</details>

---

### Question 30
**Scenario:** Interface VPC endpoints for several AWS services are centralized in a shared services VPC that spoke VPCs reach through a Transit Gateway. Spokes still resolve the services to public IPs.

A. Enable private DNS on each endpoint, which makes the endpoint names resolve privately in every attached VPC
B. Disable private DNS on the endpoints, create private hosted zones for the service names with alias records to the endpoints, and associate the zones with the spoke VPCs
C. Add Transit Gateway routes for the AWS public IP ranges toward the shared services VPC attachment
D. Create gateway endpoints in each spoke for every service, which then resolve through the central endpoints

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Private DNS on an interface endpoint only affects the VPC where the endpoint lives. For a centralized pattern, you create private hosted zones for the service names, alias them to the endpoint DNS names, and associate the zones with each spoke so spokes resolve to the central endpoint IPs. Routing public ranges does not change DNS answers. Gateway endpoints exist only for S3 and DynamoDB and do not work through other VPCs.
</details>

---

## Where to go deeper

- [ANS-C01 cert page](../../exams/aws/specialty/advanced-networking-ans-c01/) - notes, practice plan, strategy
- [AZ-700 practice questions](./azure-network-engineer-az-700.md) - the Azure networking counterpart
- [VPC explained](../../learn/concepts/vpc-explained.md) - cloud networking fundamentals
- [Networking topic index](../../topics/networking.md) - cross-cloud comparisons
- **[📖 AWS Certification](https://aws.amazon.com/certification/)** - official exam guides
