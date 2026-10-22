---
last-updated: 2026-10-22
---

# Section 5: Managing, Monitoring, and Troubleshooting Network Operations (~14%)

Operations questions give you a symptom ("tunnel up but no traffic", "502s after a deploy", "one region cannot reach on-premises") and ask for the fastest correct diagnostic step or fix. You score well here by knowing **which signal lives where**: which logs must be turned on, which metrics exist without setup, and which Network Intelligence Center tool answers which question. The three tasks:

| Task | Scope |
|------|-------|
| 5.1 | Logging and monitoring with Google Cloud Observability for every network component |
| 5.2 | Maintaining and troubleshooting connectivity: draining, VPN, Interconnect, BGP, flow logs, firewall logs, Packet Mirroring |
| 5.3 | Network Intelligence Center: Network Topology, Connectivity Tests, Performance Dashboard, Firewall Insights, Network Analyzer, Flow Analyzer |

A systematic approach that works for most connectivity questions:

1. **Is the path configured?** Routes, firewall rules and policies, NAT, peering and NCC: check with **Connectivity Tests** (configuration analysis) and the effective routes.
2. **Is the control plane healthy?** VPN tunnel status, BGP session state, learned and advertised routes, load balancer backend health.
3. **Is traffic actually flowing and being dropped?** VPC Flow Logs, firewall rule logs, Cloud NAT logs, load balancer logs, metrics.
4. **Do you need packet contents?** Packet Mirroring to a collector.

---

## 5.1 Logging and monitoring with Google Cloud Observability

### What logs exist and how to turn them on

Some network logs are always on (admin activity audit logs); most data-plane logs must be enabled per resource because they cost money.

| Component | Log | How to enable | What it tells you |
|-----------|-----|---------------|-------------------|
| **Cloud VPN** | VPN gateway logs (IKE and tunnel events) | Emitted automatically to Cloud Logging (`resource.type="vpn_gateway"`) | Negotiation failures, proposal mismatches, tunnel up/down |
| **Cloud Router** | Router logs and BGP events | Emitted for BGP session events; audit logs for config | Session flaps, notifications, route changes |
| **VPC Service Controls** | Cloud Audit Logs with VPC-SC metadata | Automatic for denials; dry-run violations also logged | `violationReason`, perimeter name, caller, method |
| **Cloud NGFW / firewall rules** | Firewall Rules Logging per rule; NGFW Enterprise threat logs | `--enable-logging` on a VPC rule; `--enable-logging` on a policy rule; threat logs are written automatically for intercepted traffic | Which rule allowed or denied a connection; detected threats |
| **Firewall Insights** | Insights and recommendations | Needs Firewall Rules Logging for hit-count based insights | Shadowed, unused and overly permissive rules |
| **VPC Flow Logs** | Sampled flow records | Per subnet, VPC network, organization, VLAN attachment or VPN tunnel | 5-tuple, bytes, packets, RTT, VM and geo metadata |
| **Cloud DNS** | Query logs | Server policy `--enable-logging` (private); per-zone logging for public zones | Who queried what, response code |
| **Cloud NAT** | Translation and error logs | `--enable-logging --log-filter=ALL|ERRORS_ONLY|TRANSLATIONS_ONLY` on the gateway | New NAT translations, and drops for lack of ports |
| **Network Connectivity Center** | Cloud Audit Logs and hub/spoke state | Automatic | Spoke acceptance, route table changes, who changed what |
| **Load balancers** | Request logs | `--enable-logging --logging-sample-rate` on the backend service | Status code, latency, `statusDetails`, cache hit, Cloud Armor outcome |
| **Cloud Armor** | Fields in load balancer logs (`enforcedSecurityPolicy`); verbose logging option | Enabled with LB logging; `--log-level=VERBOSE` on the policy for details | Which rule matched, preview results, rate limit actions |

