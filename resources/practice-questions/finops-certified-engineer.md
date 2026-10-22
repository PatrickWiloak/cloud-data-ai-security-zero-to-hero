---
last-updated: 2026-10-22
difficulty: intermediate
---

# FinOps Certified Engineer - Practice Questions

30 questions for the FinOps Certified Engineer exam, focused on the engineering side of cloud efficiency: architecture, workload optimization, automation, and embedding cost awareness in delivery.

> **Cert page:** [exams/finops/certified-engineer/](../../exams/finops/certified-engineer/)

---

### Question 1
**Scenario:** An engineer is asked to reduce a service's cost without harming reliability.

A. Attack waste first: rightsize against measured utilization, remove idle and orphaned resources, and schedule non-production
B. Move the service to a cheaper region, which lowers the unit price but adds migration work and latency
C. Reduce replicas to the minimum the service can run on, since each replica removed is cost saved with no effect on availability or on how much traffic it can absorb
D. Reduce redundancy by moving from three zones to one, which cuts cross-zone charges and capacity at the expense of resilience and zone-failure tolerance

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Waste reduction has no reliability cost, so it comes first by definition. Orphaned resources are the usual quick win: unattached volumes, unassociated addresses, old snapshots, and load balancers with no targets accumulate silently.
</details>

---

### Question 2
**Scenario:** Instances are sized from a spreadsheet estimate made before launch.

A. Double every instance to be safe, so that the launch estimate is replaced by a generous margin that no later peak could exceed
B. Halve every instance on the assumption the spreadsheet was cautious, then restore any size that causes alerts
C. Keep them as they are, since the estimate was approved before launch and has not caused an incident yet
D. Rightsize against observed CPU, memory, and I/O percentiles, with headroom for peaks rather than sizing to the average

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Pre-launch estimates embed guesswork plus a safety margin nobody revisits. Sizing to observed percentiles with deliberate headroom is the disciplined version; sizing to the average is the failure mode that turns a cost win into an incident.
</details>

---

### Question 3
**Scenario:** A batch workload tolerates interruption and reruns cheaply.

A. On-demand instances, which give steady availability with no interruptions at the full list price for every hour
B. Dedicated hosts, which give the single-tenant isolation that suits licence-bound workloads but cost more than shared capacity
C. Spot or preemptible capacity with checkpointing, falling back to on-demand when spot is unavailable
D. Reserved instances for a one-year term, which discount steady usage but are wasted when the batch runs only occasionally

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Interruption tolerance is the qualifying property, and checkpointing is what makes an interruption a pause rather than a lost run. Stateless, retryable, non-urgent work is the right fit; a stateful licensed database is not.
</details>

---

### Question 4
**Scenario:** Storage costs grow steadily while access falls off after 30 days.

A. Lifecycle policies moving data to colder tiers on a schedule, with expiry where retention allows, plus a review of old snapshots and versions
B. Buy more storage capacity in advance at the committed rate, which lowers the unit price as volumes keep growing
C. Compress the data at the application layer before writing, which reduces the stored bytes but leaves every object in the hot tier
D. Delete everything after 30 days, which stops growth but also removes data that retention rules or audits may still require

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Tiering matches cost to access frequency automatically. The overlooked contributors are usually object versions and orphaned snapshots, which grow without any corresponding growth in what the application actually reads.
</details>

---

### Question 5
**Scenario:** Data transfer charges are unexpectedly high.

A. Reduce the data volume only, by trimming payload fields and response sizes, while leaving traffic paths between zones, regions, and the internet unchanged
B. Move to another provider whose list price per gigabyte is lower, and migrate the heaviest workloads
C. Map the flows: cross-zone and cross-region traffic, NAT processing, and egress; then co-locate, use private endpoints or a CDN
D. Compress everything at the application layer, which reduces bytes but not the paths traffic takes

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Transfer cost is architectural, not incidental. Cross-zone chatter between tiers and NAT processing charges for traffic that could use a private service endpoint are the two most common surprises, and both are fixed by design changes rather than tuning.
</details>

---

### Question 6
**Scenario:** A Kubernetes cluster runs at 20% node utilization.

