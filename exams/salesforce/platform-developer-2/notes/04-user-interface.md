---
last-updated: 2026-07-29
---

# PD2 04 - User Interface

Lightning Web Components, Aura, and Visualforce. PD2 focuses on Lightning Web Components as
the modern standard, while expecting awareness of the older frameworks.

## Lightning Web Components (LWC)

The current, standards-based UI framework and the exam's primary focus.

- **Web standards foundation** - LWC is built on standard web components: custom elements, shadow DOM, ES modules, and modern JavaScript. Knowing standard HTML and JavaScript transfers directly.
- **Component bundle** - an HTML template, a JavaScript class, a metadata configuration file, and optional CSS and SVG.
- **Reactivity** - fields used in the template re-render when they change. Fields decorated with `@track` deep-track objects and arrays (largely automatic in current versions for primitives and reassignments).
- **`@api`** - exposes a public property or method, so a parent can pass data in or call the child.
- **`@wire`** - reactively reads Salesforce data from a wire adapter or Apex method. Re-invokes when its reactive parameters change.
- **Imperative Apex** - calling an `@AuraEnabled` Apex method directly from JavaScript when you need control over timing or to call on a user action rather than reactively.

## LWC data access

- **Lightning Data Service (LDS)** - reads and writes records without Apex, via wire adapters (`getRecord`, `getObjectInfo`) and functions (`createRecord`, `updateRecord`). LDS caches and keeps records consistent across components, and respects field-level security automatically. Prefer it over Apex for simple record operations.
- **`lightning-record-form`, `-edit-form`, `-view-form`** - base components that build record UIs with minimal code and honour security.
- **Apex methods** - `@AuraEnabled(cacheable=true)` for wire-compatible read methods; without `cacheable`, for imperative and write operations. `cacheable=true` methods must not mutate data.

Prefer LDS and base components for CRUD; drop to Apex when the logic exceeds what they can
do. That preference is examined.

## Component communication

- **Parent to child** - the parent sets a child's `@api` property, or calls its `@api` method.
- **Child to parent** - the child dispatches a `CustomEvent`; the parent listens with `on<eventname>`.
- **Unrelated components** - the **Lightning Message Service (LMS)** communicates across the DOM, including across LWC, Aura, and Visualforce, using a message channel.
- **Pub-sub (legacy)** - an older cross-component pattern, superseded by LMS.

Match the mechanism to the relationship: properties down, events up, Lightning Message
Service across. Choosing the wrong one is a common exam trap.

## Events and the DOM

- **CustomEvent** - the mechanism for child-to-parent communication, optionally carrying a `detail` payload, and configurable to bubble.
- **Shadow DOM** - encapsulates a component's markup and styles, which is why a parent cannot style a child's internals directly and events must cross the boundary deliberately.
- **Lifecycle hooks** - `constructor`, `connectedCallback` (inserted into the DOM, where you subscribe or fetch), `renderedCallback` (after each render, used carefully to avoid loops), `disconnectedCallback` (cleanup, unsubscribe), and `errorCallback` (capture descendant errors).

## Aura components

The predecessor to LWC, still present and interoperable.

- **When you still meet Aura** - features not yet available in LWC, and legacy code. LWC can be nested inside Aura, but not the reverse.
- **Aura versus LWC** - Aura is a proprietary framework; LWC is web-standards-based, lighter, and faster. New development should be LWC.

## Visualforce

The oldest framework, page-based and server-rendered.

- **Controllers** - standard controller (out-of-the-box CRUD for one object), custom controller (all logic in Apex), and controller extension (adds to a standard controller).
- **`with sharing` versus `without sharing`** - a Visualforce custom controller runs in system mode by default, so declaring `with sharing` to respect the user's record access is a security decision the exam tests.
- **View state** - the serialised state of a Visualforce page, with a size limit; large view state causes performance problems.
- **When still used** - PDF rendering, email templates, and legacy pages.

## Security in the UI layer

- **CRUD and FLS enforcement** - Apex does not automatically enforce object and field permissions. Enforce with `WITH SECURITY_ENFORCED` in SOQL, the `Security.stripInaccessible` method, or `Schema` describe checks. LDS and base components enforce automatically, which is a reason to prefer them.
- **Sharing** - `with sharing`, `without sharing`, and `inherited sharing` on Apex classes control record-level visibility.
- **Locker Service / Lightning Web Security** - the runtime sandbox restricting what component JavaScript can do, protecting one component from another.

Apex enforces neither CRUD, FLS, nor sharing unless you make it. This gap, and the ways to
close it, is a reliable exam topic.

## Exam pointers

- LWC is the primary framework; know its decorators (`@api`, `@wire`) and lifecycle hooks.
- Prefer Lightning Data Service and base components for CRUD; they enforce security automatically.
- Communication: properties down, events up, Lightning Message Service across unrelated components.
- `@AuraEnabled(cacheable=true)` methods are wire-compatible and must not mutate data.
- Apex does not enforce CRUD, FLS, or sharing automatically; use `WITH SECURITY_ENFORCED`, `stripInaccessible`, and sharing keywords.
- Visualforce custom controllers run in system mode; add `with sharing` to respect user access.

## Official documentation

**[📖 Platform Developer II exam guide](https://trailhead.salesforce.com/credentials/platformdeveloperii)** - authoritative objectives
**[📖 Lightning Web Components Developer Guide](https://developer.salesforce.com/docs/platform/lwc/guide)** - decorators, wire, lifecycle
**[📖 Enforcing security in Apex](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_perms_enforcing.htm)** - CRUD, FLS, and sharing
