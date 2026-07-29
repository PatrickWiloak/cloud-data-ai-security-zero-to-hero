---
last-updated: 2026-07-29
---

# ServiceNow CSA - Exam Scenarios

Fourteen worked scenarios in CSA style. Illustrative, written for this repo, not real exam
questions. CSA questions are short and turn on knowing which platform feature does what,
so the analysis below focuses on why the distractors are wrong.

---

## 1. The changes went into the wrong container

An administrator spends a morning configuring forms and business rules, then discovers the
work is captured in the Default update set.

**Fix:** move the individual updates to a named update set, or create one and re-apply.
Prevention is selecting the correct update set *before* starting work.

**Takeaway:** always confirm the current update set first. Default is never migrated.

---

## 2. Users still cannot see the field

A field-level ACL is created granting `itil` read access to `incident.description`. Users
with `itil` still cannot see it.

**Why?** They must pass the table-level ACL as well. Field-level access does not override a
table-level denial.

**Takeaway:** the user must pass both field-level and table-level ACLs.

---

## 3. Testing access as an admin

An administrator verifies a new ACL by loading the record themselves and confirming they
can see it.

**Why is this wrong?** The admin role bypasses most ACLs, so the test proves nothing.

**Fix:** impersonate a user who holds only the target role.

**Takeaway:** impersonation is the correct way to test access.

---

## 4. Duplicate records after every import

A weekly CSV import creates a fresh set of records each run instead of updating existing
ones.

**Why?** No coalesce field is set on the transform map, so every row is treated as new.

**Takeaway:** coalesce determines insert versus update.

---

## 5. Making a field mandatory everywhere

A field on the Task table must be mandatory on Incident but not on Change.

**Answer:** a dictionary override on the Incident table.

**Takeaway:** dictionary overrides change inherited field behavior on one child table.

---

## 6. Catalog item or record producer?

The business wants a friendly form that raises an Incident directly, without generating a
request and fulfilment tasks.

**Answer:** a record producer, which creates a record on a specified table.

**Takeaway:** catalog items generate REQ/RITM/SCTASK; record producers create records
directly.

---

## 7. Comments visible to the wrong audience

A fulfiller writes internal troubleshooting detail in a field, and the customer sees it in
the portal.

**Why?** They used Additional comments, which is customer-visible, instead of Work notes.

**Takeaway:** Work notes internal, Additional comments customer-facing.

---

## 8. The record was copied, not updated

An administrator opens an existing Incident, edits a field, chooses Insert from the context
menu, and later finds two records.

**Why?** Insert creates a new record from the current form values. Update modifies the
existing record.

**Takeaway:** Insert and Insert and Stay create copies.

---

## 9. Priority will not change

A user tries to set Priority directly on an Incident form and finds it read-only.

**Why?** Priority is derived from Impact and Urgency through the priority lookup rules.

**Fix:** change Impact and Urgency, or modify the lookup rules if the matrix itself is
wrong.

**Takeaway:** Impact + Urgency = Priority.

---

## 10. Enforcing a rule on imported data

A field must be mandatory whether the record is created on a form, by import, or through a
web service. A UI policy is in place but imports still create incomplete records.

**Why?** UI policies act on the form only.

**Fix:** a data policy, which enforces at the data layer.

**Takeaway:** UI policy for forms, data policy for data including imports and APIs.

---

## 11. Two users, one report, different numbers

A report is shared with a group. Two members open it and see different record counts.

**Why?** Reports respect ACLs. Each user sees only records they are permitted to read.

**Takeaway:** sharing a report does not share the data behind it.

---

## 12. Reaching an internal system

An integration must pull data from a database inside the customer's data center, which has
no internet exposure.

**Answer:** a MID Server, installed on the customer network, which polls the instance and
performs the work locally.

**Takeaway:** MID Server is the bridge to non-internet-facing systems.

---

## 13. Updating a related record

When an Incident closes, a related Problem record must be updated.

**Answer:** an *after* business rule. Before rules act on the record being saved; after
rules are where you touch other records.

**Takeaway:** before modifies current, after modifies related.

---

## 14. Restricting knowledge to a department

Only HR staff should read a particular knowledge base.

**Answer:** user criteria on the knowledge base, with Can Read set to the HR group. ACLs
are not the mechanism here.

**Takeaway:** user criteria control knowledge and catalog access, and Cannot-Read takes
precedence over Can-Read.

---

## Patterns worth memorizing

| Symptom or requirement | Answer |
|---|---|
| Changes not migrating | Wrong or Default update set |
| Access denied despite a field ACL | Table-level ACL also required |
| Testing access | Impersonate, never test as admin |
| Duplicates on import | Missing coalesce field |
| Inherited field mandatory on one child | Dictionary override |
| Friendly form creating a record directly | Record producer |
| Internal notes leaked | Work notes vs Additional comments |
| Accidental duplicate record | Insert instead of Update |
| Priority read-only | Derived from Impact and Urgency |
| Rule must apply to imports | Data policy |
| Different users see different report data | ACLs apply to reports |
| Integration to an internal system | MID Server |
| Update a different record on save | After business rule |
| Restrict a knowledge base | User criteria |
