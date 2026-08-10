---
last-updated: 2026-08-09
difficulty: intermediate
---

# HashiCorp Boundary Associate - Practice Questions

15 questions for Boundary Associate prep across the domain model, targets and hosts, credential management, session lifecycle, and deployment.

> **Cert page:** [exams/hashicorp/boundary-associate/](../../exams/hashicorp/boundary-associate/)

---

### Question 1
**Scenario:** What problem does Boundary solve compared with a bastion host and a VPN?

A. It replaces the network entirely
B. It grants identity-based access to specific services without giving network access to the whole subnet, and without distributing credentials
C. It is a firewall
D. It stores secrets

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A VPN puts the user on the network and then relies on downstream controls; Boundary brokers a session to one target and nothing else. Combined with credential injection, the user never sees the credential at all, which is the practical difference from a bastion.
</details>

---

### Question 2
**Scenario:** What are the two main components of a Boundary deployment?

A. Server and agent
B. Controllers, which handle API, authentication, and authorization, and workers, which proxy session traffic
C. Client and proxy
D. Master and replica

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Controllers hold state in the database and make decisions; workers sit near the targets and carry the data path. Because workers do the proxying, they can live inside private networks that the controller cannot reach directly, which is what makes Boundary work across network boundaries.
</details>

---

### Question 3
**Scenario:** Boundary's resource hierarchy, from the top.

A. Global scope, organization scopes, project scopes
B. Project, organization, global
C. Account, user, role
D. Host, target, session

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Scopes nest global to org to project, and permissions granted at a higher scope can apply downward. Targets, host catalogs, and credential stores live in projects, while auth methods and roles are commonly defined at global or org level.
</details>

---

### Question 4
**Scenario:** Users must connect to a set of interchangeable web servers by one name.

A. A target with a host set containing the host catalog's matching hosts
B. One target per host
C. A DNS record
D. A load balancer only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A target references host sets, and Boundary picks a host from the set at connection time. With a dynamic host catalog backed by a cloud provider, membership updates automatically as instances come and go, so access does not need re-configuring after every scaling event.
</details>

---

### Question 5
**Scenario:** A user should connect to a database without ever learning the password.

A. Credential injection from a credential library, with the worker supplying credentials to the session
B. Emailing the password
C. A shared vault of static passwords
D. Credential brokering only

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Injection means the credential goes into the protocol session and never to the user's screen, which is the strongest form. Brokering returns the credential to the client, which is still an improvement over static distribution but leaves the secret in the user's hands.
</details>

---

### Question 6
**Scenario:** Boundary integrates with Vault for credentials.

A. Boundary stores its own passwords only
B. A Vault credential store with credential libraries issuing dynamic credentials per session
C. Vault is not supported
D. Only static credentials are supported

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** This pairing is the point: Vault mints a short-lived credential when the session starts, Boundary hands it to the session, and it is revoked when the session ends. Access and secrets are then both temporary and both attributable to a named identity.
</details>

---

### Question 7
**Scenario:** Which authentication methods can Boundary use?

A. Password only
B. Password, OIDC (for enterprise identity providers), and LDAP
C. Certificates only
D. Kerberos only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** OIDC is the production choice because it inherits the organization's existing MFA and lifecycle, and managed groups can map IdP claims to Boundary roles. The password method exists mainly for initial setup and break-glass.
</details>

---

### Question 8
**Scenario:** Permissions are assigned to whom in Boundary?

A. Directly to users only
B. Through roles containing grants, assigned to users, groups, or managed groups within a scope
C. To hosts
D. To sessions

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Grants use a resource and action syntax such as `ids=*;type=target;actions=authorize-session`, attached to roles. Assigning roles to groups (and managed groups sourced from the IdP) is what makes access review tractable as the estate grows.
</details>

---

### Question 9
**Scenario:** An auditor asks who accessed which host last Tuesday.

A. Boundary session recording and audit events, showing principal, target, host, and times
B. Firewall logs
C. Host-level logs only
D. It cannot be determined

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Boundary records session metadata for every connection with the authenticated identity attached, which host-level logs often cannot supply because they see only a source IP. Session recording, an Enterprise and HCP feature, captures the session content itself for SSH targets.
</details>

---

### Question 10
**Scenario:** A session must automatically end after a defined period.

A. Set session max seconds and connection limits on the target
B. Ask the user to disconnect
C. Reboot the host
D. Sessions never end

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Targets carry session TTL and connection limits, and administrators can cancel sessions on demand. Bounded sessions matter because they turn access into something that expires by default rather than something that must be remembered and removed.
</details>

---

### Question 11
**Scenario:** Targets live in a private network the controller cannot reach.

A. It cannot work
B. Deploy workers inside that network; they connect outward to the controller and proxy sessions to local targets
C. Expose the targets publicly
D. Use a VPN

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Multi-hop worker chains extend this further, letting a worker in a DMZ relay to a worker deeper inside. Because the connection is initiated outward, no inbound firewall rule to the private network is required, which is usually the deciding factor.
</details>

---

### Question 12
**Scenario:** A host catalog should update automatically as cloud instances change.

A. Static host catalogs updated manually
B. A dynamic host catalog with a plugin for AWS, Azure, or GCP, using tag-based filters
C. A cron job editing the catalog
D. Manual imports

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Dynamic catalogs query the cloud provider and build host sets from tag filters, so an autoscaled instance becomes reachable as soon as it exists. Static catalogs are fine for fixed infrastructure and become stale everywhere else.
</details>

---

### Question 13
**Scenario:** A user runs `boundary connect ssh -target-id ttcp_...`. What happens?

A. Boundary opens the firewall
B. Boundary authorizes the session, returns connection details, and the local client proxies through a worker to the chosen host
C. The user gets a network route to the subnet
D. The target's password is printed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The client establishes a local listener and proxies through the worker, so the user's machine never gets a route into the target network. Authorization is evaluated per session, which is why revoking a role takes effect on the next connection attempt.
</details>

---

### Question 14
**Scenario:** Boundary's database.

A. It stores secrets in plaintext
B. Controllers use PostgreSQL for configuration and session state, with a KMS for encrypting sensitive values
C. It uses SQLite in production
D. No database is needed

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** PostgreSQL is the state store, and the KMS blocks (root, worker-auth, recovery) encrypt sensitive data and authenticate workers. Losing the KMS keys makes the database unusable, so key management is part of the backup plan rather than an afterthought.
</details>

---

### Question 15
**Scenario:** How does Boundary fit a zero trust model?

A. It replaces identity providers
B. Every session is authenticated, authorized against a policy at connection time, scoped to one service, time-bounded, and logged
C. It grants standing network access
D. It is a network firewall

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Those five properties are close to a definition of zero trust access: no implicit trust from network position, per-session authorization, least privilege scope, expiry by default, and an audit record. That is exactly what a flat VPN does not give you.
</details>

---

## Where to go deeper

- [Boundary Associate cert page](../../exams/hashicorp/boundary-associate/) - notes, practice plan, strategy
- [Vault Associate practice questions](./hashicorp-vault-associate.md) - the credential source Boundary uses
- [Zero trust architecture](../architecture-patterns/zero-trust-architecture.md) - the model in depth
- [IAM topic index](../../topics/iam.md) - identity across the repo
- **[📖 Boundary documentation](https://developer.hashicorp.com/boundary/docs)** - primary source
