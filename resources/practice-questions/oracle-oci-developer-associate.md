---
last-updated: 2026-10-22
difficulty: intermediate
---

# Oracle Cloud Infrastructure Developer Associate (1Z0-1084) - Practice Questions

30 questions for OCI Developer Associate prep, weighted toward OCI developer services (20%) and Functions (20%), then OKE (15%), DevOps services (15%), and OCIR, observability, and cloud native fundamentals.

> **Cert page:** [exams/oracle/oci-developer-associate/](../../exams/oracle/oci-developer-associate/)

---

### Question 1
**Scenario:** OCI Functions is based on which open source project?

A. Kubeless
B. Fn Project, the open source container-native serverless platform
C. Knative Serving, the Kubernetes-native framework that OCI Functions runs on a managed OKE cluster
D. OpenFaaS, the self-hosted function framework

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OCI Functions is a managed Fn Project service, so functions are packaged as container images and the `fn` CLI is the local tooling. Knowing it is container-based explains why any language works and why cold start relates to image size.
</details>

---

### Question 2
**Scenario:** A function must access an Object Storage bucket without stored credentials.

A. Resource principals: a dynamic group matching the function and a policy for that group
B. A username and password for a dedicated IAM user, stored in the function configuration and rotated every 90 days
C. An API key and fingerprint for a service user, loaded from a file inside the function image at start-up
D. A public bucket

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Resource principals are the serverless equivalent of instance principals: the function authenticates as itself using a token the platform supplies. Any credential embedded in the image is visible to anyone who can pull it from the registry.
</details>

---

### Question 3
**Scenario:** A function must run when an object is uploaded to a bucket.

A. Poll the bucket from a long-running compute instance every minute and invoke the function for each new object it finds
B. An Events rule matching the object create event, with the function as the action
C. A webhook from the client
D. A scheduled job that lists the bucket every five minutes, which is simple but runs whether or not anything was uploaded

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OCI Events emits on resource lifecycle changes, and rules route matching events to Functions, Notifications, or Streaming. Polling adds latency equal to half the interval and costs money finding nothing most of the time.
</details>

---

### Question 4
**Scenario:** Container images must be stored privately for OKE to pull.

A. A file server inside the VCN holding image tarballs, which nodes copy and load by hand before starting each pod
B. Local build only
C. OCIR, with an image pull secret or the appropriate policy for the cluster
D. A public Docker Hub repository, since OKE nodes can pull from it without any secret and rate limits do not apply

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** OCIR is the private registry integrated with OCI IAM, so access follows compartment policy. The practical detail is authentication: OCIR uses an auth token rather than your console password for docker login.
</details>

---

### Question 5
**Scenario:** An OKE cluster's worker nodes must be private but still pull images and reach OCI services.

A. No gateways at all, because worker nodes in a private subnet reach OCIR and OCI services over internal DNS
B. Private node subnets with a NAT gateway for internet egress and a service gateway for OCI services such as OCIR and Object Storage
C. Public worker nodes
D. An internet gateway on the node subnet with security lists that deny all inbound traffic

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Private nodes need outbound access without inbound reachability, which is exactly NAT, and the service gateway keeps OCIR and Object Storage traffic on the Oracle network. Putting an internet gateway on the node subnet would make the nodes publicly reachable.
</details>

---

### Question 6
**Scenario:** A microservice must publish events consumed by several independent services.

A. Direct HTTP calls to each consuming service in turn, with the producer retrying whichever call fails, which keeps every consumer in sync
B. OCI Streaming (Kafka-compatible), where each consumer group reads independently
C. A single queue with one consumer service that re-publishes each message to the other services after it has processed it
D. A shared database table

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A stream retains messages and lets multiple consumer groups read at their own offsets, which is what "several independent consumers" requires. A queue delivers each message once, so adding a consumer means losing messages from another.
</details>

---

### Question 7
**Scenario:** An API must be published with authentication, rate limiting, and request validation.

A. Expose the function directly through its invoke endpoint and add checks in the function code, with throttling left to the caller
B. A load balancer in front with a listener per backend, which spreads traffic but does not validate tokens or limit request rates per client
C. API Gateway in front, with policies for authentication, rate limiting, and CORS
D. A security list on the subnet that allows only the client CIDR ranges, which filters by address but not by caller identity

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The gateway centralizes cross-cutting concerns and gives a stable external contract, so backends can change without breaking consumers. It can also invoke a function as an authorizer for custom authentication logic.
</details>

