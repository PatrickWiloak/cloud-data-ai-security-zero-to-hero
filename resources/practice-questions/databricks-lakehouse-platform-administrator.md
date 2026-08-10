---
last-updated: 2026-08-09
difficulty: intermediate
---

# Databricks Certified Lakehouse Platform Administrator - Practice Questions

15 questions for this exam, weighted toward workspace administration (30%) and identity and access (25%), then data management (20%), cluster and warehouse management (15%), and security (10%).

> **Cert page:** [exams/databricks/lakehouse-platform-administrator/](../../exams/databricks/lakehouse-platform-administrator/)

---

### Question 1
**Scenario:** Users, groups, and service principals must be managed once across all workspaces.

A. Per-workspace user lists
B. Account-level identity federation, with SCIM provisioning from the identity provider and groups assigned to workspaces
C. Manual creation in each workspace
D. Shared accounts

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Account-level identities plus SCIM mean joiners and leavers are handled by the IdP, which is what makes deprovisioning reliable. Per-workspace user management guarantees that someone who left last quarter still has access somewhere.
</details>

---

### Question 2
**Scenario:** Data governance must span workspaces with a single permission model.

A. Table ACLs per workspace
B. Unity Catalog, with a metastore per region and a three-level `catalog.schema.table` namespace
C. Cloud storage IAM only
D. Notebook permissions

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Unity Catalog sits above workspaces, so one grant applies everywhere the catalog is attached, and it adds lineage and audit. Storage IAM cannot express table, column, or row scope, and the legacy Hive metastore is per-workspace by design.
</details>

---

### Question 3
**Scenario:** Unity Catalog must access cloud storage without embedded credentials.

A. Access keys in the cluster configuration
B. A storage credential (using a managed identity or IAM role) plus an external location defining the path scope
C. Public buckets
D. Per-user credentials

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The storage credential holds the cloud identity and the external location binds it to a path prefix, so grants are made on the location rather than distributing keys. Cluster-level keys give everyone on the cluster the same access, which defeats fine-grained governance.
</details>

---

### Question 4
**Scenario:** Costs must be attributed to teams.

A. One shared cluster with no tags
B. Cluster policies enforcing tags, plus system tables and budget alerts for per-team reporting
C. Estimate from headcount
D. Split evenly

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Tags must be enforced at creation or coverage decays, which is exactly what a cluster policy does by requiring or fixing tag values. System tables then provide the usage data to report on, and budgets alert before the invoice arrives.
</details>

---

### Question 5
**Scenario:** Users keep creating oversized clusters.

A. Ask them not to
B. Cluster policies constraining instance types, node counts, autotermination, and enabling autoscaling
C. Delete clusters manually
D. Remove cluster creation entirely

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Policies set guardrails rather than removing capability, so users keep self-service within bounds you defined. Enforcing autotermination is usually the single biggest saving, because idle clusters are the largest avoidable cost in most workspaces.
</details>

---

### Question 6
**Scenario:** SQL analysts need low-latency queries with automatic scaling.

A. An all-purpose cluster
B. A SQL warehouse, ideally serverless, with autostop and scaling configured
C. A job cluster
D. A single node

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SQL warehouses are optimized for concurrent short queries with result caching, and serverless removes start-up latency. All-purpose clusters are for notebook development and behave badly as a shared BI backend.
</details>

---

### Question 7
**Scenario:** Notebook results containing sensitive data must not be visible to all workspace users.

A. Trust users
B. Restrict access with workspace object permissions, apply Unity Catalog grants to the underlying data, and consider disabling result downloads
C. Delete notebooks
D. Use a single admin account

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Two layers matter: who can open the notebook, and who can read the data it queries. Getting only the first right leaves the data reachable from any other notebook, which is why data-layer grants are the durable control.
</details>

---

### Question 8
**Scenario:** An audit must show who queried a sensitive table last month.

