---
last-updated: 2026-07-29
---

# PCNSA - Exam Scenarios

Fourteen worked scenarios in PCNSA style. Illustrative, written for this repo, not real
exam questions. PCNSA questions are shorter than AWS professional-tier scenarios but turn
on precise product behaviour, especially NAT, policy evaluation order, and what each
feature can and cannot do.

Attempt each before reading the analysis.

---

## 1. The NAT rule that looks right

An internal web server at 10.1.1.50 in the DMZ zone is published on public address
203.0.113.10. A destination NAT rule translates 203.0.113.10 to 10.1.1.50. The security
rule permits untrust to DMZ, destination 10.1.1.50, application `web-browsing`. External
users cannot reach the server.

**Why?** Security policy matches the **pre-NAT destination address**. The rule must
specify destination 203.0.113.10, with destination zone DMZ (the post-NAT zone). Using the
private address never matches.

**Takeaway:** pre-NAT addresses, post-NAT zones. Expect this repeatedly.

---

## 2. Traffic denied, nothing in the logs

Users report a blocked application. The administrator searches traffic logs and finds no
entries at all for that session.

**Why?** The traffic is hitting the interzone-default rule, which denies and does **not**
log by default. Override the rule and enable logging so denies become visible.

**Takeaway:** absence of a log is itself a clue that a default rule matched.

---

## 3. Inserting a firewall without redesign

A customer wants a firewall between two existing network segments, but cannot change
addressing, routing, or default gateways.

**Answer:** Virtual Wire deployment. Two interfaces bonded transparently, no IP, no MAC
changes, no routing impact.

**Takeaway:** vwire is the no-redesign insertion mode. Tap is visibility only and cannot
block.

---

## 4. Identifying the infected host

Anti-Spyware is blocking DNS queries to a known command-and-control domain. Logs show the
source as the internal DNS server, 10.1.1.53. The administrator cannot tell which
workstation is infected.

**Answer:** enable DNS sinkholing. The firewall responds with a sinkhole address, so the
infected workstation connects directly to it and appears as the source in traffic logs.

**Takeaway:** sinkholing exists to identify the infected client, not merely to block the
domain.

---

## 5. The rule that permits too much

A rule permits application `web-browsing` with service `any`. Users are tunnelling other
protocols over port 80.

**Answer:** change the service to `application-default`, restricting the application to
its standard ports.

**Takeaway:** `application-default` is the recommended service setting for application-based
rules.

---

## 6. Cloud servers that keep changing

An auto-scaling group in AWS constantly adds and removes instances. The administrator does
not want to commit a configuration change every time.

**Answer:** dynamic address groups with tags. Membership updates without a commit.

**Takeaway:** DAGs and external dynamic lists both change enforcement without a commit.
Static address groups do not.

---

## 7. Migrating away from port-based rules

A firewall has 200 legacy port-based rules. Management wants App-ID rules without breaking
production.

**Answer:** use the policy optimiser. It shows which applications actually matched each
port-based rule, so rules can be converted from evidence rather than guesswork.

**Takeaway:** never convert to App-ID rules without first observing what traffic really
matched.

---

## 8. Failover that drops sessions

An active/passive HA pair fails over. Users lose all established sessions and must
reconnect.

**Why?** The HA2 link, which synchronises session state, is not configured or has failed.
HA1 carries control traffic only, so the pair can be healthy for failover purposes while
session state is not shared.

**Takeaway:** HA1 control, HA2 session sync, HA3 packet forwarding in active/active.

---

## 9. A rule with no threat detection

A security rule allows traffic and is logging correctly, but known malware passes through
undetected. Threat Prevention is licensed and signatures are current.

**Why?** No security profiles are attached to the rule. Profiles are what inspect content;
allowing traffic does not inspect it.

**Takeaway:** attach a security profile group to every allow rule that matters. Profiles do
nothing on deny rules.

---

## 10. Encrypted traffic is invisible

The ACC shows a large volume of `ssl` traffic that App-ID cannot resolve into specific
applications.

**Answer:** implement SSL Forward Proxy decryption so App-ID and Content-ID can inspect the
payload, with exclusions for categories such as financial and health services.

**Takeaway:** without decryption, inspection of encrypted traffic is severely limited.
Certificate-pinned applications must be excluded or they will break.

---

## 11. The change that did nothing

An administrator edits a security rule, verifies it on screen, and asks a user to retest.
Behaviour is unchanged.

**Why?** The change is in the candidate configuration. It takes effect only on commit.

**Takeaway:** nothing is enforced until commit.

---

## 12. Users bypass the user-based rule

A rule permits `finance-group` to reach an application. Some users reach it who are not in
that group.

**Why?** Those users' IP addresses are not mapped by User-ID, so their traffic does not
match user-based rules and falls through to a later rule permitting `any` user.

**Takeaway:** user-based policy is only as complete as User-ID mapping coverage. Captive
portal or authentication policy fills the gaps.

---

## 13. Sending specific traffic out a backup link

All traffic routes out the primary ISP. The customer wants guest wireless traffic to use a
secondary link regardless of the routing table.

**Answer:** policy-based forwarding, matching the guest source zone and directing it to the
secondary egress interface.

**Takeaway:** PBF overrides the routing table based on policy criteria.

---

## 14. Flood from the internet

The firewall is being hit with a SYN flood from many external addresses. The administrator
wants protection applied to all traffic entering the untrust zone.

**Answer:** a zone protection profile on the untrust zone, with SYN flood protection
enabled. DoS protection policies handle more granular per-rule limits.

**Takeaway:** zone protection profiles attach to zones and handle floods and reconnaissance.
Security profiles attach to rules and handle content.

---

## Patterns worth memorising

| Symptom | Usual answer |
|---|---|
| Published server unreachable | Security rule using post-NAT address instead of pre-NAT |
| Denied traffic with no log entry | Interzone-default rule, logging disabled |
| Insert firewall with no redesign | Virtual Wire |
| Cannot identify infected internal host | DNS sinkholing |
| Application tunnelled on wrong port | `application-default` service |
| Constantly changing server set | Dynamic address groups |
| Sessions dropped on HA failover | HA2 link |
| Malware passing an allow rule | No security profiles attached |
| Change appears to have no effect | Not committed |
| Encrypted traffic unidentified | SSL Forward Proxy decryption |
