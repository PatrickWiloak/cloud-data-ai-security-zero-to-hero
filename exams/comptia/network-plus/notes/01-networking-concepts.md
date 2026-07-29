---
last-updated: 2026-07-29
---

# Network+ Domain 1 - Networking Concepts (23%)

The vocabulary domain. Nearly everything later in the exam assumes the OSI model, ports,
and subnetting are automatic for you.

## The OSI model

| Layer | Name | PDU | Lives here |
|---|---|---|---|
| 7 | Application | Data | HTTP, DNS, SMTP, FTP |
| 6 | Presentation | Data | Encryption, encoding, compression |
| 5 | Session | Data | Session establishment and teardown |
| 4 | Transport | Segment (TCP) / Datagram (UDP) | TCP, UDP, port numbers |
| 3 | Network | Packet | IP, ICMP, routers |
| 2 | Data Link | Frame | MAC addresses, switches, VLANs |
| 1 | Physical | Bits | Cables, connectors, signalling |

- **Encapsulation** - each layer wraps the layer above with its own header as data moves down the stack.
- **Decapsulation** - each header is stripped in turn as data moves up the stack on the receiving host.
- **Maximum transmission unit (MTU)** - the largest frame payload a link will carry, 1500 bytes on standard Ethernet.
- **Jumbo frame** - an Ethernet frame with an MTU around 9000 bytes, used in storage and data-centre networks to cut per-packet overhead.

Troubleshooting shortcut: a device that makes decisions using MAC addresses is Layer 2, and
one using IP addresses is Layer 3. That single distinction answers many questions.

## Ports and protocols

Learn these cold. They appear throughout the exam.

| Port | Protocol | Notes |
|---|---|---|
| 20/21 | FTP | 20 data, 21 control |
| 22 | SSH / SFTP / SCP | Encrypted remote access and transfer |
| 23 | Telnet | Unencrypted, should not be used |
| 25 | SMTP | Mail transfer |
| 53 | DNS | UDP for queries, TCP for zone transfers and large responses |
| 67/68 | DHCP | Server 67, client 68 |
| 69 | TFTP | Trivial FTP, UDP, no authentication |
| 80 | HTTP | Unencrypted web |
| 110 | POP3 | Mail retrieval, downloads and typically deletes |
| 123 | NTP | Time synchronisation |
| 143 | IMAP | Mail retrieval, keeps mail on server |
| 161/162 | SNMP | 161 queries, 162 traps |
| 389 | LDAP | Directory services |
| 443 | HTTPS | TLS-encrypted web |
| 445 | SMB | Windows file sharing |
| 636 | LDAPS | LDAP over TLS |
| 3389 | RDP | Remote Desktop |

- **TCP (Transmission Control Protocol)** - connection-oriented, reliable, ordered. Uses a three-way handshake: SYN, SYN-ACK, ACK.
- **UDP (User Datagram Protocol)** - connectionless, no delivery guarantee, lower overhead. Preferred for voice, video, and DNS queries.
- **ICMP (Internet Control Message Protocol)** - error and diagnostic messaging. Carries ping and traceroute, and has no ports.

## IP addressing

- **IPv4 address** - 32 bits, written as four dotted octets.
- **IPv6 address** - 128 bits, written as eight hextets in hexadecimal, with `::` compressing one run of consecutive zero groups.
- **Subnet mask** - marks which bits are network and which are host.
- **CIDR notation** - the count of network bits, for example /24.
- **Default gateway** - the router a host sends traffic to when the destination is outside its own subnet.

**Private ranges (RFC 1918)** - not routable on the internet:

- 10.0.0.0/8
- 172.16.0.0/12
- 192.168.0.0/16

Also know **169.254.0.0/16** (APIPA, self-assigned when DHCP fails - a very common exam
symptom) and **127.0.0.0/8** (loopback).

- **NAT (Network Address Translation)** - rewrites addresses so private hosts can reach the internet through a public address.
- **PAT (Port Address Translation)** - many private hosts share one public address, distinguished by port. This is what most home routers do.

**IPv6 specifics**

- **Global unicast** - publicly routable, typically 2000::/3.
- **Link-local** - fe80::/10, automatically configured, valid only on the local link.
- **SLAAC (Stateless Address Autoconfiguration)** - a host builds its own address from the router advertisement.
- **Dual stack** - running IPv4 and IPv6 simultaneously. IPv6 has no broadcast; it uses multicast and anycast instead.

