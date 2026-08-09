---
last-updated: 2026-08-09
difficulty: intermediate
---

# HashiCorp Packer Associate (003) - Practice Questions

15 questions for Packer Associate prep across templates, builders, provisioners, post-processors, variables, and HCP Packer.

> **Cert page:** [exams/hashicorp/packer-associate/](../../exams/hashicorp/packer-associate/)

---

### Question 1
**Scenario:** What does Packer produce?

A. Running infrastructure
B. Machine images (AMIs, VM images, container images) built from a template
C. Kubernetes manifests
D. Terraform state

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Packer builds artifacts; Terraform provisions infrastructure from them. Keeping that split clear is the point of the immutable infrastructure workflow: bake the image once, then deploy it many times without configuring machines after launch.
</details>

---

### Question 2
**Scenario:** A single template must produce an AWS AMI and an Azure image from the same configuration.

A. Two separate templates
B. One build block with multiple sources, so both are produced in parallel from the same provisioners
C. It is not supported
D. Run Packer twice manually

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A build block can reference several sources, and Packer runs them concurrently through the same provisioning steps. This is what keeps multi-cloud golden images genuinely identical rather than approximately similar.
</details>

---

### Question 3
**Scenario:** Software must be installed into the image during the build.

A. A provisioner block, such as shell, file, Ansible, or PowerShell
B. A post-processor
C. A source block
D. A variable

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Provisioners run inside the temporary build instance. Post-processors act on the resulting artifact, for example tagging, compressing, or uploading it. Source blocks define what to start from and where to build.
</details>

---

### Question 4
**Scenario:** Which HCL block defines the plugins a template requires?

A. `packer { required_plugins { ... } }`
B. `build`
C. `source`
D. `locals`

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Since plugins were split out of the core binary, templates declare what they need with version constraints, and `packer init` installs them. Forgetting this block is the most common first error when moving a template from an older Packer version.
</details>

---

### Question 5
**Scenario:** A secret must be passed into a build without appearing in the template.

A. Hard-code it
B. A sensitive variable supplied by environment variable, a var file outside version control, or fetched from Vault
C. A comment
D. A local value

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Marking a variable `sensitive = true` keeps it out of Packer's log output, and sourcing it from the environment or Vault keeps it out of the repository. Anything written into the template is in git history forever.
</details>

---

### Question 6
**Scenario:** Build credentials should not be baked into the image.

A. They will be removed automatically
B. Clean up build-time credentials, SSH keys, and history in a final provisioner step, and verify the resulting image
C. Ignore it
D. Encrypt the image only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Anything present on disk at snapshot time ships in the image and to everyone who launches it. Cloud-init and sysprep handle some of this, but build artifacts such as temporary keys, package caches, and shell history need explicit removal.
</details>

---

### Question 7
**Scenario:** The same image must be validated before it is published.

A. `packer validate` for syntax, plus a test provisioner or an external tool such as InSpec or Goss to verify the built image
B. Only `packer build`
C. Manual login
D. Nothing is available

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** `validate` catches template errors before spending build time, but it says nothing about whether the software actually installed. Running a compliance or smoke test as the last provisioner is what turns "the build succeeded" into "the image is correct."
</details>

---

### Question 8
**Scenario:** Build output should be tagged and registered so downstream Terraform can find it.

A. A manifest post-processor writing artifact IDs, or HCP Packer registry with channels
B. Copy the ID by hand
C. Hard-code the AMI ID in Terraform
D. Use `latest` tags

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** HCP Packer tracks image versions and channels, and Terraform's HCP Packer data source resolves a channel such as `production` to a concrete image ID. Hard-coded IDs are how estates end up running images nobody can rebuild.
</details>

---

### Question 9
**Scenario:** A build fails halfway and leaves a running instance.

A. It always cleans up
B. Packer normally cleans up on failure; use `-on-error=abort` or `ask` to keep the instance for debugging, and check for orphans after crashes
C. Terminate the whole account
D. Nothing can be done

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The default cleanup is what keeps builds from leaking resources, but it also destroys the evidence. `-on-error=ask` pauses so you can SSH in and see what the provisioner actually hit, which is the fastest way to debug a failing step.
</details>

---

### Question 10
**Scenario:** Multiple similar images differ only in a version number.

A. Duplicate the template
B. Use input variables and locals, with `-var` or a `.pkrvars.hcl` file per variant
C. Edit the template each time
D. Use separate repositories

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Parameterization keeps one template as the source of truth. Duplicated templates drift, and the drift is usually discovered when one variant fails to build months later for a reason the other one already fixed.
</details>

---

### Question 11
**Scenario:** What is the benefit of immutable infrastructure built with Packer?

A. Cheaper storage
B. Servers are replaced rather than modified, so configuration drift is eliminated and rollback means redeploying a previous image
C. No monitoring needed
D. Faster networking

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Configuration drift is the thing that makes long-lived servers unreproducible, and replacing rather than patching removes the cause. Rollback also becomes trivial, because the previous image still exists and is known good.
</details>

---

### Question 12
**Scenario:** Build times are long because every build installs the full base software stack.

A. Accept it
B. Use a layered approach: build a base image, then build application images from it, so common steps run once
C. Remove provisioners
D. Use a larger instance only

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A base image rebuilt weekly plus thin application images built on every commit gives fast application builds and a controlled patching cadence for the shared layer. It is the same reasoning as container base images.
</details>

---

### Question 13
**Scenario:** A shell provisioner needs to run as root.

A. `execute_command` with sudo, or the `elevated_user` settings on Windows
B. Run Packer as root locally
C. It cannot be done
D. Change the source image

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Privilege applies inside the build instance, not on the workstation running Packer. The `execute_command` setting controls how the script is invoked there, and on Windows the elevated user settings serve the same purpose for tasks needing full privileges.
</details>

---

### Question 14
**Scenario:** Golden images must be patched on a regular cadence.

A. Patch running servers instead
B. Rebuild images on a schedule in CI, run the validation suite, publish to a channel, and roll instances onto the new version
C. Rebuild only when something breaks
D. Ignore patching

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** In an immutable model the pipeline is the patching mechanism, which means the rebuild has to be automated and routine or the estate falls behind. Publishing to a channel decouples building the image from adopting it.
</details>

---

### Question 15
**Scenario:** Packer and Terraform in the same workflow.

A. They are alternatives
B. Packer builds the image, Terraform provisions infrastructure that uses it, with the image ID passed by data source or variable
C. Terraform builds images
D. Packer deploys infrastructure

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The separation keeps each tool doing what it is good at: Packer produces an artifact, Terraform manages the lifecycle of resources referencing it. Terraform provisioners exist but are documented as a last resort precisely because baking is the better answer.
</details>

---

## Where to go deeper

- [Packer Associate cert page](../../exams/hashicorp/packer-associate/) - notes, practice plan, strategy
- [Terraform Associate practice questions](./hashicorp-terraform-associate.md) - the deployment half of the workflow
- [Terraform explained](../../learn/concepts/terraform-explained.md) - IaC in plain English
- **[📖 Packer documentation](https://developer.hashicorp.com/packer/docs)** - primary source
