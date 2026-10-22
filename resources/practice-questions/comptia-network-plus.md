---
last-updated: 2026-10-22
difficulty: beginner
---

# CompTIA Network+ (N10-009) - Practice Questions

30 questions for Network+ prep across networking concepts (23%), implementation (20%), operations (19%), security (14%), and troubleshooting (24%).

> **Cert page:** [exams/comptia/network-plus/](../../exams/comptia/network-plus/)

---

### Question 1
**Scenario:** Which OSI layer does a router operate at?

A. Layer 4, transport, forwarding by port number
B. Layer 3, network, where packets are forwarded by destination IP address
C. Layer 7, application, where devices inspect HTTP and DNS requests before forwarding them
D. Layer 2, data link, forwarding by MAC address

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Routers forward by IP address at layer 3; switches forward by MAC address at layer 2. Knowing the layer is what tells you which address a device uses and therefore which troubleshooting tool applies.
</details>

---

### Question 2
**Scenario:** A host has IP 192.168.10.50 with mask 255.255.255.0.

A. The mask is invalid for a 192.168 address
B. The network is 192.168.10.0/24, with 254 usable host addresses
C. The network is 192.168.0.0/16, because the first two octets of a private address define the network
D. There are 256 usable hosts, because every address in the 192.168.10.0 block can be assigned to a device

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** 255.255.255.0 is /24, leaving 8 host bits: 256 addresses minus the network and broadcast addresses gives 254 usable. Subnetting arithmetic appears throughout the exam, so practice converting between dotted-decimal masks and CIDR notation fluently.
</details>

---

### Question 3
**Scenario:** TCP versus UDP.

A. They are interchangeable, since each of them guarantees delivery and ordering and they differ only in port numbers
B. UDP is more reliable, because it sends each datagram without a handshake and so cannot be delayed by retransmission
C. TCP has no ordering, because segments are delivered in whatever order the network happens to carry them
D. TCP is connection-oriented with acknowledgment, ordering, and retransmission; UDP is connectionless with lower overhead and no delivery guarantee

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** UDP suits real-time traffic where a late packet is worse than a lost one: voice, video, DNS queries. TCP's three-way handshake (SYN, SYN-ACK, ACK) is a frequent exam item, as is the port list that goes with each protocol.
</details>

---

### Question 4
**Scenario:** A workstation gets a 169.254.x.x address.

A. It has a public IP, assigned by the ISP because the workstation is directly connected to the internet
B. It has a valid static address, which an administrator configured in the 169.254 range for management
C. APIPA: it failed to reach a DHCP server, so check DHCP availability, the relay agent, and layer 2 connectivity
D. It is on the internet, with a working DHCP lease and gateway, and the problem is DNS resolution

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** An APIPA address is a self-assigned link-local fallback and a direct symptom of DHCP failure. Because DHCP uses broadcasts, a client on a different subnet from the server needs a relay agent (IP helper), which is the usual cause when one VLAN works and another does not.
</details>

---

### Question 5
**Scenario:** Which DNS record maps a hostname to an IPv4 address?

A. MX, which lists mail servers
B. CNAME, which makes one name an alias for another name rather than an address
C. A record, mapping a hostname to an IPv4 address
D. AAAA record, for IPv6 addresses

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** An A record is IPv4, AAAA is IPv6, CNAME is an alias to another name, MX routes mail, PTR does reverse lookup, and TXT holds arbitrary text used for SPF and domain verification. Record-type identification is reliably on the exam.
</details>

---

### Question 6
**Scenario:** VLANs are configured and two hosts in different VLANs cannot communicate.

A. Change the cable between the switches
B. That is expected; inter-VLAN routing requires a layer 3 device
C. The VLANs are broken, so erase the switch configuration
D. Add more switches, so that the hosts in each VLAN have another path to reach the other VLAN

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** VLANs create separate broadcast domains by design, so traffic between them must be routed. A router-on-a-stick uses a trunk with subinterfaces; a layer 3 switch does it with switched virtual interfaces. Trunk ports carry tagged frames (802.1Q); access ports carry one untagged VLAN.
</details>

