---
last-updated: 2026-07-29
---

# Network+ Domain 2 - Network Implementation (20%)

Routing, switching, wireless, and the physical layer. This is where the concepts from
Domain 1 become configuration.

## Routing

- **Static route** - manually configured. Predictable, no protocol overhead, does not adapt to failure.
- **Dynamic route** - learned from a routing protocol. Adapts automatically, at the cost of complexity and CPU.
- **Default route** - 0.0.0.0/0, the route of last resort.
- **Administrative distance (AD)** - trustworthiness of a route source when two protocols offer the same destination. Lower wins.
- **Metric** - the cost used to choose between routes *within* one protocol.
- **Longest prefix match** - the most specific matching route wins, regardless of protocol or metric. This rule is applied before AD.

| Source | AD |
|---|---|
| Directly connected | 0 |
| Static | 1 |
| eBGP | 20 |
| EIGRP (internal) | 90 |
| OSPF | 110 |
| RIP | 120 |
| iBGP | 200 |

**Protocols**

- **RIP** - distance vector, metric is hop count, maximum 15 hops. Simple and slow to converge.
- **OSPF** - link state, metric is cost derived from bandwidth, organized into areas with area 0 as the backbone. The most commonly tested interior protocol.
- **EIGRP** - Cisco's advanced distance vector, metric from bandwidth and delay.
- **BGP** - path vector, the routing protocol of the internet, chooses paths between autonomous systems using policy rather than pure speed.

- **Interior gateway protocol (IGP)** - runs within one autonomous system: RIP, OSPF, EIGRP.
- **Exterior gateway protocol (EGP)** - runs between autonomous systems: BGP.
- **Convergence** - the time for all routers to agree on the topology after a change.

## Switching

- **VLAN (Virtual LAN)** - a logical broadcast domain. Hosts in different VLANs need a router to communicate.
- **Access port** - carries one VLAN, connects to an end device.
- **Trunk port** - carries multiple VLANs between switches, tagging frames with 802.1Q.
- **Native VLAN** - the untagged VLAN on a trunk. Mismatched native VLANs cause traffic to leak between VLANs.
- **Voice VLAN** - a separate VLAN for IP phones, so voice traffic is isolated and prioritized.
- **Inter-VLAN routing** - performed by a Layer 3 switch or a router-on-a-stick subinterface configuration.

**Spanning Tree Protocol**

- **STP (802.1D)** - prevents Layer 2 loops by blocking redundant paths. Without it, a loop causes a broadcast storm that collapses the network.
- **RSTP (802.1w)** - rapid STP, converges in seconds rather than tens of seconds.
- **Root bridge** - the reference point of the spanning tree, elected by lowest bridge ID.
- **PortFast** - moves an access port straight to forwarding, for end devices only.
- **BPDU guard** - disables a port that receives a BPDU, protecting against a rogue switch.
- **Root guard** - prevents a downstream switch from becoming root.

**Other switch features**

- **Link aggregation (LACP, 802.3ad)** - bundles physical links into one logical link for bandwidth and redundancy.
- **Port security** - restricts which MAC addresses may use a port.
- **Port mirroring (SPAN)** - copies traffic to a monitoring port for capture.
- **Power over Ethernet (PoE)** - delivers power over the data cable. 802.3af is roughly 15 W, 802.3at (PoE+) roughly 30 W, 802.3bt (PoE++) higher still. Check the power budget of the switch, not just the port.

## Wireless

| Standard | Common name | Band | Notes |
|---|---|---|---|
| 802.11a | - | 5 GHz | Legacy |
| 802.11b/g | - | 2.4 GHz | Legacy, long range, slow |
| 802.11n | Wi-Fi 4 | 2.4 and 5 GHz | Introduced MIMO |
| 802.11ac | Wi-Fi 5 | 5 GHz | MU-MIMO downlink |
| 802.11ax | Wi-Fi 6 / 6E | 2.4, 5, and 6 GHz | OFDMA, better in dense environments |
| 802.11be | Wi-Fi 7 | 2.4, 5, 6 GHz | Multi-link operation |

- **Channel planning** - in 2.4 GHz only channels 1, 6, and 11 are non-overlapping. Overlapping channels are a leading cause of poor performance.
- **Co-channel interference** - neighboring access points on the same channel contending for airtime.
- **Service set identifier (SSID)** - the wireless network name.
- **BSSID** - the MAC address of the radio, identifying a specific access point.
- **Antenna types** - omnidirectional radiates in all directions; directional (Yagi, parabolic) focuses energy for point-to-point links.
- **Site survey and heat map** - measuring actual coverage and interference before and after deployment.

**Wireless security**

- **WPA2** - AES-CCMP encryption. Still widespread.
- **WPA3** - replaces the pre-shared key handshake with SAE, protecting against offline dictionary attacks.
- **802.1X** - port-based network access control, authenticating users rather than sharing one key. Uses EAP with a RADIUS server.
- **EAP variants** - PEAP and EAP-TTLS tunnel credentials inside TLS; EAP-TLS uses certificates on both sides and is the strongest.
- **Captive portal** - intercepts web traffic to force authentication or acceptance of terms.

## Physical installation

- **Twisted pair categories** - Cat 5e up to 1 Gbps, Cat 6 up to 10 Gbps over shorter runs, Cat 6a 10 Gbps to 100 m, Cat 8 for short data-center runs.
- **100 meter limit** - the maximum copper Ethernet run, 90 m of solid cable plus 10 m of patch leads.
- **Fiber: single-mode versus multimode** - single-mode carries one light path over long distances; multimode is cheaper and used for shorter runs.
- **Straight-through versus crossover** - modern equipment auto-negotiates with Auto-MDIX, making crossover cables largely historical.
- **Rack units (U)** - 1.75 inches of vertical rack space each.
- **Environmental factors** - temperature, humidity, and airflow. Hot aisle and cold aisle containment manages data-center heat.
- **Grounding and bonding** - protects equipment and people, and reduces interference.

## Exam pointers

- Longest prefix match is checked before administrative distance. Questions frequently test the order.
- A trunk carrying only some VLANs is a classic cause of "these two hosts cannot talk but everything else works."
- A broadcast storm with all switch lights flashing is a spanning-tree failure or a physical loop.
- If a wireless problem mentions many access points in a small area, look at channel overlap.
- If a PoE device will not power up, check the switch's total power budget and the PoE standard supported.

## Official documentation

**[📖 CompTIA Network+ N10-009 objectives](https://www.comptia.org/certifications/network#examdetails)** - authoritative domain list
**[📖 IEEE 802.11 standards](https://standards.ieee.org/ieee/802.11/7028/)** - wireless specifications
**[📖 IEEE 802.1Q](https://standards.ieee.org/ieee/802.1Q/10323/)** - VLAN tagging
