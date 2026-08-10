---
last-updated: 2026-08-09
difficulty: beginner
---

# CompTIA Network+ (N10-009) - Practice Questions

15 questions for Network+ prep across networking concepts, implementation, operations, security, and troubleshooting.

> **Cert page:** [exams/comptia/network-plus/](../../exams/comptia/network-plus/)

---

### Question 1
**Scenario:** Which OSI layer does a router operate at?

A. Layer 2, data link
B. Layer 3, network
C. Layer 4, transport
D. Layer 7, application

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Routers forward by IP address at layer 3; switches forward by MAC address at layer 2. Knowing the layer is what tells you which address a device uses and therefore which troubleshooting tool applies.
</details>

---

### Question 2
**Scenario:** A host has IP 192.168.10.50 with mask 255.255.255.0.

A. The network is 192.168.10.0/24 with 254 usable host addresses
B. The network is 192.168.0.0/16
C. There are 256 usable hosts
D. The mask is invalid

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** 255.255.255.0 is /24, leaving 8 host bits: 256 addresses minus the network and broadcast addresses gives 254 usable. Subnetting arithmetic appears throughout the exam, so practice converting between dotted-decimal masks and CIDR notation fluently.
</details>

---

### Question 3
**Scenario:** TCP versus UDP.

A. They are interchangeable
B. TCP is connection-oriented with acknowledgment, ordering, and retransmission; UDP is connectionless with lower overhead and no delivery guarantee
C. UDP is more reliable
D. TCP has no ordering

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** UDP suits real-time traffic where a late packet is worse than a lost one: voice, video, DNS queries. TCP's three-way handshake (SYN, SYN-ACK, ACK) is a frequent exam item, as is the port list that goes with each protocol.
</details>

---

### Question 4
**Scenario:** A workstation gets a 169.254.x.x address.

A. It has a valid static address
B. APIPA: it failed to reach a DHCP server, so check DHCP availability, the relay agent, and layer 2 connectivity
C. It is on the internet
D. It has a public IP

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** An APIPA address is a self-assigned link-local fallback and a direct symptom of DHCP failure. Because DHCP uses broadcasts, a client on a different subnet from the server needs a relay agent (IP helper), which is the usual cause when one VLAN works and another does not.
</details>

---

### Question 5
**Scenario:** Which DNS record maps a hostname to an IPv4 address?

A. A record
B. AAAA record
C. CNAME
D. MX

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A is IPv4, AAAA is IPv6, CNAME is an alias to another name, MX routes mail, PTR does reverse lookup, and TXT holds arbitrary text used for SPF and domain verification. Record-type identification is reliably on the exam.
</details>

---

### Question 6
**Scenario:** VLANs are configured and two hosts in different VLANs cannot communicate.

A. That is expected; inter-VLAN routing requires a layer 3 device
B. VLANs are broken
C. Add more switches
D. Change the cable

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** VLANs create separate broadcast domains by design, so traffic between them must be routed. A router-on-a-stick uses a trunk with subinterfaces; a layer 3 switch does it with switched virtual interfaces. Trunk ports carry tagged frames (802.1Q); access ports carry one untagged VLAN.
</details>

---

### Question 7
**Scenario:** Which topology change prevents switching loops?

A. Adding more links
B. Spanning Tree Protocol, which blocks redundant paths while keeping them available for failover
C. Removing all redundancy
D. Increasing bandwidth

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Without STP, redundant layer 2 links create broadcast storms because frames have no TTL to expire them. STP keeps the redundancy for failover while logically blocking the loop. The symptom is a network that becomes unusable after adding a switch link.
</details>

---

### Question 8
**Scenario:** A user reports slow performance. What is the first troubleshooting step?

A. Reboot the server
B. Identify the problem: gather information, question the user, and determine what changed
C. Replace hardware
D. Escalate immediately

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The methodology is examinable in order: identify the problem, establish a theory, test it, establish a plan, implement, verify full functionality, and document. "What changed recently" resolves a large share of real incidents before any tool is opened.
</details>

---

### Question 9
**Scenario:** Which command traces the path a packet takes to a destination?

A. `ping`
B. `traceroute` / `tracert`
C. `ipconfig`
D. `netstat`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Traceroute reveals where a path breaks by incrementing TTL and recording each responding hop. `ping` tests reachability, `netstat` shows connections and listening ports, and `nslookup` or `dig` test name resolution specifically.
</details>

---

### Question 10
**Scenario:** Cable choice for a 100-metre run in an environment with heavy electrical interference.

A. Unshielded twisted pair
B. Fiber optic, which is immune to electromagnetic interference
C. Coaxial
D. Any cable

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Fiber is immune to EMI and exceeds copper's 100-metre limit. Shielded twisted pair is the copper mitigation when fiber is not practical. Single-mode fiber goes farther than multimode; multimode is cheaper for short runs.
</details>

---

### Question 11
**Scenario:** Which addresses are reserved for private use?

A. 8.8.8.8
B. 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16
C. 1.1.1.1
D. 169.254.0.0/16

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** These RFC 1918 ranges are not routable on the internet and require NAT for outbound access. 169.254.0.0/16 is the separate link-local APIPA range. Recognizing the middle range's odd /12 boundary (172.16 through 172.31) is a common exam catch.
</details>

---

### Question 12
**Scenario:** A wireless network must authenticate users against a central directory rather than a shared passphrase.

A. WPA3-Personal
B. WPA2 or WPA3-Enterprise with 802.1X and a RADIUS server
C. WEP
D. An open network with a captive portal

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Enterprise mode gives per-user credentials, so removing one user does not require rotating a shared key. Personal mode uses a pre-shared key. WEP is broken and should never appear in a correct answer.
</details>

---

### Question 13
**Scenario:** Which device operates at layer 7 and can inspect application content?

A. A layer 2 switch
B. A next-generation firewall or application-layer proxy
C. A hub
D. A media converter

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Traditional firewalls filter on IP, port, and protocol; next-generation firewalls add application awareness, user identity, and intrusion prevention. A load balancer can also operate at layer 7, routing by URL path or hostname.
</details>

---

### Question 14
**Scenario:** Network documentation must support future troubleshooting.

A. Nothing is needed
B. Physical and logical diagrams, an IP address plan, rack and cable labeling, configuration backups, and a change log
C. Diagrams alone
D. A single spreadsheet of IPs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The distinction the exam draws is physical (where cables and devices are) versus logical (how traffic flows, VLANs, subnets, routing). Configuration backups are what turn a failed device into a swap rather than a rebuild.
</details>

---

### Question 15
**Scenario:** High availability is required for the default gateway.

A. Two gateways with manual failover
B. A first-hop redundancy protocol such as HSRP or VRRP presenting a virtual IP
C. A second internet link
D. More bandwidth

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** FHRPs let two routers share a virtual IP and MAC so clients never change their gateway setting on failover. Pair it with redundant links and link aggregation (LACP) for a design with no single point of failure at the edge.
</details>

---

## Where to go deeper

- [Network+ cert page](../../exams/comptia/network-plus/) - notes, practice plan, strategy
- [Security+ practice questions](./comptia-security-plus.md) - the security sibling
- [CCNA practice questions](./cisco-ccna.md) - the vendor-specific counterpart
- [Networking topic index](../../topics/networking.md) - cloud networking builds on this
- **[📖 CompTIA Network+](https://www.comptia.org/certifications/network)** - official exam objectives
