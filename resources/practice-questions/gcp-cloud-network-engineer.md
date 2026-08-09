---
last-updated: 2026-08-09
difficulty: advanced
---

# Google Cloud Professional Cloud Network Engineer - Practice Questions

15 questions for the Professional Cloud Network Engineer exam, covering VPC design, hybrid connectivity, network services, and security.

> **Cert page:** [exams/gcp/cloud-network-engineer/](../../exams/gcp/cloud-network-engineer/)

---

### Question 1
**Scenario:** How does a Google Cloud VPC differ from a typical cloud VPC?

A. It is zonal
B. It is a global resource, with subnets scoped to regions, so one VPC spans regions without peering
C. It is regional only
D. It cannot have subnets

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** This is the defining GCP difference: a VPC is global and subnets are regional, so instances in different regions communicate over internal IPs with no peering or gateway. Routes and firewall rules are also VPC-wide, which changes how you design segmentation.
</details>

---

### Question 2
**Scenario:** Several projects must share one network administered centrally.

A. VPC Network Peering between all projects
B. Shared VPC, with a host project owning the network and service projects attaching to it
C. A VPN mesh
D. One project for everything

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Shared VPC separates network administration from workload ownership: network admins manage subnets and firewall rules in the host project while application teams deploy into service projects. Peering connects distinct networks and is not transitive, so it does not give centralized control.
</details>

---

### Question 3
**Scenario:** Firewall rules must allow SSH only to instances with a specific role.

A. Allow from 0.0.0.0/0
B. A rule targeting a network tag or service account, sourced from Identity-Aware Proxy's range for tunneled SSH
C. Allow all internal traffic
D. Rely on the OS firewall

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Targeting by service account is more robust than network tags because tags can be added by anyone who can edit the instance. IAP TCP forwarding removes the need for public IPs or a bastion entirely, restricting the source to Google's forwarding range with IAM controlling who may use it.
</details>

---

### Question 4
**Scenario:** Instances in a private subnet need outbound internet access without public IPs.

A. Cloud NAT configured on the region's router
B. A public IP per instance
C. A proxy VM
D. Private Google Access

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cloud NAT is a managed, distributed service with no NAT instance to run, configured on the Cloud Router. Private Google Access is the related but different feature: it lets instances without external IPs reach Google APIs, which is not general internet egress.
</details>

---

### Question 5
**Scenario:** An instance must reach Cloud Storage without traversing the internet and without a public IP.

A. Cloud NAT
B. Private Google Access on the subnet, or Private Service Connect for a private endpoint
C. A public IP
D. Cloud VPN

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Private Google Access lets instances reach Google APIs over internal routing. Private Service Connect goes further by giving the service an internal IP in your VPC, which is what you need when on-premises clients must resolve and reach it privately too.
</details>

---

### Question 6
**Scenario:** Hybrid connectivity must be resilient with a 99.99% availability SLA.

A. A single Dedicated Interconnect
B. Four Dedicated Interconnect connections across two metropolitan areas and two zones, per Google's topology requirements
C. HA VPN alone
D. Two connections in one location

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Google publishes explicit topologies for 99.9% and 99.99%, and the higher tier requires geographic and zone diversity, not just two circuits. HA VPN reaches 99.99% on its own tier with two interfaces, but with internet-path characteristics rather than dedicated bandwidth.
</details>

---

### Question 7
**Scenario:** A Cloud Router must advertise only specific subnets to on-premises.

A. It always advertises everything
B. Configure custom route advertisements on the BGP session, listing the prefixes
C. Use static routes only
D. Change the subnet range

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The default is to advertise the VPC's subnets, and custom advertisement mode lets you narrow or extend that, including advertising ranges that are not subnets. MED values on the advertisements control which path on-premises prefers when several are available.
</details>

---

### Question 8
**Scenario:** A global HTTPS application needs one anycast IP and routing to the closest healthy backend.

