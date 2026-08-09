---
last-updated: 2026-08-09
difficulty: advanced
reading-time: 14 min
---

# 04 - Application and data security

**Domain 4: Design security solutions for applications and data (20-25%)**

Application identity, secure development, data classification and protection, encryption and key management, and the newer material on securing AI workloads.

---

## Application identity

**Managed identities** are the default answer to "how should this application authenticate to that Azure service".

- **System-assigned** - lifecycle tied to the resource, one-to-one. Use when the identity belongs to exactly one resource.
- **User-assigned** - standalone resource, assignable to many. Use when several resources share an identity or when the identity must exist before the resource.

Managed identities remove secrets from the application entirely, which is why they beat Key Vault-stored credentials whenever the target supports Entra ID authentication.

**Workload identity federation** extends this to workloads outside Azure: GitHub Actions, Kubernetes service accounts, and other clouds obtain Entra tokens through a trust relationship rather than a stored client secret. This is the answer for "eliminate long-lived credentials in our CI/CD pipeline".

**App registration governance**: restrict who can register applications, require admin consent for permissions above a threshold, review consented permissions, and use application access policies to limit which mailboxes or sites an app can reach.

---

## Secure development lifecycle

| Stage | Control |
|---|---|
| Code | GitHub Advanced Security or Defender for DevOps: secret scanning, code scanning with CodeQL, dependency review |
| Build | Signed builds, pinned dependencies, SBOM generation |
| Infrastructure as code | IaC scanning for misconfiguration before deployment |
| Registry | Container image scanning through Defender for Containers |
| Deploy | Azure Policy deny effects and deployment gates |
| Runtime | Defender for App Service, Defender for Containers, WAF |

**Defender for DevOps** connects GitHub and Azure DevOps into Defender for Cloud so that code-level findings appear alongside cloud posture, and so that a misconfiguration can be traced from a running resource back to the template that created it.

---

## API security

- **API Management** policies: rate limiting, quota, IP filtering, JWT validation, mutual TLS, request and response transformation
- **Defender for APIs**: discovery of unmanaged and shadow APIs, sensitive data exposure detection, and runtime threat detection
- Design pattern: front APIs with API Management, validate tokens at the gateway, enforce a rate limit per subscription key, and place a WAF ahead of it for OWASP protections

---

## Data classification and protection with Purview

The Purview stack, in the order a design uses it:

1. **Data map and scanning** - discover and catalog data across Azure, on-premises, and other clouds
2. **Sensitive information types and trainable classifiers** - identify what the data is
3. **Sensitivity labels** - apply classification and protection (encryption, watermarking, access restriction) that travels with the file
4. **Auto-labeling policies** - apply labels at scale without manual review, in service-side and client-side variants
5. **Data loss prevention** - prevent labeled or classified data leaving through endpoints, Exchange, SharePoint, Teams, Defender for Cloud Apps, and AI applications
6. **Insider risk management** - behavioral detection of risky user activity
7. **Data lifecycle and records management** - retention and disposition
8. **Compliance Manager** - assessment workflow and evidence
9. **DSPM for AI** - visibility into what sensitive data AI interactions touch

**Sensitivity label vs DLP** is a recurring exam distinction. A label classifies and can encrypt the file itself, persisting wherever the file goes. A DLP policy inspects activity and blocks or warns at a boundary. Requirements about protection that travels with the document need labels; requirements about preventing an action need DLP. Many scenarios need both.

---

## Encryption and key management

| Option | Control level | Choose when |
|---|---|---|
| Platform-managed keys | Microsoft manages entirely | Default; no specific key requirement |
| Customer-managed keys (CMK) in Key Vault | You control key lifecycle and revocation | Compliance requires customer control or crypto-shredding |
| Managed HSM | Single-tenant, FIPS 140-2 Level 3 validated HSM | Regulatory requirement for hardware isolation |
| Azure Dedicated HSM / Payment HSM | Bare-metal HSM you administer | Legacy or PCI PIN workloads needing direct HSM control |
| Customer-provided keys | Key supplied per request, never stored | Rare, blob-level scenarios |
| Double encryption | Two independent layers, infrastructure plus service | Regulatory requirement for defense in depth on encryption |
| Confidential computing | Data encrypted in use, in a TEE | Data must be protected from the host and operator |

