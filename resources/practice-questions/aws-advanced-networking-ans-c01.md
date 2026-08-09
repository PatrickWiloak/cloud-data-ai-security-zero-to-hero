---
last-updated: 2026-08-09
difficulty: advanced
---

# AWS Certified Advanced Networking - Specialty (ANS-C01) - Practice Questions

15 questions for ANS-C01 prep, weighted toward network design (30%), implementation (26%), security and compliance (24%), and management and operation (20%).

> **Cert page:** [exams/aws/specialty/advanced-networking-ans-c01/](../../exams/aws/specialty/advanced-networking-ans-c01/)

---

### Question 1
**Scenario:** Fifty VPCs across several accounts must communicate with each other and with on-premises, with centralized routing.

A. Full-mesh VPC peering
B. AWS Transit Gateway with route tables and attachments, shared through Resource Access Manager
C. A VPN per VPC pair
D. PrivateLink for everything

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Peering is non-transitive and a 50-VPC mesh needs 1,225 connections, which is unmanageable. Transit Gateway is a hub with attachment-level route tables that give you segmentation, and RAM shares it across accounts. PrivateLink exposes individual services rather than providing general routing.
</details>

---

### Question 2
**Scenario:** Two VPCs have overlapping CIDR blocks and one application in each must talk to the other.

A. Re-address one VPC
B. Use PrivateLink to expose the specific service, or NAT the overlapping ranges through a middlebox
C. VPC peering
D. Transit Gateway

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Neither peering nor Transit Gateway supports overlapping CIDRs, because routing becomes ambiguous. PrivateLink sidesteps it entirely by presenting the service on an endpoint in the consumer's address space. Re-addressing works but is usually the most disruptive option.
</details>

---

### Question 3
**Scenario:** A Direct Connect connection must be resilient to a single device or location failure.

A. One connection with a VPN backup only
B. Two connections at two different Direct Connect locations, ideally with diverse providers, plus BGP for failover
C. Two connections on the same router
D. A single 100 Gbps connection

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Maximum resilience requires separate locations and separate devices, because two circuits into the same router share a failure domain. A VPN backup is a reasonable lower tier but has different bandwidth and latency characteristics, which changes application behavior during failover.
</details>

---

### Question 4
**Scenario:** Traffic from on-premises prefers one Direct Connect path over another.

A. Static routes only
B. BGP attributes: AS path prepending or local preference to influence path selection in each direction
C. Route table priorities in the VPC
D. DNS

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** AWS uses BGP path selection, so influencing it means using BGP attributes, and each direction is controlled separately: longest prefix match first, then local preference for AWS-to-on-premises, and AS path prepending to influence what AWS prefers. Asymmetric routing is the usual symptom of getting one direction wrong.
</details>

---

### Question 5
**Scenario:** Private DNS resolution is needed between on-premises and a VPC in both directions.

A. Route 53 Resolver inbound and outbound endpoints with forwarding rules
B. Public hosted zones
C. Host files
D. A NAT gateway

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Inbound endpoints give on-premises resolvers an IP in the VPC to query for private zones, and outbound endpoints with rules forward VPC queries for on-premises domains to your resolvers. Both are needed for bidirectional resolution, and forgetting one is the standard hybrid DNS bug.
</details>

---

### Question 6
**Scenario:** All egress to the internet from many VPCs must be inspected centrally.

A. A NAT gateway per VPC
B. A centralized inspection VPC with AWS Network Firewall or third-party appliances, reached through Transit Gateway with appliance mode enabled
C. Security groups
D. NACLs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Centralized inspection needs traffic steered through a hub, and appliance mode on the Transit Gateway attachment ensures both directions of a flow use the same appliance, which stateful inspection requires. Without appliance mode, asymmetric routing breaks the firewall's state table.
</details>

---

### Question 7
**Scenario:** A Network Load Balancer must preserve the client IP for backends.

A. Enable proxy protocol v2 or use target type IP or instance where client IP preservation applies
B. Use an Application Load Balancer
C. Use X-Forwarded-For on NLB
D. It is impossible

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** NLB operates at layer 4, so there is no HTTP header to add: client IP preservation depends on the target type and setting, and proxy protocol carries the original addresses when preservation is not available. X-Forwarded-For is an ALB (layer 7) mechanism.
</details>

---

### Question 8
**Scenario:** An application must be reachable from another VPC without exposing the whole VPC.

