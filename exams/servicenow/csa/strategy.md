---
last-updated: 2026-07-29
---

# ServiceNow CSA - Exam Strategy

> Cert-specific tactics. General study advice lives in [study-strategies.md](../../../resources/study-strategies.md).

## Format reminder

- 60 questions, 90 minutes
- Multiple choice and multiple answer
- Passing score is not officially published; around 70% is the working assumption
- Prerequisite: the Now Learning "ServiceNow System Administration Fundamentals" path
- Maintenance: a short delta exam per release, so the credential stays current

90 seconds per question. Time is not the constraint on this exam; precision is.

## The single most important preparation step

Get a **Personal Developer Instance** and use it. It is free, and CSA is a practical exam
about a product you can hold in your hands. Reading about update sets is a poor substitute
for capturing one, previewing it, and committing it.

Build these at least once:

- A catalog item with variables, and a record producer, so the difference is concrete
- An ACL, then impersonate a user to test it
- An import set with and without a coalesce field, and observe the duplicates
- A flow in Flow Designer with an approval
- An update set moved between two instances, including a preview with a collision

That list covers a large share of the exam.

## The top traps

1. **ACL evaluation.** The user must pass both the field-level and the table-level ACL, and
   every part of a single ACL (role, condition, script) must evaluate true. Expect several
   questions here.

2. **Testing as an admin.** Admin bypasses ACLs. Any answer that verifies access by
   checking as an administrator is wrong; impersonation is the method.

3. **Update sets do not carry data.** They capture configuration. Users, groups, CMDB
   records, and other data need export/import or an import set.

4. **Personalise versus Configure.** Personalise affects only you; Configure changes it for
   everyone and needs a role. The same personal-versus-global split recurs across lists,
   forms, and reports.

5. **Insert versus Update.** Insert creates a copy. Questions describing accidental
   duplicates are usually pointing here.

6. **Catalog item versus record producer.** Item produces REQ/RITM/SCTASK; producer creates
   a record on a table.

7. **UI policy versus data policy versus client script.** UI policy for form behaviour,
   data policy for data-layer enforcement including imports, client script only when
   scripting is genuinely required. ServiceNow's own preference is configuration over code,
   and the exam follows it.

8. **Business rule timing.** Before modifies the current record, after modifies related
   records, async defers work, display populates `g_scratchpad`.

9. **Impact + Urgency = Priority.** Priority is derived, not typed.

10. **User criteria, not ACLs**, control knowledge base and catalog access.

## Question triage

CSA questions are short. Read for the *feature* being asked about and eliminate options
that describe features which cannot do the job. Distractors are usually real platform
features in the wrong role, which is why knowing what each feature is *for* matters more
than knowing its configuration screens.

Multiple-answer questions state how many to select. Count them, and treat each option as an
independent true or false claim.

Where two answers both work, choose the one that is configuration rather than code, and
platform-standard rather than bespoke.

## Study sequence

1. **Platform overview** - instances, tables, inheritance, roles.
   See [notes/01-platform-overview.md](notes/01-platform-overview.md).
2. **Lists, forms, tasks** - daily administration.
   See [notes/02-lists-forms-tasks.md](notes/02-lists-forms-tasks.md).
3. **Database administration** - ACLs and imports, the heaviest scoring area.
   See [notes/04-database-administration.md](notes/04-database-administration.md).
4. **Self-service and automation** - catalog and Flow Designer.
   See [notes/03-self-service-process-automation.md](notes/03-self-service-process-automation.md).
5. **Configuration and migration** - update sets.
   See [notes/05-configuration-customization.md](notes/05-configuration-customization.md).
6. **Reporting and knowledge**.
   See [notes/06-application-reporting-knowledge.md](notes/06-application-reporting-knowledge.md).
7. **Work [scenarios.md](scenarios.md)** and articulate why each distractor fails.

Follow the week-by-week structure in [practice-plan.md](practice-plan.md).

## The week before

- Recite the ACL evaluation order and the both-levels rule.
- Recite the update set workflow: select, change, complete, retrieve, preview, commit.
- Review business rule timings and client script types.
- Review the REQ / RITM / SCTASK relationship.
- Re-read the [fact-sheet](fact-sheet.md), which is deliberately dense for exactly this purpose.
- Do not start new material in the final two days.

## Exam day

Standard logistics are in the [exam-day checklist](../../../resources/exam-day-checklist.md).

CSA specifics: the platform vocabulary is precise, and several distractors differ from the
correct answer by one word (personalise versus configure, insert versus update, catalog
item versus record producer). Read the full option text rather than matching on the first
few words.

## After passing

The Certified Implementation Specialist (CIS) exams are the usual next step, chosen by
product line: ITSM, HR, CSM, or Discovery. Certified Application Developer (CAD) is the
alternative if you want to build on the platform rather than implement it.