A. Global external Application Load Balancer
B. Network Load Balancer
C. Internal load balancer
D. Cloud DNS round robin

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The global Application Load Balancer gives a single anycast address, terminates TLS at the edge, and routes by URL map to the nearest healthy backend with Cloud CDN and Cloud Armor available on top. DNS-based distribution cannot fail over quickly because resolvers cache.
</details>

---

### Question 9
**Scenario:** Layer 7 protection against SQL injection and volumetric attacks is required.

A. Firewall rules
B. Cloud Armor security policies with preconfigured WAF rules and rate limiting, attached to the load balancer backend
C. VPC Service Controls
D. Cloud NAT

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cloud Armor operates at the edge in front of the load balancer, so malicious traffic never reaches your backends. VPC firewall rules are layer 3 and 4 and cannot inspect a request body. VPC Service Controls is a data exfiltration boundary for Google APIs, a different control entirely.
</details>

---

### Question 10
**Scenario:** Data exfiltration from BigQuery to a personal project must be prevented.

A. IAM alone
B. VPC Service Controls creating a service perimeter around the projects
C. Firewall rules
D. Cloud Armor

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** IAM controls who can act, but a legitimately authorized insider can still copy data to an outside project. A service perimeter restricts API access based on the network and project boundary, so the copy is refused regardless of the caller's permissions.
</details>

---

### Question 11
**Scenario:** Two VPCs have overlapping IP ranges but one service must be shared.

A. VPC Peering
B. Private Service Connect, which publishes a service reachable via an endpoint in the consumer's address space
C. Shared VPC
D. A VPN

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Peering requires non-overlapping ranges and is non-transitive. Private Service Connect exposes one service through a consumer-side endpoint, so the address spaces never need to be reconciled, which also makes it the pattern for SaaS-style publishing.
</details>

---

### Question 12
**Scenario:** DNS names in a VPC must resolve from on-premises.

A. Public DNS zones
B. Cloud DNS private zones with inbound and outbound server policies (DNS forwarding) between on-premises and the VPC
C. Host files
D. A public IP

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** An inbound server policy creates forwarding addresses on-premises resolvers can query, and outbound forwarding sends VPC queries for on-premises domains to your resolvers. Both directions must be configured, and missing one is the standard hybrid DNS failure.
</details>

---

### Question 13
**Scenario:** Packet-level visibility is needed for traffic between two instances.

A. VPC Flow Logs
B. Packet Mirroring to a collector instance group
C. Cloud Audit Logs
D. Cloud Monitoring

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Packet Mirroring copies full packets including payload to a collector behind an internal load balancer, which is what an IDS needs. Flow Logs record connection metadata and sampled flow records, which answer "who talked to whom" but not "what was in it."
</details>

---

### Question 14
**Scenario:** Connectivity between two instances fails and the cause is unclear.

A. Recreate the instances
B. Connectivity Tests in Network Intelligence Center, which simulates the path against the configuration and names the blocking rule or missing route
C. Ping only
D. Restart the VPC

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Connectivity Tests evaluate the actual configuration, including firewall rules, routes, and peering, and report exactly where the packet would be dropped. It works even when the instances are stopped, because it analyzes configuration rather than sending traffic.
</details>

---

### Question 15
**Scenario:** A GKE cluster must not expose its control plane to the internet.

A. A public cluster with authorized networks
B. A private cluster, with private endpoint access and authorized networks for administrative access
C. Firewall rules on nodes
D. Cloud Armor

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Private clusters give nodes internal IPs and can restrict the control plane endpoint to private access, reached through peering, VPN, or a bastion. Authorized networks on a public endpoint narrows the exposure but still leaves the endpoint on the internet.
</details>

---

## Where to go deeper

- [Professional Cloud Network Engineer cert page](../../exams/gcp/cloud-network-engineer/) - notes, practice plan, strategy
- [GCP Cloud Architect practice questions](./gcp-cloud-architect.md) - networking in architecture context
- [ANS-C01 practice questions](./aws-advanced-networking-ans-c01.md) - the AWS counterpart
- [Networking topic index](../../topics/networking.md) - cross-cloud comparisons
- **[📖 Google Cloud certification](https://cloud.google.com/learn/certification)** - official exam guides
