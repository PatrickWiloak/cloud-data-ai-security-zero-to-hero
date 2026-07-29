---
last-updated: 2026-07-29
---

# CISA Domain 5 - Protection of Information Assets (27%)

The largest domain. Logical and physical security controls, and how an auditor tests
whether they actually work.

## Information asset security frameworks

- **Information security governance** - direction, accountability, and monitoring for security. Owned by senior management, not by the security team alone.
- **Information security policy** - the mandate. Must be approved by senior management and communicated, or it is unenforceable.
- **Data classification** - the foundation. Protection should be proportionate to sensitivity, and you cannot be proportionate without classification.
- **Asset inventory** - you cannot protect what you have not identified.
- **Privacy by design** - building privacy protections into systems from the start.
- **Data privacy principles** - purpose limitation, data minimization, accuracy, storage limitation, and accountability.

## Identity and access management

- **Identification** - claiming an identity.
- **Authentication** - proving it.
- **Authorization** - what the proven identity may do.
- **Accountability** - attributing actions to an individual. Shared accounts destroy accountability, which is why they are a standing finding.

**Authentication factors** - something you know, something you have, something you are.
Two factors from the *same* category is not multifactor.

- **Biometrics** - measured by false acceptance rate (FAR, wrongly admitting an impostor), false rejection rate (FRR, wrongly rejecting a legitimate user), and the crossover error rate (CER, where FAR equals FRR). Lower CER means a better system. FAR is the security-critical measure.
- **Single sign-on (SSO)** - one authentication grants access to many systems. Improves user experience and password hygiene, but concentrates risk in one credential.
- **Privileged access management (PAM)** - controlled issuance, monitoring, and rotation of administrative credentials.
- **Access provisioning and deprovisioning** - joiner, mover, leaver. Failure to revoke access on termination is among the most frequently reported audit findings.
- **User access review (recertification)** - periodic confirmation by the data owner that access remains appropriate. Performed by the business owner, not by IT.
- **Least privilege and need to know** - minimum access required for the role and the task.

**Access control models**

- **Discretionary access control (DAC)** - the data owner grants access at their discretion.
- **Mandatory access control (MAC)** - access determined by labels and clearances, enforced by the system. Used where classification is legally mandated.
- **Role-based access control (RBAC)** - access derived from job role. Scales well and simplifies recertification.
- **Attribute-based access control (ABAC)** - decisions from attributes of user, resource, and context.

## Network and endpoint security

- **Firewall types** - packet filtering inspects headers; stateful tracks connections; application-layer (proxy) understands protocol content and is the most thorough but slowest.
- **DMZ** - a screened subnet hosting internet-facing services, separating them from the internal network.
- **IDS versus IPS** - detection and alerting versus inline prevention.
- **Network segmentation** - limits lateral movement and reduces audit scope.
- **VPN** - encrypted tunnel over an untrusted network.
- **Data loss prevention (DLP)** - detects and blocks sensitive data leaving the organization.
- **Endpoint protection** - anti-malware, host firewall, and EDR telemetry.
- **Patch management** - risk-prioritized, tested, and evidenced. The absence of a defined patch cycle is a finding regardless of how current systems happen to be.

## Cryptography

- **Symmetric encryption** - one shared key, fast, suited to bulk data. Key distribution is the problem. AES is the standard.
- **Asymmetric encryption** - public and private key pair, slow, solves key distribution. RSA and ECC.
- **Hybrid approach** - asymmetric to exchange a symmetric session key, then symmetric for the data. This is how TLS works.
- **Hashing** - one-way fixed-length digest, used for integrity. SHA-256 is current; MD5 and SHA-1 are broken for collision resistance.
- **Digital signature** - hash of the message encrypted with the sender's *private* key. Provides integrity, authentication, and non-repudiation. It does not provide confidentiality.
- **Encryption for confidentiality** - encrypt with the recipient's *public* key so only their private key can read it.
- **Public key infrastructure (PKI)** - certificate authorities, registration authorities, certificates, and revocation lists (CRL/OCSP) binding identities to public keys.
- **Key management** - generation, distribution, storage, rotation, and destruction. Weak key management defeats strong algorithms, and is what auditors actually test.

The private-key-signs, public-key-encrypts distinction is examined repeatedly. Signing
uses the sender's private key; confidentiality uses the recipient's public key.

## Physical and environmental security

- **Layered physical controls** - perimeter, building, floor, room, cabinet.
- **Access control vestibule (mantrap)** - admits one person at a time, defeating tailgating.
- **Badge and biometric entry** - with logging and periodic review of who holds access.
- **CCTV** - detective, and a deterrent. Retention must match investigation needs.
- **Visitor management** - registration and escort in sensitive areas.
- **Fire suppression** - water-based systems risk equipment; gas-based (clean agent) suppresses without residue. Detection should precede suppression.
- **Environmental monitoring** - temperature, humidity, and water detection under raised floors.

## Security monitoring and incident response

- **Logging and monitoring** - logs must be complete, protected from modification, time-synchronized, and actually reviewed. Collected-but-unreviewed logs are a finding.
- **SIEM** - correlation and alerting across sources.
- **Security incident response plan** - roles, escalation, communication, and evidence handling.
- **Forensic readiness** - chain of custody and imaging procedures defined in advance.
- **Penetration testing** - authorized simulated attack. Scope, rules of engagement, and written authorization are mandatory.
- **Vulnerability assessment** - identifies weaknesses; it does not exploit them. Penetration testing does.

## Auditing security controls

- **Testing access controls** - request a user listing, sample accounts, and trace back to authorized approvals. Look for terminated employees with live accounts.
- **Reviewing privileged accounts** - who holds them, why, and whether activity is logged and reviewed.
- **Testing the recertification process** - was it performed, by the owner, with evidence, and were revocations acted on?
- **Evaluating encryption** - what is encrypted, with what algorithm and key length, and how keys are managed.

## Exam pointers

- Failure to revoke access on termination is the highest-frequency finding in this domain.
- User access reviews are performed by the business data owner, not IT or security.
- Non-repudiation comes from digital signatures, which use the sender's private key.
- Shared or generic accounts break accountability; look for that in scenario questions.
- A biometric system's security is judged on FAR; user acceptance is judged on FRR.
- Logs that are collected but never reviewed provide no detective control.

## Official documentation

**[📖 ISACA CISA exam content outline](https://www.isaca.org/credentialing/cisa)** - authoritative domain list
**[📖 NIST SP 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)** - security and privacy controls catalog
**[📖 ISO/IEC 27001](https://www.iso.org/standard/27001)** - information security management systems