---

### Question 8
**Scenario:** A build and deployment pipeline must run in OCI.

A. A shell script on a VM triggered by cron that pulls the repository, builds, and copies files to servers, with no approval stages
B. Manual builds on a developer workstation, tagged by hand and pushed to the registry once someone has checked the tests passed
C. OCI DevOps service with build pipelines, an artifact registry, and deployment pipelines supporting rolling, blue-green, and canary strategies
D. Local deployment

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The DevOps service covers the whole path from source through build to deployment with approval stages, so the artifact that was tested is the artifact deployed. Deployment strategy support is what makes a safe rollout a configuration rather than a script.
</details>

---

### Question 9
**Scenario:** A function is timing out on a long-running task.

A. Increase the timeout indefinitely, since the function setting has no upper limit and a long task then always completes
B. Add memory only, because more memory also raises the execution time limit and so lets the long task finish in one run
C. Retry forever from the caller whenever the call times out, so the task eventually completes on a lucky invocation
D. Functions have a maximum execution time, so decompose the work, hand it to a queue or a container instance, or use a different compute service for long jobs

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Recognizing when a workload has outgrown serverless is the design skill. Long-running or stateful work belongs in Container Instances, OKE, or a compute instance, with the function acting as a trigger rather than the worker.
</details>

---

### Question 10
**Scenario:** Application secrets must not appear in the container image or environment.

A. OCI Vault secrets, retrieved at run time using the resource or instance principal
B. A config file kept in the repository, encrypted with a key that is committed in a separate branch of the same repository
C. Bake them into the image in a build layer that is deleted before the final stage, so the image history holds no copy
D. Command-line arguments passed at container start, which keep them out of the image but not out of the process list

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Vault plus a principal-based identity means no secret exists in the artifact or the deployment manifest, and rotation happens in one place. Environment variables are better than baking into the image but are still visible to anyone who can describe the resource.
</details>

---

### Question 11
**Scenario:** Application traces must be collected across services.

A. Manual timing added around each call with log statements, then compared by hand between services after each incident
B. Metrics only, such as CPU and request counts per service, which show that latency rose but not which service caused it
C. APM with tracing, instrumented in the application, plus Logging for events
D. Logs only, shipped to one log group, with each service writing its own timestamps and request identifiers

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Traces show where the latency went across service boundaries, which logs cannot without manual correlation. The prerequisite is context propagation: every service must forward the trace headers or the trace fragments.
</details>

---

### Question 12
**Scenario:** A twelve-factor principle relevant to cloud native development.

A. Store configuration in the environment, keep processes stateless, and treat backing services as attached resources
B. One deployment artifact per environment, with the configuration compiled into each build so nothing varies at run time or changes without a rebuild
C. Store configuration in the code, committed per environment so every setting is versioned with the app
D. Use local disk for state, since a container's filesystem persists across restarts and reschedules

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Stateless processes with external configuration are what make a container replaceable at any moment, which is the assumption every orchestrator makes. Local state means a rescheduled pod loses data, and the orchestrator will reschedule.
</details>

---

### Question 13
**Scenario:** A Kubernetes deployment on OKE must scale with request load.

A. A larger node shape for the pool, which raises capacity per node but does not add pods as request load grows
B. A fixed replica count sized for the daily peak, which handles load without any autoscaler but pays for it around the clock
C. Manual scaling by an engineer who runs `kubectl scale` when an alert fires, which reacts only after users see slow responses
D. An HPA on a suitable metric, with the cluster autoscaler adding nodes when pods cannot be placed

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The two autoscalers work together: HPA adds pods and the cluster autoscaler adds nodes when there is nowhere to put them. Pods must declare resource requests, or the scheduler cannot tell when the cluster is full.
</details>

---

### Question 14
**Scenario:** A function's cold start latency is too high.

A. Nothing can be done, because cold start is fixed by the platform and is not affected by image size or start-up code
B. Add more functions to the application, splitting the same code across several so each cold start is shorter overall
C. Increase the timeout, which gives the first slow invocation more time to finish but does not shorten the start-up itself or the image pull
D. Reduce image size, minimize initialization work, and use provisioned concurrency where available for latency-sensitive paths

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Cold start is dominated by image pull and runtime initialization, so a slim image and lazy initialization address most of it. Where the latency budget is strict, keeping instances warm is the remaining lever, at the cost of paying for idle capacity.
</details>

