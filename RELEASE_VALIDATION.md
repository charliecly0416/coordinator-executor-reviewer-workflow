# Release validation

## v2.0.0 — 2026-10-04

This release is a structural rewrite of the runtime skill. It makes the mode boundary explicit, gives findings a severity and repair policy, and closes accepted work before optional improvements can turn into a second project. It preserves independent review for critical deliverables and the evidence, authorization, migration, and archive rules that protect correctness.

Executed checks:

- `python scripts/validate_skill.py`: package structure, Markdown references, and 34 scenario definitions passed.
- Codex skill-creator `quick_validate.py`: skill metadata and structure passed.
- `python scripts/test_trial_checker.py`: all 5 existing evidence-checker tests passed.
- `python scripts/check_artifact_trial.py`: the saved baseline and candidate artifact outputs still satisfy their integrity checks.
- `npx --yes skills add . --list`: the CLI discovered exactly one skill with the expected name.
- The bounded launch-note and artifact smoke outputs from the previous release remain valid under the rewritten acceptance rules; the maintainer rechecked their commands, arithmetic, preserved inputs, pending approval, and self-review labels.

The runtime entry point is 119 lines and the monitoring reference is 39 lines. The expanded scenario definitions remain test specifications, not behavioral passes. No claim is made about statistical reliability, exact token savings, live agent recovery, or archive portability from this validation alone. A fresh behavioral trial should cover the new stop-after-acceptance and repair-triage cases before making such claims.

## Historical validation

### v1.1.0 historical validation

This earlier revision makes direct execution the default for ordinary subtasks while preserving review requirements for critical deliverables. The maintainer checked coverage against the supplied optimization brief; an independent agent reviewed the runtime instructions without editing them.

Executed checks:

- `python scripts/validate_skill.py`: package structure, Markdown references, and 30 scenario definitions passed. Definitions are not executed behavioral tests.
- Codex skill-creator `quick_validate.py`: skill metadata and structure passed.
- `python scripts/test_trial_checker.py`: all 5 existing evidence-checker tests passed.
- `python scripts/check_artifact_trial.py`: historical baseline/candidate artifacts still satisfy the checker; this is not a new old-version comparison.
- `npx --yes skills add . --list`: the CLI discovered exactly one skill with the expected name. No npm package publication is required for GitHub-based installation.
- One isolated worker completed a Chinese launch note and the existing purchase-summary exercise using the candidate. The maintainer inspected the note and independently recomputed the artifact checks: all items retained, total 670, inputs preserved, obsolete/empty success claims rejected, self-review labeled, and external approval left pending.
- Independent read-only content review found no blocking issues. A scoped follow-up review found no blocking issues with exempting simple compression from unnecessary receipts and suggested making receipts explicit for complex result handoffs. That suggestion was adopted and checked by the maintainer; unaffected calculation trials were not rerun.

Saved outputs and version fingerprints: [bounded smoke validation](evals/results/proportionate-workflow-smoke/validation.json), [launch note](evals/results/proportionate-workflow-smoke/launch/launch.md), [purchase summary](evals/results/proportionate-workflow-smoke/artifact/summary.md), [decision](evals/results/proportionate-workflow-smoke/artifact/decision.json), and [self-review](evals/results/proportionate-workflow-smoke/artifact/review.md). The purchase inputs are the unchanged files in `evals/fixtures/artifact-task/`.

Limits: one worker and one trial per task; further delegation and external actions were disabled by the harness. These checks do not prove autonomous agent-count selection, portability, real environment migration, live agent recovery, broad reliability, or time/token savings. New scenario definitions remain unexecuted unless accompanied by a recorded trial. Historical failures and evidence are retained below.

## Historical v1.0.0 validation

The following records describe the original bounded release candidate, not new v1.1.0 trials.

## Executed

- Portable structure validation is available in `scripts/validate_skill.py`.
- One isolated artifact task per version (baseline and candidate) was executed by separate agents. Both corrected the deliverable, preserved inputs, labelled self-review, and retained the pending external approval.
- Saved inputs and outputs are in `evals/results/artifact-smoke/`; `scripts/check_artifact_trial.py` independently recomputes the table and validates selected outcomes from the saved files.
- Corruption regression suite: `python scripts/test_trial_checker.py` — 5 passed (valid output plus empty, incorrect total, invented approval, and changed-input rejection).
- Candidate multi-event deterministic exercise: 8 logged events; it recovered an incomplete delivery, reviewed the repaired version, routed an approval-only HOLD, and paused at the external boundary. Independent review verified the sequence and SHA-256.
- Worker activity reports are self-reported, not complete platform telemetry. Exact aggregate model token usage was not supplied, so no token reduction is claimed.

## Scope limits

These runs are bounded smoke checks with one trial per variant, not a statistical benchmark. The exercise explicitly constrained tool access and external actions. Passing it does not establish behavior across arbitrary tasks, hosts or long sessions. The baseline also passed; no superiority is inferred from these results.

The scenario definitions in `evals/evals.json` are separate from executed results. Definitions without a corresponding recorded trial remain untested.

Completed for this bounded release candidate: controlled multi-event candidate exercise and independent final review. Remaining maturity evidence is listed below. That original validation did not itself perform public deployment or external distribution.

## Maturity limitations

This release has one bounded trial per baseline/candidate, one deterministic simulated host, and no exact model-token telemetry. The saved activity records are self-reported and do not prove all host-level events. More independent runs across hosts, real event traces, and joint quality/cost measurements are required before claiming broad reliability or token savings.
