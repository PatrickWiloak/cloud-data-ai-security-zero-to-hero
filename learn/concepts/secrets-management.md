---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 8 min
---

# Secrets Management

> **8-minute read. Assumes you've read [IAM explained](./iam-explained.md).**

## The one-line answer

A secret is any credential that grants access: a database password, an API key, a private key, a token. Secrets management is the practice of storing them somewhere they can be controlled, rotated, and audited, and getting them to applications without leaving copies everywhere.

The goal to aim for is having **no long-lived secrets at all**, which modern cloud identity makes achievable for a surprising amount of a system.

## Why the obvious approaches fail

**In the source code.** Committed to version control, visible to everyone with repository access, and permanent: deleting it in a later commit does not remove it from history. Automated scanners find these constantly on public repositories.

**In a `.env` file.** Better, until it is copied to a laptop, pasted into a chat message, or accidentally committed because someone forgot the `.gitignore` entry.

**In environment variables.** A reasonable delivery mechanism, and not a storage mechanism. Environment variables appear in process listings, crash dumps, and logs, and are inherited by child processes. They also cannot be rotated without a restart.

**In a wiki or password manager for humans.** Fine for humans, wrong for applications: no programmatic access, no rotation, no audit of which service used which credential.

## The ladder

From worst to best. Move up as far as your platform allows.

| Level | Approach | Problem it still has |
|---|---|---|
| 1 | Hardcoded in source | Everything |
| 2 | Config file outside version control | Copies proliferate, no rotation, no audit |
| 3 | Environment variables from a deployment system | Better delivery, still a long-lived credential |
| 4 | **Secrets manager**, fetched at runtime | Central control, rotation, and audit. The application still authenticates to the manager |
| 5 | **Workload identity**: no stored credential at all | The platform vouches for the workload |

Level 4 is the practical baseline. Level 5 is the goal wherever the target service supports it.

## Secrets managers

The dedicated services: AWS Secrets Manager and Parameter Store, Azure Key Vault, Google Secret Manager, and HashiCorp Vault.

What they give you beyond a file:

- **Access control** per secret, so a service reads only what it needs
- **Audit logging** of every read, which is what turns "we think it leaked" into "here is who accessed it"
- **Rotation**, sometimes automatic in coordination with the target service
- **Versioning**, so a bad rotation can be rolled back
- **Encryption at rest** with keys you can control
- **Dynamic secrets** in Vault's case: credentials created on demand with a short lifetime, so there is nothing long-lived to steal

## Workload identity: the level worth reaching

The insight is that if the platform already knows which workload is running, the workload does not need a password to prove it.

- **AWS**: IAM roles for EC2, ECS task roles, IRSA and EKS Pod Identity for Kubernetes
- **Azure**: managed identities, system-assigned or user-assigned
- **GCP**: service accounts attached to resources, and Workload Identity for GKE
- **Across boundaries**: workload identity federation, so GitHub Actions, another cloud, or a Kubernetes cluster can obtain credentials by presenting a token from its own issuer rather than holding a stored secret

The practical effect: your application code calls the cloud SDK with no credentials configured, and it works, because the runtime supplies short-lived credentials automatically. There is nothing in a file to leak and nothing to rotate.

## Getting secrets into Kubernetes

Kubernetes `Secret` objects are **base64-encoded, not encrypted**, and anyone with read access to the namespace can decode them. Treat them as a delivery mechanism, not a vault.

The common patterns:

| Pattern | How it works |
|---|---|
| **External Secrets Operator** | A controller syncs values from a real secrets manager into Kubernetes Secrets |
| **Secrets Store CSI Driver** | Mounts secrets from a manager directly into the pod filesystem |
| **Sealed Secrets** | Encrypted secrets can be committed to Git; only the in-cluster controller can decrypt |
| **SOPS** | File-level encryption, decrypted at apply time |
| **Workload identity** | Best of all: no secret to deliver |

Also enable **encryption at rest** for etcd, or a Kubernetes Secret is stored in plaintext on the control plane's disk.

## Rotation

A secret that has never been rotated is a secret you cannot revoke without an outage, which means you will hesitate during an incident.

Practical rotation without downtime uses **two valid credentials at once**:

1. Create a second credential
2. Deploy the new one, so both are in use
3. Confirm nothing is still using the old one, using access logs
4. Revoke the old one

That sequence is why secrets managers support versions, and why credential systems support multiple active keys.

Rotate immediately, not on schedule, when someone with access leaves, a secret appears somewhere it should not, or a system is suspected of compromise.

## What to do when one leaks

Order matters:

1. **Revoke it.** Not later, now. A rotated-but-not-revoked credential is still valid.
2. **Assess the blast radius**: what could that credential reach?
3. **Check the audit logs** for use you did not expect.
4. **Then** clean up the exposure: rewrite history, remove the file, fix the process.

Step 4 is the one people do first, and it is the least urgent. Removing a secret from a public repository does not help if someone already copied it.

## Practical checklist

- [ ] No secrets in source control, enforced by pre-commit hooks and repository secret scanning
- [ ] Secrets stored in a secrets manager, not in files or CI variables
- [ ] Workload identity used wherever the platform supports it
- [ ] Access scoped per service, not one shared credential
- [ ] Audit logging on, and monitored
- [ ] Rotation possible without downtime, and tested
- [ ] Kubernetes Secrets backed by a real manager, with etcd encryption at rest
- [ ] Secrets absent from application logs, error messages, and crash dumps
- [ ] A written procedure for a leaked credential, starting with revoke

## What to look at next

- **[IAM explained](./iam-explained.md)** - the identity model workload identity builds on
- **[TLS and HTTPS](./tls-and-https.md)** - certificates are secrets with their own lifecycle
- **[Terraform explained](./terraform-explained.md)** - and why state files must be treated as secret
- **[Zero trust architecture](../../resources/architecture-patterns/zero-trust-architecture.md)**
- **[Agent and tool security](../../resources/ai-security/agent-security.md)** - why AI agents must never hold credentials in prompts
