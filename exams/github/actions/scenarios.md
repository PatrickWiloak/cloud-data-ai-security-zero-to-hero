---
last-updated: 2026-10-22
---

# GitHub Actions High-Yield Scenarios and Practice Problems

## Scenario 1: CI/CD Workflow Design

**Scenario**: Design a workflow that runs tests on every PR to main, requires tests to pass before merging, builds a Docker image on merge to main, and deploys to staging automatically but requires manual approval for production.

**Solution Pattern**:
- Trigger: `pull_request` for tests, `push` to main for build/deploy
- Use environments with protection rules for production
- Use job dependencies (`needs`) for sequential execution
- Use concurrency to prevent duplicate deployments

```yaml
on:
  pull_request:
    branches: [main]
  push:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - run: npm test
  build:
    if: github.event_name == 'push'
    needs: test
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - run: docker build -t myapp:${{ github.sha }} .
  deploy-staging:
    needs: build
    environment: staging
    runs-on: ubuntu-latest
    steps:
    - run: echo "Deploy to staging"
  deploy-production:
    needs: deploy-staging
    environment: production  # Has required reviewers
    runs-on: ubuntu-latest
    steps:
    - run: echo "Deploy to production"
```

**Key Takeaway**: Use `if` conditions to control which jobs run for which events. Use environments with protection rules for deployment approvals.

---

## Scenario 2: Matrix Strategy

**Scenario**: Test a Node.js library across Node 16, 18, and 20 on Ubuntu and macOS. Node 16 on macOS is known to fail - exclude it. Also add a specific test for Node 20 with experimental features enabled.

**Solution Pattern**:
```yaml
strategy:
  fail-fast: false
  matrix:
    node: [16, 18, 20]
    os: [ubuntu-latest, macos-latest]
    exclude:
    - node: 16
      os: macos-latest
    include:
    - node: 20
      os: ubuntu-latest
      experimental: true
```

**Common Distractors**:
- Using `fail-fast: true` (default) would cancel all jobs if one fails
- Forgetting `exclude` syntax (must match full combination)
- Not knowing that `include` can add extra variables to specific combinations

**Key Takeaway**: Matrix creates all combinations. Use `exclude` to remove specific combinations and `include` to add extras with additional variables.

---

## Scenario 3: Custom Action Development

**Scenario**: Create a composite action that checks if a PR has the required labels before allowing merge. It should accept a list of required labels as input and fail if any are missing.

**Solution Pattern**:
```yaml
# action.yml
name: 'Check Required Labels'
description: 'Verify PR has required labels'
inputs:
  required-labels:
    description: 'Comma-separated list of required labels'
    required: true
  github-token:
    description: 'GitHub token'
    required: true
runs:
  using: 'composite'
  steps:
  - name: Check labels
    shell: bash
    env:
      REQUIRED: ${{ inputs.required-labels }}
      GH_TOKEN: ${{ inputs.github-token }}
    run: |
      # Get PR labels and check against required
      labels=$(gh pr view ${{ github.event.number }} --json labels -q '.labels[].name')
      # Check each required label
```

**Common Distractors**:
- Using JavaScript action when composite is simpler for this use case
- Forgetting `shell: bash` on composite action run steps (required)
- Not passing the GitHub token as an input

**Key Takeaway**: Composite actions combine steps and are the simplest to create. JavaScript actions provide more power. Docker actions support any language but are Linux-only.

---

## Scenario 4: Reusable Workflows

**Scenario**: An organization has 50 repositories that all need the same security scanning workflow. How should this be implemented to maintain consistency and reduce duplication?

**Solution Pattern**:
- Create a reusable workflow in a central repository
- Use `workflow_call` trigger with inputs for customization
- Call the reusable workflow from each repository

```yaml
# Central repo: .github/workflows/security-scan.yml
on:
  workflow_call:
    inputs:
      language:
        type: string
        required: true
    secrets:
      token:
        required: true
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Run security scan
      run: echo "Scanning ${{ inputs.language }}"
      env:
        TOKEN: ${{ secrets.token }}
```

```yaml
# Each repo's workflow
on: [push]
jobs:
  security:
    uses: org/central-repo/.github/workflows/security-scan.yml@main
    with:
      language: javascript
    secrets:
      token: ${{ secrets.SCAN_TOKEN }}
```

**Common Distractors**:
- Confusing reusable workflows with composite actions (different mechanisms)
- Not knowing that `secrets: inherit` passes all secrets from the caller
- Forgetting that reusable workflows have a maximum nesting depth of 4

**Key Takeaway**: Reusable workflows enable DRY CI/CD across an organization. Use `workflow_call` trigger, define inputs and secrets, and call from other workflows.

---

## Scenario 5: Enterprise Runner Management

**Scenario**: A company needs self-hosted runners that can access internal services behind a firewall. Different teams should only use runners assigned to them. How should this be configured?

**Solution Pattern**:
- Install self-hosted runners on machines with network access to internal services
- Create runner groups for each team (e.g., "frontend-runners", "backend-runners")
- Assign repositories to the appropriate runner group
- Label runners for specific capabilities (e.g., `gpu`, `high-memory`)

```yaml
# Workflow targeting a specific runner group and label
jobs:
  build:
    runs-on: [self-hosted, backend, linux]
```

**Common Distractors**:
- Running self-hosted runners on public repositories (security risk - anyone can submit a PR and execute code)
- Not using runner groups for access control
- Not considering auto-scaling (Actions Runner Controller for Kubernetes)

**Key Takeaway**: Self-hosted runners provide access to internal resources. Use runner groups for access control and labels for capability selection. Never use self-hosted runners with public repositories.

---

