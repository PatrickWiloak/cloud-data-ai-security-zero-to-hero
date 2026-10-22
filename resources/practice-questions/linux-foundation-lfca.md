---
last-updated: 2026-10-22
difficulty: beginner
---

# Linux Foundation Certified IT Associate (LFCA) - Practice Questions

30 questions for LFCA prep, weighted across Linux fundamentals, system administration, and cloud computing (20% each), then DevOps and SRE (16%), security and networking (12% each).

LFCA is multiple choice and entry-level. It covers breadth across IT, not depth in any one area.

> **Cert page:** [exams/linux-foundation/lfca/](../../exams/linux-foundation/lfca/)

---

### Question 1
**Scenario:** Which command shows the current working directory?

A. `whoami`
B. `cd`
C. `pwd` (print working directory)
D. `ls -la`, which lists every file in the directory along with its permissions

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `pwd` prints the working directory. `ls` lists its contents, `cd` changes it, and `whoami` prints your username. These four are the orientation commands worth having reflexive.
</details>

---

### Question 2
**Scenario:** A file has permissions `-rw-r--r--`. Who can modify it?

A. The owner only
B. Nobody
C. Everyone
D. The owner and group

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Read the string in three triplets after the type character: owner `rw-`, group `r--`, others `r--`. Only the owner has write. In octal this is 644, which is the standard permission for a regular data file.
</details>

---

### Question 3
**Scenario:** Which is the correct description of an IP subnet mask of /24?

A. 24 subnets, one for each bit of the mask, each holding the same number of addresses
B. The first 24 bits are the network portion, leaving 256 addresses, of which 254 are usable
C. 24 usable hosts, one per bit of the mask, with the rest reserved for the network
D. IPv6 only, since the prefix length notation is not used for IPv4 addressing

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** CIDR notation counts network bits. A /24 leaves 8 host bits, so 2^8 = 256 addresses, minus the network and broadcast addresses, leaving 254 usable. This arithmetic shows up constantly in both cloud and on-premises networking.
</details>

---

### Question 4
**Scenario:** What is the main advantage of infrastructure as code?

A. Infrastructure is defined in version-controlled files, so changes are reviewable and repeatable
B. It removes the need for testing, because the declared state is guaranteed to match what is actually deployed in the cloud
C. It eliminates cloud costs by shutting down every undeclared resource
D. It runs faster than a GUI because the provider's API handles scripted calls faster than console ones do in every case

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The value is that infrastructure gets the same review, history, and rollback story as application code, and that a new environment can be recreated identically. Speed is a side effect. It does not remove testing, and it does not change pricing.
</details>

---

### Question 5
**Scenario:** Which cloud service model gives you the operating system to manage but not the physical hardware?

A. FaaS, where you upload single functions that run on demand with no server to manage
B. IaaS, where you rent virtual machines and patch the OS yourself
C. PaaS, where the provider manages the OS and runtime and you deploy only application code
D. SaaS, where the provider runs the finished application and you use it through a browser

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** IaaS gives you virtual machines: you own the OS, patching, and everything above. PaaS abstracts the OS so you deploy applications. SaaS is a finished application. FaaS runs individual functions with no server management at all.
</details>

---

### Question 6
**Scenario:** A git workflow requires a change to be reviewed before entering the main branch.

A. Create a branch, push it, and open a pull request for review before merging
B. Commit directly to main, then ask a teammate to read the commit after it has been pushed
C. Email a patch to the whole team and merge it into main when nobody replies in two days
D. Use `git push --force` to publish the branch to main, which triggers a mandatory review

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Branch, push, review, merge is the standard flow, and branch protection rules on main enforce it. Committing straight to main skips review. Force pushing rewrites shared history and is destructive on a protected branch.
</details>

---

### Question 7
**Scenario:** What does DNS do?

A. Routes packets between networks using each router's forwarding table
B. Encrypts web traffic between the browser and the server
C. Resolves human-readable names to IP addresses
D. Assigns IP addresses to devices when they join a network

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** DNS is the name-to-address lookup. DHCP assigns addresses, routing moves packets, and TLS encrypts traffic. Mixing DNS and DHCP is a common beginner error worth being firm about.
</details>

---

### Question 8
**Scenario:** Which practice best describes continuous integration?

A. Monitoring servers and alerting the team whenever a deployment fails in production
B. Merging changes to a shared branch often, with an automated build and test on every merge
C. Writing documentation continuously as part of every commit, with a build step that publishes it
D. Deploying to production several times a day, with each change released as soon as it is merged

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** CI is about integrating early and catching breakage automatically. Frequent production deployment is continuous delivery or deployment, which builds on CI but is a separate practice. The automated verification is what makes CI more than "merging often."
</details>

---

### Question 9
**Scenario:** A password policy should reduce the impact of a leaked credential most effectively.