---

### Question 7
**Scenario:** Which topology change prevents switching loops?

A. Increasing bandwidth on the uplinks, which lets the switches absorb a broadcast storm without dropping frames
B. Raising the TTL on Ethernet frames so looping frames expire later
C. Adding more links between the same switches, so that traffic is shared across more parallel paths
D. Spanning Tree Protocol, which blocks redundant paths yet keeps them available for failover

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Without STP, redundant layer 2 links create broadcast storms because frames have no TTL to expire them. STP keeps the redundancy for failover while logically blocking the loop. The symptom is a network that becomes unusable after adding a switch link.
</details>

---

### Question 8
**Scenario:** A user reports slow performance. What is the first troubleshooting step?

A. Identify the problem: gather information, question the user, and find out what changed
B. Replace hardware on the user's workstation and switch port, since slow performance is usually a failing component
C. Reboot the server that hosts the application, and check whether the user still sees slow performance
D. Escalate immediately to the vendor or a tier 3 team, before collecting any detail about the symptoms

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The methodology is examinable in order: identify the problem, establish a theory, test it, establish a plan, implement, verify full functionality, and document. "What changed recently" resolves a large share of real incidents before any tool is opened.
</details>

---

### Question 9
**Scenario:** Which command traces the path a packet takes to a destination?

A. `traceroute` / `tracert`, which lists each hop on the way to the destination by incrementing the TTL
B. `ipconfig`, which shows the IP address, mask, and gateway configured on the local interfaces
C. `ping`, which tests whether a destination answers ICMP echo requests but does not list hops
D. `netstat`, which lists active connections and listening ports on the local host

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Traceroute reveals where a path breaks by incrementing TTL and recording each responding hop. `ping` tests reachability, `netstat` shows connections and listening ports, and `nslookup` or `dig` test name resolution specifically.
</details>

---

### Question 10
**Scenario:** Cable choice for a 100-metre run in an environment with heavy electrical interference.

A. Fiber optic, which is immune to electromagnetic interference
B. Any cable, because the interference limit applies only to runs longer than the 100-metre maximum
C. Coaxial, which is thicker and so reaches farther than twisted pair at the same interference level
D. Unshielded twisted pair, which cancels interference through the twists in each pair at 100 metres

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Fiber is immune to EMI and exceeds copper's 100-metre limit. Shielded twisted pair is the copper mitigation when fiber is not practical. Single-mode fiber goes farther than multimode; multimode is cheaper for short runs.
</details>

---

### Question 11
**Scenario:** Which addresses are reserved for private use?

A. 169.254.0.0/16, the range a host falls back to when no DHCP server answers
B. 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16
C. 1.1.1.1, a public DNS resolver
D. 8.8.8.8, a public DNS resolver address that is routable on the internet

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** These RFC 1918 ranges are not routable on the internet and require NAT for outbound access. 169.254.0.0/16 is the separate link-local APIPA range. Recognizing the middle range's odd /12 boundary (172.16 through 172.31) is a common exam catch.
</details>

---

### Question 12
**Scenario:** A wireless network must authenticate users against a central directory rather than a shared passphrase.

A. WPA2 or WPA3-Enterprise with 802.1X and a RADIUS server backed by the directory
B. WPA3-Personal, with a shared passphrase
C. An open network with a captive portal
D. WEP with a long key, which is easy to rotate but is the only option on very old access points

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Enterprise mode gives per-user credentials, so removing one user does not require rotating a shared key. Personal mode uses a pre-shared key. WEP is broken and should never appear in a correct answer.
</details>

---

### Question 13
**Scenario:** Which device operates at layer 7 and can inspect application content?

