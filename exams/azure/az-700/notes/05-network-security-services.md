---
last-updated: 2026-10-22
---

# 05 - Design and Implement Azure Network Security Services (15-20%)

This domain covers the three layers of network filtering Azure gives you, from the inside out: network security groups on subnets and NICs, Azure Firewall (managed centrally with Firewall Manager), and the Web Application Firewall in front of web apps. The July 27, 2026 outline also folds in virtual network flow logs, IP flow verify, Bastion and the security side of Azure Virtual Network Manager. The exam usually tests choosing the right layer and then reading its rules correctly.

**[📖 AZ-700 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-700)** - the official skills outline this note follows

---

## Which layer does what

| Layer | Works at | Filters on | Typical job |
|---|---|---|---|
| NSG | Subnet or NIC | 5-tuple, service tags, ASGs | Micro-segmentation between tiers, block inbound internet |
| AVNM security admin rules | Many VNets at once | 5-tuple, service tags | Organization-wide guardrails that NSGs cannot override |
| Azure Firewall | Central hub, all traffic routed through it | 5-tuple, FQDNs, URLs, web categories, threat intelligence, IDPS (Premium) | Egress control, spoke-to-spoke and hybrid inspection |
| WAF | Application Gateway or Front Door | HTTP content | OWASP attacks, bots, rate limits |

They stack. A typical design has a WAF at the edge, Azure Firewall in the hub, NSGs on every subnet and AVNM admin rules as guardrails above them all.

---

## 1. Implement and manage network security groups

### Creating and associating NSGs

A **network security group** is a stateful list of allow and deny rules. You create it once and **associate** it with subnets, NICs or both. Microsoft's guidance is to prefer subnet association and use NIC association only when a single VM needs different rules, because two layers of NSGs double the places a packet can be dropped.

Evaluation order matters when both exist. For **inbound** traffic the subnet NSG is evaluated first, then the NIC NSG. For **outbound** traffic the NIC NSG is first, then the subnet NSG. A packet must be allowed by both to pass. Because NSGs are stateful, return traffic for an allowed flow is permitted automatically.

### Inbound and outbound rules

Each rule has a priority (100 to 4096, lower wins and processing stops at the first match), source and destination (IP ranges, **service tags**, or **application security groups**), ports, protocol (TCP, UDP, ICMP or Any), direction and action. **Augmented rules** let one rule hold several IPs, ports and tags.

Every NSG has default rules at priorities 65000 and above that you cannot delete but can override with a lower number:

- Inbound: allow `VirtualNetwork` to `VirtualNetwork`, allow `AzureLoadBalancer`, deny everything else.
- Outbound: allow `VirtualNetwork` to `VirtualNetwork`, allow to `Internet`, deny everything else.

Note that `VirtualNetwork` covers the VNet, peered VNets and on-premises ranges known through a gateway, so the default rules allow more than people expect.

**Service tags** are Microsoft-maintained groups of IP prefixes, such as `Internet`, `AzureLoadBalancer`, `Storage`, `Sql.EastUS`, `AzureMonitor` or `AzureFrontDoor.Backend`. Using them keeps rules correct as Microsoft's ranges change.

### Application security groups

An **application security group (ASG)** is a label you attach to NICs. Rules reference the ASG instead of IP addresses: "allow TCP 1433 from `asg-app` to `asg-db`". When you add a VM, you attach its NIC to the right ASG and the rules apply with no edits. All NICs in an ASG must be in the same VNet, and a rule's source and destination ASGs must be in the same VNet. This is the answer to "manage rules by workload role without maintaining IP lists".

### Remote server administration and Azure Bastion

Never open RDP or SSH to the internet. The exam's preferred answers, in order:

- **Azure Bastion** - a managed service in `AzureBastionSubnet` that gives browser-based (and, on higher SKUs, native client) RDP and SSH to VMs that have no public IP. Bastion's subnet NSG must allow what the platform needs: inbound HTTPS 443 from `Internet` (users) and from `GatewayManager` and `AzureLoadBalancer`, and inbound 8080 and 5701 from `VirtualNetwork` for Bastion's own data plane; outbound 22 and 3389 to `VirtualNetwork` (the targets), 443 to `AzureCloud`, 8080 and 5701 to `VirtualNetwork`, and 80 to `Internet` for certificate checks. The target VMs' NSGs must allow RDP or SSH from the Bastion subnet.
- **Just-in-time VM access** (Defender for Cloud) - adds a temporary NSG allow rule for a requested source IP and time window, then removes it.
- A restricted rule allowing management ports only from a known admin IP range, as a last resort.

