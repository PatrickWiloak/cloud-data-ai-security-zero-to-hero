---
last-updated: 2026-10-22
difficulty: advanced
---

# Cisco CCNP Enterprise ENCOR (350-401) - Practice Questions

30 questions across the ENCOR blueprint: architecture, virtualization, infrastructure (the largest section, covering switching, routing, and wireless), network assurance, security, and automation.

> **Cert page:** [exams/cisco/ccnp-enterprise-encor-350-401/](../../exams/cisco/ccnp-enterprise-encor-350-401/)

---

### Question 1
**Scenario:** Which OSPF LSA type describes a summary route into an area from an ABR?

A. Type 1, the router LSA that an ABR floods across area boundaries
B. Type 7
C. Type 3, the summary LSA that an ABR originates for the inter-area prefixes of each area it connects
D. Type 5, the LSA an ABR originates for each summarized inter-area prefix

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Type 1 and 2 stay within an area, Type 3 carries inter-area routes from the ABR, Type 5 carries external routes from an ASBR, and Type 7 is the NSSA form of an external route that the ABR translates back to Type 5.
</details>

---

### Question 2
**Scenario:** A switch must load balance traffic across two uplinks to the same neighbor as one logical link.

A. Spanning tree, which forwards across the two uplinks at once and balances per VLAN as a single logical link
B. An EtherChannel using LACP, with matching speed, duplex, and mode on each end
C. Two separate VLANs
D. HSRP

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Spanning tree would block the redundant link; bundling makes both forward as one logical interface. Load balancing is per flow based on a hash, so a single large flow does not split across members regardless of the hashing method chosen.
</details>

---

### Question 3
**Scenario:** Which first hop redundancy protocol is a Cisco proprietary protocol with an active and standby router?

A. VRRP, the Cisco proprietary protocol that elects a master and backup router sharing a virtual IP
B. GLBP only, because it is the only Cisco protocol that has an active and standby router with a virtual IP
C. HSRP: active and standby roles, virtual IP
D. LACP

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** VRRP is the open standard with master and backup roles, and GLBP adds load balancing across multiple forwarders. HSRP's preemption is off by default, which is the behavior detail that surprises people after a failover.
</details>

---

### Question 4
**Scenario:** Traffic between two VLANs on the same switch must be routed.

A. Port security with sticky MAC addresses, which forwards frames between VLANs on the same switch
B. An access port
C. A separate switch
D. SVIs on a multilayer switch with IP routing enabled

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** SVIs route in hardware on the switch, which is why inter-VLAN routing moved off the router. Router-on-a-stick with subinterfaces over a trunk is the older design and puts every inter-VLAN packet across one physical link.
</details>

---

### Question 5
**Scenario:** Which BGP attribute is evaluated first in the best path selection?

A. AS path length, since the shortest AS path is compared first for every prefix
B. Local preference, which is compared first and shared with all iBGP peers
C. MED
D. Weight, which is Cisco proprietary, local to the router, and never advertised to any peer

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The order runs weight (highest wins, local only), then local preference (highest, within the AS), then locally originated, then shortest AS path, then origin, then MED (lowest). Weight never leaves the router, which is what makes it a per-router override.
</details>

---

### Question 6
**Scenario:** A wireless client roams between APs on different subnets without dropping its session.

A. Layer 3 roaming with an anchor controller that keeps the client's original subnet and IP
B. Layer 2 roaming, with the client's IP rewritten at the second AP
C. Not supported
D. A new DHCP lease on the second subnet, which keeps the session alive because the client then reconnects automatically

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Layer 2 roaming keeps the client in the same subnet and needs no tunnel. Crossing subnets requires the traffic to be tunneled back to the anchor so the client's IP stays valid, which is why anchor and foreign controller roles exist.
</details>

---

### Question 7
**Scenario:** Which overlay technology does Cisco SD-Access use for the data plane?

