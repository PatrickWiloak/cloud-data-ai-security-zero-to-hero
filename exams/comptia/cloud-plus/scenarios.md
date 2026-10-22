---
last-updated: 2026-10-22
applies-to: CompTIA Cloud+ CV0-004 exam objectives v2.0, checked 2026-10-22
difficulty: intermediate
---

# CompTIA Cloud+ (CV0-004) - High-Yield Scenarios and Patterns

Scenarios are grouped by the six CV0-004 domains. Each shows the pattern behind the right answer and the distractors the exam likes to offer. The notes for each domain are linked in the [README](README.md).

## Domain 1: Cloud Architecture (23%) Scenarios

### Designing for High Availability
**Scenario**: An e-commerce company requires 99.99% uptime for their application across multiple geographic regions.

**Solution Pattern**:
- **Compute**: Auto-scaling groups in multiple availability zones per region
- **Database**: Multi-region replication with automatic failover
- **Load balancing**: Global load balancer with health checks and failover routing
- **DNS**: Latency-based or geolocation routing
- **CDN**: Content delivery network for static assets

**Common Distractors**:
- Single region with multi-AZ only (wrong - doesn't meet 99.99% for regional failure)
- Manual failover (wrong - increases RTO significantly)
- No health checks (wrong - cannot detect failures for automatic failover)

### Selecting Service Models
**Scenario**: A startup with limited DevOps staff needs to deploy a web application quickly without managing servers, but needs full control over their database schema.

**Solution Pattern**:
- **Application**: PaaS for the web application (no server management)
- **Database**: DBaaS for managed database with schema control
- **Storage**: Object storage (SaaS-like) for static assets
- **Rationale**: Minimizes operational overhead while maintaining application control

**Common Distractors**:
- IaaS for everything (wrong - too much management overhead for small team)
- SaaS only (wrong - no custom application development)
- Self-managed database on IaaS (wrong - unnecessary operational burden)

### Connecting Many Networks
**Scenario**: A company has twelve VPCs (production, development, shared services and several business units) and a site-to-site VPN to its data centre. Teams keep adding peering links, routes are inconsistent, and some VPCs cannot reach shared services through another VPC.

**Solution Pattern**:
- **Hub**: Attach every VPC and the VPN (or dedicated connection) to a transit gateway
- **Routing**: Use transit gateway route tables to control which spokes can talk to each other, for example keeping development away from production
- **Addressing**: Confirm no two VPCs use overlapping CIDR blocks before attaching them
- **Rationale**: Peering is one-to-one and not transitive, so a full mesh of twelve VPCs needs 66 links; a hub needs twelve attachments

**Common Distractors**:
- More peering links (wrong - does not scale and is never transitive)
- A single shared VPC for everyone (wrong - removes isolation between business units)
- Static routes on every instance (wrong - unmanageable and not a cloud-native control)

### Choosing Storage for a Workload
**Scenario**: A media company stores 400 TB of finished video. Files are read heavily for 30 days after release, occasionally for a year, and must be kept for ten years for licensing audits. Editors also need a shared drive that several render servers mount at once.

**Solution Pattern**:
- **Finished video**: Object storage with a lifecycle policy: hot for 30 days, cold after that, archive after one year
- **Shared editing space**: File storage (NFS or SMB) that many servers can mount
- **Render server scratch disks**: SSD block storage for high IOPS
- **Rationale**: Each access pattern gets the cheapest storage type and tier that still meets it

**Common Distractors**:
- Everything on SSD block storage (wrong - very expensive at 400 TB and cannot be shared easily)
- Archive tier from day one (wrong - retrieval takes hours and costs the most when reads are frequent)
- Object storage as the shared editing drive (wrong - it is not a mountable file system for in-place edits)

### Cost Optimization
**Scenario**: A company's cloud bill has grown 40% quarter-over-quarter. Management wants to reduce costs without impacting performance.

**Solution Pattern**:
- **Right-sizing**: Analyze utilization and downsize over-provisioned resources
- **Reserved capacity**: Commit to reserved instances for steady-state workloads
- **Auto-scaling**: Scale down during off-peak hours
- **Storage tiering**: Move infrequently accessed data to cheaper storage classes
- **Unused resources**: Identify and remove orphaned resources (unattached volumes, unused IPs)
- **Tagging**: Implement cost allocation tags for accountability

**Common Distractors**:
- Only reduce instance sizes (wrong - may impact performance)
- Move everything to reserved (wrong - variable workloads need on-demand)
- Disable monitoring to save costs (wrong - creates operational risk)

## Domain 2: Deployment (19%) Scenarios

### Choosing the Right Deployment Model
**Scenario**: A financial services company needs to process sensitive customer data while also running a public-facing web application that experiences variable traffic.

**Solution Pattern**:
- **Sensitive workloads**: Private cloud for compliance and data control
- **Web application**: Public cloud for scalability and cost efficiency
- **Integration**: Hybrid cloud with secure connectivity (VPN or dedicated connection)
- **Data sovereignty**: Keep regulated data in private cloud, replicate non-sensitive data

**Common Distractors**:
- All public cloud (wrong - compliance requirements for sensitive data)
- All private cloud (wrong - cost-ineffective for variable web traffic)
- Multi-cloud without integration (wrong - needs orchestration between environments)

### Migration Strategy Selection
**Scenario**: A company has a legacy monolithic application running on aging hardware. They need to move to the cloud quickly while planning a future modernization effort.

**Solution Pattern**:
- **Phase 1**: Rehost (lift-and-shift) to IaaS for immediate hardware refresh
- **Phase 2**: Replatform - optimize for cloud (managed database, auto-scaling)
- **Phase 3**: Refactor - break into microservices for cloud-native benefits
- **Rationale**: Phased approach reduces risk and delivers immediate value

**Common Distractors**:
- Immediate full refactor (wrong - too risky and time-consuming for urgent migration)
- Repurchase SaaS (wrong - custom application may not have SaaS equivalent)
- Retain on-premises (wrong - hardware is aging, doesn't meet requirement)

### Infrastructure as Code Implementation
**Scenario**: A team manages cloud infrastructure across three environments (dev, staging, production) and needs consistent, repeatable deployments.

**Solution Pattern**:
- **Tool**: Terraform for multi-environment IaC
- **State management**: Remote state backend with locking
- **Variables**: Environment-specific variable files (dev.tfvars, staging.tfvars, prod.tfvars)
- **Modules**: Reusable modules for common infrastructure patterns
- **Version control**: Git repository with branch-per-environment or workspace strategy
- **CI/CD**: Automated plan/apply pipeline with manual approval for production

**Common Distractors**:
- Manual console deployments (wrong - not repeatable or auditable)
- Single template for all environments (wrong - environments need different configurations)
- No state management (wrong - leads to configuration drift)

### Choosing a Deployment Strategy
**Scenario**: An online retailer is releasing a new checkout service. A bad release last quarter affected every customer for an hour. The business wants to limit how many customers a faulty release can reach and to catch problems using real traffic.

**Solution Pattern**:
- **Strategy**: Canary release, starting with about 5 percent of traffic
- **Gates**: Automated checks on error rate and latency before each increase
- **Rollback**: Route canary traffic back to the current version if metrics degrade
- **Rationale**: Canary limits blast radius and validates with real users

**Common Distractors**:
- In-place deployment (wrong - causes downtime and exposes everyone at once)
- Blue-green (partly right - zero downtime and instant rollback, but switches all users at once rather than limiting exposure)
- Rolling update with no health gates (wrong - mixed versions reach many users before a problem is noticed)

## Domain 3: Operations (17%) Scenarios

### Monitoring and Alerting Strategy
**Scenario**: A cloud environment with 200+ resources needs comprehensive monitoring with minimal alert fatigue.

**Solution Pattern**:
- **Metrics**: Collect infrastructure and application metrics
- **Thresholds**: Set appropriate warning and critical thresholds
- **Alert routing**: Severity-based escalation (P1 to on-call, P3 to ticket)
- **Dashboards**: Service-level dashboards for quick assessment
- **Log correlation**: Centralized logging with correlation IDs
- **Runbooks**: Automated and documented response procedures

**Common Distractors**:
- Alert on every metric (wrong - creates alert fatigue)
- No severity levels (wrong - all alerts treated equally wastes time)
- Email-only notifications (wrong - critical alerts need immediate paging)

### Change Management Process
**Scenario**: A production deployment caused an outage due to an untested configuration change. The company needs to prevent future incidents.

**Solution Pattern**:
- **RFC process**: Formal change request with impact analysis
- **Change Advisory Board**: Review and approve significant changes
- **Testing**: Mandatory testing in staging environment
- **Rollback plan**: Documented rollback procedure for every change
- **Maintenance windows**: Scheduled deployment windows for changes
- **Post-implementation review**: Verify change success and document lessons learned

**Common Distractors**:
- Freeze all changes (wrong - prevents necessary updates and improvements)
- Skip testing for urgent changes (wrong - creates risk of repeat incidents)
- No documentation (wrong - prevents learning from incidents)

### Backup and Recovery After Ransomware
**Scenario**: Ransomware encrypted a file server's data volume overnight. Nightly backups run at 01:00, and the attacker also tried to delete snapshots. The RPO is 24 hours and the RTO is 8 hours. The security team wants to keep the encrypted volume for investigation.

**Solution Pattern**:
- **Recovery type**: Parallel recovery to a new volume, so the infected volume is preserved as evidence
- **Recovery option**: Bulk restore of the whole volume from the last backup taken before the infection
- **Backup location**: Restore from an off-site copy in a separate account with immutability (object lock), which the attacker could not delete
- **Verification**: Check integrity (file counts, checksums, sample files open) before reconnecting users
- **Prevention**: Restrict who can delete backups, keep the 3-2-1 rule with one immutable copy, test restores on a schedule

**Common Distractors**:
- In-place restore over the encrypted volume (wrong - destroys evidence and leaves no fallback)
- Restore the most recent backup without checking its date (wrong - it may already contain encrypted files)
- Rely on replication to a second region (wrong - replication copies the encrypted data too)

### Restoring a Single Deleted Item
**Scenario**: A user deleted one project folder from a shared file server yesterday afternoon. Everyone else's work since then must not be lost.

**Solution Pattern**:
- **Recovery option**: Granular restore of just that folder
- **Recovery type**: Parallel, to an alternate path, then copy the folder back once the owner confirms it
- **Backup type in use**: Any; with incrementals, the backup software rebuilds the folder from the full plus the needed increments

**Common Distractors**:
- Bulk in-place restore of the whole volume (wrong - overwrites a day of other users' changes)
- Rebuild the server from a golden image (wrong - images do not contain user data)

### Scaling for Known and Unknown Peaks
**Scenario**: A ticketing site gets a predictable surge every Friday at 10:00 when sales open, and occasional unpredictable spikes when an artist announces a tour. Users report being logged out when the site scales in.

**Solution Pattern**:
- **Scheduled scaling**: Add capacity at 09:45 on Fridays
- **Load-triggered scaling**: Target CPU or request-count tracking for unexpected spikes
- **Horizontal scaling**: More instances behind a load balancer, not bigger ones
- **State**: Move sessions out of instance memory into a shared cache or database so scale-in does not log users out

**Common Distractors**:
- Vertical scaling only (wrong - has a ceiling and needs restarts)
- Manual scaling by the on-call engineer (wrong - too slow for sudden spikes)
- Disable scale-in to avoid logouts (wrong - treats the symptom and wastes money)

## Domain 4: Security (19%) Scenarios

### Implementing Zero Trust Access
**Scenario**: A company with remote workers needs secure access to cloud resources. They have experienced credential theft attacks.

**Solution Pattern**:
- **MFA**: Require multi-factor authentication for all users
- **SSO**: Federated identity with corporate IdP
- **RBAC**: Role-based access with least privilege
- **Network**: Micro-segmentation, no implicit trust based on network location
- **Monitoring**: Continuous authentication and session monitoring
- **Device**: Device posture validation before granting access

**Common Distractors**:
- VPN-only access (wrong - VPN doesn't prevent lateral movement after breach)
- Password-only authentication (wrong - vulnerable to credential theft)
- Network-perimeter security only (wrong - zero trust requires identity verification)

### Data Encryption Strategy
**Scenario**: A healthcare organization must encrypt all patient data to comply with HIPAA, both at rest and in transit.

**Solution Pattern**:
- **At rest**: AES-256 encryption for databases and storage volumes
- **In transit**: TLS 1.2+ for all API calls and data transfers
- **Key management**: Customer-managed keys with HSM for HIPAA compliance
- **Key rotation**: Automatic key rotation every 90 days
- **Access logging**: Audit trail for all key usage and data access
- **Backup encryption**: Encrypted snapshots and backup copies

**Common Distractors**:
- Provider-managed keys only (wrong - HIPAA may require customer control)
- Encryption in transit only (wrong - data at rest must also be encrypted)
- No key rotation (wrong - compliance requires regular key rotation)

### Compliance Framework Selection
**Scenario**: A company processes credit card payments and stores customer data for European and US customers.

**Solution Pattern**:
- **PCI-DSS**: Required for credit card payment processing
- **GDPR**: Required for EU customer personal data
- **SOC 2**: Demonstrates security controls to business partners
- **Implementation**: Segmented network for cardholder data, data residency controls for EU data
- **Audit**: Regular compliance assessments and penetration testing

**Common Distractors**:
- HIPAA (wrong - healthcare, not payment processing)
- FedRAMP (wrong - US government, not commercial retail)
- ISO 27001 only (wrong - doesn't specifically address payment card requirements)

## Domain 5: DevOps Fundamentals (10%) Scenarios

### Container Orchestration
**Scenario**: A development team runs 50+ microservices and needs automated scaling, self-healing, and zero-downtime deployments.

**Solution Pattern**:
- **Platform**: Kubernetes for container orchestration
- **Deployments**: Rolling updates for zero-downtime
- **Scaling**: Horizontal Pod Autoscaler based on CPU/memory
- **Health**: Liveness and readiness probes for self-healing
- **Networking**: Service mesh for inter-service communication
- **Registry**: Private container registry for image management

**Common Distractors**:
- Docker Compose (wrong - not designed for production-scale orchestration)
- Manual container management (wrong - doesn't scale for 50+ services)
- Virtual machines per service (wrong - too much overhead)

### Promoting Artifacts Through a Pipeline
**Scenario**: A team's application works in staging but fails in production. The pipeline runs `docker build` separately for each environment and uses the `latest` tag of a public base image.

**Solution Pattern**:
- **Build once**: Build the image a single time per commit and tag it with a version or commit hash
- **Promote**: Deploy the same image digest to staging and then to production
- **Base image**: Pin a specific base image version and pull it through a private registry with vulnerability scanning
- **Pipeline security**: Fail the build on critical CVEs or exposed secrets

**Common Distractors**:
- Rebuild in production with a hotfix flag (wrong - still ships an untested artifact)
- Switch from containers to VMs (wrong - the problem is the pipeline, not the packaging)

### Choosing an Integration Style
**Scenario**: When an order is placed, billing, shipping, analytics and a loyalty service must all react. New services will be added next year. Separately, the customer dashboard must show live delivery updates without the browser polling.

**Solution Pattern**:
- **Order processing**: Event-driven architecture. The order service publishes an "order placed" event to a topic; each consumer subscribes (fan-out). New consumers subscribe without changing the producer
- **Live dashboard**: WebSockets for server-to-browser push
- **Public partner API**: REST over HTTPS with JSON

**Common Distractors**:
- Order service calls each downstream service directly with RPC (wrong - tight coupling; a slow consumer blocks orders and every new consumer needs a code change)
- SOAP for the browser dashboard (wrong - heavy and still request-response)
- GraphQL for the live updates (partly wrong - GraphQL shapes queries; push needs subscriptions over WebSockets)

### Picking DevOps Tools
**Scenario**: A company wants to define its AWS and Azure networks in code, configure 300 existing Linux servers without installing agents, run pipelines on pull requests in GitHub, and search logs from all servers in one place.

**Solution Pattern**:
- **Networks in code across clouds**: Terraform
- **Configure existing servers, agentless**: Ansible
- **Pipelines on pull requests in GitHub**: GitHub Actions (Jenkins if a self-hosted server is required)
- **Central log search**: ELK stack, with Grafana for metric dashboards

**Common Distractors**:
- Ansible to create both clouds' networks (partly wrong - possible, but Terraform is the purpose-built IaC tool with state and plan)
- Kubernetes to configure servers (wrong - it orchestrates containers, it does not configure hosts)
- Grafana as the log store (wrong - Grafana visualizes data held elsewhere)

## Domain 6: Troubleshooting (12%) Scenarios

### Network Connectivity Failure
**Scenario**: Users cannot access a web application hosted in the cloud. The application was working earlier today.

**Troubleshooting Steps**:
1. **Verify the issue**: Confirm from multiple locations and users
2. **Check DNS**: Verify DNS resolution returns correct IP addresses
3. **Check health**: Verify load balancer health checks and backend instances
4. **Check security**: Review security group and firewall rule changes
5. **Check routing**: Verify route tables and network ACLs
6. **Check application**: Review application logs for errors
7. **Recent changes**: Review change log for recent modifications

**Root Cause Patterns**:
- Security group rule accidentally removed
- DNS record change propagation
- SSL certificate expiration
- Application deployment failure
- Resource limits exceeded

### Performance Degradation
**Scenario**: An application is running slowly. Response times have increased from 200ms to 2000ms over the past hour.

**Troubleshooting Steps**:
1. **Identify scope**: Which services and endpoints are affected
2. **Check metrics**: CPU, memory, disk I/O, network throughput
3. **Check database**: Query performance, connection count, locks
4. **Check dependencies**: External API response times
5. **Check capacity**: Auto-scaling status, resource limits
6. **Check traffic**: Unexpected traffic spike or pattern change
7. **Correlate changes**: Recent deployments or configuration changes

**Root Cause Patterns**:
- Database query performance degradation
- Memory leak in application
- Disk I/O saturation
- Network bandwidth throttling
- Insufficient auto-scaling configuration

### Security Incident Response
**Scenario**: The security team detects unusual API calls from an IAM user at 3 AM, including attempts to access resources outside their normal scope.

**Response Steps**:
1. **Contain**: Temporarily disable compromised credentials
2. **Assess**: Review audit logs for scope of unauthorized access
3. **Investigate**: Determine how credentials were compromised
4. **Remediate**: Rotate credentials, patch vulnerability
5. **Recover**: Restore any affected resources
6. **Improve**: Update security controls and monitoring

**Key Actions**:
- Review API call logs and access patterns
- Check for newly created resources or users
- Verify data integrity and check for exfiltration
- Enable additional MFA requirements
- Update incident response procedures

### Automation Failure
**Scenario**: A Terraform apply fails with state lock errors and some resources were partially created.

**Troubleshooting Steps**:
1. **Check state**: Verify state file integrity and lock status
2. **Force unlock**: If previous apply crashed, force-unlock state (carefully)
3. **Import resources**: Import partially created resources into state
4. **Plan**: Run terraform plan to identify drift
5. **Fix**: Address root cause of failure (permissions, quotas, dependencies)
6. **Apply**: Re-run terraform apply to reach desired state

**Prevention**:
- Use remote state with locking (S3 + DynamoDB, Terraform Cloud)
- Implement CI/CD pipeline with state management
- Set appropriate timeouts for resource creation
- Use depends_on for explicit dependencies

---

### VLAN and DHCP Failure After a Host Move
**Scenario**: In a private cloud, a hypervisor host was moved to a new switch port. VMs on VLAN 10 still work, but VMs on VLAN 20 now show 169.254.x.x addresses and cannot reach anything.

**Troubleshooting Steps**:
1. **Identify**: The 169.254.x.x addresses mean the VMs got no answer from DHCP
2. **Theory**: DHCP is fine for VLAN 10, so the problem is VLAN 20's path, not the DHCP server
3. **Test**: Check the new switch port. It is configured as an access port on VLAN 10, or as a trunk that does not allow VLAN 20
4. **Fix**: Configure the port as a trunk that allows VLANs 10 and 20 with the correct tags and matching native VLAN
5. **Verify**: Renew leases on the VMs and confirm gateway reachability
6. **Document**: Record the port configuration in the change record

**Root Cause Patterns**:
- Access port where a trunk is needed
- VLAN missing from the trunk's allowed list
- Wrong VLAN tag on the VM port group
- DHCP relay missing for a new VLAN

### Deployment Blocked by Limits
**Scenario**: During a product launch, auto scaling stops adding instances. The deployment pipeline is also failing intermittently with HTTP 429 errors when it calls the provider API.

**Troubleshooting Steps**:
1. **Read the errors**: Scaling activity shows a vCPU "LimitExceeded" message; the pipeline shows "Rate exceeded" (HTTP 429)
2. **Service quota**: Request a vCPU quota increase for the region, and pre-raise quotas before future launches and in the DR region
3. **API throttling**: Add exponential backoff with jitter to the pipeline's API calls and reduce polling frequency
4. **Verify**: Scaling resumes and pipeline runs complete

**Common Distractors**:
- Change the scaling policy thresholds (wrong - the policy is firing; the quota blocks it)
- Give the pipeline administrator permissions (wrong - 429 is throttling, not authorization)

## Scenario Analysis Framework

When approaching exam scenarios, follow this pattern:

1. **Identify the requirement** - What is the business or technical need?
2. **Identify constraints** - Budget, compliance, timeline, team skill level
3. **Match to solution** - Which cloud concepts and tools best fit?
4. **Evaluate trade-offs** - Cost vs performance vs complexity
5. **Choose the best answer** - Most appropriate, not just correct

### Key Decision Factors
- **Cost** - Is cost optimization a primary concern?
- **Compliance** - Are there regulatory requirements?
- **Availability** - What is the required uptime?
- **Performance** - Are there latency or throughput requirements?
- **Complexity** - What is the team's skill level?
- **Vendor** - Is vendor neutrality important?
