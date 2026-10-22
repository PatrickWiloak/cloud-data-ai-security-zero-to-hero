---
last-updated: 2026-10-22
difficulty: intermediate
---

# CompTIA Cloud+ (CV0-004) - Practice Questions

30 questions for Cloud+ prep. Questions 16-30 follow the CV0-004 objectives: cloud architecture (23%), deployment (19%), security (19%), operations (17%), troubleshooting (12%), and DevOps fundamentals (10%).

Cloud+ is vendor-neutral, so answers describe concepts rather than a specific provider's service names.

> **Cert page:** [exams/comptia/cloud-plus/](../../exams/comptia/cloud-plus/)

---

### Question 1
**Scenario:** A workload has a predictable baseline plus unpredictable spikes.

A. Provision the minimum
B. Provision for the peak permanently so no spike ever causes a capacity shortfall or latency
C. Provision the average
D. Provision the baseline with a committed discount and use autoscaling for spikes

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Splitting baseline from burst captures the discount on predictable usage while keeping elasticity for peaks. Provisioning for the average is the worst option: it fails during every spike while still paying for idle capacity off-peak.
</details>

---

### Question 2
**Scenario:** A migration approach must be chosen for a legacy application.

A. Always retire any application older than five years, since legacy systems carry the most technical debt
B. Assess per application: rehost, replatform, refactor, repurchase, retire, or retain
C. Always refactor every application into cloud-native microservices before moving anything to the cloud
D. Always rehost every application as is, so that no code changes are needed before the cutover

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The six R's are a per-application decision driven by business value, technical debt, and remaining lifespan. Rehosting everything carries the debt into a more expensive place; refactoring everything is the most expensive default.
</details>

---

### Question 3
**Scenario:** A VM template must be produced so every instance starts identically.

A. Clone a running production instance and edit its settings by hand after each launch
B. A documentation page
C. A golden image built by an automated pipeline, versioned and rebuilt on a patching cadence
D. Configure each instance by hand

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Images built by a pipeline are reproducible and auditable; manual builds embed whatever was on the machine that day. The operational detail people miss is the rebuild cadence: in an immutable model, the pipeline is how patching happens.
</details>

---

### Question 4
**Scenario:** Storage must be shared by many instances with file semantics.

A. File storage (NFS or SMB)
B. Local ephemeral disk
C. Object storage
D. Block storage attached read-write to every instance, each mounting it with its own local file system

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Block attaches to one instance like a disk, file provides concurrent POSIX or SMB access, and object is API-accessed with no file semantics. Matching the storage type to the access pattern is a recurring Cloud+ question shape.
</details>

---

### Question 5
**Scenario:** Data must survive the loss of a whole availability zone.

A. RAID 10 across several disks within one zone, which protects against drive failures and gives fast rebuilds
B. Replication across zones or regions, plus backups tested by restore
C. A larger disk
D. Snapshots taken every hour and stored in the same zone as the volume they protect

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** RAID and same-zone snapshots protect against device failure, not zone failure. The other half is the restore test: a backup that has never been restored is an assumption, and its failures surface during the incident.
</details>

---

### Question 6
**Scenario:** Costs are rising and the cause is unclear.

A. Estimate from headcount
B. Reduce all resources
C. Tag resources consistently, analyze cost by tag and service, then act on the largest contributors
D. Cancel unused accounts

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Attribution before action, because cost is normally concentrated in a few resources. Tag enforcement at creation matters, since coverage decays otherwise and untagged spend becomes invisible to the analysis.
</details>

---

### Question 7
**Scenario:** An application tier must not be reachable from the internet.

A. A strong password on every account, plus key-only SSH login and MFA on each instance
B. A host firewall rule on each instance that drops inbound traffic except on port 443
C. A public IP with an allowlist of approved source addresses on the instance's security group
D. A private subnet with no internet gateway route, using NAT for outbound only

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Routing is the structural control and security groups are the filter on top. NAT permits outbound-initiated traffic while blocking inbound. An allowlisted public IP is still internet-reachable and depends on the list staying correct.
</details>

---

### Question 8
**Scenario:** Identity and access must follow least privilege across teams.

A. Role-based groups, per-service scoping, MFA on privileged accounts, and periodic review
B. Full access for every engineer on request, with all activity logged and reviewed after the fact
C. One shared administrator account whose password the team lead rotates every month and stores in a vault
D. Individual permissions per user, granted on request by the team lead and recorded in a shared tracking spreadsheet

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Groups make joiners and leavers a membership change rather than a permission audit. Shared accounts destroy attribution, which is the first thing an incident investigation needs. Access review is what catches privilege creep.
</details>

---

