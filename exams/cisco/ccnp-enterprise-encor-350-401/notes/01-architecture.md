---
last-updated: 2026-07-29
---

# ENCOR 01 - Architecture

Enterprise design, SD-WAN, SD-Access, QoS, and the hardware and software switching model.
Roughly 15% of the exam, and the conceptual foundation for the rest.

## Enterprise campus design

- **Three-tier model** - access, distribution, and core. Used in large campuses where core and distribution serve too many devices to collapse.
- **Two-tier (collapsed core)** - distribution and core combined. Standard in small and medium campuses.
- **Access layer** - end-device connectivity, port security, PoE, and VLAN assignment.
- **Distribution layer** - aggregation, routing between VLANs, policy enforcement, and route summarization.
- **Core layer** - high-speed transport between distribution blocks. Kept simple: no policy, no filtering.
- **Spine-leaf** - the data-center topology giving predictable any-to-any latency, with every leaf connected to every spine and no leaf-to-leaf links.

Design questions usually reward keeping the core simple and pushing policy to the
distribution layer.

## High availability design

- **Redundancy** - hardware (supervisors, power), link (EtherChannel), and device (chassis pairs).
- **StackWise** - stacking access switches so they behave as one logical device.
- **VSS / StackWise Virtual** - two chassis operating as a single logical switch, removing the need for STP blocking on the uplinks and for a first-hop redundancy protocol.
- **Graceful Restart / Non-Stop Forwarding (NSF)** - forwarding continues during a control-plane switchover.
- **Stateful Switchover (SSO)** - the standby supervisor keeps state so failover does not reset sessions.
- **First-hop redundancy** - HSRP, VRRP, and GLBP, covered in the infrastructure note.

## Switching model

- **Process switching** - each packet handled by the CPU. Slowest; used only where no faster path exists.
- **CEF (Cisco Express Forwarding)** - the default. Builds a **FIB** (Forwarding Information Base) from the routing table and an **adjacency table** from ARP, so forwarding decisions require no per-packet CPU work.
- **FIB versus RIB** - the RIB is the control-plane routing table; the FIB is the data-plane forwarding table derived from it.
- **TCAM** - the hardware table matching ACLs, QoS, and forwarding entries at line rate.
- **Control plane, data plane, management plane** - control builds the tables, data forwards traffic, management provides administrative access. This separation underpins SDN.

CEF is the default and the expected answer for hardware forwarding. Punting to the CPU
(process switching) is what happens when CEF cannot handle a packet.

## Software-defined networking concepts

- **SDN** - separation of control plane from data plane, with centralized control.
- **Northbound API** - between the controller and applications, typically REST.
- **Southbound API** - between the controller and network devices: NETCONF, RESTCONF, OpenFlow, or vendor protocols.
- **Overlay and underlay** - the underlay is the physical IP transport; the overlay is the virtual topology built on top with tunnels.
- **Fabric** - the combination of underlay, overlay, and a control plane that maps endpoints.

## Cisco SD-Access

- **SD-Access** - Cisco's campus fabric, managed by DNA Center (now Catalyst Center).
- **Control plane node** - runs LISP, maintaining the endpoint identity-to-location database.
- **Edge node** - the access switch where endpoints connect.
- **Border node** - connects the fabric to external networks.
- **Fabric components** - VXLAN for data-plane encapsulation, LISP for control plane, and Cisco TrustSec (SGTs) for policy.
- **Scalable Group Tag (SGT)** - a policy tag carried with traffic so policy follows the user rather than the IP address.
- **Catalyst Center / DNA Center** - automation, assurance, and policy management.

The triad to memorize: **LISP control plane, VXLAN data plane, TrustSec policy**.

## Cisco SD-WAN

- **vManage** - centralized management and configuration GUI.
- **vSmart** - the control plane, distributing policy and routes using OMP.
- **vBond** - the orchestrator, performing authentication and NAT traversal to introduce devices to each other.
- **vEdge / cEdge** - the data-plane routers at each site.
- **OMP (Overlay Management Protocol)** - distributes routing, TLOC, and service information between vSmart and edge devices.
- **TLOC (Transport Locator)** - identifies a WAN transport attachment point.
- **Benefits** - transport independence, centralized policy, application-aware routing, and zero-touch provisioning.

vBond authenticates and introduces, vSmart distributes policy, vManage manages, vEdge
forwards. Role questions are common.

## Wireless architecture

- **Autonomous AP** - standalone, self-configured.
- **Lightweight AP with WLC** - the AP tunnels traffic to a wireless LAN controller using CAPWAP.
- **CAPWAP** - control (UDP 5246) and data (UDP 5247) tunnels between AP and WLC.
- **Local mode** - traffic tunnelled back to the WLC. Simple, but adds a hairpin.
- **FlexConnect** - traffic switched locally at the branch, control still centralized. The answer for branches with a slow WAN link.
- **Split MAC architecture** - real-time functions on the AP, management functions on the WLC.
- **AP modes** - local, FlexConnect, monitor, sniffer, rogue detector, bridge.

## Quality of Service

- **Classification and marking** - identify traffic and mark it, ideally as close to the source as possible.
- **DSCP** - 6 bits in the IP header. Key values: **EF (46)** for voice, **AF41 (34)** for interactive video, **CS6 (48)** for network control, and **DF (0)** for best effort.
- **CoS** - 3 bits in the 802.1Q header, Layer 2 only, so it is lost when the frame is routed.
- **Trust boundary** - where markings from downstream devices are accepted. Untrusted markings should be rewritten at the access layer.
- **Queuing** - CBWFQ provides bandwidth guarantees; LLQ adds a strict priority queue for voice.
- **Policing** - drops or re-marks traffic above a rate. Does not buffer, so it causes TCP retransmissions.
- **Shaping** - buffers traffic to a rate, smoothing bursts. Adds delay but avoids drops.

Policing drops, shaping buffers. Shaping is applied outbound; policing can be either.

## Exam pointers

- CEF is the default forwarding method; FIB comes from the RIB.
- SD-Access: LISP control plane, VXLAN data plane, TrustSec policy.
- SD-WAN: vBond orchestrates and authenticates, vSmart controls, vManage manages, vEdge forwards.
- FlexConnect is the answer for branch APs on constrained WAN links.
- EF (46) marks voice; LLQ is the queuing mechanism that serves it.
- Shaping buffers and delays; policing drops or re-marks.

## Official documentation

**[📖 ENCOR 350-401 exam topics](https://learningnetwork.cisco.com/s/encor-exam-topics)** - authoritative blueprint
**[📖 Cisco SD-Access design guide](https://www.cisco.com/c/en/us/solutions/design-zone.html)** - fabric architecture
**[📖 Cisco SD-WAN documentation](https://www.cisco.com/c/en/us/support/routers/sd-wan/series.html)** - component roles
