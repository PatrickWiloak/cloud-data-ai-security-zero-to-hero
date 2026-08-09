---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 9 min
---

# 04 - Security operations

**Domain 4: Security Operations (18%)**

---

## Data handling

The data lifecycle: **create, store, use, share, archive, destroy.**

**Classification** assigns a sensitivity level so that handling requirements follow the data. Commercial schemes commonly use Public, Internal, Confidential, Restricted; government schemes use Unclassified, Confidential, Secret, Top Secret.

**Labelling** marks the data with its classification so people and systems can apply the right handling.

**Roles**:
- **Data owner** - accountable for the data, decides classification and who may access it
- **Data custodian** - implements the controls the owner specifies, typically IT
- **Data processor** - processes data on behalf of the controller
- **Data subject** - the individual the personal data is about

**Retention**: keep data only as long as required by business need or regulation. Keeping it longer increases breach exposure and legal discovery scope.

**Destruction**, by increasing assurance:
- **Deletion** - removes the pointer; data is recoverable
- **Overwriting** (clearing) - writes over the data
- **Degaussing** - destroys magnetic media with a strong magnetic field; ineffective on solid state
- **Cryptographic erasure** - destroy the encryption key so the ciphertext is unrecoverable
- **Physical destruction** - shredding, incineration, pulverizing. Highest assurance

---

## Cryptography basics

| Type | Keys | Speed | Used for |
|---|---|---|---|
| **Symmetric** | One shared key | Fast | Bulk data encryption (AES) |
| **Asymmetric** | Public and private key pair | Slow | Key exchange, digital signatures (RSA, ECC) |
| **Hashing** | None | Fast | Integrity, password storage (SHA-256) |

Key points the exam tests:
- **Hashing is one way.** It provides **integrity**, not confidentiality, and it cannot be reversed. This is why passwords are hashed (with a **salt**) rather than encrypted
- **Symmetric** is efficient but requires securely distributing the shared key
- **Asymmetric** solves key distribution. Encrypt with the recipient's **public** key so only their **private** key can decrypt
- A **digital signature** works the other way: sign with your **private** key, and anyone can verify with your **public** key. This provides authenticity, integrity, and **non-repudiation**
- Real systems combine them: asymmetric to exchange a symmetric key, then symmetric for the data
- **Encryption at rest** protects stored data; **encryption in transit** protects data moving across a network
- **PKI** (public key infrastructure) issues and manages certificates; a **certificate authority** vouches for the binding between a public key and an identity

---

## Logging and monitoring

Record what happens so it can be reviewed and investigated.

- **What to log**: authentication attempts, authorization failures, administrative actions, configuration changes, and data access
- **SIEM** (security information and event management) centralizes logs, correlates events across sources, and raises alerts
- **Log protection**: logs must be tamper-resistant and access-controlled, because an attacker's first move is often to clear them
- **Time synchronization** (NTP) matters, because correlating events across systems requires consistent timestamps
- **Retention** must satisfy the longest applicable regulatory requirement

---

## Configuration management

- **Inventory** - you cannot protect what you do not know you have
- **Baseline** - the approved secure configuration for a system type
- **Hardening** - removing unnecessary services, accounts, and software; changing default credentials
- **Patch management** - identify, test, deploy, and verify updates
- **Change management** - request, review, approve, implement, and document changes. It exists because most outages are caused by change
- **Version control** - track what changed, when, and by whom

---

## Policies and awareness

Common policies the exam names:
- **Acceptable use policy (AUP)** - how organizational systems may be used
- **Bring your own device (BYOD)** - rules for personal devices accessing organizational data
- **Password policy** - complexity, length, rotation, reuse
- **Privacy policy** - how personal data is handled
- **Change management policy**
- **Data handling policy**

**Security awareness training** addresses the human layer: recognizing phishing and social engineering, reporting incidents, handling data, and clean desk practice. **Phishing simulations** measure and reinforce it. Training is an **administrative, preventive** control, and it is the primary defense against social engineering, since technical controls cannot fully address it.

---

## Key terms

- **Data classification** - assigning a sensitivity level so handling requirements follow the data
- **Data owner** - the role accountable for data, deciding its classification and who may access it
- **Data custodian** - the role implementing the controls the data owner specifies
- **Data retention** - the policy governing how long data is kept before disposal
- **Degaussing** - destroying data on magnetic media with a strong magnetic field
- **Cryptographic erasure** - rendering data unrecoverable by destroying the key that encrypts it
- **Symmetric encryption** - encryption using a single shared key, fast and suited to bulk data
- **Asymmetric encryption** - encryption using a public and private key pair, solving key distribution
- **Hashing** - a one-way function producing a fixed-length value, used for integrity and password storage
- **Salt** - random data added before hashing a password so identical passwords hash differently
- **Digital signature** - data signed with a private key, providing authenticity, integrity, and non-repudiation
- **PKI** - public key infrastructure, the system issuing and managing digital certificates
- **Certificate authority** - the trusted entity vouching for the binding between a public key and an identity
- **SIEM** - security information and event management, centralizing and correlating log data
- **Baseline** - the approved secure configuration for a given system type
- **Hardening** - reducing a system's attack surface by removing unnecessary services and defaults
- **Change management** - the controlled process for requesting, approving, and documenting changes
- **Acceptable use policy** - the policy defining how organizational systems may be used
- **Security awareness training** - an administrative preventive control addressing the human attack surface

---

## Related

- [Notes 05: BC, DR, and incident response](./05-bcdr-and-incident-response.md)
- [Scenarios](../scenarios.md) - scenario 7