### Question 9
**Scenario:** Encryption keys must be under organizational control.

A. Provider-managed keys only, because the provider rotates them automatically and handles all key storage
B. Customer-managed keys in a key management service, with rotation and audit logging
C. Keys in application configuration
D. No encryption, relying on network isolation and access controls to protect the stored data

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Customer-managed keys give revocation and an audit trail, which is usually what the compliance requirement actually means. Keys in configuration files are the anti-pattern: they leak through repositories, images, and backups.
</details>

---

### Question 10
**Scenario:** Capacity planning for a growing service.

A. Trend historical utilization, model growth, load test to find the limit, and plan for lead times
B. Rely entirely on autoscaling, since it adds instances automatically whenever demand rises beyond the current capacity
C. React when it breaks
D. Over-provision heavily from day one so that no load test, forecast or lead-time planning is ever required of the team

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Autoscaling handles variation within a provisioned envelope but not quota ceilings, license limits, or a dependency that cannot scale. Knowing the measured breaking point, rather than the extrapolated one, is what makes the plan credible.
</details>

---

### Question 11
**Scenario:** A deployment must be reversible if it goes wrong.

A. A strategy with a rollback path: blue-green, canary, or rolling with health-gated progression
B. Deploy and hope
C. Deploy at night
D. Notify users first, with a maintenance banner posted a day before

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Blue-green swaps whole environments so rollback is a traffic switch; canary exposes a small share first; rolling replaces gradually. All three require health checks that actually detect failure, or the automation happily rolls out a broken version.
</details>

---

### Question 12
**Scenario:** An instance is unreachable and the cause is unknown.

A. Restart the instance's network service and the virtual router, then retest from the same client; repeat until it responds
B. Rebuild the instance from the template and retest, since that is the quickest way to rule out its configuration
C. Contact the provider first and wait for its support team to diagnose the instance before anyone touches anything
D. Work the layers: instance state and console output, then routing and security groups, then the app

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Systematic layer-by-layer isolation is the Cloud+ troubleshooting method, and it is faster than guessing because each step eliminates a category. Rebuilding destroys the evidence and often recreates the same misconfiguration.
</details>

---

### Question 13
**Scenario:** Monitoring must detect problems before users do.

A. Log everything with no alerts
B. Check the dashboards at the start of each shift and escalate anything that looks abnormal to the team lead by email
C. Metrics with alerting on user-affecting symptoms, log aggregation, synthetic checks, and an escalation path
D. Alert on every metric

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Alerting on symptoms rather than causes is what keeps pages actionable; alerting on every metric produces fatigue and missed real incidents. Synthetic checks give the outside-in view that internal metrics cannot.
</details>

---

### Question 14
**Scenario:** A compliance requirement mandates data stay within a country.

A. Use a CDN
B. Select in-region services and restrict replication, backup, and DR targets to that jurisdiction
C. Add a policy document
D. Encrypt the data with customer-managed keys, which satisfies residency because only the key holder can read it

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Residency leaks through the paths nobody chose deliberately: cross-region backups, DR replicas, and telemetry. Verifying each is what turns a residency claim into something defensible.
</details>

---

### Question 15
**Scenario:** Infrastructure must be reproducible across environments.

A. Screenshots
B. Runbooks with detailed console steps, reviewed every quarter and kept on the team wiki for each environment
C. Infrastructure as code in version control, deployed by a pipeline with environment parameters
D. A configuration spreadsheet listing every setting per environment, kept up to date by hand after each change

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** IaC gives review, history, and rollback for infrastructure, and it is the precondition for any credible disaster recovery plan, because the second region must be buildable. Console-driven environments drift and cannot be verified.
</details>

---

### Question 16
**Scenario:** A company runs VMs on an IaaS platform. An audit finds the guest operating systems are missing months of security patches. Who is responsible?

A. The provider, because IaaS includes full management of every VM it hosts
B. The provider and the customer equally, with patching split by day of the week
C. Nobody, because cloud VMs are patched automatically by the hypervisor
D. The customer, because in IaaS the guest OS sits on the customer's side of the shared responsibility model

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** In IaaS the provider secures the physical hosts, network and hypervisor, while the customer owns the guest OS, its patches and everything above it. Full OS management by the provider is closer to PaaS or a managed service. Responsibilities are split by layer, not by schedule. The hypervisor does not patch guest operating systems.
</details>

---

### Question 17
**Scenario:** A database server needs low-latency storage it can format with its own file system and attach to one VM.

