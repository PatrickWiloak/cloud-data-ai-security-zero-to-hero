---
last-updated: 2026-10-22
difficulty: advanced
---

# Google Cloud Professional Cloud Network Engineer - Practice Questions

30 questions for the Professional Cloud Network Engineer exam. Questions 16-30 follow the current exam guide's six sections: designing and planning a VPC network (~21%), implementing a VPC network (~20%), managed network services (~16%), hybrid and multicloud interconnectivity (~16%), network operations (~14%), and network security (~13%).

> **Cert page:** [exams/gcp/cloud-network-engineer/](../../exams/gcp/cloud-network-engineer/)

---

### Question 1
**Scenario:** How does a Google Cloud VPC differ from a typical cloud VPC?

A. It is regional only, so instances in different regions need VPC peering to talk over internal IPs
B. It cannot have subnets, so every instance receives an address from a single flat range for the whole project
C. It is global, with regional subnets, so one VPC spans regions without peering
D. It is zonal, so each zone has its own VPC and traffic between zones has to cross a gateway

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** This is the defining GCP difference: a VPC is global and subnets are regional, so instances in different regions communicate over internal IPs with no peering or gateway. Routes and firewall rules are also VPC-wide, which changes how you design segmentation.
</details>

---

### Question 2
**Scenario:** Several projects must share one network administered centrally.

A. VPC Network Peering between every project's network
B. Shared VPC, with a host project owning the network and service projects attached
C. A VPN mesh between per-project networks and gateways
D. One project for everything, so every team holds roles in a single project and ownership is not separated

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Shared VPC separates network administration from workload ownership: network admins manage subnets and firewall rules in the host project while application teams deploy into service projects. Peering connects distinct networks and is not transitive, so it does not give centralized control.
</details>

---

### Question 3
**Scenario:** Firewall rules must allow SSH only to instances with a specific role.

A. Rely on the OS firewall alone and skip VPC firewall rules
B. Allow from 0.0.0.0/0 on port 22, and depend on SSH key authentication alone to keep unauthorized users out of every instance
C. A rule targeting a service account or network tag, with the source set to IAP's range for tunneled SSH
D. Allow all internal traffic in the VPC, so any instance can SSH to any other regardless of its role or purpose

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Targeting by service account is more robust than network tags because tags can be added by anyone who can edit the instance. IAP TCP forwarding removes the need for public IPs or a bastion entirely, restricting the source to Google's forwarding range with IAM controlling who may use it.
</details>

---

### Question 4
**Scenario:** Instances in a private subnet need outbound internet access without public IPs.

A. A public IP per instance, removed once the download finishes
B. Private Google Access, which lets instances without external IPs reach any internet destination
C. An internal passthrough Network Load Balancer for the subnet
D. Cloud NAT configured on a Cloud Router in the region, so no VM needs an external IP

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Cloud NAT is a managed, distributed service with no NAT instance to run, configured on the Cloud Router. Private Google Access is the related but different feature: it lets instances without external IPs reach Google APIs, which is not general internet egress.
</details>

---

### Question 5
**Scenario:** An instance must reach Cloud Storage without traversing the internet and without a public IP.

A. Cloud VPN between the subnet and Google, which is designed for hybrid links to on-premises networks
B. Private Google Access on the subnet, or Private Service Connect for a private endpoint
C. A public IP on the instance, restricted by firewall rules to Google's published address ranges
D. Cloud NAT, which translates private addresses so the instance reaches Cloud Storage on its public endpoint over the internet

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Private Google Access lets instances reach Google APIs over internal routing. Private Service Connect goes further by giving the service an internal IP in your VPC, which is what you need when on-premises clients must resolve and reach it privately too.
</details>

---

### Question 6
**Scenario:** Hybrid connectivity must be resilient with a 99.99% availability SLA.

A. Four Dedicated Interconnect connections across two metros and two zones, per Google's topology requirements
B. Two connections in one location on separate devices, which Google's topologies rate at 99.9 percent at best because one site is a shared failure domain
C. HA VPN with the two tunnels ending on a single on-premises peer device and gateway interface
D. A single Dedicated Interconnect connection with a redundant cross connect inside the same facility, leaving one site as a shared failure point

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Google publishes explicit topologies for 99.9% and 99.99%, and the higher tier requires geographic and zone diversity, not just two circuits. HA VPN reaches 99.99% on its own tier with two interfaces, but with internet-path characteristics rather than dedicated bandwidth.
</details>