### Virtual network flow logs

Network Watcher **flow logs** record IP flows. There are two kinds, and the outline now names only the newer one:

- **NSG flow logs** are retiring on September 30, 2027, and Azure no longer allows new NSG flow logs to be created. Migrate existing ones.
- **Virtual network flow logs** are the replacement. You enable them on a VNet, subnet or NIC, and they record every flow regardless of whether an NSG is attached, so they also cover AVNM security admin rule decisions and traffic with no NSG. Records land as JSON in a storage account in the same region.

To **implement**: register the `Microsoft.Insights` provider, have a Standard general-purpose v2 storage account in the same region, create the flow log on the target with a retention period, and optionally enable **traffic analytics** to a Log Analytics workspace (which processes the logs every 10 or 60 minutes into maps, top talkers and malicious flow detection).

To **interpret**: each flow tuple carries a timestamp, source and destination IPs and ports, protocol, direction, a decision (allowed or denied), and a flow state - **B** (begin), **C** (continuing, with byte and packet counts) and **E** (end, with final counts). Virtual network flow logs also record which rule (NSG or AVNM) made the decision and, where virtual network encryption is in use, the encryption status. A spike of `D` (denied) inbound flows from internet IPs to a management port tells you something is scanning you; a missing `B` record for an expected flow tells you the traffic never arrived.

### Verify IP flow

Network Watcher **IP flow verify** takes a VM, a direction, a protocol, local and remote IPs and ports, and tells you whether the packet would be allowed or denied and **which rule** decides it. It is the fastest way to answer "which NSG rule is blocking this?". **NSG diagnostics** does the same across every NSG and AVNM rule in the path and works for more source types.

### Virtual network security with Azure Virtual Network Manager

AVNM **security admin configurations** hold **security admin rules** that apply to every VNet in a network group, across subscriptions. They are evaluated **before** NSGs, and their action decides what happens next:

- **Deny** - drop the traffic; no NSG can allow it.
- **Allow** - allow at this layer, then let the NSG make the final decision.
- **Always Allow** - allow and skip NSG evaluation entirely, so a local NSG cannot block it.

Use them for organization-wide guardrails, such as "deny inbound RDP and SSH from the internet everywhere" or "always allow traffic from the security scanner". Like every AVNM configuration, they do nothing until deployed to the target regions.

---

## 2. Design and implement Azure Firewall and Azure Firewall Manager

### Features and SKUs

Azure Firewall is a managed, stateful, highly available firewall service with built-in scaling. Deploy it in `AzureFirewallSubnet` (`/26`) in a hub VNet or inside a Virtual WAN hub, spread across availability zones, and route traffic to it with UDRs (or routing intent in Virtual WAN).

| SKU | Fit | Notable capabilities |
|---|---|---|
| Basic | Small businesses, low throughput | Network and application rules, DNAT, threat intelligence alerts |
| Standard | Most enterprises | Adds FQDN tags, web categories, DNS proxy, threat intelligence in alert or deny mode, autoscaling |
| Premium | Regulated and sensitive environments | Adds TLS inspection, signature-based IDPS, full URL filtering and URL-path aware web categories |

Selection logic: "inspect inside encrypted traffic" or "intrusion detection and prevention signatures" means **Premium**. "Allow outbound only to `*.windowsupdate.com`" means application rules on Standard. "Small branch, cost first" means Basic.

### Designing a deployment

The common designs are:

- **Hub-and-spoke**: the firewall in the hub VNet, spokes with a UDR `0.0.0.0/0` (and spoke-to-spoke prefixes) pointing to the firewall's private IP, and the gateway subnet with routes sending spoke-bound traffic from on-premises through the firewall. Disable gateway route propagation on spoke route tables so BGP routes do not bypass the firewall.
- **Secured virtual hub**: the firewall inside a Virtual WAN hub, with routing intent sending internet and private traffic through it.
- **Forced tunneling**: the firewall's own internet traffic goes to on-premises. This needs the separate management NIC in `AzureFirewallManagementSubnet` with its own public IP so Microsoft can still manage the firewall.

For SNAT, the firewall translates outbound traffic to its public IPs; add more public IPs, or attach a NAT gateway to the firewall subnet, to avoid SNAT port exhaustion. Use **DNS proxy** when application or network rules use FQDNs, so the firewall and the clients resolve names the same way.