A. Reduce replicas of every deployment to the minimum, which frees pod capacity but does not change the requests that reserve node capacity
B. Set requests to match observed usage, enable cluster autoscaling with bin-packing, and consolidate workloads
C. Add more nodes to the cluster so each node carries a smaller share of the pods and utilization stays under control
D. Buy commitments for the nodes at the current count, which lowers the rate while leaving the idle capacity in place

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Over-declared requests are the classic Kubernetes cost problem: the scheduler reserves what you asked for, so nodes fill up while sitting idle. Fixing requests is what lets the autoscaler actually remove nodes.
</details>

---

### Question 7
**Scenario:** A serverless function is invoked millions of times and costs more than a container would.

A. Serverless is always cheaper than provisioned compute at any volume, because there is no idle capacity to pay for
B. Model the crossover: serverless wins for spiky or low-volume work, while sustained high-volume traffic often favors provisioned compute or containers with committed pricing
C. Reduce the timeout to the shortest value the function can meet, which caps the cost of a slow call but not of many calls
D. Raise memory and timeout to the maximum, since billing is per request only and these settings do not affect cost

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Per-request pricing scales linearly and eventually crosses the cost of an always-on instance. Note the counterintuitive tuning detail: raising a function's memory often lowers total cost, because it also raises CPU and shortens the billed duration.
</details>

---

### Question 8
**Scenario:** Cost must be considered before code ships, not after.

A. Monthly review meetings between finance and engineering, where the previous month's spend is compared with the budget set for each team
B. A dashboard for engineers that shows each team's daily spend, which they can check whenever they want to
C. Shift left: cost estimates in infrastructure-as-code pull requests, policy checks, and cost as a design constraint
D. Quarterly audits of the largest accounts by a central team, who list savings opportunities for the owners to act on later

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Architecture decisions set the cost floor, and no amount of later tuning removes a design with inherently heavy cross-region transfer or per-request pricing at scale. A pull-request estimate is the cheapest possible moment to catch it.
</details>

---

### Question 9
**Scenario:** Idle non-production resources must stop accruing cost automatically.

A. Automated scheduling that stops resources outside working hours, plus expiry on ephemeral environments with an override
B. Delete them every weekend and have developers recreate what they need on Monday, which saves cost but loses state and setup time
C. Reduce their size to the smallest type, which lowers the hourly rate but leaves the resources running at all hours
D. Ask developers to remember to stop their own environments, backed by a reminder posted in the team channel on Friday afternoons each week

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Automation removes the person who might forget, which is the entire point. An override path matters too: a schedule with no exception mechanism gets disabled the first time it interrupts real work.
</details>

---

### Question 10
**Scenario:** A team wants to know whether an optimization actually worked.

A. Ask the team whether it feels cheaper, since the people who made the change know best
B. Check the invoice total for the month after the change against the previous month's invoice
C. Measure the specific resource or unit metric before and after, isolating the change from unrelated growth
D. Look at total spend next month across all accounts and judge the change a success if the figure has fallen at all

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Total spend moves for many reasons at once, so attribution requires narrowing to the affected resources or to a unit cost. Without that isolation, a successful optimization masked by growth looks like a failure and gets reverted.
</details>

---

### Question 11
**Scenario:** A database is over-provisioned but the team fears a resize.

A. Leave it as it is, since a resize risks an outage and the current cost has already been accepted in the budget
B. Add a cache in front of the database instead, which cuts read load but leaves the instance oversized
C. Halve it immediately in one change, and watch for alerts, since the instance can be scaled back up if needed
D. Reduce in stages with monitoring and a rollback plan, validating the smaller size on a replica or a test restore under realistic load first

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Staged change with a rollback path is how you make a reversible experiment out of something that feels irreversible. Validating on a copy under realistic load removes most of the uncertainty that drives the fear.
</details>

---

### Question 12
**Scenario:** Which architectural change most reduces cost for a read-heavy workload?

