---
last-updated: 2026-08-09
difficulty: intermediate
---

# IBM Certified Application Developer - Cloud Platform - Practice Questions

15 questions for this exam, weighted toward IBM Cloud platform services (25%), development fundamentals (20%), then data services, AI and Watson integration, security, and messaging.

> **Cert page:** [exams/ibm/cloud-developer/](../../exams/ibm/cloud-developer/)

---

### Question 1
**Scenario:** Which principles guide building applications for cloud?

A. The twelve-factor principles: config in the environment, stateless processes, attached backing services, disposability
B. Keep session state on the local disk of each instance, so that restarts reload it quickly and scaling stays simple and cheap for the team
C. Manual configuration per environment
D. One large deployable unit, in which every feature and library is built, tested and released together on one fixed release schedule

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** These principles are what make an application safe to scale horizontally and to replace at any moment. Configuration from the environment is the one that makes the same artifact promotable across environments, which is the basis of a sane pipeline.
</details>

---

### Question 2
**Scenario:** An application must run as a container without managing a cluster.

A. Virtual servers, where the cloud provider patches the operating system and orchestrates the container lifecycle for you
B. A Kubernetes cluster you operate
C. IBM Cloud Code Engine, which runs containers, jobs, and functions with scale-to-zero
D. Bare metal

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Code Engine handles the platform so the deployable unit is the container image. A managed Kubernetes service is the right choice once you need the full Kubernetes API for operators, custom controllers, or complex networking.
</details>

---

### Question 3
**Scenario:** An application binds to a managed database.

A. Ask an administrator each time
B. Hard-code the connection string in a constant in the source code, so the application starts without needing any lookup
C. A configuration file in the image holding the connection string, which the container registry encrypts at rest
D. Use a service credential or binding, injecting connection details as environment variables at run time

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Binding injects credentials at run time so the image contains no secrets and works unchanged across environments. Anything baked into the image is in the registry, in the layer history, and in every environment that pulls it.
</details>

---

### Question 4
**Scenario:** A document-oriented store is needed with offline sync for mobile.

A. Redis
B. Cloudant, a JSON document store with replication and offline sync
C. Db2
D. Object Storage

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cloudant's replication protocol is what enables the offline-first mobile pattern, syncing when connectivity returns. Db2 is the relational option and Object Storage holds unstructured blobs, neither of which offers document sync.
</details>

---

### Question 5
**Scenario:** A large file uploaded by a user must be stored durably.

A. In the memory of the process that received the upload, kept until the next restart
B. A BLOB column in a single-instance database that has no replication or backups configured
C. IBM Cloud Object Storage, with the object key returned to the application
D. The application's local filesystem, mirrored to a second disk on the same host for durability

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Local disk disappears when the container is replaced, which is guaranteed to happen. Object storage is durable, cheap per gigabyte, and can serve the file directly with a presigned URL, keeping the bytes off your application's request path entirely.
</details>

---

### Question 6
**Scenario:** Services must communicate asynchronously with durable delivery.

A. Direct synchronous HTTP for everything, with the caller waiting on each response before it continues
B. A message queue or event stream such as IBM MQ or Event Streams (Kafka)
C. Local files written by the producer and read by the consumer from the same shared folder
D. Consumers polling a shared database table every few seconds, with no delivery guarantees

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Durable messaging means the consumer can be down without work being lost, and the producer is not blocked by the consumer's speed. Choose a queue when each message has one consumer and a stream when several consumers need independent replay.
</details>

---

### Question 7
**Scenario:** An application must call a watsonx or Watson service.

A. Install the model locally
B. Use a public endpoint with no authentication
C. Provision the service, obtain credentials via IAM, and call the REST API or SDK with a bearer token
D. Train a model first

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** IBM Cloud services authenticate through IAM tokens derived from an API key, and the SDKs handle the exchange and refresh. The point of a consumable AI service is that no training is required to start.
</details>

---

### Question 8
**Scenario:** An API must be exposed to external consumers with rate limiting and keys.

A. A load balancer, which authenticates callers with API keys and enforces per-consumer rate limits and quotas
B. A firewall
C. Expose the service directly to consumers on its own public URL, and leave the limits to each service's own code
D. An API gateway (API Connect or equivalent) handling authentication, rate limits, and analytics

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The gateway centralizes cross-cutting API concerns so each service does not reimplement them. It also gives you a stable external contract, which means you can version and refactor services behind it without breaking consumers.
</details>

