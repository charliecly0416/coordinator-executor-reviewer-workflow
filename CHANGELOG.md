# Changelog

## 2.0.0 — 2026-10-04

- Rewrote the runtime workflow around one closed loop: choose a mode, define acceptance, execute, verify, classify findings, repair only what matters, and close.
- Added an explicit mode boundary so Direct work stops after its self-check and does not inherit collaboration or monitoring rules.
- Added blocker/material/minor/optional finding triage, a default targeted repair pass for Direct and Assisted work, and a stop rule for repeated patches without material progress.
- Kept independent review for critical deliverables, evidence and failure provenance, authorization boundaries, impact-scoped verification, migration semantics, and portable handoff checks.
- Removed duplicate lifecycle prose, mandatory-looking report patterns, and open-ended continuation language that encouraged bloated deliverables.

## 1.1.0 — 2026-10-04

- Put direct execution, local verification, and critical-deliverable independent review first; ordinary subtasks do not inherit the full collaboration loop.
- Tie checks to concrete risks and versions, reuse unaffected evidence, and scope dependencies and migration conditions to the delivery promise.
- Freeze archive contents, separate build output and final acceptance receipts, and retain portability checks for handoffs that promise recomputation.
- Consolidate monitoring and context guidance, make report examples optional, and replace fixed repair checkpoints with evidence-based reassessment.
- Preserve authorization, independent-review integrity, negative results, failure history, and continuation through the whole authorized objective.

## 1.0.0 — 2026-09-13

- Generalized the coordinator–executor–reviewer workflow for technical and nontechnical tasks.
- Added lightweight, independent-review, and parallel-execution selection guidance.
- Added cause-based `HOLD` routing, host status adaptation, repeated-repair alignment checks, safe user-decision pauses, and evidence-integrity rules.
- Added context/token economy guidance that preserves acceptance evidence.
- Added portable structure validation, corrupted-artifact regression checks, bounded baseline/candidate evidence, and a deterministic multi-event coordination exercise.
- Documented bounded validation limits; no cross-host reliability or token-savings claim is made.
