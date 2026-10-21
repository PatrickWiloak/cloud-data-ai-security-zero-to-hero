---
last-updated: 2026-10-14
difficulty: intermediate
---

# Google Cloud Associate Google Workspace Administrator - Practice Questions

45 original scenario questions mapped to the six sections of the [exam guide](https://services.google.com/fh/files/misc/associate_google_workspace_administrator_exam_guide_english.pdf): users, domains and Directory (~20%), core services (~23%), governance (~15%), security and access (~20%), browsers and endpoints (~10%), and troubleshooting (~13%). Not real exam questions.

> **Cert page:** [exams/gcp/workspace-administrator/](../../exams/gcp/workspace-administrator/)

---

### Question 1
**Section:** 1. Users, domains, Directory
**Scenario:** A setting must apply to the marketing department but not the rest of the organization.

A. Apply it to the marketing OU, or target a group where the setting supports groups, and leave other OUs unchanged
B. Change it per user by hand for every marketing employee, and repeat for each new hire
C. Apply it at the top-level OU so that it flows down to every department in the organization
D. It is not possible, because settings can only be applied to the whole organization

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Settings inherit down the OU tree and can be overridden in a child OU. For supported services a group can target people who span OUs, and group settings override OU settings.
</details>

---

### Question 2
**Section:** 1. Users, domains, Directory
**Scenario:** Users must sign in with the company's existing identity provider, and an IdP outage must not lock admins out of the Admin console.

A. Use GCDS to create accounts and rely on it for sign-in, with no SAML profile configured at all
B. Disable 2SV for admins so that no second factor is needed during an IdP outage
C. SAML SSO with the IdP, plus a break-glass super admin that does not depend on the IdP
D. Keep separate Workspace passwords for every user, managed in the Admin console, instead of the IdP

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** SAML SSO moves authentication to the IdP. A break-glass super admin outside SSO keeps recovery possible during an outage. GCDS provisions accounts, groups and OUs; it does not handle sign-in.
</details>

---

### Question 3
**Section:** 1. Users, domains, Directory
**Scenario:** New accounts must be created automatically from Active Directory, including groups and OUs.

A. A weekly CSV upload of users into the Admin console, with groups created by hand
B. Manual creation of each account, group and OU in the Admin console as hires arrive
C. GCDS (Google Cloud Directory Sync), a one-way sync of users, groups and OUs from Active Directory or LDAP
D. SAML SSO only, which authenticates users at the IdP but does not create their accounts

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** GCDS is one-way sync from AD or LDAP of users, groups and OUs. SSO handles sign-in, not creation.
</details>

---

### Question 4
**Section:** 1. Users, domains, Directory
**Scenario:** A user was deleted 12 days ago and is needed back.

A. Unsuspend the user, since deletion only suspends the account
B. Restore the user in the Admin console, then re-add group memberships
C. Create a new user and import the old data from a Takeout export taken before deletion
D. Impossible; deleted users cannot be recovered after a few days

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Deleted users can be restored for 20 days. Group memberships are not restored automatically.
</details>

---

### Question 5
**Section:** 1. Users, domains, Directory
**Scenario:** A departing employee's data must stay under Vault retention and no one will sign in again. The company wants to stop paying a full license.

A. Suspend the user, which blocks sign-in and releases the license while data stays in Vault
B. Delete the user, since Vault keeps deleted users' data for the length of the retention rule
C. Move the user to an Archived User license
D. Remove the license and keep the account, so Vault can no longer retain the data

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A suspended user is billed like an active one. Deleting a user removes data held or retained by Vault, and recovery lasts only 20 days. Archived User keeps data under Vault retention at a lower cost.
</details>

---

### Question 6
**Section:** 1. Users, domains, Directory
**Scenario:** Before deleting a departed user, the manager needs their Drive files.

A. Export Gmail only, and leave the Drive files to be deleted along with the account
B. Use the data transfer tool to move Drive ownership first
C. Share each file by hand after deletion, using the manager's own account
D. Delete first, then ask Google support to restore the files for the manager

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Transfer ownership before deletion so the files remain owned by an active account.
</details>

---

### Question 7
**Section:** 1. Users, domains, Directory
**Scenario:** A team needs a shared mailbox where messages can be assigned and marked resolved.

A. A Collaborative Inbox group
B. A shared user account that the whole team signs in to with one password
C. A calendar shared with the team, with events used to track each request
D. A distribution list that relays every message to members without assignment or status

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Collaborative Inbox turns a group into a shared mailbox with assignment and status.
</details>

---

### Question 8
**Section:** 1. Users, domains, Directory
**Scenario:** Membership of an Engineering group must always match the Department attribute on the user profile.

A. Manual updates each week by an admin who compares the Department column to the member list
B. A dynamic group
C. A Collaborative Inbox, which turns the group into a shared mailbox with assignment and status
D. A security group managed by hand, with owners adding and removing members as people move

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Dynamic groups compute membership from user attributes and keep it current.
</details>

---

### Question 9
**Section:** 1. Users, domains, Directory
**Scenario:** The company acquires a brand with its own domain and wants separate email identities for that brand's staff.

A. A domain alias, which mirrors every existing user's address on the new domain name, with no new users
B. A secondary domain, which adds a separate address space for the new brand's users
C. A user alias, which gives one user an extra address on the same domain
D. A group, which can receive mail at the new domain but is not a set of separate identities

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A secondary domain adds a separate address space and users. A domain alias only mirrors existing users' addresses on another name.
</details>

---

### Question 10
**Section:** 1. Users, domains, Directory
**Scenario:** Every user should receive mail at both @company.com and @company.co.uk without new accounts.

A. Add a secondary domain and create a new user on it for each person, which gives separate identities
B. Add a domain alias, which gives each user an address on the second domain automatically
C. Forward mail from one domain to the other with a routing rule
D. Add user aliases for managers only, leaving other staff on the first domain

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A domain alias gives every user an address on the second domain automatically.
</details>

---

### Question 11
**Section:** 1. Users, domains, Directory
**Scenario:** Hundreds of rooms across several offices must be created quickly, with capacity and equipment details.

A. Bulk upload buildings and rooms from a CSV file, defining features such as capacity and whiteboard
B. Create each room by hand in the Calendar app, one resource at a time per office
C. Use shared drives named after each room to hold its equipment details
D. Create a group per room and put the room details in the group description

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Buildings and rooms can be created in bulk, and features describe resources.
</details>

---

### Question 12
**Section:** 2. Core services
**Scenario:** Mail for the domain must be delivered to Google.

A. Publish SPF, which lists the servers allowed to send mail for the domain
B. Publish the MX record `smtp.google.com` and activate Gmail
C. Add a CNAME named mail that points to Google
D. Publish a DMARC record, which tells receivers how to handle mail that fails authentication

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** MX tells senders where to deliver. SPF, DKIM and DMARC are trust records, not delivery.
</details>

---

### Question 13
**Section:** 2. Core services
**Scenario:** The company wants receivers to reject spoofed mail from its domain without losing legitimate mail.

A. SPF and DKIM, then DMARC from none to quarantine to reject while reading reports
B. SPF only, set to hard fail, which does not authenticate the visible From address that users see
C. Allowlist all partners so that every one of their messages is accepted without checks
D. Block inbound mail from outside the company, which does not stop spoofing on other receivers

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Authenticate and observe before enforcing. Jumping straight to reject risks dropping real mail.
</details>

---

### Question 14
**Section:** 2. Core services
**Scenario:** All messages containing a project code name must be held for review before delivery to external recipients.

A. Attachment compliance, which matches file type, name or size, not message text
B. Content compliance rule matching the code name, with a quarantine action for outbound mail
C. A hold in Vault, which preserves messages for legal discovery but does not stop or delay delivery
D. An approved senders list, which exempts senders from spam filtering

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Content compliance matches message content and can quarantine for admin review.
</details>

---

### Question 15
**Section:** 2. Core services
**Scenario:** Executable attachments must never be delivered.

A. A larger message limit, which affects total size but not attachment type
B. A warning footer on outbound mail
C. Educate users not to send executables
D. Attachment compliance rule blocking those file types

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Attachment compliance matches type, name or size and rejects or quarantines.
</details>

---

### Question 16
**Section:** 2. Core services
**Scenario:** Management wants an assistant to read an executive's mailbox without knowing the password.

A. Auto-forward all mail to the assistant, which copies messages rather than granting access
B. Mail delegation
C. Send-as only, which lets the assistant send from the address but not read the mailbox
D. Share the password with the assistant so they can sign in as the executive

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Delegation grants access without credentials. Forwarding copies mail.
</details>

---

### Question 17
**Section:** 2. Core services
**Scenario:** Finance must not share files outside the company, except with the external auditor's domain.

A. A Gmail routing rule that rejects outbound mail to any address outside the company domain
B. Remove Finance's Drive licenses so that they cannot share files with anyone outside
C. Turn external sharing off for the whole company, which also blocks the auditor
D. A Drive trust rule scoped to Finance that blocks external sharing and allows the auditor domain

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Trust rules take scope, trigger, condition and action. They apply to files owned by users in scope.
</details>

---

### Question 18
**Section:** 2. Core services
**Scenario:** Link sharing options are 'anyone in the company' or named people only. HR wants a middle option limited to HR staff.

A. Disable link sharing completely, so that no one can share by link at all
B. Use Drive labels, which classify files but add no link audience
C. Put HR in the top-level OU so that HR settings apply to everyone in the company, whatever their department
D. Create a target audience for HR, which users can then pick when they share a link

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A target audience is a named audience that users can pick when sharing a link.
</details>

---

### Question 19
**Section:** 2. Core services
**Scenario:** Project files must outlive any member who leaves.

A. Group-owned My Drive files, since a group can be set as the owner of a file
B. Local sync folders on each member's laptop, backed up to the team server
C. My Drive folders owned by the project lead and shared with the other members
D. A shared drive

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Shared drive content is owned by the team, not by an individual.
</details>

---

### Question 20
**Section:** 2. Core services
**Scenario:** Meet recordings and Gemini notes should be available only to the Product organization for a pilot.

A. Enable for everyone and ask other departments not to use the features
B. Enable them at the top-level OU, which applies to every user unless overridden
C. Give Product super admin rights so that they can switch the features on for themselves
D. Enable them for the Product OU or group only

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Service and Gemini features can be scoped to an OU or group.
</details>

---

### Question 21
**Section:** 2. Core services
**Scenario:** The Gemini app is switched off for the company, but users still see Gemini suggestions in Gmail.

A. Gemini is broken and needs a support case with Google to repair it
B. Vault is overriding the setting because a hold applies to the users' mail
C. Users need to restart their browsers so that the setting change reaches Gmail and the other services
D. Gemini features inside Gmail, Docs and Meet have separate controls from the Gemini app

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Turning off the Gemini app does not switch off Gemini in Gmail, Docs or Meet.
</details>

---

### Question 22
**Section:** 2. Core services
**Scenario:** A non-developer team needs a simple mobile app on top of their spreadsheet.

A. Apps Script, a JavaScript platform that needs code to build the mobile app
B. Admin SDK, the API for managing users and settings rather than building apps
C. Cloud Functions, which runs developer-written code in response to events
D. AppSheet, Google's no-code app builder, which builds mobile apps directly on top of a spreadsheet

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** AppSheet is the no-code app builder. Apps Script is code.
</details>

---

### Question 23
**Section:** 3. Governance
**Scenario:** A legal hold and a 1-year retention rule both apply to a user's mail. A message is 18 months old.

A. It is moved to the archive, because the retention rule ends and the hold only copies data
B. Retention wins, so the message is purged once it is older than one year
C. It is purged, because the 1-year rule applies to all mail older than a year
D. It is preserved, because a hold overrides retention rules and keeps the data until the hold is removed

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A hold preserves data until it is removed, even if a retention rule would purge it.
</details>

---

### Question 24
**Section:** 3. Governance
**Scenario:** An admin wants to place a hold on every user.

A. Avoid it; scope holds to the people or groups in the matter
B. Put a hold on the top-level OU, which is the simplest way to cover every user
C. Hold all shared drives only, which captures the files of every user
D. Disable Vault so that no hold can be placed

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Holding the top-level OU can prevent deleting accounts and keeps unneeded data. Scope holds to the matter.
</details>

---

### Question 25
**Section:** 3. Governance
**Scenario:** Employees paste card numbers into Gmail and Drive. The company wants to measure first and block later.

A. Retention for 7 years, which keeps messages but does not detect or measure card numbers
B. A DLP rule with the card detector in audit-only mode, then warn or block after reviewing the results
C. Disable Drive for the whole company, which stops the leak but measures nothing
D. Block all attachments in Gmail and Drive, which stops legitimate work immediately

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Audit-only reveals volume and false positives before enforcement.
</details>

---

### Question 26
**Section:** 3. Governance
**Scenario:** Files labeled Confidential must never be shared externally.

A. Turn off Takeout, which stops bulk exports but does not block sharing of individual files
B. Move files to a shared drive, which changes ownership but leaves the external sharing rules as they were
C. A rule that uses the Confidential label as a condition to block external sharing
D. Ask users to be careful and review sharing before sending any link

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Classification labels can drive DLP and sharing rules.
</details>

---

### Question 27
**Section:** 3. Governance
**Scenario:** Admins want to stop users exporting their own data from Google Takeout.

A. Use Vault
B. Turn Takeout off or restrict data types for the OU
C. Disable Gmail
D. Remove licenses

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Takeout can be switched off or restricted per OU. It is an exfiltration control.
</details>

---

### Question 28
**Section:** 3. Governance
**Scenario:** A subsidiary's data at rest must stay in Europe.

A. A shared drive, which controls who can see files but not where they are stored
B. Apply a Europe data region to the subsidiary's OU, so covered data at rest stays there
C. DLP, which detects sensitive content but does not choose where data is stored
D. Use a different mail server hosted in a European data center for the subsidiary's mail and Drive files

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Data regions pin covered data at rest to the US or Europe, applied per OU.
</details>

---

### Question 29
**Section:** 4. Security and access
**Scenario:** Super admins must be protected against phishing and SIM swapping.

A. Enforce security keys or passkeys for the admin OU, which resist phishing and SIM swapping
B. Backup codes, which are single-use but can still be phished or stolen
C. Longer passwords, which resist guessing but can still be phished
D. SMS codes sent to the admin's phone, which can be intercepted by SIM swapping

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Security keys and passkeys are phishing resistant. SMS is the weakest option.
</details>

---

### Question 30
**Section:** 4. Security and access
**Scenario:** The help desk needs to reset passwords for staff only.

A. Groups Admin, which manages groups and memberships but not user passwords
B. Help Desk Admin, scoped to the OU that contains the staff whose passwords need resetting
C. Services Admin, which manages service settings but not user passwords
D. Super Admin, which can reset passwords but has far more access than needed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Help Desk Admin resets non-admin passwords. A scoped role follows least privilege.
</details>

---

### Question 31
**Section:** 4. Security and access
**Scenario:** Finance data in Drive must be accessible only from managed, encrypted devices.

A. Context-aware access with an access level for managed, encrypted devices, assigned to Drive for Finance
B. Block Drive for desktop on all devices so that files cannot sync locally
C. 2-step verification, which proves who the user is but says nothing about the device they use
D. A separate OU for Finance, which scopes settings but does not check the device used

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** CAA decides access by user plus context such as device and location.
</details>

---

### Question 32
**Section:** 4. Security and access
**Scenario:** The security team wants to see which settings fall short of Google recommendations.

A. Email Log Search in the Admin console
B. Security health
C. Audit logs
D. Vault

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Security health compares configuration to recommended practice.
</details>

---

### Question 33
**Section:** 4. Security and access
**Scenario:** An alert and an automatic suspension are required when a user shares many files externally in an hour.

A. A trust rule, which controls file sharing but does not suspend users
B. A DLP rule in Gmail, which scans message content rather than Drive sharing events or counts
C. Read the Drive log daily and suspend the user by hand when a spike appears in the sharing numbers
D. An activity rule on the Drive sharing event, with an alert and a suspend action

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Activity rules turn log events into alerts and automatic actions.
</details>

---

### Question 34
**Section:** 4. Security and access
**Scenario:** A user granted an unreviewed app access to all their Drive files.

A. Disable Drive for the entire company until every third-party app grant has been reviewed by hand
B. Ignore it, since the user chose to consent
C. Delete the user, which does not close the gap that allowed consent
D. Revoke the grant and limit OAuth access to reviewed apps with app access control

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** App access control and an allowlist stop risky consent grants.
</details>

---

### Question 35
**Section:** 5. Endpoints
**Scenario:** Staff phones need a passcode and the ability to remove company data when they leave. No agent should be installed.

A. Advanced mobile management with the device policy app
B. Basic mobile management
C. Chrome policies
D. Third-party MDM with its own agent installed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Basic management is on by default and covers passcodes and account wipe.
</details>

---

### Question 36
**Section:** 5. Endpoints
**Scenario:** Company-owned Android devices must be fully wiped when lost, and personal data must be separated on BYOD.

A. No management, relying on users to sign out of their accounts after a loss
B. Advanced management with work profiles
C. Basic management, which supports account wipe but not a full device wipe or work profiles
D. Account wipe only, which removes work data but leaves the company-owned device intact

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Advanced management adds device wipe and work profiles.
</details>

---

### Question 37
**Section:** 5. Endpoints
**Scenario:** A contractor leaves. Their personal phone has the work account.

A. Wipe the device
B. Wipe the account from the device
C. Do nothing, because the contractor's access ends on the last working day
D. Delete the device from the list only, leaving the account signed in

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Account wipe removes only work data and leaves personal data intact.
</details>

---

### Question 38
**Section:** 5. Endpoints
**Scenario:** Only a vetted set of Chrome extensions may be used, and a password manager must be on every machine.

A. Block by default, allow the vetted list, and force install the password manager
B. Block all extensions, including the password manager that must be on every machine in the company
C. Disable Chrome on managed laptops so that no extension can be installed
D. Let users choose their own extensions and recommend the vetted list by email to every employee

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Extension modes are allow, block and force install.
</details>

---

### Question 39
**Section:** 5. Endpoints
**Scenario:** Browsers on corporate laptops must receive machine policies even when no one is signed in.

A. Use Gmail rules, which route mail but do not apply policies to browsers
B. Use mobile management, which covers phones and tablets rather than Chrome on laptops
C. User policies only, which apply when a user signs in to Chrome with a managed profile
D. Enroll the browsers with an enrollment token

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Enrollment gives managed browsers machine-level policies.
</details>

---

### Question 40
**Section:** 6. Troubleshooting
**Scenario:** A partner says a message sent three days ago never arrived.

A. Capture a HAR file, which records browser traffic for sign-in and loading problems
B. Reset the sender's password in case the account was compromised
C. Check Vault, which searches stored message content rather than delivery status
D. Email Log Search by sender, recipient or message ID

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Email Log Search shows delivery status for about the last 30 days.
</details>

---

### Question 41
**Section:** 6. Troubleshooting
**Scenario:** A message from your domain landed in spam. The recipient forwards the full header.

A. Reset the sender password in case the account was compromised and is sending spam
B. Delete the message; ask the recipient to mark not spam
C. Disable spam filtering for the domain so that its mail always reaches the inbox
D. Paste it into Messageheader and read the spf, dkim and dmarc results

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Messageheader shows the route and authentication results, so you can fix the failing DNS record.
</details>

---

### Question 42
**Section:** 6. Troubleshooting
**Scenario:** Many users report that Gmail is slow at the same moment.

A. Change routing rules to bypass the content filters on inbound mail
B. Reinstall Chrome on the affected machines to clear the cache
C. Reset passwords for all users to refresh their sessions
D. Check the Workspace Status Dashboard first

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Rule out a Google-side incident before changing configuration.
</details>

---

### Question 43
**Section:** 6. Troubleshooting
**Scenario:** One office has choppy Meet calls and others are fine.

A. Disable recordings for the affected office to reduce the bandwidth that Meet uses on its network
B. Reinstall Meet on every laptop in the office, since the client is likely to be corrupt on all of them
C. Suspend the users in the office until the network team finds the cause
D. Use the Meet quality tool for those calls and investigate the network at that office

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The quality tool shows per-call network and media detail.
</details>

---

### Question 44
**Section:** 6. Troubleshooting
**Scenario:** Google Support asks for evidence of a browser sign-in problem.

A. A DLP report
B. A HAR file captured in the browser
C. A Takeout archive of the user's Gmail, Drive and Calendar data
D. A Vault export

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** HAR files capture browser traffic for sign-in, loading and performance issues.
</details>

---

### Question 45
**Section:** 6. Troubleshooting
**Scenario:** A user permanently deleted Drive files 10 days ago and the trash is empty.

A. Restore from DNS, by publishing a record that points back to the deleted files
B. Impossible, because permanently deleted files cannot be recovered after the trash is emptied
C. An admin restores the user's files from the Admin console within the restore window
D. Support rebuilds the Drive from Google's backups at the admin's request

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Admins can restore a user's permanently deleted Drive files for a limited window after deletion.
</details>

---

## Where to go deeper

- [Workspace Administrator cert page](../../exams/gcp/workspace-administrator/) - notes, scenarios, practice plan, strategy
- [MS-900 practice questions](./azure-m365-fundamentals-ms-900.md) - the Microsoft 365 counterpart
- [SC-300 practice questions](https://security.noblerworks.com/resources/practice-questions/azure-identity-access-sc-300/) - identity administration at depth
- [IAM topic index](https://security.noblerworks.com/topics/iam/) - identity across the repo
- **[📖 Google Cloud certification](https://cloud.google.com/learn/certification)** - official exam guides
