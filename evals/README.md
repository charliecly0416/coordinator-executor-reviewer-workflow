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
