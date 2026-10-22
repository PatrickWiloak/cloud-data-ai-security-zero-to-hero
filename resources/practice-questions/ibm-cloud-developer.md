---
last-updated: 2026-10-22
difficulty: intermediate
---

# IBM Certified Application Developer - Cloud Platform - Practice Questions

30 questions for this exam, weighted toward IBM Cloud platform services (25%), development fundamentals (20%), then data services, AI and Watson integration, security, and messaging.

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

### Question 16
**Scenario:** A web app stores user sessions in process memory. When it scales from one instance to four, users are randomly logged out. What is the cloud-native fix?

A. Pin each user to one instance with sticky sessions and never scale in
B. Increase the memory of each instance so sessions are kept for longer
C. Move session state to an external store such as Databases for Redis
D. Run a single large instance instead of four smaller instances

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Cloud-native processes should be stateless, with shared state held in a backing service, so any instance can serve any request and instances can come and go. Sticky sessions break when an instance is replaced or scaled in. More memory does not share sessions between instances. One large instance gives up horizontal scaling and resilience.

**Key Concept:** Keep processes stateless and put state in backing services. See [Getting started with Databases for Redis](https://cloud.ibm.com/docs/databases-for-redis?topic=databases-for-redis-getting-started).
</details>

---

### Question 17
**Scenario:** A containerized service on Kubernetes takes 60 seconds to load its cache at startup. During that time it receives traffic and returns errors. Separately, it sometimes hangs and needs restarting. Which probes address both problems?

A. A readiness probe to hold traffic until it is ready, and a liveness probe to restart it when hung
B. A liveness probe to hold traffic until it is ready, and a readiness probe to restart it when hung
C. Only a liveness probe with a short timeout, which handles both startup and hangs
D. No probes; a larger replica count hides both problems from users

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A failing readiness probe removes the pod from service endpoints without restarting it, which fits a slow start. A failing liveness probe restarts the container, which fits a hang. Swapping them restarts healthy-but-starting pods and leaves hung pods in service. A short liveness probe alone would kill the pod during its 60 second start; a startup probe can also help here. More replicas still send some traffic to bad pods.

**Key Concept:** Readiness controls traffic; liveness controls restarts. See [Liveness, readiness, and startup probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/).
</details>

---

### Question 18
**Scenario:** An order service consumes messages with at-least-once delivery. After a network blip, some messages arrive twice and customers are charged twice. What should the developer change?

A. Switch to at-most-once delivery so a message can never arrive twice
B. Add a sleep before each message is processed so duplicates expire first
C. Increase the consumer count so duplicates are spread across instances
D. Make processing idempotent, for example by tracking processed order IDs

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** With at-least-once delivery, duplicates are expected, so consumers must be idempotent: processing the same message twice has the same effect as once, for example by recording each order ID. At-most-once delivery can lose payments instead. Sleeping does not remove duplicates. More consumers make duplicates more likely to run in parallel.

**Key Concept:** Design consumers to be idempotent in event-driven systems. See [What is event-driven architecture?](https://www.ibm.com/think/topics/event-driven-architecture)
</details>

---

### Question 19
**Scenario:** A nightly task processes a batch of files and then exits. It does not serve HTTP requests. The team wants to run it on Code Engine. Which Code Engine resource fits?

A. An application, configured with a minimum scale of one instance
B. A job, which runs instances to completion and then stops
C. A build, which compiles the code and runs it as part of the build
D. A configmap, which stores the batch logic and runs on a schedule

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Code Engine jobs run one or more instances to completion and stop, which suits batch work; they can be run on a schedule with a cron subscription. Applications serve HTTP requests and keep running or scale on traffic. Builds turn source into images. Configmaps hold configuration data, not code to run.

**Key Concept:** Apps for request-driven workloads, jobs for run-to-completion workloads. See [Planning for Code Engine jobs](https://cloud.ibm.com/docs/codeengine?topic=codeengine-job-plan).
</details>

---

### Question 20
**Scenario:** A Code Engine application is cheap to run because it scales to zero, but the first request after a quiet period is slow. The team wants to remove that delay for a latency-sensitive API. What should they change?

A. Set the minimum number of instances to one so an instance is always running
B. Lower the maximum number of instances so the application starts faster
C. Move the application to a Code Engine job that runs on a schedule
D. Increase the request timeout so slow first requests do not fail

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** With a minimum scale of zero, the first request after idle waits for an instance to start. Setting the minimum to one keeps an instance warm, at the cost of paying for it. Lowering the maximum limits scale-out and does not affect start time. Jobs do not serve requests. A longer timeout hides failures but keeps the delay.

**Key Concept:** Scale-to-zero trades cold-start latency for cost. See [Configuring application scaling](https://cloud.ibm.com/docs/codeengine?topic=codeengine-app-scale).
</details>

---

### Question 21
**Scenario:** A team has a Node.js application in a Git repository with no Dockerfile. They want Code Engine to turn the source into a container image and run it. What should they use?

A. A Code Engine job that clones the repository and runs `npm start` on each run
B. A Kubernetes Service cluster, because Code Engine only runs prebuilt images
C. A manual build on a laptop, pushed to Container Registry before each deploy
D. A Code Engine build using the buildpacks strategy to create the image

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Code Engine builds can create images from source using a Dockerfile strategy or a buildpacks strategy, which detects the language and builds without a Dockerfile. A job that clones and runs source on each run is slow and unrepeatable. Code Engine can build from source, so a cluster is not needed. Laptop builds are not reproducible or automated.

**Key Concept:** Buildpacks build images from source without a Dockerfile. See [Planning your build](https://cloud.ibm.com/docs/codeengine?topic=codeengine-plan-build).
</details>

---

### Question 22
**Scenario:** Before deploying, a team wants to know whether their container images in IBM Cloud Container Registry contain packages with known vulnerabilities. What should they use?

A. IBM Cloud Monitoring alerts on each running container's CPU usage
B. Activity Tracker events for every image push to the registry
C. Vulnerability Advisor, which scans images in Container Registry
D. Secrets Manager, which rotates credentials stored inside each image

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Vulnerability Advisor scans images stored in Container Registry for known vulnerable packages and reports issues to fix. Monitoring tracks runtime metrics. Activity Tracker records who pushed an image, not what is in it. Secrets Manager manages secrets and should be used instead of putting credentials in images.

**Key Concept:** Scan images before they reach production. See [Managing image security with Vulnerability Advisor](https://cloud.ibm.com/docs/Registry?topic=Registry-va_index).
</details>

---

### Question 23
**Scenario:** A new billing feature needs strict relational integrity, multi-table transactions, and complex joins. Which managed database fits best?

A. IBM Cloudant, a JSON document store
B. Databases for PostgreSQL, a relational database
C. Databases for Redis, an in-memory key-value store
D. IBM Cloud Object Storage, an object store

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** PostgreSQL is a relational database with ACID transactions, foreign keys, and rich joins, which billing data needs. Cloudant is a document store that suits flexible JSON and sync, not multi-table transactions. Redis is fast for caching and sessions but is not a system of record for relational data. Object Storage holds files, not transactional records.

**Key Concept:** Choose the data store by access pattern and consistency needs. See [Getting started with Databases for PostgreSQL](https://cloud.ibm.com/docs/databases-for-postgresql?topic=databases-for-postgresql-getting-started).
</details>

---

### Question 24
**Scenario:** Users upload video files of several gigabytes. Routing uploads through the application server is slow and costly. The team wants browsers to upload straight to Object Storage for a short, controlled time. What should the app do?

A. Make the bucket publicly writable so that browsers can upload without credentials
B. Send the bucket's API key to each browser so that it can authenticate by itself
C. Stream every upload through a Code Engine function that writes the object
D. Generate a short-lived presigned URL, using HMAC credentials, for each upload

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** A presigned URL grants time-limited permission for one operation on one object, so the browser uploads directly to Object Storage without receiving long-term credentials; Object Storage presigned URLs require HMAC credentials. A publicly writable bucket lets anyone upload anything. Sending API keys to browsers leaks them. Streaming through a function keeps the slow, costly hop.

**Key Concept:** Presigned URLs delegate narrow, temporary access to clients. See [Creating a presigned URL](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-presign-url).
</details>

---

### Question 25
**Scenario:** A support chatbot built on a watsonx.ai foundation model gives confident but wrong answers about the company's own products, which the model was never trained on. What is the most suitable approach?

A. Retrieval-augmented generation, adding relevant company documents to each prompt
B. A higher temperature setting, so the model explores more possible answers
C. A longer maximum output length, so the model can explain itself fully
D. A larger model, which will know the company's products from pretraining

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** RAG retrieves relevant passages from the company's own content and includes them in the prompt, grounding answers in facts the model was never trained on. Higher temperature adds randomness and usually more errors. Longer output does not add knowledge. A larger model still has not seen private product documents.

**Key Concept:** Ground foundation models in your own data with retrieval. See [What is retrieval-augmented generation?](https://www.ibm.com/think/topics/retrieval-augmented-generation)
</details>

---

### Question 26
**Scenario:** A contact center app must turn recorded customer calls into text so they can be searched and analysed. Which IBM service fits directly?

A. Watson Text to Speech, which produces audio from text
B. Watson Speech to Text, which transcribes audio to text
C. IBM Cloud Object Storage, which indexes audio contents
D. Event Streams, which converts audio into text events

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Speech to Text transcribes spoken audio into text through an API, including for recorded audio files. Text to Speech does the reverse. Object Storage stores the audio files but does not transcribe them. Event Streams moves messages between systems; it does not process audio.

**Key Concept:** Pick the AI service whose input and output match the task. See [Getting started with Speech to Text](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-gettingStarted).
</details>

---

### Question 27
**Scenario:** Several independent services must read the same stream of order events at their own pace, and a new analytics service must be able to replay the last seven days of events. Which service fits best?

A. Databases for Redis, using a list as a work queue that each service drains
B. An HTTP webhook from the order service to each consumer, sent once
C. IBM Event Streams, a Kafka-based service that retains events for replay
D. IBM Cloud Object Storage, polled every second by each consuming service

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Event Streams is managed Apache Kafka: events are kept in a log for a set retention time, each consumer group reads at its own offset, and consumers can replay from earlier offsets. A Redis list is drained by whoever pops first, so services would compete for events. Webhooks are fire-once with no replay. Polling object storage is slow and not built for streams.

**Key Concept:** Use a log-based event stream when many consumers need the same events and replay. See [About Event Streams](https://cloud.ibm.com/docs/EventStreams?topic=EventStreams-about).
</details>

---

### Question 28
**Scenario:** A payment system exchanges messages with a core banking platform. Each message must be delivered once and only once, inside transactions, even if a system restarts mid-transfer. Which messaging service is the strongest fit?

A. A plain HTTP call from one system to the other with no retries
B. A shared file in Object Storage that each system reads and writes
C. Databases for Redis publish and subscribe channels between systems
D. IBM MQ, which provides assured, transactional message delivery

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** IBM MQ is built for assured, once-only delivery with transactional support, which is why it is common in banking. A plain HTTP call can lose messages on failure. A shared file has no delivery guarantees and invites conflicts. Redis pub/sub is fire-and-forget: subscribers that are offline miss messages.

**Key Concept:** Match the messaging service to the delivery guarantee the business needs. See [IBM MQ](https://www.ibm.com/products/mq).
</details>

---

### Question 29
**Scenario:** A Code Engine application needs to call other IBM Cloud APIs. The team does not want to create, store, or rotate an API key for it. What should they use?

A. A trusted profile, so the workload gets IAM tokens without a stored API key
B. The account owner's personal API key, stored in a Code Engine secret
C. A service ID API key, hard-coded in the source code for convenience
D. No authentication, because calls from inside IBM Cloud are trusted

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Trusted profiles let compute resources, including Code Engine workloads, obtain IAM tokens based on their identity, so there is no long-lived key to store or rotate. A personal key ties the app to one user and grants far too much. Hard-coded keys leak through source control. IBM Cloud APIs always require authentication.

**Key Concept:** Prefer workload identity over stored keys. See [Using trusted profiles with Code Engine](https://cloud.ibm.com/docs/codeengine?topic=codeengine-trusted-profiles).
</details>

---

### Question 30
**Scenario:** A regulated customer requires that data in an Object Storage bucket be encrypted with a root key they control and can revoke, rather than with provider-managed keys. What should the developer configure?

A. Client-side base64 encoding of each object before it is uploaded
B. A Key Protect root key used to encrypt the bucket's data encryption keys
C. A private endpoint for the bucket so data never crosses the internet
D. A bucket retention policy so that objects cannot be deleted early

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** With Key Protect, a customer-managed root key wraps the data encryption keys for the bucket (envelope encryption), so the customer controls access and can revoke the key to make data unreadable. Base64 is encoding, not encryption. Private endpoints protect data in transit, not key control. Retention policies prevent deletion but do not change encryption.

**Key Concept:** Envelope encryption with customer-managed keys gives control over data access. See [Envelope encryption](https://cloud.ibm.com/docs/key-protect?topic=key-protect-envelope-encryption).
</details>

---

## Where to go deeper

- [IBM Cloud Developer cert page](../../exams/ibm/cloud-developer/) - notes, practice plan, strategy
- [IBM Cloud Advocate practice questions](./ibm-cloud-advocate.md) - the platform fundamentals
- [IBM Cloud Security Engineer practice questions](https://security.noblerworks.com/resources/practice-questions/ibm-cloud-security-engineer/) - the security domain in depth
- [Twelve-factor thinking in CI/CD](../../learn/concepts/cicd-explained.md) - pipelines in plain English
- **[📖 IBM Training](https://www.ibm.com/training/)** - official certification pages