---

### Question 7
**Scenario:** A Cloud Router must advertise only specific subnets to on-premises.

A. Change the subnet range so that only the intended prefixes fall inside the VPC address space
B. Switch the Cloud Router to custom route advertisement mode on the BGP session and list only the prefixes to advertise
C. Use static routes only and remove the BGP session, which stops Cloud Router advertising anything
D. It always advertises everything, because the advertisement mode on a Cloud Router cannot be changed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The default is to advertise the VPC's subnets, and custom advertisement mode lets you narrow or extend that, including advertising ranges that are not subnets. MED values on the advertisements control which path on-premises prefers when several are available.
</details>

---

### Question 8
**Scenario:** A global HTTPS application needs one anycast IP and routing to the closest healthy backend.

A. Network Load Balancer, a regional pass-through balancer that preserves the client IP
B. Internal load balancer, which uses a private address reachable only inside the VPC
C. Cloud DNS round robin, returning several regional IP addresses in rotation
D. Global external Application Load Balancer

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The global Application Load Balancer gives a single anycast address, terminates TLS at the edge, and routes by URL map to the nearest healthy backend with Cloud CDN and Cloud Armor available on top. DNS-based distribution cannot fail over quickly because resolvers cache.
</details>

---

### Question 9
**Scenario:** Layer 7 protection against SQL injection and volumetric attacks is required.

A. Cloud Armor security policies with preconfigured WAF rules and rate limiting on the backend service
B. VPC firewall rules that deny the SQL injection signatures and cap new connections per source address on the backend VMs
C. Cloud NAT, which hides backend addresses so injection requests cannot reach them
D. VPC Service Controls, with a perimeter that blocks malicious HTTP requests before they reach the load balancer

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cloud Armor operates at the edge in front of the load balancer, so malicious traffic never reaches your backends. VPC firewall rules are layer 3 and 4 and cannot inspect a request body. VPC Service Controls is a data exfiltration boundary for Google APIs, a different control entirely.
</details>

---

### Question 10
**Scenario:** Data exfiltration from BigQuery to a personal project must be prevented.

A. IAM alone, granting BigQuery roles only to approved users
B. Firewall rules that block egress from the project's VMs to the personal project's address ranges
C. VPC Service Controls creating a service perimeter around the BigQuery projects
D. Cloud Armor policies on the BigQuery endpoint

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** IAM controls who can act, but a legitimately authorized insider can still copy data to an outside project. A service perimeter restricts API access based on the network and project boundary, so the copy is refused regardless of the caller's permissions.
</details>

---

### Question 11
**Scenario:** Two VPCs have overlapping IP ranges but one service must be shared.

A. Shared VPC, which puts the two projects' workloads in one network and so cannot join overlapping ranges together
B. VPC Peering, which exchanges routes between the two networks and works whatever their address ranges are, with no overlap check
C. A VPN between the two networks, with Cloud Router advertising the ranges to each side
D. Private Service Connect, publishing the service through an endpoint in the consumer's address space

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Peering requires non-overlapping ranges and is non-transitive. Private Service Connect exposes one service through a consumer-side endpoint, so the address spaces never need to be reconciled, which also makes it the pattern for SaaS-style publishing.
</details>

---

### Question 12
**Scenario:** DNS names in a VPC must resolve from on-premises.

A. Public DNS zones containing the private records, so on-premises resolvers can find them over the internet instead
B. A public IP on each instance, so clients reach them by address
C. Cloud DNS private zones with an inbound server policy and outbound forwarding to on-premises resolvers
D. Host files copied to every on-premises machine

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** An inbound server policy creates forwarding addresses on-premises resolvers can query, and outbound forwarding sends VPC queries for on-premises domains to your resolvers. Both directions must be configured, and missing one is the standard hybrid DNS failure.
</details>

---

### Question 13
**Scenario:** Packet-level visibility is needed for traffic between two instances.

A. Packet Mirroring to a collector instance group behind an internal load balancer
B. VPC Flow Logs, which sample connections and record metadata such as addresses, ports, and bytes
C. Cloud Monitoring, which charts metrics such as CPU use and network bytes for each instance
D. Cloud Audit Logs, which record administrative API calls and data access to Google Cloud services

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Packet Mirroring copies full packets including payload to a collector behind an internal load balancer, which is what an IDS needs. Flow Logs record connection metadata and sampled flow records, which answer "who talked to whom" but not "what was in it."
</details>

