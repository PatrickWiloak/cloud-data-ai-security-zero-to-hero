---
last-updated: 2026-10-22
---

# GCP Professional Cloud Network Engineer (PCNE) - Exam Scenarios

> Six worked scenarios mirroring PCNE question style. Section references follow the current six-section exam guide.

---

## Scenario 1 - Shared VPC vs VPC peering (Section 1.2 / 2.1)

A company has a central platform team and 30 application projects. Network admin should be centralized; application teams provision their own resources within designated subnets.

**Options:** A. Shared VPC: host project owns the VPC; service projects attach. Subnet-level IAM lets app teams use specific subnets. B. VPC peering between every pair. C. Cloud VPN between projects. D. Each project has its own isolated VPC.

**Analysis:** A is right - Shared VPC is purpose-built for centralized networking with delegated subnet IAM. B is non-transitive and operationally heavy. C is overkill. D doesn't share at all.

**Answer:** A

**Key takeaway:** Shared VPC for centralized networking with delegated app teams. VPC peering for connecting independent VPCs.

---

## Scenario 2 - Hybrid 99.99% availability (Section 1.3 / 4.1)

Production needs 99.99% private connectivity to a single GCP region.

**Options:** A. Four Dedicated Interconnect connections, two in each of two metros (different edge availability domains per metro), with Cloud Routers in two regions and global dynamic routing. B. A single Dedicated Interconnect connection. C. HA VPN over the internet. D. Two Dedicated Interconnect connections in one metro.

**Analysis:** A is right - the 99.99% Interconnect topology needs four connections across two metros, Cloud Routers in at least two regions, and the VPC in global dynamic routing mode, even if all workloads are in one region. D is the 99.9% topology. C reaches 99.99% but over the public internet, so it is not private connectivity. B has no SLA.

**Answer:** A

**Key takeaway:** Interconnect SLAs: 99.9% = two connections in one metro, different edge availability domains; 99.99% = four connections across two metros, two Cloud Router regions, global routing. HA VPN gets 99.99% with tunnels on both gateway interfaces.

---

## Scenario 3 - Global load balancing for HTTP (Section 3.1)

A consumer app needs anycast IP, geo-routing to nearest backend, WAF-style filtering, and TLS termination at edge.

**Options:** A. Global external Application Load Balancer (Premium Tier) with backend services across regions; Cloud Armor for WAF; Google-managed certificates. B. Regional external passthrough Network Load Balancer. C. Internal Application Load Balancer. D. Cloud DNS round-robin.

**Analysis:** A is right - the global external Application Load Balancer uses a single anycast IP, terminates TLS at Google's edge, routes to the nearest healthy backend and integrates with Cloud Armor. B is regional L4. C is internal-only. D is DNS, not a load balancer.

**Answer:** A

**Key takeaway:** Global external Application LB (formerly global HTTP(S) LB) = the L7 anycast solution and needs Premium Tier. Cloud Armor = WAF + DDoS protection. Use the global external proxy Network LB for non-HTTP global TCP.

---

## Scenario 4 - Private Google Access vs Private Service Connect (Section 2.1)

VMs without public IPs need to reach Google APIs (Cloud Storage, BigQuery, etc.).

**Options:** A. Private Google Access on the subnet; or Private Service Connect endpoints for private-IP access to Google APIs. B. NAT Gateway. C. Public IP per VM. D. Cloud VPN.

**Analysis:** A is right - both options. PGA lets VMs without external IPs reach Google APIs over Google's network (optionally through the private.googleapis.com `199.36.153.8/30` or restricted.googleapis.com `199.36.153.4/30` VIPs). PSC creates an internal IP of your choosing in your VPC for Google APIs, and its `vpc-sc` bundle pairs with VPC Service Controls. B (Cloud NAT) works but sends API traffic to public endpoints and is unnecessary. C exposes VMs. D does not apply.

**Answer:** A

**Key takeaway:** PGA = enable Google APIs from private VMs (still uses Google network). PSC = private IP endpoint in your VPC. PSC is the modern higher-security choice.

---

## Scenario 5 - Cloud Armor (Section 6.1)

A company needs DDoS protection, geo-blocking (block Russia, China for compliance), and OWASP Top 10 rule sets in front of an HTTPS LB.

**Options:** A. Cloud Armor security policy with preconfigured OWASP WAF rules + a geo-restriction rule (`origin.region_code`); Adaptive Protection enabled. B. Cloud CDN only. C. Manual IP blocking with Cloud Run functions. D. Cloud NAT.

**Analysis:** A is right - Cloud Armor has preconfigured WAF rules based on the OWASP Core Rule Set, geography-based rules, and Adaptive Protection (ML-based Layer 7 DDoS detection). B doesn't block. C is reactive. D is for outbound traffic.

**Answer:** A

**Key takeaway:** Cloud Armor = WAF + DDoS protection. Tiers are Standard (pay as you go) and Enterprise (Paygo or Annual, formerly Managed Protection Plus); full Adaptive Protection, Google Threat Intelligence and advanced network DDoS protection need Enterprise, while Standard gets Adaptive Protection alerting only.

---

## Scenario 6 - Multi-VPC mesh at scale (Section 1.2 / 2.3)

A company will grow to 200 VPCs across multiple regions. They want full any-to-any connectivity with minimal management.

**Options:** A. Network Connectivity Center (NCC) with VPCs as spokes. B. Full mesh of VPC peering. C. Shared VPC at the org level. D. Manual Cloud Routes.

**Analysis:** A is right - NCC with VPC spokes is Google Cloud's transit answer for multi-VPC connectivity at scale, in a mesh topology for any-to-any (or star for segmentation). B is non-transitive, hits peering limits and is operationally heavy. C - Shared VPC is one VPC shared across projects, not multi-VPC connectivity. D is manual.

**Answer:** A

**Key takeaway:** GCP transit: Network Connectivity Center (modern transit hub, similar to AWS TGW / Azure Virtual WAN). Shared VPC is a different pattern (one VPC, many projects).
