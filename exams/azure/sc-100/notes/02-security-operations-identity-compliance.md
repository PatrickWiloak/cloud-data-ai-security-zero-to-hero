---
last-updated: 2026-08-09
difficulty: advanced
reading-time: 16 min
---

# 02 - Security operations, identity, and compliance

**Domain 2: Design security operations, identity, and compliance capabilities (30-35%)**

The largest domain. Identity design and SOC design, plus the compliance capabilities that sit on top of both.

---

## Identity architecture

### Tenant design

One tenant is the default. Multiple tenants appear after acquisitions or where regulatory separation is mandatory. Multi-tenant estates are operationally expensive, so exam answers usually favour **Azure Lighthouse** for cross-tenant management and **B2B collaboration** for cross-tenant access over tenant consolidation projects.

External identity options:

- **B2B collaboration** - invite external users as guests into your tenant. Default for partner and contractor access.
- **B2B direct connect** - trust relationship for Teams shared channels.
- **External ID for customers (CIAM)** - consumer-facing identity, formerly B2C.
- **Cross-tenant access settings** - govern which external tenants can collaborate, and whether MFA claims from the home tenant are trusted.

### Hybrid identity

| Method | How it works | Choose when | Cost |
|---|---|---|---|
| **Password hash sync** | Hash of the password hash syncs to Entra ID | Default. Most resilient, simplest | Cloud auth survives on-prem outage |
| **Pass-through authentication** | Lightweight agents validate against on-prem AD | Policy forbids any hash in cloud | Sign-in depends on connector availability |
| **Federation (AD FS)** | On-prem STS issues tokens | Smart card, third-party MFA, or specific claims rules required | Most infrastructure; Microsoft steers away from it |

Password hash sync also enables **leaked credential detection** in Identity Protection, which PTA and federation do not, and provides a fallback during on-premises outages when configured alongside them.

### Conditional Access

The policy engine. Signals in, controls out.

**Signals**: user or group, cloud app or action, device platform and state, location and named locations, client app, sign-in risk, user risk, authentication context, and filters for devices and apps.

**Controls**: block, require MFA, require compliant or hybrid-joined device, require approved client app, require app protection policy, require terms of use, require password change, and session controls (sign-in frequency, persistent browser, Conditional Access App Control, token protection).

Design rules the exam expects:

- Always exclude at least two **break-glass accounts** from every policy, cloud-only, with long complex passwords or FIDO2 keys, monitored by alerts.
- Use **report-only mode** before enforcing.
- Prefer **named locations** and device filters over IP allowlisting alone.
- Conditional Access evaluates **after** primary authentication, so it cannot prevent a credential from being validated, only what the resulting session may do.

### Privileged access

**Privileged Identity Management (PIM)** provides eligible assignments, just-in-time activation, approval workflows, time-bound access, justification, and activation alerts. It covers Entra roles, Azure resource roles, and PIM for Groups.

**The enterprise access model** separates the control plane (identity systems, Tier 0), the management plane, and the data and workload plane. The design consequence: administrative accounts for one plane must not be usable in a lower-trust plane, and privileged access should originate from a **privileged access workstation**.

Design a privileged path: separate admin accounts, cloud-only for cloud roles, phishing-resistant MFA, PIM eligibility, PAW for the session, and access reviews for the assignments.

### Identity governance

- **Entitlement management** - access packages bundling groups, apps, and SharePoint sites with an approval workflow and expiry. The answer for contractor and project-based access at scale.
- **Access reviews** - recurring recertification of group membership, app assignment, and role assignment, with auto-remove on no response.
- **Lifecycle workflows** - automated joiner, mover, and leaver tasks.
- **Permissions Management** - CIEM across Azure, AWS, and GCP, reporting the gap between granted and used permissions.

---

## Security operations design

### Defender XDR vs Sentinel

| | Defender XDR | Microsoft Sentinel |
|---|---|---|
| Scope | Microsoft workloads: endpoint, identity, email, SaaS, cloud | Any source, including third-party and on-premises |
| Function | Correlated detection and automated response | SIEM plus SOAR: long retention, custom analytics, hunting |
| Cost model | Per-user or per-workload licensing | Per GB ingested plus retention |
| When it is enough | Microsoft-only estate, standard detections | Third-party sources, custom rules, compliance retention, cross-cloud |

