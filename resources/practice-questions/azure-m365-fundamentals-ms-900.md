---
last-updated: 2026-08-09
difficulty: beginner
---

# Microsoft 365 Fundamentals (MS-900) - Practice Questions

15 questions for MS-900 prep across cloud concepts, Microsoft 365 apps and services, security and compliance, and pricing, licensing, and support.

MS-900 is a business-and-vocabulary exam. It rewards knowing what each product is for, not how to configure it.

> **Cert page:** [exams/azure/ms-900/](../../exams/azure/ms-900/)

---

### Question 1
**Scenario:** Which cloud deployment model combines on-premises infrastructure with public cloud services?

A. A hybrid cloud model
B. Community cloud shared by several organizations
C. Private cloud
D. Public cloud run by a provider

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Hybrid keeps some workloads on-premises, often for latency, regulation, or legacy dependency, while consuming cloud services alongside. Microsoft 365 is delivered as SaaS from the public cloud, and hybrid identity through Entra Connect is the most common hybrid pattern organizations run.
</details>

---

### Question 2
**Scenario:** Which describes the difference between capital expenditure and operating expenditure in a cloud move?

A. CapEx is a monthly subscription paid as services are used; OpEx is a large upfront purchase of assets
B. They are the same
C. CapEx is upfront purchase of assets; OpEx is ongoing consumption-based spending
D. OpEx applies only to hardware, such as servers and network devices that are bought and depreciated

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Buying servers is CapEx: a large upfront cost depreciated over years. Subscribing to Microsoft 365 is OpEx: a predictable recurring cost that scales with headcount. The finance shift is one of the standard business-value arguments the exam tests.
</details>

---

### Question 3
**Scenario:** Which service is the hub for teamwork, combining chat, meetings, and file collaboration?

A. Exchange Online
B. Microsoft Teams, the hub for chat, meetings, and files
C. Power BI
D. SharePoint Online

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Teams is the collaboration front end, and it is built on the others: files live in SharePoint, chat and calendar data touches Exchange, and identity comes from Entra ID. Understanding that Teams composes the platform rather than replacing it is the useful mental model.
</details>

---

### Question 4
**Scenario:** A department needs a document library with versioning, co-authoring, and permissions for a project site.

A. OneDrive for Business sync client
B. SharePoint Online
C. Viva Engage
D. Exchange Online shared mailbox

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** SharePoint provides team sites and document libraries for shared content. OneDrive is personal storage for an individual's work files, though it is the same underlying technology. Exchange is mail and calendaring, and Viva is the employee experience suite.
</details>

---

### Question 5
**Scenario:** Which tool automates a workflow, such as saving email attachments to SharePoint?

A. Power BI, which connects to SharePoint lists and email data sources to build interactive dashboards
B. Power Automate
C. Power Apps, which builds a low-code app that users open to save the attachments by hand
D. Dataverse, the data platform that stores attachments as table rows once a person uploads them

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Power Automate builds triggered and scheduled flows across connectors. Power Apps builds low-code applications, Power BI does analytics and reporting, and Dataverse is the underlying data platform the Power Platform uses.
</details>

---

### Question 6
**Scenario:** Which describes Microsoft 365 Copilot's data access model?

A. It trains on your tenant data and shares what it learns with other tenants
B. It only works on public web data retrieved through Bing
C. It respects existing permissions, so a user can only surface content they already have access to
D. It bypasses permissions so that every user can find any file in the tenant

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Copilot grounds responses in Microsoft Graph within the user's existing permission boundary. The practical consequence is that Copilot surfaces oversharing that already existed, which is why permission cleanup and Purview DSPM for AI are recommended before rollout rather than after.
</details>

---

### Question 7
**Scenario:** Which portal do administrators use to manage devices, app protection, and compliance policies?

A. Exchange admin center, which manages mailboxes, mail flow rules, and transport settings
B. Power Platform admin center, which manages environments, data policies, and connectors
C. Microsoft Intune admin center
D. Azure portal only, because every Microsoft 365 setting is administered from one Azure screen

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Intune is the endpoint management service for enrollment, configuration profiles, compliance policies, and app protection policies, including for personal devices. Each other admin center manages its own workload.
</details>

---

### Question 8
**Scenario:** An organization needs Microsoft 365 with advanced threat protection, Intune, and Entra ID P2 in one license.

A. Microsoft 365 E5 plan
B. Microsoft 365 Business Basic
C. Office 365 E1
D. Microsoft 365 Apps for enterprise

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** E5 is the top enterprise bundle and includes Defender, Entra ID P2, Purview advanced compliance, and Power BI Pro. E3 has the productivity plus baseline security and compliance. Office 365 plans lack the Windows and Intune components, and Apps for enterprise is the Office applications alone.
</details>

