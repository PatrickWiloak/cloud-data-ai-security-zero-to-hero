---
last-updated: 2026-10-22
applies-to: GH-200 skills measured as of January 2026, checked 2026-10-22
difficulty: intermediate
---

# Domain 3: Author and Maintain Actions (15-20%)

This domain covers building your own actions: choosing a type, writing `action.yml`, using workflow commands from inside an action, troubleshooting it, and distributing and versioning it. It covers the three skill groups "create and troubleshoot custom actions", "define action structure and metadata" and "distribute and maintain actions".

**[📖 GH-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200)** - the skills list this note follows.
**[📖 Creating actions](https://docs.github.com/en/actions/how-tos/create-and-publish-actions)** - tutorials for each action type.
**[📖 Metadata syntax for GitHub Actions](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax)** - every `action.yml` key.

## Choosing an action type

An action is a reusable unit that a step calls with `uses:`. There are three kinds, and the choice is mostly about where the code runs.

**JavaScript actions** run directly on the runner with the Node.js runtime that the runner ships (`using: node20` or `node24`). They start fast because nothing has to be built, and they work on Linux, Windows and macOS runners. You write them in JavaScript or TypeScript, use the `@actions/*` toolkit, and commit a bundled `dist/` folder (built with a bundler such as `ncc` or `esbuild`) because the runner does not run `npm install` for you. Choose JavaScript when the action must be quick, cross-platform, or talk to the GitHub API.

**Docker container actions** run inside a container the runner builds from a `Dockerfile` or pulls from a registry (`image: docker://ghcr.io/org/tool:1.4`). The container carries its own operating system and tools, so you can write the action in any language and pin exact dependency versions. The costs are start-up time (build or pull on every run, unless the image is prebuilt) and platform: Docker actions run only on Linux runners, and on self-hosted runners they need Docker installed.

**Composite actions** are a list of steps in `action.yml` (`using: composite`). Each step is either `run:` (which must declare `shell:`) or `uses:` another action. They run in the caller's job, so they share its workspace and runner. Choose composite when the "action" is really a repeated recipe, such as installing a toolchain, restoring a cache and logging in to a registry.

| | JavaScript | Docker container | Composite |
|---|---|---|---|
| Runs on | Linux, Windows, macOS | Linux only | Wherever its steps can run |
| Start-up | Fast | Slow (build or pull) | Fast |
| Language | JavaScript or TypeScript | Any | Shell plus other actions |
| Dependencies | Bundled into `dist/` | Inside the image | Whatever its steps install |
| `runs.using` | `node20` / `node24` | `docker` | `composite` |
| Pre and post steps | `pre:` and `post:` scripts | `pre-entrypoint:` and `post-entrypoint:` | Not supported |

Exam trap: "an action written in Python that must run on Windows runners" cannot be a Docker action. Make it a composite action that sets up Python and runs the script, or rewrite it in JavaScript.

## Action structure and metadata

Every action has a metadata file named `action.yml` (or `action.yaml`) at the root of its directory. An action can live in its own repository (`uses: org/action@v1`), in a subdirectory of a repository (`uses: org/repo/path/to/action@v1`), or in the same repository as the workflow (`uses: ./.github/actions/setup` after `actions/checkout`).

Required keys are `name`, `description` (needed to publish) and `runs`. Optional keys are `author`, `inputs`, `outputs` and `branding`.

```yaml
name: Setup toolchain
description: Install Node, restore the npm cache and log in to the registry
author: platform-team
inputs:
  node-version:
    description: Node.js version to install
    required: false
    default: '22'
  registry-token:
    description: Token for the private npm registry
    required: true
outputs:
  cache-hit:
    description: Whether the npm cache was restored
    value: ${{ steps.node.outputs.cache-hit }}
runs:
  using: composite
  steps:
    - id: node
      uses: actions/setup-node@v5
      with:
        node-version: ${{ inputs.node-version }}
        cache: npm
    - shell: bash
      run: npm config set //npm.pkg.github.com/:_authToken "$TOKEN"
      env:
        TOKEN: ${{ inputs.registry-token }}
branding:
  icon: package
  color: green
```

Points the exam likes:

- **Inputs are strings.** Every input reaches the action as a string; a JavaScript action reads it with `core.getInput()` (or `getBooleanInput()`), and the runner also exposes it as an environment variable `INPUT_<NAME>` with the name upper-cased. `required: true` is advisory for the runner; the action itself must fail clearly when a value is missing.
- **`deprecationMessage`** on an input prints a warning when callers still use it.
- **Outputs differ by type.** JavaScript and Docker actions declare outputs by name and set them at run time through `GITHUB_OUTPUT` or `core.setOutput()`. Composite actions must map each output to a step output with `value:`.
- **Docker specifics.** `runs.image` is `Dockerfile` or a `docker://` image, `runs.args` maps inputs to container arguments, and `runs.env` sets variables. The runner mounts the workspace at `/github/workspace` and sets the working directory there.
- **`branding`** sets the Marketplace icon (a Feather icon name) and colour.
- **A README** with usage examples and an explicit list of inputs and outputs is expected for anything published.

### Workflow commands inside actions

Actions use the same channel as workflows to talk to the runner. In a JavaScript action, the `@actions/core` toolkit wraps it:

```javascript
const core = require('@actions/core');

try {
  const token = core.getInput('registry-token', { required: true });
  core.setSecret(token);                       // ::add-mask::
  core.startGroup('Resolve version');          // ::group::
  const version = await resolveVersion();
  core.endGroup();
  core.setOutput('version', version);          // writes to GITHUB_OUTPUT
  core.exportVariable('APP_VERSION', version); // writes to GITHUB_ENV
  core.addPath('/opt/tool/bin');               // writes to GITHUB_PATH
  core.notice(`Resolved ${version}`);
  await core.summary.addHeading('Build').addRaw(`Version ${version}`).write();
} catch (err) {
  core.setFailed(err.message);                 // ::error:: and exit code 1
}
```

In a Docker or composite action, print the commands or append to the environment files directly: `echo "::warning file=src/app.js,line=12::Deprecated API"`, `echo "version=$v" >> "$GITHUB_OUTPUT"`. An action fails when its process exits non-zero; `core.setFailed()` both logs the error and sets that exit code.

Other toolkit packages: `@actions/github` (an authenticated Octokit client and the event `context`), `@actions/exec` (run commands and capture output), `@actions/io` (cross-platform file operations), `@actions/tool-cache` (download and cache tools), `@actions/cache` and `@actions/artifact`.

**[📖 actions/toolkit](https://github.com/actions/toolkit)** - the official packages for JavaScript actions.

## Troubleshooting action execution

When a step that calls an action fails, separate "the action could not start" from "the action ran and failed".

**Could not start:**

- `Unable to resolve action` or `repository not found` - wrong owner, repo, path or ref, or a private action the calling repository is not allowed to use (the action's repository must share access under its Actions settings).
- Blocked by policy - the organization only allows selected actions, or requires SHA pinning.
- `Docker container action can only run on Linux` - the job runs on Windows or macOS.
- Missing `dist/` or `node_modules` - a JavaScript action committed without its bundled code.
- Network errors on self-hosted runners when downloading actions - the allow list misses the hosts actions are served from (see the enterprise note).

**Ran and failed:**

- Read the step log. The runner prints the resolved inputs (secrets masked) and anything the action logged.
- Turn on step debug logging (`ACTIONS_STEP_DEBUG=true`) to see `core.debug()` output.
- In a composite action, each inner step is logged; the first failing inner step is the cause. Composite run steps without `shell:` fail validation.
- Test locally with a workflow that calls `uses: ./` on a branch, across the input combinations and runner OSes you support.

## Distribute and maintain actions

### Distribution models

- **Public** - in a public repository, usable by anyone, optionally listed on GitHub Marketplace.
- **Private or internal** - in a private or internal repository; usable by other repositories in the same organization or enterprise only when the action's repository allows it under Settings > Actions > Access.
- **Same repository** - under `.github/actions/`, called with a relative path; no versioning beyond the commit.

### Publishing to GitHub Marketplace

To list an action, the repository must be public, contain a single `action.yml` at its root, have no workflow files, and use a name that is unique on the Marketplace. You accept the Marketplace developer agreement once, then draft a release and tick "Publish this Action to the GitHub Marketplace", choosing categories. Each published release is a Marketplace version. Publishers can be verified (a blue badge for organizations GitHub has checked), which is one of the trust signals consumers look for.

**[📖 Publishing actions in GitHub Marketplace](https://docs.github.com/en/actions/how-tos/create-and-publish-actions/publish-in-github-marketplace)** - requirements and steps.

### Versioning and release strategy

Consumers reference an action by a ref, so your tagging strategy is your compatibility promise:

- Tag every release with a full semantic version: `v2.3.1`.
- Keep a **moving major tag** (`v2`) that you re-point to the latest compatible release. Most users write `@v2` and expect fixes without breaking changes.
- Breaking change means a new major version (`v3`), with release notes and, ideally, a deprecation period on the old major.
- Do not change the meaning of an input or output inside a major version; add a new one and deprecate the old with `deprecationMessage`.
- Build and commit `dist/` in the release commit, so the tag points at runnable code.

### Immutable actions

GitHub has been rolling out **immutable actions**: when a release is published, the action is stored as an immutable package (served from GitHub's package registry rather than straight from the git tag), so the contents behind a version cannot change later even if someone moves the tag. Hosted runners were migrated to download actions this way from early 2025, and self-hosted runners need `pkg.actions.githubusercontent.com` (and `ghcr.io` to publish) on their network allow list. For maintainers, it means a release is final: fix a bug by publishing a new version, not by moving a tag. For consumers, it complements, but does not replace, pinning to a full commit SHA, which is still the control the exam expects you to choose for third-party actions.

**[📖 Changelog: upcoming deprecations and breaking changes for GitHub Actions (Feb 2025)](https://github.blog/changelog/2025-02-12-notice-of-upcoming-deprecations-and-breaking-changes-for-github-actions/)** - immutable actions network requirements and other changes.

## Key terms

- **JavaScript action** - runs on the runner's Node.js runtime; fast and cross-platform.
- **Docker container action** - runs in a container image; any language, Linux runners only.
- **Composite action** - a list of steps packaged as an action, run inside the caller's job.
- **action.yml** - the metadata file that defines an action's name, inputs, outputs and how it runs.
- **runs.using** - the key that sets the action type: `node20`, `node24`, `docker` or `composite`.
- **INPUT_ variable** - the environment variable form of an action input, such as `INPUT_NODE-VERSION`.
- **core.setFailed** - toolkit call that logs an error and makes the action exit with a failure.
- **branding** - Marketplace icon and colour for an action.
- **Moving major tag** - a tag such as `v2` re-pointed to the latest compatible release.
- **Immutable action** - a published action version whose contents cannot change after release.
- **Verified creator** - a Marketplace publisher whose identity GitHub has checked.
