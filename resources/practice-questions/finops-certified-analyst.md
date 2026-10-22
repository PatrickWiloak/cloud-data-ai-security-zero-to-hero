---
last-updated: 2026-10-22
difficulty: intermediate
---

# FinOps Certified Analyst (FOCA) - Practice Questions

30 questions for FOCA prep across the FinOps framework's principles, personas, phases, domains, and the analyst's day-to-day capabilities.

> **Cert page:** [exams/finops/certified-analyst/](../../exams/finops/certified-analyst/)

---

### Question 1
**Scenario:** The three FinOps phases, in order.

A. Measure, Reduce, Report - a cycle that starts with metering usage
B. Inform, Optimize, Operate - visibility first, then efficiency actions, then continuous governance
C. Detect, Analyze, Act - a security-incident style loop for billing spikes
D. Plan, Build, Run - the software delivery lifecycle phases, applied to cloud projects but not the phases the FinOps framework defines

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Inform establishes visibility and allocation, Optimize identifies and executes efficiency actions, Operate makes it continuous through process and governance. Teams iterate through the phases per workload rather than progressing through them once as an organization.
</details>

---

### Question 2
**Scenario:** Which FinOps principle addresses who owns cloud spend?

A. Procurement decides, because it signs the cloud contracts and so controls the spend, with engineers consuming whatever budget remains
B. Engineering has no cost responsibility, since engineers focus on delivering features and the finance team handles all cloud billing matters
C. Teams need to take ownership of their cloud usage
D. Finance owns all decisions about cloud spend, as the budget holders, and engineers are told the limits after the money is allocated

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Decentralized ownership with centralized enablement is the model: the team that provisions the resource owns its cost, while a central FinOps function provides the data, tooling, and rate negotiation. Cost decisions made far from the engineers who cause them do not stick.
</details>

---

### Question 3
**Scenario:** A cost report shows 40% of spend as unallocated.

A. Address the allocation gap: enforce tagging at creation, use account or subscription structure for what tags cannot cover, and apply a documented method for shared costs
B. Split it evenly across all teams so that every group carries a share of the cost, regardless of how much each one used
C. Assign it to the largest team since that team probably drives most of the unallocated spend, and let it chase the details
D. Ignore it because the remaining 60% is allocated, and the unallocated part is only a rounding issue in the billing export

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Allocation is the foundation of the Inform phase, because nobody optimizes what they are not accountable for. Enforcement at creation is what stops coverage decaying, and shared costs (support, networking, shared clusters) need a stated method rather than an ad hoc one.
</details>

---

### Question 4
**Scenario:** The difference between showback and chargeback.

A. Chargeback is only for finance teams, and engineering only sees showback
B. Showback reports cost to teams for visibility; chargeback actually bills it to their budget
C. Showback bills teams for their costs against their own budget, while chargeback only displays a report of cost without moving money
D. They are identical, and different companies simply use whichever term they prefer for sending a cost report to the team

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Organizations usually start with showback because it needs no accounting integration and builds trust in the data. Moving to chargeback before allocation is accurate produces disputes about the numbers rather than action on the costs.
</details>

---

### Question 5
**Scenario:** Which optimization lever changes the unit price rather than the usage?

A. Deleting unused volumes and snapshots, which cuts what is consumed, so it changes the usage side rather than the price paid per unit
B. Commitment-based discounts such as reserved instances or savings plans, plus negotiated enterprise agreements
C. Rightsizing instances to a smaller family after reviewing utilization, which lowers usage of capacity, not the rate paid for each hour
D. Scheduling non-production shutdowns outside working hours, which reduces the hours used and so lowers usage, not the unit price

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The two levers are rate and usage. Rate optimization (commitments, negotiated rates, spot) changes what you pay per unit; usage optimization (rightsizing, scheduling, deletion, architecture) changes how many units you consume. Commit only to a baseline you have already reduced.
</details>

---

### Question 6
**Scenario:** Which order should the two levers be applied in?