A. Cluster logs
B. Unity Catalog audit logs and system tables, which record query and access events with the principal
C. Notebook revision history
D. Driver logs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Audit logs record the identity, action, and object at the governance layer, independent of which compute ran it. Cluster and driver logs show execution detail without the governed object identity, which is not what an access audit needs.
</details>

---

### Question 9
**Scenario:** A workspace must not be reachable from the public internet.

A. Strong passwords
B. Network configuration: private connectivity to the control plane, IP access lists, and no public IPs on compute
C. A firewall on the laptop
D. Disable the UI

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Network isolation covers three paths: how users reach the workspace, how the control plane reaches compute, and how compute reaches storage and external services. Address all three, since leaving any one public undermines the other two.
</details>

---

### Question 10
**Scenario:** A table's data must be deleted to satisfy a data subject request.

A. Delete and rely on time travel expiring
B. Delete the rows, then `VACUUM` with an appropriate retention so the underlying files are removed, and confirm no clones or shares retain them
C. Drop the table
D. Overwrite the file

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Delta deletes are logical until VACUUM removes the files, so time travel would still expose the data. Shallow clones and Delta Sharing recipients are the two places people forget, and both must be checked before declaring the deletion complete.
</details>

---

### Question 11
**Scenario:** Data must be shared with an external organization without copying it.

A. Export to CSV and email
B. Delta Sharing, with recipients granted access to specific shares
C. Grant workspace access
D. A public bucket

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Delta Sharing is an open protocol that lets recipients read live data without duplicating it or joining your platform, with revocable, auditable grants. Exports create uncontrolled copies that outlive the relationship.
</details>

---

### Question 12
**Scenario:** A workspace admin must delegate catalog administration to a data team.

A. Grant account admin
B. Grant the specific catalog's ownership or `USE CATALOG` and management privileges to a group, keeping account admin narrow
C. Share credentials
D. Grant metastore admin to everyone

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Unity Catalog privileges are delegable per securable, so a team owns its catalog without gaining rights over others. Metastore admin is the powerful role that should stay with a small platform team.
</details>

---

### Question 13
**Scenario:** Jobs are failing after a runtime upgrade.

A. Roll back everything permanently
B. Pin runtime versions for production jobs, test upgrades against a staging environment, and adopt LTS releases for stability
C. Always use the newest runtime
D. Ignore the failures

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Runtime upgrades change library versions and can change behavior, so production jobs should pin a version and move deliberately. LTS releases have longer support windows, which reduces how often you must run that migration.
</details>

---

### Question 14
**Scenario:** Secrets must be available to jobs without appearing in notebooks.

A. Hard-code them
B. Databricks secret scopes (optionally backed by a cloud key vault), referenced through `dbutils.secrets`, with redaction in output
C. Environment variables in the notebook
D. A config table

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Secret scopes keep values out of code and out of revision history, and Databricks redacts them from notebook output if printed. Backing the scope with a cloud key vault centralizes rotation with the rest of the organization's secrets.
</details>

---

### Question 15
**Scenario:** Storage costs are growing from old table versions and unused data.

A. Delete files manually
B. Run `VACUUM` on a schedule with an appropriate retention, review table retention requirements, and drop or archive unused tables
C. Increase the storage quota
D. Disable Delta

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Retention is a policy decision before it is a cleanup task: the window has to satisfy both concurrent readers and any recovery requirement. Deleting files directly from storage corrupts tables, because the transaction log still references them.
</details>

---

## Where to go deeper

- [Lakehouse Platform Administrator cert page](../../exams/databricks/lakehouse-platform-administrator/) - notes, practice plan, strategy
- [Data Engineer Professional practice questions](./databricks-data-engineer-professional.md) - the pipelines this platform runs
- [Cloud cost basics](../../learn/concepts/cloud-cost-basics.md) - the cost domain in plain English
- **[📖 Databricks certification](https://www.databricks.com/learn/certification)** - official exam guides