A. VXLAN, with LISP for the control plane and TrustSec for policy
B. MPLS with LDP labels in the data plane, and BGP route reflectors to distribute endpoint reachability and policy
C. GRE tunnels between edge nodes, carrying the group policy tag in a GRE key field set by the control plane
D. IPsec only, with a tunnel between every pair of fabric nodes and encryption supplying the segmentation

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The three-plane split is the point: VXLAN carries the encapsulated traffic and its VNI, LISP maps endpoint identifiers to locators, and scalable group tags carry policy independently of IP addressing.
</details>

---

### Question 8
**Scenario:** Network device configuration must be automated across many devices.

A. TFTP config copies pushed to each device's startup file, then a reload to apply the new configuration
B. Manual CLI sessions on each device, repeating each change by hand and noting every one in a runbook
C. SNMP writes to the configuration MIB, with a commit step that rolls back changes if the device rejects one
D. Model-driven programmability: NETCONF or RESTCONF with YANG, driven by Ansible or Python

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** NETCONF over SSH with XML and RESTCONF over HTTPS with JSON both operate on structured YANG models, so a change is validated against a schema rather than screen-scraped. SNMP writes are rarely used for configuration and lack transactional semantics.
</details>

---

### Question 9
**Scenario:** Which mechanism provides real-time streaming of device telemetry?

A. Syslog streamed to a collector, which carries counters and interface statistics at one-second intervals
B. SNMP polling
C. Model-driven telemetry: the device pushes data on a subscription, periodic or on-change
D. NetFlow only, which streams every counter and operational state on the device at a configurable rate

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Polling scales poorly and its resolution is bounded by the poll interval. Push-based telemetry with dial-in or dial-out subscriptions gives higher-frequency data at lower device cost, which is what modern assurance platforms consume.
</details>

---

### Question 10
**Scenario:** A packet capture is needed on traffic passing through a switch port.

A. A tap only, since a switch cannot copy frames from one of its own ports to another port or to a remote host
B. SPAN for local capture, RSPAN across a VLAN, or ERSPAN to a remote destination
C. NetFlow
D. Syslog

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SPAN copies frames to a monitor port; ERSPAN encapsulates them in GRE so the analyzer can live anywhere routable. NetFlow gives flow records rather than packets, which answers who talked to whom but not what was in the packets.
</details>

---

### Question 11
**Scenario:** Which QoS model provides per-hop behavior based on packet marking?

A. DiffServ: DSCP markings select a per-hop behavior at each device
B. No QoS
C. Best effort, which marks packets with DSCP values so that each router can pick the per-hop behavior for them
D. IntServ with RSVP, which keeps no per-flow state and so scales to large networks by acting on markings at each hop

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** DiffServ scales because each hop acts on the marking without holding per-flow state. IntServ reserves resources per flow with RSVP and does not scale to a large network, which is why DiffServ is what enterprise designs use.
</details>

---

### Question 12
**Scenario:** A device must authenticate users against a central server for network access.

A. Local accounts configured on every access switch, synchronized nightly from a central template for consistency
B. 802.1X with RADIUS to an identity service, falling back to MAB for devices lacking 802.1X
C. No authentication
D. TACACS+ for network access, which combines authentication and authorization in one exchange for end user ports

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RADIUS handles network access authentication and authorization together, while TACACS+ separates them and is used for device administration. MAC authentication bypass is the fallback for printers and similar devices, and it is weak because MAC addresses are trivially spoofed.
</details>

---

### Question 13
**Scenario:** Which spanning tree feature protects against a switch being connected to an access port?

A. Loop Guard, which blocks a port when it receives a BPDU on a link where an end host should be attached
B. PortFast alone
C. BPDU Guard, which errdisables a PortFast port that receives a BPDU, so a newly attached switch cannot join the tree
D. Root Guard, which errdisables an access port as soon as it receives any BPDU from a newly attached switch

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** BPDU Guard shuts the port when something that speaks spanning tree appears where an end host should be. Root Guard is the different case of preventing a legitimate switch from becoming root through that port.
</details>

---

### Question 14
**Scenario:** A GRE tunnel must carry traffic securely over the internet.

