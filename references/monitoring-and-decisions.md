# Monitoring and decision examples

Read this reference only for active Assisted or Reviewed work. Direct work needs no monitoring ceremony.

## Dispatch

> Complete the named deliverable from the listed inputs and constraints. Meet the acceptance criteria, preserve relevant evidence, and report material uncertainty or a blocker. Work to a natural checkpoint; do not trade correctness for a quick reply.

A useful packet names the outcome, inputs and versions, scope, acceptance criteria, expected evidence, owner, and next checkpoint. Do not transmit the full conversation when the original sources remain available.

## Monitoring

| Observation | Action |
|---|---|
| Evidence is advancing | Let the worker continue; update the user when useful. |
| No visible process while reading or editing | Allow the agreed checkpoint; no PID is not proof of a hang. |
| A checkpoint is genuinely missed | Inspect relevant artifacts and send one targeted inquiry. |
| An inquiry is pending | Wait or do independent authorized work; do not repeat it. |
| A worker returns only a progress note | Record the missing deliverable and resume or reassign it. |
| Required work remains but all workers are idle | Reuse, reassign, or use an authorized self-execution path; do not wait for nonexistent output. |
| A safety, data, scope, or authorization boundary appears | Preserve state, pause dependent work, and prepare the user decision. |

Do not demand “quick PASS,” minute-by-minute reports, or reduced verification to make progress visible. A user update does not require a new worker message.

## Route findings

- `PASS`: continue only if another required deliverable remains; otherwise close.
- `PASS with nonblocking notes`: record and close when the promised result is usable.
- `FAIL`: repair the concrete unmet criterion, then run an impact-scoped recheck.
- `HOLD`: route by cause—missing evidence, external dependency, or user decision. Do not patch a correct deliverable.
- `STOP`: determine its scope before ending the overall objective.

## Repair diagnosis

After each repair, compare remaining findings with the locked acceptance contract. Continue only for an in-scope mandatory finding with a concrete repair and evidence of material improvement. If the input version, diagnosis, or dependency is wrong, correct that cause once within scope; otherwise stop patching and report the boundary. New phases, reports, or renamed findings do not restart the workflow.

## Compact handoff

Record the authoritative task reference, current result and version, verified facts, unresolved blocking item, authorization, owner/state, evidence location, and next action. A small task can put these facts in the final response; it does not need a separate handoff file.