A. Usage first: reduce what you consume, then commit to the remaining stable baseline
B. Rate first, then usage, so that the discount applies to today's full footprint before the team looks for waste to remove
C. Simultaneously with no sequencing, since the two levers each lower the bill and the order has little effect on the resulting commitment
D. Rate only, because commitments have the largest percentage discount

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Committing before rightsizing locks in a discount on waste, and the commitment then discourages the rightsizing that would strand it. Reducing usage first means the commitment covers a genuine floor.
</details>

---

### Question 7
**Scenario:** A team asks whether their application is getting more efficient as it grows.

A. A unit economics metric: cost per transaction, per customer, or per unit of business value
B. Number of instances running over time, which shows the size of the footprint
C. Percentage change in spend from month to month, which rises with growth and cannot separate efficiency from a larger workload
D. Total monthly spend compared with the budget, which tells you whether spend is on target but not whether efficiency is improving

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Total spend rising during growth is expected and says nothing about efficiency. Unit cost is what distinguishes healthy scaling from waste, and it is the metric that lets engineering defend a rising bill to finance.
</details>

---

### Question 8
**Scenario:** A commitment purchase has 60% utilization.

A. Buy more commitments to bring the average discount up, since the unused portion will be filled as the workloads grow later in the year and prices only rise
B. Investigate: the workload changed or was rightsized after purchase; consider exchanging where allowed, and reduce future commitment scope
C. Ignore it because 60% is within the normal range for a commitment
D. Cancel all commitments immediately and return to on-demand pricing

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Utilization and coverage are the two commitment metrics: utilization is how much of what you bought you used, coverage is how much of your eligible usage a commitment covers. Low utilization is unused spend; low coverage is a missed discount opportunity.
</details>

---

### Question 9
**Scenario:** Anomaly detection flags a spend spike.

A. Reduce budgets for the owning team to discourage further spikes, before anyone has checked what caused the extra spend
B. Wait for the invoice at the end of the month to confirm the amount, because alerts are often wrong and could waste time
C. Triage it: confirm whether it is legitimate growth, a misconfiguration, a forgotten test environment, or a security incident, then route it to the owning team
D. Assume it is an error in the billing data and dismiss the alert, since a spike most often comes from a data glitch

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Not every spike is waste; a successful launch looks the same in the data. Cryptomining after a credential compromise also appears as a spend anomaly, which is why FinOps anomaly triage sometimes hands off to security rather than to engineering.
</details>

---

### Question 10
**Scenario:** Forecasting next quarter's spend.

A. Ask each team for a number and add them together, which captures local knowledge but ignores trends and commitment changes
B. Use the budget as the forecast, because it has already been approved and represents the amount the business expects to spend
C. Use last month multiplied by three, which assumes flat usage and misses growth, launches, and expiring commitments
D. Combine historical trend, known planned changes (launches, migrations, decommissions), and commitment expirations, then track forecast accuracy over time

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Trend alone misses planned events, which are exactly what makes a forecast wrong. Tracking accuracy is what improves the method: a forecast nobody checks afterwards never gets better.
</details>

---

### Question 11
**Scenario:** Who are the FinOps personas the framework names?

A. Only engineering and finance, since those two groups produce and pay for the spend and everyone else is a consumer of reports
B. Only the FinOps team, which owns the data and the process for all cost decisions on behalf of the rest of the company
C. Engineering, finance, procurement, leadership, product, and FinOps practitioners
D. Only finance, because it holds the budget and the invoices

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The framework is explicitly cross-functional, and much of the analyst's job is translation: engineering wants efficiency levers, finance wants predictability, leadership wants unit economics. The same underlying data serves all three in different presentations.
</details>

---

### Question 12
**Scenario:** Non-production environments run 24 hours a day but are used during business hours.

