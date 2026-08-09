---
last-updated: 2026-08-09
difficulty: advanced
---

# CISA - Certified Information Systems Auditor - Practice Questions

15 questions across the five CISA domains: the information systems auditing process, governance and management of IT, acquisition and development and implementation, operations and business resilience, and protection of information assets.

CISA questions reward the auditor's mindset. The correct answer is usually the one about evidence, independence, and process rather than the one about fixing the problem yourself.

> **Cert page:** [exams/isaca/cisa/](../../exams/isaca/cisa/)

---

### Question 1
**Scenario:** An auditor discovers a control deficiency during fieldwork.

A. Fix it immediately
B. Document the finding with evidence, assess its risk, discuss it with management, and report it
C. Report it to the regulator first
D. Ignore it if it is minor

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Implementing the fix destroys the auditor's independence, because you would later be auditing your own work. The auditor's product is a documented, evidenced finding and a recommendation; remediation belongs to management.
</details>

---

### Question 2
**Scenario:** What is the FIRST step in planning an audit?

A. Select the sample
B. Understand the business and its risks, then define scope and objectives based on a risk assessment
C. Test controls
D. Write the report

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Risk-based planning is what directs limited audit effort toward what matters. CISA questions asking for the FIRST step almost always want the understanding-and-planning answer rather than a testing activity.
</details>

---

### Question 3
**Scenario:** Which evidence is most reliable?

A. A verbal statement from the system owner
B. Evidence obtained directly by the auditor from an independent external source
C. An internal report provided by the auditee
D. A policy document

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Reliability rises with auditor-obtained, external, and objective evidence, and falls with auditee-provided, internal, and verbal evidence. A policy document shows what should happen, not what did, which makes it evidence of design rather than of operation.
</details>

---

### Question 4
**Scenario:** An auditor must test whether a control operated throughout the year, not just today.

A. An inquiry
B. A test of operating effectiveness over a sample of the period, using attribute sampling with a defined confidence level
C. Observation on one day
D. A walkthrough

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A walkthrough tests design, sampling across the period tests operation. Sample size follows from the population, tolerable deviation rate, and confidence level, which is why the statistical basis matters rather than picking a round number.
</details>

---

### Question 5
**Scenario:** Segregation of duties cannot be achieved in a small IT team.

A. Accept the risk silently
B. Recommend compensating controls: supervisory review, detailed logging with independent log review, and reconciliation
C. Hire more staff
D. Report it as a critical failure with no alternative

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Compensating controls are the standard answer where a preventive control is infeasible. The residual risk still has to be documented and accepted by management at an appropriate level, rather than quietly absorbed by the audit.
</details>

---

### Question 6
**Scenario:** Which control type is a detective control?

A. An access control list
B. Log review and reconciliation, which identify problems after they occur
C. Encryption
D. Segregation of duties

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Preventive controls stop an event, detective controls find it, corrective controls restore. Detective controls only have value if someone acts on what they detect, which is why "logs are collected" is a weaker finding response than "logs are reviewed."
</details>

---

### Question 7
**Scenario:** A change was moved to production without approval.

A. A minor issue
B. A control failure in change management; assess whether it is isolated or systemic by testing a sample of other changes
C. Reverse the change
D. Ignore it if the change worked

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A single exception may be an anomaly or the visible part of a broken process, and the difference determines the finding's severity. Expanding the sample to establish which is the auditor's next action, not remediation.
</details>

---

### Question 8
**Scenario:** A business continuity plan exists but has never been tested.

A. It is adequate
B. An untested plan provides limited assurance; recommend testing appropriate to criticality, from walkthrough to full interruption test
C. Testing is optional
D. Rewrite the plan

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Testing is what turns a document into a capability, and it is where unrecorded dependencies surface. The test type escalates with criticality: checklist, walkthrough, simulation, parallel, then full interruption.
</details>

---

### Question 9
**Scenario:** Which metric defines the maximum acceptable data loss?

A. RTO
B. RPO, the recovery point objective
C. MTD
D. MTBF

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RPO is measured backwards from the incident and drives backup and replication frequency; RTO is measured forwards and drives recovery capability. The maximum tolerable downtime bounds the RTO, and the two are frequently confused in exam wording.
</details>

---

### Question 10
**Scenario:** An auditor is asked to audit a system they helped design last year.

A. Proceed as normal
B. Disclose the impairment to independence and have someone else perform that portion of the audit
C. Decline all work with that client
D. Note it in the report only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Independence in both fact and appearance is the profession's foundation, and self-review is the classic impairment. Disclosure plus reassignment is the standard remedy under the ISACA code of professional ethics.
</details>

---

### Question 11
**Scenario:** Sampling finds 3 exceptions in a sample of 60 from a population of 6,000.

A. Conclude there are exactly 300 exceptions
B. Project the deviation rate to the population, compare it against the tolerable rate, and consider extending testing before concluding
C. Ignore the exceptions
D. Test the whole population

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A sample supports an inference with a confidence interval, not a point count. Whether the projected rate exceeds the tolerable rate is what decides the conclusion, and exceptions also warrant asking whether they share a root cause.
</details>

---

### Question 12
**Scenario:** An organization outsources payroll processing to a third party.

A. Risk transfers entirely to the provider
B. Accountability remains with the organization; obtain assurance through a service auditor's report such as SOC 1 or SOC 2 and review complementary user entity controls
C. No audit is required
D. Audit the provider directly always

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Outsourcing shifts the activity, not the accountability. Complementary user entity controls are the part most often skipped: the report's conclusions only hold if the customer implements the controls it assumes.
</details>

---

### Question 13
**Scenario:** Which control best addresses the risk of privileged account misuse?

A. Password complexity
B. Privileged access management with checkout, session recording, and independent review of privileged activity
C. Annual access reviews
D. Account lockout

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Privileged users can often alter the very logs that would show misuse, which is why independent review and tamper-resistant recording matter more than credential strength. Annual reviews are too infrequent to be the primary control here.
</details>

---

### Question 14
**Scenario:** An audit report finding is disputed by management.

A. Remove the finding
B. Re-examine the evidence; if the finding stands, report it with management's response included
C. Escalate to the board immediately
D. Soften the wording

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Including management's response is standard practice and lets the reader weigh both positions. Removing or softening a supported finding compromises the audit's integrity, while immediate escalation skips a legitimate step in the process.
</details>

---

### Question 15
**Scenario:** Which is the strongest evidence that a data center's physical access control works?

A. The policy document
B. Observation combined with testing the access log against the authorized personnel list for the period
C. An interview with the facilities manager
D. A photograph of the badge reader

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Reconciling actual entries against authorization tests operation over time, while observation confirms the control exists as described. Comparing the two also catches badges belonging to leavers, which is the usual finding.
</details>

---

## Where to go deeper

- [CISA cert page](../../exams/isaca/cisa/) - notes, practice plan, strategy
- [CISM practice questions](./isaca-cism.md) - the management counterpart
- [CCSP practice questions](./isc2-ccsp.md) - cloud security at professional level
- [SOC 2 guide](../soc2.md) - the service auditor report auditors rely on
- **[📖 ISACA CISA](https://www.isaca.org/credentialing/cisa)** - official exam content outline
