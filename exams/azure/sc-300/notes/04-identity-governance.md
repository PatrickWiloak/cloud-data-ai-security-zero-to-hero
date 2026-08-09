---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 11 min
---

# 04 - Identity governance

**Domain 4: Plan and implement identity governance (20-25%)**

Governance answers four questions: who should have access, do they still need it, how do they get it, and can you prove any of that.

---

## Entitlement management

The request-and-approve layer.

| Object | Purpose |
|---|---|
| **Catalog** | A container grouping resources that can be offered together, with its own owners |
| **Access package** | A bundle of resources (groups, applications, SharePoint sites) offered as one request |
| **Policy** | Who can request the package, who approves, how long access lasts, and what happens at expiry |

Capabilities the exam tests:
- Multi-stage approval, including approval by the requester's manager
- Expiry and extension, with a renewal request path
- **Separation of duties**: an access package can be configured as incompatible with another package or group, blocking a request that would create a toxic combination
- External users can request packages, with a governed lifecycle including automatic account removal at the end

Choose an access package when the requirement mentions request, approval, bundling, or expiry. Choose a plain group when access is simply assigned.

---

## Access reviews

The recertification layer. Reviews can target group membership, application assignment, Entra role assignment, Azure resource role assignment, and access package assignment.

Configuration to know:
- **Reviewers**: the resource owner, the group owner, selected users, the users themselves (self-review), or the manager
- **Frequency**: one-time or recurring
- **Auto-apply results**: changes take effect automatically at the end
- **If reviewers do not respond**: no change, remove access, approve access, or take system recommendations. "Remove access" is the answer when the requirement says access must lapse without positive recertification
- **Decision helpers**: last sign-in information surfaced to reviewers

---

## Lifecycle workflows

Automates joiner, mover, and leaver tasks against attribute triggers such as employee hire date or leave date.

Tasks include sending a welcome email, generating a Temporary Access Pass, adding to or removing from groups and access packages, disabling the account, removing all licences, and deleting the user.

Requires Entra ID Governance licensing. The typical exam use is "automatically disable the account and remove all access on the employee's last day, without manual intervention".

---

## Privileged Identity Management

Just-in-time privileged access for Entra roles, Azure resource roles, and groups.

| Concept | Meaning |
|---|---|
| **Eligible** | The user may activate the role but does not hold it by default |
| **Active** | The user holds the role now; may still be time-bound |
| **Activation** | The act of elevating, with optional MFA, justification, ticket number, and approval |
| **PIM for Groups** | Making membership of a group itself eligible, which extends just-in-time to anything the group grants |

Settings per role: maximum activation duration, whether MFA is required, whether justification and approval are required, who approves, and notification recipients.

**PIM alerts** flag conditions such as too many Global Administrators, roles assigned outside PIM, and accounts not using MFA.

**PIM access reviews** recertify who is even eligible, which is a separate control from activation.

Requires Entra ID P2.

---

## Terms of use

A document users must accept, enforced through a Conditional Access grant control. Supports per-language documents, expiry and re-acceptance schedules, and reporting on who accepted what and when. Useful for contractor and guest scenarios where acceptance must be evidenced.

---

## Monitoring and reporting

| Log | Contains |
|---|---|
| **Sign-in logs** | Interactive and non-interactive sign-ins, service principal sign-ins, managed identity sign-ins, with Conditional Access policy results |
| **Audit logs** | Directory changes: who changed what object, when |
| **Provisioning logs** | SCIM provisioning activity and failures |
| **Risky users and risky sign-ins** | Identity Protection detections |

Retention in the portal is limited (typically 30 days on premium tiers), so any requirement mentioning longer retention or correlation means **diagnostic settings** exporting to a Log Analytics workspace, a storage account for archive, or an Event Hub for third-party SIEM. From Log Analytics the data is available to Microsoft Sentinel and to workbooks.

**Entra Permissions Management** provides CIEM across Azure, AWS, and GCP, reporting the Permission Creep Index: the gap between permissions granted and permissions actually used.

---

## Key terms

- **Access package** - a bundle of groups, applications, and sites offered through a request and approval workflow with an expiry
- **Catalog** - the entitlement management container that groups resources and delegates their administration
- **Separation of duties** - configuration preventing a user from holding two incompatible access packages or groups at once
- **Access review** - a recurring recertification of access with configurable reviewers and automatic application of results
- **Auto-apply results** - the access review setting that enacts reviewer decisions without an administrator applying them manually
- **Lifecycle workflow** - automated joiner, mover, and leaver tasks triggered by user attributes such as hire or leave date
- **Eligible assignment** - a PIM assignment allowing a user to activate a role rather than holding it permanently
- **Activation** - the PIM act of elevating into a role, optionally requiring MFA, justification, and approval
- **PIM for Groups** - extending just-in-time activation to membership of a group, and therefore to everything the group grants
- **Terms of use** - a document enforced through Conditional Access that users must accept before access is granted
- **Diagnostic settings** - the configuration exporting Entra logs to Log Analytics, storage, or Event Hubs for retention and analysis
- **Permission Creep Index** - Permissions Management's measure of the gap between permissions granted and permissions used

---

## Related

- [Notes 01: identities and tenant configuration](./01-identities-and-tenant.md)
- [Scenarios](../scenarios.md) - scenarios 1 and 8
- [SC-100](../../sc-100/) - governance as a design decision
- [Identity and IAM topic](../../../../topics/iam.md)
