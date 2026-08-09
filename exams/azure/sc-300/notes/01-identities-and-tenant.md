---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 11 min
---

# 01 - Identities and tenant configuration

**Domain 1: Implement and manage user identities (20-25%)**

---

## Tenant fundamentals

A Microsoft Entra tenant is a dedicated instance of the directory. It is the boundary for users, groups, applications, and policy. One organization can hold several tenants, usually after an acquisition or where regulatory separation demands it.

Tenant-level settings that appear on the exam: company branding, user settings (who can register applications, who can create tenants, restrict access to the administration portal), external collaboration settings, and the properties blade including the technical and security contacts.

---

## Users

| User type | Meaning |
|---|---|
| **Member** | Belongs to this organization, full default directory permissions |
| **Guest** | Invited external identity, restricted default permissions |

Source of authority matters: a user created in the cloud is editable in Entra ID, a user synced from Active Directory is mastered on-premises and most attributes are read-only in the cloud.

**Bulk operations**: create, invite, delete, and download users through CSV. The exam tends to ask which operations support bulk rather than the CSV format.

---

## Groups

| Dimension | Options |
|---|---|
| Type | Security, Microsoft 365 |
| Membership | Assigned, dynamic user, dynamic device |
| Source | Cloud, synced from on-premises |

**Dynamic membership** uses a rule against user or device attributes:

```text
(user.department -eq "Finance") and (user.country -eq "DE")
(user.extensionAttribute1 -eq "contractor")
(device.deviceOSType -eq "Windows") and (device.isCompliant -eq true)
```

Constraints worth knowing: a group is either assigned or dynamic, never both; a dynamic group cannot have a rule based on membership of another group; evaluation is not instantaneous; and synced groups cannot be made dynamic in the cloud.

**Group-based licensing** assigns licenses by group membership, with reconciliation when a user joins or leaves. If licenses run out, new members enter an error state rather than silently going unlicensed.

---

## Administrative units

An administrative unit scopes a role assignment to a subset of the directory: specific users, groups, or devices. The pattern is a regional or business-unit helpdesk that can reset passwords only for its own users.

Key points:
- Roles are assigned **over** an administrative unit, not inside it
- Not every role supports administrative unit scoping
- Restricted management administrative units prevent even tenant-level admins from modifying members, which supports separation of duties for sensitive accounts

---

## Roles

Entra ID roles govern the directory. Azure RBAC roles govern Azure resources. They are separate systems, and a Global Administrator does not automatically have Azure resource access unless they elevate through the "Access management for Azure resources" toggle.

Roles you should be able to select correctly:

| Role | Can | Cannot |
|---|---|---|
| **Global Administrator** | Everything | - |
| **User Administrator** | Manage users and groups, reset passwords for non-admins | Reset credentials for privileged roles |
| **Groups Administrator** | Manage all groups | Manage users |
| **Authentication Administrator** | Manage authentication methods for non-admin users | Act on users holding privileged roles |
| **Privileged Authentication Administrator** | Manage authentication methods for any user including admins | - |
| **Application Administrator** | Manage all applications and consent | Manage the directory generally |
| **Cloud Application Administrator** | As above, excluding Application Proxy | - |
| **Conditional Access Administrator** | Manage Conditional Access policies | Manage users |
| **Privileged Role Administrator** | Manage role assignments and PIM settings | - |
| **Security Reader** | Read security features | Change anything |

**Custom roles** are available for application management scenarios; the exam expects you to reach for a built-in role first.

---

## Hybrid identity

**Entra Connect Sync** is the full-featured synchronization engine, installed on a Windows server. It supports device writeback, password writeback, exchange hybrid, and complex filtering and transformation.

**Entra Cloud Sync** is a lightweight agent-based alternative, managed from the cloud, supporting multiple disconnected forests and simpler deployment. It has grown considerably but still does not cover every Connect Sync scenario.

Choose Cloud Sync for simple, multi-forest, or agent-only scenarios; choose Connect Sync where you need transformation rules, device writeback, or Exchange hybrid features.

**Password writeback** is what makes SSPR work for synced users. Without it, a reset changes only the cloud password.

---

## Device identity

| State | Meaning | Enables |
|---|---|---|
| **Entra registered** | Personal device with a work account added | Conditional Access device state, limited |
| **Entra joined** | Cloud-only organizational device | SSO to cloud, Windows Hello for Business, compliance |
| **Hybrid Entra joined** | Domain-joined and registered in Entra | Cloud SSO while retaining on-premises Group Policy |

Device compliance is evaluated by Intune and consumed by Conditional Access as a grant control.

---

## External identities

- **B2B collaboration** - invite external users as guests. Governed by external collaboration settings and cross-tenant access settings.
- **Cross-tenant access settings** - inbound and outbound access per partner tenant, plus trust settings that let you accept MFA and device claims from the partner's tenant rather than forcing re-registration.
- **B2B direct connect** - a trust for Teams shared channels without guest objects.
- **External ID for customers (CIAM)** - consumer identity with user flows, custom branding, and social identity providers.

Guest default permissions should be set to the most restrictive option unless a specific application requires directory reads.

---

## Key terms

- **Tenant** - a dedicated instance of Microsoft Entra ID that acts as the boundary for identities, applications, and policy
- **Administrative unit** - a directory container that scopes a role assignment to a subset of users, groups, or devices
- **Restricted management administrative unit** - an administrative unit whose members cannot be modified even by tenant-level administrators
- **Dynamic group** - a group whose membership is computed from an attribute rule rather than assigned manually
- **Group-based licensing** - assigning product licenses through group membership with automatic reconciliation
- **Entra Connect Sync** - the full-featured server-based directory synchronization engine supporting writeback and transformation
- **Entra Cloud Sync** - the lightweight cloud-managed synchronization agent supporting multiple disconnected forests
- **Password writeback** - the capability that pushes a cloud password change back to on-premises Active Directory
- **Entra joined** - a device joined directly to Entra ID with no on-premises domain membership
- **Hybrid Entra joined** - a device joined to on-premises Active Directory and registered in Entra ID
- **B2B collaboration** - inviting external users into your tenant as guest objects
- **Cross-tenant access settings** - per-partner configuration of inbound and outbound collaboration and claim trust
- **Privileged Authentication Administrator** - the role able to manage authentication methods for users who hold privileged roles

---

## Related

- [Notes 02: authentication and Conditional Access](./02-authentication-and-conditional-access.md)
- [Scenarios](../scenarios.md) - scenarios 3 and 5
- [IAM explained](../../../../learn/concepts/iam-explained.md)
