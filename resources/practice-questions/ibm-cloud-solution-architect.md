---
last-updated: 2026-10-22
difficulty: advanced
---

# IBM Certified Solution Architect - Cloud Architect - Practice Questions

30 questions for this exam, weighted toward architecture design principles (25%), then infrastructure architecture and application and data architecture (20% each), security architecture (15%), and HA/DR and performance.

> **Cert page:** [exams/ibm/cloud-solution-architect/](../../exams/ibm/cloud-solution-architect/)

---

### Question 1
**Scenario:** A requirement states "the system must be highly available." What should the architect do first?

A. Add redundancy everywhere, duplicating every component and database in each zone before any availability target has been agreed with the business
B. Quantify it: define the availability target, RTO, and RPO, and identify what the business loses per hour of downtime
C. Buy the largest instances
D. Deploy across three zones

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** "Highly available" is not a design input until it is a number, because the cost difference between 99.9% and 99.99% is large and the business may not want to pay it. RTO and RPO then drive the specific mechanisms: replication, backup frequency, and failover automation.
</details>

---

### Question 2
**Scenario:** An application must be portable across IBM Cloud, another public cloud, and on-premises.

A. Rewrite per environment
B. Virtual machines with manual configuration scripts kept separately for each cloud and each data center
C. Use IBM-specific PaaS everywhere
D. Containerize on Red Hat OpenShift, keeping cloud-specific dependencies behind abstractions

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A consistent platform is what makes portability real rather than theoretical. Be honest about the cost: portability means avoiding the managed services that would otherwise reduce your operational burden, so it should be justified by an actual requirement.
</details>

---

### Question 3
**Scenario:** A monolith is being decomposed. What should drive the service boundaries?

A. Business capabilities and data ownership, so each service owns its data and changes independently
B. Code file count
C. Team size, creating one service per team and sizing each service to match that team's headcount exactly
D. Technology preference, so that each team picks its favourite language and framework for its own service

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Boundaries that cut across a business capability produce services that must be deployed together, which is a distributed monolith: all the operational cost of microservices with none of the independence. Shared databases are the usual symptom.
</details>

---

### Question 4
**Scenario:** Two services must remain consistent across a business transaction without distributed transactions.

A. The saga pattern, with local transactions and compensating actions, accepting eventual consistency
B. A shared database
C. Two-phase commit across the services' databases, with a coordinator locking rows until every participant votes
D. Manual reconciliation by operations staff, who compare the two databases each night and fix the differences

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Two-phase commit couples availability across services: if one participant is down, nothing commits. Sagas trade atomicity for availability, which requires designing the compensating action and accepting a window where the system is inconsistent.
</details>

---

### Question 5
**Scenario:** An architecture must tolerate a regional outage with an RPO under 15 minutes.

A. Multi-zone within one region, which survives a data center failure but not the loss of the whole region
B. A larger instance size in the primary region, with more CPU and memory for the database
C. Backups taken every five minutes to a bucket in the same region as the production system
D. Cross-region asynchronous replication with a rehearsed failover procedure

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Multi-zone protects against a data center, not a region. Asynchronous cross-region replication meets a 15-minute RPO comfortably, and the part that determines whether it works is rehearsal: an untested failover reliably fails on a dependency nobody remembered.
</details>

---

### Question 6
**Scenario:** A design uses a message queue between services.

A. It adds no benefit
B. It decouples producers from consumers in time and rate, absorbing bursts and letting the consumer fail without losing work
C. It removes the need for error handling because messages are always delivered exactly once and processed successfully by every consumer
D. It guarantees ordering globally

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Buffering and decoupling are the benefits. The costs are real too: eventual consistency, harder end-to-end tracing, and the need to handle duplicate delivery, since most systems guarantee at-least-once rather than exactly-once.
</details>

---

### Question 7
**Scenario:** Data residency requires that customer data never leaves a specific country.

A. Use a global CDN so that customer data is cached close to the users in every country they live in
B. Use in-country regions, restrict replication and backup targets, and verify managed services
C. Encrypt the data with a customer-managed key and then store the encrypted copies in any convenient region
D. Document the residency intent in the security policy and ask each team to follow it when it deploys

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The parts that leak are the ones you did not choose explicitly: backup destinations, disaster recovery replicas, telemetry, and provider support access. Verifying each is what turns a residency claim into something defensible in an audit.
</details>

---

### Question 8
**Scenario:** A security architecture must limit lateral movement after a compromise.

