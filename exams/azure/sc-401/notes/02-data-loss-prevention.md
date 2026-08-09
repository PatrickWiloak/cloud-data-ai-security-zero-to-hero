---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 11 min
---

# 02 - Data loss prevention

**Domain 2: Implement data loss prevention (30-35%)**

DLP inspects activity and intervenes at a boundary. It does not change the file.

---

## Policy anatomy

A DLP policy is: **locations** plus one or more **rules**, each with **conditions**, optional **exceptions**, **actions**, **user notifications**, **user overrides**, and **incident reports**.

**Conditions** include content containing a sensitive information type, sensitivity label, or retention label; content shared with people inside or outside the organization; document properties; file extension; and sender or recipient attributes.

**Actions** include restricting access or encrypting, blocking the activity, blocking with override, auditing only, and running Power Automate flows.

**Rule priority** matters: rules are evaluated in order and the first matching rule's actions apply for a given policy.

---

## Locations and their differences

| Location | Notable behavior |
|---|---|
| **Exchange** | Mail flow inspection, transport-level blocking, notification to sender |
| **SharePoint / OneDrive** | Content at rest and on sharing; blocks external sharing of matched content |
| **Teams chat and channel messages** | Blocks messages and file shares in conversations |
| **Devices (endpoint DLP)** | Requires onboarded devices; controls copy, print, USB, network share, browser upload, clipboard |
| **On-premises repositories** | Through the Information Protection scanner |
| **Fabric and Power BI** | Applies to semantic models and datasets |
| **Defender for Cloud Apps** | Extends to third-party SaaS through the app connector |
| **AI applications** | Covers Microsoft 365 Copilot and other AI apps, restricting what content can be processed |

---

## Endpoint DLP

The location with the most prerequisites and the most exam detail.

- Devices must be **onboarded** (through Intune, Configuration Manager, or a script). An unonboarded device enforces nothing.
- **Restricted apps and app groups**: name applications that may not access protected content.
- **Unallowed browsers**: uploads through a browser that is not policy-aware are blocked rather than monitored, which is how personal cloud storage uploads are stopped.
- **Service domains**: allow or block lists governing where content may be uploaded.
- **Removable storage, network share, printing, clipboard, and Bluetooth** controls.
- **Advanced classification** sends content to the service for evaluation when local classification is insufficient.

For unmanaged devices, endpoint DLP is not available and **Defender for Cloud Apps session policies** are the alternative control.

---

## Rollout discipline

The exam consistently rewards staged deployment:

1. **Test mode** (simulation) with no user impact, reviewing matches
2. **Test with policy tips**, so users see notifications and you learn about false positives
3. **Enforce**, usually with **override plus business justification** for a period
4. **Tighten** to hard block for the highest-severity rules

**Incident reports** and alerts feed the DLP alerts dashboard, and can raise severity based on volume and repetition.

---

## Adaptive Protection

Links Insider Risk Management to enforcement. A user whose insider risk level rises from minor to moderate to elevated automatically receives progressively stricter DLP actions, and can also be targeted by Conditional Access.

This is the recurring exam answer to "apply stricter controls only to users who are behaving riskily, without applying them to everyone".

---

## DLP for AI

- Prevents content carrying specified sensitivity labels from being processed or summarized by Microsoft 365 Copilot and other AI applications.
- Works alongside **DSPM for AI**, which reports what is happening, while DLP enforces.
- The important design point remains that AI honors existing permissions, so DLP and labels are layered on top of a permissions clean-up rather than substituting for it.

---

## Key terms

- **DLP policy** - a rule set that inspects activity and blocks, warns, or audits when classified content crosses a boundary
- **Policy tip** - the in-product notification shown to a user when their action matches a DLP rule
- **User override** - a DLP setting allowing a user to proceed with a business justification, recorded in the incident report
- **Test mode** - a DLP state that evaluates policy and records matches without affecting users
- **Endpoint DLP** - the DLP location enforcing on onboarded devices, covering copy, print, USB, clipboard, and browser upload
- **Device onboarding** - the prerequisite process registering a device so endpoint DLP and Defender for Endpoint can enforce
- **Unallowed browser** - a browser that is not DLP-aware, whose uploads endpoint DLP blocks outright
- **Service domain list** - the endpoint DLP allow or block list of destinations content may be uploaded to
- **Adaptive Protection** - the capability that raises DLP or Conditional Access strictness automatically as a user's insider risk level increases
- **Incident report** - the record generated when a DLP rule matches, including the activity, content, and any justification
- **Advanced classification** - endpoint DLP capability sending content to the service for evaluation beyond local classification
- **DLP for AI applications** - DLP coverage preventing classified content being processed by Copilot and other AI applications

---

## Related

- [Notes 03: risks, alerts, and activities](./03-risks-alerts-and-activities.md)
- [Scenarios](../scenarios.md) - scenarios 4 and 6
- [Prompt injection defense](../../../../resources/ai-security/prompt-injection-defense.md)