A. Object storage accessed over HTTPS, with each database page stored as a separate object
B. Block storage volume
C. A shared network file share mounted by every server in the environment at the same time
D. An archive storage tier

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Block storage appears to the VM as a raw disk that the OS formats and the database uses with low latency, which is how cloud database volumes work. Object storage is accessed through an API, has higher latency per request, and is not a disk. A shared file share adds protocol overhead and locking concerns, and the requirement is one VM. Archive tiers have retrieval delays of minutes to hours.
</details>

---

### Question 18
**Scenario:** An image-resize job runs only when a file is uploaded, which happens a few hundred times a day at random. The team wants to pay only when it runs and manage no servers.

A. A serverless function triggered by the upload event
B. A large reserved VM that runs the resize job in a loop and checks for new files every few seconds
C. A container cluster with three always-on nodes and a scheduler that checks for work every minute
D. A dedicated bare-metal host

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Serverless functions run on events, scale to zero, and bill per invocation and duration, which fits sporadic, short tasks with no servers to manage. A reserved VM bills all day whether busy or idle and still needs patching. An always-on cluster has the same idle cost plus more to operate. Bare metal is the most expensive and most hands-on option of all.
</details>

---

### Question 19
**Scenario:** The business states that after an outage, no more than 15 minutes of data may be lost and service must be back within 4 hours. What do these figures describe?

A. The RTO is 15 minutes and the RPO is 4 hours, so service must be back within 15 minutes
B. The SLA is 15 minutes and the MTBF is 4 hours for the service
C. The RPO is 15 minutes and the RTO is 4 hours
D. The retention period is 15 minutes and the backup window is 4 hours

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The recovery point objective (RPO) is how much data, measured in time, can be lost, so backups or replication must run at least every 15 minutes. The recovery time objective (RTO) is how long restoration may take, here 4 hours. Swapping the two gives the wrong design targets. SLA and MTBF measure availability commitments and failure frequency. Retention and backup windows are operational settings, not business recovery targets.
</details>

---

### Question 20
**Scenario:** A team wants to release a new version with near-zero downtime and switch back instantly if it fails.

A. Recreate deployment
B. Blue-green deployment, switching traffic from the current environment to an identical new one
C. In-place upgrade on the production servers during business hours, with a manual rollback plan
D. Deploy straight to production from a developer's laptop, then test the change once it is live

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Blue-green runs the new version in a parallel environment, switches traffic when it is healthy, and switches back just as quickly if it is not. Recreate stops the old version before starting the new one, which causes downtime. In-place upgrades change the only environment, so rollback is slow and risky. Deploying from a laptop skips every control and testing step.
</details>

---

### Question 21
**Scenario:** A company must move 80 TB of archived data into the cloud. Its internet link is 100 Mbps and already busy.

A. Upload the data over the existing link during business hours with a sync tool
B. Compress the data with a stronger algorithm so the upload over the existing link finishes in one night
C. Email the files to the cloud provider in batches of attachments
D. Use the provider's offline data transfer appliance, shipped to the site and back

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** At 100 Mbps, 80 TB takes roughly two months even with the link to itself, so a shipped transfer appliance is faster and leaves the link free. Uploading during business hours competes with production traffic for months. Compression helps a little, but already-archived data usually does not shrink enough to finish overnight. Email is not a data transfer method at this scale.
</details>

---

### Question 22
**Scenario:** A company keeps its regulated customer database in its own data center but runs its web front end in a public cloud, connected over a private link.

A. Hybrid cloud
B. Community cloud, shared by several organizations with the same compliance needs
C. Private cloud, because one part of the system runs on equipment the company owns
D. Multi-tenant SaaS

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Hybrid cloud combines on-premises or private infrastructure with public cloud, connected so they work as one system. Community cloud is shared infrastructure for organizations with common needs, which is not described here. Private cloud alone would not include the public cloud front end. SaaS is a service model, not a deployment model for the company's own systems.
</details>

---

### Question 23
**Scenario:** Monitoring shows a fleet of VMs averaging 8% CPU and 20% memory use for three months.

A. Add more VMs to the fleet so each one has even more spare headroom for future peaks
B. Move the VMs to a dedicated host so they get more consistent performance at the same size
C. Right-size the VMs to smaller instance types and keep monitoring
D. Ignore it, because unused capacity in the cloud costs nothing

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Sustained low utilization means the instances are oversized; moving to smaller types cuts cost while monitoring confirms performance holds. Adding VMs increases waste. A dedicated host costs more and does not address oversizing. Cloud bills for provisioned capacity whether it is used or not.
</details>

---

### Question 24
**Scenario:** Nightly backups have run successfully for a year, but nobody has ever restored one.