---

### Question 15
**Scenario:** A container must run without managing a Kubernetes cluster.

A. OCI Container Instances, running containers directly as a serverless workload with no nodes to manage
B. A function only, since Functions runs any container for as long as it needs without a time limit on a single invocation
C. OKE only, because a container can be scheduled only by Kubernetes, so a cluster must be created
D. Kubernetes built by hand on compute instances, so the team still operates the cluster

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Container Instances fills the gap between Functions (short, event-driven) and OKE (full orchestration): a container that runs for a while with no cluster to operate. Choosing between the three by workload shape is a recurring exam theme.
</details>

---

### Question 16
**Scenario:** A developer runs an OCI SDK script on a laptop. The SDK must authenticate as the developer's own IAM user without hardcoding credentials in the code.

A. Use instance principal authentication from the laptop
B. Paste the user's console password into an environment variable
C. Use an API signing key referenced by a profile in `~/.oci/config`
D. Use resource principal authentication inside the script

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** For a person working outside OCI, the SDKs and CLI read a configuration file profile holding the user OCID, tenancy OCID, key fingerprint, region, and the path to a private API signing key. Instance principals only work on OCI compute instances, and resource principals only inside supported OCI resources such as functions. The console password is never used for API signing.

**Key Concept:** [SDK and CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm)
</details>

---

### Question 17
**Scenario:** A batch job calling OCI APIs occasionally gets HTTP 429 (too many requests) and 503 responses, and the job then fails outright.

A. Use the SDK's retry strategy with exponential backoff
B. Retry immediately in a tight loop until the call succeeds
C. Ignore failed calls and continue with the next record
D. Request a higher service limit for every OCI service used

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** 429 and 503 are transient, and the OCI SDKs provide retry strategies that wait with exponential backoff and jitter before trying again. Retrying in a tight loop makes throttling worse. Skipping failed calls silently loses work, and service limits govern how many resources you can create, not API request rates.

**Key Concept:** [Python SDK: Retries](https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html)
</details>

---

### Question 18
**Scenario:** A shell script needs only the display names and OCIDs of instances from `oci compute instance list`, without installing extra JSON tools on the build agent.

A. Pipe the output through `grep` for lines containing "ocid1"
B. Use the CLI's `--query` option with a JMESPath expression
C. Add `--output table` and parse the column positions with `cut`
D. Call the REST API directly with `curl` and parse it by hand

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The OCI CLI supports `--query` with JMESPath to filter and reshape its JSON output, so the script gets exactly the fields it needs. Grepping JSON lines or slicing table columns breaks when formats or field lengths change. Hand-signing raw REST calls with `curl` is far more work than using the CLI that is already installed.

**Key Concept:** [Using the CLI](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliusing.htm)
</details>

---

### Question 19
**Scenario:** A function needs non-sensitive settings such as a bucket name and log level that differ between dev and prod, without rebuilding the image.

A. Hardcode the values and build a separate image per environment
B. Write the values to a file inside the function's container at startup
C. Store the values in an Autonomous Database table read on each call
D. Set configuration parameters on the application or the function

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** OCI Functions lets you define key-value configuration on the application (shared by all its functions) or on an individual function, passed in as environment variables at runtime. Building one image per environment breaks build-once-deploy-many. A file written at startup still needs the values from somewhere, and a database lookup on every call adds latency for static settings. Secrets belong in Vault, not in this configuration.

**Key Concept:** [Passing Custom Configuration Parameters to Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionspassingconfigparams.htm)
</details>

---

### Question 20
**Scenario:** Every function in one compartment must be allowed to read secrets from Vault using resource principals. The administrator is writing the dynamic group.

A. `ALL {instance.compartment.id = '<compartment-ocid>'}`
B. `ALL {resource.type = 'fnfunc', resource.compartment.id = '<compartment-ocid>'}`
C. `ALL {resource.type = 'fnapp', request.user.id = '<user-ocid>'}`
D. `ANY {group.name = 'Developers'}`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Functions are matched in dynamic group rules by `resource.type = 'fnfunc'`, narrowed here by compartment, and a policy then grants the dynamic group access to secrets. The `instance.compartment.id` rule matches compute instances, not functions. Request variables such as `request.user.id` are not dynamic group matching rules, and a dynamic group does not match IAM groups.