```bash
# Flow logs on a subnet, 5-second aggregation, 50% secondary sampling, all metadata
gcloud compute networks subnets update app-subnet --region=us-central1 \
  --enable-flow-logs \
  --logging-aggregation-interval=interval-5-sec \
  --logging-flow-sampling=0.5 \
  --logging-metadata=include-all

# Firewall rule logging on a VPC firewall rule
gcloud compute firewall-rules update allow-web --enable-logging \
  --logging-metadata=include-all

# Cloud NAT error logging (port exhaustion shows here)
gcloud compute routers nats update app-nat --router=nat-router \
  --region=us-central1 --enable-logging --log-filter=ERRORS_ONLY

# DNS query logging for a VPC
gcloud dns policies update hub-inbound --enable-logging
```

**VPC Flow Logs details** worth knowing: records are **sampled** (Google samples packets on the host, then a configurable secondary sampling rate applies) and **aggregated** over an interval (default 5 seconds, up to 15 minutes); metadata annotations (VM names, regions, geographic data, GKE details) can be excluded to save cost; filters let you keep only matching flows; logs are kept 30 days in the `_Default` bucket unless you route them elsewhere. Mirrored packets are not logged. Flow logs can also be configured centrally at the **organization or VPC network level**, and on **VLAN attachments and VPN tunnels** to see hybrid flows.

Useful log queries:

```bash
# Denied connections from firewall logging
gcloud logging read 'logName:"compute.googleapis.com%2Ffirewall" AND jsonPayload.disposition="DENIED"' --limit=20

# VPC Service Controls denials
gcloud logging read 'protoPayload.metadata."@type"="type.googleapis.com/google.cloud.audit.VpcServiceControlAuditMetadata"' --limit=20

# Load balancer 5xx with the reason
gcloud logging read 'resource.type="http_load_balancer" AND httpRequest.status>=500' \
  --format="value(httpRequest.status,jsonPayload.statusDetails)" --limit=20
```

For long-term analysis, route flow logs to **BigQuery** or a **Log Analytics**-enabled log bucket with a sink, then query top talkers, port scans or unexpected egress. Flow Analyzer (5.3) builds on the Log Analytics option.

```sql
-- Top talkers by bytes over the last day (BigQuery export)
SELECT jsonPayload.connection.src_ip AS src, jsonPayload.connection.dest_ip AS dst,
       SUM(CAST(jsonPayload.bytes_sent AS INT64)) / POW(1024, 3) AS gib
FROM `project.vpc_flows.compute_googleapis_com_vpc_flows_*`
WHERE _TABLE_SUFFIX >= FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
GROUP BY src, dst ORDER BY gib DESC LIMIT 20;
```

### Monitoring networking metrics

Cloud Monitoring collects network metrics automatically. Know roughly what exists for each component and what you would alert on:

| Component | Signals to watch | Typical alert |
|-----------|------------------|---------------|
| **Cloud VPN** | Tunnel established status, sent and received bytes and packets, dropped packets (including by reason), per-tunnel packets per second | Tunnel down; packets near the per-tunnel limit; drops due to exceeding MTU |
| **Cloud Interconnect and VLAN attachments** | Circuit operational status and receive/transmit light levels, link capacity and utilization, attachment throughput, dropped packets | Circuit down; light level out of range; attachment near capacity |
| **Cloud Router** | BGP session up, number of received and advertised routes, learned route count against quota | Session down; received routes dropped to zero; route limit approaching |
| **Load balancers** | Request count by response code class, total and backend latencies, backend health | 5xx ratio; latency SLO burn; unhealthy backends |
| **Google Cloud Armor** | Requests allowed, denied, throttled and previewed per policy and rule; Adaptive Protection alerts | Spike in denies; Adaptive Protection attack alert |
| **Cloud NAT** | Allocated ports, port usage, dropped sent packets (reason `OUT_OF_RESOURCES`), open connections, NAT IP usage | Any drops for lack of ports |

```bash
# Example: alert when a VPN tunnel is not established
gcloud alpha monitoring policies create --policy-from-file=- <<'EOF'
displayName: VPN tunnel down
combiner: OR
conditions:
- displayName: tunnel_established == 0
  conditionThreshold:
    filter: metric.type="vpn.googleapis.com/tunnel_established" resource.type="vpn_gateway"
    comparison: COMPARISON_LT
    thresholdValue: 1
    duration: 300s
EOF
```

