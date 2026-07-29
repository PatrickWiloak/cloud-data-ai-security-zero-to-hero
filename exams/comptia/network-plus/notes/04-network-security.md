---
last-updated: 2026-07-29
---

# Network+ Domain 4 - Network Security (14%)

The smallest domain by weight. It is security through a networking lens: attacks that
exploit network protocols, and the switch and router features that stop them.

## Core principles

- **Confidentiality** - only authorized parties can read the data.
- **Integrity** - data has not been altered.
- **Availability** - the service is reachable when needed.
- **Least privilege** - grant the minimum access needed to do the job.
- **Defense in depth** - layered controls so one failure is not fatal.
- **Zero trust** - no implicit trust from network location; verify every request.
- **Separation of duties** - split sensitive tasks so no single person can act unchecked.

## Common attacks

**Layer 2**

- **ARP poisoning / ARP spoofing** - forged ARP replies map the attacker's MAC to another host's IP, putting the attacker in the path. Mitigated by dynamic ARP inspection.
- **MAC flooding** - overwhelming a switch's MAC table so it floods frames to all ports, letting the attacker sniff. Mitigated by port security.
- **VLAN hopping** - reaching a VLAN you should not, by double tagging or by negotiating a trunk. Mitigated by disabling auto-trunking and changing the native VLAN.
- **Rogue DHCP server** - hands out bad gateway or DNS settings. Mitigated by DHCP snooping.
- **Spanning tree manipulation** - injecting BPDUs to become root and redirect traffic. Mitigated by BPDU guard and root guard.

**Layer 3 and above**

- **On-path attack (formerly man-in-the-middle)** - the attacker relays and possibly alters traffic between two parties.
- **DNS poisoning** - corrupting resolver cache so a name resolves to an attacker address. Mitigated by DNSSEC.
- **DoS and DDoS** - exhausting resources so legitimate users cannot be served. DDoS uses many sources.
- **Amplification attack** - small requests to a third party produce large responses aimed at the victim, commonly abusing DNS or NTP.
- **Session hijacking** - stealing a valid session token to impersonate a user.
- **Denial via resource exhaustion** - SYN floods leaving half-open connections.

**Wireless**

- **Evil twin** - a rogue access point advertising a legitimate SSID to harvest credentials or intercept traffic.
- **Rogue access point** - any unauthorized AP attached to the network, often installed by an employee for convenience.
- **Deauthentication attack** - forged management frames disconnect clients, often to force a reconnection the attacker can capture. 802.11w management frame protection mitigates it.

**Human**

- **Phishing, spear phishing, whaling** - fraudulent messages, targeted at anyone, at a specific person, or at an executive.
- **Tailgating and piggybacking** - following an authorized person through a controlled door, without and with their awareness respectively.
- **Shoulder surfing** - observing credentials being entered.
- **Social engineering** - manipulating people rather than technology. Training is the control.

## Security devices and protocols

- **Firewall** - filters by rule. Stateless firewalls inspect each packet alone; stateful firewalls track connection state.
- **Next-generation firewall (NGFW)** - adds application awareness, user identity, and integrated IPS.
- **IDS versus IPS** - an IDS observes a copy and alerts; an IPS sits inline and can drop. An IPS can cause an outage if it false-positives, which is the usual trade-off in exam scenarios.
- **Network access control (NAC)** - checks device posture and identity before granting network access. 802.1X is the common enforcement mechanism.
- **VPN concentrator** - terminates many VPN tunnels.
- **Proxy** - mediates requests, allowing inspection, filtering, and caching.
- **Jump box** - a hardened host through which administrative access flows.

**Encryption and tunnelling**

- **IPsec** - encrypts at Layer 3. AH provides authentication and integrity only; ESP provides confidentiality as well, which is why ESP is used in practice. Transport mode protects the payload; tunnel mode protects the whole original packet and is used for site-to-site VPNs.
- **TLS** - encrypts at the transport layer, protecting HTTPS and much else. See [TLS and HTTPS](../../../../learn/concepts/tls-and-https.md).
- **SSH** - encrypted remote administration, and a tunnel for other protocols.
- **IKE** - negotiates the IPsec security association, in two phases.

## Authentication, authorization, and accounting

- **AAA** - authentication proves identity, authorization decides permissions, accounting records what was done.
- **RADIUS** - AAA protocol, UDP, encrypts only the password. Widely used for network access including 802.1X.
- **TACACS+** - Cisco-oriented, TCP, encrypts the entire payload, separates authentication from authorization. Preferred for device administration.
- **Kerberos** - ticket-based authentication using a Key Distribution Center. Time-sensitive: clock skew beyond about five minutes breaks it.
- **LDAP** - directory access protocol. LDAPS is the TLS-protected form.
- **SAML** - XML-based federation for web single sign-on.
- **Multifactor authentication** - combining something you know, have, and are.

RADIUS versus TACACS+ is a favorite comparison: RADIUS for network access, TACACS+ for
device administration, and only TACACS+ encrypts the whole payload.

## Hardening

- **Port security** - limit MAC addresses per port and define the violation action.
- **DHCP snooping** - trust only designated ports to serve DHCP.
- **Dynamic ARP inspection** - validate ARP against the DHCP snooping binding table.
- **BPDU guard and root guard** - protect the spanning tree.
- **Disable unused ports and services** - reduce the attack surface.
- **Change default credentials** - the single most exploited weakness in network gear.
- **Firmware patching** - close known vulnerabilities.
- **Private VLANs** - restrict communication between hosts within the same VLAN.
- **Access control lists (ACLs)** - permit or deny traffic by address, protocol, and port.

## Physical security

- **Badge readers and access control vestibules (mantraps)** - prevent tailgating by admitting one person at a time.
- **Locking racks and cabinets** - physical access to a switch is administrative access to a switch.
- **Cameras and asset tags** - detective controls.
- **Environmental controls and fire suppression** - protect availability.

## Exam pointers

- Match the attack to its specific mitigation. DHCP snooping stops rogue DHCP, dynamic ARP inspection stops ARP poisoning, BPDU guard stops STP manipulation, port security stops MAC flooding.
- An IDS never blocks. If the question requires stopping traffic, the answer is an IPS or a firewall.
- Kerberos problems that appear after a server rebuild are usually clock skew.
- "Users connected to a network that looked legitimate but was not" is an evil twin.
- Anything about checking device health before granting access is NAC.

## Official documentation

**[📖 CompTIA Network+ N10-009 objectives](https://www.comptia.org/certifications/network#examdetails)** - authoritative domain list
**[📖 NIST SP 800-41](https://csrc.nist.gov/publications/detail/sp/800-41/rev-1/final)** - guidelines on firewalls and firewall policy
**[📖 RFC 4301](https://datatracker.ietf.org/doc/html/rfc4301)** - IPsec architecture