A. Requiring multi-factor authentication
B. Forbidding password managers, so passwords cannot be copied out of a vault
C. Requiring a longer password of twenty characters, which stays useful if it leaks
D. Rotating passwords monthly, so a leaked credential expires before it can be used

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** MFA means a stolen password alone is not enough, which directly addresses leakage. Length helps against guessing but not against a leak. Frequent forced rotation pushes people toward predictable variations and is no longer recommended by NIST. Blocking password managers makes things worse.
</details>

---

### Question 10
**Scenario:** What is the purpose of a service level objective (SLO)?

A. An incident report written after an outage, listing its causes, the timeline, and the follow-up work
B. An internal target for a measured reliability indicator, which sets the error budget
C. A monitoring dashboard showing the current error rate and latency
D. A legal contract with a customer that sets refund terms when availability drops under target

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** An SLI is the measurement, the SLO is the target for it, and an SLA is the external contract with consequences. The practical value of an SLO is the error budget it creates: when the budget is spent, reliability work outranks features.
</details>

---

### Question 11
**Scenario:** Which command would show disk space usage per filesystem?

A. `free -h`
B. `lsblk`
C. `df -h`, which reports used and free space for each mounted filesystem
D. `du -sh` run on a path, which adds up the size of all files and folders beneath it

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `df` reports free and used space per mounted filesystem, and `-h` makes it human-readable. `du` sums the size of files under a path, which is how you find what filled the disk after `df` tells you which one is full. `free` is memory and `lsblk` lists block devices.
</details>

---

### Question 12
**Scenario:** What does a load balancer accomplish?

A. It encrypts database storage so that backend servers hold only ciphertext on disk and in backups
B. It compresses data on the wire so that fewer bytes are sent from each backend server to the client
C. It stores static files in a cache so the backend servers never receive requests for them
D. It distributes incoming requests across multiple backend servers and drops unhealthy ones from rotation

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Distribution plus health checking is the core function, which is what turns several servers into one available service. Compression and TLS termination are common extras but not the purpose. Static file storage is a CDN or object store concern.
</details>

---

### Question 13
**Scenario:** Which best describes a container image?

A. A running process created from the application, with its own PID namespace
B. A virtual machine disk with its own kernel, booted by a hypervisor
C. A read-only, layered package of an application and its dependencies, from which any number of containers can be started
D. A configuration file that tells the runtime which ports and volumes to use

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The image is the immutable artifact; the container is a running instance of it. Layers let images share common bases and make pulls incremental. Containers use the host kernel, which is the key difference from a VM disk image.
</details>

---

### Question 14
**Scenario:** Backups exist but have never been restored. What is the risk?

A. Backups will expire after thirty days unless someone renews the retention setting in the console for each vault and region
B. Backups will be too large to store once the data grows, so the job eventually fails to start
C. None, because backups run automatically and a completed job is proof that the data can be restored in time, so no restore test is needed
D. An untested backup is an assumption, not a recovery capability; failures typically surface in a real incident

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Restore testing is the control, not backup completion. Silent failures include incomplete snapshots, missing encryption keys, and formats no current tool can read. Schedule restores and measure how long they take, because recovery time is part of the requirement.
</details>

---

### Question 15
**Scenario:** Which principle should guide granting access to a system?

A. Give broad access to reduce tickets, then remove it only if an audit finds a problem
B. Share one admin account for simplicity, with the password kept in the team's wiki
C. Grant access permanently once approved, so users never have to request it again, whatever their role later becomes
D. Least privilege: grant the minimum permissions needed for the role, and review them periodically

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Least privilege limits the blast radius of any compromised or misused account. Shared admin accounts destroy accountability because you cannot attribute actions. Permanent grants accumulate into privilege creep, which is why periodic access review exists.
</details>

---

### Question 16
**Scenario:** A junior admin needs to see every entry in a directory, including hidden dotfiles such as `.bashrc`, along with permissions and owners.

A. `ls -R`, which recurses into every subdirectory
B. `ls -lh`, which prints sizes in human-readable units
C. `ls -la`, which adds hidden entries to the long listing
D. `ls -t`, which sorts the listing by modification time

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `-l` gives the long format (permissions, owner, group, size, date) and `-a` includes entries whose names start with a dot, which `ls` hides by default. `-lh` gives the long format but still hides dotfiles. `-R` recurses without showing hidden files or details, and `-t` only changes the sort order.

