---
last-updated: 2026-07-29
---

# PD2 05 - Testing, Debugging, and Deployment

Apex testing beyond the coverage minimum, debugging tools, and the deployment lifecycle.
The exam expects testing rigor, not just "hit 75%."

## Apex testing

- **Coverage requirement** - 75% org-wide code coverage to deploy to production, and every trigger must have some coverage. But coverage is a floor, not a goal: the exam tests whether you understand *good* testing.
- **Test method structure** - `@isTest` on the method or class. Tests run in isolation and see no existing org data by default (`@isTest(SeeAllData=false)`, the default).
- **Test data creation** - create the data the test needs inside the test, or via a `@testSetup` method that runs once and is rolled back after each test method. `@testSetup` is the efficient pattern for shared setup.
- **`Test.startTest()` and `Test.stopTest()`** - reset governor limits for the code between them (so you test your code's limits, not the setup's), and force asynchronous code enqueued inside to run synchronously at `stopTest`. This is how you test future, queueable, and batch logic.
- **Assertions** - `Assert.areEqual`, `Assert.isTrue`, and so on. A test with no assertions proves nothing beyond that the code ran; the exam treats assertion-free tests as inadequate.
- **Positive and negative testing** - test the success path, the failure path, boundary values, and bulk (200 records) to prove bulkification.
- **`System.runAs`** - runs a block as a specified user, the way to test sharing, profiles, and permission behavior.
- **Mocking callouts** - `HttpCalloutMock` and `Test.setMock` provide fake responses, because tests cannot make real callouts.
- **Test.loadData and static resources** - loading test data from a CSV static resource.

Good tests assert outcomes, cover positive, negative, bulk, and permission scenarios, and
create their own data. Coverage percentage alone is not the target.

## Debugging

- **Debug logs** - capture execution detail. Log levels (NONE, ERROR, WARN, INFO, DEBUG, FINE, FINEST) per category (Apex code, database, callouts, validation, workflow) control verbosity.
- **`System.debug()`** - writes to the log at a chosen level.
- **Developer Console** - inspect logs, view the execution timeline, run anonymous Apex, and check query plans.
- **Log limits and truncation** - logs cap at a size; very large logs truncate, hiding the part you need. Narrow the categories.
- **Checkpoints** - inspect heap state at a point in the Developer Console.
- **Apex Replay Debugger** - step through a captured debug log in VS Code as if debugging live.
- **Query plan tool** - shows whether a SOQL query uses an index, essential for LDV performance work.

## Exceptions and error handling

- **Try/catch/finally** - catch specific exception types before generic `Exception`.
- **Custom exceptions** - a class extending `Exception`, for meaningful error signaling.
- **`addError()`** - on a record or field in a trigger, to block the DML with a user-facing message.
- **Uncatchable exceptions** - `LimitException` cannot be caught; design to stay within limits rather than catching.
- **Platform events for error logging** - publishing an error event so the log survives a rollback, because a caught-and-logged error written by DML is rolled back with the transaction otherwise.

That last point is a subtle exam favorite: to persist a log record even when the
transaction rolls back, publish a Platform Event, which is not rolled back.

## Deployment and application lifecycle

- **Change sets** - declarative deployment between related orgs (sandbox to production). Simple, but manual and not version-controlled.
- **Metadata API** - programmatic retrieve and deploy, the basis of tooling.
- **Salesforce CLI (sf)** - the command-line tool for source-driven development and deployment.
- **Source-driven development** - metadata stored in version control as the source of truth, deployed via CLI, enabling real CI/CD.
- **Unlocked packages** - versioned, source-based packaging for modular deployment. The modern recommended approach for organizing and deploying customisations.
- **Scratch orgs** - ephemeral, source-defined orgs for development and testing, spun up and torn down from configuration.
- **Sandboxes** - Developer, Developer Pro, Partial Copy, and Full, differing in data and refresh interval. Full sandboxes copy production data and are for final testing.

**Deployment testing** - deploying to production runs tests. You can run local tests, all
tests, or specified tests. A deployment fails if coverage drops below 75% or any test fails.

## CI/CD

- **Version control** - Git as the source of truth.
- **Automated deployment** - CLI-driven, triggered by a pipeline.
- **Automated testing** - running the Apex test suite on each change.
- See the repo's [CI/CD explained](../../../../learn/concepts/cicd-explained.md) for the general pattern.

## Exam pointers

- 75% coverage is the floor; the exam values meaningful assertions, negative tests, and bulk (200-record) tests.
- `Test.startTest`/`stopTest` reset limits and force async code to complete, which is how you test batch, future, and queueable.
- Use `@testSetup` for shared data and `System.runAs` for sharing and permission tests.
- Mock callouts with `HttpCalloutMock`; tests cannot make real callouts.
- To persist an error log despite a rollback, publish a Platform Event.
- Unlocked packages and source-driven development are the modern lifecycle; change sets are the legacy declarative path.

## Official documentation

**[📖 Platform Developer II exam guide](https://trailhead.salesforce.com/credentials/platformdeveloperii)** - authoritative objectives
**[📖 Testing Apex](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_testing.htm)** - test structure and best practices
**[📖 Salesforce DX Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/)** - source-driven development and packaging
