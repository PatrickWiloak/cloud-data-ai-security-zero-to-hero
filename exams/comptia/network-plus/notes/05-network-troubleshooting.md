---
last-updated: 2026-07-29
---

# Network+ Domain 5 - Network Troubleshooting (24%)

The largest domain. Most questions are scenarios: symptoms are described and you pick the
cause, the next step, or the right tool. Method matters as much as knowledge.

## The CompTIA troubleshooting methodology

Know this in order. Questions frequently ask what to do *next*, and the answer is
whichever step follows the one described.

1. **Identify the problem** - gather information, question users, identify symptoms, determine what changed, and duplicate the problem if possible.
2. **Establish a theory of probable cause** - question the obvious first, and consider multiple approaches (top-to-bottom or bottom-to-top of the OSI model, or divide and conquer).
3. **Test the theory to determine the cause** - if confirmed, move to a plan. If not, establish a new theory or escalate.
4. **Establish a plan of action** - and identify potential effects.
5. **Implement the solution or escalate**.
6. **Verify full system functionality** - and, where applicable, implement preventive measures.
7. **Document findings, actions, and outcomes**.

Two rules the exam enforces: never skip documentation, and always verify before closing.

## Command-line tools

| Tool | What it does | Typical use |
|---|---|---|
| `ping` | ICMP echo | Is the host reachable |
| `traceroute` / `tracert` | Path discovery hop by hop | Where the path breaks |
| `ipconfig` / `ifconfig` / `ip` | Local interface configuration | Check address, mask, gateway |
| `nslookup` / `dig` | DNS queries | Name resolution problems |
| `netstat` / `ss` | Connections and listening ports | Is the service listening |
| `arp -a` | ARP cache | Duplicate IPs, poisoning |
| `route` / `ip route` | Routing table | Is there a path |
| `nmap` | Host and port discovery | What is on the network |
| `tcpdump` / Wireshark | Packet capture | Protocol-level detail |
| `iperf` | Throughput testing | Measure actual bandwidth |

- **`ping` succeeds by IP but fails by name** - the network is fine; DNS is the problem. This is one of the most common exam scenarios.
- **`traceroute` showing asterisks mid-path** - not necessarily a fault. Many routers deprioritize or block ICMP. Only a break that persists to the destination indicates a real problem.

## Hardware tools

- **Cable tester** - verifies continuity and correct pinout.
- **Toner and probe** - traces which cable is which in a bundle or patch panel.
- **Time-domain reflectometer (TDR)** - locates a break or fault along a copper run by distance. OTDR is the fiber equivalent.
- **Light meter / optical power meter** - measures fiber signal strength, diagnosing dirty or damaged connectors.
- **Multimeter** - electrical measurements, including PoE voltage.
- **Loopback adapter** - tests a port by returning its own signal.
- **Wi-Fi analyzer** - shows channel usage, signal strength, and interference.
- **Protocol analyzer** - captures and decodes traffic.

## Common wired issues

- **Incorrect IP configuration** - wrong mask, wrong gateway, or wrong DNS. A wrong subnet mask produces the signature symptom of local traffic working and remote traffic failing.
- **APIPA address (169.254.x.x)** - the DHCP server was unreachable.
- **Duplicate IP address** - intermittent connectivity for both hosts, with ARP cache showing conflict.
- **Duplex mismatch** - one end full duplex, the other half. Produces late collisions and terrible throughput while the link stays up.
- **Speed mismatch** - the link may not come up at all.
- **VLAN mismatch** - the host is in the wrong broadcast domain; it cannot reach its gateway.
- **Bad or exceeded cable** - runs beyond 100 m, or damaged, cause intermittent errors and CRC counters climbing.
- **Crosstalk and EMI** - interference from adjacent pairs or nearby electrical equipment, common when cable is run alongside power.
- **Broadcast storm** - a Layer 2 loop; all ports light up and the network becomes unusable.
- **Asymmetric routing** - traffic leaves by one path and returns by another, which stateful firewalls will drop.
- **Routing loop** - packets circulate until TTL expires, visible in traceroute as repeating hops.
- **MTU mismatch and black-hole** - large packets silently dropped when path MTU discovery fails; small pings succeed while transfers stall.

## Common wireless issues

- **Insufficient signal strength** - too far, or an obstruction. Measured in dBm, where closer to zero is stronger.
- **Channel overlap and interference** - in 2.4 GHz, use only channels 1, 6, and 11.
- **Client capability** - an old client cannot use a newer standard's speeds and can slow the cell for everyone.
- **Roaming misbehavior** - a client clinging to a distant AP rather than switching to a closer one.
- **Captive portal problems** - the client associates but has no access until authentication completes.
- **Incorrect passphrase or authentication type** - association fails immediately.
- **Simultaneous wired and wireless connections** - can create routing ambiguity on the host.

## Common service issues

- **DNS failure** - name resolution fails while IP connectivity works.
- **DHCP scope exhaustion** - no addresses left, so new clients get APIPA. Common after a guest event or a lease time that is too long.
- **Expired IP address or stale lease** - fixed by release and renew.
- **NTP drift** - breaks Kerberos authentication and makes correlated logs untrustworthy.
- **Certificate expiry** - TLS failures across many services at once, often the explanation for a sudden simultaneous outage.
- **Blocked ports or ACL misconfiguration** - a specific application fails while everything else works.

## A workable diagnostic order

1. Is it one host, one segment, or everything? Scope narrows the cause immediately.
2. Can the host reach its own gateway? If not, the problem is local: cable, VLAN, address, or mask.
3. Does IP work but name resolution fail? DNS.
4. What changed? Recent changes cause most incidents, so check change records early.
5. Move up the OSI stack, or start at both ends and meet in the middle.

## Exam pointers

- Methodology-order questions are guaranteed. Memorize the seven steps and their sequence.
- "Works by IP, not by name" is DNS. Almost every time.
- Local traffic fine, remote traffic broken points at subnet mask or default gateway.
- Late collisions on a link that is up means duplex mismatch.
- New clients failing while existing clients work usually means DHCP scope exhaustion.
- When asked for the *next step* after a theory is confirmed, the answer is to establish a plan of action, not to implement the fix immediately.

## Official documentation

**[📖 CompTIA Network+ N10-009 objectives](https://www.comptia.org/certifications/network#examdetails)** - authoritative domain list, including the troubleshooting methodology
**[📖 Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/)** - packet analysis reference
