---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 5 min
---

# ISC2 Certified in Cybersecurity (CC)

The genuine entry point to security certification: **no prerequisites, no work experience required, and both the training and the exam are free** through the ISC2 One Million Certified in Cybersecurity initiative.

This repo is called "zero to hero". Until now its security path started at [Security+](../../comptia/security-plus/), which assumes some background and costs money. CC is the actual zero.

## Exam Details

- **Exam Code:** CC
- **Duration:** 120 minutes
- **Questions:** 100, multiple choice, linear
- **Passing Score:** 700/1000
- **Cost:** Free exam and training through the ISC2 initiative; an Annual Maintenance Fee applies after certification
- **Validity:** 3 years, maintained with CPE credits and the AMF
- **Prerequisites:** None

Full detail in the [fact sheet](./fact-sheet.md).

## Domains

| Domain | Weight | Notes |
|--------|-------:|-------|
| Security Principles | 26% | [01](./notes/01-security-principles.md) |
| Network Security | 24% | [02](./notes/02-network-security.md) |
| Access Control Concepts | 22% | [03](./notes/03-access-control.md) |
| Security Operations | 18% | [04](./notes/04-security-operations.md) |
| Business Continuity, Disaster Recovery, and Incident Response | 10% | [05](./notes/05-bcdr-and-incident-response.md) |

## What to expect

CC tests **vocabulary and concepts**, not implementation. You are not asked to configure a firewall; you are asked what a firewall does, where it sits, and which control type it is.

That makes it very learnable in a few weeks, and it makes precision matter. The exam distinguishes carefully between terms that sound similar:

- Threat, vulnerability, and risk
- Authentication, authorization, and accounting
- Preventive, detective, corrective, deterrent, and compensating controls
- Technical, administrative, and physical controls
- Business continuity, disaster recovery, and incident response
- RTO and RPO
- Symmetric encryption, asymmetric encryption, and hashing

If you can define each of those cleanly and give an example, you are most of the way there.

## Study sequence

1. **Security principles** - the vocabulary everything else uses. 26% of the exam.
2. **Network security** - the hardest domain for beginners, and 24%. Start early.
3. **Access control** - conceptually straightforward once principles are solid.
4. **Security operations** - data handling, encryption basics, logging, policies.
5. **BC, DR, and IR** - smallest domain, and mostly about knowing which is which.

Schedule in the [practice plan](./practice-plan.md).

## If the networking vocabulary is new

Domain 3 assumes you know what an IP address, a port, and a protocol are. If that is unfamiliar, work through the repo's beginner material first; it will save you time overall:

- [What is a server?](../../../learn/day-one/what-is-a-server.md)
- [HTTP and APIs](../../../learn/day-one/http-and-apis.md)
- [Networking troubleshooting](../../../learn/day-one/networking-troubleshooting.md)
- [DNS explained](../../../learn/concepts/dns-explained.md)
- [TLS and HTTPS](../../../learn/concepts/tls-and-https.md)

## Study resources

- **[📖 ISC2 CC certification page](https://www.isc2.org/certifications/cc)** - registration and the free training offer
- **[📖 ISC2 CC exam outline](https://www.isc2.org/certifications/cc/cc-certification-exam-outline)** - the authoritative domain list; study against this
- **[📖 ISC2 free online self-paced training](https://www.isc2.org/landing/1mcc)** - the official course, free
- [Practice questions](../../../resources/practice-questions/isc2-cc.md) - question bank in this repo

## After CC

| Next | Why |
|---|---|
| [Security+](../../comptia/security-plus/) | Broader and more technical; the common hiring baseline |
| [SC-900](../../azure/sc-900/) or [AZ-900](../../azure/az-900/) | If your direction is cloud |
| [CCSK](../../cloud-security-alliance/ccsk/) | Cloud security specifically |
| [CCSP](../ccsp/) or [CISSP](../cissp/) | Later, once you have the experience requirement |

See the [Security Engineer roadmap](../../../resources/certification-roadmap-security-engineer.md) for the full path.