A. A VLAN across the internet path, which isolates the GRE traffic from other users of the transit network
B. GRE over IPsec, since GRE offers no confidentiality itself
C. GRE alone, because its encapsulation hides the inner packets from anyone inspecting the traffic on the internet
D. IPsec cannot carry GRE, so encrypted overlays must use IPsec tunnel mode with static routes and no multicast

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** GRE encapsulates and supports multicast and routing protocols; IPsec encrypts but in tunnel mode does not natively carry multicast. Combining them is what makes a routed, encrypted overlay, and it is the basis of DMVPN.
</details>

---

### Question 15
**Scenario:** Which virtualization technology allows one physical device to appear as multiple logical devices?

A. Trunking, which carves one physical port into logical interfaces and so makes one device appear as several
B. VRFs for routing-table separation, and VDCs for full logical separation
C. EtherChannel, which presents several members as one logical interface and lets a single switch act as separate devices
D. VLANs, which split one switch into logical switches and also give each one its own routing table by default

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** VRFs separate routing tables on shared hardware, which is what makes overlapping address space between tenants possible. VLANs segment at layer 2 only and share a single routing table unless VRFs are added.
</details>

---

### Question 16
**Scenario:** In a Cisco Catalyst SD-WAN fabric, which component distributes routing information and data plane policy to the WAN edge routers using OMP?

A. SD-WAN Manager (vManage), the GUI that stores device templates and pushes configuration to each router
B. SD-WAN Validator (vBond), which authenticates new devices and tells them where the controllers are
C. The WAN edge router itself, which builds the overlay routing table by flooding LSAs to its peers
D. SD-WAN Controller (vSmart), the control plane element that runs OMP with every WAN edge

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The SD-WAN Controller (formerly vSmart) is the centralized control plane: it holds OMP sessions with each WAN edge and distributes routes, TLOCs, and policy. The Manager is the management plane for configuration and monitoring. The Validator handles orchestration, authenticating devices and introducing them to the controllers. WAN edges do not flood LSAs in the overlay.
</details>

---

### Question 17
**Scenario:** Branch APs register to a central WLC across a WAN. Branch users must keep reaching local resources if the WAN link to the controller fails.

A. Local mode APs, which tunnel all client traffic to the WLC through CAPWAP
B. FlexConnect mode APs with local switching of the branch WLANs onto local VLANs
C. Monitor mode APs, which keep serving clients while the WLC is unreachable
D. Sniffer mode APs, which forward captured frames to the local switch instead

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** FlexConnect APs can switch client traffic locally onto branch VLANs and, in standalone mode, keep serving locally switched WLANs when the controller is unreachable. Local mode tunnels all data to the WLC, so a WAN failure stops service. Monitor and sniffer modes do not serve clients.
</details>

---

### Question 18
**Scenario:** A virtualization host runs its hypervisor directly on the server hardware, with no general-purpose operating system underneath.

A. A type 2 hypervisor, which runs as an application on a host operating system
B. A container runtime, which shares the host kernel between isolated processes
C. A type 1 hypervisor, also called a bare-metal hypervisor
D. A virtual switch, which connects virtual machines to the physical network

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A type 1 (bare-metal) hypervisor, such as ESXi, runs directly on hardware. A type 2 hypervisor runs on top of a host OS. Containers share a kernel and are not a hypervisor. A virtual switch is a networking component inside a virtualized host, not the hypervisor itself.
</details>

---

### Question 19
**Scenario:** Two OSPF routers on a link stay stuck in the EXSTART/EXCHANGE state and never reach FULL. Hellos and timers match.

A. The interface MTUs differ, so database description packets are rejected
B. The router IDs differ, which stops the routers from exchanging DBD packets
C. The area numbers differ, which allows a neighbor but stops the LSA exchange
D. The OSPF process IDs differ, which must match for an adjacency to form

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** An MTU mismatch is the classic cause of EXSTART/EXCHANGE: a router drops DBD packets advertising an MTU larger than its own. Router IDs must be unique, so differing IDs are expected. An area mismatch stops the neighbor forming at all, because hellos are rejected. Process IDs are locally significant and need not match.
</details>

---

### Question 20
**Scenario:** An EIGRP route has a successor with a feasible distance of 3000. A second neighbor reports the same prefix with a reported distance of 2500 and a total distance of 4000.

