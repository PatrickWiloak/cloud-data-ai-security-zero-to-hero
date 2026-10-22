---
last-updated: 2026-10-22
difficulty: beginner
---

# Microsoft 365 Fundamentals (MS-900) - Practice Questions

30 questions for MS-900 prep across cloud concepts, Microsoft 365 apps and services, security and compliance, and pricing, licensing, and support.

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

### Question 16
**Scenario:** An organization moves email from its own Exchange servers to Exchange Online. Which cloud service model is it now consuming?

A. Infrastructure as a service, because Microsoft supplies the virtual machines that the organization manages
B. Platform as a service, because the organization deploys its own code onto Microsoft's runtime
C. Software as a service, because Microsoft runs the complete application and the organization uses it
D. On-premises hosting, because the mailboxes still belong to the organization's own domain name

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Exchange Online is a finished application delivered over the internet, with Microsoft running the servers, operating system, and application, which is SaaS. IaaS would leave the organization managing virtual machines and Exchange itself. PaaS is for deploying your own code. Using your own domain name does not make a service on-premises.
</details>

---

### Question 17
**Scenario:** Under the shared responsibility model for Microsoft 365, which responsibility always stays with the customer?

A. Patching the Exchange and SharePoint servers that host the tenant's mailboxes and sites
B. Its data, user accounts and identities, and the devices that connect to the service
C. Physical security of the datacenters, including guards, cameras, and access badges
D. Replacing failed disks and network hardware in the regions that host the tenant

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** In every cloud model the customer keeps responsibility for its information and data, accounts and identities, and endpoint devices. In SaaS, Microsoft is responsible for the application, servers, hardware, and physical datacenters, which covers patching, disk replacement, and site security.
</details>

---

### Question 18
**Scenario:** An employee needs a personal place to store work files, sync them to a laptop, and share individual files with colleagues when needed.

A. OneDrive, the personal work file storage that syncs to devices and supports sharing
B. A SharePoint communication site, created by the employee for their own working files
C. An Exchange Online shared mailbox, with files stored as attachments in the mailbox folders
D. A Teams channel, created by the employee so that the files sit in the channel's Files tab

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** OneDrive is each user's personal file storage in Microsoft 365, with sync to devices and per-file sharing. SharePoint sites and Teams channels are for team and organizational content. A mailbox is not a file store, and attachments do not sync as files.
</details>

---

### Question 19
**Scenario:** A team wants a table of action items that can be edited live inside a Teams chat and an Outlook email at the same time, staying in sync everywhere it appears.

A. A Word document attached to the email and posted in the chat, with track changes enabled for edits
B. A Power BI report embedded in both places, so that the action items are refreshed on a schedule
C. A Microsoft Forms survey sent to the team, with responses collected into a shared Excel workbook
D. A Microsoft Loop component, which stays in sync across Teams, Outlook, and other Microsoft 365 apps

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Loop components are portable pieces of content, such as tables, lists, and task lists, that stay in sync wherever they are shared, so edits in Teams appear in Outlook. An attachment creates separate copies. Power BI reports are for analytics, not shared editing. Forms collects responses rather than providing a shared table.
</details>

---

### Question 20
**Scenario:** Leadership wants a company-wide place for communities, announcements, and conversations across the whole organization, beyond individual team chats.

A. Microsoft Viva Engage, the community and social networking experience in Microsoft 365
B. Microsoft Bookings, which schedules appointments between staff members and customers
C. Microsoft Planner, which assigns tasks to people and tracks them on shared boards
D. Microsoft Stream, which stores and shares recorded meetings and other video files

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Viva Engage (formerly Yammer) provides organization-wide communities, announcements, and conversations. Bookings is for scheduling appointments, Planner for task tracking, and Stream for video. Each has a place in Microsoft 365, but none is the community hub the scenario describes.
</details>

---

### Question 21
**Scenario:** Contractors need a full, personalized Windows desktop with a fixed monthly price per user, streamed to any device, without the company managing virtual machine hosts.