Use **uptime checks** for external endpoints, **log-based metrics** to turn log patterns (for example Cloud NAT `OUT_OF_RESOURCES` errors) into alertable time series, and dashboards per component. Pre-built dashboards exist in the console for VPN, Interconnect, Cloud NAT, load balancing and Cloud Armor.

---

## 5.2 Maintaining and troubleshooting connectivity issues

### Draining and redirecting traffic with an Application Load Balancer

Planned maintenance should never drop user requests:

- **Connection draining** (`--connection-draining-timeout` on the backend service): when an instance is removed from a group or deleted, existing requests get up to that many seconds to finish while no new requests are sent to it.
- **Capacity scaler `0`** on a backend: stops new traffic to that whole instance group or NEG (drain a zone or region) while keeping it attached so you can bring it back.
- **Weighted traffic splitting** in a URL map route rule: shift traffic gradually from one backend service to another (blue/green, canary), and roll back by changing weights.
- **URL redirects** (`urlRedirect`) to move clients to a new host or path, or HTTP to HTTPS.
- **Managed instance group rolling updates** with `maxUnavailable` and `maxSurge` to replace instances while the load balancer keeps serving.

```bash
gcloud compute backend-services update web-bes --global --connection-draining-timeout=120
gcloud compute backend-services update-backend web-bes --global \
  --instance-group=web-mig-us --instance-group-region=us-central1 --capacity-scaler=0
```

Load balancer error clues: a **502** with `statusDetails` like `failed_to_connect_to_backend` or `backend_timeout` points at the backend or a firewall/health check problem; a **503** with `no_healthy_backends` means health checks are failing everywhere (often the `35.191.0.0/16` and `130.211.0.0/22` firewall rule); `denied_by_security_policy` is Cloud Armor. Google-managed certificate stuck in `PROVISIONING` almost always means DNS does not yet point at the LB IP, or a CAA record blocks Google's CA.

### Managing and troubleshooting VPNs

Work from the outside in:

1. **Tunnel status**: `gcloud compute vpn-tunnels describe` shows `status` and `detailedStatus` (for example "No incoming packets", "Negotiation failure", "Peer not responding").
2. **Reachability of the peer**: on-premises must allow **UDP 500, UDP 4500 and ESP** to and from the Google gateway IPs; NAT in front of the peer requires NAT-T (UDP 4500).
3. **IKE settings**: mismatched shared secret, IKE version, ciphers or lifetimes show up in VPN logs as negotiation or proposal failures.
4. **Classic VPN traffic selectors**: policy-based tunnels need exactly matching local and remote selectors.
5. **BGP over the tunnel**: tunnel up but no routes means a BGP problem (next section).
6. **Data plane**: tunnel and BGP up but large transfers hang usually means **MTU/MSS** problems; drops near the per-tunnel packet limit mean you need more tunnels.

```bash
gcloud compute vpn-tunnels describe tunnel-0 --region=us-central1 \
  --format="value(status,detailedStatus)"
gcloud logging read 'resource.type="vpn_gateway" AND severity>=WARNING' --limit=20
```

### Managing and troubleshooting Cloud Interconnect

- **Circuit layer**: connection state and **light levels** (receive/transmit optical power) show whether the physical cross-connect is healthy; a circuit that never came up after the LOA-CFA usually needs the colocation provider to fix the cross-connect.
- **Attachment layer**: Partner attachments sit in `PENDING_PARTNER` until the provider provisions them, then must be **activated**; Dedicated attachments need the right VLAN ID on your router.
- **BGP layer**: Partner Cloud Routers must use ASN **16550**; Layer 2 partner connections need you to configure BGP; MD5 mismatches keep sessions down.
- **MTU**: attachment MTU must match the on-premises interface and VPC; a mismatch often shows as BGP up but large packets dropped.
- **Capacity**: an attachment at its configured bandwidth drops packets; check attachment throughput metrics and raise capacity or add attachments.
- **Maintenance**: Google notifies about maintenance per EAD; redundant designs ride through it, single-EAD designs go down.

