---
last-updated: 2026-07-29
---

# CySA+ Domain 1 - Security Operations (33%)

The largest domain. It assumes you can read logs and network data and say what is
happening, then place that activity inside a recognised attack framework.

## System and network architecture as a security concern

Architecture decides what an attacker can reach and what you can see.

- **Attack surface** - every point where an untrusted party can submit input or reach a service. Reducing it is cheaper than defending it.
- **Network segmentation** - dividing a network so a compromise in one segment does not grant access to another. The single most effective containment control.
- **Zero trust** - never trust based on network location alone; authenticate and authorise every request. See [zero trust architecture](../../../../resources/architecture-patterns/zero-trust-architecture.md).
- **Defence in depth** - layered controls so no single failure is fatal.
- **Asset inventory** - the list of what you own. You cannot protect or prioritise what you do not know exists, which is why inventory underpins vulnerability management too.

**Identity and access concepts that show up as log evidence**

- **Federation** - one identity provider vouches for a user across multiple services. Compromise of the IdP is compromise of everything downstream.
- **Single sign-on (SSO)** - one authentication event grants access to many systems.
- **Privileged access management (PAM)** - controlled checkout, monitoring, and rotation of admin credentials.
- **Multifactor authentication (MFA)** - two or more of something you know, have, or are. MFA-fatigue push spam is a tested attack.

**Logging considerations**

- **Log aggregation** - centralising logs so an attacker who wipes a host cannot erase the evidence.
- **Time synchronisation** - NTP across all sources. Without it, correlating events across systems is guesswork.
- **Log retention** - how long you keep data. Incidents are frequently discovered months after initial compromise, so short retention destroys the investigation.

## Analysing indicators of potentially malicious activity

Know which indicator points at which category of problem.

**Network-related**

- **Bandwidth consumption** - unexpected volume, especially outbound, suggests exfiltration.
- **Beaconing** - regular, periodic callbacks to an external host. A hallmark of command and control.
- **Irregular peer-to-peer communication** - internal hosts talking directly to each other in patterns they normally do not, suggesting lateral movement.
- **Rogue devices** - unknown hardware on the network.
- **Scans and sweeps** - one host touching many addresses or many ports; reconnaissance.
- **Common protocol over non-standard port** - HTTP on 8443, SSH on 443. Usually evasion.

**Host-related**

- **Processor consumption** - sustained spikes may indicate cryptomining.
- **Memory consumption and unauthorised processes** - unfamiliar binaries, or familiar names in wrong locations.
- **Data exfiltration** - large archives staged before transfer, often compressed and encrypted.
- **Abnormal OS process behaviour** - a process spawning an unexpected child, for example a document application launching a shell. Very high signal.
- **File system changes** - new executables in temp directories, modified system binaries.
- **Registry changes and unauthorised scheduled tasks** - classic persistence.

**Application-related**

- **Anomalous activity and introduction of new accounts** - especially privileged ones created outside change control.
- **Unexpected output or outages** - can indicate injection or tampering.
- **Service interruption** - may be the attack, or the cover for it.

## Tools and techniques for determining malicious activity

| Category | Tools | Use it for |
|---|---|---|
| Packet capture | Wireshark, tcpdump | Full payload inspection, protocol analysis |
| Log analysis | SIEM, syslog | Correlation across many sources |
| Endpoint | EDR | Process trees, parent-child relationships |
| File analysis | Strings, hashing (SHA-256), VirusTotal | Triage of a suspicious binary |
| Sandboxing | Detonation environments | Observing behaviour without risking production |
| Email | Header analysis, DKIM/SPF/DMARC checks | Phishing and spoofing investigations |

- **SIEM (Security Information and Event Management)** - collects, correlates, and alerts on log data from many sources.
- **SOAR (Security Orchestration, Automation, and Response)** - automates repeatable response actions, reducing analyst toil.
- **EDR (Endpoint Detection and Response)** - agent-based telemetry and response on hosts.
- **Sandboxing** - executing suspect code in an isolated environment to observe behaviour.
- **DKIM, SPF, and DMARC** - email authentication mechanisms. SPF authorises sending IPs, DKIM signs the message, DMARC ties them together and states a policy.

## Attack methodology frameworks

You need to be able to place an observation into a stage.

- **MITRE ATT&CK** - a matrix of adversary tactics (the why) and techniques (the how), based on real-world observation. The most commonly referenced framework, and the one to know in most detail.
- **Cyber Kill Chain** - Lockheed Martin's linear model: reconnaissance, weaponisation, delivery, exploitation, installation, command and control, actions on objectives.
- **Diamond Model of Intrusion Analysis** - relates adversary, capability, infrastructure, and victim. Useful for attribution reasoning.
- **OWASP Top 10** - the most common web application security risks.

Exam framing: ATT&CK describes *what an adversary does*, the Kill Chain describes *the
sequence*, and the Diamond Model describes *the relationships between the parties*.

## Threat intelligence and threat hunting

- **Threat intelligence** - evidence-based knowledge about existing or emerging threats, used to inform decisions.
- **Indicator of compromise (IoC)** - an artefact observed that suggests an intrusion: a hash, an IP, a domain, a registry key.
- **Tactics, techniques, and procedures (TTPs)** - the behavioural patterns of an adversary. Harder for an attacker to change than an IoC, so more durable for detection.
- **Threat hunting** - proactively searching for threats that existing detection has missed, starting from a hypothesis rather than an alert.
- **Confidence levels** - intelligence is graded on source reliability and information credibility. Acting on low-confidence intelligence generates false positives.
- **Open-source intelligence (OSINT)** - intelligence gathered from publicly available sources.
- **Information sharing and analysis centres (ISACs)** - sector-specific bodies for sharing threat data.

**The pyramid of pain** ranks indicators by how much it costs an attacker when you block
them: hash values are trivial to change, TTPs are expensive. Detection built on TTPs
survives; detection built on hashes does not.

## Efficiency and process improvement

- **Standardisation of processes** - documented, repeatable procedures so outcomes do not depend on which analyst is on shift.
- **Streamlining operations** - automating repetitive tasks, typically enrichment and triage, so analysts spend time on judgement.
- **Technology and tool integration** - APIs and webhooks connecting SIEM, ticketing, and EDR so context follows the case.
- **Single pane of glass** - one console presenting data from many tools. Reduces context switching and missed signals.

## Exam pointers

- Questions often give log output and ask what it indicates. Read for the *anomaly*, not the volume: one unexpected parent-child process relationship outweighs a thousand routine denials.
- "Beaconing" almost always means command and control.
- If asked what best survives an attacker's changes, the answer relates to TTPs or behaviour, not to a specific IoC.
- Segmentation is the usual right answer for limiting blast radius; MFA for credential attacks; EDR for host-level visibility.

## Official documentation

**[📖 CompTIA CySA+ exam objectives](https://www.comptia.org/certifications/cybersecurity-analyst#examdetails)** - authoritative domain list
**[📖 MITRE ATT&CK](https://attack.mitre.org/)** - the tactics and techniques matrix
**[📖 NIST SP 800-150](https://csrc.nist.gov/publications/detail/sp/800-150/final)** - guide to cyber threat information sharing