---

### Question 9
**Scenario:** What does the Microsoft 365 service level agreement of 99.9% mean in practice?

A. A best-effort target with no remedy if it is missed
B. A guarantee covering the customer's own network, devices, and internet connection as well as the service
C. No downtime is possible, because the data centers are redundant
D. A financially backed uptime commitment with service credits if Microsoft misses it

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** An SLA is a contractual commitment with a defined remedy, normally service credits the customer must claim. It covers Microsoft's service, not your internet connection, your devices, or misconfiguration on your side, which is a distinction the exam likes.
</details>

---

### Question 10
**Scenario:** Where do administrators track planned changes and current service incidents?

A. The Microsoft 365 admin center Service health and Message center
B. The Azure pricing calculator, which estimates the monthly cost of the services in a planned deployment
C. The Service Trust Portal, where Microsoft publishes audit reports and compliance documentation for customers
D. Compliance Manager, which scores the organization's compliance posture against regulatory templates

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Service health shows current incidents and advisories, and the Message center announces upcoming changes and required actions. The Service Trust Portal publishes audit reports and compliance documentation, which is a different need.
</details>

---

### Question 11
**Scenario:** Which describes the difference between Microsoft 365 and Office 365?

A. Office 365 includes Windows and device management as well as the Office apps
B. Microsoft 365 is on-premises only, delivered as software on the customer's servers
C. They are identical, and the name was changed only for marketing, with the same licensed components in each
D. Microsoft 365 includes Office 365 plus Windows and enterprise mobility and security components

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Office 365 is the productivity cloud services. Microsoft 365 bundles those with Windows licensing and Enterprise Mobility + Security, including Intune and Entra ID. Naming has shifted over time, so the exam expects the current bundle relationship.
</details>

---

### Question 12
**Scenario:** A retention policy is applied to a mailbox for 7 years. A user deletes an email after 2 years.

A. The mailbox is locked and the user is blocked from any further deletion until the policy ends
B. Retention only applies to SharePoint sites and has no effect on Exchange mailbox content or deletions
C. The email is preserved in the recoverable items area until the retention period ends
D. The email is permanently gone because a user deletion always overrides any retention policy

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Retention wins over user deletion: the content is preserved invisibly for compliance and only truly removed when retention expires. This is why retention is a compliance control rather than a user-facing feature, and why "delete" in a governed tenant does not mean what users assume.
</details>

---

### Question 13
**Scenario:** Which support option is included with a standard Microsoft 365 subscription?

A. No support at all, because every request needs a paid support contract
B. Access to online support requests and the admin center support experience for all customers
C. A dedicated technical account manager who reviews the tenant and answers calls around the clock, every day
D. On-site visits from Microsoft engineers whenever a severity A problem is raised

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** All paying tenants can raise support requests through the admin center, with severity levels and response targets. Named account managers and proactive services come with paid support offerings such as Unified Support, not with the subscription itself.
</details>

---

### Question 14
**Scenario:** An organization wants to try Microsoft 365 before committing to annual billing.

A. Only annual commitment exists, so the organization must pay for a full year of seats upfront before any use
B. There is no trial
C. Trials require a Microsoft partner to set up the tenant
D. A free trial for limited users and days, plus monthly billing if flexibility matters more than price

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Trials exist for most plans, and the licensing choice afterward is a trade: annual commitment is cheaper per seat, monthly costs more but lets you reduce seats. Knowing that trade-off is the kind of business question MS-900 asks.
</details>

---

### Question 15
**Scenario:** Which best describes Microsoft Purview in the Microsoft 365 context?

A. The data governance, protection, and compliance solution set: labels, DLP, retention, insider risk, eDiscovery
B. An identity provider that handles sign-in, multifactor authentication, and conditional access for users
C. A device management tool that enrolls laptops and phones and applies configuration profiles
D. A virtual desktop service that streams a Windows desktop to remote users from Azure

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Purview is the umbrella for data governance and compliance across Microsoft 365 and beyond. Intune manages devices, Entra ID is identity, and Azure Virtual Desktop is the desktop service. Matching the product to the requirement is the whole skill this exam measures.
</details>

---

## Where to go deeper

- [MS-900 cert page](../../exams/azure/ms-900/) - notes, practice plan, strategy
- [AZ-900 practice questions](./azure-fundamentals-az-900.md) - the Azure fundamentals sibling
- [SC-900 practice questions](https://security.noblerworks.com/resources/practice-questions/azure-security-compliance-identity-sc-900/) - security and compliance fundamentals
- [IaaS vs PaaS vs SaaS](../../learn/concepts/iaas-paas-saas.md) - the service models in plain English
- **[📖 MS-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-900)** - official skills outline
