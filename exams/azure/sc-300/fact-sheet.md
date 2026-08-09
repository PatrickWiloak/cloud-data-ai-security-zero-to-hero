---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 13 min
---

# Microsoft Identity and Access Administrator (SC-300) Fact Sheet

## Exam Overview

**Exam Code:** SC-300
**Exam Name:** Microsoft Identity and Access Administrator
**Level:** Associate
**Duration:** 100 minutes
**Format:** Multiple choice, multiple select, drag-and-drop, case studies, and yes/no series questions
**Questions:** Typically 40-60
**Passing Score:** 700 out of 1000
**Cost:** USD 165 (varies by country)
**Valid For:** 1 year, renewable free online through Microsoft Learn
**Delivery:** Pearson VUE, test center or online proctored
**Prerequisites:** None formally; working knowledge of Microsoft Entra ID and Microsoft 365 expected

> **Verify before booking.** Microsoft revises skills-measured documents on a rolling basis and prices vary by region. Confirm the current outline and price on the official pages below.

**[📖 SC-300 certification page](https://learn.microsoft.com/en-us/credentials/certifications/identity-and-access-administrator/)** - registration and renewal
**[📖 SC-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300)** - the authoritative skills-measured outline
**[📖 Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/)** - product documentation for everything on this exam

## Why this exam matters here

Identity is the control plane of the modern cloud. This repo has an [identity topic page](../../../topics/iam.md), an [identity service comparison](../../../resources/service-comparison-identity-iam.md), and IAM content threaded through nearly every cert, but SC-300 is the identity-specific certification.

It is also the practical prerequisite path into [SC-100](../sc-100/), and it pairs naturally with [AZ-104](../az-104/) for administrators and [SC-200](../sc-200/) for the SOC side.

## Target Audience

- Identity and access administrators managing Entra ID
- Microsoft 365 administrators who own identity
- Cloud administrators moving into an identity-focused role
- Security engineers who need Conditional Access and governance depth

Expected background: managing Entra ID tenants, configuring authentication methods, troubleshooting sign-in issues, and familiarity with Microsoft 365 and Azure RBAC.

## Exam Domains

### Domain 1: Implement and manage user identities (20-25%)

**Key Concepts:**
- Tenant configuration, company branding, and tenant properties
- User and group creation, bulk operations, and dynamic membership rules
- Administrative units and delegated administration
- Entra ID roles: built-in roles, custom roles, and scoped assignment
- Licensing: group-based licensing and license reconciliation
- External identities: B2B collaboration, guest invitation and redemption, cross-tenant access settings
- External ID for customers (CIAM) concepts and user flows
- Hybrid identity: Entra Connect Sync and Cloud Sync, filtering, sync errors, and password writeback
- Device identity: registered, Entra joined, hybrid joined, and what each enables

**[📖 Manage users and groups](https://learn.microsoft.com/en-us/entra/fundamentals/)** - tenant and directory object management
**[📖 Entra Connect and Cloud Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/)** - hybrid identity options

### Domain 2: Implement authentication and access management (25-30%)

The largest domain.

**Key Concepts:**
- Authentication methods policy: FIDO2 security keys, Windows Hello for Business, Microsoft Authenticator, passkeys, temporary access pass, certificate-based authentication, OATH tokens, SMS and voice
- Passwordless and phishing-resistant authentication design
- Self-service password reset: registration, writeback, and combined registration
- Password protection: global and custom banned password lists, on-premises agent
- Multifactor authentication: methods, registration campaigns, and number matching
- Conditional Access: assignments, conditions, grant controls, session controls, filters, authentication context
- Continuous access evaluation
- Identity Protection: sign-in risk, user risk, risk policies, and remediation
- Entra ID Protection integration with Conditional Access
- Global Secure Access concepts: Entra Internet Access and Entra Private Access
- Privileged Identity Management: eligible assignments, activation, approval, alerts, and access reviews for roles

**[📖 Authentication methods](https://learn.microsoft.com/en-us/entra/identity/authentication/)** - method policy and passwordless
**[📖 Conditional Access documentation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/)** - policy design and templates
**[📖 Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/)** - risk detection and policy

### Domain 3: Plan and implement workload identities (20-25%)

**Key Concepts:**
- Application registration vs enterprise application (service principal), and the relationship between them
- App consent: user consent settings, admin consent workflow, and consent grant review
- Permissions: delegated vs application permissions, scopes, and roles
- Single sign-on options: SAML, OIDC, password-based, linked, and header-based with application proxy
- Application Proxy for on-premises web applications
- Managed identities: system-assigned and user-assigned
- Workload identity federation for GitHub Actions, Kubernetes, and other clouds
- Service principal credential management, certificate and secret rotation
- Conditional Access for workload identities
- App governance and risky application detection

**[📖 Application management](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/)** - enterprise apps, SSO, and consent
**[📖 Managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/)** - Azure resource identity

### Domain 4: Plan and implement identity governance (20-25%)

**Key Concepts:**
- Entitlement management: catalogs, access packages, policies, approval, and expiry
- Access reviews for groups, applications, and role assignments
- Lifecycle workflows: joiner, mover, and leaver automation
- Terms of use and their enforcement through Conditional Access
- Privileged Identity Management for Entra roles, Azure resources, and groups
- Separation of duties in access packages
- Monitoring and reporting: sign-in logs, audit logs, provisioning logs, and workbooks
- Log integration with Log Analytics, Sentinel, and Event Hubs
- Microsoft Entra Permissions Management concepts

**[📖 Entra ID Governance](https://learn.microsoft.com/en-us/entra/id-governance/)** - entitlement management, reviews, lifecycle workflows
**[📖 Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/)** - just-in-time privileged access

## Licensing quick reference

Licensing constrains many exam answers. If a scenario states a tier, features above it are wrong.

| Feature | Minimum license |
|---|---|
| Security defaults, basic MFA | Free |
| Group-based licensing, SSPR for cloud users, dynamic groups | P1 |
| Conditional Access | P1 |
| Self-service password reset with writeback | P1 |
| Application Proxy | P1 |
| Identity Protection risk policies | P2 |
| Privileged Identity Management | P2 |
| Access reviews, entitlement management | P2 or Entra ID Governance |
| Lifecycle workflows | Entra ID Governance |
| Permissions Management | Separate license |

## Related repo material

- [Notes](./notes/) - four notes, one per domain
- [Practice plan](./practice-plan.md) - 6-week schedule
- [Scenarios](./scenarios.md) - identity design scenarios
- [Strategy](./strategy.md) - study and exam technique
- [SC-100](../sc-100/) - the expert exam this feeds into
- [AZ-104](../az-104/) - Azure administration, overlapping RBAC content
- [Identity and IAM topic](../../../topics/iam.md)
- [IAM explained](../../../learn/concepts/iam-explained.md) - the plain-English primer
