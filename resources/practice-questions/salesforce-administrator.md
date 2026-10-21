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

A. Set the object's organization-wide default to Public Read/Write and rely on page layouts to keep other users' records out of view
B. Create a permission set
C. Set the organization-wide default to Private and enable Grant Access Using Hierarchies
D. Use field-level security

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Sharing is built from the most restrictive baseline upward: the organization-wide default sets the floor, and role hierarchy, sharing rules, manual sharing, and teams open it back up. Field-level security controls which fields are visible, not which records.
</details>

---

### Question 2
**Scenario:** A field must be hidden from one group of users but visible to another.

A. Field-level security via profiles or permission sets
B. Record types, assigning one record type to the first group and a different one to the second group
C. Validation rules
D. Page layouts alone, removing the field from the layout assigned to the group that must not see it

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Removing a field from a page layout hides it from that layout only; it remains reachable through reports, the API, and list views. Field-level security is the enforced control, applied at the data layer.
</details>

---

### Question 3
**Scenario:** Additional permissions must be granted to a handful of users without cloning their profile.

A. Change each user's role so that the extra permissions come down through the role hierarchy
B. Assign a permission set, or a permission set group for a bundle of related access, without touching the user's profile
C. Create a new profile that is a copy of the current one and add the extra permissions there
D. Change the organization-wide default

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Permission sets are additive and prevent profile proliferation, which is why Salesforce's guidance is a minimum-access profile plus permission sets. Permission set groups bundle several sets for a persona, with muting available to remove specific permissions from the group.
</details>

---

### Question 4
**Scenario:** Two divisions need different picklist values and page layouts on the same object.

A. Record types, each with its own picklist value sets and page layout assignments
B. Two profiles
C. Field dependencies, which filter a dependent picklist based on the value chosen in a controlling field
D. Two custom objects, one per division, each with its own fields, picklist values, and page layouts

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Record types partition a single object into business variants and drive both layout and picklist behavior per profile. Duplicating the object would split reporting and duplicate every piece of automation.
</details>

---

### Question 5
**Scenario:** Which automation tool should be used for new declarative automation?

A. Process Builder, because it is the most flexible declarative tool for building multi-step record automation
B. Workflow Rules, because they have been available the longest and are the most widely documented
C. Flow Builder, which Salesforce has consolidated automation into
D. Apex triggers

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Workflow Rules and Process Builder are retired for new automation and existing ones should be migrated. Flow covers record-triggered, screen, scheduled, and autolaunched cases, and record-triggered flows split into before-save (fast field updates on the same record) and after-save (related records and external actions).
</details>

---

### Question 6
**Scenario:** A value must be prevented from being saved when it fails a business rule.

A. A formula field that returns an error message whenever the value does not satisfy the business rule
B. A required field on the page layout
C. A validation rule that evaluates to true when the data is invalid
D. A workflow rule with a field update action that clears the value shortly after the record is saved

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The logic is inverted from how people read it: the rule's formula returning true is what blocks the save and shows the error. Validation rules also fire on API and data loader inserts, which page-layout requirements do not.
</details>

---

### Question 7
**Scenario:** A relationship must cascade delete children when the parent is deleted and support roll-up summaries.

A. An external lookup relationship, which links the child to records held in an external data source
B. A master-detail relationship
C. A hierarchical relationship, a special lookup that links a user to another user
D. A lookup relationship on the child object, with the parent field marked as required on the page layout

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Master-detail children are owned by the parent: they inherit its sharing, have no owner field, and are deleted with it, which is also what makes roll-up summary fields possible. Lookups are loose, optional, and do not cascade.
</details>

---

### Question 8
**Scenario:** Duplicate accounts are being created by users.

A. Duplicate rules with matching rules, set to alert or block on create and edit
B. Data Loader, scheduled to export and de-duplicate the accounts each night after users have created them
C. A report that lists accounts with similar names so that users can check it before creating records
D. A validation rule that checks only the Account Name field for an exact text match with another record

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A matching rule defines what counts as a duplicate, fuzzy matching included, and the duplicate rule defines what happens when one is found. Alert with a bypass is common for sales teams, since a hard block on a fuzzy match creates its own problem.
</details>

---

### Question 9
**Scenario:** A report must show accounts with no related opportunities.