---

### Question 14
**Scenario:** Connectivity between two instances fails and the cause is unclear.

A. Connectivity Tests in Network Intelligence Center, which simulates the path and names the blocking rule or missing route
B. Ping only, repeated from each instance until the pattern of drops makes the failing hop obvious
C. Recreate the instances in a new subnet, in case the original network interface is corrupted
D. Restart the VPC from the console, which reloads every firewall rule and route in the network

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Connectivity Tests evaluate the actual configuration, including firewall rules, routes, and peering, and report exactly where the packet would be dropped. It works even when the instances are stopped, because it analyzes configuration rather than sending traffic.
</details>

---

### Question 15
**Scenario:** A GKE cluster must not expose its control plane to the internet.

A. Cloud Armor, which filters web requests but does not change where the control plane endpoint is reachable
B. A private cluster with the control plane on a private endpoint, plus authorized networks for administration from known ranges
C. A public cluster with authorized networks, which narrows access but leaves the endpoint reachable from the internet
D. Firewall rules on nodes, which cannot change who can reach the managed control plane endpoint

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Private clusters give nodes internal IPs and can restrict the control plane endpoint to private access, reached through peering, VPN, or a bastion. Authorized networks on a public endpoint narrows the exposure but still leaves the endpoint on the internet.
</details>

---

### Question 16
**Scenario:** A team is planning a VPC-native GKE cluster that will grow to hundreds of nodes and thousands of pods. What must the IP plan include?

A. Only a primary range big enough for nodes, because GKE assigns pod IPs from a hidden Google-managed range
B. A public IP range for pods so they can be reached directly from the internet
C. A subnet primary range for nodes plus secondary ranges sized for pods and Services
D. One /29 subnet per node pool

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** VPC-native clusters use alias IPs: nodes come from the subnet's primary range, pods and Services from secondary ranges, and the pod range must be sized for the maximum pods per node times the number of nodes. Pod IPs are not taken from a hidden range in VPC-native mode; they are your secondary range. Pods do not need public IPs, and exposing them that way is poor design. A /29 is far too small for any node pool's pods.
</details>

---

### Question 17
**Scenario:** Two companies, each with its own Google Cloud organization, need private, low-latency connectivity between one VPC in each. Their IP ranges do not overlap.

A. VPC Network Peering between the two VPCs
B. Shared VPC, with one company's project attached as a service project of the other's host project
C. Cloud NAT on both sides so each VPC can reach the other's external IP addresses
D. A Cloud VPN tunnel to the internet

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** VPC Network Peering works across projects and organizations, keeps traffic on Google's network with internal IPs, and needs non-overlapping ranges, which is the case here. Shared VPC works only within one organization. Cloud NAT is for outbound internet access and would send traffic over external IPs. A VPN adds gateways and tunnel throughput limits for no gain when peering fits.
</details>

---

### Question 18
**Scenario:** A VPC has subnets in three regions, but on-premises routes learned by a Cloud Router in one region are only reachable from VMs in that region.

A. Create a second VPN tunnel in every other region and attach it to the same Cloud Router
B. Add static routes for the on-premises prefixes in each region's subnet route table
C. Enable Private Google Access on all subnets so the VMs can reach the routes
D. Change the VPC's dynamic routing mode from regional to global

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** In regional dynamic routing mode, routes learned by a Cloud Router apply only in its region; global mode makes them available to every region in the VPC. Extra tunnels are not needed, and a tunnel belongs to its own region's Cloud Router. Google Cloud VPCs do not have per-subnet route tables, and static routes would lose the dynamic failover. Private Google Access is about reaching Google APIs, not on-premises routes.
</details>

---

### Question 19
**Scenario:** A new VPC will be connected to an on-premises network that uses parts of `10.128.0.0/9`. The team wants full control over which subnets exist and their ranges.

A. Create an auto mode VPC, which picks ranges that never overlap with on-premises networks
B. Create a custom mode VPC and define each subnet's range explicitly
C. Use the default network that Google creates in every new project
D. Create a legacy network

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Custom mode VPCs create no subnets until you define them, so ranges can avoid on-premises space. Auto mode creates a subnet in every region from `10.128.0.0/9`, which is exactly the range that overlaps here. The default network is an auto mode VPC with permissive firewall rules. Legacy networks are deprecated and have no subnets at all.
</details>