A. Caching in front of the datastore and a CDN for static content, removing repeated work
B. Add more read replicas to the database tier, which spreads reads across instances but still serves every request from the datastore
C. A larger database instance class with more memory, which speeds up each query but does not reduce how many are run
D. A faster disk type such as provisioned IOPS, which cuts latency per read but adds cost for every request still served

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Caching removes the request rather than serving it more cheaply, which is a larger effect than any resizing. The design work is invalidation: TTL-based lazy loading is simple but serves stale data, write-through stays fresh at the cost of write complexity.
</details>

---

### Question 13
**Scenario:** GPU instances for machine learning sit idle between training runs.

A. Keep them running between runs for convenience, so the next training job starts without waiting for capacity or any setup time
B. Buy one-year commitments for them, which lowers the hourly rate but leaves the idle hours in place
C. Use CPU instead of GPU for all training, which removes the GPU cost entirely at the price of much longer runs and slower iteration
D. Managed training jobs that scale to zero, checkpoint to durable storage, and keep training apart from inference

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** GPUs are among the most expensive idle resources in any estate. Separating training from inference matters because their load shapes differ completely: bursty long jobs versus steady low-latency requests.
</details>

---

### Question 14
**Scenario:** An engineer is asked to commit to a three-year reservation.

A. Commit to the peak so every hour of usage is covered, and accept the discount on capacity that sits idle off-peak
B. Commit only to the stable baseline that survives planned changes, after rightsizing
C. Never commit to a term, because the flexibility of paying on demand outweighs any discount over three years
D. Commit to current usage as measured last month, which is easy to justify but locks in any waste that is already present in it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A commitment is a bet on future usage, and a three-year term outlives most architectures. Committing to a rightsized floor rather than current usage is what prevents locking in waste and stranding the discount later.
</details>

---

### Question 15
**Scenario:** Cost anomalies should reach the engineer who caused them.

A. An annual review of cloud spend by the finance team, where the largest variances are explained afterward
B. Automated anomaly detection routing alerts to the owning team by tag or account, close to when the change happened
C. A shared inbox where all anomaly alerts are collected, so that anyone in the organization can pick one up and look into it
D. A monthly report to finance listing the accounts over budget, who then ask engineering why

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Feedback loses value with distance in both time and organization: an alert a month later reaches someone who no longer remembers the change. Routing by ownership tag is what makes the alert actionable rather than informational.
</details>

---

### Question 16
**Scenario:** A platform team manages hundreds of AWS resources in Terraform, and allocation reports keep showing resources with no `team` or `cost-center` tag because engineers forget to add them. What is the simplest engineering fix?

A. Add a monthly script that scans the account and tags anything missing as `unknown`
B. Add a comment block to each module reminding engineers which tags are required
C. Set `default_tags` in the AWS provider block so every resource it creates gets them
D. Ask finance to allocate untagged resources by hand at the end of each month

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The AWS provider's `default_tags` applies a tag set to every resource the provider manages, so tags cannot be forgotten resource by resource. A monthly script tags after the fact, and `unknown` is not an allocation. Comments rely on memory. Manual allocation by finance is slow and inaccurate.

**Key Concept:** Put cost metadata in the IaC layer so allocation is correct from creation. See [Terraform AWS provider default_tags](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configuration-block).
</details>

---

### Question 17
**Scenario:** A team's development environment mirrors production exactly: three Availability Zones, a multi-AZ database, and the same instance sizes. Dev costs nearly as much as prod. What is the most cost-aware change?

A. Match resilience to the environment: run dev in one zone on smaller sizes, keep prod multi-AZ
B. Remove the dev environment and test changes directly in production behind feature flags
C. Keep dev identical to prod, because any difference makes every test result unreliable
D. Buy three-year commitments for dev so that the identical setup costs less each month

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Non-production rarely needs production's availability, so cutting zones and sizes removes most of the cost while keeping the same architecture and code paths for testing. Testing only in production raises risk. Perfect parity is costly, and the few tests that need it can use a short-lived prod-like stack. Commitments discount waste instead of removing it, and lock in dev capacity for years.

