---
last-updated: 2026-10-22
applies-to: CompTIA Cloud+ CV0-004 exam objectives v2.0, checked 2026-10-22
difficulty: intermediate
---

# Domain 6: Troubleshooting (12%)

This note covers objectives 6.1 to 6.3: troubleshooting deployment issues, network issues and security issues. It opens with the troubleshooting methodology, which CompTIA uses across all its exams and which underpins every scenario in this domain.

**[📖 CompTIA Cloud+ CV0-004 Exam Objectives v2.0 (PDF)](https://comptiacdn.azureedge.net/webcontent/docs/default-source/exam-objectives/comptia-cloud-cv0-004-exam-objectives-%282-0%29.pdf)** - the official topic list this note follows.

Troubleshooting questions are scenarios with symptoms. The skill being tested is reading the symptom precisely and mapping it to the most likely cause. A timeout, a "connection refused" and an HTTP 403 point to three different layers. Performance-based questions often show a route table, a security group, a log excerpt or command output and ask you to find the faulty line.

## The troubleshooting methodology

1. **Identify the problem.** Gather information from users, alerts and logs. Define the symptoms and scope: one user or all, one region or all, since when. Ask what changed recently, because most incidents follow a change.
2. **Establish a theory of probable cause.** Start with the simple and common (question the obvious). Check the provider's status page for regional incidents. Consider recent deployments, configuration changes and expiring certificates.
3. **Test the theory to determine the cause.** Use diagnostic tools and logs to confirm or eliminate it. If the theory is wrong, form a new one or escalate.
4. **Establish a plan of action** to resolve the problem, including its risk, its effect on other systems and a rollback. Follow change management for production.
5. **Implement the solution** or escalate if it is beyond your authority or skill.
6. **Verify full system functionality** and, where appropriate, implement preventive measures.
7. **Document findings, actions and outcomes** so the next person (or you, at 03:00 next month) can fix it faster.

**Exam trap:** The exam likes to ask "what should the administrator do next?" If the cause is not yet confirmed, the answer is to test the theory, not to implement a fix. If the fix is in, the next step is verification, then documentation.

## 6.1 Troubleshoot deployment issues

Deployment issues are failures when creating, updating or scaling resources, or when a new release goes live.

### Incompatibility

The new component does not work with something it depends on: an application built for a newer runtime than the platform offers, a container image built for ARM running on x86 nodes, a driver that does not support the hypervisor, an API client using a version the service no longer accepts, or a VM image format the target cloud cannot import. Check version matrices and release notes, and test in an environment that matches production.

### Misconfigurations

- **Resource allocation** - not enough CPU, memory, disk or IP addresses assigned, or a Kubernetes pod requesting more than any node can provide (the pod stays `Pending`). Container limits set too low cause OOM kills (`OOMKilled`, exit code 137).
- **Permission issues** - the deployment identity lacks rights to create a resource, read a secret or pass a role to a service. Look for "AccessDenied", "Forbidden", "AuthorizationFailed" or HTTP 403 in the deployment logs. Fix by granting the specific missing permission, not by making the pipeline an administrator.
- **Oversubscription** - more virtual resources are promised than physical resources exist, such as too many vCPUs per physical core on a private cloud host or too many VMs on a datastore. Symptoms include high CPU ready or steal time and storage latency even though each VM looks lightly used.
- **Sizing issues** - the instance type or volume is too small (performance problems, failed health checks under load) or too large (wasted money). Also includes choosing a type that does not support a needed feature, such as a GPU or enhanced networking.

### Outdated component definitions

IaC templates, modules, container base images, Helm charts or golden images that reference old versions, deprecated instance types or retired images. The deployment fails because the referenced item no longer exists, or succeeds but deploys something vulnerable. Fix by updating definitions regularly, pinning and then deliberately bumping versions, and testing the bump.

### Deprecation of functionality

Providers retire API versions, runtimes (an old Python or Node.js version for functions), instance families and features after published notice. After the date, new deployments fail or existing ones stop being supported. Symptoms include errors such as "runtime is no longer supported for creation" or an API returning a deprecation error. Track provider deprecation notices and plan upgrades early.

### Outages: full and partial

- **Full outage** - the service is completely unavailable to everyone. Check provider status pages, DNS, certificates, load balancer health and the most recent change. Fail over to another region if the design allows.
- **Partial outage** - some users, some features or some regions are affected, or the service is degraded but up. Narrow the scope: which AZ, which instance group, which version (a bad canary), which client type. Partial outages are harder to spot and are where good monitoring and tracing pay off.

### Resource limits

- **API throttling** - the provider limits how many API calls per second an account or caller may make. Too many calls return HTTP 429 (Too Many Requests) or errors such as "Rate exceeded" or "ThrottlingException". Fix with exponential backoff and jitter on retries, caching, batching calls, and spreading automation over time.
- **Service quotas** - per-account or per-region limits on resources such as the number of vCPUs, VPCs, elastic IPs or load balancers. When reached, creation fails with "LimitExceeded" or "QuotaExceeded". Request an increase in advance, especially before a launch or a DR failover into a region where you normally run little.

**Exam trap:** Auto scaling stops adding instances during a traffic spike and the error mentions a limit. That is a service quota, not a scaling policy bug. Request the quota increase.

### Regional service availability

Not every service, instance type or feature exists in every region, and new services often launch in a few regions first. A template that works in one region fails in another with "not supported in this region". DR plans must check that every service in the primary region is also available in the recovery region.

### Deployment diagnostics

```bash
# Kubernetes: why is a pod not running?
kubectl get pods
kubectl describe pod <pod-name>     # events: scheduling, image pull, OOMKilled
kubectl logs <pod-name> --previous  # logs from the crashed container
kubectl get events --sort-by=.metadata.creationTimestamp

# Terraform: what would change, and did something drift?
terraform validate
terraform plan
```

Common pod states: `ImagePullBackOff` (wrong image name or tag, or registry authentication failed), `CrashLoopBackOff` (the app starts and exits, so read its logs), `Pending` (no node has enough resources, or a volume cannot be attached).

## 6.2 Troubleshoot network issues

### Network service unavailability

- **DHCP** - hands out IP addresses, gateways and DNS servers. When it fails, new machines get no address or a self-assigned APIPA address (169.254.x.x on Windows) and cannot reach anything. In cloud VPCs the provider runs DHCP, so issues are usually a wrong DHCP options set (for example pointing to a DNS server that does not exist). On premises, check the scope, the relay agent between VLANs and whether the server is up.
- **DNS** - turns names into addresses. Symptoms are "could not resolve host" or connections going to an old address. Causes include wrong or missing records, TTL caching after a change, a private hosted zone not associated with the VPC, split-horizon confusion, or a resolver that cannot be reached on port 53 UDP and TCP.
- **NTP** - keeps clocks in sync. Clock drift breaks things that depend on time: Kerberos authentication (fails beyond 5 minutes of skew by default), TLS certificate validation, signed API requests (cloud APIs reject requests whose timestamp is too far off) and log correlation. Symptom: authentication errors that make no sense, or "request expired" or "signature not yet valid".
- **NAT** - lets private instances reach the internet using a shared public address. If a private subnet cannot reach the internet (package installs time out), check that its route table sends 0.0.0.0/0 to a NAT gateway, that the NAT gateway sits in a public subnet with an internet gateway route, and that the NAT gateway is healthy. NAT gateways can also run out of ports under very high connection counts.
- **HTTP status codes** - the response code tells you which side failed.

| Code | Meaning | Usual cause |
|---|---|---|
| 200 | OK | Working |
| 301 / 302 | Redirect | Moved or HTTP to HTTPS redirect; redirect loops are a misconfiguration |
| 400 | Bad request | Malformed request from the client |
| 401 | Unauthorized | Not authenticated: missing or invalid credentials or token |
| 403 | Forbidden | Authenticated but not allowed: IAM, bucket policy or WAF block |
| 404 | Not found | Wrong path, missing object or wrong routing rule |
| 408 | Request timeout | Client too slow to send the request |
| 429 | Too many requests | Rate limiting or API throttling |
| 500 | Internal server error | Application bug or unhandled exception |
| 502 | Bad gateway | Load balancer or proxy got an invalid response from the backend (backend crashed or wrong port) |
| 503 | Service unavailable | No healthy backends, overloaded or in maintenance |
| 504 | Gateway timeout | Backend too slow to answer the load balancer or proxy |

**Exam trap:** 4xx means the client side (including permissions); 5xx means the server side. 401 is "who are you?"; 403 is "I know who you are, and no".

### Latency and bandwidth or throughput

- **Latency** - delay. Causes include geographic distance, too many hops, cross-region or cross-AZ calls in a chatty application, VPN over a congested internet path, and DNS lookups. Fix by moving compute closer to users or data, using a CDN, keeping chatty tiers in one AZ, or using a dedicated connection.
- **Bandwidth or throughput issues** - not enough capacity. Causes include an instance type with low network bandwidth, a saturated VPN tunnel (one IPsec tunnel often tops out around 1.25 Gbps on major providers), a NAT gateway or firewall bottleneck, and MTU mismatches that cause fragmentation (VPN tunnels need a smaller MTU because of encapsulation overhead).

### Network device misconfiguration

Wrong settings on routers, switches, firewalls, load balancers or virtual appliances: wrong interface IP or mask, wrong default gateway, a firewall rule in the wrong order, a load balancer health check on the wrong port or path, or a security group that does not allow the health checker's traffic. Compare the running configuration against the intended one, and check the device's own logs.

### Protocol incompatibility and protocol deprecations

- **Protocol incompatibility** - two ends cannot agree: IKEv1 on one VPN peer and IKEv2 only on the other, mismatched encryption or Diffie-Hellman groups in VPN phase 1 or 2, HTTP/2 or gRPC through a proxy that only speaks HTTP/1.1, IPv6-only clients reaching an IPv4-only service, or SMB versions that do not overlap.
- **Protocol deprecations** - old protocols turned off for security: SSLv3, TLS 1.0 and 1.1, SMBv1, older SSH key types. A legacy client that only supports a deprecated protocol suddenly fails after a server or provider update. Fix by upgrading the client, not by re-enabling the weak protocol.

### IP addressing issues

- **Scope exhaustion** - the DHCP scope or subnet has no free addresses left. New instances, pods or containers fail to launch with "insufficient free addresses". In cloud subnets remember the provider reserves some addresses (AWS reserves five per subnet), and Kubernetes pod networking can consume one VPC address per pod. Fix by adding a larger or additional subnet or CIDR block, and size subnets with growth in mind.
- **Network overlap** - two networks use the same address range, so they cannot be routed to each other. You cannot peer two VPCs whose CIDR blocks overlap, and a VPN to an on-premises network that also uses 10.0.0.0/16 will not route. Prevention is an IP address management (IPAM) plan before you build. Fixes after the fact include re-addressing or NAT between the overlapping networks.

### Routing issues

- **Missing routes** - the route table has no entry for the destination, so traffic goes nowhere or out the default route. Classic cases: a VPC peering connection was accepted but neither side added a route; a new subnet was associated with the wrong route table; a VPN is up but the on-premises CIDR was never added or propagated.
- **Misconfigured routes** - the route exists but points to the wrong target, such as a private subnet's default route pointing at an internet gateway (instances without public IPs then cannot reach the internet at all) or an overlapping, more specific route sending traffic the wrong way. Remember the longest prefix match wins.

### Switching issues: VLANs

- **Misconfigured VLAN tags** - a VM's port group or a physical switch port is tagged with the wrong VLAN ID, so the host lands in the wrong network. It gets no DHCP address or the wrong one, and cannot reach its gateway.
- **Access versus trunk ports** - an access port carries one untagged VLAN and connects an end device. A trunk port carries many tagged VLANs and connects switches or hypervisor hosts. A hypervisor uplink configured as an access port means only one VLAN reaches the host, so VMs on other VLANs lose connectivity. A trunk with the VLAN missing from its allowed list does the same. Native VLAN mismatches between the two ends of a trunk cause traffic to leak into the wrong VLAN.

**Exam trap:** "VMs on VLAN 20 lost connectivity after a host was moved to a new switch port, but VMs on VLAN 10 still work" points to the new port being an access port on VLAN 10, or a trunk without VLAN 20 allowed.

### Network diagnostics

```bash
# DNS
nslookup app.example.com
dig app.example.com
dig @10.0.0.2 app.example.com     # ask a specific resolver
dig +trace app.example.com        # follow delegation from the root
cat /etc/resolv.conf

# Addressing, routes and reachability
ip addr show
ip route show
ping -c 4 10.0.2.15
traceroute 10.0.2.15
mtr 10.0.2.15                     # continuous traceroute with loss per hop
nc -vz 10.0.2.15 5432             # is the TCP port open?
curl -v https://app.example.com   # TLS handshake and HTTP status

# Throughput and sockets
iperf3 -c 10.0.2.15
ss -tunap

# Time sync
timedatectl
chronyc tracking

# Packet capture
tcpdump -i eth0 -n host 10.0.2.15
```

A good order of work for a "cannot connect" problem: name resolution, then IP addressing, then routing, then filtering (security group, network ACL, host firewall), then the service itself listening on the port. Timeouts usually mean traffic is dropped by a filter or route; "connection refused" usually means you reached the host but nothing is listening.

## 6.3 Troubleshoot security issues

- **Cipher suite deprecations** - providers and libraries remove weak cipher suites (RC4, 3DES, CBC-mode suites, SHA-1 signatures) and old TLS versions. Symptoms: TLS handshake failures, "no shared cipher" or "protocol version" errors from older clients, appliances or Java versions after a load balancer security policy update. Fix by updating the client or its TLS library. Only as a short, documented exception should you select a more permissive policy on the server side.
- **Authorization issues: privilege escalation** - a user or workload gains more rights than intended, for example a role that can attach any policy to itself, pass an admin role to a new function, or edit its own group membership. Signs include IAM policy changes by non-admins and sudden administrator activity from a service account. Fix by removing the escalation path (no `iam:*` or policy-attach rights for non-admins), using permission boundaries, and reviewing audit logs.
- **Authorization issues: unauthorized access** - someone reaches data or resources they should not, often through a misconfiguration such as a public bucket, a share link, an overly broad role or a security group open to the world. Contain first (remove the public access, revoke sessions), then investigate with access logs, then fix the policy and add a guardrail so it cannot recur.
- **Authentication issues: leaked credentials** - access keys or passwords exposed in a public repository, a container image, logs or a phishing attack. Signs include API calls from unfamiliar IPs or regions, new users or keys you did not create, and new instances (often cryptominers). The response order matters: revoke or rotate the credential immediately, review what it did using the audit trail, remove anything the attacker created, then find how it leaked and prevent it (secret scanning, short-lived credentials, MFA).
- **Software vulnerability issues** - a scanner or advisory reports a CVE in an OS package, library or container image. Assess exposure, patch or upgrade, rebuild images, redeploy, then rescan. If no patch exists, mitigate with a WAF rule, network restriction or configuration change.
- **Unauthorized software** - software installed outside policy, such as a cryptominer, a remote access tool, an unapproved database or an unlicensed product. Found by endpoint agents, software inventory and process monitoring. Remove it, find how it was installed, and enforce allow-lists or golden images with no interactive admin access.

### Security troubleshooting checklist

1. Contain first: revoke credentials, isolate the instance (move it to a quarantine security group rather than terminating, so evidence survives), block the source.
2. Preserve evidence: snapshot disks, export logs.
3. Investigate with the audit trail: who, what, when, from where.
4. Eradicate: remove persistence, unauthorized users, keys and software.
5. Recover: rebuild from known good images and backups.
6. Prevent: fix the root cause and add a detective control.

**Exam trap:** For leaked credentials, the first action is always to revoke or rotate them. Investigating first leaves the attacker active while you read logs.

## Performance troubleshooting quick reference

Performance problems appear across all three objectives. Match the bottleneck to the metric.

```bash
top                               # overall CPU, memory, load
vmstat 1                          # 'st' column = CPU steal (noisy neighbour or oversubscription), 'wa' = I/O wait
free -h                           # memory and swap
dmesg | grep -i "out of memory"   # OOM killer events
iostat -x 1                       # per-disk IOPS, throughput, latency, utilization
df -h                             # disk space
```

| Symptom | Likely bottleneck | Fix |
|---|---|---|
| High CPU, high load | Compute | Scale up or out, optimize code |
| High steal time | Oversubscribed host | Move host, dedicated instance |
| High I/O wait, CPU otherwise idle | Storage IOPS or throughput | Faster volume, provisioned IOPS, caching |
| OOM kills, heavy swap | Memory | More memory, fix leaks, set limits correctly |
| Slow only for distant users | Network latency | CDN, closer region |

---

## Key takeaways

1. Follow the methodology in order: identify, theorize, test, plan, implement, verify, document.
2. Deployment failures: check permissions (403, AccessDenied), quotas and throttling (429, LimitExceeded), regional availability and deprecated versions.
3. Partial outages need scoping by AZ, version and client; full outages start with status pages, DNS, certificates and the last change.
4. DHCP failure gives APIPA addresses, NTP skew breaks authentication and signed requests, NAT failure blocks private subnets from the internet.
5. 4xx is client side, 5xx is server side. 401 is unauthenticated, 403 is unauthorized, 502 to 504 are gateway problems.
6. Overlapping CIDRs cannot be peered or routed; plan IP space early. Scope exhaustion stops new instances launching.
7. Access ports carry one untagged VLAN, trunks carry many tagged VLANs.
8. Leaked credentials: revoke first, then investigate. Deprecated ciphers: upgrade the client, do not weaken the server.
