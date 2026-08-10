---
last-updated: 2026-08-09
difficulty: advanced
---

# Oracle Cloud Infrastructure Architect Professional (1Z0-997) - Practice Questions

15 questions for OCI Architect Professional prep, weighted toward advanced architecture design (20%) and networking and connectivity (20%), then HA/DR, security and compliance, performance, and database architecture.

> **Cert page:** [exams/oracle/oci-architect-professional/](../../exams/oracle/oci-architect-professional/)

---

### Question 1
**Scenario:** A hub-and-spoke topology must let spoke VCNs reach on-premises and each other, with inspection.

A. A full peering mesh
B. A DRG with transit routing, spokes attached, and route tables directing traffic through a firewall appliance in the hub
C. Internet gateways in each spoke
D. Separate DRGs per spoke

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** DRG route tables and route distributions are what express the policy: which attachment learns which routes and where traffic is steered. Sending spoke-to-spoke traffic through the hub firewall requires explicit routes, because otherwise transit routing delivers it directly.
</details>

---

### Question 2
**Scenario:** FastConnect must be resilient to a single circuit or device failure.

A. One virtual circuit
B. Redundant virtual circuits over diverse physical connections and locations, with BGP for failover, optionally with an IPSec VPN as backup
C. A single high-bandwidth circuit
D. A VPN only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Bandwidth is not redundancy: a single circuit is a single failure domain regardless of size. Diversity must extend to the physical path and the terminating devices, and BGP attributes control which path is preferred in each direction.
</details>

---

### Question 3
**Scenario:** An application must fail over to a second region with an RTO of 15 minutes.

A. Backups restored manually
B. A warm standby: data replicated continuously, infrastructure defined as code and pre-provisioned at reduced scale, with automated scale-up and DNS or traffic steering on failover
C. Cold rebuild from scratch
D. Multi-AD only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A 15-minute RTO does not permit provisioning from nothing, so the standby must already exist in some form. Traffic Management steering policies with health checks handle the redirection, and Full Stack Disaster Recovery can orchestrate the sequence.
</details>

---

### Question 4
**Scenario:** A database must support both high availability and disaster recovery.

A. Data Guard alone in one AD
B. RAC or Data Guard within the region for HA, plus Data Guard or Autonomous Data Guard to a second region for DR
C. Backups only
D. A read replica

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** HA and DR are different failure domains and need different mechanisms: local redundancy handles instance and AD failure, cross-region replication handles regional loss. Treating one as covering the other is the design error the exam probes.
</details>

---

### Question 5
**Scenario:** A large on-premises Oracle estate must move to OCI with minimal change.

A. Rewrite for a different database
B. Assess per workload: lift and shift to compute or Exadata, migrate with Zero Downtime Migration or Data Pump, and use Data Guard for the cutover where downtime must be short
C. Export to CSV
D. Rebuild everything cloud native

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Oracle-to-Oracle migration is the case where lift and shift is genuinely low risk, and Exadata Cloud Service preserves the performance characteristics some workloads depend on. Standby-based cutover is what compresses the downtime window.
</details>

---

### Question 6
**Scenario:** Traffic between OCI and another cloud provider must be private and high bandwidth.

A. Site-to-site VPN over the internet only
B. FastConnect to a colocation provider with a cross-connect to the other cloud's direct connectivity service, or Oracle Interconnect for Azure where available
C. Public endpoints
D. A NAT gateway

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Multicloud designs need dedicated connectivity to be predictable. The Oracle and Microsoft interconnect gives low-latency private connectivity in paired regions without a partner circuit, which is why it appears in Oracle multicloud reference architectures.
</details>

---

### Question 7
**Scenario:** Compliance requires that data never leaves a jurisdiction, including for support.

A. Encrypt everything
B. Select in-region services, restrict cross-region replication and backup targets, and evaluate whether a dedicated or sovereign region is required
C. A public region with tags
D. Documentation

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Residency leaks through the paths you did not choose deliberately: backups, DR replicas, and telemetry. Where the requirement extends to operator access, Dedicated Region or a sovereign region is the answer rather than configuration within a commercial region.
</details>

---