**Key Concept:** [ls(1) manual page](https://man7.org/linux/man-pages/man1/ls.1.html)
</details>

---

### Question 17
**Scenario:** On a Linux system that follows the Filesystem Hierarchy Standard, an admin must edit the system-wide SSH server configuration. Which directory tree holds it?

A. `/var`, for logs, spools, and other variable data
B. `/etc`, for host-specific system configuration
C. `/opt`, for add-on application software packages
D. `/usr/bin`, for most user command binaries

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The FHS reserves `/etc` for host-specific configuration, so the SSH daemon reads `/etc/ssh/sshd_config`. `/var` holds data that changes while the system runs, such as logs under `/var/log`. `/opt` is for self-contained add-on packages, and `/usr/bin` holds executables, not their configuration.

**Key Concept:** [FHS 3.0: /etc](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch03s07.html)
</details>

---

### Question 18
**Scenario:** A nightly script must add its output to the end of `app.log` without erasing what earlier runs wrote.

A. `cmd > app.log`, which redirects standard output there
B. `cmd 2> app.log`, which sends only standard error there
C. `cmd < app.log`, which feeds the file in as standard input
D. `cmd >> app.log`, which appends standard output to it

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** `>>` opens the file in append mode, creating it if needed, so earlier content survives. A single `>` truncates the file first, so each run would wipe the previous log. `2>` redirects only standard error (and also truncates), and `<` reads from the file rather than writing to it.

**Key Concept:** [Bash manual: Redirections](https://www.gnu.org/software/bash/manual/html_node/Redirections.html)
</details>

---

### Question 19
**Scenario:** An Ubuntu server needs the `nginx` package installed from the configured repositories, with its dependencies resolved automatically.

A. `sudo apt install nginx`
B. `sudo dpkg -i nginx`
C. `sudo rpm -i nginx`
D. `sudo dnf install nginx`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** On Debian and Ubuntu, `apt` fetches packages from the configured repositories and resolves dependencies. `dpkg -i` installs a local `.deb` file you already have and does not download dependencies. `rpm` and `dnf` are the Red Hat family tools (RHEL, Fedora, Rocky) and are not the package manager on Ubuntu.

**Key Concept:** [apt(8) manual page](https://manpages.debian.org/bookworm/apt/apt.8.en.html)
</details>

---

### Question 20
**Scenario:** A server feels slow. The admin wants a live, continuously refreshing view of which processes are using the most CPU and memory right now.

A. `ps aux`, which prints a one-time process snapshot
B. `df -h`, which prints free space on each filesystem
C. `top`, which refreshes a sorted process view live
D. `uptime`, which prints the load averages once

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** `top` redraws every few seconds and sorts by CPU by default, so you can watch the culprit in real time. `ps aux` lists the same processes but only once. `uptime` shows load averages without naming any process, and `df -h` is about disk space, not CPU or memory.

**Key Concept:** [top(1) manual page](https://man7.org/linux/man-pages/man1/top.1.html)
</details>

---

### Question 21
**Scenario:** Several admins share a server. Each must be able to run privileged commands, and the security team needs a record of who ran what.

A. Share the root password and have admins log in as root directly
B. Grant each admin `sudo` rights and keep their own accounts
C. Add every admin to the same shared `admin` login account
D. Set the setuid bit on the shell so any user gets root

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** `sudo` lets each person elevate with their own credentials and logs each command against their username, which preserves accountability. A shared root password or shared login makes every action anonymous. A setuid shell would hand root to every user on the system, which is a severe security hole.

**Key Concept:** [sudo manual](https://www.sudo.ws/docs/man/sudo.man/)
</details>

---

### Question 22
**Scenario:** A retail site's cloud environment adds web servers automatically during a holiday spike and removes them when traffic drops, so the company pays only for what it uses.

A. High availability
B. Multi-tenancy
C. Fault tolerance
D. Rapid elasticity

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** NIST lists rapid elasticity as an essential characteristic of cloud computing: capacity is provisioned and released automatically to match demand, in both directions. High availability and fault tolerance are about surviving failures, not matching load. Multi-tenancy describes many customers sharing pooled infrastructure.

**Key Concept:** [NIST SP 800-145: The NIST Definition of Cloud Computing](https://csrc.nist.gov/pubs/sp/800/145/final)
</details>

---

### Question 23
**Scenario:** A team runs Linux virtual machines on an IaaS provider. A critical vulnerability is announced in the guest operating system's kernel.

A. The customer patches the guest OS on its own instances
B. The provider patches it, because it owns the instances
C. Nobody needs to act, because IaaS kernels are immutable
D. The hardware vendor patches it through a firmware update

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Under the shared responsibility model for IaaS, the provider secures the physical hosts, network, and hypervisor, while the customer owns the guest OS, its patches, and everything above it. The provider does not patch customer instances. Guest kernels are not immutable, and firmware updates do not fix a guest OS vulnerability.

**Key Concept:** [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)
</details>

---

### Question 24
**Scenario:** A small piece of code must run each time a file is uploaded. The team wants no servers to manage and to pay only while the code is running.

A. A dedicated bare metal server running a polling script
B. A virtual machine left running with a cron job every minute
C. A serverless function triggered by the upload event
D. A container cluster sized for the busiest expected day

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Serverless functions run in response to events, scale automatically, and bill for invocations and execution time, with no servers to patch. A VM or bare metal server bills around the clock and needs OS management. A cluster sized for peak load wastes capacity most of the time and still needs to be operated.

**Key Concept:** [What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
</details>

---

### Question 25
**Scenario:** A team wants to release a new version with near-zero downtime and the ability to switch back instantly if it misbehaves.

A. Rolling deployment, replacing servers one at a time in place
B. Blue-green deployment, flipping traffic between two environments
C. Big-bang deployment, updating all servers during a maintenance window
D. Recreate deployment, stopping the old version before starting the new

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Blue-green keeps the old environment intact while the new one takes traffic, so rollback is just switching the router back. A rolling deployment avoids downtime, but rolling back means rolling again across every server. Big-bang and recreate both involve downtime and have no instant fallback.

**Key Concept:** [BlueGreenDeployment (Martin Fowler)](https://martinfowler.com/bliki/BlueGreenDeployment.html)
</details>

---

### Question 26
**Scenario:** A service has a 99.9% monthly availability SLO. By mid-month, outages have already used all the allowed downtime.

A. Lower the SLO to 99% so the service is back in compliance
B. Keep shipping features, since the SLO resets next month
C. Add more monitoring dashboards and continue as normal
D. Pause risky releases and focus on reliability work

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The 0.1% the SLO permits is the error budget. When it is spent, SRE practice is to slow or freeze risky changes and invest in reliability until the budget recovers. Lowering the target hides the problem from users who still see failures. Shipping as usual or only adding dashboards ignores the signal the budget exists to give.

**Key Concept:** [Google SRE book: Embracing Risk](https://sre.google/sre-book/embracing-risk/)
</details>

---

### Question 27
**Scenario:** A developer must start work on a new feature in Git without touching `main`, creating a branch and switching to it in one step.

A. `git switch -c feature-login`
B. `git merge feature-login`
C. `git commit -m feature-login`
D. `git push origin feature-login`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `git switch -c` creates the branch and checks it out in one command (the older equivalent is `git checkout -b`). `git merge` combines an existing branch into the current one, `git commit` records changes on the current branch, and `git push` publishes a branch that must already exist locally.

**Key Concept:** [git-switch documentation](https://git-scm.com/docs/git-switch)
</details>

---

### Question 28
**Scenario:** An attacker phishes an employee's password for the company VPN. Which control most directly stops the attacker from logging in with it?

A. A longer minimum password length policy
B. Encrypting the laptop's hard drive
C. Multi-factor authentication on the VPN
D. A screen lock after five minutes idle

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** MFA requires a second factor the attacker does not have, so a stolen password alone is not enough. A longer password does not help once the password itself has been handed over. Disk encryption protects a lost device, and a screen lock protects an unattended one; neither affects a remote VPN login.

**Key Concept:** [CISA: More than a Password (MFA)](https://www.cisa.gov/MFA)
</details>

---

### Question 29
**Scenario:** A web application must store user passwords so that a stolen copy of the database does not reveal them.

A. Encrypted with a key kept in the same database
B. Hashed with a salted, slow algorithm such as Argon2 or bcrypt
C. Base64-encoded so they are unreadable to a casual viewer
D. Stored in plain text in a table only admins can read

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A salted, deliberately slow one-way hash means the application can verify a password without ever storing it, and cracking stolen hashes becomes expensive. Encryption is reversible, and a key stored beside the data is stolen with it. Base64 is an encoding, not protection, and plain text relies entirely on access control never failing.

**Key Concept:** [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
</details>

---

### Question 30
**Scenario:** A firewall in front of a new web server must allow encrypted browser traffic using the standard port.

A. TCP 22
B. TCP 80
C. UDP 53
D. TCP 443

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** HTTPS (HTTP over TLS) uses TCP port 443 by default. Port 80 is unencrypted HTTP, port 22 is SSH, and UDP 53 is DNS. Knowing the common well-known ports is basic networking literacy for reading and writing firewall rules.

**Key Concept:** [IANA Service Name and Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)
</details>

---

## Where to go deeper

- [LFCA cert page](../../exams/linux-foundation/lfca/) - notes, practice plan, strategy
- [LFCS practice questions](./linux-foundation-lfcs.md) - the hands-on next step
- [Day One](../../learn/day-one/) - terminal, git, HTTP, servers from zero
- [What is cloud computing?](../../learn/concepts/what-is-cloud-computing.md) - the cloud domain in plain English
- **[📖 LFCA exam page](https://training.linuxfoundation.org/certification/linux-foundation-certified-it-associate/)** - official domains and logistics
