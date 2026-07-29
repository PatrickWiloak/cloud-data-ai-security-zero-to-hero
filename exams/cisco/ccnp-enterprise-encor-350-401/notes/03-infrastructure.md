---
last-updated: 2026-07-29
---

# ENCOR 03 - Infrastructure

Layer 2 switching, routing protocols, wireless, and IP services. The largest section at
roughly 30% of the exam.

## Layer 2

- **VLAN** - a logical broadcast domain.
- **Trunking (802.1Q)** - carries multiple VLANs, tagging all but the native VLAN.
- **Native VLAN** - untagged on a trunk. Mismatched native VLANs between switches cause traffic to cross VLAN boundaries and generate CDP errors.
- **DTP (Dynamic Trunking Protocol)** - negotiates trunking. Should be disabled (`switchport nonegotiate`) on ports facing end devices, because auto-negotiation enables VLAN hopping.
- **VTP (VLAN Trunking Protocol)** - propagates VLAN databases. Modes: server, client, transparent, and off. A higher revision number overwrites the domain, so inserting a switch with a high revision number can wipe the VLAN database. VTP transparent or version 3 mitigates this.

**Spanning Tree**

- **STP (802.1D)** - prevents loops by blocking redundant paths.
- **RSTP (802.1w)** - rapid convergence, port roles root/designated/alternate/backup.
- **MST (802.1s)** - maps many VLANs onto a few spanning-tree instances, reducing CPU load.
- **PVST+ / Rapid PVST+** - Cisco per-VLAN instances, allowing per-VLAN load balancing.
- **Root bridge election** - lowest bridge ID, which is priority plus MAC address. Priority is set in increments of 4096.
- **Path cost** - lower is better, based on link speed.
- **Port states (RSTP)** - discarding, learning, forwarding.
- **PortFast** - immediate forwarding for access ports connected to end devices.
- **BPDU Guard** - err-disables a PortFast port that receives a BPDU.
- **Root Guard** - prevents a neighbor from becoming root on that port.
- **Loop Guard** - protects against unidirectional link failures causing a blocked port to start forwarding.
- **UDLD** - detects unidirectional fiber links.

Root bridge election and the guard features are staple exam content. Set the root bridge
deliberately with priority rather than letting MAC address decide.

**EtherChannel**

- **LACP (802.3ad)** - standard negotiation; modes active and passive. At least one side must be active.
- **PAgP** - Cisco proprietary; modes desirable and auto. At least one side must be desirable.
- **On** - no negotiation; both sides must be On, and a mismatch causes a loop.
- **Requirements** - matching speed, duplex, VLAN allowed list, and trunk mode across all member ports.
- **Load balancing** - by source/destination MAC, IP, or port. Choose a method that varies across your traffic, or one link carries everything.

## Routing protocols

**EIGRP**

- Advanced distance vector, Cisco-originated, AD 90 internal and 170 external.
- **Metric** - bandwidth and delay by default (K1 and K3).
- **Feasible distance (FD)** - the best metric to a destination.
- **Reported/advertised distance (RD)** - the neighbor's metric to the destination.
- **Feasibility condition** - RD < FD, which guarantees loop freedom.
- **Successor** - the best path. **Feasible successor** - a backup meeting the feasibility condition, allowing instant failover without going active.
- **Active versus passive** - a route goes active when no feasible successor exists and queries must be sent. Stuck-in-active is a scaling problem.

**OSPF**

- Link state, AD 110, metric is cost derived from bandwidth.
- **Areas** - area 0 is the backbone; all other areas must connect to it, directly or via a virtual link.
- **Router types** - internal, backbone, ABR (area border), ASBR (autonomous system boundary).
- **LSA types** - Type 1 router, Type 2 network, Type 3 summary, Type 4 ASBR summary, Type 5 external, Type 7 NSSA external.
- **Area types** - standard, stub (no Type 5), totally stubby (no Type 3 or 5), NSSA (allows Type 7), totally NSSA.
- **Network types** - broadcast (DR/BDR elected), point-to-point (no DR), non-broadcast, point-to-multipoint.
- **DR/BDR election** - highest priority, then highest router ID. Priority 0 means never DR.
- **Adjacency requirements** - matching area, hello and dead timers, subnet, authentication, MTU, and area type. Mismatches are the standard troubleshooting scenario.

**BGP**

- Path vector, AD 20 external and 200 internal, uses TCP 179.
- **eBGP** - between autonomous systems; AD 20; TTL 1 by default so peers must be directly connected unless multihop is configured.
- **iBGP** - within an AS; AD 200; **iBGP routes are not advertised to other iBGP peers**, requiring a full mesh, route reflectors, or confederations.
- **Path selection order** - weight (highest, Cisco-only, local), local preference (highest, AS-wide), locally originated, AS path (shortest), origin (IGP < EGP < incomplete), MED (lowest), eBGP over iBGP, lowest IGP metric to next hop, oldest route, lowest router ID.
- **Attributes** - well-known mandatory (origin, AS path, next hop), well-known discretionary (local preference, atomic aggregate), optional transitive (community, aggregator), optional non-transitive (MED).
- **Route reflector** - relaxes the iBGP full-mesh requirement.

Memorize the BGP path selection order. It is examined directly, and weight before local
preference is the pair most often confused.

## Wireless

- **RF fundamentals** - 2.4 GHz has three non-overlapping channels (1, 6, 11); 5 GHz has many more.
- **Signal metrics** - **RSSI** (received signal strength), **SNR** (signal-to-noise ratio), and noise floor. SNR is the better predictor of usable throughput.
- **802.11 standards** - 802.11n (Wi-Fi 4), ac (Wi-Fi 5), ax (Wi-Fi 6/6E), be (Wi-Fi 7).
- **AP-to-WLC association** - the AP discovers a WLC by DHCP option 43, DNS, broadcast, or a primed controller, then builds a CAPWAP tunnel.
- **Roaming** - intra-controller, inter-controller (Layer 2), and Layer 3 roaming with anchor and foreign controllers.
- **WLAN security** - WPA2 with AES, WPA3 with SAE, 802.1X with EAP, and PSK.

## IP services

- **NTP** - stratum hierarchy; authenticated NTP prevents spoofed time.
- **PTP** - sub-microsecond precision where NTP is insufficient.
- **NAT and PAT** - inside local, inside global, outside local, outside global. Learn the four terms; questions use them precisely.
- **First-hop redundancy**:
  - **HSRP** - Cisco, active and standby, virtual MAC 0000.0c07.acXX, default priority 100, preemption off by default.
  - **VRRP** - standard, master and backup, can use a real interface address as the virtual IP, preemption on by default.
  - **GLBP** - Cisco, load balances across multiple forwarders (AVG and AVFs).
- **SNMP** - v2c uses community strings in clear text; v3 adds authentication and encryption.
- **Syslog severities** - 0 emergency through 7 debug. Lower is more severe.

## Exam pointers

- BGP path selection order, memorized, in sequence.
- OSPF adjacency failures: check area, timers, subnet, MTU, and authentication.
- EIGRP feasible successor requires RD < FD.
- A VTP server with a higher revision number can overwrite the VLAN database.
- LACP active/passive and PAgP desirable/auto; at least one side must actively negotiate.
- HSRP preemption is off by default; VRRP preemption is on.

## Official documentation

**[📖 ENCOR 350-401 exam topics](https://learningnetwork.cisco.com/s/encor-exam-topics)** - authoritative blueprint
**[📖 BGP best path selection algorithm](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/13753-25.html)** - the ordered criteria
**[📖 OSPF design guide](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/7039-1.html)** - areas and LSA types
