---
last-updated: 2026-07-29
---

# PCNSA Domain 1 - Palo Alto Networks Portfolio and Architecture

What the platform is, how the firewall processes a packet, and the identification
technologies that distinguish a next-generation firewall from a port-based one.

## The portfolio

- **Strata** - the network security product line: PAN-OS next-generation firewalls, Panorama, and associated subscriptions. This is what PCNSA covers.
- **Prisma** - cloud security: Prisma Access (SASE), Prisma Cloud (CNAPP), Prisma SD-WAN.
- **Cortex** - security operations: Cortex XDR, XSOAR for orchestration, Xpanse for attack surface management.
- **Unit 42** - the threat intelligence and incident response arm.

PCNSA is a Strata exam. Prisma and Cortex appear only as context.

## Firewall form factors

- **PA-Series** - physical hardware appliances, from branch to data centre.
- **VM-Series** - virtual firewalls for private and public cloud.
- **CN-Series** - containerised firewall for Kubernetes environments.
- **Cloud NGFW** - managed firewall service in public cloud.

## Single-pass parallel processing

The architectural claim that underpins the product.

- **Single-Pass Architecture (SP3)** - the packet is parsed once, and all inspection (App-ID, Content-ID, User-ID, policy) happens against that single parse rather than in a chain of separate engines.
- **Parallel processing** - dedicated hardware planes handle networking, security, and management concurrently.
- **Control plane** - management, logging, and routing protocol processes.
- **Data plane** - packet forwarding and inspection. Separating them means heavy management activity does not degrade throughput.

The exam framing: single-pass means enabling more inspection features does not multiply
latency the way chained engines would.

## Packet flow

Knowing the order matters, because it explains why a rule that looks correct does not
match.

1. **Ingress** - packet arrives, interface and zone determined.
2. **Session lookup** - if it matches an existing session, fast path applies.
3. **For a new session**: forwarding lookup determines the egress interface and therefore the destination zone.
4. **NAT policy evaluation** - the *destination* NAT decision is made here, before security policy.
5. **Security policy evaluation** - matched against pre-NAT addresses but post-NAT zones.
6. **Content inspection** - security profiles applied to allowed traffic.
7. **Egress** - source NAT applied, packet forwarded.

The single most tested consequence: **security policy uses the original (pre-NAT) IP
addresses but the post-NAT zones.** Rules written with post-NAT addresses do not match.

## The identification technologies

- **App-ID** - identifies the application regardless of port, protocol, or encryption evasion. The core differentiator. A rule permitting `web-browsing` permits that application wherever it runs, and a rule permitting port 80 alone permits anything on that port.
- **User-ID** - maps IP addresses to usernames and groups, so policy can be written in terms of people rather than addresses.
- **Content-ID** - the inspection stream: threat prevention, URL filtering, file blocking, and data filtering.
- **Device-ID** - identifies device types, useful for IoT policy.

**How App-ID works** - the firewall applies signatures, decoders, and heuristics to
identify traffic. Until identification completes, traffic is provisionally handled, and
the application may shift as more of the flow is seen. This is why `application-default`
and dependency handling matter.

**How User-ID works** - agents or agentless collection read domain controller security
logs, plus options including captive portal, syslog parsing, XML API, and terminal server
agents for multi-user hosts.

## Security zones and interfaces

- **Zone** - a logical grouping of interfaces with the same security treatment. All policy is written zone to zone.
- **Intrazone traffic** - within one zone. Allowed by default.
- **Interzone traffic** - between zones. Denied by default.
- **Layer 3 interface** - has an IP address and routes.
- **Layer 2 interface** - switches within a VLAN.
- **Virtual Wire (vwire)** - two interfaces bonded transparently, requiring no IP or routing changes. The usual answer for inserting a firewall into an existing network without redesign.
- **Tap interface** - passive monitoring of a mirrored port; can see and log but not block.
- **Loopback and tunnel interfaces** - for management, VPN, and routing purposes.

An interface must be assigned to a zone before it can pass traffic through policy.

## Management

- **Web interface, CLI, and XML/REST API** - the management paths.
- **Panorama** - centralised management for many firewalls: shared policy via device groups, and shared configuration via templates.
- **Device group** - policy and objects pushed to a set of firewalls.
- **Template and template stack** - network and device configuration pushed to firewalls.
- **Candidate configuration** - your edits, not yet active.
- **Running configuration** - what the firewall is actually enforcing.
- **Commit** - moves candidate to running. Nothing you change takes effect until commit, which is a favourite exam point.

With Panorama, pre-rules and post-rules sandwich locally defined rules, and local
administrators cannot edit the pushed rules.

## Licences and subscriptions

- **Threat Prevention** - IPS, anti-malware, anti-spyware.
- **Advanced URL Filtering** - web categorisation and credential-theft prevention.
- **WildFire** - cloud sandboxing for unknown files, returning verdicts and new signatures.
- **DNS Security** - blocks malicious domains and DNS tunnelling.
- **GlobalProtect** - remote access VPN, licensed for advanced features.
- **SD-WAN and IoT Security** - additional subscriptions.

The base firewall does App-ID and policy without subscriptions. Threat signatures, URL
categories, and sandboxing all require active licences, and expired licences silently
degrade protection.

## Exam pointers

- Security policy matches pre-NAT addresses and post-NAT zones. Expect this to be tested more than once.
- Intrazone traffic is allowed by default; interzone is denied by default.
- Virtual Wire is the deployment mode that requires no IP or routing change.
- Nothing takes effect until you commit.
- A tap interface cannot block, only observe.

## Official documentation

**[📖 PCNSA exam blueprint](https://www.paloaltonetworks.com/services/education/certification)** - authoritative objectives
**[📖 PAN-OS Administrator's Guide](https://docs.paloaltonetworks.com/pan-os)** - the primary reference
**[📖 Packet flow sequence in PAN-OS](https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClVWCA0)** - the authoritative flow diagram