```bash
gcloud compute interconnects describe my-interconnect-ead1 \
  --format="value(state,operationalStatus)"
gcloud compute interconnects get-diagnostics my-interconnect-ead1
gcloud compute interconnects attachments describe attach-us-ead1 --region=us-central1 \
  --format="value(state,operationalStatus)"
```

### Troubleshooting Cloud Router BGP peering

```bash
gcloud compute routers get-status vpn-router --region=us-central1 \
  --format="table(result.bgpPeerStatus[].name,result.bgpPeerStatus[].status,result.bgpPeerStatus[].state,result.bgpPeerStatus[].numLearnedRoutes)"
# Routes this router installed in the VPC
gcloud compute routers get-status vpn-router --region=us-central1 \
  --format="table(result.bestRoutes[].destRange,result.bestRoutes[].nextHopIp,result.bestRoutes[].priority)"
```

Common causes and fixes:

| Symptom | Likely cause |
|---------|--------------|
| Session stays `Idle`/`Connect` | Wrong peer IP or ASN, link-local addresses mismatched, MD5 key mismatch, tunnel or attachment down |
| Session flaps | Unstable link, BFD timers too aggressive, MTU problems on the BGP session |
| Session up, zero learned routes | Peer not advertising, route filters or route policies dropping prefixes |
| Learned routes present but not used | A more specific or lower-priority route wins elsewhere; regional routing mode keeps them in one region; learned route quota exceeded |
| On-premises does not learn a range | It is not a local subnet and needs **custom advertisement** (peered subnets, PSA range, PGA VIPs) |
| Asymmetric paths | MED/advertised route priority and AS path settings differ between links; legacy best path selection ignores AS path across regions |

### Troubleshooting with VPC Flow Logs, firewall logs and Packet Mirroring

These three tools answer different questions and the exam likes to make you choose:

| Tool | Answers | Limits |
|------|---------|--------|
| **VPC Flow Logs** | Did traffic flow between A and B, how much, how fast (RTT), from where | Sampled metadata, no payload, not every packet |
| **Firewall Rules Logging** | Which specific rule allowed or denied a connection | Only for rules with logging on; logs connections, not every packet; implied rules are not logged (create an explicit deny with logging to see default-deny hits) |
| **Packet Mirroring** | What exactly is inside the packets (headers and payload) | Costs bandwidth and money; needs a collector behind an internal passthrough NLB; same region and VPC rules apply |