A. Azure Virtual Desktop host pools, which the company sizes, scales, and pays for by the hour
B. Windows 365 Cloud PCs, which provide a dedicated cloud Windows desktop per user at a fixed price
C. Microsoft 365 Apps for business, which install the desktop Office apps on each contractor's device
D. Remote Desktop to an on-premises server, which each contractor reaches over a VPN connection

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Windows 365 gives each user a Cloud PC licensed per user per month, managed through Intune, with no host infrastructure to run. Azure Virtual Desktop is flexible but needs the company to build and scale host pools and pay for consumption. Microsoft 365 Apps provides Office apps, not a desktop. On-premises Remote Desktop keeps the company running servers.
</details>

---

### Question 22
**Scenario:** Which mail-related service is a core part of Microsoft 365 and provides mailboxes, calendars, and contacts?

A. Exchange Online, the cloud email and calendaring service used by Outlook
B. SharePoint Online, which stores mail in document libraries for each user
C. Microsoft Teams, which replaces mailboxes with persistent chat for each user
D. Microsoft Entra ID, which stores each user's email messages with their identity

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Exchange Online hosts mailboxes, calendars, and contacts, and Outlook is the client that uses them. SharePoint stores files and sites. Teams uses Exchange for calendars and does not replace mailboxes. Entra ID holds identities and group memberships, not mail.
</details>

---

### Question 23
**Scenario:** A security team adopts Zero Trust. Which set of principles is it adopting?

A. Trust devices on the corporate network, block devices outside it, and audit the network once a year
B. Encrypt all data at rest, disable MFA to reduce friction, and allow access from any device
C. Verify explicitly, use least privilege access, and assume breach
D. Rely on a strong perimeter firewall, since attackers cannot reach anything that sits behind it

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Microsoft's Zero Trust model rests on three principles: verify every request explicitly using all available signals, grant only the access needed, and design as if attackers are already inside. Trusting the corporate network or relying on the perimeter is the model Zero Trust replaces. Disabling MFA contradicts verifying explicitly.
</details>

---

### Question 24
**Scenario:** Users must complete MFA when signing in from outside the office, and sign-ins from non-compliant devices must be blocked from SharePoint.

A. Microsoft Purview retention policies, which apply to sign-ins as well as to files and mail
B. Microsoft Entra Conditional Access policies that evaluate location and device compliance at sign-in
C. Microsoft Defender for Office 365, which scans every sign-in for malicious attachments
D. A password expiry policy, which forces users to change passwords every 30 days

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Conditional Access evaluates signals such as user, location, device compliance, and risk at sign-in, and then requires MFA, allows, or blocks access. Retention policies govern how long content is kept. Defender for Office 365 protects mail and collaboration content. Password expiry does not consider location or device, and Microsoft no longer recommends forced periodic expiry.
</details>

---

### Question 25
**Scenario:** Phishing emails with malicious links and weaponized attachments are reaching users. The organization wants links checked at click time and attachments opened in a sandbox before delivery.

A. Microsoft Purview Data Loss Prevention, which scans outbound mail for sensitive data
B. Microsoft Intune app protection policies, which stop users opening untrusted attachments
C. Microsoft Entra ID Protection, which flags risky users after a phishing email is opened
D. Microsoft Defender for Office 365 Safe Links and Safe Attachments

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Safe Links rewrites and checks URLs when they are clicked, and Safe Attachments detonates attachments in a sandbox before delivery. DLP stops sensitive data from leaving, which is the opposite direction. Intune app protection governs data inside apps. Entra ID Protection detects risky sign-ins and users but does not inspect mail.
</details>

---

### Question 26
**Scenario:** An auditor asks for Microsoft's independent audit reports, such as ISO 27001 and SOC 2, for the Microsoft 365 cloud services.