---

### Question 9
**Scenario:** Users must authenticate with social or enterprise identities.

A. Store passwords in the database
B. Build your own user store with hashed passwords and a login page, which keeps all identities under your control
C. Basic authentication
D. IBM Cloud App ID (or another identity provider) handling sign-in and tokens

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Delegating authentication removes password storage, reset flows, and MFA from your codebase, which is a large amount of security-critical work you would otherwise own. Your application validates a token and reads claims.
</details>

---

### Question 10
**Scenario:** A container image must be built and deployed on every commit.

A. Deploy straight from an IDE plugin on each developer's machine whenever that developer decides a change is finished
B. A pipeline (Continuous Delivery toolchain or other CI) that builds, scans and deploys with promotion
C. Manual builds run by the release manager from a written checklist on the day of each planned release, with no automation
D. Build on a developer laptop, then push the finished image to the registry by hand from that same machine each time

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Automation makes the build reproducible and inserts the vulnerability scan and tests as gates. Laptop builds embed whatever was installed on that machine, which is how "works on my machine" becomes a production incident.
</details>

---

### Question 11
**Scenario:** An application must handle a transient failure calling a downstream service.

A. Retry forever until the service answers, which guarantees that no request is ever lost during an outage
B. Fail immediately and return an error to the caller on the first timeout or error response, with no retry
C. Retry with exponential backoff and jitter, bounded, with a circuit breaker and a timeout
D. Ignore errors

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Transient failures are normal in distributed systems, but unbounded retries amplify an outage rather than riding it out. Jitter prevents every client retrying in the same instant, and a circuit breaker stops hammering a service that is clearly down.
</details>

---

### Question 12
**Scenario:** Application logs must be searchable across instances.

A. Write structured logs to stdout and let the platform collect them centrally
B. Print to the console only
C. Write to local files on each instance and rotate them nightly, then search them with grep over SSH
D. Email logs

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Treating logs as an event stream on stdout is a twelve-factor principle for exactly this reason: the platform routes them, so the application does not need log rotation or shipping code. Structure makes them queryable rather than grep-able.
</details>

---

### Question 13
**Scenario:** A configuration value differs per environment.

A. Environment variables or a config service, so one image runs everywhere
B. Rebuild per environment, baking each environment's values into its own image at build time
C. Hard-code the value with an if statement that checks which environment the code runs in
D. Keep a separate code branch for each environment, with the values edited directly in each branch

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Rebuilding per environment means the artifact you tested is not the artifact you shipped. One image promoted through environments with external configuration is what makes staging results meaningful.
</details>

---

### Question 14
**Scenario:** A serverless function should run when an object lands in Object Storage.

A. An event-driven trigger invoking the function on the object creation event
B. Poll the bucket
C. Manual invocation
D. A scheduled job

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Event triggers respond immediately and cost nothing while idle. Polling burns cycles finding nothing most of the time and adds latency equal to half the polling interval on average.
</details>

---

### Question 15
**Scenario:** An application's dependencies must be kept current and free of known vulnerabilities.

A. Pin forever
B. Automated dependency scanning in the pipeline with update pull requests and severity thresholds
C. Update only when something breaks, because stable pinned versions avoid regressions from untested upgrades
D. Update once a year

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Most application vulnerabilities arrive through dependencies rather than your own code. Automating both detection and the update pull request keeps the effort small and continuous, which is the only way it survives contact with a delivery schedule.
</details>

---

## Where to go deeper

- [IBM Cloud Developer cert page](../../exams/ibm/cloud-developer/) - notes, practice plan, strategy
- [IBM Cloud Advocate practice questions](./ibm-cloud-advocate.md) - the platform fundamentals
- [IBM Cloud Security Engineer practice questions](https://security.noblerworks.com/resources/practice-questions/ibm-cloud-security-engineer/) - the security domain in depth
- [Twelve-factor thinking in CI/CD](../../learn/concepts/cicd-explained.md) - pipelines in plain English
- **[📖 IBM Training](https://www.ibm.com/training/)** - official certification pages
