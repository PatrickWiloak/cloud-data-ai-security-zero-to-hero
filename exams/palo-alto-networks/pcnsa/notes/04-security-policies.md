---
last-updated: 2026-07-29
---

# PCNSA Domain 4 - Security Policies and Profiles

Writing rules, and attaching the inspection that makes them next-generation rather than
port-based.

## Rule structure and evaluation

- **Top-down, first-match** - rules are evaluated in order and the first match wins. Rule order is therefore functional, not cosmetic.
- **Rule components** - name, tag, source zone, source address, source user, destination zone, destination address, application, service, URL category, action, and profiles.
- **Actions** - allow, deny, drop, reset client, reset server, reset both.
  - **Deny** - applies the application's default deny action.
  - **Drop** - silently discards.
  - **Reset** - sends a TCP reset, so the client fails fast rather than waiting for a timeout.
- **Rule types** - universal (default, matches both intrazone and interzone), intrazone only, or interzone only.
- **Implicit rules** - intrazone-default allows, interzone-default denies. Both can be overridden and both have logging disabled by default.

## Application-based policy

- **App-ID in rules** - specify the application rather than the port. This is the central practice the exam tests.
- **`application-default` service** - permits the application only on its standard ports. The recommended setting, because it stops an allowed application being used as a tunnel on an arbitrary port.
- **Application dependencies** - some applications require others to be permitted. The interface shows dependencies, and missing them is a common cause of a rule that appears correct but fails.
- **Application groups** - static collections of applications.
- **Application filters** - dynamic collections defined by category, subcategory, technology, and risk. Filters update automatically as new App-IDs arrive, which groups do not.
- **Implicit application dependency** - applications such as `ssl` and `web-browsing` frequently underpin others.

**Migrating from port-based rules** - the workflow is to run port-based rules, use the
policy optimizer to see which applications actually matched, then rewrite as
application-based rules. Cutting straight to App-ID rules without that data breaks
traffic.

## User-based policy

- **User-ID in rules** - source user or group instead of source address.
- **Group mapping** - LDAP directory groups usable in policy.
- **User mapping** - IP-to-user associations from domain controller logs, syslog, captive portal, the XML API, or terminal server agents.
- **Captive portal / Authentication policy** - forces authentication for users who cannot be mapped passively.
- **Unknown user handling** - traffic from unmapped addresses matches rules written for `any` user, so relying on user-based rules without full mapping coverage leaves gaps.

## Security profiles

Profiles inspect the *content* of traffic that a rule has already allowed. They are
attached to allow rules, and have no effect on deny rules.

- **Antivirus** - blocks known malware in supported protocols.
- **Anti-Spyware** - blocks command-and-control traffic, and includes DNS sinkholing.
- **Vulnerability Protection** - IPS signatures for exploit attempts against clients and servers.
- **URL Filtering** - permits, blocks, alerts, or continues based on web category, and includes credential-theft prevention.
- **File Blocking** - controls file types by direction and application.
- **WildFire Analysis** - forwards unknown files for sandbox analysis.
- **Data Filtering** - detects sensitive patterns such as card numbers leaving the network.

- **Security profile group** - a bundle of profiles applied together, so rules stay consistent.
- **Default profile group** - can be applied automatically to new rules.
- **DNS sinkhole** - answers a malicious DNS query with a controlled address, so the infected internal host connects to the sinkhole and is immediately identifiable in the logs. Without sinkholing, the firewall sees only the DNS server making the query, not the infected client. This is the point of the feature and it is examined.

## Policy objects

- **Address objects and groups** - named addresses, reused across rules.
- **Dynamic address groups (DAG)** - membership determined by tags, updated without a commit. The answer for environments where servers appear and disappear, such as cloud auto-scaling.
- **Service objects** - port and protocol definitions.
- **Tags** - color-coded labels for organization and for DAG membership.
- **External dynamic list (EDL)** - a list of IPs, URLs, or domains fetched from a web server on a schedule, so third-party threat feeds can be enforced without manual updates.

Dynamic address groups and EDLs both exist so policy can change without a commit, which is
the distinguishing benefit to remember.

## Other policy types

- **NAT policy** - address translation, evaluated before security policy.
- **Decryption policy** - what to decrypt and what to exclude.
- **Authentication policy** - when to challenge a user.
- **Policy-based forwarding** - overrides routing.
- **DoS protection policy** - rate limits per rule, complementing zone protection profiles.
- **QoS policy** - traffic prioritization.

## Best practice rulebase shape

1. Explicit deny rules for known-bad at the top, if used.
2. Specific allow rules, application-based, with `application-default`, users where possible, and profile groups attached.
3. Logging enabled on rules that matter, at session end.
4. Overridden interzone-default rule at the bottom with logging enabled, so denied traffic is visible.

- **Policy optimizer** - identifies port-based rules to convert, unused rules, and unused applications within rules.
- **Rule usage tracking (hit count)** - shows which rules are actually matching, and finds dead rules.

## Exam pointers

- First match wins, top down. Reordering rules changes behavior.
- `application-default` restricts an application to its standard ports; this is the recommended service setting.
- Security profiles only apply to allow rules.
- DNS sinkholing exists so you can identify the *infected internal host*, not merely block the domain.
- Dynamic address groups update without a commit; static address groups do not.
- Application filters are dynamic and pick up new App-IDs; application groups are static.
- The interzone-default rule denies but does not log unless you enable logging.

## Official documentation

**[📖 PAN-OS security policy](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/policy)** - rule construction and evaluation
**[📖 Security profiles](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/policy/security-profiles)** - profile types and settings
**[📖 App-ID overview](https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/app-id)** - identification and dependencies
**[📖 Best practice internet gateway security policy](https://docs.paloaltonetworks.com/best-practices)** - recommended rulebase structure