A. Nothing can be done because the environments must be available at any time in case a developer needs to test something at night
B. Buy commitments for them, which lowers the hourly rate but still pays for every idle night and weekend hour of capacity
C. Rightsize them to smaller instances, which lowers the hourly cost but leaves them running around the clock when nobody is using them
D. Schedule shutdown outside working hours, which is one of the highest-return, lowest-risk optimizations available

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Non-production often runs at roughly a quarter of the hours it is billed for. It is also the safest place to start a FinOps program, because the blast radius of getting it wrong is a developer waiting for an environment rather than a customer outage.
</details>

---

### Question 13
**Scenario:** Which describes the FOCUS specification?

A. An open specification for a common cost and usage data format across providers
B. A tagging standard that defines the required keys and values for allocation, which helps grouping but does not define the billing data format
C. A pricing model that describes how providers charge for compute, storage and network, including on-demand and commitment rates
D. A discount program run by cloud providers for customers who commit to a minimum annual spend over several years

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** FOCUS normalizes billing data so multicloud analysis does not require a per-provider translation layer. It matters most for organizations reporting across clouds, where each provider's native format uses different column names and semantics for the same concepts.
</details>

---

### Question 14
**Scenario:** Engineering resists a cost reduction because it risks reliability.

A. Escalate to finance so that they can decide on the savings, even though they do not know the reliability needs of the workload
B. Mandate the change from leadership, since cost goals are set at the top and engineering must find a way to meet them
C. Treat it as a trade-off decision with the business: quantify the saving against the reliability risk, and let the workload's criticality decide
D. Drop the initiative, because reliability always outweighs savings and no change should be made if an engineer objects to it, whatever the size of the saving

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A FinOps principle states that a business value decision, not a cost minimum, is the goal. Sometimes the right answer is to spend more. Framing it as a trade-off rather than a mandate is also what preserves the engineering relationship the practice depends on.
</details>

---

### Question 15
**Scenario:** Which capability makes optimization continuous rather than a one-off project?

A. An annual review of cloud spend with leadership, which finds savings once a year but leaves waste to grow for the other eleven months
B. A cost dashboard that shows spend by team, which provides visibility but changes no behavior
C. A single optimization sprint led by a central team, which captures savings once and then decays
D. Operate-phase practices: automated policies, embedded cost checks in delivery, regular cadence reviews, and metrics with owners

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** One-off exercises decay because new resources arrive constantly. The Operate phase is about making the behavior structural, which is also why architecture and delivery process are FinOps concerns rather than purely financial ones.
</details>

---

### Question 16
**Scenario:** A new analyst is mapping FinOps Framework capabilities to domains. Planning and estimating, forecasting, budgeting, benchmarking, and unit economics all sit in the same domain. Which one?

A. Understand Usage and Cost
B. Optimize Usage and Cost
C. Manage the FinOps Practice
D. Quantify Business Value

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Quantify Business Value groups the capabilities that connect spend to plans and outcomes: planning and estimating, forecasting, budgeting, benchmarking, and unit economics. Understand Usage and Cost covers ingestion, allocation, reporting, and anomaly management. Optimize Usage and Cost covers rate and usage optimization. Manage the FinOps Practice covers the operating model, education, and policy.

