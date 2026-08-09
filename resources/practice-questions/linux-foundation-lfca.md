---
last-updated: 2026-08-09
difficulty: beginner
---

# Linux Foundation Certified IT Associate (LFCA) - Practice Questions

15 questions for LFCA prep, weighted across Linux fundamentals, system administration, and cloud computing (20% each), then DevOps and SRE (16%), security and networking (12% each).

LFCA is multiple choice and entry-level. It covers breadth across IT, not depth in any one area.

> **Cert page:** [exams/linux-foundation/lfca/](../../exams/linux-foundation/lfca/)

---

### Question 1
**Scenario:** Which command shows the current working directory?

A. `ls`
B. `pwd`
C. `cd`
D. `whoami`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `pwd` prints the working directory. `ls` lists its contents, `cd` changes it, and `whoami` prints your username. These four are the orientation commands worth having reflexive.
</details>

---

### Question 2
**Scenario:** A file has permissions `-rw-r--r--`. Who can modify it?

A. Everyone
B. The owner only
C. The owner and group
D. Nobody

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Read the string in three triplets after the type character: owner `rw-`, group `r--`, others `r--`. Only the owner has write. In octal this is 644, which is the standard permission for a regular data file.
</details>

---

### Question 3
**Scenario:** Which is the correct description of an IP subnet mask of /24?

A. 24 usable hosts
B. The first 24 bits are the network portion, leaving 256 addresses of which 254 are usable
C. 24 subnets
D. IPv6 only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** CIDR notation counts network bits. A /24 leaves 8 host bits, so 2^8 = 256 addresses, minus the network and broadcast addresses, leaving 254 usable. This arithmetic shows up constantly in both cloud and on-premises networking.
</details>

---

### Question 4
**Scenario:** What is the main advantage of infrastructure as code?

A. It runs faster than a GUI
B. Infrastructure is defined in version-controlled files, so changes are reviewable, repeatable, and auditable
C. It removes the need for testing
D. It eliminates cloud costs

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The value is that infrastructure gets the same review, history, and rollback story as application code, and that a new environment can be recreated identically. Speed is a side effect. It does not remove testing, and it does not change pricing.
</details>

---

### Question 5
**Scenario:** Which cloud service model gives you the operating system to manage but not the physical hardware?

A. SaaS
B. PaaS
C. IaaS
D. FaaS

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** IaaS gives you virtual machines: you own the OS, patching, and everything above. PaaS abstracts the OS so you deploy applications. SaaS is a finished application. FaaS runs individual functions with no server management at all.
</details>

---

### Question 6
**Scenario:** A git workflow requires a change to be reviewed before entering the main branch.

A. Commit directly to main
B. Create a branch, push it, and open a pull request for review before merging
C. Use `git push --force`
D. Email a patch

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Branch, push, review, merge is the standard flow, and branch protection rules on main enforce it. Committing straight to main skips review. Force pushing rewrites shared history and is destructive on a protected branch.
</details>

---

### Question 7
**Scenario:** What does DNS do?

A. Assigns IP addresses to devices
B. Resolves human-readable names to IP addresses
C. Routes packets between networks
D. Encrypts web traffic

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** DNS is the name-to-address lookup. DHCP assigns addresses, routing moves packets, and TLS encrypts traffic. Mixing DNS and DHCP is a common beginner error worth being firm about.
</details>

---

### Question 8
**Scenario:** Which practice best describes continuous integration?

A. Deploying to production several times a day
B. Merging changes to a shared branch frequently, with automated build and test on every merge
C. Writing documentation continuously
D. Monitoring servers

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** CI is about integrating early and catching breakage automatically. Frequent production deployment is continuous delivery or deployment, which builds on CI but is a separate practice. The automated verification is what makes CI more than "merging often."
</details>

---

### Question 9
**Scenario:** A password policy should reduce the impact of a leaked credential most effectively.

A. Requiring a longer password
B. Requiring multi-factor authentication
C. Rotating passwords monthly
D. Forbidding password managers

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** MFA means a stolen password alone is not enough, which directly addresses leakage. Length helps against guessing but not against a leak. Frequent forced rotation pushes people toward predictable variations and is no longer recommended by NIST. Blocking password managers makes things worse.
</details>

---

### Question 10
**Scenario:** What is the purpose of a service level objective (SLO)?

A. A legal contract with a customer
B. An internal target for a measured reliability indicator, used to decide when to prioritize reliability work
C. A monitoring dashboard
D. An incident report

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** An SLI is the measurement, the SLO is the target for it, and an SLA is the external contract with consequences. The practical value of an SLO is the error budget it creates: when the budget is spent, reliability work outranks features.
</details>

---

### Question 11
**Scenario:** Which command would show disk space usage per filesystem?

A. `du -sh`
B. `df -h`
C. `free -h`
D. `lsblk`

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `df` reports free and used space per mounted filesystem, and `-h` makes it human-readable. `du` sums the size of files under a path, which is how you find what filled the disk after `df` tells you which one is full. `free` is memory and `lsblk` lists block devices.
</details>

---

### Question 12
**Scenario:** What does a load balancer accomplish?

A. It compresses data
B. It distributes incoming requests across multiple backend servers and removes unhealthy ones from rotation
C. It stores static files
D. It encrypts databases

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Distribution plus health checking is the core function, which is what turns several servers into one available service. Compression and TLS termination are common extras but not the purpose. Static file storage is a CDN or object store concern.
</details>

---

### Question 13
**Scenario:** Which best describes a container image?

A. A running process
B. A read-only, layered package of an application and its dependencies
C. A virtual machine disk with its own kernel
D. A configuration file

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The image is the immutable artifact; the container is a running instance of it. Layers let images share common bases and make pulls incremental. Containers use the host kernel, which is the key difference from a VM disk image.
</details>

---

### Question 14
**Scenario:** Backups exist but have never been restored. What is the risk?

A. None, backups are automatic
B. An untested backup is an assumption, not a recovery capability, and failures typically surface only during a real incident
C. Backups will expire
D. Backups will be too large

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Restore testing is the control, not backup completion. Silent failures include incomplete snapshots, missing encryption keys, and formats no current tool can read. Schedule restores and measure how long they take, because recovery time is part of the requirement.
</details>

---

### Question 15
**Scenario:** Which principle should guide granting access to a system?

A. Give broad access to reduce support tickets
B. Least privilege: grant the minimum permissions needed for the role, and review them periodically
C. Share one admin account for simplicity
D. Grant access permanently once approved

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Least privilege limits the blast radius of any compromised or misused account. Shared admin accounts destroy accountability because you cannot attribute actions. Permanent grants accumulate into privilege creep, which is why periodic access review exists.
</details>

---

## Where to go deeper

- [LFCA cert page](../../exams/linux-foundation/lfca/) - notes, practice plan, strategy
- [LFCS practice questions](./linux-foundation-lfcs.md) - the hands-on next step
- [Day One](../../learn/day-one/) - terminal, git, HTTP, servers from zero
- [What is cloud computing?](../../learn/concepts/what-is-cloud-computing.md) - the cloud domain in plain English
- **[📖 LFCA exam page](https://training.linuxfoundation.org/certification/linux-foundation-certified-it-associate/)** - official domains and logistics
