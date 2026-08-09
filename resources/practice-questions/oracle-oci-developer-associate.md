---
last-updated: 2026-08-09
difficulty: intermediate
---

# Oracle Cloud Infrastructure Developer Associate (1Z0-1084) - Practice Questions

15 questions for OCI Developer Associate prep, weighted toward OCI developer services (20%) and Functions (20%), then OKE (15%), DevOps services (15%), and OCIR, observability, and cloud native fundamentals.

> **Cert page:** [exams/oracle/oci-developer-associate/](../../exams/oracle/oci-developer-associate/)

---

### Question 1
**Scenario:** OCI Functions is based on which open source project?

A. Knative
B. Fn Project
C. OpenFaaS
D. Kubeless

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OCI Functions is a managed Fn Project service, so functions are packaged as container images and the `fn` CLI is the local tooling. Knowing it is container-based explains why any language works and why cold start relates to image size.
</details>

---

### Question 2
**Scenario:** A function must access an Object Storage bucket without stored credentials.

A. An API key in the function code
B. Resource principals: a dynamic group matching the function and a policy granting that group access
C. A public bucket
D. A username and password

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Resource principals are the serverless equivalent of instance principals: the function authenticates as itself using a token the platform supplies. Any credential embedded in the image is visible to anyone who can pull it from the registry.
</details>

---

### Question 3
**Scenario:** A function must run when an object is uploaded to a bucket.

A. Poll the bucket
B. An Events rule matching the object create event, with the function as the action
C. A scheduled job
D. A webhook from the client

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OCI Events emits on resource lifecycle changes, and rules route matching events to Functions, Notifications, or Streaming. Polling adds latency equal to half the interval and costs money finding nothing most of the time.
</details>

---

### Question 4
**Scenario:** Container images must be stored privately for OKE to pull.

A. Docker Hub public
B. OCI Container Registry (OCIR), with an image pull secret or the appropriate policy for the cluster
C. A file server
D. Local build only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OCIR is the private registry integrated with OCI IAM, so access follows compartment policy. The practical detail is authentication: OCIR uses an auth token rather than your console password for docker login.
</details>

---

### Question 5
**Scenario:** An OKE cluster's worker nodes must be private but still pull images and reach OCI services.

A. Public worker nodes
B. Private node subnets with a NAT gateway for internet egress and a service gateway for OCI services
C. No gateways
D. An internet gateway on the node subnet

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Private nodes need outbound access without inbound reachability, which is exactly NAT, and the service gateway keeps OCIR and Object Storage traffic on the Oracle network. Putting an internet gateway on the node subnet would make the nodes publicly reachable.
</details>

---

### Question 6
**Scenario:** A microservice must publish events consumed by several independent services.

A. Direct HTTP calls to each
B. OCI Streaming (Kafka-compatible), where each consumer group reads independently
C. A shared database table
D. A queue with one consumer

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A stream retains messages and lets multiple consumer groups read at their own offsets, which is what "several independent consumers" requires. A queue delivers each message once, so adding a consumer means losing messages from another.
</details>

---

### Question 7
**Scenario:** An API must be published with authentication, rate limiting, and request validation.

A. Expose the function directly
B. API Gateway in front, with policies for authentication, rate limiting, and CORS
C. A load balancer
D. A security list

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The gateway centralizes cross-cutting concerns and gives a stable external contract, so backends can change without breaking consumers. It can also invoke a function as an authorizer for custom authentication logic.
</details>

---

### Question 8
**Scenario:** A build and deployment pipeline must run in OCI.

A. Manual builds
B. OCI DevOps service with build pipelines, an artifact registry, and deployment pipelines supporting rolling, blue-green, and canary strategies
C. A shell script on a VM
D. Local deployment

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The DevOps service covers the whole path from source through build to deployment with approval stages, so the artifact that was tested is the artifact deployed. Deployment strategy support is what makes a safe rollout a configuration rather than a script.
</details>

---

### Question 9
**Scenario:** A function is timing out on a long-running task.

A. Increase the timeout indefinitely
B. Functions have a maximum execution time, so decompose the work, hand it to a queue or a container instance, or use a different compute service for long jobs
C. Retry forever
D. Add memory only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Recognizing when a workload has outgrown serverless is the design skill. Long-running or stateful work belongs in Container Instances, OKE, or a compute instance, with the function acting as a trigger rather than the worker.
</details>

---

### Question 10
**Scenario:** Application secrets must not appear in the container image or environment.

A. Bake them into the image
B. OCI Vault secrets, retrieved at run time using the resource or instance principal
C. A config file in the repository
D. Command-line arguments

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Vault plus a principal-based identity means no secret exists in the artifact or the deployment manifest, and rotation happens in one place. Environment variables are better than baking into the image but are still visible to anyone who can describe the resource.
</details>

---

### Question 11
**Scenario:** Application traces must be collected across services.

A. Logs only
B. Application Performance Monitoring with tracing, instrumented in the application, plus Logging for events
C. Metrics only
D. Manual timing

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Traces show where the latency went across service boundaries, which logs cannot without manual correlation. The prerequisite is context propagation: every service must forward the trace headers or the trace fragments.
</details>

---

### Question 12
**Scenario:** A twelve-factor principle relevant to cloud native development.

A. Store configuration in the code
B. Store configuration in the environment, keep processes stateless, and treat backing services as attached resources
C. Use local disk for state
D. One deployment per environment build

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Stateless processes with external configuration are what make a container replaceable at any moment, which is the assumption every orchestrator makes. Local state means a rescheduled pod loses data, and the orchestrator will reschedule.
</details>

---

### Question 13
**Scenario:** A Kubernetes deployment on OKE must scale with request load.

A. A fixed replica count
B. A Horizontal Pod Autoscaler on a suitable metric, with the cluster autoscaler adding nodes when pods cannot be placed
C. A larger node
D. Manual scaling

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The two autoscalers work together: HPA adds pods and the cluster autoscaler adds nodes when there is nowhere to put them. Pods must declare resource requests, or the scheduler cannot tell when the cluster is full.
</details>

---

### Question 14
**Scenario:** A function's cold start latency is too high.

A. Nothing can be done
B. Reduce image size, minimize initialization work, and use provisioned concurrency where available for latency-sensitive paths
C. Increase the timeout
D. Add more functions

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cold start is dominated by image pull and runtime initialization, so a slim image and lazy initialization address most of it. Where the latency budget is strict, keeping instances warm is the remaining lever, at the cost of paying for idle capacity.
</details>

---

### Question 15
**Scenario:** A container must run without managing a Kubernetes cluster.

A. OKE only
B. OCI Container Instances, running containers directly as a serverless workload
C. A compute instance with Docker
D. A function only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Container Instances fills the gap between Functions (short, event-driven) and OKE (full orchestration): a container that runs for a while with no cluster to operate. Choosing between the three by workload shape is a recurring exam theme.
</details>

---

## Where to go deeper

- [OCI Developer Associate cert page](../../exams/oracle/oci-developer-associate/) - notes, practice plan, strategy
- [OCI Foundations practice questions](./oracle-oci-foundations.md) - the platform fundamentals
- [OCI Architect Associate practice questions](./oracle-oci-architect-associate.md) - the infrastructure counterpart
- [Serverless explained](../../learn/concepts/serverless-explained.md) - functions in plain English
- **[📖 Oracle University certification](https://education.oracle.com/oracle-certification-path/pFamily_647)** - official exam pages
