# Coordinator · Executor · Reviewer

[![skills.sh](https://skills.sh/b/charliecly0416/coordinator-executor-reviewer-workflow)](https://skills.sh/charliecly0416/coordinator-executor-reviewer-workflow)

A proportionate workflow for carrying an authorized task to a useful, verified result. It supports direct execution, targeted assistance, and independent review of critical deliverables across technical and nontechnical work.

## Install

Install from GitHub with the skills CLI:

```bash
npx skills add charliecly0416/coordinator-executor-reviewer-workflow --skill coordinator-executor-reviewer-workflow
```

Use `-g -a codex` for a global Codex installation. Refresh a global installation with:

```bash
npx skills update coordinator-executor-reviewer-workflow -g
```

## Use

> Use coordinator-executor-reviewer-workflow to complete this assignment. Keep ordinary work direct, use independent review where the result requires it, preserve evidence, and stop when the agreed acceptance criteria are met.

Provide the actual task, constraints, inputs, authorization, and definition of done. The skill selects the smallest sufficient mode for each deliverable. It does not require three agents, a repository, code tests, phase files, or formal reports for ordinary work.

## Design

- Direct tasks are completed and self-checked by the current agent.
- Assisted tasks receive targeted verification from one executor.
- Critical deliverables receive independent review against predefined criteria.
- Findings are classified before repair; optional improvements do not become hidden work.
- Repairs are small and impact-scoped. The result closes once mandatory criteria pass.
- Evidence, failures, negative results, authorization boundaries, and portability claims remain truthful.
- Complex archives freeze their contents before packaging and keep the final acceptance receipt outside the archive.

## Validation

Run `python scripts/validate_skill.py` for package checks. Maintainers can run `python scripts/test_trial_checker.py` and `python scripts/check_artifact_trial.py` for evidence-integrity checks. See [evaluation protocol](evals/README.md) and [release validation](RELEASE_VALIDATION.md) for bounded coverage and known limits. Passing these checks does not prove broad model behavior or token savings.

`SKILL.md` is the runtime entry point. The monitoring reference is read only for active delegated work. The `evals/` and `scripts/` directories are maintainer resources.
