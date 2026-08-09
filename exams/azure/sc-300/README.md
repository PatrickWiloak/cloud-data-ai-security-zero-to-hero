---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 7 min
---

# Microsoft Identity and Access Administrator (SC-300)

The identity certification. SC-300 covers designing, implementing, and operating Microsoft Entra ID: user and group management, authentication, Conditional Access, application identity, and identity governance.

It is the natural depth exam for anyone whose job touches access control, and one of the four qualifying prerequisites for [SC-100](../sc-100/).

## Exam Details

- **Exam Code:** SC-300
- **Level:** Associate
- **Duration:** 100 minutes
- **Questions:** Typically 40-60, may include case studies
- **Passing Score:** 700/1000
- **Cost:** USD 165, varies by region
- **Prerequisites:** None formal
- **Validity:** 1 year, free online renewal

See the [fact sheet](./fact-sheet.md) for full detail and official links.

## Domains

| Domain | Weight | Notes |
|--------|-------:|-------|
| Implement and manage user identities | 20-25% | [01](./notes/01-identities-and-tenant.md) |
| Implement authentication and access management | 25-30% | [02](./notes/02-authentication-and-conditional-access.md) |
| Plan and implement workload identities | 20-25% | [03](./notes/03-workload-identities-and-apps.md) |
| Plan and implement identity governance | 20-25% | [04](./notes/04-identity-governance.md) |

## What the exam actually tests

Three recurring themes:

1. **Licensing awareness.** Many questions are decided by the tier stated in the scenario. Conditional Access needs P1. Identity Protection risk policies and PIM need P2. Lifecycle workflows need Entra ID Governance. If you recommend a P2 feature to a P1 tenant, the answer is wrong regardless of how well it solves the problem.
2. **Feature boundaries.** Conditional Access, PIM, entitlement management, and access reviews all govern access, and the exam consistently offers them as alternatives to each other. Knowing precisely what each one does, and does not, is worth more than knowing configuration steps.
3. **Order of operations.** Several questions ask what must be configured first: password writeback before SSPR for synced users, an authentication method registered before a policy can require it, a catalog before an access package.

## Study sequence

1. **Tenant and directory objects** - users, groups, dynamic membership, administrative units, roles.
2. **Authentication** - methods policy, passwordless, SSPR, MFA. Get this solid before Conditional Access.
3. **Conditional Access and Identity Protection** - the heart of the exam. Build policies in a trial tenant.
4. **Applications** - registrations, service principals, consent, SSO, managed identities.
5. **Governance** - entitlement management, access reviews, PIM, lifecycle workflows.

Detailed schedule in the [practice plan](./practice-plan.md).

## Hands-on matters here

Entra ID has a free trial tenant and a developer program. Build these, because reading about them does not stick:

- A Conditional Access policy in report-only mode, then read the workbook
- A dynamic group with a membership rule using a custom attribute
- An access package with an approval workflow and 90-day expiry
- A PIM eligible assignment with approval and justification
- An app registration with delegated and application permissions, then compare the consent experience
- A user-assigned managed identity granted RBAC on a storage account

## Study resources

- **[📖 SC-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300)** - authoritative outline
- **[📖 Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/)** - the primary reference
- **[📖 Conditional Access templates](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common)** - the policy patterns Microsoft recommends
- **[📖 Microsoft Learn SC-300 path](https://learn.microsoft.com/en-us/training/browse/?terms=SC-300)** - free official modules
- [Practice questions](../../../resources/practice-questions/azure-identity-access-sc-300.md) - question bank in this repo

## Related

- [SC-100 Cybersecurity Architect](../sc-100/) - the expert design exam
- [SC-401 Information Security Administrator](../sc-401/) - the data protection counterpart
- [AZ-104 Azure Administrator](../az-104/) - RBAC and subscription administration
- [AZ-500 Azure Security Engineer](../az-500/) - the broader Azure security exam
- [Identity and IAM topic](../../../topics/iam.md)
- [Security Engineer roadmap](../../../resources/certification-roadmap-security-engineer.md)
