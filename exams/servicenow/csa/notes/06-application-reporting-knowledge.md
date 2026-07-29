---
last-updated: 2026-07-29
---

# CSA 06 - Reporting, Knowledge, and Platform Applications

Reporting and dashboards, plus the application-level content the exam expects an
administrator to recognize.

## Reporting

- **Report** - a saved visualization of data from one table or database view.
- **Report types** - bar, column, pie, donut, line, time series, trend, pivot, single score, list, and map.
- **Data source for a report** - a table or a **database view** when data from joined tables is needed. A report cannot join tables by itself.
- **Group by** - the dimension for aggregation.
- **Aggregation** - count, sum, average, minimum, maximum.
- **Filter and conditions** - which records are included.
- **Stacked by** - a second dimension in bar and column charts.
- **Drill-down** - clicking a chart segment to reach the underlying records.
- **Sharing** - reports can be shared with users, groups, or roles, published to a dashboard, or scheduled by email.
- **Scheduled report** - emailed on a schedule as PDF, CSV, or Excel.

**Report permissions** - `report_user` can create personal reports, `report_publisher` can
publish and share, and `report_admin` administers reporting. Sharing a report does not
bypass ACLs: recipients see only records they are allowed to see, so two users can open the
same report and see different row counts. That behavior is a favorite exam question.

## Dashboards and Performance Analytics

- **Dashboard** - a page of widgets, typically reports.
- **Widget** - a dashboard element: a report, a filter, or content.
- **Interactive filter** - a dashboard control that filters multiple widgets at once.
- **Responsive dashboard** - the current dashboard framework.
- **Performance Analytics (PA)** - trend analysis over time using **indicators** and **scores** collected on a schedule. It answers "how has this changed over months," which reporting cannot, because reports show current data only.
- **Indicator** - the metric PA collects.
- **Scorecard** - the display of an indicator over time with targets and breakdowns.

Reporting is a snapshot of current data; Performance Analytics is a time series built from
scheduled collections. That distinction is examined.

## Knowledge Management

- **Knowledge base** - a container of articles with its own ownership and access rules.
- **Article lifecycle** - draft, review, published, retired.
- **Article template** - a standard structure, for example how-to or troubleshooting.
- **User criteria** - defines who can read or contribute to a knowledge base. This is the access mechanism for knowledge, not ACLs.
- **Can Read / Cannot Read / Can Contribute / Cannot Contribute** - the four user-criteria assignments on a knowledge base. Cannot-Read takes precedence over Can-Read.
- **Knowledge feedback** - ratings, comments, and flags for review.
- **Search and relevance** - articles surface in the portal and in the platform search.

## Service Portal

- **Portal** - the end-user experience, composed of pages built from widgets.
- **Widget** - a reusable component with HTML, CSS, client script, and server script.
- **Theme** - branding: colors, logos, fonts.
- **Page** - a portal route with a unique ID.

At CSA level you are expected to know the components and how to brand a portal, not to
write widgets.

## Core applications an administrator meets

- **ITSM** - Incident, Problem, Change, Request, Knowledge, and the CMDB underpinning them.
- **ITOM** - Discovery, Service Mapping, Event Management, Orchestration.
- **ITBM / SPM** - project and portfolio management.
- **HR Service Delivery** - HR cases and employee service.
- **CSM** - customer service management.
- **SecOps** - security incident response and vulnerability response.
- **GRC** - governance, risk, and compliance.

CSA is platform-focused, so these appear as recognition questions rather than deep content.

## Integrations at CSA level

- **REST and SOAP** - the platform is both a provider and a consumer of web services.
- **Table API** - the standard REST interface for CRUD on any table.
- **REST API Explorer** - the built-in tool for constructing and testing calls.
- **Inbound email actions** - create or update records from received email.
- **Email accounts and notifications** - outbound configuration.
- **IntegrationHub** - low-code integration actions used inside Flow Designer spokes.
- **MID Server** - an on-premises Java application that lets the cloud instance reach systems inside a customer network without exposing them to the internet. This is the answer whenever an integration must reach an internal, non-internet-facing system.

## Instance security and administration

- **Instance security hardening settings** - a documented checklist including session timeouts, password policies, and blocking of high-risk features.
- **High Security Settings plugin** - introduces the `security_admin` elevated role and default-deny behavior.
- **Login and session management** - SSO via SAML, multi-factor authentication, and the local login fallback.
- **System logs and transaction logs** - diagnosing errors and slow transactions.

## Exam pointers

- A report sees only records the viewing user is permitted to see, even when shared.
- Reports need a database view to combine data from multiple tables.
- Performance Analytics provides trends over time; reports show current data.
- User criteria, not ACLs, control knowledge base access, and Cannot-Read wins.
- A MID Server is what lets the instance reach systems inside the customer network.
- Interactive filters apply across multiple dashboard widgets at once.

## Official documentation

**[📖 Reporting](https://www.servicenow.com/docs/)** - report types and sharing
**[📖 Knowledge Management](https://www.servicenow.com/docs/)** - user criteria and article lifecycle
**[📖 MID Server](https://www.servicenow.com/docs/)** - architecture and use cases
**[📖 Now Learning CSA path](https://nowlearning.servicenow.com/lxp/en/now-platform/certified-system-administrator)** - official curriculum
