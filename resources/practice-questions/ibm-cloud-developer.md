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

A. Store state on local disk
B. The twelve-factor principles: configuration from the environment, stateless processes, backing services as attached resources, disposability, and logs as event streams
C. One large deployable unit
D. Manual configuration per environment

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** These principles are what make an application safe to scale horizontally and to replace at any moment. Configuration from the environment is the one that makes the same artifact promotable across environments, which is the basis of a sane pipeline.
</details>

---

### Question 2
**Scenario:** An application must run as a container without managing a cluster.

A. Virtual servers
B. IBM Cloud Code Engine, which runs containers, jobs, and functions with scale-to-zero
C. Bare metal
D. A Kubernetes cluster you operate

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Code Engine handles the platform so the deployable unit is the container image. A managed Kubernetes service is the right choice once you need the full Kubernetes API for operators, custom controllers, or complex networking.
</details>

---

### Question 3
**Scenario:** An application binds to a managed database.

A. Hard-code the connection string
B. Create a service credential or use a service binding, injecting the connection details as environment variables at run time
C. A configuration file in the image
D. Ask an administrator each time

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Binding injects credentials at run time so the image contains no secrets and works unchanged across environments. Anything baked into the image is in the registry, in the layer history, and in every environment that pulls it.
</details>

---

### Question 4
**Scenario:** A document-oriented store is needed with offline sync for mobile.

A. Db2
B. Cloudant, a JSON document store with replication and offline sync
C. Object Storage
D. Redis

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cloudant's replication protocol is what enables the offline-first mobile pattern, syncing when connectivity returns. Db2 is the relational option and Object Storage holds unstructured blobs, neither of which offers document sync.
</details>

---

### Question 5
**Scenario:** A large file uploaded by a user must be stored durably.

A. The application's local filesystem
B. IBM Cloud Object Storage, with the object key returned to the application
C. A database BLOB column
D. In memory

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Local disk disappears when the container is replaced, which is guaranteed to happen. Object storage is durable, cheap per gigabyte, and can serve the file directly with a presigned URL, keeping the bytes off your application's request path entirely.
</details>

---

### Question 6
**Scenario:** Services must communicate asynchronously with durable delivery.

A. Direct synchronous HTTP for everything
B. A message queue or event stream such as IBM MQ or Event Streams (Kafka), decoupling producer and consumer
C. Shared database polling
D. Local files

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Durable messaging means the consumer can be down without work being lost, and the producer is not blocked by the consumer's speed. Choose a queue when each message has one consumer and a stream when several consumers need independent replay.
</details>

---

### Question 7
**Scenario:** An application must call a watsonx or Watson service.

A. Train a model first
B. Provision the service, obtain credentials via IAM, and call the REST API or SDK with a bearer token
C. Install the model locally
D. Use a public endpoint with no authentication

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** IBM Cloud services authenticate through IAM tokens derived from an API key, and the SDKs handle the exchange and refresh. The point of a consumable AI service is that no training is required to start.
</details>

---

### Question 8
**Scenario:** An API must be exposed to external consumers with rate limiting and keys.

A. Expose the service directly
B. An API gateway (API Connect or equivalent) handling authentication, rate limits, versioning, and analytics
C. A load balancer
D. A firewall

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The gateway centralizes cross-cutting API concerns so each service does not reimplement them. It also gives you a stable external contract, which means you can version and refactor services behind it without breaking consumers.
</details>

---

### Question 9
**Scenario:** Users must authenticate with social or enterprise identities.

A. Build your own user store
B. IBM Cloud App ID (or another identity provider) handling sign-in, token issuance, and federation
C. Store passwords in the database
D. Basic authentication

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Delegating authentication removes password storage, reset flows, and MFA from your codebase, which is a large amount of security-critical work you would otherwise own. Your application validates a token and reads claims.
</details>

---

### Question 10
**Scenario:** A container image must be built and deployed on every commit.

A. Manual builds
B. A pipeline (Continuous Delivery toolchain or another CI system) building, scanning, and deploying with environment promotion
C. Build on a developer laptop
D. Deploy from an IDE

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Automation makes the build reproducible and inserts the vulnerability scan and tests as gates. Laptop builds embed whatever was installed on that machine, which is how "works on my machine" becomes a production incident.
</details>

---

### Question 11
**Scenario:** An application must handle a transient failure calling a downstream service.

A. Fail immediately
B. Retry with exponential backoff and jitter, bounded, with a circuit breaker and a timeout
C. Retry forever
D. Ignore errors

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Transient failures are normal in distributed systems, but unbounded retries amplify an outage rather than riding it out. Jitter prevents every client retrying in the same instant, and a circuit breaker stops hammering a service that is clearly down.
</details>

---

### Question 12
**Scenario:** Application logs must be searchable across instances.

A. Write to local files
B. Write structured logs to stdout and let the platform collect them into a centralized logging service
C. Email logs
D. Print to the console only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Treating logs as an event stream on stdout is a twelve-factor principle for exactly this reason: the platform routes them, so the application does not need log rotation or shipping code. Structure makes them queryable rather than grep-able.
</details>

---

### Question 13
**Scenario:** A configuration value differs per environment.

A. Separate code branches
B. Environment variables or a configuration service, so the same image runs everywhere
C. Hard-code with an if statement
D. Rebuild per environment

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Rebuilding per environment means the artifact you tested is not the artifact you shipped. One image promoted through environments with external configuration is what makes staging results meaningful.
</details>

---

### Question 14
**Scenario:** A serverless function should run when an object lands in Object Storage.

A. Poll the bucket
B. An event-driven trigger invoking the function on the object creation event
C. A scheduled job
D. Manual invocation

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Event triggers respond immediately and cost nothing while idle. Polling burns cycles finding nothing most of the time and adds latency equal to half the polling interval on average.
</details>

---

### Question 15
**Scenario:** An application's dependencies must be kept current and free of known vulnerabilities.

A. Update once a year
B. Automated dependency scanning in the pipeline with alerts and update pull requests, plus a policy for severity thresholds
C. Update only when something breaks
D. Pin forever

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Most application vulnerabilities arrive through dependencies rather than your own code. Automating both detection and the update pull request keeps the effort small and continuous, which is the only way it survives contact with a delivery schedule.
</details>

---

## Where to go deeper

- [IBM Cloud Developer cert page](../../exams/ibm/cloud-developer/) - notes, practice plan, strategy
- [IBM Cloud Advocate practice questions](./ibm-cloud-advocate.md) - the platform fundamentals
- [IBM Cloud Security Engineer practice questions](./ibm-cloud-security-engineer.md) - the security domain in depth
- [Twelve-factor thinking in CI/CD](../../learn/concepts/cicd-explained.md) - pipelines in plain English
- **[📖 IBM Training](https://www.ibm.com/training/)** - official certification pages
