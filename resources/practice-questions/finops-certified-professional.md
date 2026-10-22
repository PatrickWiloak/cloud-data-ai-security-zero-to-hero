---
last-updated: 2026-10-22
difficulty: advanced
---

# FinOps Certified Professional (FOCP-Pro) - Practice Questions

30 questions at professional level: running a FinOps practice, not just performing its tasks. Covers operating model, maturity, cross-functional influence, and scaled governance.

> **Cert page:** [exams/finops/certified-professional/](../../exams/finops/certified-professional/)

---

### Question 1
**Scenario:** A new FinOps practice is being stood up. What comes first?

A. Negotiate commitments with the cloud providers before usage is understood
B. Establish allocation and visibility; nobody can act on unseen cost
C. Set cost reduction targets for every team before the allocation model is agreed
D. Buy a cost management tool and connect every account, so dashboards exist before any allocation model is argued over

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The Inform phase is first for a reason: targets set before allocation is trustworthy produce arguments about the numbers rather than action. Buying tooling before deciding the allocation model usually means configuring the tool twice.
</details>

---

### Question 2
**Scenario:** Which describes the FinOps maturity model?

A. A vendor assessment
B. Crawl, Walk, Run applied per capability, so an organization sits at different levels for different capabilities
C. The FinOps lifecycle of Inform, Optimize and Operate, which every team completes once, in that order, and is then considered fully mature
D. A certification level

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Maturity is per capability, which matters practically: a team can be at Run for allocation and Crawl for forecasting. Chasing Run everywhere at once is how practices stall; picking the capability whose immaturity is currently costing most is how they progress.
</details>

---

### Question 3
**Scenario:** Engineering treats FinOps as the cost police.

A. Enforce harder, by adding automated shutdowns and a weekly report naming every team that exceeded its tagged budget
B. Escalate to leadership and ask executives to require that every team cut spend by a fixed percentage each quarter, with exceptions approved by finance
C. Reframe it as enablement: give engineers the data and tooling they want and celebrate wins
D. Set mandatory spending quotas for each team and block any deployment that would take the team over its quota this month

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Adoption is the binding constraint on a FinOps practice, and enforcement without relationship produces compliance theatre: tags applied meaninglessly, recommendations dismissed. The principle that FinOps optimizes for business value, sometimes by spending more, is the reframing that lands.
</details>

---

### Question 4
**Scenario:** A commitment portfolio must be managed across a large estate.

A. Avoid commitments entirely and stay on on-demand pricing for flexibility
B. Buy annually in one purchase at the start of the fiscal year to get the best discount
C. Centralize commitment management so it can be pooled across teams, with laddered expiries and continuous utilization tracking
D. Each team buys its own to match its budget

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Pooling raises utilization because one team's shortfall offsets another's excess. Laddering expiries avoids a cliff where a large share of the portfolio renews at once, which is both a budget shock and a negotiation weakness.
</details>

---

### Question 5
**Scenario:** Shared costs (support, networking, shared clusters, observability tooling) must be allocated.

A. Leave them unallocated
B. Charge them to the FinOps team
C. Split by headcount in every case, since headcount is easy to audit and every team agrees on its own team size
D. Choose and document a method, such as proportional to direct spend, and apply it consistently

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** No method is objectively correct, so consistency and transparency matter more than precision. What breaks trust is changing the method quietly, which makes teams' month-over-month numbers move for reasons they cannot explain.
</details>

---

### Question 6
**Scenario:** Unit economics must be established for a multi-product organization.

A. Per-product unit metrics tied to how each product creates value
B. Total monthly spend per product, compared across all products on the same scale
C. Cloud cost per employee, reported for the whole organization every quarter
D. One organization-wide metric such as total cost divided by total revenue, applied to every product

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A single metric across dissimilar products compares nothing useful. The value of unit economics is that it makes a rising bill defensible: cost per transaction falling while spend rises is a growth story rather than a waste story.
</details>

---

