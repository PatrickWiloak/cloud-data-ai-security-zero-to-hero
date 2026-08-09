---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 8 min
---

# 03 - Access control concepts

**Domain 2: Access Control Concepts (22%)**

---

## Physical access controls

Protecting the physical environment, which is a real exam topic and not an afterthought.

| Control | Purpose |
|---|---|
| **Badge or card reader** | Preventive; restricts entry to authorized holders |
| **Mantrap** (access control vestibule) | Prevents **tailgating** by allowing one person through at a time |
| **Turnstile** | Enforces single-person entry |
| **Security guard** | Preventive and deterrent; can exercise judgement |
| **CCTV** | Deterrent when visible, detective when recorded |
| **Fence, bollard, lighting** | Deterrent and preventive perimeter controls |
| **Sensor and alarm** | Detective |
| **Biometric reader** | Preventive; authentication by something you are |

**Tailgating** (following an authorized person through a door) and **piggybacking** (being let through knowingly) are the attacks these controls address.

---

## Principles

- **Least privilege**: grant only the permissions needed to perform the job, and no more. Limits what a subject can **do**.
- **Need to know**: grant access only to the information required for the task, even where broader access is technically possible. Limits what a subject can **see**.
- **Separation of duties**: split a sensitive process so no single person can complete it alone. The person who requests a payment must not be the person who approves it.
- **Two-person control** (dual control): require two people to act together for the most sensitive operations.
- **Job rotation**: move people between roles periodically, which both spreads capability and surfaces fraud that depends on one person staying in place.
- **Mandatory vacation**: similar detective purpose, since ongoing concealment usually requires presence.
- **Defense in depth** applied to access: physical, network, host, application, and data layers each enforce their own controls.

---

## Access control models

| Model | Who decides | Characteristic | Typical setting |
|---|---|---|---|
| **DAC** (discretionary) | The data owner | The owner grants access at their discretion | File shares, personal file permissions |
| **MAC** (mandatory) | The system, from labels and clearances | Users cannot override; enforced centrally | Military and government classification |
| **RBAC** (role-based) | Roles carry permissions; users are assigned roles | Scales well, simplifies administration | Most enterprises |
| **ABAC** (attribute-based) | A policy evaluates attributes at access time | Most flexible: user, resource, device, time, location | Modern cloud and zero trust |
| **Rule-based** | Predefined rules applied uniformly | Often used alongside another model | Firewall rule sets, time-of-day restrictions |

Distinguishing DAC from MAC is a reliable question: DAC lets the owner decide, MAC does not.

---

## Identity and access lifecycle

1. **Provisioning** - create the identity and grant initial access, based on role
2. **Modification** - adjust access when the person changes role. The classic failure is **privilege creep**, where access accumulates because old permissions are never removed
3. **Review** - periodic recertification that access is still needed, usually by the manager or resource owner
4. **Deprovisioning** - remove access promptly on departure. Delayed deprovisioning is a common audit finding and a real insider risk

**Privileged access management** applies stricter treatment to administrative accounts: separate admin accounts, stronger authentication, just-in-time elevation, session recording, and closer monitoring.

---

## Authentication in practice

- **Something you know**: password, PIN, security question
- **Something you have**: hardware token, smart card, phone with an authenticator app
- **Something you are**: fingerprint, face, iris, voice

Sometimes added: **somewhere you are** (location) and **something you do** (behavioral patterns).

**Multi-factor authentication** requires factors from **different categories**. A password plus a security question is single factor, because both are something you know.

**Biometric measures**: the **false acceptance rate** (wrongly accepting an impostor) and the **false rejection rate** (wrongly rejecting a legitimate user) trade against each other. The **crossover error rate**, where the two are equal, is used to compare systems.

**Single sign-on** lets one authentication serve many systems, improving user experience and centralizing control, at the cost of concentrating risk in that one authentication event, which is why SSO is normally paired with MFA.

---

## Key terms

- **Least privilege** - granting only the permissions required to perform a role, and no more
- **Need to know** - restricting access to only the information required for a specific task
- **Separation of duties** - dividing a sensitive process so no one person can complete it alone
- **Job rotation** - periodically moving staff between roles, which helps surface concealed fraud
- **Tailgating** - following an authorized person through a physical access control without authenticating
- **Mantrap** - an access control vestibule permitting one person through at a time
- **DAC** - discretionary access control, where the data owner decides who may access a resource
- **MAC** - mandatory access control, where the system enforces access from labels and clearances
- **RBAC** - role-based access control, where permissions attach to roles and users are assigned roles
- **ABAC** - attribute-based access control, where a policy evaluates multiple attributes at access time
- **Privilege creep** - the accumulation of unnecessary permissions as a person changes roles over time
- **Provisioning** - creating an identity and granting its initial access
- **Deprovisioning** - removing access when a person leaves or no longer requires it
- **Access review** - periodic recertification that existing access is still required
- **Privileged access management** - the stricter controls applied to administrative accounts
- **False acceptance rate** - the rate at which a biometric system wrongly accepts an impostor
- **False rejection rate** - the rate at which a biometric system wrongly rejects a legitimate user
- **Crossover error rate** - the point where false acceptance and false rejection rates are equal
- **Single sign-on** - one authentication event granting access to multiple systems

---

## Related

- [Notes 04: security operations](./04-security-operations.md)
- [Scenarios](../scenarios.md) - scenarios 3 and 4
- [IAM explained](../../../../learn/concepts/iam-explained.md)