---

### Question 20
**Scenario:** Eight VPCs in different projects must all reach each other privately. Peering is not transitive, and the team does not want to manage 28 separate peerings.

A. Attach the VPCs as VPC spokes to a Network Connectivity Center hub
B. Peer every VPC with one hub VPC and rely on peering to pass traffic between the spokes
C. Give every VM an external IP and allow the other VPCs' addresses in firewall rules
D. Use Cloud CDN

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Network Connectivity Center VPC spokes exchange subnet routes through a central hub, giving full mesh reachability without managing each pair. Peering is not transitive, so a hub VPC with peerings does not connect spoke to spoke. External IPs send traffic over the internet path and widen exposure. Cloud CDN caches HTTP content and does not connect VPCs.
</details>

---

### Question 21
**Scenario:** A VPC has two custom static routes to `192.168.0.0/16`: one with priority 100 through an appliance, one with priority 1000 through a VPN tunnel. Both next hops are healthy.

A. Traffic is split evenly between both next hops using ECMP because the destinations match
B. The route with priority 1000 wins, because a larger number means a higher preference
C. The route with priority 100 wins, because a lower number means a higher preference
D. Neither route is used and traffic follows the default internet gateway route

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** For routes with the same destination, Google Cloud prefers the lowest priority number, so priority 100 is used and priority 1000 acts as a backup. ECMP applies only when routes share the same destination and the same priority. Larger numbers mean lower preference. The default route is only used when no more specific route matches.
</details>

---

### Question 22
**Scenario:** VMs in one region need a private, highly available TCP load balancer for a fleet of backends that must see the original client IP. No HTTP features are needed.

A. A global external Application Load Balancer with backends in that region only
B. An external proxy Network Load Balancer with a reserved public IP address
C. Cloud DNS round-robin records pointing at every backend VM
D. An internal passthrough Network Load Balancer

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The internal passthrough Network Load Balancer is regional, private, layer 4, and does not proxy, so backends see the client's source IP. A global external Application Load Balancer is public and HTTP-based. An external proxy load balancer is internet-facing and terminates connections, hiding the client IP unless PROXY protocol is used. DNS round robin has no health checking and caches stale answers.
</details>

---

### Question 23
**Scenario:** Paid video files are served through Cloud CDN. Only logged-in customers should be able to fetch them, for a limited time.

A. Make the backend bucket private and turn off Cloud CDN caching for the video paths
B. Use Cloud CDN signed URLs or signed cookies with an expiry time
C. Put the videos behind Identity-Aware Proxy and cache them at the edge for every user
D. Add a firewall rule allowing only customers' IP addresses

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Signed URLs and signed cookies grant time-limited access to cached content, and Cloud CDN checks the signature at the edge, so access stays controlled while caching still works. Turning off caching loses the CDN benefit and does not by itself authenticate users. IAP protects applications behind a load balancer but is not the intended pattern for time-limited cached media. Customer IPs change constantly and cannot be listed.
</details>

---

### Question 24
**Scenario:** A company's public Cloud DNS zone must protect resolvers against forged responses for its domain.

A. Enable DNSSEC on the public managed zone and add the DS record at the domain registrar
B. Convert the public zone to a private zone so only internal resolvers can query it
C. Lower the TTL on every record in the zone to 30 seconds
D. Put Cloud Armor in front of Cloud DNS

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** DNSSEC signs the zone's records so validating resolvers can detect forged answers; the DS record at the registrar completes the chain of trust. A private zone would stop the public from resolving the domain at all. Short TTLs limit how long a forged answer is cached but do not prevent forgery. Cloud Armor protects HTTP load balancer backends, not DNS.
</details>

---

### Question 25
**Scenario:** A company needs private, high-throughput connectivity to Google Cloud but has no equipment in any colocation facility where Google meets customers.

A. Dedicated Interconnect, which needs no presence at a colocation facility
B. Direct Peering, which gives private RFC 1918 access to VPC resources
C. Classic VPN with static routes to every VPC subnet
D. Partner Interconnect through a supported service provider

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Partner Interconnect connects through a service provider that already has a link to Google, so the company does not need its own equipment in a colocation facility. Dedicated Interconnect requires a physical cross-connect in such a facility. Direct Peering reaches Google's public services, not VPC internal addresses. Classic VPN runs over the internet and is not high-throughput private connectivity.
</details>