### Question 7
**Scenario:** Cloud spend must be forecast for annual budgeting.

A. Ask the provider
B. Combine bottom-up team forecasts with top-down trend analysis, include launches and migrations, track accuracy
C. Use last year's spend plus a flat 10% for growth, then lock the number for the whole year and report any overrun to finance as a variance
D. Extrapolate the trend from the last six months of billing data and add a fixed buffer for growth and expected price changes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Bottom-up captures planned events that trend analysis cannot see; top-down catches the optimism in team estimates. Reconciling the two is the professional-level skill, and measured accuracy is what makes the next cycle better.
</details>

---

### Question 8
**Scenario:** A multicloud estate must be reported on consistently.

A. Separate reports per provider
B. Report only the largest provider
C. Convert every provider's usage to normalized instance hours, since compute is the one unit all providers bill in a comparable way
D. Normalize to a common data model, ideally the FOCUS specification, so unit metrics are comparable across providers

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Each provider's billing export uses different column names and semantics for the same concepts, so per-provider reports cannot be compared without a translation layer. FOCUS is that layer as an open specification rather than a bespoke internal one.
</details>

---

### Question 9
**Scenario:** Governance must prevent waste without blocking delivery.

A. Manual approval for every new resource by the central cloud team, with finance reviewing each request against the quarterly budget before launch
B. Guardrails: policy limits, mandatory tagging at creation, budget alerts, and automated cleanup
C. Quarterly audits only
D. No controls, trusting engineers to clean up what they launch and finance to spot anything unusual on the invoice

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Guardrails preserve self-service within bounds, which is the model that survives contact with engineering. Manual approval moves the bottleneck to a person and gets routed around; quarterly audits find the waste after months of paying for it.
</details>

---

### Question 10
**Scenario:** Leadership asks for a 20% cost reduction target.

A. Refuse
B. Accept the target and ask each team to pledge its own saving, with the pledges totalled and reported monthly
C. Apply it uniformly across teams, so every team cuts 20% of its own spend and the target is met fairly in every cost center, with progress reported monthly to the executive sponsor
D. Analyze where waste sits, propose owned initiatives, and flag where the target harms value

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A uniform cut punishes efficient teams and rewards wasteful ones, since the efficient team has nothing easy left to give. Making the trade-off visible where the target conflicts with growth is the practitioner's job, not resistance to it.
</details>

---

### Question 11
**Scenario:** Sustainability reporting is added to the FinOps remit.

A. Unrelated to FinOps
B. Closely related: the same usage data underpins carbon and cost reporting, and many efficiency actions cut them together, though they sometimes diverge
C. Replaces cost reporting
D. Only relevant to hardware, because carbon emissions come from the manufacture and shipping of physical servers rather than from how cloud workloads are scheduled and sized

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Rightsizing, decommissioning, and workload scheduling improve both. Divergence appears in regional placement, where the cheapest region and the lowest-carbon region are frequently different, which is a business trade-off rather than an optimization.
</details>

---

### Question 12
**Scenario:** A FinOps practice must scale beyond a central team.

A. Embed champions in engineering teams, provide self-service data and tooling, and keep the central function on negotiation and standards
B. Centralize all decisions in the FinOps team so every purchase and design choice gets one consistent review
C. Outsource it
D. Hire more central practitioners until each one covers about ten engineering teams

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A central team scaling linearly with the estate becomes the bottleneck. The federated model puts decisions with the teams that make the technical choices, while centralizing the things that genuinely benefit from scale: contracts, tooling, and standards.
</details>

---

### Question 13
**Scenario:** Which metric best indicates the FinOps practice itself is working?

A. A portfolio: unit cost trend, allocation coverage, commitment utilization, forecast accuracy, time to act
B. Number of optimization recommendations generated by the tooling each month, plus the count of dashboards published to teams
C. Tool count
D. Total spend reduction year on year, measured across the invoices of all accounts and business units, with a target set by finance

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Total spend can fall for reasons unrelated to the practice, or rise while efficiency improves. Recommendation counts measure activity rather than outcome. Time to act is the one that reveals whether insight is converting into change.
</details>