### Question 8
**Scenario:** An architecture must minimize cost without sacrificing the availability target.

A. Reduce redundancy
B. Right-size shapes, use flexible shapes and preemptible instances for tolerant workloads, apply lifecycle tiering to storage, and commit to universal credits where usage is predictable
C. Move everything to bare metal
D. Turn off monitoring

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cost work should attack waste rather than resilience. Preemptible instances suit stateless batch workloads specifically, and lifecycle policies address storage, which is usually a larger share of a mature estate's bill than people expect.
</details>

---

### Question 9
**Scenario:** Performance must be diagnosed for a distributed application.

A. CPU graphs only
B. Application Performance Monitoring with tracing, plus Logging Analytics and Monitoring metrics correlated together
C. Guess
D. Increase shape sizes

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Metrics tell you something is slow, traces tell you where, and logs tell you why. APM's synthetic monitoring adds the outside-in view, which distinguishes "our service is slow" from "the path to our service is slow."
</details>

---

### Question 10
**Scenario:** Governance must prevent developers creating internet-exposed resources.

A. Training
B. Security Zones with policies denying public access, plus IAM policies restricting who may create gateways, and Cloud Guard detecting anything that slips through
C. Weekly review
D. A naming convention

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Preventive and detective controls together: Security Zones refuse the operation, IAM limits who can even attempt it, and Cloud Guard covers compartments outside a security zone. Any one alone leaves a gap.
</details>

---

### Question 11
**Scenario:** A multi-tenant SaaS application must isolate customers on OCI.

A. One compartment for everything
B. Compartment-per-tenant or tenancy-per-tenant depending on the isolation requirement, with IAM policies and network segmentation matching
C. Application-level filtering only
D. Separate regions per tenant

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The choice follows the isolation requirement and the operational cost you can carry: compartments give strong policy and cost separation within one tenancy, while separate tenancies give the hardest boundary at the price of managing many tenancies.
</details>

---

### Question 12
**Scenario:** Autonomous Database must be reachable only from a specific VCN.

A. A public endpoint with an ACL
B. A private endpoint in the VCN, with public access disabled
C. A NAT gateway
D. A bastion only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A private endpoint gives the database an address inside your subnet and removes the public listener entirely. An access control list on a public endpoint narrows exposure but the endpoint still exists on the internet.
</details>

---

### Question 13
**Scenario:** Infrastructure must be reproducible across regions and environments.

A. Console clicks with screenshots
B. Terraform (Resource Manager stacks), parameterized per environment and stored in version control
C. Manual runbooks
D. Custom images only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Reproducible infrastructure is the precondition for any credible DR plan, because the standby region must be buildable. Resource Manager runs Terraform as a managed service with state handling and drift detection.
</details>

---

### Question 14
**Scenario:** A workload has unpredictable bursts and a stable baseline.

A. Provision for the peak permanently
B. Provision the baseline with committed capacity and handle bursts with autoscaling, using preemptible capacity where the workload tolerates interruption
C. Provision the average
D. Manual scaling

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Splitting baseline from burst lets you commit to the predictable part for a discount while paying on demand only for the peaks. Provisioning for the average means failing during every burst, which is why the naive middle option is the worst of the three.
</details>

---

### Question 15
**Scenario:** An architecture review must record why a design was chosen.

A. A diagram
B. An architecture decision record with context, options, decision, and consequences, kept with the code
C. A meeting
D. Nothing

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A diagram captures the result, not the constraints that produced it, so the next team cannot tell which trade-offs still apply. Recording the rejected options is what stops the same debate recurring after the original participants have moved on.
</details>

---

## Where to go deeper

- [OCI Architect Professional cert page](../../exams/oracle/oci-architect-professional/) - notes, practice plan, strategy
- [OCI Architect Associate practice questions](./oracle-oci-architect-associate.md) - the prerequisite level
- [OCI Operations Associate practice questions](./oracle-oci-operations-associate.md) - the operations counterpart
- [SRE and reliability topic index](../../topics/sre-and-reliability.md) - DR and availability in practice
- **[📖 Oracle University certification](https://education.oracle.com/oracle-certification-path/pFamily_647)** - official exam pages