A. A media converter, which changes the signal between copper and fiber cabling at layer 1
B. A layer 2 switch, which forwards frames by destination MAC address and sees no application data
C. A next-generation firewall or application-layer proxy
D. A hub, which repeats every signal to all ports at layer 1 and cannot inspect any content

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Traditional firewalls filter on IP, port, and protocol; next-generation firewalls add application awareness, user identity, and intrusion prevention. A load balancer can also operate at layer 7, routing by URL path or hostname.
</details>

---

### Question 14
**Scenario:** Network documentation must support future troubleshooting.

A. Nothing is needed, because the devices store their own configuration and administrators can read it when needed
B. A single spreadsheet of IP addresses
C. Physical and logical diagrams, an IP address plan, cable labels, configuration backups, and a change log
D. Diagrams alone, drawn once at installation, since the topology does not change after that point in the life of the site

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The distinction the exam draws is physical (where cables and devices are) versus logical (how traffic flows, VLANs, subnets, routing). Configuration backups are what turn a failed device into a swap rather than a rebuild.
</details>

---

### Question 15
**Scenario:** High availability is required for the default gateway.

A. Two gateways with manual failover, where an administrator changes each client's gateway address after an outage
B. A second internet link, which adds a path out but leaves clients pointing at a single gateway address
C. More bandwidth on the gateway uplink, which reduces congestion but does not remove the single gateway
D. A first-hop redundancy protocol such as HSRP or VRRP presenting a virtual IP

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** FHRPs let two routers share a virtual IP and MAC so clients never change their gateway setting on failover. Pair it with redundant links and link aggregation (LACP) for a design with no single point of failure at the edge.
</details>

---

### Question 16
**Scenario:** A branch office is given 192.168.50.0/26. How many usable host addresses does that subnet provide?

A. 64, because every address in a /26 block can be assigned to a host including the first and last
B. 30
C. 62 usable hosts
D. 126, because a /26 leaves seven bits for hosts after the network portion of the address

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A /26 leaves 6 host bits, so 2^6 = 64 addresses, minus the network and broadcast addresses gives 62 usable hosts. 64 forgets that the network and broadcast addresses cannot be assigned. 30 is the usable count for a /27. 126 is the usable count for a /25, which has seven host bits, not a /26.
</details>

---

### Question 17
**Scenario:** An administrator needs encrypted command-line access to manage Linux servers remotely. Which protocol and default port fit?

A. SSH on TCP port 22, with key-based or password login
B. Telnet on TCP 23, which encrypts the session with TLS when both ends support it
C. RDP on TCP port 3389
D. SNMP on UDP port 161, which gives a shell on the target server once the community string is known

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** SSH provides an encrypted remote shell and runs on TCP 22 by default. Telnet sends everything, including passwords, in clear text and has no built-in encryption. RDP is a graphical remote desktop protocol, mainly for Windows, not a command-line shell. SNMP is for monitoring and management of devices and does not give a shell.
</details>

---

### Question 18
**Scenario:** A host's IPv6 configuration shows an address beginning with `fe80::`. What kind of address is it?

A. A global unicast address that is routable across the internet
B. A unique local address, the IPv6 equivalent of private IPv4 space such as 10.0.0.0/8
C. A multicast address that delivers each packet to every node in the same multicast group
D. A link-local address, valid only on the local segment and never routed

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `fe80::/10` is link-local: every IPv6 interface has one, and routers never forward it beyond the local link. Global unicast addresses currently come from `2000::/3`. Unique local addresses use `fc00::/7`, usually seen as `fd..`. Multicast addresses start with `ff`.
</details>

---

### Question 19
**Scenario:** A new 2.4 GHz wireless network uses three access points with overlapping coverage. Which channel plan avoids co-channel and adjacent-channel interference?

A. Channels 1, 2 and 3, because adjacent numbers keep the access points close together in the band
B. Channels 1, 6 and 11, spaced so their 20 MHz widths do not overlap
C. Channel 6 on all three, so clients can roam between access points without changing channel
D. Channels 3, 7 and 9, which are spaced evenly across the band and so never overlap with each other

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** In the 2.4 GHz band, channels 1, 6 and 11 are the standard non-overlapping set in most regions. Channels 1, 2 and 3 overlap heavily and cause adjacent-channel interference. Putting every access point on channel 6 creates co-channel contention where coverage overlaps. Channels 3, 7 and 9 still overlap because each 20 MHz channel spans about five channel numbers.
</details>

