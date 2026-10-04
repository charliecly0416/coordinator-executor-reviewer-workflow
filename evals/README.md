# Evaluation protocol

`evals.json` contains scenario definitions and expected behavior. Definitions are not passing tests. Grade the actions and artifacts produced by a worker; do not put the expected answer or optimization rationale in its task packet.

## What to test

The suite covers proportional mode selection, ordinary work inside large projects, meaningful rule changes, independent-review honesty, evidence integrity, authorization boundaries, worker monitoring, partial verdicts, changed inputs, migration conditions, dependency scope, archive receipts, and reuse of unaffected evidence.

Scenarios 31–34 cover the v2.0.0 repair behavior: a direct task closes after self-check, a minor finding does not create a repair phase, a repeated patch without new evidence stops with a truthful boundary, and a blocking defect receives a targeted repair and impact-scoped recheck.

## Bounded artifact exercise

Use `fixtures/artifact-task/` as read-only inputs and an isolated writable output directory. The task requires a reconciled summary, a release decision, and a self-review while preserving inputs, historical evidence, and pending external approval. Check actual files: all source items retained, totals reconciled, false or stale completion claims rejected, approval not invented, and local completion distinguished from release readiness.

## Comparisons and limits

Use identical inputs, isolated outputs, fixed skill snapshots, and consistent model settings when comparing revisions. Capture deliverables, tool events, findings, and usage only when the host exposes them. Do not infer exact token savings from word counts. Repeat trials before drawing statistical conclusions. Preserve failures and record which scenarios were not run.