A. A single perimeter firewall at the network edge that blocks inbound traffic while trusting every workload already inside the internal network
B. Strong passwords
C. Network segmentation, per-service identity with least privilege, and an assume-breach posture
D. Antivirus software installed on every server and developer laptop, with signatures updated every day

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A perimeter defends the outside only, so once one workload is compromised a flat network gives the attacker everything. Segmentation plus workload identity means each additional step requires defeating another control, which is the assume-breach posture.
</details>

---

### Question 9
**Scenario:** An architecture decision must be recorded for future teams.

A. A diagram alone, drawn once in a slide deck, shared by email at kickoff and never updated after the design changes later
B. A verbal agreement
C. An architecture decision record with the context, options considered, decision and consequences
D. Code comments written by the developers next to the relevant source code at the time of each change, kept in the repo

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A diagram shows what was built but not why, so the next team cannot tell which constraints still apply. Recording the rejected options is the part that prevents relitigating the same debate two years later.
</details>

---

### Question 10
**Scenario:** Performance requirements must be validated before go-live.

A. Measure only the average response time under the normal daily load and report it to the sponsor
B. Test in production after launch, using the first wave of paying customers as the load test
C. Load test against the defined targets, including soak and peak-plus-headroom tests
D. Assume it will scale because the cloud provider advertises elastic capacity for every service

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Averages hide the tail users experience, so measure percentiles. Soak testing catches leaks and resource exhaustion that a short burst test misses, which is the class of problem that appears three days after launch.
</details>

---

### Question 11
**Scenario:** Cost must be considered in the architecture, not after it.

A. Optimize later
B. Model the cost of each design option, including data transfer and operational effort, and treat it as a design constraint alongside performance and availability
C. Cost is a finance problem
D. Choose the cheapest option always

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Architecture decisions set the cost floor: choosing an architecture with heavy cross-zone data transfer or per-request pricing at scale locks in a bill that no later tuning removes. Operational effort belongs in the model because staff time is a real cost.
</details>

---

### Question 12
**Scenario:** A stateless application tier is preferred. Why?

A. Any instance can serve any request, so scaling, replacement, and failure recovery are trivial; state lives in a data store or cache
B. It is always faster
C. It needs no database
D. It is simpler to write

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Statelessness is what makes horizontal scaling and instance replacement safe. Session affinity is the compromise that reintroduces the problem, which is why sessions usually move to a shared cache instead.
</details>

---

### Question 13
**Scenario:** An integration must connect to an on-premises system from cloud.

A. Poll the on-premises system over the public internet on a schedule from a cloud function
B. Private connectivity (Direct Link or VPN) plus an API gateway or secure connector
C. Copy the data by hand every night using exported files that are moved across on a shared drive
D. Expose the on-premises system publicly through a static IP address and rely on a shared application password sent in a request header

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Private connectivity plus a controlled integration point limits exposure to one interface rather than a whole system. Direct Link provides dedicated, predictable bandwidth where a VPN over the internet does not.
</details>

---

### Question 14
**Scenario:** An architecture review asks about observability.

A. Logs are enough
B. Add monitoring after launch
C. Rely on the provider's dashboards
D. Design for metrics, logs, and traces from the start, with correlation identifiers propagated across services, plus SLIs and SLOs for the user-facing behavior

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Trace propagation must be built into the services, so retrofitting it means touching everything. Defining SLIs from the user's perspective rather than from infrastructure metrics is what makes alerts correspond to real problems.
</details>

---

### Question 15
**Scenario:** A stakeholder asks for a technology the architect believes is wrong for the requirement.

A. Build it the way the architect prefers without telling the stakeholder, then explain the change after delivery if someone notices and complains
B. Comply silently
C. State the trade-offs with evidence, propose an alternative, and if the decision stands, record it as an ADR with the accepted risks
D. Refuse

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The architect's job is to make consequences visible, not to win. Recording the decision with its accepted risks means the organization owns the choice knowingly, which is also what protects the team when the risk materializes.
</details>

---

### Question 16
**Scenario:** A bank is designing its first regulated workload on IBM Cloud. Its regulators expect documented controls mapped to financial services requirements, and the architects want a validated starting point rather than designing every control from scratch. What should they build on?

A. The IBM Cloud Framework for Financial Services, with its control requirements and reference architectures
B. A generic public cloud landing zone, with extra controls bolted on later once the auditors raise findings
C. A copy of another bank's architecture diagrams, adapted by the team without any further validation
D. An on-premises design moved unchanged to virtual servers, so existing audits still apply to it

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The IBM Cloud Framework for Financial Services provides a set of controls aligned to financial services regulation, plus reference architectures designed to meet them, giving a validated baseline. A generic landing zone with controls added after findings is reactive and risks failing audits. Another bank's diagrams carry no validation for this context. Moving an on-premises design unchanged does not carry over its audits, because the environment and responsibilities change.