---

### Question 20
**Scenario:** A link between two switches must carry traffic for VLANs 10, 20 and 30.

A. Configure the link as an 802.1Q trunk that allows VLANs 10, 20 and 30
B. Configure the link as an access port in VLAN 10, which forwards every VLAN by default
C. Run three separate access links, one per VLAN, and enable Spanning Tree on each so they never form a loop
D. Enable port mirroring on the link

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** An 802.1Q trunk tags frames with their VLAN ID so one link can carry several VLANs, and the allowed list limits it to the ones needed. An access port belongs to a single VLAN and does not carry others. Three access links can work but waste ports and do not scale. Port mirroring copies traffic for analysis and does not carry VLANs between switches.
</details>

---

### Question 21
**Scenario:** A company has 25 routers across many sites. Routes must update automatically when a link fails.

A. Static routes on every router, updated by hand by the on-call engineer whenever a link fails
B. A default route on each router pointing to the head office
C. Network address translation on every router, so each site hides behind one public address
D. A dynamic routing protocol such as OSPF running on every router

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A dynamic routing protocol like OSPF shares link-state information between routers and recalculates paths automatically when a link fails. Static routes require manual changes and do not react to failures on their own. A default route to one site ignores alternative paths and creates a single point of failure. NAT translates addresses; it does not build or update routes.
</details>

---

### Question 22
**Scenario:** The network team wants switches to push an alert to the monitoring server the moment an interface goes down, rather than waiting for the next poll.

A. Increase the SNMP polling interval from 5 minutes to 60 minutes so fewer requests are sent to each switch
B. Configure SNMP traps (or informs) to the monitoring server
C. Run a packet capture on the monitoring server
D. Enable NetFlow on every interface, which reports interface status changes as flow records

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SNMP traps and informs are sent by the device as soon as an event, such as link down, occurs, so alerts do not wait for the next poll. Longer polling makes detection slower. A packet capture records traffic but does not generate device alerts. NetFlow reports traffic flows, not interface state changes.
</details>

---

### Question 23
**Scenario:** A network printer gets its address from DHCP, but users' saved print settings break each time its address changes.

A. Shorten the DHCP lease time to one hour
B. Disable DHCP on the whole subnet and give every device a static address by hand
C. Create a DHCP reservation for the printer's MAC address
D. Move the printer to the guest VLAN, which keeps device addresses fixed for the length of each visit

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A DHCP reservation always hands the same address to that MAC address, giving a stable IP while still managing it centrally. Shorter leases make the address change more often, not less. Static addressing for every device is a lot of manual work and error-prone. Guest VLANs are for isolation, not fixed addressing.
</details>

---

### Question 24
**Scenario:** A business needs a disaster recovery site that can take over within minutes, with current data and running equipment.

A. A hot site with running systems and replicated data
B. A cold site, which has power and space but needs equipment installed and data restored first
C. A warm site, which has some equipment but needs data and configuration loaded before use
D. Off-site tape backups

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A hot site has equipment running and data replicated, so failover takes minutes. A cold site provides space and power only, so recovery takes days or weeks. A warm site has some equipment but needs data and setup, so recovery takes hours to days. Tape backups protect data but give you nowhere to run it.
</details>

---

### Question 25
**Scenario:** An attacker plugs into an open office wall port and floods the switch with fake MAC addresses so it starts flooding traffic out of every port.

