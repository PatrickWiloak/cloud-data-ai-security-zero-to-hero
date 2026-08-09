---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 10 min
---

# 04 - Manage and secure Power BI

**Domain 4: Manage and secure Power BI (15-20%)**

The smallest domain and the one most often under-studied, which makes it good value.

---

## Workspaces and roles

| Role | Can |
|---|---|
| **Admin** | Everything: delete the workspace, manage access, publish and update apps |
| **Member** | Add members at Member and below, publish and update apps, share content |
| **Contributor** | Create, edit, and delete content, schedule refresh; **cannot publish an app** |
| **Viewer** | View and interact only; **row-level security applies** |

The two facts most often tested: Contributor cannot publish an app, and RLS applies only to Viewers. Anyone with Contributor or above sees all rows in the workspace regardless of RLS roles, which is why RLS must be validated through the app or as a real Viewer.

---

## Distribution

| Method | Use when |
|---|---|
| **App** | Broad distribution. Supports **audiences**, so different groups see different content from one app |
| **Workspace access** | Authors and collaborators |
| **Direct share** | One-off sharing of a report or dashboard; hard to govern at scale |
| **Sharable link** | Convenient, with options for people in the organization, people with existing access, or specific people |
| **Embed** | In Teams, SharePoint, or a custom application |

Publishing an app separates what consumers see from what authors are working on. Until the app is republished, edits in the workspace do not reach consumers, which is the main operational reason to use apps.

---

## Licensing

| Licence | Gives |
|---|---|
| **Free** | Personal use in My Workspace; can consume content hosted on Premium or Fabric capacity |
| **Pro** | Publish and share, consume shared content in shared capacity |
| **Premium Per User (PPU)** | Pro plus premium features for that user; consumers also need PPU |
| **Fabric / Premium capacity** | Dedicated capacity; free users can consume content in workspaces on that capacity |

Licensing is a frequent hidden constraint in distribution questions. If content must reach many free users, it has to sit on a Fabric or Premium capacity.

---

## Refresh

- **Scheduled refresh** on Import and composite models, with a frequency limit that depends on license and capacity
- **Gateway** required for on-premises and some private sources
- **Credentials** stored per data source and per gateway
- **Refresh failures** commonly come from expired credentials, gateway offline, source schema changes, or timeouts
- **Incremental refresh** reduces duration; see [notes 01](./01-prepare-the-data.md)
- **Refresh history** is the first diagnostic stop

---

## Security in the service

- **Row-level security**: roles are defined in Desktop, members are assigned in the service. Test as a Viewer.
- **Object-level security**: hides tables and columns from a role.
- **Sensitivity labels** from Microsoft Purview apply to Power BI content and flow through to exported files, which is where [SC-401](../../sc-401/) material connects.
- **Tenant settings** in the admin portal govern export, sharing with external users, publish to web, and custom visuals. Publish to web makes content publicly accessible on the internet and is a common misconfiguration.
- **Service principals** for automation, where supported by tenant settings.

---

## Lifecycle management

**Deployment pipelines** move content through Development, Test, and Production stages.

- Content is compared between stages and deployed selectively
- **Deployment rules** swap data source parameters and connection details per stage, so production points at production data
- Requires Premium Per User or capacity

**Version control and Git integration** in Fabric workspaces allows source control for Power BI items.

**Endorsement** signals trust: **Promoted** by content owners, **Certified** by designated reviewers under a tenant policy. Certified content surfaces preferentially in discovery.

---

## Monitoring

- **Usage metrics** per report: views, viewers, distribution method
- **Audit log** through Purview or the admin portal, covering activity across the tenant
- **Capacity metrics app** for Premium and Fabric capacity utilization, throttling, and slow items
- **Lineage view** in the workspace showing sources, dataflows, semantic models, reports, and dashboards and their dependencies
- **Impact analysis** before changing a semantic model, showing which downstream reports are affected

---

## Key terms

- **Workspace** - the collaboration container holding semantic models, reports, dashboards, and other Fabric items
- **Contributor** - the workspace role that can create and edit content but cannot publish an app
- **Viewer** - the workspace role limited to viewing and interacting, and the only role to which row-level security applies
- **App** - the packaged, governed distribution of workspace content to consumers, supporting multiple audiences
- **Audience** - an app configuration presenting different content to different groups from a single app
- **Premium Per User** - the per-user license granting premium capabilities without dedicated capacity
- **Deployment pipeline** - the Development, Test, and Production promotion mechanism for Power BI and Fabric content
- **Deployment rule** - a pipeline configuration swapping data sources or parameters as content moves between stages
- **Endorsement** - the Promoted or Certified trust signal applied to content, with Certified governed by tenant policy
- **Lineage view** - the workspace visualization of dependencies from source through model to report
- **Impact analysis** - the report of downstream items affected by a change to a semantic model
- **Publish to web** - the tenant setting that makes content publicly accessible on the internet, a common misconfiguration
- **Capacity metrics app** - the monitoring application reporting Fabric or Premium capacity utilization and throttling

---

## Related

- [Notes 01: prepare the data](./01-prepare-the-data.md)
- [Scenarios](../scenarios.md) - scenario 7
- [DP-600 Fabric Analytics Engineer](../../dp-600/)
- [SC-401](../../sc-401/) - sensitivity labels applied to Power BI content
