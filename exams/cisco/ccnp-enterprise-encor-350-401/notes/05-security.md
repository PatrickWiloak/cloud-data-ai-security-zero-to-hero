---
last-updated: 2026-07-29
---

# ENCOR 05 - Security

Device hardening, access control, and network security features. Roughly 20% of the exam.

## Device access control

- **AAA** - authentication (who you are), authorisation (what you may do), accounting (what you did).
- **TACACS+** - TCP 49, encrypts the entire payload, separates authentication from authorisation. Preferred for device administration because it supports per-command authorisation.
- **RADIUS** - UDP 1812/1813 (or legacy 1645/1646), encrypts only the password, combines authentication and authorisation. Preferred for network access such as 802.1X.
- **Local authentication fallback** - a local account configured as a backup method so loss of the AAA server does not lock you out. Configuring AAA without a fallback is how administrators lock themselves out of production.
- **Privilege levels** - 0, 1 (user EXEC), and 15 (privileged EXEC), with custom levels in between.
- **Role-based CLI (parser views)** - finer-grained command restriction than privilege levels.
- **Line protection** - `transport input ssh`, ACLs on VTY lines, `exec-timeout`, and `login block-for` to slow brute force.

TACACS+ for device administration, RADIUS for network access. This comparison appears on
every Cisco exam.

## Control plane protection

- **CoPP (Control Plane Policing)** - a QoS policy applied to the control plane, rate-limiting traffic punted to the CPU so a flood cannot starve it.
- **Control Plane Protection (CPPr)** - subdivides the control plane into host, transit, and CEF-exception subinterfaces for finer policing.
- **Routing protocol authentication** - MD5 or SHA on OSPF, EIGRP, and BGP prevents an attacker injecting routes.
- **BGP TTL Security (GTSM)** - accepts BGP packets only with a high TTL, so distant spoofed peers are rejected.

## Layer 2 security

- **Port security** - limits MAC addresses per port; violation actions are protect (drop silently), restrict (drop and log), and shutdown (err-disable, the default).
- **DHCP snooping** - trusts only designated ports to serve DHCP, building a binding table of IP-to-MAC-to-port.
- **Dynamic ARP Inspection (DAI)** - validates ARP against the DHCP snooping binding table, defeating ARP poisoning. It depends on DHCP snooping being enabled.
- **IP Source Guard** - filters traffic whose source IP does not match the binding table, defeating IP spoofing.
- **BPDU Guard and Root Guard** - protect the spanning tree from rogue switches.
- **Storm control** - rate-limits broadcast, multicast, and unknown unicast.
- **Private VLANs** - promiscuous, isolated, and community ports restricting communication within a VLAN.
- **VLAN hopping mitigation** - disable DTP on access ports, change the native VLAN, and do not use VLAN 1.

DAI requires DHCP snooping. Questions that enable DAI alone and expect protection are
testing that dependency.

## Wireless security

- **WPA2** - AES-CCMP.
- **WPA3** - SAE replaces the PSK four-way handshake, protecting against offline dictionary attacks; also adds protected management frames.
- **802.1X** - port-based access control with a supplicant, authenticator, and authentication server.
- **EAP methods** - EAP-TLS (certificates both sides, strongest), PEAP and EAP-TTLS (server certificate with tunnelled credentials), EAP-FAST (Cisco, PAC-based).
- **MAB (MAC Authentication Bypass)** - authenticates by MAC address for devices without a supplicant, such as printers. Weak, because MAC addresses are trivially spoofed.
- **Web authentication** - captive portal for guests.

## Network security features

- **ACLs** - standard (source only, numbered 1-99 and 1300-1999) and extended (source, destination, protocol, port, numbered 100-199 and 2000-2699), plus named ACLs. There is an implicit `deny any` at the end of every ACL.
- **ACL placement** - standard ACLs close to the destination (they match on source only, so placing them near the source would block too much); extended ACLs close to the source, to drop unwanted traffic early.
- **Time-based ACLs** - active during defined periods.
- **uRPF (Unicast Reverse Path Forwarding)** - drops packets whose source address is not reachable via the receiving interface, mitigating spoofing. Strict and loose modes.
- **Zone-Based Firewall (ZBF)** - policy between security zones on IOS routers.
- **Cisco TrustSec** - SGT-based policy, decoupling policy from IP addressing.
- **MACsec (802.1AE)** - hop-by-hop Layer 2 encryption.

Standard ACL near the destination, extended ACL near the source. This placement rule is
reliably examined.

## Endpoint and infrastructure protection

- **Cisco ISE (Identity Services Engine)** - centralised policy for 802.1X, profiling, posture assessment, and guest access. Issues SGTs for TrustSec.
- **Cisco Umbrella** - DNS-layer security.
- **Cisco Stealthwatch / Secure Network Analytics** - flow-based anomaly detection using NetFlow.
- **Cisco AMP / Secure Endpoint** - endpoint malware protection.
- **Next-generation firewall (Firepower / Secure Firewall)** - application-aware inspection with IPS.

## Secure management

- **SSH over Telnet** - always. Requires a hostname, domain name, and RSA key of adequate length.
- **SNMPv3** - authPriv for authentication and encryption.
- **NTP authentication** - prevents time spoofing, which matters for certificates and log correlation.
- **Secure copy (SCP)** and **HTTPS** for file transfer and web management.
- **Management plane separation** - a dedicated management VRF or out-of-band network.

## Exam pointers

- TACACS+ encrypts the whole payload and supports per-command authorisation; RADIUS does not.
- Always configure a local fallback when enabling AAA.
- Dynamic ARP Inspection depends on DHCP snooping.
- Port security default violation action is shutdown (err-disable).
- Standard ACLs go near the destination; extended ACLs near the source.
- Every ACL ends with an implicit deny.
- CoPP protects the CPU from control-plane floods.

## Official documentation

**[📖 ENCOR 350-401 exam topics](https://learningnetwork.cisco.com/s/encor-exam-topics)** - authoritative blueprint
**[📖 Cisco IOS security configuration guide](https://www.cisco.com/c/en/us/support/ios-nx-os-software/ios-xe-17/series.html)** - AAA, ACLs, CoPP
**[📖 Catalyst Layer 2 security features](https://www.cisco.com/c/en/us/support/switches/catalyst-9000/series.html)** - DHCP snooping, DAI, port security
