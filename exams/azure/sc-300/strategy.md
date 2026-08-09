---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 6 min
---

# SC-300 Study Strategy

## Three things decide most questions

**1. Licensing.** SC-300 is unusually license-sensitive. Read the tier in the scenario first. A perfect answer that needs P2 in a P1 tenant is wrong. Memorize the boundary table in the [fact sheet](./fact-sheet.md).

**2. Feature boundaries.** Conditional Access, PIM, entitlement management, and access reviews all appear as alternatives to each other in the same question. They solve different problems:

| Feature | Governs | Answers the requirement |
|---|---|---|
| Conditional Access | The conditions of a sign-in | "Block, or require MFA, when..." |
| PIM | Activation of a privileged role | "No standing admin rights" |
| Entitlement management | Bundled access with request and approval | "Contractors need a set of resources for 6 months" |
| Access reviews | Recertification over time | "Access must be reviewed quarterly" |
| Lifecycle workflows | Automated joiner/mover/leaver tasks | "When someone leaves, do X automatically" |

**3. Least privilege.** When a question asks which role to assign, the answer is the narrowest built-in role that covers the task. Global Administrator is almost never correct. Learn the common ones: User Administrator, Groups Administrator, Authentication Administrator, Privileged Authentication Administrator, Application Administrator, Cloud Application Administrator, Conditional Access Administrator, Security Reader.

The distinction between **Authentication Administrator** and **Privileged Authentication Administrator** is a favorite: the former cannot reset credentials for users holding privileged roles, the latter can.

## Phase 1: Directory objects (week 1-2)

Get comfortable with the object model: users, groups, devices, service principals, administrative units, and roles. Everything later assumes it.

Focus on:
- Dynamic membership rule syntax and its limits (no nested group rules, attribute availability)
- Administrative units as the delegation boundary
- Group-based licensing and what happens when licenses run out
- Guest user default permissions and how to restrict them

## Phase 2: Authentication (week 3)

Learn the authentication methods policy as the single modern control point. Legacy per-user MFA and the old SSPR method settings are being consolidated into it, and the exam reflects that.

Know the ladder of method strength: SMS and voice at the bottom, Authenticator with number matching in the middle, FIDO2 and Windows Hello for Business as phishing-resistant at the top. Requirements that say "phishing-resistant" have exactly one class of correct answer.

## Phase 3: Conditional Access (week 4)

The single highest-value topic. Build policies rather than reading about them.

Design rules the exam expects:
- Two break-glass accounts excluded from every policy
- Report-only before enforce
- Policies are additive; all matching policies apply and any block wins
- Conditional Access runs after primary authentication succeeds
- Use authentication strengths rather than the older "require MFA" where the scenario needs a specific method

## Phase 4: Applications (week 5)

The registration versus enterprise application distinction trips people up. One registration is the global definition of the app in its home tenant; the enterprise application (service principal) is the local instance in each tenant that consents to it.

Permission types:
- **Delegated** - the app acts as the signed-in user, effective permission is the intersection of app permission and user permission
- **Application** - the app acts as itself with no user, effective permission is exactly what was granted, so these always require admin consent

## Phase 5: Governance (week 6)

The governance features are conceptually simple but easy to confuse. Anchor each to the problem it solves using the table above, then learn the configuration objects: catalog, access package, policy, review, workflow.

## Common traps

| Trap | Reality |
|---|---|
| Recommending Global Administrator | Almost always wrong; find the narrow role |
| Ignoring the stated license tier | The most common source of wrong answers |
| Confusing app registration with enterprise application | Different objects, different blades, different questions |
| Assuming Conditional Access can block a password from being validated | It evaluates after authentication |
| Using a group where an access package is asked for | Groups have no request, approval, or expiry workflow |
| Forgetting password writeback | Required for SSPR to work for synced users |
| Treating dynamic groups as instant | Membership evaluation is not immediate |

## Exam day

- 100 minutes, roughly 40-60 items. Case studies, if present, appear as a distinct section that may not be revisitable.
- Read the license tier and the constraint before the options.
- Mark and move on anything taking more than 2 minutes.
- No penalty for wrong answers, so leave nothing blank.
- Renewal is free online within six months of expiry. Set a reminder at month 10.

## Related

- [Practice plan](./practice-plan.md)
- [Scenarios](./scenarios.md)
- [Fact sheet](./fact-sheet.md)
- [Study strategies](../../../resources/study-strategies.md)
- [Exam day checklist](../../../resources/exam-day-checklist.md)