**Key Concept:** Four domains organise the capabilities; every phase touches all four. See [FinOps Framework domains](https://www.finops.org/framework/domains/).
</details>

---

### Question 17
**Scenario:** A company is deciding which optimization decisions to centralize and which to leave with product teams. Which split matches common FinOps practice?

A. Commitment and rate decisions sit centrally, while usage decisions such as rightsizing stay with engineering teams
B. Usage decisions sit centrally, while each engineering team buys its own commitments for its own accounts
C. Both rate and usage decisions sit centrally, so engineering teams never need to see cost data
D. Both rate and usage decisions sit with each team, and the central team only pays the invoice

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Rate optimization benefits from pooling: a central team sees aggregate usage and buys commitments that cover it with less risk of waste. Usage optimization needs the engineers who know the workload. Teams buying their own commitments fragment coverage and leave capacity unused. Centralizing everything removes ownership, and fully decentralizing leaves no one to manage rates.

**Key Concept:** A centralized team drives FinOps, while everyone takes ownership of their usage. See [FinOps principles](https://www.finops.org/framework/principles/).
</details>

---

### Question 18
**Scenario:** Monthly tag audits keep finding 25% of new resources without a `cost-center` tag, and the analyst spends days retagging them. What change most reduces the problem?

A. Run the audit weekly instead of monthly so missing tags are found sooner
B. Ask each team lead to sign off that their resources are tagged each quarter
C. Enforce the tag at provisioning time with policy and infrastructure as code
D. Allocate every untagged resource to the platform team by default each month

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Preventing untagged resources at creation, through policy-as-code, required tags in IaC modules, or provider tag policies, fixes the cause rather than the symptom. A faster audit still leaves manual retagging. Sign-offs rely on memory and do not stop new gaps. Dumping untagged cost on one team hides the problem and makes that team's numbers wrong.

**Key Concept:** Proactive allocation through enforced tagging beats reactive cleanup. See [Allocation capability](https://www.finops.org/framework/capabilities/allocation/).
</details>

---

### Question 19
**Scenario:** The organisation pays a monthly enterprise support fee that cannot be tagged to any resource. Five product teams use the cloud. Which allocation approach is most defensible?

A. Charge the entire fee to the team with the most support cases logged this month
B. Spread the fee across teams in proportion to each team's share of direct cloud spend
C. Leave the fee unallocated, since it does not belong to any resource or team at all
D. Split the fee equally five ways, because each team has equal access to support

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Proportional allocation based on direct spend is the standard, transparent method for shared costs without a better driver, because support fees often scale with spend. Charging one team on case count swings wildly month to month. Leaving shared costs unallocated hides part of the true cost of every product. An equal split overcharges small teams and undercharges large ones.

**Key Concept:** Shared costs are split evenly, proportionally, or by a fixed agreed ratio; agree the method up front. See [Allocation capability](https://www.finops.org/framework/capabilities/allocation/).
</details>

---

### Question 20
**Scenario:** Tag coverage on legacy resources is poor, but every product team already has its own set of accounts and subscriptions. What is the most reliable allocation key for that legacy spend while tagging improves?

A. Resource names, parsed with naming patterns that guess the owning product
B. The engineer who created each resource, taken from the provider's audit logs
C. The region each resource runs in, since most teams deploy to one region
D. The account and subscription hierarchy, mapped to the team that owns each one

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Account, subscription, or project boundaries are assigned to every resource automatically and cannot be forgotten, so mapping them to owners gives a reliable baseline. Name parsing is guesswork. The creating engineer may have changed teams or left, and audit logs are not kept forever. Regions are shared by many teams.

**Key Concept:** Use the hierarchy as the first allocation layer and tags for finer detail. See [Allocation capability](https://www.finops.org/framework/capabilities/allocation/).
</details>

---

### Question 21
**Scenario:** Compute spend rose 18% month over month. Finance asks why. What is the most useful way to break the variance down?

A. Split the change into rate effects, usage volume effects, and mix effects across services
B. Report the 18% figure against budget and flag whether it breached the threshold
C. List the ten most expensive resources this month alongside their total cost
D. Compare the increase with the cloud market's overall growth rate for the year

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Variance analysis separates what changed: unit prices (for example, an expired commitment), how much was used, and which services or instance types the usage moved to. That tells finance whether the cause was a decision, growth, or waste. A budget flag says that it changed, not why. A top-ten list shows where money goes, not what moved. Market growth has no bearing on this company's bill.

**Key Concept:** Explain variance as price, volume, and mix so the right owner acts. See [Reporting and Analytics capability](https://www.finops.org/framework/capabilities/reporting-analytics/).
</details>

---

### Question 22
**Scenario:** A static daily alert for "spend above $5,000" fires every Monday when batch jobs run, and engineers have started ignoring it. A real spike last Thursday went unnoticed. What should the analyst change?

A. Raise the static threshold to $8,000 so that Monday batch runs stop firing it
B. Use baseline detection that learns weekly seasonality and alerts on deviation
C. Send the alert to the finance team instead, who are less likely to ignore it
D. Turn the alert off on Mondays and keep the same $5,000 threshold for other days

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Spend has normal weekly patterns, and detection that learns the baseline and seasonality flags real deviations without paging on expected peaks. Raising a static threshold hides real spikes on quiet days. Sending alerts to finance moves them away from the engineers who can act. Muting Mondays means a real Monday spike is never caught.

**Key Concept:** Good anomaly detection is accurate, timely, and routed to the owner who can act. See [Anomaly Management capability](https://www.finops.org/framework/capabilities/anomaly-management/).
</details>

---

### Question 23
**Scenario:** A team bought a one-year, all-upfront compute commitment in January. Their January cost report shows a huge spike, and the rest of the year looks cheap. How should the analyst present the team's cost?

A. Show the purchase in January only, since that is when the money left the bank
B. Remove the commitment from reports, because prepaid costs are not cloud costs
C. Use the amortized view that spreads the upfront fee across the twelve months
D. Report on-demand list prices all year so that the commitment does not distort trends

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Amortized cost spreads the upfront payment across the commitment term, so each month carries its fair share and trends stay meaningful. The cash view is right for finance's cash flow but distorts team-level trends. Removing commitments understates real cost. List prices overstate cost and hide the savings the commitment delivers.

**Key Concept:** Use billed cost for invoices and cash; use amortized cost for team reporting and trends. See [FOCUS specification](https://focus.finops.org/).
</details>

---

### Question 24
**Scenario:** Leadership wants to move from showback to chargeback next quarter. Currently 35% of spend is unallocated, and teams dispute several allocation rules. What should the analyst advise?

A. Start chargeback now and put the unallocated 35% on the central IT budget
B. Start chargeback now for the 65% that is allocated and decide on the rest later
C. Delay chargeback indefinitely, because chargeback never works in large companies
D. Raise allocation accuracy and agree the rules with teams before money moves

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Chargeback moves real budget, so teams must trust the numbers and accept the rules first; high unallocated spend and open disputes mean the data is not ready. Charging partial or approximate numbers creates arguments and erodes trust in the whole practice. Chargeback is common and workable once allocation is mature; the issue is readiness, not size.

**Key Concept:** Showback builds trust in the data; chargeback depends on it. See [Invoicing and Chargeback capability](https://www.finops.org/framework/capabilities/invoicing-chargeback/).
</details>

---

### Question 25
**Scenario:** A central FinOps team buys savings plans for the whole company. Product teams are charged back monthly. How should commitment costs and benefits appear in the teams' chargeback?

A. Charge each team the effective discounted rate for its covered usage, and hold unused commitment centrally
B. Charge the full upfront amount to whichever team first asked for the commitment to be purchased
C. Charge teams nothing for any usage the commitment covers, because the purchase was made centrally
D. Split the total commitment cost equally among all teams, regardless of how much each one used

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Charging the effective rate passes the discount to the teams whose usage earned it, keeps costs comparable month to month, and leaves the central team accountable for commitments that go unused. Charging the requesting team penalises them for a company-wide decision. Zero cost for covered usage hides real cost and kills incentives to optimize. An equal split ignores consumption.

**Key Concept:** Allocate commitment benefits to consumers and commitment waste to the owner of the purchase decision. See [Rate Optimization capability](https://www.finops.org/framework/capabilities/rate-optimization/).
</details>

---

### Question 26
**Scenario:** A payments company wants one unit metric to track cloud efficiency for its core platform, whose cost scales mostly with payment volume. Which metric fits best?

A. Cloud cost per employee in the company
B. Cloud cost per 1,000 payment transactions processed
C. Cloud cost as a percentage of total IT budget
D. Cloud cost per virtual machine running in production

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A good unit metric divides cost by a business driver that the cost actually scales with and that the business cares about; payment transactions are both. Headcount does not drive platform cost. A percentage of IT budget measures budget share, not efficiency. Cost per VM is a technical ratio that can improve while the business gets worse value.

**Key Concept:** Unit economics ties spend to business value, so growth in spend can be judged. See [Unit Economics capability](https://www.finops.org/framework/capabilities/unit-economics/).
</details>

---

### Question 27
**Scenario:** Last month the platform cost $100,000 for 2,000,000 transactions. This month it cost $90,000 for 1,500,000 transactions. What happened to unit cost?

A. It fell by 10%, from $0.05 to $0.045 per transaction
B. It stayed flat at $0.05 per transaction in both months
C. It rose by 20%, from $0.05 to $0.06 per transaction
D. It rose by 25%, from $0.05 to $0.0625 per transaction

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** $100,000 / 2,000,000 = $0.05, and $90,000 / 1,500,000 = $0.06, a 20% rise. Total cost fell, but volume fell faster, so efficiency got worse. A 10% fall confuses total cost with unit cost. A flat result ignores the volume drop. $0.0625 would need $93,750 of cost.

**Key Concept:** Falling total spend can hide worsening unit economics. See [Unit Economics capability](https://www.finops.org/framework/capabilities/unit-economics/).
</details>

---

### Question 28
**Scenario:** The commitment dashboard shows 98% utilization and 45% coverage for steady compute. What does this suggest?

A. Existing commitments are well used, and there is room to cover more steady usage
B. Too many commitments were bought, and some should be sold or exchanged quickly
C. Coverage and utilization are both healthy, so no further action is needed now
D. Utilization is too high, which signals a risk of paying for unused capacity

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Utilization measures how much of the purchased commitment is used; 98% means little waste. Coverage measures how much eligible usage is covered; 45% means over half of steady usage still pays on-demand. Over-buying would show low utilization, not high. Leaving 55% uncovered on a steady workload is a missed saving. High utilization is the opposite of paying for unused capacity.

**Key Concept:** Track utilization (waste) and coverage (opportunity) together. See [Rate Optimization capability](https://www.finops.org/framework/capabilities/rate-optimization/).
</details>

---

### Question 29
**Scenario:** An analyst is building a FOCUS-based report and wants cost that reflects negotiated discounts, commitment discounts, and amortized upfront fees. Which FOCUS column fits?

A. ListCost
B. BilledCost
C. ContractedCost
D. EffectiveCost

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** EffectiveCost is the amortized cost after all discounts, including the share of upfront commitment fees. BilledCost is what appears on the invoice, so upfront fees land in the purchase month. ListCost is at public list prices. ContractedCost applies negotiated rates but not commitment amortization.

**Key Concept:** FOCUS defines several cost columns for different questions; pick the one that matches the audience. See [FOCUS specification](https://focus.finops.org/).
</details>

---

### Question 30
**Scenario:** A FOCUS dataset contains usage rows plus tax, credit, and commitment purchase rows. The analyst wants to study only consumption of cloud resources. Which filter is correct?

A. `ServiceCategory = 'Compute'`
B. `ChargeCategory = 'Usage'`
C. `ChargeFrequency = 'One-Time'`
D. `BilledCost > 0`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** ChargeCategory classifies each row as Usage, Purchase, Tax, Credit, or Adjustment, so filtering on Usage isolates consumption. ServiceCategory narrows to one kind of service but still includes non-usage rows. One-time charges are mostly purchases and fees, the opposite of what is wanted. A positive billed cost keeps taxes and purchases and drops usage fully covered by commitments.

**Key Concept:** Use ChargeCategory to separate consumption from purchases, taxes, and credits. See [FOCUS specification](https://focus.finops.org/).
</details>

---

## Where to go deeper

- [FOCA cert page](../../exams/finops/certified-analyst/) - notes, practice plan, strategy
- [FinOps Certified Practitioner practice questions](./finops-certified-practitioner.md) - the foundation level
- [Cloud cost basics](../../learn/concepts/cloud-cost-basics.md) - plain-English primer
- [FinOps topic index](../../topics/finops.md) - the cert family in context
- **[📖 FinOps Foundation](https://www.finops.org/)** - the framework and certification pages
