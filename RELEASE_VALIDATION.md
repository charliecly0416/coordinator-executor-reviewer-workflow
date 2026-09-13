# Release validation

Status: v1.0.0 community release candidate with bounded validation. This is not a claim of broad platform certification.

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

Completed for this bounded release candidate: controlled multi-event candidate exercise and independent final review. Remaining maturity evidence is listed below. No public deployment or external distribution has been performed.

## Maturity limitations

This release has one bounded trial per baseline/candidate, one deterministic simulated host, and no exact model-token telemetry. The saved activity records are self-reported and do not prove all host-level events. More independent runs across hosts, real event traces, and joint quality/cost measurements are required before claiming broad reliability or token savings.