A. It is not a feasible successor, because its total distance of 4000 is higher than 3000
B. It is a feasible successor, because its reported distance of 2500 is lower than the feasible distance
C. It is the new successor, because EIGRP prefers the path with the lower reported distance
D. It is not a feasible successor, because a feasible successor must have equal total distance

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The feasibility condition requires the neighbor's reported distance to be less than the current feasible distance. 2500 is less than 3000, so the path is loop-free and is kept as a feasible successor, even though its total distance is higher. The successor is chosen by lowest total distance, not reported distance, and equal cost is not required.
</details>

---

### Question 21
**Scenario:** Two routers in different autonomous systems must form an eBGP session between their loopback addresses, which are one routed hop apart.

A. Configure the session on the physical addresses, since eBGP cannot use loopback addresses at all
B. Configure next-hop-self on both routers, which allows the TCP session to reach the loopbacks
C. Configure the neighbors as route reflector clients, which removes the eBGP TTL limit
D. Configure update-source loopback and ebgp-multihop (or disable-connected-check) on both routers

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** eBGP packets are sent with a TTL of 1 and the peer is expected to be directly connected, so loopback peering needs ebgp-multihop or disable-connected-check, and update-source so the session is sourced from the loopback, plus a route to the peer's loopback. eBGP can use loopbacks. next-hop-self changes advertised next hops, not session setup. Route reflection is an iBGP feature.
</details>

---

### Question 22
**Scenario:** An AP survey shows a client receiving the signal at -65 dBm, with a noise floor of -90 dBm. What is the signal-to-noise ratio?

A. 155 dB
B. -25 dB
C. 25 dB
D. 65 dB

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** SNR is the difference between the received signal and the noise floor: -65 - (-90) = 25 dB. Adding the magnitudes gives 155, which is meaningless. A negative SNR would mean noise is stronger than the signal. 65 dB is only the signal magnitude.
</details>

---

### Question 23
**Scenario:** A multicast network uses PIM sparse mode. Receivers join a group, but no traffic flows from a new source.

A. Sparse mode floods traffic to every interface and prunes back, so the source must be pruned first
B. IGMP snooping must be disabled on every switch, since it blocks sparse mode traffic by design
C. The source must send IGMP joins toward the receivers before PIM can build any tree
D. A rendezvous point must be configured and known to all routers, statically, by Auto-RP, or by BSR

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** PIM sparse mode builds shared trees rooted at a rendezvous point: sources register with the RP and receivers join toward it, so without a known RP nothing meets. Flood-and-prune is dense mode behavior. IGMP snooping constrains flooding and does not block PIM. Sources do not send IGMP joins; receivers do.
</details>

---

### Question 24
**Scenario:** A static default route points to an ISP. If the ISP's gateway stops answering pings, the route must be withdrawn so a backup route takes over.

A. IP SLA ICMP echo operation, a track object, and the static route bound to that track
B. A floating static route with a higher administrative distance and no tracking at all
C. HSRP on the WAN interface, which removes the static route when the gateway fails
D. A SPAN session on the WAN interface, which detects lost pings and removes the route

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** An IP SLA probe tests reachability, a track object follows its result, and a static route tied to the track is removed when the probe fails, letting a backup route take over. A floating static alone only takes over when the primary interface goes down, not when the far end stops forwarding. HSRP provides gateway redundancy for hosts. SPAN copies traffic for analysis.
</details>

---

### Question 25
**Scenario:** The network team needs to see which applications and hosts consume WAN bandwidth over time, with records of each flow exported to a collector.

A. Syslog at debugging level, which logs every packet that crosses the WAN interface
B. SNMP interface counters, which report bytes per application on each interface
C. Flexible NetFlow with a flow record and an exporter to a collector
D. Port mirroring of the WAN interface to an analyzer for permanent capture

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Flexible NetFlow defines flow records keyed on fields such as addresses, ports, and protocol, and exports them to a collector for long-term traffic analysis. Debug-level syslog is not designed for flow accounting and can overload the device. SNMP counters show totals per interface, not per application. Permanent full capture is heavy and expensive compared with flow records.
</details>

---