**Key Concept:** [Accessing Other Oracle Cloud Infrastructure Resources from Running Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsaccessingociresources.htm)
</details>

---

### Question 21
**Scenario:** A developer changed a function's code and wants one command that builds the new image, pushes it to Container Registry, and updates the function to use it.

A. `fn invoke myapp myfunc`
B. `docker build -t myfunc .`
C. `fn deploy --app myapp`
D. `oci fn function list`

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `fn deploy` builds the image, pushes it to the configured registry, and creates or updates the function in the named application in one step. `fn invoke` calls the function that is already deployed. `docker build` only builds a local image, and the `oci fn function list` command lists functions without changing any of them.

**Key Concept:** [Creating Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingfunctions.htm)
</details>

---

### Question 22
**Scenario:** A team wants Kubernetes on OKE but does not want to size, patch, or upgrade worker node VMs, and wants to pay for pod resources only.

A. An enhanced OKE cluster using virtual nodes
B. A basic OKE cluster with a large managed node pool
C. Self-managed Kubernetes installed on compute instances
D. OCI Functions with a Kubernetes manifest uploaded

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Virtual nodes give a serverless Kubernetes experience: OCI manages the underlying capacity and you pay for the resources pods request. Managed node pools still put worker VMs in your tenancy to size and upgrade, and self-managed Kubernetes adds the control plane as well. Functions does not run Kubernetes manifests.

**Key Concept:** [Comparing Virtual Nodes with Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingvirtualwithmanagednodes_topic.htm)
</details>

---

### Question 23
**Scenario:** Pods on an OKE cluster fail with `ImagePullBackOff` when pulling an image from a private OCI Container Registry repository.

A. Make the repository public so any cluster can pull it
B. Rebuild the image with a smaller base layer to speed pulls
C. Restart the worker nodes so the kubelet retries the pull
D. Create an auth-token pull secret and set `imagePullSecrets`

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** For a private repository, the pod needs credentials: a Kubernetes docker-registry secret with the tenancy namespace and username plus an OCI auth token as the password, referenced from the pod spec's `imagePullSecrets`. Making the repository public exposes the image. Image size and node restarts do not fix an authentication failure.