**Key Vault design**: separate vaults per environment and per trust boundary, RBAC over access policies for new deployments, purge protection and soft delete enabled, private endpoint access, rotation policies, and diagnostic logging to a workspace.

**Crypto-shredding**: with CMK, revoking or destroying the key renders the data unrecoverable. This is the answer when a scenario requires provable data destruction across many storage systems.

---

## Database protections

| Requirement | Feature |
|---|---|
| Encrypt data at rest transparently | Transparent Data Encryption, optionally with CMK |
| Hide values from privileged operators | Always Encrypted (with secure enclaves for range queries) |
| Mask values for non-privileged users | Dynamic data masking (presentation only, not a security boundary) |
| Restrict rows by user context | Row-level security |
| Detect anomalous access | Defender for SQL |
| Discover and classify columns | SQL data discovery and classification, feeding Purview |
| Authenticate without passwords | Entra ID authentication with managed identity |

Dynamic data masking is frequently offered as a distractor for requirements that need Always Encrypted. Masking obscures data in results but does not prevent a determined user with query access from inferring or extracting it.

---

## Securing AI workloads

Newer material, and increasingly present on the exam.

- **Azure AI Content Safety** - text and image moderation, plus **Prompt Shields** for direct (jailbreak) and indirect (document) prompt injection detection, and groundedness detection for hallucination
- **Purview DSPM for AI** - discovery of sensitive data flowing through AI interactions, including Copilot
- **DLP for AI applications** - preventing sensitive content from being sent to or returned from AI apps
- **Private networking for Azure OpenAI** - private endpoints and disabled public access
- **CMK for Azure AI services** - customer-controlled encryption of stored data
- **Managed identity** for application-to-model authentication, removing API keys
- **Defender for AI Services** - runtime detection signals for AI workloads
- Permission hygiene first: an assistant that honors existing permissions turns oversharing into exposure, so SharePoint access reviews and site controls precede the rollout

For engineering depth beyond the exam, see the repo's [AI security](../../../../resources/ai-security/) material.

---

## Key terms

- **Managed identity** - an Entra ID identity Azure manages for a resource, removing stored credentials from application code
- **Workload identity federation** - trust configuration letting external workloads such as GitHub Actions obtain Entra tokens without a stored secret
- **Sensitivity label** - a Purview classification that applies protection travelling with the file, including encryption and access restriction
- **Auto-labeling** - Purview policy applying sensitivity labels automatically based on classifiers rather than user action
- **Data loss prevention** - policy that inspects activity and blocks or warns when classified data crosses a defined boundary
- **DSPM for AI** - Purview capability giving visibility into sensitive data touched by AI interactions
- **Customer-managed key** - an encryption key you control in Key Vault or Managed HSM, enabling revocation and crypto-shredding
- **Managed HSM** - single-tenant, FIPS 140-2 Level 3 validated hardware security module service
- **Crypto-shredding** - rendering data unrecoverable by destroying the customer-managed key that protects it
- **Always Encrypted** - SQL feature keeping data encrypted from the database engine and privileged operators, with keys held by the client
- **Dynamic data masking** - presentation-layer obfuscation of query results, not a security boundary
- **Row-level security** - SQL predicate-based restriction limiting which rows a given user context can read
- **Prompt Shields** - Azure AI Content Safety capability detecting direct jailbreak and indirect document-based prompt injection
- **Defender for DevOps** - Defender for Cloud capability surfacing code, secret, and IaC findings from GitHub and Azure DevOps

---

## Related

- [Notes 01: security strategy and frameworks](./01-security-strategy-and-frameworks.md)
- [Scenarios](../scenarios.md) - scenario 6 exercises this domain
- [SC-401 Information Security Administrator](../../sc-401/) - Purview at implementation depth
- [AI security](../../../../resources/ai-security/) - engineering depth on securing AI workloads
- [AI security topic](../../../../topics/ai-security.md)
