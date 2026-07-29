---
last-updated: 2026-07-29
---

# CSA 05 - Configuration, Customisation, and Migration

The distinction between configuring and customising, and how changes move between
instances. Update sets are heavily examined.

## Configuration versus customisation

- **Configuration** - changing the platform using its intended settings: form layouts, UI policies, business rules on your own tables, flows, catalog items. Survives upgrades cleanly.
- **Customisation** - modifying base system artefacts, for example editing a ServiceNow-provided business rule or script include. Creates upgrade risk, because your change and the vendor's change collide.
- **Skipped changes** - during an upgrade, records you modified that ServiceNow also changed are *skipped* and left for manual review. Reviewing skipped changes is a required post-upgrade activity.

The exam's expected preference: configure rather than customise, and when customisation is
unavoidable, document it and expect upgrade review.

## Update sets

- **Update set (`sys_update_set`)** - a container capturing configuration changes so they can be moved between instances.
- **Current update set** - the one capturing your changes right now. Selecting the wrong one is the single most common mistake, and the changes end up in the wrong container.
- **Default update set** - the fallback container. Work captured here should be moved to a named set; leaving it in Default is bad practice because Default is never marked complete or moved.
- **Update set states** - In Progress, Complete, Ignore.
- **Batching (parent and child update sets)** - grouping related sets so they migrate together in dependency order.

**The migration workflow**

1. Create and select a named update set on the development instance.
2. Make the configuration changes.
3. Mark the update set **Complete** (it can no longer capture changes).
4. **Retrieve** the update set on the target instance (via an update source), or export to XML and import.
5. **Preview** it. Preview finds collisions and errors, and problems must be resolved or accepted before commit.
6. **Commit** it. The changes are applied.
7. **Back out** if necessary; this reverses the committed changes.

**What update sets do NOT capture**

- **Data**, as opposed to configuration. Records in `sys_user`, `incident`, and other data tables are not captured.
- **Scheduled job execution history**, logs, and similar runtime records.
- Some artefacts require manual movement or an explicit "add to update set" action.

The data exclusion is a reliable exam question: moving users, groups, or CMDB records
between instances requires an export/import or a data-migration tool, not an update set.

## Moving data between instances

- **Export to XML** - right-click a list or record to export, then import on the target. Suitable for small volumes of data.
- **Import sets** - the standard mechanism for bulk data.
- **Clone** - copies production over a sub-production instance, with clone exclude rules (tables not copied) and preserve rules (target data retained).

## Scripting basics at CSA level

CSA expects recognition and light reading of scripts, not deep development.

- **GlideRecord** - the server-side API for querying and writing records.
  - `var gr = new GlideRecord('incident');` creates the object.
  - `gr.addQuery('active', true);` adds a condition.
  - `gr.query();` executes it.
  - `while (gr.next()) { ... }` iterates results.
  - `gr.update()` saves changes; `gr.insert()` creates a record.
- **GlideAggregate** - for counts and sums without retrieving every record.
- **GlideSystem (`gs`)** - server-side utilities: `gs.info()` for logging, `gs.getUser()`, `gs.hasRole()`, `gs.addInfoMessage()`.
- **GlideForm (`g_form`)** - client-side form API: `g_form.setValue()`, `g_form.setMandatory()`, `g_form.setVisible()`, `g_form.addErrorMessage()`.
- **GlideUser (`g_user`)** - client-side user info: `g_user.hasRole()`.
- **current** - in a business rule, the record being processed.
- **previous** - the record's prior state, available in business rules other than inserts.
- **g_scratchpad** - the object a display business rule populates for use by client scripts, avoiding a server round trip.

**Client script performance** - avoid synchronous GlideRecord calls in client scripts; use
GlideAjax or a display rule with `g_scratchpad` instead. This is both real guidance and a
tested point.

## Application development basics

- **Studio** - the IDE for building scoped applications.
- **Application scope** - namespacing that protects other applications' data.
- **Application repository / ServiceNow Store** - distributing applications.
- **Delegated development** - allowing non-admins to develop within specified applications.

## Instance maintenance

- **Plugins** - activate optional functionality. Some cannot be deactivated, so activate on sub-production first.
- **System upgrade** - ServiceNow applies family releases; the customer reviews skipped changes and tests.
- **Instance security hardening** - the security best-practice settings checklist.

## Exam pointers

- Update sets capture configuration, not data.
- Always confirm which update set is current before making changes.
- Preview before commit; resolve collisions rather than ignoring them.
- Mark an update set Complete before retrieving it elsewhere.
- Skipped changes after an upgrade are records you customised that ServiceNow also changed.
- Prefer configuration over customisation; prefer UI policies over client scripts.
- Avoid synchronous GlideRecord in client scripts.

## Official documentation

**[📖 Update sets](https://www.servicenow.com/docs/)** - capture, preview, and commit
**[📖 GlideRecord API reference](https://developer.servicenow.com/dev.do#!/reference)** - server-side scripting
**[📖 Now Learning CSA path](https://nowlearning.servicenow.com/lxp/en/now-platform/certified-system-administrator)** - official curriculum
