---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 11 min
---

# 03 - Workload identities and applications

**Domain 3: Plan and implement workload identities (20-25%)**

---

## App registration vs enterprise application

The single most confused topic in this domain.

| Object | What it is | Where it lives |
|---|---|---|
| **Application registration** | The global definition of the application: redirect URIs, exposed API, requested permissions, credentials | Only in the app's home tenant |
| **Service principal (enterprise application)** | The local instance of that application in a tenant, holding consent grants, assignments, and SSO configuration | In every tenant where the app is used |

Registering an app in your tenant creates both objects. Consenting to a third-party multi-tenant app creates only a service principal in your tenant, because the registration lives in the vendor's tenant.

Practical consequence: you configure SAML SSO, user assignment, and provisioning on the **enterprise application**; you configure API permissions, redirect URIs, and credentials on the **app registration**.

---

## Permissions and consent

### Permission types

| Type | Acts as | Effective permission | Consent |
|---|---|---|---|
| **Delegated** | The signed-in user | Intersection of the app's permission and the user's own rights | User or admin, depending on the permission |
| **Application** | Itself, no user present | Exactly what was granted, tenant-wide | Always admin consent |

A daemon or scheduled job with no signed-in user requires application permissions. A delegated permission cannot work in that scenario no matter how high the permission.

### Consent governance

- **User consent settings**: allow for all apps, allow only for verified publishers and low-impact permissions, or disable entirely.
- **Admin consent workflow**: users request, designated reviewers approve, with a record.
- **Consent grant review**: periodically audit which apps hold which permissions, and revoke what is unused. Illicit consent grants are a real attack technique.
- **App governance** (via Defender for Cloud Apps) detects overprivileged and anomalous applications.

---

## Single sign-on options

| Method | Use when |
|---|---|
| **SAML 2.0** | Enterprise SaaS supporting SAML federation |
| **OIDC / OAuth 2.0** | Modern applications, including anything using Microsoft identity platform libraries |
| **Password-based** | Legacy apps with only a form login; Entra stores and replays credentials |
| **Linked** | A tile in My Apps that points elsewhere; no authentication integration |
| **Header-based** | Legacy on-premises apps expecting headers, through Application Proxy |

**Application Proxy** publishes on-premises web applications through Entra ID without opening inbound firewall ports, using an outbound connector. Entra Private Access is the newer, broader answer for private application access.

**Provisioning**: SCIM-based automatic user provisioning to SaaS applications, with attribute mapping, scoping filters, and provisioning logs.

---

## Managed identities

An Entra identity that Azure manages for a resource, with no credential in your code.

| Type | Lifecycle | Use when |
|---|---|---|
| **System-assigned** | Created with the resource, deleted with it, one-to-one | The identity belongs to exactly one resource |
| **User-assigned** | Standalone resource, assignable to many | Several resources share an identity, or the identity must pre-exist |

Managed identities work wherever the target supports Entra ID authentication: Key Vault, Storage, SQL, Service Bus, Cosmos DB, and Microsoft Graph. Prefer them over any stored secret.

---

## Workload identity federation

Extends the no-secret model beyond Azure. An external workload presents a token from its own issuer, and Entra ID exchanges it for an access token based on a configured trust.

Supported issuers include GitHub Actions, Kubernetes service accounts, Google Cloud, AWS, and any OIDC-compliant provider.

Design points the exam cares about:
- The **subject** of the federated credential should be as narrow as possible: a specific repository and branch or environment, not the whole organization
- Use separate federated credentials per environment so a feature branch cannot deploy to production
- Federation removes the secret entirely; it does not remove the need to scope RBAC

---

## Securing workload identities

- **Conditional Access for workload identities** applies location and risk conditions to service principals, which is the only way to constrain where a service principal may authenticate from.
- **Workload Identity Premium** licensing covers Conditional Access for workload identities and risk detection for service principals.
- **Credential hygiene**: prefer managed identity, then federation, then certificate, then secret. Rotate and set short expiry. Alert on credentials nearing expiry rather than discovering it during an outage.
- **Ownership and lifecycle**: applications need owners and periodic review, or they accumulate as orphaned identities holding permissions nobody remembers granting.

---

## Key terms

- **Application registration** - the global definition of an application in its home tenant, holding redirect URIs, permissions, and credentials
- **Service principal** - the local instance of an application in a tenant, holding consent grants, assignments, and SSO configuration
- **Delegated permission** - a permission where the application acts on behalf of a signed-in user, limited to the intersection of app and user rights
- **Application permission** - a permission where the application acts as itself with no user, always requiring admin consent
- **Admin consent workflow** - a process letting users request access to applications and designated reviewers approve it
- **Illicit consent grant** - an attack where a user is tricked into consenting to a malicious application's permissions
- **Application Proxy** - a service publishing on-premises web applications through Entra ID using an outbound connector
- **SCIM provisioning** - standards-based automatic user provisioning and deprovisioning to SaaS applications
- **System-assigned managed identity** - an identity created with and tied to the lifecycle of a single Azure resource
- **User-assigned managed identity** - a standalone Azure resource identity that can be assigned to multiple resources
- **Workload identity federation** - a trust configuration allowing external workloads to obtain Entra tokens without a stored secret
- **Conditional Access for workload identities** - policies applying location and risk conditions to service principals rather than users

---

## Related

- [Notes 04: identity governance](./04-identity-governance.md)
- [Scenarios](../scenarios.md) - scenarios 4 and 6
- [Agent and tool security](../../../../resources/ai-security/agent-security.md) - the same identity principles applied to AI agents