## Subnetting

The most practised skill in the exam. Memorise the mask table:

| CIDR | Mask | Usable hosts | Block size |
|---|---|---|---|
| /24 | 255.255.255.0 | 254 | 256 |
| /25 | 255.255.255.128 | 126 | 128 |
| /26 | 255.255.255.192 | 62 | 64 |
| /27 | 255.255.255.224 | 30 | 32 |
| /28 | 255.255.255.240 | 14 | 16 |
| /29 | 255.255.255.248 | 6 | 8 |
| /30 | 255.255.255.252 | 2 | 4 |

Usable hosts is 2^h - 2, subtracting the network and broadcast addresses. A /30 gives two
usable addresses, which is why it suits point-to-point links.

- **VLSM (Variable Length Subnet Masking)** - using different mask lengths within one network so subnet sizes fit actual need.
- **Supernetting / route summarisation** - combining contiguous networks into one advertisement to shrink routing tables.

## Topologies and network types

- **Star** - every node connects to a central device. Dominant in modern LANs.
- **Mesh** - nodes interconnect directly; full mesh gives maximum redundancy at high cost.
- **Hybrid** - a mixture, which is what real networks are.
- **Point-to-point** - two endpoints, typically a WAN link.
- **LAN, WAN, MAN, PAN, CAN, SAN, WLAN** - scope descriptors from a single room to a metropolitan area. A SAN is a storage-specific network.

## Cloud concepts

- **IaaS** - you manage the OS upward.
- **PaaS** - you manage the application and data.
- **SaaS** - you manage configuration and data only.

See [IaaS, PaaS, SaaS explained](../../../../learn/concepts/iaas-paas-saas.md) and the
[shared responsibility model](../../../../learn/concepts/shared-responsibility-model.md).

- **Public, private, hybrid, and community cloud** - deployment models distinguished by who owns the infrastructure and who may use it.
- **VPC (Virtual Private Cloud)** - a logically isolated network inside a provider's cloud.
- **Direct Connect / ExpressRoute** - dedicated private circuits between on-premises and the cloud, bypassing the internet.
- **NFV (Network Function Virtualisation)** - running firewalls, load balancers, and routers as software instances.

## Network services

- **DHCP** - automatic IP configuration. The DORA sequence is Discover, Offer, Request, Acknowledge.
- **DHCP relay / IP helper** - forwards DHCP broadcasts across a router to a server on another subnet.
- **DNS** - resolves names to addresses. Record types: A (IPv4), AAAA (IPv6), CNAME (alias), MX (mail), TXT (arbitrary text, used for SPF), PTR (reverse), NS (name server), SOA (zone authority).
- **NTP** - synchronises clocks. Stratum numbers indicate distance from the reference clock.
- **SNMP** - device monitoring. v3 adds authentication and encryption; v1 and v2c send community strings in clear text.

See [DNS explained](../../../../learn/concepts/dns-explained.md) for the resolution walk-through.

## Network devices

- **Hub** - Layer 1, repeats to all ports, one collision domain. Obsolete.
- **Switch** - Layer 2, forwards by MAC address, each port its own collision domain.
- **Router** - Layer 3, forwards between networks by IP, separates broadcast domains.
- **Firewall** - filters traffic by rule. Stateful firewalls track connection state.
- **Load balancer** - distributes traffic across servers. See [load balancing deep dive](../../../../resources/networking-deep-dives/load-balancing-deep-dive.md).
- **Proxy** - forward proxies act for clients, reverse proxies act for servers.
- **IDS / IPS** - an IDS detects and alerts; an IPS sits inline and blocks.
- **Wireless controller** - centrally manages access points.
- **Content delivery network (CDN)** - geographically distributed caching. See [CDN explained](../../../../learn/concepts/cdn-explained.md).

## Exam pointers

- A host with a 169.254.x.x address did not reach a DHCP server. This is one of the most common scenario answers on the exam.
- Duplicate IP addresses cause intermittent connectivity for both hosts.
- If a question distinguishes collision domains from broadcast domains: switches split collision domains, routers split broadcast domains.
- Practise subnetting until block size arithmetic is instant. It is the highest-yield preparation you can do.

## Official documentation

**[📖 CompTIA Network+ N10-009 objectives](https://www.comptia.org/certifications/network#examdetails)** - authoritative domain list
**[📖 RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918)** - private address allocation
**[📖 IANA port number registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)** - authoritative port assignments
