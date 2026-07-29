---
last-updated: 2026-07-29
---

# OSCP 05 - Active Directory Attacks

Active Directory is a major component of the current OSCP exam, worth a dedicated point
block. The exam presents a small domain to compromise from an initial foothold to domain
controller.

> Authorized testing only. Methodology as taught in PEN-200, for the exam, your lab, or
> engagements with written permission.

## Why AD matters on this exam

The exam includes a dedicated Active Directory set worth a significant share of the total.
You typically start with a foothold on one domain-joined host and must move laterally and
escalate to Domain Admin or an equivalent. Failing the AD set makes passing very hard, so
this material deserves proportionate study.

## Active Directory fundamentals

- **Domain** - a boundary of administration and a shared authentication database.
- **Domain controller (DC)** - hosts the directory and authenticates users. The usual objective is control of a DC or a Domain Admin account.
- **Forest** - one or more domains sharing a schema and trust.
- **Organizational unit (OU)** - a container for grouping objects and applying policy.
- **Group Policy (GPO)** - centralized configuration. Control of a GPO applied to a target is a path to compromise it.
- **Kerberos** - the primary authentication protocol, based on tickets from the Key Distribution Center.
- **NTLM** - the legacy challenge-response protocol, still present and central to several attacks.
- **Service Principal Name (SPN)** - links a service to the account running it, and is the basis of Kerberoasting.

## Domain enumeration

Once you have any domain credentials or a domain-joined foothold:

- **Users, groups, and computers** - enumerate the directory to map the terrain.
- **Group memberships** - especially privileged groups: Domain Admins, Enterprise Admins, and accounts with delegated rights.
- **Shares** - SMB shares often hold scripts and configuration files with credentials.
- **SPNs** - service accounts, targets for Kerberoasting.
- **Trust relationships** - between domains, relevant in multi-domain scenarios.
- **BloodHound-style graph analysis** - maps relationships to find the shortest path from your position to Domain Admin. Confirm the exam's tool policy, but graph-based path finding is standard AD methodology.

Enumeration from an authenticated position is where the AD path is found. The same
enumerate-thoroughly principle applies.

## Credential access and lateral movement

- **Credential harvesting** - from memory, the registry, files, and configuration. On a compromised host, cached and in-memory credentials are the pivot to the next.
- **Pass-the-Hash** - authenticating with an NTLM hash rather than the plaintext password, because NTLM authentication uses the hash directly.
- **Pass-the-Ticket** - reusing a stolen Kerberos ticket.
- **Overpass-the-Hash / Pass-the-Key** - using an NTLM hash to request a Kerberos ticket.
- **Kerberoasting** - requesting service tickets for accounts with SPNs, then cracking the ticket offline to recover the service account password. Service accounts often have weak, non-expiring passwords, which is why this works.
- **AS-REP Roasting** - for accounts with Kerberos pre-authentication disabled, requesting and cracking an AS-REP offline.
- **Password spraying** - trying one common password across many accounts, avoiding lockout by staying under the threshold. Effective because at least one user usually chooses a weak password.

## Common attack chain

1. Foothold on a domain-joined host as a low-privilege user.
2. Local privilege escalation on that host.
3. Harvest credentials and hashes from the host.
4. Enumerate the domain with those credentials.
5. Kerberoast or AS-REP roast to obtain more accounts.
6. Move laterally with pass-the-hash or valid credentials to a host where a privileged user is logged in.
7. Harvest the privileged credentials.
8. Reach Domain Admin, then the domain controller.
9. Optionally, dump the domain credential store from the DC for full proof.

## Persistence and dominance techniques (conceptual)

Recognize these; the exam is about achieving the goal, not maintaining covert access:

- **DCSync** - abusing replication rights to pull password hashes from the DC without running code on it.
- **Golden ticket** - forging a Kerberos ticket-granting ticket using the domain's krbtgt hash.
- **Silver ticket** - forging a service ticket for a specific service.

## Tooling note for the exam

The OSCP exam has specific rules on Active Directory tooling and on automated frameworks.
Some techniques are expected to be performed with permitted tools and manual methods rather
than a restricted framework. Read the exam guide's tool section carefully; using a
prohibited tool on the AD set can cost the whole block.

## Exam pointers

- The AD set is worth a large share; budget time for it and do not leave it last.
- The standard progression is foothold, local escalation, credential harvest, lateral movement, then domain compromise.
- Kerberoasting targets SPN accounts; AS-REP roasting targets accounts without pre-authentication.
- Pass-the-hash uses the NTLM hash directly, no cracking required.
- Password spraying beats brute force against lockout policies.
- Confirm which AD tools the exam permits before relying on any of them.

## Official documentation

**[📖 OffSec PEN-200 syllabus](https://www.offsec.com/courses/pen-200/)** - authoritative content list, including the AD module
**[📖 OSCP exam guide - Active Directory](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide)** - scoring and tool rules
**[📖 Microsoft Active Directory security documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/best-practices-for-securing-active-directory)** - the defender's view of these techniques