The two integrate: Defender XDR incidents flow into Sentinel through a connector, and the unified portal presents them together. A frequent exam answer is "use Defender XDR alone" when the estate is Microsoft-only and cost is a constraint.

### Sentinel architecture

- **Workspace strategy**: driven by data residency and tenancy, not by subscription count. Fewer workspaces are cheaper and easier to hunt across; residency and tenant boundaries force splits.
- **Cross-workspace queries** and **workspace manager** let one SOC operate across several.
- **Azure Lighthouse** enables cross-tenant SOC operations without migrating identities.
- **Cost levers**: which connectors are enabled, table-level retention, Basic and Auxiliary log tiers for high-volume low-value tables, archive tier for long retention, and commitment tiers for predictable volume.
- **Content**: analytics rules (scheduled, NRT, anomaly, threat intelligence), watchlists, workbooks, hunting queries, and playbooks built on Logic Apps.

### Logging strategy

Decide per source: what to collect, where to send it, how long to keep it interactive, and how long to archive.

Key sources: Entra ID sign-in and audit logs, Azure Activity Log, resource diagnostic settings, Defender alerts, Microsoft 365 audit, network flow logs, and DNS.

Retention design must satisfy the longest applicable requirement, which is usually regulatory rather than operational. Archive tier plus search jobs is the cost-efficient shape for long retention.

---

## Compliance capabilities

- **Purview Compliance Manager** - assessments per regulation, improvement actions, and a compliance score. The workflow and evidence layer.
- **Azure Policy initiatives** - the enforcement layer. Regulatory initiatives (ISO 27001, PCI DSS, NIST SP 800-53, CIS) assigned at management group scope.
- **Defender for Cloud regulatory compliance dashboard** - the reporting layer showing control state across connected environments including AWS and GCP.
- **Azure Blueprints is deprecated**; use **Template Specs and Deployment Stacks** with Azure Policy for repeatable governed deployments.

---

## Key terms

- **Conditional Access** - Entra ID policy engine that evaluates signals at sign-in and applies access controls such as MFA or device compliance requirements
- **Break-glass account** - an emergency cloud-only administrative account excluded from Conditional Access policies to prevent lockout
- **PIM** - Privileged Identity Management, providing just-in-time, time-bound, approval-gated activation of privileged roles
- **Entitlement management** - Entra ID Governance capability bundling resources into access packages with request, approval, and expiry workflows
- **Access review** - a recurring recertification of access assignments that can automatically remove access when reviewers do not respond
- **Password hash sync** - hybrid identity method syncing a hash of the on-premises password hash to Entra ID, enabling cloud authentication and leaked credential detection
- **Pass-through authentication** - hybrid identity method validating passwords against on-premises AD through lightweight agents, storing no hash in the cloud
- **Azure Lighthouse** - delegated resource management enabling cross-tenant administration without migrating identities
- **Defender XDR** - Microsoft's extended detection and response platform correlating signals across endpoint, identity, email, SaaS, and cloud
- **Analytics rule** - a Sentinel detection that queries ingested data on a schedule or in near real time and raises incidents
- **Basic and Auxiliary logs** - lower-cost Sentinel ingestion tiers for high-volume tables with reduced query capability
- **Permissions Management** - Microsoft's CIEM product reporting granted versus used permissions across Azure, AWS, and GCP
- **Cross-tenant access settings** - Entra ID configuration governing which external tenants may collaborate and whether their MFA claims are trusted

---

## Related

- [Notes 03: infrastructure security design](./03-infrastructure-security-design.md)
- [Scenarios](../scenarios.md) - scenarios 2, 3, and 7 exercise this domain
- [SC-300](../../sc-300/) - identity at implementation depth
- [SC-200](../../sc-200/) - security operations at implementation depth
- [Identity and IAM topic](../../../../topics/iam.md)