### Configuring rules

Rules live in rule collections, which live in rule collection groups, inside a **Firewall Policy**. There are three rule types:

- **DNAT rules** publish an inbound port on the firewall's public IP to a private IP and port.
- **Network rules** filter by source, destination (IP, service tag, IP group or FQDN), port and protocol.
- **Application rules** filter outbound HTTP, HTTPS and MSSQL by FQDN, FQDN tag (for example `WindowsUpdate`) or web category, and on Premium by URL.

Processing order: DNAT rules first, then network rules, then application rules. Within each type, rule collection groups and then rule collections are processed by priority, lowest number first. A network rule match ends processing, so an application rule for the same traffic is never reached. If nothing matches, the traffic is denied. Rules inherited from a parent policy always take precedence over the child policy's own rules. Use **IP groups** to reuse address lists across rules.

### Azure Firewall Manager and policies

**Azure Firewall Manager** is the central console for many firewalls across regions and subscriptions. **Firewall policies** are the objects it manages. A **parent policy** holds organization-wide rules (for example "deny known-bad categories", "allow core platform FQDNs"), and **child policies** inherit them and add local rules for each region or business unit. One policy can be associated with many firewalls. Firewall Manager also manages DDoS protection plans and WAF policies across your estate.

### Secured virtual hub

A **secured virtual hub** is a Virtual WAN hub with Azure Firewall deployed inside it and associated with a Firewall Policy. You create it from Firewall Manager (or convert an existing hub), then set **routing intent** for internet traffic, private traffic or both. That makes the hub send branch-to-VNet, VNet-to-VNet and internet traffic through the firewall without hand-built UDRs. It is the answer to "centrally inspect all traffic between many branches and VNets in a Virtual WAN".

---

## 3. Design and implement a Web Application Firewall deployment

### WAF features

The Azure WAF protects HTTP applications against common exploits such as SQL injection, cross-site scripting, command injection and protocol violations, plus bots and request floods. It is not a separate resource you deploy in a subnet; it is a **WAF policy** you attach to **Application Gateway WAF_v2** (regional) or **Front Door** (global edge). Use Front Door WAF to stop attacks at the edge before they reach any region, and Application Gateway WAF for regional apps or as a second layer.

### Designing a deployment

Design decisions:

- **Where**: Front Door for global apps and DDoS-scale filtering at the edge; Application Gateway for regional and internal apps; both for defense in depth.
- **Which rules**: managed rule sets plus your own custom rules.
- **Granularity**: on Application Gateway a policy can apply to the whole gateway, to a single listener (site) or to a single path, with the most specific winning. On Front Door you attach a policy to one or more domains through a **security policy**.
- **Logging**: send WAF logs to Log Analytics so you can tune.

### Detection versus prevention mode

In **detection** mode the WAF evaluates and logs matches but blocks nothing. In **prevention** mode it blocks requests that match (with Application Gateway returning 403 and Front Door returning a configurable response). The standard rollout is: start in detection, review logs against real traffic, add **exclusions** for fields that legitimately trip rules (for example a rich-text field that looks like script), then switch to prevention. Turning prevention on day one, or disabling whole rule sets to stop false positives, are the wrong answers.

### Rule sets on Front Door and on Application Gateway

- **Managed rule sets**: Microsoft's **Default Rule Set (DRS)**, which tracks OWASP Core Rule Set categories with Microsoft threat intelligence additions, and the **Bot Manager** rule set that identifies good bots, bad bots and unknown bots. On Application Gateway you can also choose OWASP CRS versions such as 3.2. Current managed rule sets use **anomaly scoring**: matches add to a score and the request is blocked only when the score crosses a threshold, which reduces false positives. On Front Door, managed rule sets and bot protection require the **Premium** tier; Standard supports custom rules only.
- **Custom rules** are evaluated **before** managed rules. They match on IP address or range, geography (geo-match), request URI, headers, query string, body or method, and they can **allow**, **block**, **log** or (on Front Door) **redirect**. **Rate-limit rules** count requests per client over a window (for example more than 100 requests in a minute from one IP) and block the excess, which is the answer to scraping and simple floods.

### Implementing and associating a policy

Create the WAF policy for the right platform (Application Gateway and Front Door policies are different resource types and are not interchangeable), choose the mode, add the managed rule set and version, add custom rules and exclusions, then **associate** it: to the Application Gateway, a listener or a path rule; or to Front Door domains through a security policy. An Application Gateway WAF_v2 must have a policy associated.