## Scenario 6: OIDC Cloud Deployment

**Scenario**: Deploy to AWS from GitHub Actions without storing long-lived AWS credentials as secrets. How should authentication be configured?

**Solution Pattern**:
- Configure OIDC trust between GitHub and AWS
- Use the `aws-actions/configure-aws-credentials` action with OIDC
- Restrict trust to specific repository, branch, and environment

```yaml
permissions:
  id-token: write
  contents: read
jobs:
  deploy:
    environment: production
    runs-on: ubuntu-latest
    steps:
    - uses: aws-actions/configure-aws-credentials@v4
      with:
        role-to-assume: arn:aws:iam::123456789:role/github-actions
        aws-region: us-east-1
    - run: aws s3 ls
```

**Common Distractors**:
- Forgetting `permissions: id-token: write` (required for OIDC token)
- Storing AWS access keys as secrets (works but less secure than OIDC)
- Not restricting the IAM trust policy to specific repos/branches

**Key Takeaway**: OIDC eliminates the need for long-lived cloud credentials. Configure trust at the cloud provider level, restrict to specific repos/branches, and always set `id-token: write` permission.

---

## Scenario 7: Secrets and Security

**Scenario**: A workflow needs to access a database password, an API key shared across the organization, and a deployment token only available in the production environment. How should secrets be organized?

**Solution Pattern**:
- **Database password**: Repository secret (specific to this repo)
- **API key**: Organization secret (shared across repos)
- **Deployment token**: Environment secret on the "production" environment (with required reviewers)

**Access in workflow:**
```yaml
jobs:
  deploy:
    environment: production
    runs-on: ubuntu-latest
    steps:
    - name: Access secrets
      env:
        DB_PASS: ${{ secrets.DATABASE_PASSWORD }}       # Repo secret
        API_KEY: ${{ secrets.ORG_API_KEY }}              # Org secret
        DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}        # Env secret
      run: echo "Deploying..."
```

**Common Distractors**:
- Printing secrets in logs (they are masked, but avoid deliberately logging them)
- Using repository secrets for shared values (org secrets reduce duplication)
- Not using environment protection rules for sensitive deployment secrets

**Key Takeaway**: Use the appropriate scope for each secret - repository for repo-specific, organization for shared, environment for deployment-specific. Environment secrets benefit from protection rules.

## Scenario 8: Troubleshooting a Failed Matrix Run

**Scenario**: A pull request's CI shows `test (ubuntu-latest, 22)` failed, and the five other matrix jobs show "cancelled". The same commit passed yesterday. The developer wants to know what broke and to re-check only the failing combination.

**Approach**: Treat only the first failure as evidence. The cancelled jobs were stopped by `fail-fast`, which is `true` by default, so they say nothing about their own combinations. Open the failed job, read the annotations at the top of the summary, then expand "Set up job": it names the runner image version and the resolved SHA of each action. A new image version or a moved action tag on an unchanged commit is the usual explanation for "it passed yesterday". Re-run with debug logging if the log is thin, and use "Re-run failed jobs" (or `gh run rerun RUN_ID --failed`) to repeat just that job. Remember a re-run uses the original commit and workflow file, so it will not pick up a fix pushed since.

**Common Distractors**:
- Assuming the cancelled matrix jobs also failed
- Pushing an empty commit to "retry" instead of re-running the failed job
- Expecting a re-run to use the latest version of the workflow file

**Key Takeaway**: Map the job name to its matrix values, find the first real failure, and compare the setup step against the last green run.

## Scenario 9: Script Injection in an Issue Triage Workflow

**Scenario**: An `issues: opened` workflow runs `run: echo "New issue: ${{ github.event.issue.title }}" | ./triage.sh` with `permissions: write-all`. A security review flags it.

**Approach**: The expression is pasted into the script before bash runs, so a title containing shell syntax executes with a write-capable token. Move the value into an environment variable and quote it, drop the permissions to what triage needs, and validate the input in the script.

```yaml
permissions:
  issues: write
jobs:
  triage:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - run: echo "New issue: $TITLE" | ./triage.sh
        env:
          TITLE: ${{ github.event.issue.title }}
```

**Common Distractors**:
- Wrapping the expression in single quotes inside the script (still injectable)
- Relying on secret masking to make the step safe
- Switching to `pull_request_target`, which adds secrets instead of removing risk

**Key Takeaway**: Untrusted event text goes through `env:` and quoted shell variables, never directly into `run:`, and the job keeps least-privilege permissions.

## Key Decision Factors

### Domain Priority for Study (skills measured as of January 2026)
1. **Author and manage workflows (20-25%)** - triggers, structure, matrices, service containers, YAML anchors, contexts and expressions, outputs, summaries, environments
2. **Manage GitHub Actions for the enterprise (20-25%)** - action policies, runners and runner groups, networking and IP allow lists, preinstalled software, secrets and variables via UI and REST
3. **Consume and troubleshoot workflows (15-20%)** - reading runs and logs, matrix failures, re-runs, artifacts via UI and API, templates vs reusable workflows vs composite actions, disable vs delete
4. **Author and maintain actions (15-20%)** - JS, Docker, composite, `action.yml`, workflow commands, Marketplace, versioning, immutable actions
5. **Secure and optimize automation (10-15%)** - environments and approvals, script injection, `GITHUB_TOKEN` vs PAT, OIDC, SHA pinning, attestations, caching and cost

### Common Anti-Patterns
- Memorizing syntax without building and debugging real workflows
- Ignoring security features (OIDC, SHA pinning, least-privilege permissions)
- Not understanding the difference between workflow templates, reusable workflows and composite actions
- Skipping enterprise administration, which is now joint-largest at 20-25%
