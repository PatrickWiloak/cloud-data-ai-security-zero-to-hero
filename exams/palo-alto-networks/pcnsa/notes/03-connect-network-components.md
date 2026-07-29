---
last-updated: 2026-07-29
---

# PCNSA Domain 3 - Connect and Secure Network Components

Interfaces, zones, routing, NAT, and the supporting services. NAT is the highest-yield
topic in this domain.

## Interface types

- **Layer 3** - has an IP address, participates in routing. The general-purpose choice.
- **Layer 2** - switches frames within a VLAN; no IP on the interface itself.
- **Virtual Wire** - two interfaces bonded, passing traffic transparently. No IP, no routing, no MAC changes, so it can be inserted into an existing segment without redesign.
- **Tap** - receives a mirrored copy for visibility only. Cannot block.
- **Aggregate Ethernet (AE)** - bonded physical interfaces for bandwidth and redundancy.
- **Subinterface** - VLAN-tagged logical interface on a physical port.
- **Loopback** - virtual interface, used for management, GlobalProtect portals, and routing.
- **Tunnel** - terminates IPsec or GlobalProtect tunnels.

An interface passes no traffic until it is assigned to a **virtual router** (for Layer 3)
and a **security zone**.

## Zones

- **Security zone** - a grouping of interfaces sharing security treatment. Every rule is written zone to zone.
- **Zone types** - must match the interface type: Layer 3 interfaces go in Layer 3 zones, and so on.
- **Intrazone default rule** - traffic within a zone is allowed by default.
- **Interzone default rule** - traffic between zones is denied by default.
- **Zone protection profile** - defends against floods (SYN, UDP, ICMP), reconnaissance (port scans, host sweeps), and packet-based attacks. Applied to a zone, not to a rule.

The two default rules can be overridden and, importantly, can have logging enabled. By
default they do not log, which is why "traffic is being denied but I see nothing in the
logs" is a common scenario.

## Virtual routers and routing

- **Virtual router (VR)** - an independent routing instance. Multiple VRs give routing separation on one firewall.
- **Static route** - manually defined, with optional path monitoring to withdraw the route when the next hop is unreachable.
- **Dynamic routing** - OSPF, BGP, and RIP are supported.
- **Route redistribution** - importing routes between protocols.
- **Administrative distance** - preference between route sources when the destination matches.
- **Policy-based forwarding (PBF)** - overrides the routing table based on source, application, or service. The usual answer for sending specific traffic out a particular link regardless of routes.

Remember from the packet flow: the forwarding lookup determines the egress interface and
therefore the destination zone *before* security policy is evaluated.

## NAT

The most-tested topic in this domain.

- **Source NAT** - translates the source address of outbound traffic. Types: dynamic IP and port (many to one, the common internet access case), dynamic IP (many to many), and static IP (one to one).
- **Destination NAT** - translates the destination address of inbound traffic, publishing an internal server on a public address.
- **Bi-directional NAT** - a static source NAT option that automatically creates the matching destination NAT.
- **U-Turn NAT (hairpin)** - internal clients reaching an internal server via its public address. Requires careful zone handling and is a favourite scenario.

**The rule that decides most NAT questions**

Security policy is evaluated using the **original, pre-NAT IP addresses** but the
**post-NAT zone**.

For inbound traffic to a server published by destination NAT:

- The NAT rule uses the *pre-NAT destination* (the public address) with the source zone untrust and destination zone untrust, because the routing lookup happens before translation.
- The security rule uses the *pre-NAT destination address* (the public address) but the destination zone of the *server's actual zone* (for example DMZ).

Writing the security rule with the private address is the classic error, and produces
traffic that is denied despite an apparently correct rule.

## DHCP, DNS, and supporting services

- **DHCP server, relay, and client** - the firewall can act as any of the three on a Layer 3 interface.
- **DNS proxy** - the firewall resolves on behalf of clients, allowing DNS-based policy and split DNS.
- **Service route** - specifies which interface and source address the firewall uses for its own outbound services (updates, DNS, syslog, LDAP). Management traffic defaults to the management interface.
- **NTP** - time synchronisation, which matters for log correlation and certificate validation.

## VPN

- **Site-to-site IPsec** - connects networks. Configuration comprises an IKE gateway, an IPsec tunnel, a tunnel interface, and routing (static or dynamic) pointing at the tunnel.
- **IKE phase 1** - authenticates peers and builds a secure channel. Main mode or aggressive mode.
- **IKE phase 2** - negotiates the IPsec SA that protects the data.
- **Proxy IDs** - define the interesting traffic for the tunnel; mismatches with a peer are a leading cause of phase 2 failure.
- **Tunnel monitoring** - detects a tunnel that is up but not passing traffic.
- **GlobalProtect** - remote access. Comprises a **portal** (configuration distribution and agent download) and one or more **gateways** (the actual tunnel termination and enforcement).

Tunnel interfaces must be in a zone and referenced by a route, or traffic will never reach
the tunnel.

## Exam pointers

- Security policy: pre-NAT addresses, post-NAT zones. If you learn one thing from this domain, learn this.
- Interzone default is deny, intrazone default is allow, and neither logs by default.
- Virtual Wire requires no IP addressing or routing changes.
- Policy-based forwarding overrides the routing table.
- Zone protection profiles attach to zones and handle floods and reconnaissance; security profiles attach to rules and handle content.
- GlobalProtect portal distributes configuration; the gateway terminates the tunnel.

## Official documentation

**[📖 PAN-OS networking](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-networking-admin)** - interfaces, routing, NAT
**[📖 NAT configuration examples](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/networking/nat)** - including U-Turn NAT
**[📖 GlobalProtect administration](https://docs.paloaltonetworks.com/globalprotect)** - portal and gateway architecture
