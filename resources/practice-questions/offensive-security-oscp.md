---
last-updated: 2026-08-09
difficulty: advanced
---

# OSCP (PEN-200) - Practice Questions

15 questions on the concepts behind the OSCP: enumeration, exploitation, privilege escalation, lateral movement, Active Directory attacks, and reporting.

OSCP is a 24-hour hands-on practical exam with a report, not a multiple-choice test. These questions check conceptual understanding and methodology; the exam itself is passed on the keyboard in the labs. Everything here assumes an authorized engagement or a lab you own.

> **Cert page:** [exams/offensive-security/oscp-pen-200/](../../exams/offensive-security/oscp-pen-200/)

---

### Question 1
**Scenario:** What determines success on the OSCP more than any other factor?

A. Memorizing exploits
B. Thorough enumeration, since most failures are missed information rather than missing exploitation skill
C. Fast typing
D. Tool count

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** "Try harder" in practice means enumerate more. A stuck box is usually a service, a virtual host, a directory, or a credential reuse path that was never found, not an exploit that failed.
</details>

---

### Question 2
**Scenario:** An initial port scan shows ports 22, 80, and 445 open.

A. Attack port 22 with a password list
B. Enumerate each service in depth: web content and technologies on 80, SMB shares and versions on 445, and SSH version and any known issues on 22
C. Run every exploit available
D. Move to the next host

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Service enumeration precedes exploitation, and web applications usually carry the most surface. Brute forcing SSH first is slow, noisy, and rarely the intended path in a lab designed around discoverable information.
</details>

---

### Question 3
**Scenario:** A web application has a file upload feature.

A. Nothing to test
B. Test for unrestricted upload leading to code execution: extension and content type handling, where files are stored, and whether the storage path is executable
C. Upload a large file
D. Only test authentication

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Both halves have to be true for it to matter: the file must bypass validation and it must land somewhere the server will execute it. Blocklist-based extension filtering is the common weakness, since alternate extensions and case variations slip through.
</details>

---

### Question 4
**Scenario:** A low-privilege shell has been obtained on a Linux host.

A. Give up
B. Enumerate systematically: kernel and distribution version, SUID and SGID binaries, sudo rights, cron jobs, writable pa