---

### Question 26
**Scenario:** Traffic from on-premises should use Cloud Interconnect normally and fall back to HA VPN only if the interconnect fails. Both advertise the same prefixes through Cloud Router.

A. Delete the VPN tunnels and recreate them by hand whenever the interconnect fails
B. Give the VPN BGP sessions a worse advertised route priority (higher MED) than the interconnect
C. Add a firewall rule denying traffic from the VPN tunnels while the interconnect is up
D. Make the interconnect VLAN attachments use a smaller MTU than the VPN tunnels

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cloud Router sends the advertised route priority as BGP MED, so giving the VPN sessions a higher value makes on-premises prefer the interconnect and use the VPN only when interconnect routes disappear; on-premises can mirror this for the return path. Recreating tunnels by hand is slow and not a design. A firewall rule would break the VPN when it is needed. MTU affects packet size, not path selection.
</details>

---

### Question 27
**Scenario:** An organization has hundreds of VPC firewall rules and suspects many are never matched or are hidden by higher-priority rules.

A. Delete all rules with priority above 1000 and see which applications break
B. Run Connectivity Tests between every pair of VMs in the VPC
C. Enable Firewall Rules Logging and review Firewall Insights for shadowed and unused rules
D. Turn on Packet Mirroring for every subnet

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Firewall Insights, part of Network Intelligence Center, uses firewall rule logging and hit counts to report shadowed, overly permissive and unused rules. Deleting rules to see what breaks causes outages. Connectivity Tests analyse specific paths, not the whole rule set's usage. Packet Mirroring copies traffic for deep inspection and says nothing about rule hits.
</details>

---

### Question 28
**Scenario:** VPC Flow Logs on busy subnets are generating more log volume and cost than the team can justify, but they still want representative visibility.

A. Lower the sampling rate and increase the aggregation interval on the busy subnets
B. Turn off flow logs and rely on firewall logs alone, which capture every flow
C. Export the flow logs to BigQuery instead of Cloud Logging, which stops them being generated
D. Enable flow logs on every other subnet to spread the cost

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Flow logs support a sampling rate and an aggregation interval, plus metadata and filter options, so you can cut volume while keeping a representative view. Firewall rule logs record only connections matching logged rules, not all flows. Exporting to BigQuery changes where logs go but not how many are generated. Adding flow logs elsewhere increases total volume.
</details>

---

### Question 29
**Scenario:** Security must enforce a baseline of firewall rules, such as blocking known bad ranges, across every project in a folder, and project owners must not be able to override them.

A. Add the same VPC firewall rules to every VPC with a script that runs nightly
B. Set the rules at the lowest priority in each VPC so they are evaluated after everything else
C. Use Cloud Armor security policies attached to every VM instance in the folder
D. Use hierarchical firewall policies at the folder level

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Hierarchical firewall policies attach to the organization or folder, are evaluated before VPC rules, and cannot be changed by project owners; they can also delegate decisions to lower levels with `goto_next`. A nightly script leaves gaps and can be undone by project owners. Lowest priority means the rules are overridden by anything else. Cloud Armor attaches to load balancer backends, not to VM instances in general.
</details>

---

### Question 30
**Scenario:** VMs must reach only an approved list of external websites, and every HTTPS request must be logged with its URL.

A. Use Cloud NAT with a reserved IP so external sites can allow-list the company's addresses
B. Send egress through Secure Web Proxy with a URL allow list policy and logging
C. Add an egress firewall rule allowing TCP 443 to `0.0.0.0/0` for every VM
D. Enable Private Google Access on the subnets

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Secure Web Proxy is an explicit egress proxy that applies URL and host based policies and logs each request. Cloud NAT gives stable outbound IPs but cannot filter by URL. An open port 443 rule allows every site. Private Google Access only covers Google APIs and services, not external websites.
</details>

---

## Where to go deeper

- [Professional Cloud Network Engineer cert page](../../exams/gcp/cloud-network-engineer/) - notes, practice plan, strategy
- [GCP Cloud Architect practice questions](./gcp-cloud-architect.md) - networking in architecture context
- [ANS-C01 practice questions](./aws-advanced-networking-ans-c01.md) - the AWS counterpart
- [Networking topic index](../../topics/networking.md) - cross-cloud comparisons
- **[📖 Google Cloud certification](https://cloud.google.com/learn/certification)** - official exam guides
