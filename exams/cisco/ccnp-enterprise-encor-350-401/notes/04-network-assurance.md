---
last-updated: 2026-07-29
---

# ENCOR 04 - Network Assurance

Monitoring, diagnostics, and telemetry. Roughly 10% of the exam, and the section most
about tool selection.

## Diagnostic tools

- **ping** - reachability using ICMP echo. Extended ping allows source, size, and DF-bit control, which is how you test path MTU.
- **traceroute** - hop-by-hop path discovery using TTL expiry.
- **debug** - detailed real-time output. CPU-intensive and capable of destabilizing a production device, so use conditional debugging and always have `undebug all` ready.
- **show** commands - the safe default for state inspection.
- **Conditional debugging** - `debug condition interface` or similar to limit output scope.
- **Ping sweep and path MTU discovery** - `ping <ip> size <n> df-bit` to find the largest frame that traverses the path.

## SPAN and packet capture

- **SPAN (local)** - mirrors traffic from source ports or VLANs to a destination port on the same switch.
- **RSPAN** - mirrors across switches using a dedicated RSPAN VLAN.
- **ERSPAN** - encapsulates mirrored traffic in GRE, so it can cross a routed network to a remote analyzer.
- **Embedded Packet Capture (EPC)** - captures on the device itself and exports a pcap, without needing an external analyzer.

ERSPAN is the answer when the analyzer is across a Layer 3 boundary.

## Flow monitoring

- **NetFlow** - records flows: a unidirectional stream identified by source and destination address, ports, protocol, and interface. Answers "who talked to whom and how much."
- **Flexible NetFlow** - user-defined key and non-key fields, with a flow record, flow monitor, flow exporter, and optional flow sampler.
- **IPFIX** - the IETF standard derived from NetFlow v9.
- **NetFlow versus SPAN** - NetFlow gives metadata about all traffic at low overhead; SPAN gives full packets for a subset. Choose by whether you need payload.

## Syslog and SNMP

- **Syslog severities** - 0 emergency, 1 alert, 2 critical, 3 error, 4 warning, 5 notification, 6 informational, 7 debugging. Configuring level 4 logs levels 0 through 4.
- **Logging destinations** - console, monitor (VTY), buffer, and syslog server.
- **SNMP versions** - v1 and v2c use community strings in clear text; **v3** adds authentication and encryption, with security levels noAuthNoPriv, authNoPriv, and authPriv.
- **SNMP components** - manager, agent, MIB, OID, and traps versus informs. **Informs are acknowledged; traps are not**, so informs are more reliable at the cost of overhead.

## IP SLA

- **IP SLA** - generates synthetic traffic to measure reachability, latency, jitter, and packet loss.
- **Operations** - ICMP echo, UDP jitter (for voice quality), TCP connect, HTTP, and DNS.
- **Responder** - the far-end device, which timestamps to improve accuracy for jitter measurements.
- **Tracking** - an IP SLA operation can be tracked and tied to a static route or an HSRP priority, so a failure triggers a routing change. This is the classic use case: failing over a default route when the ISP is reachable but the path beyond it is broken.

## Model-driven telemetry

- **Streaming telemetry** - devices push data continuously, rather than being polled. Scales far better than SNMP polling and gives higher resolution.
- **YANG** - the data modeling language describing device configuration and state.
- **NETCONF** - XML-based configuration protocol over SSH (port 830), with candidate, running, and startup datastores.
- **RESTCONF** - REST/HTTP interface to YANG models, using JSON or XML.
- **gNMI** - gRPC network management interface, commonly used for telemetry subscriptions.
- **Dial-in versus dial-out** - dial-in means the collector initiates the subscription; dial-out means the device initiates the connection to the collector.

Streaming telemetry versus SNMP polling is a standard comparison: push versus pull,
high-frequency versus interval-limited.

## Cisco DNA Center / Catalyst Center assurance

- **Assurance** - correlates telemetry into health scores for clients, devices, and applications.
- **Client health and network health scores** - aggregate indicators.
- **Path trace** - visualizes the path between two endpoints, showing ACLs and QoS along the way.
- **Sensor tests** - synthetic wireless client tests from purpose-built sensors.
- **Issues and root cause analysis** - guided remediation suggestions.

## Choosing the right tool

| Requirement | Tool |
|---|---|
| Who talked to whom, and volume | NetFlow |
| Full packet payload | SPAN, or ERSPAN across Layer 3 |
| Continuous latency and jitter measurement | IP SLA |
| Push-based, high-frequency metrics | Streaming telemetry (gNMI) |
| Device event notification | Syslog, or SNMP traps/informs |
| Configuration via programmatic interface | NETCONF or RESTCONF |
| Visualize path with policy applied | Path trace in Catalyst Center |

## Exam pointers

- ERSPAN crosses Layer 3; SPAN and RSPAN do not.
- SNMP informs are acknowledged; traps are not.
- Syslog level 4 includes levels 0 to 4.
- IP SLA plus object tracking is how you fail over a static route on path failure, not just link failure.
- NETCONF uses SSH port 830 and XML; RESTCONF uses HTTP and JSON or XML.
- Streaming telemetry pushes; SNMP polls.

## Official documentation

**[📖 ENCOR 350-401 exam topics](https://learningnetwork.cisco.com/s/encor-exam-topics)** - authoritative blueprint
**[📖 Flexible NetFlow configuration guide](https://www.cisco.com/c/en/us/support/ios-nx-os-software/flexible-netflow/series.html)** - records, monitors, exporters
**[📖 Model-driven telemetry](https://www.cisco.com/c/en/us/support/ios-nx-os-software/ios-xe-17/series.html)** - YANG, NETCONF, gNMI