A. VPC peering
B. AWS PrivateLink: an endpoint service backed by an NLB, consumed via interface endpoints
C. Transit Gateway
D. A public ALB

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** PrivateLink is unidirectional and service-scoped: the consumer reaches exactly one service and nothing else, with no route between the VPCs. This makes it the right tool for SaaS-style exposure between organizations, and it also works with overlapping CIDRs.
</details>

---

### Question 9
**Scenario:** A packet capture is needed for a production EC2 instance's traffic without touching the instance.

A. VPC Flow Logs
B. VPC Traffic Mirroring to a monitoring appliance
C. CloudTrail
D. A tcpdump on the instance

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Traffic Mirroring copies packets, including payload, to a target for analysis with no agent on the source. Flow Logs record metadata about flows (source, destination, ports, action) but not contents, so they answer "was it allowed" rather than "what was in it."
</details>

---

### Question 10
**Scenario:** Global users need low-latency TCP access to regional endpoints with fast failover.

A. Amazon CloudFront
B. AWS Global Accelerator with static anycast IPs
C. Route 53 latency routing alone
D. An internet-facing NLB in one region

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Global Accelerator gives static anycast addresses, enters the AWS backbone at the nearest edge, and shifts traffic on health checks in seconds without waiting for DNS TTLs. CloudFront is the right answer for cacheable HTTP; DNS-based routing is slower to fail over because resolvers cache.
</details>

---

### Question 11
**Scenario:** IPv6 must be supported for outbound-only connectivity from private subnets.

A. A NAT gateway
B. An egress-only internet gateway
C. An internet gateway
D. A NAT instance

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** IPv6 addresses are globally routable, so there is no NAT in the IPv4 sense. The egress-only internet gateway is the stateful device that allows outbound IPv6 and blocks inbound. Using a plain internet gateway would make the instances directly reachable from the internet.
</details>

---

### Question 12
**Scenario:** A VPN over Direct Connect is required so traffic is encrypted end to end.

A. It is not supported
B. Run an AWS Site-to-Site VPN over a Direct Connect public virtual interface, or use MACsec on supported connections
C. Use a private VIF alone
D. Rely on application TLS only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Direct Connect is private but not encrypted by default. Running an IPsec VPN over a public VIF adds encryption at the cost of throughput per tunnel, and MACsec provides layer 2 encryption on supported dedicated connections at line rate. Which one fits depends on the bandwidth requirement.
</details>

---

### Question 13
**Scenario:** Flow Logs show `REJECT` for return traffic to an instance that initiated a connection.

A. The security group is wrong
B. A network ACL is blocking the ephemeral port range on the return path, because NACLs are stateless
C. The route table is wrong
D. DNS failure

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Security groups are stateful, so a permitted outbound flow returns automatically. NACLs evaluate each direction independently, so the inbound rule must allow the ephemeral port range (typically 1024-65535) for responses. This is the classic asymmetry the exam tests.
</details>

---

### Question 14
**Scenario:** A Transit Gateway must keep production and development traffic separated while both reach a shared services VPC.

A. One route table for everything
B. Separate Transit Gateway route tables per segment, with associations and propagations arranged so prod and dev can reach shared services but not each other
C. Security groups only
D. Separate Transit Gateways

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Segmentation on a Transit Gateway comes from route table design: which attachments associate to which table, and which routes propagate into it. This is the standard shared-services pattern and it is cheaper and simpler than running multiple gateways.
</details>

---

### Question 15
**Scenario:** DNS queries for an S3 VPC gateway endpoint resolve to public IPs and traffic leaves the VPC.

A. Gateway endpoints work by route table prefix lists, so verify the endpoint's route is present in the subnet's route table
B. Add an interface endpoint only
C. Change the DNS server
D. Use a NAT gateway

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Gateway endpoints for S3 and DynamoDB work by injecting a prefix list route, not by changing DNS, so the resolved address stays public while the route keeps traffic inside AWS. Interface endpoints are the DNS-based alternative and are what you need for on-premises access over Direct Connect.
</details>

---

## Where to go deeper

- [ANS-C01 cert page](../../exams/aws/specialty/advanced-networking-ans-c01/) - notes, practice plan, strategy
- [AZ-700 practice questions](./azure-network-engineer-az-700.md) - the Azure networking counterpart
- [VPC explained](../../learn/concepts/vpc-explained.md) - cloud networking fundamentals
- [Networking topic index](../../topics/networking.md) - cross-cloud comparisons
- **[📖 AWS Certification](https://aws.amazon.com/certification/)** - official exam guides