**Key Concept:** [Pulling Images from Container Registry during Deployment](https://docs.oracle.com/en-us/iaas/Content/Registry/Tasks/registrypullingimagesfromocir.htm)
</details>

---

### Question 24
**Scenario:** A web application on OKE must be reachable from the internet through an OCI-managed load balancer created and configured from the Kubernetes manifest.

A. A Service of type `ClusterIP` with the pods' container port exposed
B. A Service of type `LoadBalancer`, which provisions an OCI load balancer
C. A `NodePort` Service plus public IPs added by hand to each worker node
D. A ConfigMap that lists the pod IP addresses for external clients

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** On OKE, a Service of type `LoadBalancer` makes the cloud controller provision an OCI load balancer (or network load balancer, by annotation) in front of the pods. `ClusterIP` is reachable only inside the cluster. A hand-built `NodePort` setup exposes nodes directly and is not managed, and a ConfigMap stores configuration rather than routing traffic.

**Key Concept:** [Defining Kubernetes Services of Type LoadBalancer](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancers-subtopic.htm)
</details>

---

### Question 25
**Scenario:** An OCI DevOps deployment pipeline must release a new version to OKE by sending a small share of traffic to it first, then promoting it after validation.

A. A rolling update with `maxUnavailable` set to zero on the Deployment
B. A recreate strategy that deletes old pods first
C. A canary deployment strategy in the deployment pipeline
D. A manual `kubectl apply` run after hours

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** OCI DevOps supports canary deployments to OKE, shifting a portion of traffic to the new version and then promoting it after an approval or validation stage (it also supports blue-green). A rolling update replaces pods gradually but does not hold a controlled traffic share. Recreate causes downtime, and a manual apply skips the pipeline entirely.

**Key Concept:** [Deploying to OKE with DevOps](https://docs.oracle.com/en-us/iaas/Content/devops/using/deploy_oke.htm)
</details>

---

### Question 26
**Scenario:** A managed build stage in an OCI DevOps build pipeline must run unit tests, build a container image, and export it as an artifact. Where are those steps defined?

A. In a `build_spec.yaml` file in the source repository
B. In the OKE cluster's kubeconfig file
C. In the function's `func.yaml` file
D. In a policy statement for the DevOps dynamic group

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A managed build stage reads a build specification (`build_spec.yaml` by default) that lists the steps, environment variables, and output artifacts. kubeconfig holds cluster access details, `func.yaml` describes a single function's runtime and settings, and policies grant permissions but never define build steps.

**Key Concept:** [Build Specifications](https://docs.oracle.com/en-us/iaas/Content/devops/using/build_specs.htm)
</details>

---

### Question 27
**Scenario:** Order messages must be processed exactly by one of several worker instances, hidden from others while being processed, and returned for retry if the worker crashes.

A. A Notifications topic with an email subscription
B. An Events rule that fires on each new order
C. A Streaming stream read by every worker from the start
D. An OCI Queue with a visibility timeout

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** OCI Queue is a point-to-point message queue: a consumer receives a message, it stays hidden for the visibility timeout, and it reappears for another consumer if not deleted in time. Notifications fans out to every subscriber. Events reacts to resource state changes, and a stream read from the start by every worker delivers each message to all of them.

**Key Concept:** [Queue Overview](https://docs.oracle.com/en-us/iaas/Content/queue/overview.htm)
</details>

---

### Question 28
**Scenario:** Existing applications use Apache Kafka producer and consumer clients. The team wants a managed OCI service without rewriting the client code.

A. OCI Notifications with HTTPS subscriptions
B. OCI Streaming through its Kafka-compatible API
C. OCI Queue using its REST API
D. Object Storage with event rules

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OCI Streaming exposes a Kafka-compatible endpoint, so standard Kafka clients can produce and consume by changing connection configuration rather than code. Notifications and Queue use different APIs and messaging models, so the clients would need rewriting. Object Storage events are not a streaming log.

**Key Concept:** [Using Streaming with Apache Kafka](https://docs.oracle.com/en-us/iaas/Content/Streaming/Tasks/kafkacompatibility.htm)
</details>

---

### Question 29
**Scenario:** A team has a working Node.js application written with MongoDB drivers. It wants the data in Autonomous Database with minimal code change.

A. Rewrite every data access call in PL/SQL
B. Export the data as CSV and load it into relational tables
C. Use the Oracle Database API for MongoDB with the existing drivers
D. Run MongoDB on a compute instance in the same subnet as the database

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Autonomous Database offers the Oracle Database API for MongoDB, which lets MongoDB drivers and tools work against JSON collections stored in the database, usually with only a connection string change. Rewriting in PL/SQL or flattening to CSV is far from minimal change, and running MongoDB separately keeps the data out of Autonomous Database.

**Key Concept:** [Using Oracle Database API for MongoDB](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/mongo-using-oracle-database-api-mongodb.html)
</details>

---

### Question 30
**Scenario:** A function returns errors in production, but the developer cannot see any of the output it writes to stdout and stderr.

A. Increase the function's memory so its output is buffered and flushed to the console
B. SSH into the function's container to read the output
C. Add a Notifications topic to the function's application
D. Enable function invocation logs in the Logging service for the application

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Function output is captured once invocation logs are enabled for the application, and they can then be searched in the Logging service. Memory size does not route output anywhere. Function containers are managed and not reachable by SSH, and a Notifications topic delivers messages that something else publishes.

**Key Concept:** [Storing and Viewing Function Logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsexportingfunctionlogfiles.htm)
</details>

---

## Where to go deeper

- [OCI Developer Associate cert page](../../exams/oracle/oci-developer-associate/) - notes, practice plan, strategy
- [OCI Foundations practice questions](./oracle-oci-foundations.md) - the platform fundamentals
- [OCI Architect Associate practice questions](./oracle-oci-architect-associate.md) - the infrastructure counterpart
- [Serverless explained](../../learn/concepts/serverless-explained.md) - functions in plain English
- **[📖 Oracle University certification](https://education.oracle.com/oracle-certification-path/pFamily_647)** - official exam pages