**Key Concept:** Start regulated designs from an established control framework. See [About the IBM Cloud Framework for Financial Services](https://cloud.ibm.com/docs/framework-financial-services?topic=framework-financial-services-about).
</details>

---

### Question 17
**Scenario:** A large monolith must be modernized, but the business cannot accept a long freeze or a single cutover. What migration approach should the architect recommend?

A. A complete rewrite built in parallel, then switched over in one weekend when it is all finished
B. A lift and shift of the monolith to virtual servers, treated as the final state
C. A freeze on new features until the new microservices platform is fully built
D. Incrementally route features to new services around the monolith until it can be retired

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The strangler pattern replaces a monolith piece by piece: new or extracted features run as separate services, traffic is routed to them, and the monolith shrinks until it can be retired, with value and risk spread over time. A big-bang rewrite concentrates risk in one cutover. Lift and shift moves the monolith but does not modernize it. A feature freeze is what the business ruled out.

**Key Concept:** Modernize incrementally to keep delivering while reducing risk. See [What are microservices?](https://www.ibm.com/think/topics/microservices)
</details>

---

### Question 18
**Scenario:** A small team with no Kubernetes experience is building a set of containerized APIs with very spiky traffic and long idle periods. They want to minimise operations work and cost. Which platform should the architect recommend?

A. A self-managed Kubernetes cluster on virtual servers, sized for peak load
B. Red Hat OpenShift on IBM Cloud, with worker nodes sized for peak traffic
C. IBM Cloud Code Engine, which runs containers and scales to zero when idle
D. Bare metal servers, which give the most control over performance tuning

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Code Engine is a fully managed serverless platform for containers, scaling with demand and down to zero, so a team without Kubernetes skills has little to operate and pays little when idle. A self-managed cluster or OpenShift requires Kubernetes skills and pays for peak-sized nodes during idle periods. Bare metal maximises control but also cost and operations work.

**Key Concept:** Match the platform's operational demands to the team's skills and the traffic shape. See [About Code Engine](https://cloud.ibm.com/docs/codeengine?topic=codeengine-about).
</details>

---

### Question 19
**Scenario:** A stakeholder asks for 99.99% availability and also the lowest possible monthly cost. The two goals conflict. What should the architect do?

A. Present design options with their availability, cost, and risk so the stakeholder can choose
B. Design for 99.99% availability without telling the stakeholder what it will cost them
C. Design for the lowest cost and describe it as highly available in the proposal
D. Refuse to begin any design work until the stakeholder formally withdraws one of the two goals

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Architects make trade-offs visible: options such as single-zone, multi-zone, and multi-region designs with their cost and expected availability let the business choose knowingly. Hiding cost or overstating availability damages trust and leads to bad decisions. Refusing to proceed blocks progress when a clear comparison would resolve the conflict.

**Key Concept:** Quantify trade-offs and let the accountable owner decide. See [IBM Cloud security and architecture overview](https://cloud.ibm.com/docs/overview?topic=overview-security).
</details>

---

### Question 20
**Scenario:** An application must run across all three zones of an IBM Cloud multizone region in a VPC. How should the network be laid out?

A. One VPC per zone, connected by Transit Gateway, with one subnet in each
B. One VPC for the region, with at least one subnet in each of the three zones
C. One VPC with a single subnet that spans all three zones in the region
D. Three VPCs in three different regions, one for each of the app's tiers

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A VPC is regional and spans the region's zones, while each subnet belongs to one zone, so a multi-zone design needs subnets in each zone within one VPC. Separate VPCs per zone add needless routing and complexity. A subnet cannot span zones. Three regions is a multi-region design, not multi-zone, and splitting tiers across regions adds latency.

**Key Concept:** VPCs are regional; subnets are zonal. See [About networking for VPC](https://cloud.ibm.com/docs/vpc?topic=vpc-about-networking-for-vpc).
</details>

---

### Question 21
**Scenario:** Virtual servers in a VPC must reach Object Storage and a managed database, but security forbids any traffic to those services over public endpoints. What should the architect include?

A. A public gateway on each subnet, with security groups that allow only HTTPS
B. A floating IP on each virtual server, restricted to the services' public IPs
C. A site-to-site VPN from the VPC to the public service endpoints
D. Virtual private endpoints that give the services private IPs in the VPC

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Virtual private endpoints (VPEs) give IBM Cloud services private IP addresses inside the VPC, so traffic stays on the private network. A public gateway and floating IPs both send traffic to public endpoints, which is forbidden. A VPN is for connecting to other networks, not for reaching cloud services privately.

**Key Concept:** Reach platform services privately from a VPC with VPEs. See [About virtual private endpoint gateways](https://cloud.ibm.com/docs/vpc?topic=vpc-about-vpe).
</details>

---

### Question 22
**Scenario:** An enterprise has eight VPCs across two regions plus classic infrastructure, and an on-premises Direct Link. Workloads need to communicate privately across all of them without a mesh of point-to-point connections. What should the architect use?

A. Transit Gateway as a hub that connects the VPCs, classic, and Direct Link
B. A public gateway in each VPC, with traffic routed over the internet
C. Floating IPs on every server, with security groups between each pair
D. A VPN gateway in every VPC, connected directly to each of the other VPCs

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Transit Gateway connects VPCs, classic infrastructure, and Direct Link connections through a hub, locally or globally across regions, avoiding a full mesh. Public gateways and floating IPs send traffic over the internet. A VPN mesh between eight VPCs needs many tunnels and is hard to manage.

**Key Concept:** Use a transit hub instead of a point-to-point mesh as networks grow. See [About Transit Gateway](https://cloud.ibm.com/docs/transit-gateway?topic=transit-gateway-about).
</details>

---

### Question 23
**Scenario:** Heavy reporting queries run against the production PostgreSQL database and slow down customer transactions. Reports can tolerate data that is a few seconds old. What should the architect recommend?

A. Run the reports only at night, even though business users need them in the day
B. Scale the primary database up to the largest size and keep everything on it
C. Point reporting at a read-only replica so it is isolated from the primary
D. Move the transactional data to Object Storage and query it with SQL there

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A read-only replica receives changes from the primary and serves read queries, isolating reporting load from transactions at the cost of slight lag, which reports can accept. Night-only reporting fails the business need. Scaling up delays the problem and keeps the contention. Moving transactional data to object storage breaks the transactional workload.

**Key Concept:** Separate read-heavy analytics from transactional workloads. See [Read-only replicas](https://cloud.ibm.com/docs/databases-for-postgresql?topic=databases-for-postgresql-read-only-replicas).
</details>

---

### Question 24
**Scenario:** A company wants one platform for BI and AI workloads over large volumes of data in open table formats on object storage, without copying data into a separate proprietary warehouse for each tool. Which architecture fits?

A. A single relational OLTP database, scaled up to hold all analytical data
B. A data lakehouse, such as watsonx.data, querying open formats on object storage
C. A separate copy of the data per tool, refreshed nightly by batch export jobs
D. An in-memory cache that holds the full dataset for every analytics query

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A lakehouse combines low-cost object storage and open table formats such as Apache Iceberg with warehouse-style query engines, so several tools can use the same data. watsonx.data is IBM's lakehouse. An OLTP database is built for transactions, not large-scale analytics. Per-tool copies cost more and drift apart. An in-memory cache cannot economically hold large analytical datasets.

**Key Concept:** Lakehouses reduce data copies by sharing open-format data across engines. See [What is a data lakehouse?](https://www.ibm.com/think/topics/data-lakehouse)
</details>

---

### Question 25
**Scenario:** A product catalog page is read thousands of times per second, the data changes a few times per hour, and each database query takes 200 ms. What should the architect add?

A. More indexes on every column of every table in the catalog database
B. A second database in another region that answers every catalog read
C. A message queue that holds catalog reads until the database is free
D. A cache such as Databases for Redis, using cache-aside with a TTL

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Read-heavy, rarely changing data is the classic case for caching: cache-aside serves most reads from memory, and a time-to-live bounds how stale data can get. Indexing every column slows writes and still pays the database round trip. A remote region adds latency for most users. Queuing reads makes them slower, not faster.

**Key Concept:** Cache data that is read often and changes rarely. See [Getting started with Databases for Redis](https://cloud.ibm.com/docs/databases-for-redis?topic=databases-for-redis-getting-started).
</details>

---

### Question 26
**Scenario:** A company runs production and development in one IBM Cloud account. Auditors flag that developers could reach production by mistake, and billing is hard to separate. What should the architect recommend?

A. An enterprise with separate accounts for production and non-production, with access managed per account
B. One account, with all production resources named using a `prod-` prefix to tell them apart
C. One account, with every developer asked to sign a written policy promising never to touch production at all
D. Separate regions in the same account for each environment, chosen by the developers

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Separate accounts, grouped in an enterprise, give a hard boundary for access and billing between environments, while still allowing central management and consolidated billing. Naming conventions and signed policies do not enforce anything. Regions separate location, not access or billing ownership.

**Key Concept:** Use account boundaries for strong isolation between environments. See [Account types](https://cloud.ibm.com/docs/account?topic=account-accounts).
</details>

---

### Question 27
**Scenario:** A security requirement states that all service-to-service traffic inside a Kubernetes cluster must be encrypted and mutually authenticated, without changing application code. What should the architect specify?

A. Network policies that allow traffic only between approved namespaces
B. TLS termination at the public load balancer in front of the cluster
C. A service mesh such as Istio with mutual TLS enforced between services
D. An IP allow list on each service that lists the other services' pod IPs

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A service mesh such as Istio adds sidecar proxies that encrypt traffic with mutual TLS and verify service identities, without code changes. Network policies restrict which pods can talk but do not encrypt. TLS at the edge protects external traffic only. Pod IPs change constantly and are not an identity.

**Key Concept:** mTLS in a mesh provides encryption and workload identity together. See [Istio security concepts](https://istio.io/latest/docs/concepts/security/).
</details>

---

### Question 28
**Scenario:** An internal reporting tool is not business critical. The business accepts up to 24 hours of downtime and 24 hours of data loss after a regional disaster, and wants minimal spending on DR. Which strategy fits?

A. Active-active deployment in two regions, with synchronous replication of all data
B. Warm standby in a second region, with scaled-down servers kept running
C. Pilot light in a second region, with a database replica always running
D. Daily backups copied to another region, restored there only after a disaster

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** With an RTO and RPO of 24 hours, daily backups copied to another region and restored on demand meet the requirement at the lowest cost. Active-active, warm standby, and pilot light all keep resources running in a second region to cut recovery time, which this tool does not need and the budget does not justify.

**Key Concept:** Choose the cheapest DR strategy that meets the RTO and RPO. See [What is disaster recovery?](https://www.ibm.com/think/topics/disaster-recovery)
</details>

---

### Question 29
**Scenario:** An architecture review finds the application tier spread across three zones, but the database is a single self-managed instance on a virtual server in zone 1. What is the main finding?

A. The design is fine, because the application tier can survive a zone failure
B. The database is a single point of failure; use a multi-zone managed database
C. The application tier is over-built and should be moved into a single zone
D. The database should be moved to zone 2, which is safer than zone 1

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A system is only as available as its weakest required component; losing zone 1 takes the database and therefore the whole service down. A managed database deployed across zones removes the single point of failure. The application tier's resilience is wasted while the database stays single-zone. No zone is inherently safer than another.

**Key Concept:** Every tier on the critical path must match the availability target. See [Getting started with Databases for PostgreSQL](https://cloud.ibm.com/docs/databases-for-postgresql?topic=databases-for-postgresql-getting-started).
</details>

---

### Question 30
**Scenario:** A web tier on VPC virtual servers sees unpredictable traffic spikes that can triple load within minutes. It must handle the spikes without paying for peak capacity all day. What should the architect design?

A. An auto scale instance group behind a load balancer, scaling on a load metric
B. A fixed set of the largest available virtual servers, sized for triple load
C. A single bare metal server, with vertical scaling done by hand during each spike
D. A scheduled scale-up every morning at 9:00, and a scale-down every night

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** An instance group with auto scaling adds and removes servers behind a load balancer based on metrics such as CPU, matching capacity to unpredictable demand. A fixed peak-sized fleet pays for idle capacity. Manual vertical scaling is slow and has a hard ceiling. A fixed schedule cannot follow unpredictable spikes.

**Key Concept:** Scale horizontally and automatically for unpredictable load. See [Creating an instance group for auto scaling](https://cloud.ibm.com/docs/vpc?topic=vpc-creating-auto-scale-instance-group).
</details>

---

## Where to go deeper

- [IBM Cloud Solution Architect cert page](../../exams/ibm/cloud-solution-architect/) - notes, practice plan, strategy
- [IBM Cloud Advocate practice questions](./ibm-cloud-advocate.md) - the foundations below this
- [Zero trust architecture](https://security.noblerworks.com/resources/architecture-patterns/zero-trust-architecture/) - the security model in question 8
- [SRE and reliability topic index](../../topics/sre-and-reliability.md) - availability in practice
- **[📖 IBM Training](https://www.ibm.com/training/)** - official certification pages
