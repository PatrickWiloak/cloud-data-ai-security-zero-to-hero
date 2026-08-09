---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 10 min
---

# 01 - Security principles

**Domain 1: Security Principles (26%)** - the largest domain, and the vocabulary the rest of the exam uses.

---

## The CIA triad

| Property | Means | Broken by | Protected by |
|---|---|---|---|
| **Confidentiality** | Only authorized parties can read it | Data breach, eavesdropping, shoulder surfing | Encryption, access control, classification |
| **Integrity** | Data is accurate and unaltered | Tampering, corruption, unauthorized change | Hashing, digital signatures, change control |
| **Availability** | Authorized users can access it when needed | DoS attack, hardware failure, ransomware | Redundancy, backups, capacity planning |

Additional properties often listed alongside:
- **Authenticity** - the data or party is genuine
- **Non-repudiation** - the actor cannot credibly deny having acted, typically provided by digital signatures

---

## AAA

- **Authentication** - proving who you are. Factors: something you **know** (password), something you **have** (token, phone), something you **are** (biometric). Two or more different factors is **multi-factor authentication**; two passwords is not.
- **Authorization** - determining what you are permitted to do, after authentication succeeds
- **Accounting** (or auditing) - recording what you did

---

## Risk

| Term | Definition |
|---|---|
| **Asset** | Something of value: data, systems, people, reputation |
| **Vulnerability** | A weakness that could be exploited |
| **Threat** | A person, event, or circumstance with the potential to exploit a vulnerability |
| **Threat actor** | The entity behind a threat: criminal, insider, nation state, hacktivist |
| **Likelihood** | The probability that a threat exploits a vulnerability |
| **Impact** | The consequence if it happens |
| **Risk** | The combination of likelihood and impact |
| **Risk tolerance / appetite** | How much risk the organization is willing to accept |
| **Residual risk** | The risk remaining after controls are applied |

**Risk treatment**, four options:

| Treatment | Means | Example |
|---|---|---|
| **Avoid** | Stop doing the risky activity | Decommission the vulnerable service |
| **Mitigate** (reduce) | Apply controls to lower likelihood or impact | Patch it, add monitoring |
| **Transfer** (share) | Move the financial consequence to another party | Cyber insurance, outsourcing |
| **Accept** | Acknowledge and take no further action | Document, get sign-off, review periodically |

Risk **assessment** can be **qualitative** (high, medium, low) or **quantitative** (monetary values: single loss expectancy, annualized rate of occurrence, annualized loss expectancy).

---

## Controls

Two independent axes, and the exam tests both.

**Control type** (who or what implements it):
- **Technical** (logical) - implemented in technology: firewall, encryption, access control list
- **Administrative** (managerial) - implemented through process and people: policy, training, background check
- **Physical** - implemented in the physical world: lock, fence, guard, CCTV

**Control function** (what it does):
- **Preventive** - stops the event: lock, firewall, input validation
- **Detective** - identifies that it happened: IDS, CCTV recording, audit log review
- **Corrective** - fixes it afterwards: restore from backup, patch, incident response
- **Deterrent** - discourages the attempt: warning sign, visible camera, published penalties
- **Compensating** - an alternative when the primary control is not feasible: extra monitoring where segmentation is impossible

Any control has one of each. A CCTV camera is physical, and is both deterrent (visible) and detective (recording).

**Defense in depth** means layering controls so that failure of one does not expose the asset.

---

## Governance documents

| Document | Nature | Example |
|---|---|---|
| **Policy** | High level, mandatory, states intent | "All data must be classified" |
| **Standard** | Specific, mandatory, states requirements | "All laptops use AES-256 full disk encryption" |
| **Procedure** | Step by step, mandatory to follow | "How to enable BitLocker: steps 1 to 8" |
| **Guideline** | **Recommended**, not mandatory | "Consider using a password manager" |
| **Regulation / law** | Imposed externally, mandatory | GDPR, HIPAA |

The tested distinction: **guidelines are recommendations; policies, standards, and procedures are mandatory.**

---

## Privacy

**Personally identifiable information (PII)** is information that can identify an individual, alone or in combination. **Protected health information (PHI)** is health data under regulations such as HIPAA.

Key principles: collect only what is needed, use it only for the stated purpose, retain it only as long as necessary, and let individuals exercise their rights over it. Major regimes referenced: **GDPR** (EU), **HIPAA** (US health), **GLBA** (US financial).

---

## The ISC2 Code of Ethics

The four canons, in **order of precedence**, which is itself testable:

1. Protect society, the common good, necessary public trust and confidence, and the infrastructure
2. Act honorably, honestly, justly, responsibly, and legally
3. Provide diligent and competent service to principals
4. Advance and protect the profession

Where canons conflict, the earlier one takes precedence.

---

## Key terms

- **Confidentiality** - the property that information is accessible only to authorized parties
- **Integrity** - the property that information is accurate and has not been altered without authorization
- **Availability** - the property that information and systems are accessible to authorized users when needed
- **Non-repudiation** - assurance that an actor cannot credibly deny having performed an action
- **Authentication** - the process of proving an identity claim
- **Authorization** - the process of determining what an authenticated identity may do
- **Accounting** - the recording of actions taken by an identity, for later review
- **Multi-factor authentication** - authentication using two or more different factor categories
- **Asset** - anything of value to the organization that warrants protection
- **Vulnerability** - a weakness that a threat could exploit
- **Threat** - a circumstance or actor with the potential to exploit a vulnerability
- **Risk** - the combination of the likelihood of an event and its impact
- **Residual risk** - the risk that remains after controls have been applied
- **Risk tolerance** - the amount of risk an organization is willing to accept
- **Preventive control** - a control that stops an unwanted event from occurring
- **Detective control** - a control that identifies that an event has occurred
- **Corrective control** - a control that restores systems after an event
- **Deterrent control** - a control that discourages an actor from attempting an action
- **Compensating control** - an alternative control used when the primary control is not feasible
- **Defense in depth** - layering multiple controls so no single failure exposes the asset
- **Policy** - a high-level mandatory statement of organizational intent
- **Standard** - a specific mandatory requirement supporting a policy
- **Guideline** - a recommended, non-mandatory practice
- **PII** - personally identifiable information, data that can identify an individual

---

## Related

- [Notes 02: network security](./02-network-security.md)
- [Scenarios](../scenarios.md) - scenarios 1 and 2
