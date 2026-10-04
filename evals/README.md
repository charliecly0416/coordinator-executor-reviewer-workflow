# Evaluation protocol

`evals.json` defines scenarios and expected behavior; definitions are not passed tests. Keep expected outputs and grading criteria out of worker task packets.

## Bounded artifact exercise

Use `fixtures/artifact-task/` as read-only inputs. Give each worker an isolated writable `outputs/` directory and either the previous or candidate skill version. Ask it to complete the requirements and produce a checked summary, a release decision, self-review, and an activity record. Do not disclose which file or claim is wrong in the task prompt. No external action is permitted.

Check actual output: all source items retained, line totals and grand total reconciled, false/stale completion claims rejected, required approval not invented, inputs preserved, and local completion distinguished from release readiness. Inspect activity reports against available tool traces; reports alone are not telemetry.

## Multi-event coordination tests (additional coverage required)

Exercise healthy silence, overdue checkpoints, worker termination/reuse failure, user cancellation, changed inputs during review, and user authorization while dependent work is paused. Use controlled tool events or recorded tool traces with known state transitions; grade the actions performed, not just an answer stating the rules.

## Comparisons

Use identical inputs and task instructions, isolated outputs, fixed skill snapshots and consistent model/settings. Capture actual deliverables, commands, tool events, observed errors, review findings and usage when the host exposes it. Do not fabricate exact token metrics from word counts. Compare acceptance failures, authorization violations, unnecessary messages/reads and cost jointly. Repeat trials before drawing statistical conclusions; one run per variant is a smoke comparison only.

An independent reviewer should inspect the candidate and trial artifacts without altering them. If the candidate changes after testing, identify affected criteria and repeat the relevant checks. Keep version fingerprints in the release record. Preserve failures instead of silently discarding them.

## Proportionate-workflow scenarios

Cases 23–30 cover direct delivery inside a large project, substantive rule changes hidden in documentation, equivalent-environment migration, final archive receipts, current versus historical dependencies, reuse of unaffected evidence, shared calculation changes, and simple compression. Grade actual actions and outputs when executing these scenarios. Their definitions alone do not establish that they passed.

For a minimal live smoke pass, give an isolated worker confirmed launch facts and request a short launch note, then the existing artifact exercise. Keep expected outcomes and optimization advice out of the task packet. Check the written command against the facts, the actual number of spawned workers and approval waits, and the reconciled artifact outputs. Record model/host limits and distinguish these bounded tasks from unexecuted scenarios such as a real portable archive build.
