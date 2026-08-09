---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 13 min
---

# 02 - Authentication and Conditional Access

**Domain 2: Implement authentication and access management (25-30%)**

The largest domain and the heart of the exam.

---

## Authentication methods policy

The modern, single control point for which methods users may register and use. Legacy per-user MFA settings and the older SSPR method configuration are being consolidated into it.

Methods, roughly in order of strength:

| Method | Phishing-resistant | Notes |
|---|---|---|
| **FIDO2 security key / passkey** | Yes | Strongest, hardware-bound |
| **Windows Hello for Business** | Yes | Device-bound biometric or PIN |
| **Certificate-based authentication** | Yes | Smart card scenarios, supports strong authentication binding |
| **Microsoft Authenticator (passwordless sign-in)** | Partially | Number matching required |
| **Microsoft Authenticator (push with number matching)** | No | Resistant to fatigue attacks, not to AiTM |
| **OATH hardware or software token** | No | Offline codes |
| **SMS / voice** | No | Weakest; avoid for privileged users |
| **Temporary Access Pass** | N/A | Time-limited onboarding and recovery credential |

**Authentication strengths** let a Conditional Access policy require a specific set of methods rather than generic MFA. This is how you express "phishing-resistant MFA for administrators".

---

## Self-service password reset

Components: enabled scope (none, selected group, all), the number of methods required to reset, registration enforcement, and notification settings.

Critical dependency: **password writeback** for synced users. Without it, SSPR updates only the cloud password.

**Combined registration** enrols the user for both MFA and SSPR in one experience. **Registration campaigns** nudge users from weaker methods onto the Authenticator app.

**Entra Password Protection** blocks weak passwords using a global banned list plus a custom list, and can be extended to on-premises Active Directory through a domain controller agent.

---

## Conditional Access

The policy engine. Every policy is: **assignments** (who and what), **conditions** (when), and **controls** (what happens).

### Assignments
- Users and groups, directory roles, guest and external user types, workload identities
- Target resources: cloud apps, user actions (register security info, register or join device), authentication context, global secure access traffic

### Conditions
- Sign-in risk and user risk (requires Identity Protection, P2)
- Insider risk (Purview integration)
- Device platform
- Locations, including named and trusted locations
- Client apps (browser, mobile and desktop, legacy authentication clients)
- Filter for devices, using device attributes
- Authentication flows (device code flow, authentication transfer)

### Grant controls
Block, or require any or all of: MFA, authentication strength, compliant device, hybrid joined device, approved client app, app protection policy, password change, terms of use.

### Session controls
Sign-in frequency, persistent browser session, Conditional Access App Control (Defender for Cloud Apps), app enforced restrictions, customize continuous access evaluation, disable resilience defaults, token protection.

### Evaluation rules the exam tests
- Policies are **additive**. Every matching policy applies.
- **Block always wins** over any grant.
- Conditional Access evaluates **after** primary authentication succeeds. It cannot prevent credential validation, only the resulting access.
- Exclusions are evaluated before inclusions, which is why break-glass exclusions are reliable.
- **Report-only** mode logs what would have happened without enforcing.

### Deployment safety
Every correct exam answer that creates a Conditional Access policy includes:
1. Two **break-glass** cloud-only accounts excluded, with alerting on their use
2. **Report-only** first, reviewed through the Conditional Access workbook and the What If tool
3. Staged rollout with a pilot group

---

## Continuous access evaluation

CAE lets supporting resource providers revoke or re-evaluate a session near real time when a critical event occurs, such as account disablement, password change, or a detected risk. It shortens the window in which a stolen token remains usable, and it is why token lifetime tuning is no longer the primary answer to session revocation questions.

---

## Identity Protection

Requires Entra ID P2.

- **Sign-in risk** - probability that the sign-in is not from the legitimate owner: anonymous IP, atypical travel, malware-linked IP, unfamiliar sign-in properties, token anomalies.
- **User risk** - probability that the identity is compromised: leaked credentials, threat intelligence.
- **Risk policies** - implemented as Conditional Access policies referencing risk level, typically "require MFA on medium sign-in risk" and "require secure password change on high user risk".
- **Remediation** - self-remediation through MFA or password change, or admin dismissal, confirmation of compromise, or safe dismissal.

Leaked credential detection requires password hash sync, which is a common exam detail for federated or pass-through tenants.

---

## Global Secure Access

Entra's Security Service Edge offering, appearing on the exam at concept level:

- **Entra Internet Access** - secure web gateway with Conditional Access applied to internet traffic
- **Entra Private Access** - Zero Trust network access to private applications, the successor pattern to VPN and an evolution of Application Proxy
- Traffic forwarding profiles route Microsoft, internet, or private traffic through the service, enabling Conditional Access on network destinations

---

## Key terms

- **Authentication methods policy** - the tenant policy defining which authentication methods users may register and use
- **Authentication strength** - a named set of allowed authentication methods that a Conditional Access grant control can require
- **Phishing-resistant MFA** - authentication bound to the origin or hardware, such as FIDO2, Windows Hello for Business, or certificate-based authentication
- **Temporary Access Pass** - a time-limited passcode used to onboard or recover a user who cannot use their normal methods
- **Combined registration** - a single experience registering a user for both MFA and self-service password reset
- **Entra Password Protection** - global and custom banned password lists, extendable to on-premises Active Directory
- **Report-only mode** - a Conditional Access state that logs the policy result without enforcing it
- **Break-glass account** - an excluded emergency cloud-only administrator account protecting against tenant lockout
- **Continuous access evaluation** - near real-time session re-evaluation triggered by critical events such as password change or account disablement
- **Sign-in risk** - Identity Protection's assessment that a given authentication attempt is not from the legitimate identity owner
- **User risk** - Identity Protection's assessment that an identity itself is compromised, for example through leaked credentials
- **Conditional Access App Control** - session control routing traffic through Defender for Cloud Apps for in-session monitoring and restriction
- **Token protection** - a session control binding a refresh token to the device it was issued to
- **Global Secure Access** - Entra's security service edge covering Internet Access and Private Access

---

## Related

- [Notes 03: workload identities and applications](./03-workload-identities-and-apps.md)
- [Scenarios](../scenarios.md) - scenarios 2, 3, and 7
- [TLS and HTTPS](../../../../learn/concepts/tls-and-https.md)