A. Configure a longer MAC address table aging time so learned addresses stay in the table for longer
B. Move the management interface of the switch to a different VLAN from the user ports
C. Enable jumbo frames on the access ports
D. Enable port security to limit the number of MAC addresses learned per port

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Port security caps how many MAC addresses a port can learn and can shut the port down on a violation, which stops MAC flooding. A longer aging time keeps fake entries longer and helps the attacker fill the table. Moving the management VLAN is good practice but does not stop table overflow. Jumbo frames change frame size and have nothing to do with MAC learning.
</details>

---

### Question 26
**Scenario:** Users intermittently receive addresses from a small router someone brought from home, and lose network access.

A. Block UDP port 53 on the access switches
B. Enable DHCP snooping and trust only the port facing the real DHCP server
C. Reduce the size of the legitimate DHCP scope so the rogue server's offers are ignored by clients
D. Enable Spanning Tree PortFast on every access port so the rogue router cannot form a loop

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** DHCP snooping lets the switch drop DHCP server messages on untrusted ports, so only the trusted uplink to the real server can hand out addresses. Port 53 is DNS, not DHCP. A smaller legitimate scope does not make clients ignore a rogue server. PortFast speeds up port startup and does nothing about DHCP.
</details>

---

### Question 27
**Scenario:** A server link shows slow throughput, late collisions and rising CRC errors on one side. The other side reports no collisions.

A. A DNS misconfiguration on the server
B. An expired DHCP lease on the switch port
C. A duplex mismatch between the server and the switch port
D. A wrong VLAN assignment, which causes collisions only on the server side of the link

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** When one side runs full duplex and the other half duplex, the half-duplex side sees late collisions and CRC errors while throughput collapses. DNS problems affect name resolution, not interface error counters. Switch ports do not hold DHCP leases. A wrong VLAN stops traffic from reaching the right network rather than causing collisions.
</details>

---

### Question 28
**Scenario:** A workstation can reach other hosts on its own subnet but nothing on other subnets or the internet. Its IP and mask are correct.

A. The default gateway is missing or wrong
B. The network cable is faulty
C. The DNS server address is wrong, which blocks all traffic to other subnets by IP as well as by name
D. The switch port is disabled

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Local traffic works without a gateway, but anything off-subnet must be sent to the default gateway, so a wrong or missing gateway breaks only remote destinations. A faulty cable or a disabled port would stop local traffic too. Wrong DNS breaks name lookups, but traffic to remote IP addresses would still work.
</details>

---

### Question 29
**Scenario:** A user can ping 8.8.8.8 but cannot open any website by name.

A. The default gateway is wrong, which allows ICMP to the internet but blocks all TCP traffic
B. The firewall is blocking ICMP
C. The network interface card has failed and needs replacing
D. Name resolution is failing, so check the configured DNS servers and test with `nslookup`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Reaching an internet IP proves routing and connectivity are fine, so failure by name points at DNS; `nslookup` or `dig` confirms it. A wrong gateway would also stop the ping. ICMP clearly gets through, since the ping works. A failed NIC would stop all traffic, including the ping.
</details>

---

### Question 30
**Scenario:** After six new PoE cameras were added to a switch, several existing access points on the same switch keep rebooting.

A. The cameras use a different VLAN from the access points
B. The switch's total PoE power budget has been exceeded by the new load
C. The access points need a firmware update to support cameras on the same switch
D. The cable runs to the access points are now longer than 100 metres because the switch has more devices on it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A PoE switch has a fixed total power budget; when connected devices draw more than it can supply, it drops power to some ports and those devices reboot. VLAN membership does not affect power. Access points do not need firmware to coexist with cameras. Cable length is physical and did not change when cameras were added.
</details>

---

## Where to go deeper

- [Network+ cert page](../../exams/comptia/network-plus/) - notes, practice plan, strategy
- [Security+ practice questions](https://security.noblerworks.com/resources/practice-questions/comptia-security-plus/) - the security sibling
- [CCNA practice questions](./cisco-ccna.md) - the vendor-specific counterpart
- [Networking topic index](../../topics/networking.md) - cloud networking builds on this
- **[📖 CompTIA Network+](https://www.comptia.org/certifications/network)** - official exam objectives