---

### Question 14
**Scenario:** A large migration is planned and finance wants cost certainty.

A. Use the on-premises cost as the estimate, adjusted by the vendor's published list-price discount for the chosen instance types and applied uniformly to every workload in the migration plan
B. Promise one fixed number to finance now and hold every team to it for the whole migration, whatever the migration reveals
C. Provide a modeled range with stated assumptions, variance drivers, and regular re-forecasts against actuals
D. Refuse to give any estimate until the migration is finished and actual costs have been measured for a full quarter

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A range with named assumptions is honest and actionable; a single number is a hostage. Using the on-premises cost as the estimate is the specific trap, because lifting and shifting an over-provisioned estate reliably costs more, not less, until it is rightsized.
</details>

---

### Question 15
**Scenario:** Two teams dispute how a shared platform's cost is allocated to them.

A. Return to the documented method, check whether usage data supports a better split, and if it is wrong, change it transparently and restate prior periods
B. Escalate to leadership and let the executive sponsor decide the split
C. Leave it unallocated
D. Split it evenly and move on, noting the decision in the next quarterly review

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Allocation disputes are usually data disputes in disguise. Restating prior periods when the method changes is what preserves trust; changing it silently makes every team's historical trend meaningless and invites the next dispute.
</details>

---

### Question 16
**Scenario:** A FinOps practice built for public cloud is asked to cover SaaS subscriptions, software licensing, and the remaining data center as well. Leadership asks how the framework handles this without starting a second practice. What is the best answer?

A. Run a separate practice per technology, each with its own principles and team
B. Map all non-cloud spend onto cloud billing accounts so the cloud tools can see it
C. Define Scopes that apply the same capabilities to each segment of technology spend
D. Leave non-cloud spend to procurement, since FinOps applies only to public cloud

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The current framework uses Scopes: defined segments of technology spend, aligned to business constructs, that shape how each capability is applied, including how often and how strictly. One practice can then cover cloud, SaaS, licensing, and data center with different depths. Separate practices duplicate effort and split the data. Forcing other spend into cloud accounts distorts the data. FinOps explicitly extends beyond public cloud.