### Question 26
**Scenario:** A router's CPU is overwhelmed by a flood of traffic directed at the device itself, causing routing protocol adjacencies to drop.

A. An access list on each user-facing interface, which blocks traffic going to every remote host
B. Control plane policing, which rate-limits traffic destined to the control plane by class
C. Port security, which limits the number of MAC addresses learned on each switch port
D. Unicast RPF in strict mode on every interface, which rate-limits routing protocol packets

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** CoPP applies a QoS policy to traffic punted to the control plane, rate-limiting or dropping classes such as ICMP and management while protecting routing protocol traffic. Interface ACLs for transit traffic do not shape what reaches the CPU. Port security limits MAC addresses on switch ports. uRPF drops spoofed sources and does not rate-limit.
</details>

---

### Question 27
**Scenario:** Traffic on links between switches, and between switches and wired hosts, must be encrypted hop by hop at Layer 2.

A. IPsec in transport mode between every pair of hosts, which encrypts at Layer 2
B. WPA3 Enterprise on the switch ports, which encrypts wired frames between switches
C. 802.1X with MAB only, which encrypts traffic after a host authenticates to the port
D. MACsec (IEEE 802.1AE), which encrypts Ethernet frames on each link

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** MACsec encrypts Ethernet frames between directly connected devices, hop by hop, for switch-to-switch and switch-to-host links, with keys often derived through 802.1X and MKA. IPsec works at Layer 3. WPA3 is a wireless standard. 802.1X and MAB authenticate access and do not encrypt traffic on their own.
</details>

---

### Question 28
**Scenario:** Network administrators' CLI commands must be authorized one by one against a central server, with the whole payload of each exchange encrypted.

A. RADIUS, which encrypts the entire packet and authorizes each CLI command separately
B. TACACS+, which separates authentication, authorization, and accounting and encrypts the full body
C. Local accounts on each device, with privilege levels set the same on every router and switch
D. LDAP, which authorizes each CLI command and logs the commands for accounting

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** TACACS+ uses TCP, separates AAA functions, encrypts the whole packet body, and supports per-command authorization, which makes it the usual choice for device administration. RADIUS combines authentication and authorization, encrypts only the password, and is typical for network access. Local accounts are not central. LDAP is a directory protocol and does not do per-command authorization on network devices.
</details>

---

### Question 29
**Scenario:** A script must change a device's interface configuration using a YANG model, over HTTPS, with JSON payloads.

A. NETCONF over SSH on port 830, which uses JSON payloads with HTTP methods
B. SNMPv3 set operations, which accept YANG-modeled JSON over HTTPS
C. RESTCONF, which exposes YANG data over HTTPS and supports JSON or XML
D. gNMI over SSH on port 22, which sends JSON-encoded CLI commands

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** RESTCONF provides a REST-like HTTP interface to YANG-modeled data, using methods such as GET, PUT, PATCH, and POST, with JSON or XML encoding. NETCONF runs over SSH (port 830) and uses XML with RPC operations. SNMP uses MIBs, not YANG over HTTPS. gNMI runs over gRPC, not SSH, and does not send CLI commands.
</details>

---

### Question 30
**Scenario:** When a specific syslog message about an interface going down appears, the device itself must run a set of CLI commands and send an alert, with no external server involved.

A. An EEM applet with a syslog event detector and CLI actions
B. A Python script on a laptop that polls the device every minute
C. A NETCONF subscription from a controller that applies a template
D. An Ansible playbook triggered by a cron job on a management host

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Embedded Event Manager runs on the device: an applet can match a syslog pattern and run CLI commands, send syslog, or email, with no external dependency. The other options all rely on an external system, and polling or scheduled jobs also add delay.
</details>

---

## Where to go deeper

- [ENCOR cert page](../../exams/cisco/ccnp-enterprise-encor-350-401/) - notes, practice plan, strategy
- [CCNA practice questions](./cisco-ccna.md) - the prerequisite level
- [VPC explained](../../learn/concepts/vpc-explained.md) - how these concepts map to cloud networking
- [DNS explained](../../learn/concepts/dns-explained.md) - plain-English networking primer
- **[📖 Cisco certifications](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/index.html)** - official exam topics
