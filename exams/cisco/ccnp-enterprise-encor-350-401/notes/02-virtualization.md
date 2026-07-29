---
last-updated: 2026-07-29
---

# ENCOR 02 - Virtualization

Device virtualisation, path virtualisation, and the tunnelling technologies that build
overlays. Roughly 10% of the exam.

## Device virtualisation

- **Hypervisor** - type 1 runs on bare metal (ESXi, KVM); type 2 runs on a host OS.
- **Virtual machine** - a full guest OS with its own kernel.
- **Container** - shares the host kernel, isolated by namespaces and cgroups. Lighter and faster to start than a VM, with weaker isolation. See [containers versus VMs](../../../../learn/concepts/containers-vs-vms.md).
- **Virtual switching** - vSwitch, distributed vSwitch, or Cisco Nexus 1000v, connecting VMs to the physical network.
- **Virtual network functions (VNF)** - routers, firewalls, and load balancers running as software, for example CSR 1000v and Cisco ISRv.
- **Cisco ENCS / NFVIS** - the platform for hosting VNFs at branch sites.

## Device contexts and virtual switches

- **VRF (Virtual Routing and Forwarding)** - multiple independent routing tables on one device. Interfaces are assigned to a VRF, and routes in one VRF are invisible to another. Used for tenant separation and for keeping management traffic separate.
- **VRF-lite** - VRFs without MPLS, the common enterprise use.
- **VDC (Virtual Device Context)** - Nexus feature partitioning one physical switch into multiple logical switches with separate configuration and processes.
- **StackWise Virtual / VSS** - the reverse: several physical switches presented as one logical device.

VRF separates routing; VDC separates the whole device; VSS combines devices. Getting the
direction right is what the exam checks.

## Tunnelling and path virtualisation

- **GRE (Generic Routing Encapsulation)** - simple point-to-point tunnel, carries multicast and routing protocols, but provides **no encryption**. Protocol 47.
- **IPsec** - encryption, authentication, and integrity. Does not natively carry multicast or routing protocols, which is why it is often paired with GRE.
- **GRE over IPsec** - the standard combination: GRE carries the routing protocols and multicast, IPsec provides the encryption.
- **DMVPN (Dynamic Multipoint VPN)** - hub-and-spoke that builds dynamic spoke-to-spoke tunnels. Components: **mGRE** (multipoint GRE), **NHRP** (Next Hop Resolution Protocol, mapping tunnel addresses to physical addresses), and IPsec for protection.
  - **Phase 1** - all traffic through the hub.
  - **Phase 2** - dynamic spoke-to-spoke tunnels, spokes need full routing information.
  - **Phase 3** - hub sends NHRP redirects, allowing summarisation at the hub while still building spoke-to-spoke tunnels.
- **LISP (Locator/ID Separation Protocol)** - separates *who* a device is (EID, endpoint identifier) from *where* it is (RLOC, routing locator). Components: map server, map resolver, ingress tunnel router (ITR), and egress tunnel router (ETR). Underpins SD-Access mobility.
- **VXLAN** - MAC-in-UDP encapsulation extending Layer 2 over a Layer 3 underlay. Uses a **VNI (VXLAN Network Identifier)** of 24 bits, giving about 16 million segments against VLAN's 4094. UDP port 4789. Endpoints are **VTEPs** (VXLAN tunnel endpoints).

VXLAN's 24-bit VNI versus VLAN's 12-bit ID is the scalability point most often examined.

## Comparing the tunnel technologies

| Technology | Encryption | Multicast/routing protocols | Typical use |
|---|---|---|---|
| GRE | No | Yes | Carrying protocols across an IP network |
| IPsec | Yes | No (natively) | Confidentiality over untrusted transport |
| GRE over IPsec | Yes | Yes | Site-to-site with dynamic routing |
| DMVPN | Yes (with IPsec) | Yes | Scalable hub-and-spoke with dynamic spokes |
| VXLAN | No (natively) | Via underlay | Layer 2 extension over Layer 3 fabric |
| LISP | No | n/a | Endpoint mobility and location separation |

## Network virtualisation in the fabric

- **Underlay** - the physical routed network providing IP reachability between fabric nodes. Usually a simple IGP such as IS-IS or OSPF.
- **Overlay** - the virtual topology built with VXLAN tunnels.
- **Control plane for the overlay** - LISP in SD-Access, BGP EVPN in data-centre fabrics.
- **Macro-segmentation** - separation using virtual networks (VRFs), keeping whole groups apart.
- **Micro-segmentation** - separation within a virtual network using SGTs, controlling traffic between groups on the same subnet.

Macro-segmentation uses VNs/VRFs; micro-segmentation uses SGTs. The distinction is
directly examined.

## Exam pointers

- GRE has no encryption. If a question needs both encryption and routing protocol support, the answer is GRE over IPsec or DMVPN.
- DMVPN phase 3 uses NHRP redirects and allows hub summarisation.
- VXLAN uses a 24-bit VNI and UDP 4789; VTEPs are the tunnel endpoints.
- LISP separates EID (identity) from RLOC (location).
- VRF separates routing tables on one device; VDC partitions the device itself.
- Macro-segmentation is VRF-based; micro-segmentation is SGT-based.

## Official documentation

**[📖 ENCOR 350-401 exam topics](https://learningnetwork.cisco.com/s/encor-exam-topics)** - authoritative blueprint
**[📖 DMVPN configuration guide](https://www.cisco.com/c/en/us/support/security/dynamic-multipoint-vpn-dmvpn/series.html)** - phases and NHRP
**[📖 VXLAN overview](https://www.cisco.com/c/en/us/products/switches/data-center-switches/index.html)** - encapsulation and VTEPs