Typical flow: Connectivity Test says "allowed" but users report failures; flow logs show the SYN going out with no reply; firewall logs on the destination show a deny from a higher-priority rule or a hierarchical policy; fix the rule. If headers look right but the application still fails, mirror the traffic and look at the packets with tcpdump or an IDS. Packet Mirroring configuration is in [Section 6.4](06-network-security.md#configuring-packet-mirroring-toward-self-managed-collectors).

---

## 5.3 Using Network Intelligence Center

Network Intelligence Center (NIC) is the console home for network observability and diagnostics. Each module answers a different question:

| Module | Question it answers |
|--------|---------------------|
| **Network Topology** | What is connected to what, and how much traffic flows along each edge? |
| **Connectivity Tests** | Can packets get from source to destination, and if not, which route or firewall stops them? |
| **Performance Dashboard** | Is there packet loss or latency, in Google's network overall or in my project? |
| **Firewall Insights** | Which firewall rules are shadowed, unused or too permissive? |
| **Network Analyzer** | What misconfigurations or risky settings exist right now? |
| **Flow Analyzer** | What does my traffic look like by 5-tuple, without writing SQL? |

### Network Topology: visualize throughput and traffic flows

Network Topology draws your VPC networks, regions, subnets, instance groups, load balancers, hybrid links and GKE clusters as a graph, with **metrics on each edge**: throughput, packet loss and latency between entities, including traffic to the internet and to on-premises. It can replay a **past time window** (up to several weeks), which helps answer "what changed during the incident?" It is the fastest way to spot an unexpected heavy flow (for example cross-region traffic that should be local).

### Connectivity Tests: diagnose route and firewall misconfigurations

Connectivity Tests take a source and a destination (VM, IP, GKE Pod or control plane, Cloud SQL, load balancer, PSC endpoint, on-premises IP and more), plus protocol and port, and do two things:

- **Configuration analysis**: simulates the expected path hop by hop through routes, firewall rules and policies, peering, NCC, NAT, VPN and Interconnect, load balancers and VPC Service Controls boundaries, and reports the **exact step** that drops the packet (for example "dropped by firewall rule X" or "no route to destination").
- **Live data plane analysis**: for supported paths, sends real probe packets to measure **reachability, latency and loss**, which catches problems configuration analysis cannot see.

```bash
gcloud network-management connectivity-tests create web-to-db \
  --source-instance=projects/P/zones/us-central1-a/instances/web-1 \
  --destination-instance=projects/P/zones/us-central1-b/instances/db-1 \
  --protocol=TCP --destination-port=5432

gcloud network-management connectivity-tests describe web-to-db \
  --format="yaml(reachabilityDetails)"
gcloud network-management connectivity-tests rerun web-to-db
```

Tests are saved and can be **rerun** after a change, which makes them a natural "did my fix work?" step. They can be run against configurations you cannot easily test from a VM, such as on-premises sources over Interconnect.

### Performance Dashboard: packet loss and latency

Performance Dashboard shows packet loss and latency in two scopes:

- **Google Cloud-wide**: aggregated measurements across Google's network between zones and regions, and to the internet, independent of your workloads. Use it to answer "is it Google or is it me?"
- **Project**: measurements derived from **your** VMs' traffic between zones, regions and the internet.

If project-scope loss is high but the Google-wide view is clean, look at your own instances (CPU saturation, NIC limits, MTU). If both are elevated for the same pair of locations, it is a network-level event (check the Google Cloud Service Health dashboard).

### Firewall Insights: monitor, identify and improve rules

Firewall Insights analyzes your VPC firewall rules and firewall policy rules (hierarchical and network policies) and produces:

- **Shadowed rules**: rules that can never match because a higher- or equal-priority rule covers them.
- **Overly permissive rules**: allow rules with **no hits** in the observation period, allow rules whose **attributes are unused** (for example a port or range never seen), allow rules predicted obsolete by machine learning, and rules with excessively broad IP or port ranges.
- **Deny rules with no hits**: candidates for removal.
- **Hit counts and last hit time** per rule.

Hit-based insights require **Firewall Rules Logging** on the rules analyzed. Recommendations are also exposed through the Recommender API:

```bash
gcloud recommender insights list --project=P --location=global \
  --insight-type=google.compute.firewall.Insight \
  --format="table(insightSubtype,description)"
```

### Network Analyzer: failures, suboptimal configurations, utilization warnings

Network Analyzer runs **continuously and automatically**, examining configuration changes in near real time. It reports insights with a priority (critical, high, medium, low) in categories such as:

- **VPC network**: routes shadowed or invalid, conflicting or unused IP addresses, **IP address utilization** of subnets and secondary ranges nearing exhaustion.
- **Network services**: Cloud NAT and load balancer misconfigurations (for example a health check firewall gap, backends not reachable).
- **GKE**: connectivity from nodes to the control plane, Pod range utilization, service account problems.
- **Hybrid**: dynamic routes shadowed or not installed, quota warnings.
- **Managed services**: issues reaching services such as Cloud SQL.

It is the tool to name when a question says "proactively detect misconfigurations before users notice" or "find subnets about to run out of IPs".

### Flow Analyzer and VPC Flow Logs

Flow Analyzer queries **VPC Flow Logs stored in a log bucket upgraded to Log Analytics** (Observability Analytics). It lets you filter and group flows at **5-tuple granularity** (or by client/server roles), choose time ranges and alignment periods, and rank the top flows by volume, packet drops or latency, without writing SQL (SQL and Gemini-assisted queries are available when you need them). It answers questions like "which VMs send the most traffic to the internet", "who talks to this database", or "what is the cross-region traffic between these subnets". The prerequisite is flow logs flowing into a Log Analytics-enabled bucket; byte counts are estimates from sampled data, so do not use them for billing reconciliation.

---

## Exam traps

- Most data-plane logs are **off by default**: flow logs per subnet or VPC, firewall logging per rule, Cloud NAT logging per gateway, DNS logging via server policy, LB logging per backend service.
- Implied firewall rules are **not logged**; add an explicit low-priority deny with logging to see default-deny hits.
- Firewall Insights hit-based insights need **Firewall Rules Logging**.
- Flow logs are **sampled** and carry no payload; Packet Mirroring gives payload.
- `no_healthy_backends` 503s usually mean the health check firewall rule is missing.
- Connectivity Tests do **configuration analysis** plus **live data plane analysis**; rerun after a fix.
- Performance Dashboard **Google-wide** vs **project** scope separates "Google's network" from "my workload".
- Network Analyzer is **continuous and automatic**; it flags IP exhaustion and misconfigurations proactively.
- Flow Analyzer needs flow logs in a **Log Analytics**-enabled bucket.
- Cloud NAT port exhaustion shows as dropped packets with reason `OUT_OF_RESOURCES`.

## Key terms

- **VPC Flow Logs** - Sampled, aggregated records of network flows for subnets, VPC networks, organizations, VLAN attachments and VPN tunnels.
- **Firewall Rules Logging** - Per-rule logging that records each connection allowed or denied by that firewall rule or policy rule.
- **Connection draining** - Backend service timeout that lets in-flight requests finish on an instance being removed while no new requests arrive.
- **Network Intelligence Center** - Google Cloud console suite for network topology, connectivity testing, performance, firewall and configuration analysis.
- **Network Topology** - Network Intelligence Center graph of your network entities with throughput, loss and latency metrics on each edge.
- **Connectivity Tests** - Diagnostic that simulates a packet path through routes and firewalls and can probe the live data plane.
- **Performance Dashboard** - View of packet loss and latency for Google Cloud as a whole and for your project's resources.
- **Firewall Insights** - Analysis that flags shadowed, unused and overly permissive firewall rules using rule logging data.
- **Network Analyzer** - Continuous automatic configuration analysis that reports misconfigurations and IP utilization warnings.
- **Flow Analyzer** - Network Intelligence Center tool that analyzes VPC Flow Logs in a Log Analytics bucket at 5-tuple granularity.
- **Light levels** - Optical receive and transmit power readings on an Interconnect circuit used to diagnose physical link problems.
- **OUT_OF_RESOURCES** - Cloud NAT drop reason showing a VM ran out of allocated NAT source ports.

## Vendor documentation

- **[📖 VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs)** - sampling, aggregation, scopes
- **[📖 Firewall Rules Logging](https://cloud.google.com/firewall/docs/firewall-rules-logging)** - enabling and reading firewall logs
- **[📖 Cloud NAT logging and monitoring](https://cloud.google.com/nat/docs/monitoring)** - NAT logs and metrics
- **[📖 Cloud DNS logging and monitoring](https://cloud.google.com/dns/docs/monitoring)** - query logging
- **[📖 Cloud VPN monitoring](https://cloud.google.com/network-connectivity/docs/vpn/how-to/viewing-logs-metrics)** - tunnel logs and metrics
- **[📖 Cloud VPN troubleshooting](https://cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting)** - common tunnel failures
- **[📖 Cloud Interconnect troubleshooting](https://cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting)** - circuit, attachment and BGP issues
- **[📖 Cloud Router troubleshooting](https://cloud.google.com/network-connectivity/docs/router/support/troubleshooting)** - BGP session problems
- **[📖 Load balancing logging and monitoring](https://cloud.google.com/load-balancing/docs/https/https-logging-monitoring)** - request logs and statusDetails
- **[📖 Network Intelligence Center overview](https://docs.cloud.google.com/network-intelligence-center/docs/overview)** - all modules
- **[📖 Connectivity Tests overview](https://cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview)** - configuration and live data plane analysis
- **[📖 Performance Dashboard overview](https://cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/overview)** - loss and latency views
- **[📖 Firewall Insights overview](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/overview)** - insight types
- **[📖 Network Analyzer overview](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview)** - insight categories
- **[📖 Flow Analyzer overview](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview)** - analyzing flow logs
- **[📖 Network Topology overview](https://cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview)** - topology graph and metrics
