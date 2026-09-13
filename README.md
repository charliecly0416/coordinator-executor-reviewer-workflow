# Coordinator · Executor · Reviewer

[![skills.sh](https://skills.sh/b/charliecly0416/coordinator-executor-reviewer-workflow)](https://skills.sh/charliecly0416/coordinator-executor-reviewer-workflow)

A general-purpose workflow for carrying an authorized task from assignment through evidence-based review and completion. Applies to technical and nontechnical work.

## Use

Install the directory as a local skill using your host's supported skill installation mechanism, or give your coordinator the `SKILL.md` file. Preserve its relative `references/` directory. No runtime package, API credential, daemon, or model provider is required by the skill itself.

Example request:

> Use coordinator-executor-reviewer-workflow to complete this assignment. Define acceptance criteria, use independent review where required, keep me informed without rushing workers, repair ordinary failures, and ask me before any new authorization or material change of direction.

Provide the actual task, constraints, inputs, and definition of done. For short tasks, responsibilities can be combined with explicitly labelled self-review unless independence is required. Complex tasks may use several workers when their assignments are independent.

## Behavior

- Separate progress updates to the user from requests to workers.
- Continue authorized work after partial progress; stop safely for a genuine user decision.
- Route HOLD by its cause instead of automatically rewriting deliverables.
- Reassess repeated unsuccessful repairs without arbitrary attempt caps.
- Minimize duplicated context, polling, reports, and verification while preserving evidence.
- Never treat a service success label or self-review as proof of independent acceptance.

## Compatibility

Use only the host's real tools and status semantics. Progress channels, waiting, interruption, agent reuse, and persistent monitoring are optional capabilities, not guarantees. A host unable to maintain an active task needs a truthful handoff. The skill cannot itself keep a session alive or enforce its instructions mechanically.

`SKILL.md` is the runtime entry point. `references/monitoring-and-decisions.md` is read only when needed. `evals/` and `scripts/validate_skill.py` are maintainer resources; workers need not load them during ordinary tasks.

## Validation and limits

Run `python scripts/validate_skill.py` for portable package checks. Maintainers can also run `python scripts/test_trial_checker.py` to exercise rejection of corrupted evidence. This is structural validation, not a test that a model will follow the workflow.

See [evaluation protocol](evals/README.md) and [release validation](RELEASE_VALIDATION.md) for actual tested scope, evidence and known gaps. Do not interpret a passing smoke task as broad reliability or a guarantee of token savings. Review quality depends on the model, tools, inputs, and task.

## Distribution

No independent license grant is added by this package. Before redistributing, confirm that the original material and modifications are covered by an appropriate license from the rights holder or containing repository. No external publication is performed by installing this skill.
