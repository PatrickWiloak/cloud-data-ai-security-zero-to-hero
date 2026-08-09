---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 11 min
---

# 02 - Network security

**Domain 3: Network Security (24%)** - the second largest domain, and usually the hardest for beginners.

---

## The OSI model

| Layer | Name | Handles | Examples |
|---:|---|---|---|
| 7 | Application | The application protocol itself | HTTP, SMTP, DNS, FTP |
| 6 | Presentation | Formatting, encoding, encryption | TLS, JPEG, ASCII |
| 5 | Session | Establishing and managing sessions | Session establishment and teardown |
| 4 | Transport | End-to-end delivery, ports | TCP, UDP |
| 3 | Network | Logical addressing and routing | IP, ICMP, routers |
| 2 | Data link | Local delivery, MAC addressing | Ethernet, switches |
| 1 | Physical | Bits on the medium | Cables, radio, hubs |

The **TCP/IP model** condenses this into four: Application (OSI 5-7), Transport (4), Internet (3), Network Access (1-2).

---

## Addressing and protocols

- **IPv4** is 32 bits, written as four octets; **IPv6** is 128 bits.
- **Private ranges** (RFC 1918): `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`. Not routable on the internet, which is why NAT exists.
- **MAC address**: the layer 2 hardware address.
- **Ports** identify the service on a host. Well-known ports run 0-1023.

| Port | Service |
|---:|---|
| 22 | SSH, SFTP |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 3389 | RDP |

**TCP** is connection-oriented and reliable, using a three-way handshake (SYN, SYN-ACK, ACK). **UDP** is connectionless and faster, with no delivery guarantee, used for DNS, streaming, and VoIP.

---

## Network types and devices

| Type | Meaning |
|---|---|
| **LAN** | Local area network, one site |
| **WAN** | Wide area network, connecting sites |
| **VLAN** | Logical segmentation of a physical network |
| **VPN** | Encrypted tunnel across an untrusted network |
| **WLAN** | Wireless LAN; secured with WPA2 or WPA3, not WEP |

| Device | Layer | Does |
|---|---|---|
| **Hub** | 1 | Repeats traffic to all ports (obsolete, insecure) |
| **Switch** | 2 | Forwards frames to the correct port by MAC address |
| **Router** | 3 | Forwards packets between networks by IP |
| **Firewall** | 3-4, or 7 for next-generation | Permits or denies traffic by rule |
| **Proxy** | 7 | Intermediates requests, can filter and cache |
| **Load balancer** | 4 or 7 | Distributes traffic across backends |
| **IDS** | - | **Detects** and alerts on suspicious traffic |
| **IPS** | - | **Detects and blocks** suspicious traffic inline |

The **IDS versus IPS** distinction is a reliable exam question: detection versus inline prevention.

---

## Threats

| Threat | What it is |
|---|---|
| **DoS / DDoS** | Overwhelming a service so it cannot serve legitimate users; DDoS uses many sources |
| **On-path (man-in-the-middle)** | Intercepting communication between two parties |
| **Spoofing** | Falsifying an identity: IP, MAC, email sender |
| **Phishing** | Fraudulent messages seeking credentials or action; **spear phishing** is targeted, **whaling** targets executives, **vishing** is voice, **smishing** is SMS |
| **Social engineering** | Manipulating people rather than technology; includes pretexting, tailgating, and baiting |
| **Malware** | Virus (attaches to a file), worm (self-propagating), trojan (disguised), ransomware (encrypts for payment), spyware, rootkit, logic bomb |
| **Insider threat** | Malicious or negligent action by someone with legitimate access |
| **Zero-day** | Exploiting a vulnerability with no available patch |

---

## Defensive architecture

- **Segmentation** divides the network so a compromise in one segment does not reach another
- **DMZ** (screened subnet) hosts internet-facing services between two firewalls, isolating them from the internal network
- **Network access control (NAC)** checks device posture before granting network access
- **Defense in depth**: multiple layers, so one failure is not enough
- **Zero trust**: never trust based on network location; verify explicitly, grant least privilege, assume breach
- **Secure protocols**: prefer HTTPS over HTTP, SSH over Telnet, SFTP over FTP, and use VPN for remote access

---

## Cloud

**Service models**, and who manages what:

| Model | You manage | Provider manages | Example |
|---|---|---|---|
| **IaaS** | OS, runtime, applications, data | Hardware, virtualization, network | Virtual machines |
| **PaaS** | Applications and data | Everything below | App hosting platforms |
| **SaaS** | Data and access configuration | Everything else | Email, CRM |

**Deployment models**: **public** (shared, provider-owned), **private** (single organization), **hybrid** (both, connected), **community** (shared by organizations with common concerns).

**Shared responsibility**: responsibility shifts toward the provider from IaaS to SaaS. Two constants: **physical security is always the provider's**, and **data and access configuration are always yours**.

**MSP** (managed service provider) operates services on your behalf. **SLA** (service level agreement) defines the committed level of service and the consequence of missing it.

---

## Key terms

- **OSI model** - the seven-layer conceptual model of network communication
- **TCP** - the connection-oriented transport protocol providing reliable, ordered delivery
- **UDP** - the connectionless transport protocol offering speed without delivery guarantees
- **Port** - the number identifying a particular service on a host
- **VLAN** - a logical segmentation of a physical network
- **VPN** - an encrypted tunnel carrying traffic across an untrusted network
- **Switch** - a layer 2 device forwarding frames by MAC address
- **Router** - a layer 3 device forwarding packets between networks by IP address
- **Firewall** - a device or software permitting or denying traffic according to rules
- **IDS** - an intrusion detection system that alerts on suspicious traffic without blocking it
- **IPS** - an intrusion prevention system that detects and blocks suspicious traffic inline
- **DMZ** - a screened subnet hosting internet-facing services, isolated from the internal network
- **Network access control** - technology validating device posture before granting network access
- **DDoS** - a distributed denial of service attack using many sources to exhaust a target
- **On-path attack** - interception of communication between two parties, formerly called man-in-the-middle
- **Phishing** - fraudulent messaging seeking credentials or action, with targeted variants such as spear phishing and whaling
- **Ransomware** - malware that encrypts data and demands payment for its recovery
- **Zero-day** - an exploit against a vulnerability for which no patch exists
- **Zero trust** - a model that verifies explicitly and grants least privilege rather than trusting network location
- **IaaS** - a cloud model providing infrastructure, with the customer managing the operating system upward
- **SaaS** - a cloud model providing complete applications, with the customer managing data and access only
- **Shared responsibility model** - the division of security duties between cloud provider and customer
- **SLA** - a service level agreement defining committed service levels and remedies

---

## Related

- [Notes 03: access control](./03-access-control.md)
- [Scenarios](../scenarios.md) - scenario 8
- [DNS explained](../../../../learn/concepts/dns-explained.md)
- [TLS and HTTPS](../../../../learn/concepts/tls-and-https.md)
