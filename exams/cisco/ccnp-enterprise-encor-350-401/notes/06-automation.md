---
last-updated: 2026-07-29
---

# ENCOR 06 - Automation

Programmability, data formats, APIs, and configuration management. Roughly 15% of the
exam, and the section most likely to be unfamiliar to traditional network engineers.

## Data formats

- **JSON** - key-value pairs and arrays. Objects use `{}`, arrays `[]`. Values are strings, numbers, booleans, `null`, objects, or arrays. The dominant format in REST APIs.
- **XML** - tag-based and hierarchical, with opening and closing tags. Used by NETCONF.
- **YAML** - indentation-based, human-readable. Used by Ansible playbooks. Lists use `-`, mappings use `key: value`. **Tabs are not permitted**, only spaces, which is the classic YAML error.

Be able to read a snippet and identify the format and the value at a given path. Questions
frequently show JSON and ask what a nested key evaluates to.

## APIs

- **REST** - stateless HTTP operations on resources.
  - **GET** retrieve, **POST** create, **PUT** replace, **PATCH** partially update, **DELETE** remove.
  - **Status codes**: 200 OK, 201 Created, 204 No Content, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests, 500 Server Error.
  - **Idempotency** - GET, PUT, and DELETE are idempotent; POST is not. See [idempotency explained](../../../../learn/concepts/idempotency-explained.md).
- **Authentication** - API keys, tokens, and OAuth. Many Cisco APIs issue a time-limited token from an initial authentication call.
- **Rate limiting** - 429 responses mean back off; well-behaved clients implement retry with backoff.
- **Webhook** - a server-initiated HTTP callback, the push counterpart to polling.

Learn the verb-to-operation mapping and the common status codes. Both are directly tested.

## Network programmability protocols

- **NETCONF** - XML over SSH on port 830. Operates on datastores (running, candidate, startup) with operations `get`, `get-config`, `edit-config`, `copy-config`, `delete-config`, `lock`, `unlock`, and `commit`. Supports transactions, so a failed change can be rolled back atomically.
- **RESTCONF** - REST over HTTPS exposing YANG models, using JSON or XML. Simpler than NETCONF but without full transaction semantics.
- **YANG** - the modelling language defining the structure of configuration and operational data. Models are native (vendor-specific), OpenConfig, or IETF.
- **gNMI** - gRPC-based, used mainly for streaming telemetry subscriptions.

NETCONF supports candidate configuration and commit, which RESTCONF does not. That
difference is the usual discriminator in comparison questions.

## Configuration management tools

| Tool | Language | Agent | Push/Pull | Notes |
|---|---|---|---|---|
| **Ansible** | YAML playbooks | Agentless (SSH/API) | Push | Most common in networking |
| **Puppet** | Puppet DSL | Agent | Pull | Declarative, strong state enforcement |
| **Chef** | Ruby | Agent | Pull | Procedural recipes |
| **Terraform** | HCL | Agentless | Push | Infrastructure provisioning, state file |

- **Ansible components** - inventory (hosts), playbook (YAML tasks), module (the unit of work), role (reusable structure), and variables.
- **Idempotency in configuration management** - running the same playbook twice produces the same end state, with no change reported the second time. This is the defining property.
- **Agentless advantage** - nothing to install on network devices, which is why Ansible dominates network automation.

Ansible is agentless and push-based; Puppet and Chef use agents and pull. Terraform
provisions infrastructure rather than configuring existing devices.

## Python for network automation

Expect to read short scripts rather than write them.

- **Common libraries** - `requests` for REST, `netmiko` for SSH-based CLI automation, `napalm` for multi-vendor abstraction, `ncclient` for NETCONF, `pyats`/`genie` for testing and parsing.
- **Reading JSON** - `response.json()` produces a dictionary; index it with keys and list positions.
- **Basic constructs** - variables, lists, dictionaries, `for` loops, `if` statements, and function definitions.

A typical exam snippet retrieves JSON from a REST call and asks which line extracts a
particular value.

## Cisco platforms and on-box automation

- **Cisco DNA Center / Catalyst Center APIs** - intent-based northbound REST APIs for policy, provisioning, and assurance.
- **Cisco SD-WAN vManage API** - REST for the SD-WAN fabric.
- **Meraki Dashboard API** - REST for cloud-managed devices.
- **EEM (Embedded Event Manager)** - on-box automation reacting to events with applets or Tcl scripts. The answer for "act automatically on the device when X happens" without an external controller.
- **Guest Shell** - a Linux container on the device for running Python locally.
- **Zero-touch provisioning (ZTP)** - devices fetch configuration on first boot via DHCP and a script.
- **Cisco Plug and Play (PnP)** - Cisco's ZTP implementation within Catalyst Center.

EEM is on-box and event-driven; a controller API is off-box and centralised. Choose by
whether the reaction must be local and immediate.

## Intent-based networking

- **Intent-based networking (IBN)** - express the desired outcome, and the system translates it into device configuration, then continuously verifies it.
- **Assurance loop** - translation, activation, and assurance. The verification step is what distinguishes IBN from plain automation.

## Exam pointers

- YAML uses spaces, never tabs.
- REST verbs: GET read, POST create, PUT replace, PATCH modify, DELETE remove.
- 401 is unauthenticated, 403 is authenticated but forbidden, 429 is rate limited.
- NETCONF is XML over SSH 830 with candidate/commit; RESTCONF is HTTP with JSON or XML.
- Ansible is agentless and push; Puppet and Chef are agent-based and pull.
- EEM performs on-box event-driven automation.
- Idempotency means re-running produces no further change.

## Official documentation

**[📖 ENCOR 350-401 exam topics](https://learningnetwork.cisco.com/s/encor-exam-topics)** - authoritative blueprint
**[📖 Cisco DevNet](https://developer.cisco.com/)** - APIs, sandboxes, and learning labs
**[📖 NETCONF and RESTCONF programmability guide](https://www.cisco.com/c/en/us/support/ios-nx-os-software/ios-xe-17/series.html)** - protocol reference