**Key Concept:** Cost-aware architecture sets resilience by the business need of each environment. See [Architecting for Cloud capability](https://www.finops.org/framework/capabilities/architecting-for-cloud/).
</details>

---

### Question 18
**Scenario:** An engineer needs hourly, resource-level AWS cost and usage line items, including amortized commitment costs, to query with SQL and join with internal data. What is the right source?

A. The Cost Explorer console, exported to CSV from the monthly cost view
B. AWS Budgets reports, which email daily cost summaries per budget
C. Trusted Advisor checks, which list cost items for each account
D. AWS Data Exports (CUR 2.0) delivered to S3 and queried with Athena

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Data Exports delivers the Cost and Usage Report, the most detailed AWS billing dataset, with resource IDs, hourly granularity, and amortized cost columns, to S3 where Athena can query it. Cost Explorer is summarised and limited for this purpose. Budgets reports summarise spend against budgets. Trusted Advisor gives recommendations, not line-item billing data.

**Key Concept:** Build cost analytics on the provider's detailed billing export, not console views. See [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html).
</details>

---

### Question 19
**Scenario:** A team on Google Cloud wants detailed billing data in SQL for custom dashboards. They plan to enable the billing export next quarter and backfill the previous six months at that point. What should they know?

A. The export always backfills the full billing history, so waiting a quarter loses nothing
B. Enable the BigQuery export now; at most it backfills from the start of the previous month
C. Billing data can only be viewed in the console, so SQL dashboards are not possible at all
D. Billing data must first be copied by hand into Cloud SQL before any query can be run

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cloud Billing export to BigQuery is the standard path for SQL analysis. With a multi-region dataset it backfills only from the start of the month before the export was first enabled, and a regional dataset gets no backfill at all, so six months of history cannot be recovered later. The export is not a full history tool. SQL dashboards over the BigQuery export are a common pattern. No manual copy into Cloud SQL is needed.

**Key Concept:** Turn on billing exports on day one; history you did not export is hard to recover. See [Export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery).
</details>

---

### Question 20
**Scenario:** A shared Kubernetes cluster costs $40,000 per month, and the platform team must split it across 12 namespaces. Some namespaces request far more CPU than they use. Which allocation basis is fairest?

A. Charge each namespace for the larger of its requests or its usage, and report idle capacity separately
B. Charge each namespace for actual CPU usage only, ignoring whatever resources it requested
C. Split the cluster cost equally across all 12 namespaces, whatever their size
D. Charge each namespace by its number of pods, since pods are what the scheduler places

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Requests reserve node capacity whether used or not, so charging the larger of requests and usage holds teams accountable for capacity they block. Reporting the leftover idle cost separately shows the platform's own efficiency. Usage-only charging rewards over-requesting. An equal split and pod counts ignore actual consumption.

**Key Concept:** Allocate container cost on max(request, usage) and make idle visible. See [OpenCost specification](https://opencost.io/docs/specification).
</details>

---

### Question 21
**Scenario:** Engineers have tagged EC2 instances with `team` for weeks, but the `team` column is missing from the AWS cost and usage data. What is the cause?

A. Tags on EC2 never appear in billing data; only account IDs can be used for allocation
B. The tag value contains capital letters, which the billing pipeline silently drops
C. Billing data only shows tags that were applied before the start of the calendar year
D. The tag must be activated as a cost allocation tag in Billing, and applies from then on

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** User-defined tags appear in billing data only after they are activated as cost allocation tags in the Billing and Cost Management console, and they apply going forward from activation. EC2 tags do appear once activated. Letter case does not prevent tags appearing. There is no calendar-year rule.

**Key Concept:** Tagging resources is half the job; activate the keys for billing. See [Cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html).
</details>

---

### Question 22
**Scenario:** A company runs steady compute on EC2 today but plans to move half of it to Fargate and Lambda over the next year. They want a commitment discount that survives the move. Which fits?

A. EC2 Instance Savings Plans for the current instance family in the current region
B. Standard Reserved Instances for the exact instance types running today
C. Compute Savings Plans, which apply across EC2, Fargate, and Lambda usage
D. Spot Instances for all steady compute, since they give the deepest discount

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Compute Savings Plans apply to EC2 regardless of family, size, or region, and also to Fargate and Lambda, so the commitment follows the workload as it moves. EC2 Instance Savings Plans and Standard Reserved Instances are tied to EC2 and specific families or types. Spot can be interrupted and is not a commitment, so it does not suit steady production compute.

**Key Concept:** Trade some discount for flexibility when the architecture is changing. See [Savings Plans types](https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html).
</details>

---

### Question 23
**Scenario:** A fleet has hundreds of gp2 EBS volumes. Most are larger than needed only to get more IOPS, because gp2 IOPS scale with size. What change usually lowers cost without hurting performance?

A. Move all volumes to io2 so that IOPS are guaranteed at any size
B. Migrate to gp3, which costs less per GB and sets IOPS separately
C. Move all volumes to st1, the throughput-optimized HDD volume type
D. Take snapshots of each volume and delete the volumes every night

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** gp3 is cheaper per GB than gp2 and includes a baseline of IOPS and throughput that can be raised independently of size, so oversized volumes can shrink. io2 is a premium type for demanding workloads and costs more. st1 is HDD, unsuitable for boot or random I/O workloads. Nightly snapshot-and-delete breaks running systems.

**Key Concept:** Decoupling performance from size lets storage be rightsized. See [EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html).
</details>

---

### Question 24
**Scenario:** A rightsizing tool recommends halving an EC2 instance because average CPU is 15%. The instance runs a JVM application that is known to use a lot of memory. What should the engineer do before acting?

A. Collect memory metrics with the CloudWatch agent and check both CPU and memory first
B. Accept the recommendation, since CPU is the only metric that drives instance cost
C. Reject all rightsizing for the instance, since JVM workloads cannot be resized
D. Halve the instance and watch the error rate to see whether anything breaks

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** EC2 does not report memory utilization by default, so a CPU-only recommendation can push a memory-heavy workload into swapping or out-of-memory failures. Installing the CloudWatch agent supplies memory metrics, which tools such as Compute Optimizer can then use. Cost depends on the whole instance size, not CPU alone. JVM workloads can be resized safely with data. Resizing blind and waiting for errors risks an outage.

**Key Concept:** Rightsize on every constrained resource, not only the one reported by default. See [Compute Optimizer: enhanced infrastructure metrics and memory](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html).
</details>

---

### Question 25
**Scenario:** A cost review finds 300 EBS volumes in the `available` state, some over a year old. They were left behind when instances were terminated. What is the right action?

A. Leave them, because unattached volumes are not billed while they are idle
B. Attach each one to a running instance so that the storage is put to use
C. Convert every one of them to gp3 so that the idle storage costs less per GB
D. Confirm owners, snapshot any that need keeping, then delete the rest

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Unattached volumes are still billed for provisioned storage, and the `available` state means no instance is using them. Confirming ownership, keeping a snapshot where data may matter, then deleting removes waste safely. Attaching volumes to random instances adds risk and still wastes money. Converting to gp3 lowers the price of storage nobody uses instead of removing it.

**Key Concept:** Orphaned resources are pure waste; find them on a schedule and clean up with a safety net. See [Delete an EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-deleting-volume.html).
</details>

---

### Question 26
**Scenario:** A CPU-bound Lambda function runs at 128 MB and takes 10 seconds per call. An engineer wonders whether raising memory could lower cost. Why might it?

A. Higher memory settings get a lower price per GB-second than smaller ones
B. Lambda assigns CPU in proportion to memory, so the function may finish much faster
C. Lambda does not charge for duration above 1 GB, only for the number of requests
D. Raising memory moves the function onto Graviton, which halves its total cost

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Lambda allocates CPU power in proportion to configured memory, and cost is memory times duration. For a CPU-bound function, more memory can cut duration enough that total GB-seconds stay flat or fall, while latency improves. The price per GB-second does not drop with size. Duration is always billed. Architecture is a separate setting from memory.

**Key Concept:** Tune Lambda memory by measuring cost and duration together, for example with power tuning. See [Configure Lambda function memory](https://docs.aws.amazon.com/lambda/latest/dg/configuration-memory.html).
</details>

---

### Question 27
**Scenario:** A platform team wants an open-source tool that uses YAML policies to find EC2 instances missing required tags, notify owners, and stop them after a grace period, across many accounts. Which tool fits?

A. Infracost, which compares cost changes in Terraform pull requests
B. OpenCost, which allocates Kubernetes costs to namespaces and labels
C. Cloud Custodian, a rules engine that filters resources and runs actions
D. Prometheus, which scrapes metrics and alerts on threshold breaches

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cloud Custodian policies filter cloud resources by attributes such as missing tags and run actions such as notify, mark for later, and stop, which covers the whole workflow. Infracost estimates the cost of IaC changes before deploy. OpenCost allocates Kubernetes cost. Prometheus monitors metrics and does not act on cloud resources.

**Key Concept:** Automate governance with policy-driven remediation, not manual sweeps. See [Cloud Custodian documentation](https://cloudcustodian.io/docs/).
</details>

---

### Question 28
**Scenario:** An engineer is automating a weekly report of rightsizing opportunities for EC2 instances, EBS volumes, Lambda functions, and ECS services on Fargate. Which AWS service API covers all of these?

A. AWS Compute Optimizer
B. AWS Cost Anomaly Detection
C. AWS CloudTrail
D. AWS Budgets

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Compute Optimizer analyses utilization and returns rightsizing recommendations for EC2, Auto Scaling groups, EBS, Lambda, and ECS on Fargate through its API. Cost Anomaly Detection flags unusual spend, not rightsizing. CloudTrail records API activity. Budgets tracks spend against thresholds.

**Key Concept:** Feed rightsizing recommendations into engineering workflows automatically. See [What is Compute Optimizer?](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)
</details>

---

### Question 29
**Scenario:** A data lake holds millions of large objects whose access patterns are unpredictable: some go cold for months, then become hot again. Engineers cannot write reliable lifecycle rules. Which S3 option fits?

A. S3 Standard for everything, since tiering adds risk for unpredictable data
B. S3 Glacier Deep Archive for everything, retrieving objects when they are needed
C. A lifecycle rule moving objects to Standard-IA after 30 days without exceptions
D. S3 Intelligent-Tiering, which moves objects between tiers by observed access

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Intelligent-Tiering monitors access and moves objects between tiers automatically, with no retrieval fees, so it suits unknown or changing patterns. It charges a small monitoring fee per object, which matters little for large objects. Standard for everything overpays for cold data. Deep Archive has retrieval delays of hours, which hurts data that becomes hot. A fixed Standard-IA rule adds retrieval charges for objects that turn hot again.

**Key Concept:** Use lifecycle rules for known patterns and Intelligent-Tiering for unknown ones. See [S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html).
</details>

---

### Question 30
**Scenario:** Developer sandbox accounts have a $500 monthly limit. When a sandbox passes its limit, new EC2 launches should be blocked automatically, without anyone watching a dashboard. What should the engineer configure?

A. A Cost Explorer saved report that the account owners review each Friday
B. An AWS Budgets action that applies a restrictive policy when the budget is exceeded
C. A CloudWatch billing alarm that emails the finance team when spend crosses $500
D. A tag policy that requires a `budget` tag on every resource in the sandbox

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Budgets actions can apply an IAM policy or service control policy, or stop specific EC2 or RDS instances, when a threshold is crossed, which enforces the limit automatically. A weekly report relies on people. A billing alarm notifies but does not block anything. A tag policy enforces tag format, not spend.

**Key Concept:** Guardrails that act automatically scale better than alerts people must read. See [Configuring a budget action](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html).
</details>

---

## Where to go deeper

- [FinOps Certified Engineer cert page](../../exams/finops/certified-engineer/) - notes, practice plan, strategy
- [FOCA practice questions](./finops-certified-analyst.md) - the analyst counterpart
- [Cloud cost basics](../../learn/concepts/cloud-cost-basics.md) - plain-English primer
- [Autoscaling explained](../../learn/concepts/autoscaling-explained.md) - the elasticity lever
- **[📖 FinOps Foundation](https://www.finops.org/)** - the framework and certification pages
