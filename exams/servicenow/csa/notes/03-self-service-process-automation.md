---
last-updated: 2026-07-29
---

# CSA 03 - Self-Service and Process Automation

The Service Catalog, Flow Designer, and the automation artefacts that move work along
without human intervention.

## Service Catalog

- **Service Catalog** - the storefront where users request goods and services.
- **Catalog item** - a single requestable thing, with variables collecting the requester's input.
- **Record producer** - a catalog-style form that creates a record on *any* table, commonly used to raise an Incident through a friendly interface. Distinguishing it from a catalog item is a standard exam question: a catalog item generates a request, a record producer creates a record directly.
- **Order guide** - bundles several catalog items into one ordering experience, for example new-hire onboarding.
- **Category** - organises items within a catalog.
- **Variable** - a field on a catalog item: single line text, select box, reference, checkbox, multiple choice, and others.
- **Variable set** - a reusable group of variables shared across items.
- **Catalog client script** - runs in the browser on catalog forms, for dynamic behaviour.
- **Catalog UI policy** - declaratively makes catalog variables mandatory, read-only, or visible.

**The request lifecycle**

1. **REQ (Request)** - the overall order.
2. **RITM (Requested Item)** - one item within the order; workflow runs here.
3. **SCTASK (Catalog Task)** - the individual unit of fulfilment work.

Learning that REQ contains RITMs which spawn SCTASKs is essential, because questions
routinely ask which record a given activity attaches to.

## Service Portal

- **Service Portal** - the end-user-facing interface, built from pages, containers, rows, columns, and widgets.
- **Widget** - a reusable component rendering part of a page.
- **Portal versus platform UI** - end users experience the portal; fulfillers typically work in the platform or a workspace.

## Knowledge Management

- **Knowledge base** - a container of articles, with its own access controls.
- **Article** - the content, moving through a lifecycle of draft, review, published, and retired.
- **User criteria** - controls who can read or contribute to a knowledge base. This is the mechanism for knowledge access, and it is separate from ACLs.
- **Article versioning and feedback** - track changes and usefulness.

## Flow Designer

The current automation tool, replacing legacy Workflow for new work.

- **Flow** - a sequence of triggers, actions, and conditions, built in a no-code interface.
- **Trigger** - what starts the flow: record created or updated, a schedule, an inbound email, or an application-specific event.
- **Action** - a step performing work, for example create a record, ask for approval, or send a notification.
- **Subflow** - a reusable flow called from another flow, with inputs and outputs.
- **Data pill** - a reference to data produced by an earlier step, used to pass values between steps.
- **Flow versus legacy Workflow** - Flow Designer is the strategic tool; the Workflow editor still exists for older content. New automation should use Flow Designer.

## Process automation artefacts

- **Business rule** - server-side JavaScript that runs when a record is queried, inserted, updated, or deleted. Timing options are **before**, **after**, **async**, and **display**.
  - **Before** - runs before the record is written; used to modify field values on the record being saved.
  - **After** - runs after the write; used to update *related* records.
  - **Async** - runs in the background via the scheduler; used for work that should not delay the user.
  - **Display** - runs before the form loads, and is how you populate the `g_scratchpad` for client scripts.
- **Client script** - runs in the browser. Types: **onLoad**, **onChange**, **onSubmit**, and **onCellEdit** (for list editing).
- **UI policy** - declaratively sets fields mandatory, read-only, or visible on a form, based on conditions. Preferred over a client script for these tasks because it is configuration rather than code, and it runs later so it wins over conflicting client scripts.
- **Data policy** - enforces mandatory and read-only rules at the *data* layer, so they apply to imports and web services as well as forms. A UI policy protects the form; a data policy protects the data.
- **UI action** - a button, link, or context menu item, running client-side, server-side, or both.
- **Script include** - reusable server-side JavaScript, called from business rules and other scripts.
- **Scheduled job (scheduled script execution)** - runs on a schedule.
- **Event** - a named signal recorded in the event queue, typically consumed by notifications.

**When to use which** is the recurring exam question:

| Requirement | Use |
|---|---|
| Make a field mandatory on a form under a condition | UI policy |
| Enforce mandatory on import and web service too | Data policy |
| Set a value on the record being saved | Before business rule |
| Update a different record after this one saves | After business rule |
| React to a field change without saving | onChange client script |
| Reusable server-side logic | Script include |
| Multi-step process with approvals | Flow Designer |

Prefer configuration over code: UI policy over client script, Flow Designer over scripted
workflow. That preference is both ServiceNow's guidance and the exam's expected answer.

## Approvals and SLAs

- **Approval** - a decision record assigned to a user or group, generated by a flow or workflow.
- **Approval rules and delegation** - a user can delegate approvals during absence.
- **SLA definition** - defines the target duration with start, pause, and stop conditions.
- **Task SLA** - the running instance attached to a specific task, tracking elapsed and remaining time.
- **Retroactive start** - allows an SLA to count from a time earlier than attachment.

## Exam pointers

- Catalog item produces a request; record producer creates a record on a table directly.
- REQ contains RITM, which spawns SCTASK.
- UI policy for form behaviour, data policy for data-layer enforcement including imports.
- Before business rules modify the current record; after business rules touch related records.
- Display business rules populate `g_scratchpad` for client-side use.
- User criteria control knowledge base access, not ACLs.
- Flow Designer is the current standard for new automation.

## Official documentation

**[📖 Flow Designer](https://www.servicenow.com/docs/)** - triggers, actions, subflows
**[📖 Service Catalog](https://www.servicenow.com/docs/)** - items, variables, order guides
**[📖 Now Learning CSA path](https://nowlearning.servicenow.com/lxp/en/now-platform/certified-system-administrator)** - official curriculum
