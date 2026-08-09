---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 10 min
---

# ISC2 Certified in Cybersecurity (CC) Fact Sheet

## Exam Overview

**Exam Code:** CC
**Exam Name:** Certified in Cybersecurity
**Level:** Foundational (entry level)
**Duration:** 120 minutes
**Format:** Multiple choice, linear (not adaptive)
**Questions:** 100
**Passing Score:** 700 out of 1000
**Cost:** Free exam and free self-paced training through the ISC2 One Million Certified in Cybersecurity initiative; an Annual Maintenance Fee applies once certified
**Valid For:** 3 years, maintained with continuing professional education credits and the AMF
**Delivery:** Pearson VUE test center, or online proctored where available
**Prerequisites:** **None.** No work experience required

> **Verify before booking.** The free exam and training offer, AMF amount, and CPE requirements are set by ISC2 and change. Confirm on the official page below.

**[📖 ISC2 Certified in Cybersecurity](https://www.isc2.org/certifications/cc)** - exam outline, registration, and the free training offer
**[📖 ISC2 CC exam outline](https://www.isc2.org/certifications/cc/cc-certification-exam-outline)** - the authoritative domain breakdown
**[📖 ISC2 One Million Certified in Cybersecurity](https://www.isc2.org/landing/1mcc)** - the free training and exam program

## Why this exam is in this repo

This repository is called "zero to hero", and until now its security path started at [Security+](../../comptia/security-plus/), which assumes some background and costs several hundred dollars. CC is the genuine zero: **no prerequisites, free training, free exam**, and it is the entry rung of the ISC2 ladder that continues to [CCSP](../ccsp/) and [CISSP](../cissp/).

It is also the best first certification for someone testing whether security interests them at all, because the only cost is time.

## Target Audience

- Complete beginners to cybersecurity
- Career changers evaluating the field
- IT staff moving toward a security role
- Students, and anyone who wants an entry credential without a work-experience requirement
- Non-security staff who need credible security literacy: developers, project managers, auditors

## Exam Domains

### Domain 1: Security Principles (26%)

The largest domain.

**Key Concepts:**
- The CIA triad: confidentiality, integrity, availability
- Authentication, authorization, accounting, and non-repudiation
- Privacy and personally identifiable information
- Risk management: identification, assessment, treatment (avoid, mitigate, transfer, accept)
- Risk terminology: threat, vulnerability, likelihood, impact, asset, risk tolerance
- Security controls: technical, administrative (managerial), and physical
- Control functions: preventive, detective, corrective, deterrent, compensating
- Professional ethics, including the ISC2 Code of Ethics canons
- Governance elements: policies, standards, procedures, guidelines, and regulations

### Domain 2: Access Control Concepts (22%)

**Key Concepts:**
- Physical access controls: badges, mantraps, turnstiles, guards, CCTV, sensors
- Logical access controls
- The principle of least privilege and need to know
- Separation of duties and job rotation
- Authorization models: discretionary (DAC), mandatory (MAC), role-based (RBAC), attribute-based (ABAC)
- Rule-based access control
- Identity and access management lifecycle: provisioning, review, deprovisioning
- Privileged access management
- Defense in depth applied to access

### Domain 3: Network Security (24%)

The second largest domain, and the one most beginners find hardest.

**Key Concepts:**
- The OSI and TCP/IP models and what happens at each layer
- IP addressing, ports, and common protocols
- Network types: LAN, WAN, VLAN, VPN, and wireless
- Network devices: switch, router, firewall, proxy, load balancer
- Threats: DoS and DDoS, on-path (man-in-the-middle), spoofing, phishing, malware types, insider threat
- Intrusion detection and prevention systems
- Segmentation, DMZ, and network access control
- Zero trust concepts
- Secure protocols and encryption in transit
- Cloud service models (IaaS, PaaS, SaaS) and deployment models (public, private, hybrid, community)
- Shared responsibility in cloud
- Service level agreements and managed service providers

### Domain 4: Security Operations (18%)

**Key Concepts:**
- Data handling: classification, labeling, retention, and destruction
- Encryption basics: symmetric, asymmetric, hashing, and where each is used
- Logging and monitoring, and the role of a SIEM
- Configuration management: baselines, inventory, patching, and change management
- Security policies: acceptable use, bring your own device, privacy, change management, password policy
- Security awareness training, including phishing simulation and social engineering
- Physical and environmental controls

### Domain 5: Business Continuity, Disaster Recovery, and Incident Response (10%)

The smallest domain.

**Key Concepts:**
- Incident response: preparation, detection and analysis, containment, eradication, recovery, and lessons learned
- The incident response team and plan
- Business continuity: business impact analysis, critical functions, and the continuity plan
- Disaster recovery: RTO, RPO, backups, and recovery sites (hot, warm, cold)
- The relationship between the three: BC keeps the business running, DR restores technology, IR handles the event

## Where CC sits in the ISC2 ladder

| Certification | Experience required | Level |
|---|---|---|
| **CC** | None | Entry |
| **SSCP** | 1 year | Practitioner |
| **[CCSP](../ccsp/)** | 5 years, including cloud | Cloud specialist |
| **[CISSP](../cissp/)** | 5 years across 2 domains | Senior |

CC has no experience requirement, which is what makes it the true starting point. CISSP requires five years, so passing the exam earlier makes you an Associate of ISC2 until you accumulate it.

## Related repo material

- [Notes](./notes/) - five notes, one per domain
- [Practice plan](./practice-plan.md) - 4-week schedule
- [Scenarios](./scenarios.md)
- [Strategy](./strategy.md)
- [Security+](../../comptia/security-plus/) - the natural next step
- [CISSP](../cissp/) and [CCSP](../ccsp/) - the senior ISC2 certifications
- [Day One](../../../learn/day-one/) - if the terminal and networking vocabulary is new
- [Security topic](../../../topics/security.md)
