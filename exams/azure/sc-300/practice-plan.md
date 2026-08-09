---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 6 min
---

# SC-300 Study Plan

Six weeks at 6-8 hours per week. Every week has a lab item, because Entra ID concepts do not stick from reading alone. Use a free Microsoft 365 developer tenant or an Entra ID P2 trial.

## Week 1: Tenant, users, groups

- [ ] Read the [SC-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300) and note every task verb
- [ ] Tenant properties, company branding, and tenant-level settings
- [ ] Users: creation, bulk operations, external vs member user type
- [ ] Groups: security vs Microsoft 365, assigned vs dynamic
- [ ] Dynamic membership rule syntax, and where it fails
- [ ] Administrative units and scoped role assignment
- [ ] Entra roles: built-in, custom, and the least-privileged role for a task
- [ ] Group-based licensing and license reconciliation
- [ ] **Lab**: create a dynamic group whose rule keys on a custom extension attribute, and a scoped admin unit
- [ ] Review Notes: `notes/01-identities-and-tenant.md`

## Week 2: Hybrid and external identity

- [ ] Entra Connect Sync vs Cloud Sync: capability differences and when each applies
- [ ] Sync scoping, filtering, and troubleshooting sync errors
- [ ] Password writeback and its prerequisites
- [ ] Device identity: registered, Entra joined, hybrid joined
- [ ] B2B collaboration: invitation, redemption, guest settings
- [ ] Cross-tenant access settings: inbound, outbound, trust settings for MFA claims
- [ ] External ID for customers (CIAM) concepts and user flows
- [ ] **Lab**: invite a guest, restrict guest directory permissions, configure a cross-tenant trust setting

## Week 3: Authentication

- [ ] Authentication methods policy and migration from legacy MFA settings
- [ ] Passwordless: FIDO2, Windows Hello for Business, Microsoft Authenticator, passkeys
- [ ] Temporary access pass and certificate-based authentication
- [ ] Self-service password reset: registration, writeback, combined registration
- [ ] Password protection: global and custom banned lists, on-premises agent
- [ ] MFA: registration campaigns, number matching, method strength
- [ ] Authentication strengths and where they are referenced
- [ ] **Lab**: configure the authentication methods policy, enable a registration campaign, and register a passkey
- [ ] Review Notes: `notes/02-authentication-and-conditional-access.md`

## Week 4: Conditional Access and Identity Protection

- [ ] Conditional Access anatomy: assignments, conditions, grant, session
- [ ] Filters for devices and applications; authentication context
- [ ] Session controls: sign-in frequency, persistent browser, app enforced restrictions, token protection
- [ ] Continuous access evaluation and what it changes
- [ ] Break-glass account design and exclusion strategy
- [ ] Report-only mode, the What If tool, and the Conditional Access workbook
- [ ] Identity Protection: sign-in risk, user risk, detections, and risk policies
- [ ] Global Secure Access concepts
- [ ] **Lab**: build three policies in report-only, review the workbook, then enforce one

## Week 5: Workload identities and applications

- [ ] App registration vs enterprise application vs service principal
- [ ] Delegated vs application permissions, and consent grant review
- [ ] User consent settings and the admin consent workflow
- [ ] SSO options: SAML, OIDC, password-based, linked, header-based
- [ ] Application Proxy for on-premises apps
- [ ] Managed identities: system-assigned vs user-assigned
- [ ] Workload identity federation for CI/CD and Kubernetes
- [ ] Conditional Access for workload identities
- [ ] **Lab**: register an app, grant delegated Graph permissions, then compare with application permissions and admin consent
- [ ] Review Notes: `notes/03-workload-identities-and-apps.md`

## Week 6: Governance and review

- [ ] Entitlement management: catalogs, access packages, policies, separation of duties
- [ ] Access reviews for groups, applications, and roles; auto-apply behavior
- [ ] Lifecycle workflows: joiner, mover, leaver
- [ ] PIM: eligible vs active, activation settings, approval, alerts, PIM for Groups
- [ ] Terms of use and Conditional Access enforcement
- [ ] Monitoring: sign-in, audit, and provisioning logs; export to Log Analytics and Sentinel
- [ ] **Lab**: build an access package with approval and expiry, and a PIM eligible assignment with approval
- [ ] Review Notes: `notes/04-identity-governance.md`
- [ ] Work every scenario in [scenarios.md](./scenarios.md)
- [ ] Two full timed practice exams, reviewing every wrong answer for the licensing or feature-boundary cause

## Readiness check

You are ready when you can, without notes:

- [ ] State the minimum license for Conditional Access, PIM, Identity Protection, and lifecycle workflows
- [ ] Explain when to use an access package instead of a group, and PIM instead of either
- [ ] Describe what Conditional Access cannot do
- [ ] Name the prerequisite for SSPR to work for a synced user
- [ ] Distinguish delegated from application permissions and give an example of each
- [ ] Explain the difference between an app registration and an enterprise application
- [ ] Choose between Entra Connect Sync and Cloud Sync for a given constraint