**Key Concept:** Scopes let one practice govern many kinds of technology spend. See [FinOps Scopes](https://www.finops.org/framework/scopes/).
</details>

---

### Question 17
**Scenario:** A new recommendation feature will double its product line's cloud cost. The FinOps team has the cost data and forecasts. Who should decide whether the extra cost is worth it?

A. The FinOps practitioner, because they understand the cost data in most depth
B. Procurement, because they negotiate rates with the cloud providers
C. Finance, because they own the budget the extra cost will come from
D. The product owner, informed by FinOps data and engineering trade-offs

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Business value decisions sit with the people accountable for the product's outcomes, and the framework's principle is that business value drives technology decisions. FinOps supplies the data, forecasts, and unit economics but enables rather than decides. Procurement shapes rates, not product choices. Finance sets and tracks budgets but is not best placed to judge feature value.

**Key Concept:** FinOps informs decisions; the accountable business owner makes them. See [FinOps personas](https://www.finops.org/framework/personas/).
</details>

---

### Question 18
**Scenario:** A company bought all of its three-year commitments in one week two years ago. Next year they all expire at once, and the workload mix has changed a lot. How should the commitment strategy change for the future?

A. Buy in smaller tranches on a regular schedule so expiries are staggered over time
B. Renew everything in one purchase on the expiry date to keep the same discount
C. Let all commitments lapse and run fully on-demand to avoid any future lock-in
D. Switch everything to one-year terms bought in a single purchase each January

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Laddering purchases over time spreads expiries, lets each tranche match the current workload, and avoids a cliff where coverage drops all at once. Renewing in one block repeats the same risk. Going fully on-demand gives up large savings on steady usage. One annual block still creates a yearly cliff and a single point of misjudgment.

**Key Concept:** Manage commitments as a rolling portfolio, not a one-off purchase. See [Rate Optimization capability](https://www.finops.org/framework/capabilities/rate-optimization/).
</details>

---

### Question 19
**Scenario:** A company is moving Windows Server and SQL Server workloads to Azure. It already owns many of those licenses with active Software Assurance. Which rate lever should the FinOps lead raise first?

A. Spot virtual machines for every SQL Server database tier
B. Azure Hybrid Benefit to reuse eligible licenses on Azure
C. Moving the workloads to Linux before migration in all cases
D. Buying new pay-as-you-go licenses bundled with each VM

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Azure Hybrid Benefit lets eligible Windows Server and SQL Server licenses with Software Assurance or qualifying subscriptions be applied on Azure, removing the license portion of the VM or database price. Spot VMs can be evicted and do not suit database tiers. Re-platforming to Linux may help later but is a large project, not a rate lever. Paying again for bundled licenses wastes licenses already owned.

**Key Concept:** Licensing is often the largest rate lever in a Microsoft-heavy migration. See [Azure Hybrid Benefit](https://azure.microsoft.com/en-us/pricing/hybrid-benefit/).
</details>

---

### Question 20
**Scenario:** A cloud provider offers a larger discount for a higher committed spend over three years. The base forecast is $30M, the conservative case is $24M, and the optimistic case is $40M. Which commitment level is most defensible?

A. $40M, because the extra discount pays for itself if growth matches the plan
B. $30M, because the base forecast is the most likely single outcome
C. A level at or below the conservative case, accepting a smaller discount
D. No spend commitment at all, since any forecast for three years is unreliable

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A spend commitment shortfall is usually paid anyway, so the downside of over-committing is pure waste while the upside of a bigger discount is only a few points. Committing at or below the conservative case keeps most of the discount with little shortfall risk. Committing to the optimistic or base case bets on growth that may not come. Refusing any commitment gives up a real saving on spend that is very likely.

**Key Concept:** Size commitments to the spend you are confident of, not the spend you hope for. See [Rate Optimization capability](https://www.finops.org/framework/capabilities/rate-optimization/).
</details>

---

### Question 21
**Scenario:** An internal reporting API runs on six always-on instances. Average utilization is 2%, with short bursts during business hours and almost no traffic at night. What is the most effective architectural change?

A. Buy three-year commitments for the six instances to lower their hourly rate
B. Rightsize the six instances to the smallest size and keep them always on
C. Move the instances to a cheaper region with the same always-on setup
D. Move to a scale-to-zero model such as serverless functions or containers

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** At 2% average use with bursts, paying for capacity by the hour is the core waste; a scale-to-zero model charges for actual requests and handles bursts automatically. Commitments discount idle capacity instead of removing it. Rightsizing helps a little but still pays for idle hours and may struggle with bursts. A region move cuts price slightly and may add latency and data transfer.

**Key Concept:** Architecture sets the cost floor; match the pricing model to the traffic shape. See [Architecting for Cloud capability](https://www.finops.org/framework/capabilities/architecting-for-cloud/).
</details>

---

### Question 22
**Scenario:** A rightsizing program publishes 400 recommendations a month in a dashboard. After six months, under 10% have been acted on. What change most improves results?

A. Push prioritized recommendations into each team's backlog with an owner and track realized savings
B. Publish the dashboard more often, so that teams always see the latest recommendations
C. Let the central FinOps team apply all recommendations directly in production accounts
D. Add more recommendation types to the dashboard so teams have a wider choice of savings

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Recommendations get acted on when they arrive in the tools engineers already use, ranked by value and effort, with clear ownership and visible results. More frequent dashboards do not change behaviour. Central changes in production bypass the people who know the workload and risk outages. More recommendation types add noise to a backlog already ignored.

**Key Concept:** Optimization works when it is part of engineering workflow, not a separate report. See [Workload Optimization capability](https://www.finops.org/framework/capabilities/workload-optimization/).
</details>

---

### Question 23
**Scenario:** A SQL Server database on EC2 is licensed per vCPU. It needs a large amount of memory but uses little CPU. Licensing is now larger than compute cost. What is the most cost-effective option?

A. Move to a compute-optimized instance with more vCPUs for headroom
B. Keep the current instance and buy a three-year commitment to cover it
C. Use a memory-optimized instance and reduce active vCPUs with Optimize CPUs
D. Split the database across several smaller instances with one vCPU each

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Memory-optimized instances give more memory per vCPU, and the EC2 Optimize CPUs feature lets you run fewer active vCPUs than the default, which cuts per-vCPU license cost while keeping the memory. A compute-optimized type adds vCPUs and so adds licensing. A commitment lowers compute cost but not licensing. Splitting one database across tiny instances is a major redesign and often needs more total licenses.

**Key Concept:** For per-core licensed software, rightsize the license footprint, not only the instance. See [Optimize CPU options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html).
</details>

---

### Question 24
**Scenario:** The CFO wants to compare how much each cloud provider's discounts are saving, across AWS, Azure, and Google Cloud, on one consistent measure. The FinOps team already has FOCUS-formatted data from all three. What should they report?

A. Each provider's own savings figure from its console, placed side by side
B. Total billed cost per provider, since lower bills mean better discounts
C. The count of active commitments per provider, as a proxy for savings
D. An effective savings rate computed from ListCost and EffectiveCost per provider

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** FOCUS gives every provider the same ListCost and EffectiveCost columns, so the gap between them, as a share of list cost, is a consistent effective savings rate across clouds. Console figures use different definitions and are not comparable. Billed cost reflects usage size as much as discounts. Commitment counts say nothing about value.

**Key Concept:** A common schema enables common KPIs across providers. See [FOCUS specification](https://focus.finops.org/).
</details>

---

### Question 25
**Scenario:** A multinational's FOCUS dataset includes rows billed in USD, EUR, and JPY. Executives want one global cost view in USD. How should the team handle currency?

A. Add the cost columns together as they are, since currency differences are small overall
B. Use the BillingCurrency column to convert each row to USD with an agreed, documented rate method
C. Drop the non-USD rows from the executive view, since they come from local subsidiaries
D. Ask each provider to rebill all accounts in USD before any global reporting is done

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** FOCUS records the currency of each row in BillingCurrency, so the team can convert to a reporting currency using one agreed method, such as a monthly finance rate, applied consistently. Summing mixed currencies produces meaningless totals. Dropping rows understates global cost. Rebilling is often not possible and would break local finance processes.

**Key Concept:** Normalization includes currency, and the conversion method must be agreed with finance. See [FOCUS specification](https://focus.finops.org/).
</details>

---

### Question 26
**Scenario:** Launch of a FinOps practice has stalled for two months over whether the team should report to the CFO or the CTO. What is the most useful advice?

A. Secure an executive sponsor and a cross-functional mandate first; either reporting line can work
B. Place the team under the CFO, because FinOps is mainly a finance discipline
C. Place the team under the CTO, because only engineering can change cloud usage
D. Wait until the next reorganisation so the team can be placed in the right unit

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Successful practices sit under finance, technology, or a shared office; what predicts success is executive sponsorship and a mandate that spans finance, engineering, and product. Insisting that FinOps is mainly finance, or mainly engineering, ignores its cross-functional nature. Waiting for a reorganisation delays value with no benefit.

**Key Concept:** Executive sponsorship and cross-functional authority matter more than the org chart box. See [FinOps Practice Operations capability](https://www.finops.org/framework/capabilities/finops-practice-operations/).
</details>

---

### Question 27
**Scenario:** A policy blocks GPU instance types in non-production accounts. A research team needs GPUs in a sandbox for a six-week evaluation. How should governance handle the request?

A. Reject it, because exceptions weaken every policy over time
B. Remove the GPU policy for all teams, since one team has a valid need
C. Grant a time-bound exception with an owner, a budget, and a review date
D. Let the team run the evaluation in production, where GPUs are allowed

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Good governance enables delivery: a documented, time-limited exception with an owner and budget allows the work while keeping the guardrail for everyone else and making sure the exception ends. Blanket rejection pushes teams to work around policy. Removing the policy for all loses the control. Running experiments in production adds risk and muddles allocation.

**Key Concept:** Policies need an exception path, or teams route around them. See [Policy and Governance capability](https://www.finops.org/framework/capabilities/policy-governance/).
</details>

---

### Question 28
**Scenario:** Leadership wants actions that reduce both cloud cost and cloud carbon emissions, without trade-offs between the two. Which action fits best?

A. Moving all workloads to the region with the lowest grid carbon, even if it costs more
B. Buying three-year commitments for all steady workloads to cut the rate paid
C. Replicating all data to a second region for faster recovery after a disaster
D. Removing idle resources and rightsizing over-provisioned ones across the estate

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Idle and oversized resources consume energy and money for no value, so removing them cuts both. A low-carbon region may cost more and add latency, which is a real trade-off. Commitments cut price but not energy use. Extra replication improves resilience but adds both cost and emissions.

**Key Concept:** Waste reduction is where cost and sustainability goals align most directly. See [Cloud Sustainability capability](https://www.finops.org/framework/capabilities/cloud-sustainability/).
</details>

---

### Question 29
**Scenario:** A generative AI support assistant sends every request to the largest, most expensive model. Cost per conversation has tripled since launch. Most requests are simple FAQ lookups. What is the most effective first lever?

A. Measure cost per request by task type and route simple requests to a smaller, cheaper model
B. Buy reserved GPU capacity and move the model to self-hosting before measuring anything
C. Cap each user at five conversations a month so that total spend stays inside budget
D. Switch to the newest, largest model release, which is usually cheaper per token than older ones

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Model choice is usually the biggest cost driver for AI features, and routing simple tasks to smaller models cuts cost sharply while keeping quality where it matters. Measuring by task type first shows where routing pays. Self-hosting is a large commitment that needs usage data first. Capping users harms the product. Larger models generally cost more per token, not less.

**Key Concept:** In AI FinOps, cost per outcome and model selection are the core levers. See [FinOps Scopes](https://www.finops.org/framework/scopes/).
</details>

---

### Question 30
**Scenario:** An AI inference service runs at steady, high volume around the clock and pays on-demand per token. Volume has been stable for six months. What should the FinOps lead evaluate?

A. Moving the service to spot GPU capacity, since inference can always be retried
B. Provisioned or committed throughput priced by capacity, if utilization stays high
C. Keeping on-demand pricing, because AI services never offer committed pricing
D. Turning off the service at night to save cost, even though users rely on it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Steady, predictable demand is exactly where committed or provisioned capacity can beat per-token on-demand pricing, as long as the reserved capacity is well used. Spot capacity can be reclaimed and hurts a service users rely on. Major AI platforms do offer provisioned or committed throughput options. Turning the service off at night breaks a service needed around the clock.

**Key Concept:** The same commitment logic used for compute applies to AI capacity: commit to steady demand, stay flexible on spiky demand. See [Rate Optimization capability](https://www.finops.org/framework/capabilities/rate-optimization/).
</details>

---

## Where to go deeper

- [FOCP-Pro cert page](../../exams/finops/certified-professional/) - notes, practice plan, strategy
- [FOCA practice questions](./finops-certified-analyst.md) - the analyst level
- [FinOps Certified Engineer practice questions](./finops-certified-engineer.md) - the engineering counterpart
- [FinOps topic index](../../topics/finops.md) - the cert family in context
- **[📖 FinOps Foundation](https://www.finops.org/)** - the framework and certification pages