A. A summary report grouped by account name, built on a report type that only returns accounts with opportunities
B. A joined report with two blocks
C. A standard report
D. A cross filter with "without" on the Opportunities object

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Cross filters express the "with or without related records" question that a plain filter cannot. The report type also matters: `Accounts with Opportunities` returns only accounts that have them, so the base type must include accounts without opportunities.
</details>

---

### Question 10
**Scenario:** 50,000 records must be updated from a spreadsheet.

A. Manual entry through the standard edit pages, working through batches of records one at a time
B. Data Loader, or the Import Wizard under its 50,000-record cap, matching on record IDs or an external ID
C. A report with inline editing turned on, saving the changes to all 50,000 rows at once
D. A flow that loops over the spreadsheet after it is attached to a record as a file, updating each row it finds

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The Import Wizard handles up to 50,000 records for a subset of objects and does not support deletes; Data Loader handles larger volumes, all objects, and every operation. An external ID field lets you upsert without knowing Salesforce record IDs.
</details>

---

### Question 11
**Scenario:** Sales users must follow a defined selling process with different stages per business line.

A. Path only, configuring different guidance and key fields for each business line
B. One set of stages for everyone, told apart by a picklist field on the opportunity
C. Sales processes tied to record types, each exposing its own subset of opportunity stages, assigned by profile
D. Validation rules

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A sales process selects which stage values a record type offers, and Path then adds guidance and key fields on top for each stage. Path is a user-experience layer, not the control over which stages exist.
</details>

---

### Question 12
**Scenario:** Cases must route to the right support queue automatically.

A. Manual assignment by a support manager who watches the new case list and reassigns each case
B. Case assignment rules with ordered entry criteria, assigning to a queue or user
C. Escalation rules that reassign each case to the correct queue at the moment it is created
D. Auto-response rules that send the right team a notification email about each new case

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Assignment rules evaluate entries in order and stop at the first match, so ordering is the design decision. Escalation rules act on age and inactivity later in the case lifecycle, and auto-response rules only send email.
</details>

---

### Question 13
**Scenario:** A user reports they cannot see a field they were told they have access to.

A. Change the organization-wide default to Public Read/Write so that every user can see all fields and all records in the org
B. Check field-level security on the profile and permission sets, then the page layout for their record type
C. Give them the System Administrator profile to bypass layouts and security
D. Delete and recreate the field with the same API name, then re-add it to the page layouts

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Field visibility is the intersection of field-level security and the assigned layout, so the troubleshooting order is security first, layout second. Granting administrator rights to fix a visibility complaint replaces a small problem with a large one.
</details>

---

### Question 14
**Scenario:** Changes must move from a sandbox to production safely.

A. Edit production directly in Setup, making each change during a quiet window outside business hours
B. Data Loader, exporting the configuration records from the sandbox and importing them into production
C. Rebuild each change by hand in production while reading from a screenshot of the sandbox configuration
D. Change sets, or a source-driven SFDX pipeline with version control for larger teams

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Change sets are declarative and adequate for small changes, but they carry no version history and are one-directional. Source-driven development with a repository is what makes releases reviewable and repeatable as the team grows.
</details>

---

### Question 15
**Scenario:** Data must be recoverable after a bad bulk update.

A. The Recycle Bin for deletes within 15 days, plus your own Data Loader or export backup taken before any update
B. Salesforce Support restores any bulk change at no cost if a case is opened within the same week
C. Nothing can be done once a bulk update commits, because Salesforce keeps no history
D. A Rollback button in Setup that reverts the organization to its state before the bulk job ran

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Recycle Bin covers deletes, not overwrites, so a bad update needs your own prior extract to restore from. Taking an export before any bulk operation is the habit that makes this recoverable.
</details>

---

## Where to go deeper

- [Salesforce Administrator cert page](../../exams/salesforce/administrator/) - notes, practice plan, strategy
- [Platform Developer I practice questions](./salesforce-platform-developer-1.md) - the programmatic counterpart
- [IAM explained](https://security.noblerworks.com/learn/concepts/iam-explained/) - profiles and permissions in context
- **[📖 Salesforce Trailhead](https://trailhead.salesforce.com/credentials/administrator)** - official exam guide and study path