A. The Microsoft Service Trust Portal, which publishes audit reports and compliance documents
B. The Microsoft 365 admin center Message center, which publishes certificates each month
C. Microsoft Defender XDR, which generates ISO and SOC reports for the tenant on demand
D. The Microsoft Purview audit log, which contains Microsoft's own third-party audit results

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Service Trust Portal hosts Microsoft's third-party audit reports, certifications, and compliance guides for its cloud services. The Message center announces service changes. Defender XDR is a security operations tool. The Purview audit log records user and admin activity in the tenant, not Microsoft's audits.
</details>

---

### Question 27
**Scenario:** A company with 150 employees wants Microsoft 365 apps, device management, and advanced security in one plan designed for small and medium businesses.

A. Microsoft 365 E5, which is the only plan that includes Intune for device management
B. Microsoft 365 F3, which is the plan designed for small and medium businesses
C. Office 365 E1, which includes desktop Office apps and Intune for small teams
D. Microsoft 365 Business Premium, the SMB plan for up to 300 users

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Business Premium is aimed at organizations of up to 300 users and combines the apps with Intune, Entra ID P1, and Defender for Business. E5 is an enterprise plan, and Intune is in several plans, not only E5. F3 is for frontline workers. Office 365 E1 has web apps only and no Intune.
</details>

---

### Question 28
**Scenario:** Retail store staff share devices, mostly use Teams for shift communication, and need web and mobile apps rather than full desktop Office.

A. Microsoft 365 E5, which is required for any Teams access
B. Microsoft 365 F3, a frontline license with web and mobile apps
C. Microsoft 365 Apps for enterprise, which is a desktop-only license
D. A Microsoft 365 Copilot license, which includes Teams and Office

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Frontline plans such as F3 target staff who use shared or mobile devices, giving web and mobile Office apps, Teams, and device management at a lower price. E5 is far more than needed. Microsoft 365 Apps for enterprise covers Office apps only. Copilot is an add-on to a qualifying base license, not a standalone suite.
</details>

---

### Question 29
**Scenario:** A small company wants a partner to sell it Microsoft 365, bill it monthly, and be its first line of support, rather than buying directly from Microsoft.

A. An Enterprise Agreement, signed directly with Microsoft for organizations with thousands of users
B. Buying through the Cloud Solution Provider program, where the partner handles billing and support
C. A trial subscription, which converts into a partner-managed subscription after thirty days
D. Volume licensing through the Microsoft Store, which assigns a partner automatically

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** In the Cloud Solution Provider program, a partner sells the subscriptions, bills the customer, and provides first-line support. An Enterprise Agreement is a direct agreement for large organizations. A trial does not change the purchasing channel. The Microsoft Store is a retail channel and does not assign partners.
</details>

---

### Question 30
**Scenario:** An administrator wants to know how Microsoft 365 licenses are actually used, such as how many assigned users have been active in Teams and Exchange over the last 90 days.

A. Microsoft Purview Compliance Manager, which reports license use as a compliance score
B. The Service Trust Portal, which lists each tenant's license usage by service
C. Usage reports in the Microsoft 365 admin center
D. Microsoft Defender XDR, which tracks app usage in its incident queue

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The admin center's usage reports show activity by service and period, so administrators can spot unused licenses and plan adoption work. Compliance Manager scores compliance controls. The Service Trust Portal holds Microsoft's audit documents. Defender XDR is for security incidents.
</details>

---

## Where to go deeper

- [MS-900 cert page](../../exams/azure/ms-900/) - notes, practice plan, strategy
- [AZ-900 practice questions](./azure-fundamentals-az-900.md) - the Azure fundamentals sibling
- [SC-900 practice questions](https://security.noblerworks.com/resources/practice-questions/azure-security-compliance-identity-sc-900/) - security and compliance fundamentals
- [IaaS vs PaaS vs SaaS](../../learn/concepts/iaas-paas-saas.md) - the service models in plain English
- **[📖 MS-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-900)** - official skills outline
