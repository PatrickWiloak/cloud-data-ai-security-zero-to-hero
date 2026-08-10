---
last-updated: 2026-08-09
difficulty: beginner
---

# Salesforce Certified Administrator - Practice Questions

15 questions across the administrator exam's main areas: configuration and setup, object manager and Lightning App Builder, process automation, data and analytics management, and the sales and service applications.

> **Cert page:** [exams/salesforce/administrator/](../../exams/salesforce/administrator/)

---

### Question 1
**Scenario:** A user must see only their own records on a custom object, while their manager sees the whole team's.

A. Set the object's organization-wide default to Public Read/Write
B. Set the organization-wide default to Private and enable Grant Access Using Hierarchies
C. Create a permission set
D. Use field-level security

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Sharing is built from the most restrictive baseline upward: the organization-wide default sets the floor, and role hierarchy, sharing rules, manual sharing, and teams open it back up. Field-level security controls which fields are visible, not which records.
</details>

---

### Question 2
**Scenario:** A field must be hidden from one group of users but visible to another.

A. Page layouts alone
B. Field-level security via profiles or permission sets
C. Record types
D. Validation rules

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Removing a field from a page layout hides it from that layout only; it remains reachable through reports, the API, and list views. Field-level security is the enforced control, applied at the data layer.
</details>

---

### Question 3
**Scenario:** Additional permissions must be granted to a handful of users without cloning their profile.

A. Create a new profile
B. Assign a permission set, or a permission set group for a bundle of related access
C. Change the role
D. Change the organization-wide default

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Permission sets are additive and prevent profile proliferation, which is why Salesforce's guidance is a minimum-access profile plus permission sets. Permission set groups bundle several sets for a persona, with muting available to remove specific permissions from the group.
</details>

---

### Question 4
**Scenario:** Two divisions need different picklist values and page layouts on the same object.

A. Two custom objects
B. Record types, each with its own picklist value sets and page layout assignments
C. Two profiles
D. Field dependencies

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Record types partition a single object into business variants and drive both layout and picklist behavior per profile. Duplicating the object would split reporting and duplicate every piece of automation.
</details>

---

### Question 5
**Scenario:** Which automation tool should be used for new declarative automation?

A. Workflow Rules
B. Flow Builder, which Salesforce has consolidated automation into
C. Process Builder
D. Apex triggers

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Workflow Rules and Process Builder are retired for new automation and existing ones should be migrated. Flow covers record-triggered, screen, scheduled, and autolaunched cases, and record-triggered flows split into before-save (fast field updates on the same record) and after-save (related records and external actions).
</details>

---

### Question 6
**Scenario:** A value must be prevented from being saved when it fails a business rule.

A. A validation rule that evaluates to true when the data is invalid
B. A workflow rule
C. A formula field
D. A required field on the page layout

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The logic is inverted from how people read it: the rule's formula returning true is what blocks the save and shows the error. Validation rules also fire on API and data loader inserts, which page-layout requirements do not.
</details>

---

### Question 7
**Scenario:** A relationship must cascade delete children when the parent is deleted and support roll-up summaries.

A. A lookup relationship
B. A master-detail relationship
C. A hierarchical relationship
D. An external lookup

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Master-detail children are owned by the parent: they inherit its sharing, have no owner field, and are deleted with it, which is also what makes roll-up summary fields possible. Lookups are loose, optional, and do not cascade.
</details>

---

### Question 8
**Scenario:** Duplicate accounts are being created by users.

A. A validation rule
B. Duplicate rules with matching rules, set to alert or block on create and edit
C. Data Loader
D. A report

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A matching rule defines what counts as a duplicate, fuzzy matching included, and the duplicate rule defines what happens when one is found. Alert with a bypass is common for sales teams, since a hard block on a fuzzy match creates its own problem.
</details>

---

### Question 9
**Scenario:** A report must show accounts with no related opportunities.

A. A standard report
B. A cross filter with "without" on the Opportunities object
C. A summary report
D. A joined report

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cross filters express the "with or without related records" question that a plain filter cannot. The report type also matters: `Accounts with Opportunities` returns only accounts that have them, so the base type must include accounts without opportunities.
</details>

---

### Question 10
**Scenario:** 50,000 records must be updated from a spreadsheet.

A. Manual entry
B. Data Loader (or the Data Import Wizard below its 50,000-record limit), with the record IDs or an external ID for matching
C. A report
D. A flow

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The Import Wizard handles up to 50,000 records for a subset of objects and does not support deletes; Data Loader handles larger volumes, all objects, and every operation. An external ID field lets you upsert without knowing Salesforce record IDs.
</details>

---

### Question 11
**Scenario:** Sales users must follow a defined selling process with different stages per business line.

A. One set of stages for everyone
B. Sales processes tied to record types, each exposing its own subset of opportunity stages
C. Validation rules
D. Path only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A sales process selects which stage values a record type offers, and Path then adds guidance and key fields on top for each stage. Path is a user-experience layer, not the control over which stages exist.
</details>

---

### Question 12
**Scenario:** Cases must route to the right support queue automatically.

A. Manual assignment
B. Case assignment rules with ordered entry criteria, assigning to a queue or user
C. Escalation rules
D. Auto-response rules

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Assignment rules evaluate entries in order and stop at the first match, so ordering is the design decision. Escalation rules act on age and inactivity later in the case lifecycle, and auto-response rules only send email.
</details>

---

### Question 13
**Scenario:** A user reports they cannot see a field they were told they have access to.

A. Change the organization-wide default
B. Check field-level security on the profile and permission sets, then the page layout assignment for their record type and profile
C. Give them the System Administrator profile
D. Recreate the field

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Field visibility is the intersection of field-level security and the assigned layout, so the troubleshooting order is security first, layout second. Granting administrator rights to fix a visibility complaint replaces a small problem with a large one.
</details>

---

### Question 14
**Scenario:** Changes must move from a sandbox to production safely.

A. Rebuild them manually in production
B. Change sets, or a source-driven pipeline with SFDX and version control for larger teams
C. Data Loader
D. Edit production directly

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Change sets are declarative and adequate for small changes, but they carry no version history and are one-directional. Source-driven development with a repository is what makes releases reviewable and repeatable as the team grows.
</details>

---

### Question 15
**Scenario:** Data must be recoverable after a bad bulk update.

A. Nothing can be done
B. The Recycle Bin for deletes within 15 days, an Export Service or Data Loader backup for updates, and a documented backup approach for anything critical
C. Salesforce restores it free
D. Rollback in Setup

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The Recycle Bin covers deletes, not overwrites, so a bad update needs your own prior extract to restore from. Taking an export before any bulk operation is the habit that makes this recoverable.
</details>

---

## Where to go deeper

- [Salesforce Administrator cert page](../../exams/salesforce/administrator/) - notes, practice plan, strategy
- [Platform Developer I practice questions](./salesforce-platform-developer-1.md) - the programmatic counterpart
- [IAM explained](../../learn/concepts/iam-explained.md) - profiles and permissions in context
- **[📖 Salesforce Trailhead](https://trailhead.salesforce.com/credentials/administrator)** - official exam guide and study path