---

## Exam traps

1. NSG inbound: subnet then NIC. Outbound: NIC then subnet. Both must allow.
2. Default rules allow all `VirtualNetwork` traffic, which includes peered VNets and on-premises.
3. ASG members must be NICs in the same VNet.
4. New NSG flow logs cannot be created; use virtual network flow logs. NSG flow logs retire September 30, 2027.
5. IP flow verify names the exact rule that allows or denies a packet.
6. AVNM security admin rules run before NSGs; Always Allow skips NSG evaluation, Deny cannot be overridden.
7. Azure Firewall rule order is DNAT, network, application; a network rule match stops processing.
8. TLS inspection and IDPS need Firewall Premium.
9. Forced tunneling on Azure Firewall needs the management subnet and its own public IP.
10. WAF rollout: detection, tune exclusions, then prevention. Front Door managed rules and bot protection need Premium.

---

## Key terms

- **Network security group** - a stateful set of priority-ordered allow and deny rules on subnets or NICs
- **Service tag** - a Microsoft-maintained group of IP prefixes, such as Internet, AzureLoadBalancer or Storage
- **Application security group** - a NIC label used as a rule source or destination instead of IP addresses
- **Augmented security rule** - an NSG rule that holds several IPs, ports or service tags at once
- **Azure Bastion** - managed RDP and SSH to VMs without public IPs, deployed in AzureBastionSubnet
- **Virtual network flow logs** - Network Watcher flow records at VNet, subnet or NIC scope that replace NSG flow logs
- **Traffic analytics** - processes flow logs in Log Analytics into maps, top talkers and malicious flow detection
- **IP flow verify** - a Network Watcher test that shows whether a 5-tuple is allowed and which rule decides
- **Security admin rule** - an AVNM rule evaluated before NSGs with Allow, Always Allow or Deny actions
- **Firewall Policy** - the Azure Firewall rule container, with parent policies inherited by child policies
- **DNAT rule** - an Azure Firewall rule that publishes a public port to a private IP and port
- **Application rule** - an Azure Firewall rule that filters outbound traffic by FQDN, FQDN tag or web category
- **Secured virtual hub** - a Virtual WAN hub with Azure Firewall inside it, managed by Firewall Manager
- **Detection mode** - a WAF mode that logs matching requests without blocking them
- **Anomaly scoring** - WAF managed rule evaluation that blocks only when combined rule matches pass a threshold

---

## Vendor documentation

- **[📖 Network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)** - rules, default rules and service tags
- **[📖 How NSGs filter traffic](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-group-how-it-works)** - subnet and NIC evaluation order
- **[📖 Application security groups](https://learn.microsoft.com/en-us/azure/virtual-network/application-security-groups)** - role-based rules without IP lists
- **[📖 NSG access and Azure Bastion](https://learn.microsoft.com/en-us/azure/bastion/bastion-nsg)** - required rules for the Bastion subnet
- **[📖 Virtual network flow logs](https://learn.microsoft.com/en-us/azure/network-watcher/vnet-flow-logs-overview)** - the replacement for NSG flow logs, with the record format
- **[📖 NSG flow logs retirement](https://learn.microsoft.com/en-us/azure/network-watcher/nsg-flow-logs-overview)** - the retirement notice and migration path
- **[📖 IP flow verify](https://learn.microsoft.com/en-us/azure/network-watcher/ip-flow-verify-overview)** - test a 5-tuple against effective rules
- **[📖 Security admin rules in AVNM](https://learn.microsoft.com/en-us/azure/virtual-network-manager/concept-security-admins)** - Allow, Always Allow and Deny
- **[📖 Azure Firewall features by SKU](https://learn.microsoft.com/en-us/azure/firewall/choose-firewall-sku)** - Basic, Standard and Premium
- **[📖 Azure Firewall rule processing logic](https://learn.microsoft.com/en-us/azure/firewall/rule-processing)** - order of DNAT, network and application rules
- **[📖 Azure Firewall Manager](https://learn.microsoft.com/en-us/azure/firewall-manager/overview)** - policies, hub VNets and secured virtual hubs
- **[📖 Azure Web Application Firewall](https://learn.microsoft.com/en-us/azure/web-application-firewall/overview)** - WAF on Application Gateway and Front Door
- **[📖 WAF on Front Door policy settings](https://learn.microsoft.com/en-us/azure/web-application-firewall/afds/waf-front-door-policy-settings)** - modes, managed rules and custom rules
