---
last-updated: 2026-08-09
difficulty: intermediate
reading-time: 11 min
---

# 02 - Argo CD

**Domain 2: Argo CD (34%)**

A GitOps agent that reconciles cluster state against a repository.

---

## Architecture

| Component | Role |
|---|---|
| **API server** | gRPC and REST API, the web UI, authentication, and RBAC |
| **Repository server** | Clones repositories and renders manifests (Helm, Kustomize, plugins) |
| **Application controller** | Compares desired against live state, reports health and sync status, performs syncs |
| **Redis** | Cache for rendered manifests and cluster state |
| **Dex** (optional) | OIDC federation when not using an external provider directly |

---

## The Application resource

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: api
spec:
  project: payments
  source:
    repoURL: https://github.com/org/config
    targetRevision: main
    path: envs/prod/api
  destination:
    server: https://kubernetes.default.svc
    namespace: api
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
```

**Sync policy** flags are independent and both are directly testable:

- **`prune`** deletes cluster resources that are no longer in the source
- **`selfHeal`** reverts drift on resources still declared in the source

Automated sync without `prune` leaves orphans; without `selfHeal` it ignores manual edits.

---

## Ordering: waves and hooks

**Sync waves** order resources within a single sync using the `argocd.argoproj.io/sync-wave` annotation. Lower numbers, including negatives, apply first, and Argo CD waits for a wave to become healthy before proceeding. The canonical use is CRDs before custom resources, or a namespace and its operator before workloads.

**Resource hooks** run at defined points, typically as Jobs:

| Hook | When |
|---|---|
| `PreSync` | Before the sync, for database migrations |
| `Sync` | During the sync, alongside other resources |
| `PostSync` | After all resources are healthy, for smoke tests |
| `SyncFail` | When the sync fails, for cleanup or notification |
| `Skip` | Excludes the resource from the sync |

**Hook deletion policies** (`HookSucceeded`, `HookFailed`, `BeforeHookCreation`) control cleanup of hook Jobs.

---

## Health and diffing

Argo CD assesses **health** per resource kind with built-in checks (a Deployment is Healthy when its replicas are available) and supports **custom health checks** in Lua for custom resources.

**Sync status** is separate from health: Synced means live state matches the source; Healthy means the resources are working. A resource can be Synced and Degraded.

**`ignoreDifferences`** excludes fields from comparison, by group, kind, and JSON pointer or jq path. This is how you stop fighting another controller over `replicas` under an HPA, injected sidecars, or webhook-mutated fields.

---

## Multi-tenancy: AppProject

An `AppProject` constrains what its Applications may do:

- **Allowed source repositories**
- **Allowed destinations** (cluster and namespace)
- **Allowed cluster-scoped and namespace-scoped resource kinds**, as allow or deny lists
- **Roles and RBAC** scoped to the project
- **Sync windows** permitting or blocking syncs during defined periods

This is the boundary that makes a shared Argo CD instance safe for multiple teams.

---

## ApplicationSet

Generates many Applications from one definition.

| Generator | Produces one Application per |
|---|---|
| **List** | Static list element |
| **Cluster** | Registered cluster, optionally filtered by labels |
| **Git (directory)** | Directory matching a pattern in a repository |
| **Git (file)** | Config file discovered in a repository |
| **Matrix** | Cartesian combination of two generators |
| **Merge** | Merged output of several generators, keyed by a field |
| **Pull request** | Open pull request, for preview environments |
| **SCM provider** | Repository in an organization |

`Matrix` is how you get "every application on every cluster" from two small lists.

---

## Tooling and patterns

- **Kustomize, Helm, jsonnet** are supported natively; **config management plugins** cover anything else
- **App of apps**: a parent Application whose source contains child Application manifests, so Argo CD manages its own configuration
- **Argo CD Image Updater** watches registries and writes new tags back to the repository
- **Notifications** send sync and health events to Slack, email, or webhooks
- **Declarative setup**: Argo CD's own configuration lives in ConfigMaps and custom resources, so it can be managed by GitOps

---

## Key terms

- **Application** - the Argo CD custom resource binding a source repository path to a cluster destination
- **AppProject** - the multi-tenancy boundary restricting allowed sources, destinations, and resource kinds
- **Repository server** - the Argo CD component that clones repositories and renders manifests
- **Application controller** - the component comparing desired against live state and performing syncs
- **prune** - the sync policy flag deleting cluster resources no longer present in the source
- **selfHeal** - the sync policy flag reverting drift on resources still declared in the source
- **Sync wave** - an annotation ordering resource application within a single sync
- **Resource hook** - a resource executed at PreSync, Sync, PostSync, or SyncFail during a sync
- **Sync status** - whether live state matches the source, distinct from health
- **Health status** - whether resources are functioning, assessed per kind and extensible in Lua
- **ignoreDifferences** - configuration excluding specific fields from drift comparison
- **Sync window** - an AppProject setting permitting or blocking syncs during defined time periods
- **ApplicationSet** - the controller generating many Applications from one templated definition
- **Matrix generator** - an ApplicationSet generator producing the Cartesian combination of two generators
- **Pull request generator** - an ApplicationSet generator creating an Application per open pull request
- **App of apps** - the pattern where a parent Application deploys child Application manifests
- **Argo CD Image Updater** - the component watching registries and committing new image tags to the source

---

## Related

- [Notes 03: Argo Rollouts](./03-argo-rollouts.md)
- [Scenarios](../scenarios.md) - scenarios 3, 4, and 5
- [CGOA](../../cgoa/) - the principles this implements