A. Nothing is needed, because the backup jobs report success every night
B. Switch to weekly backups so there are fewer jobs to check each month
C. Delete older backups to make room
D. Schedule regular test restores and check that the restored data and service actually work

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A backup is only proven by a successful restore; regular test restores catch silent corruption, missing data and gaps in the runbook. A success status shows the job ran, not that the data is usable. Weekly backups increase possible data loss without testing anything. Deleting backups reduces recovery options.
</details>

---

### Question 25
**Scenario:** A developer committed a database password in an application's configuration file to a shared repository.

A. Rotate the password, remove it from the code, and load it at runtime from a secrets manager
B. Make the repository private and leave the password in place since only staff can see it now
C. Delete the file in a new commit and keep using the same password
D. Base64-encode the password in the file so it is no longer readable

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A committed secret must be treated as exposed: rotate it, remove it, and have the application fetch it from a secrets manager with access controls and auditing. Making the repository private does not undo earlier exposure. Deleting the file leaves the password in history and still valid. Base64 is encoding, not encryption, and anyone can decode it.
</details>

---

### Question 26
**Scenario:** An internal API sends customer data between two services across the provider's network. Compliance requires protection against interception in transit.

A. Enable encryption at rest on the storage volumes of both services so the data is protected end to end
B. Use TLS for all connections between the services
C. Move both services to the same subnet so traffic never leaves the provider's network
D. Disable logging on both services so the data is never written anywhere

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** TLS encrypts data in transit between the services, which is what the requirement covers. Encryption at rest protects stored data, not data moving over the network. Sharing a subnet reduces exposure but does not encrypt anything. Disabling logging does nothing about interception and hurts troubleshooting.
</details>

---

### Question 27
**Scenario:** A review finds a firewall rule allowing SSH from `0.0.0.0/0` to every Linux VM.

A. Change SSH to a non-standard port and keep the rule open to the whole internet
B. Leave the rule, because SSH is encrypted and therefore safe to expose to any address
C. Add a second rule that also allows RDP from anywhere for Windows administrators
D. Restrict SSH to the admin network or a bastion, or use the provider's session manager instead

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Limiting SSH to known admin sources, a bastion host, or a session manager with no open inbound port removes the internet-wide attack surface. A different port only slows scanners a little. Encryption protects the session but not against password guessing or exploits in the SSH service. Opening RDP widely adds a second exposed service.
</details>

---

### Question 28
**Scenario:** A team wants every code change to be built and tested automatically, and every passing build to be ready to release at any time.

A. Manual change approval boards that meet weekly
B. A shared spreadsheet that lists every build, its test results and its release status for each environment
C. Continuous integration with continuous delivery
D. Nightly full-system backups of the build server

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Continuous integration builds and tests each change as it is merged, and continuous delivery keeps every passing build in a releasable state. Weekly approval boards slow delivery and are not automation. A spreadsheet records results but does not produce them. Backups protect the build server, not the release process.
</details>

---

### Question 29
**Scenario:** An auto scaling group launches new instances during a spike, but each one is terminated as unhealthy a few minutes later, and the group keeps cycling.

A. Check the launch template's image and startup script, and the health check grace period
B. Raise the group's maximum size so it can launch even more instances at the same time
C. Turn off health checks on the load balancer so the new instances are never marked unhealthy
D. Switch the group to a different region

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** New instances failing health checks usually means the image or bootstrap script is broken, or the grace period is shorter than the app's startup time. Raising the maximum launches more broken instances. Disabling health checks hides the failure and sends traffic to instances that cannot serve. Changing region does not fix a broken template.
</details>

---

### Question 30
**Scenario:** A script that calls a cloud provider's API starts failing with HTTP 429 responses during a bulk job.

A. The API credentials have expired and must be reissued before any further calls will work
B. The script is being throttled; slow down and retry with exponential backoff and jitter
C. The provider's region is down, so fail over to another region straight away
D. The script needs a larger VM

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** HTTP 429 means too many requests: the provider is rate limiting, so the client should back off and retry with increasing, randomized delays, or request a higher quota. Expired credentials return 401 or 403, not 429. A regional outage shows up as errors or timeouts across services, not specifically rate limiting. A larger VM sends requests faster, which makes throttling worse.
</details>

---

## Where to go deeper

- [Cloud+ cert page](../../exams/comptia/cloud-plus/) - notes, practice plan, strategy
- [Security+ practice questions](https://security.noblerworks.com/resources/practice-questions/comptia-security-plus/) - the security sibling
- [AWS Cloud Practitioner practice questions](./aws-cloud-practitioner.md) - a vendor-specific view of the same concepts
- [What is cloud computing?](../../learn/concepts/what-is-cloud-computing.md) - plain-English foundation
- **[📖 CompTIA Cloud+](https://www.comptia.org/certifications/cloud)** - official exam objectives
