---
name: coordinator-executor-reviewer-workflow
description: Carry an authorized task from a clear request to a useful, verified result with proportionate coordination. Use when the user requests coordinator, executor, and reviewer roles, independent review, or sustained delegation. Apply the smallest sufficient mode; ordinary tasks stay direct and do not inherit a multi-agent workflow.
---

# Coordinator–Executor–Reviewer Workflow

This skill turns an authorized request into a finished deliverable. Its governing rule is **use the smallest workflow that can establish the promised result**. Coordination, review, records, and repair are means to acceptance; they are not deliverables by themselves.

## 1. Select the mode before acting

Choose a mode for each coherent requested outcome, not automatically for the whole project. Do not split one outcome into artificial deliverables just to create reviews or records; split only when outputs have independent acceptance criteria, owners, or risks. User requirements and an existing acceptance contract override these defaults.

| Mode | Use when | What to do |
|---|---|---|
| **Direct** | One agent can produce a low-risk result from available facts; no independent approval is required. | Produce it, check the facts and requested scope, and deliver it. Do not create agents, phase records, review gates, or extra artifacts. |
| **Assisted** | The result has real dependencies, moderate risk, or a bounded implementation that benefits from targeted testing, but no separate approval is required. | One executor completes the work. Verify the changed behavior and its necessary dependencies. Add coordination only where it removes a real dependency or risk. |
| **Reviewed** | The user or contract requires independence, or an error could materially affect scientific results, safety, money, authorization, or a complex portable handoff. | Separate executor and reviewer. Review one stable deliverable against its predefined acceptance criteria and core evidence. The coordinator routes findings and closes the result. |

A file extension, project size, or request to “use the framework” does not choose the mode. A routine launch note can be Direct; a launch note that changes evaluation rules is Reviewed. A simple archive can be Assisted; a handoff promising independent recomputation is Reviewed.

**Mode boundary:** once Direct is selected, stop after its short self-check succeeds. Do not apply the collaboration, monitoring, or repair sections merely because they appear later in this document. Escalate only if a concrete risk, unmet requirement, or explicit review requirement appears.

## 2. Define the promised result

Before execution, establish only what the current deliverable needs:

- the requested outcome and non-goals;
- authoritative inputs, constraints, and existing authorization;
- acceptance criteria and the evidence that can establish them;
- for Assisted or Reviewed work, the owner, stable version, and any independent-review boundary.

Use the task's actual instructions and sources. Do not invent approvals, experiments, dependencies, identity requirements, or follow-up work. Resolve a material ambiguity only when it blocks the dependent action; continue unaffected authorized work.

Lock the scope at this point. A suggestion, reviewer preference, or newly noticed improvement is not a requirement unless it changes whether the promised result is correct or usable. Do not turn a completed deliverable into an open-ended improvement project.

## 3. Execute and verify proportionately

The executor owns the requested result, works from the named inputs, and reports actual changes, evidence, limitations, and blockers. The coordinator remains responsible for the whole authorized objective only when Assisted or Reviewed work is active.

Choose checks for a concrete purpose: identify the error they could catch, the requirement they protect, and the deliverable affected by failure. Prefer existing evidence and mature tools. A successful command, service status, or confident summary is not evidence beyond the scope it covers. Do not write code tests for a non-code deliverable just to satisfy a template.

Bind evidence to the relevant input, implementation, and output versions. Preserve raw evidence, negative results, meaningful failures, and provenance that are relevant to the promised claim, acceptance criteria, or required scientific record; do not collect unrelated history. After a change, recheck the changed area, previous blocking findings, and dependencies whose behavior could have changed; retain evidence for unaffected areas. Examples:

- Formatting or wording change: check the document; do not rerun an experiment.
- Added table fields: check the fields and cross-table consistency; do not rerun unchanged computation.
- Changed result logic or shared execution semantics: recompute and review every affected result.
- Recompressed unchanged files: check members, hashes, and extraction as promised; do not re-review scientific conclusions.

A new status file or review report does not by itself invalidate prior evidence. If an input, interface, assumption, or shared meaning changes, mark affected evidence superseded and expand the check to the actual impact.

## 4. Review only when the mode requires it

A reviewer inspects the actual stable deliverable and its evidence against the same acceptance criteria. An independent reviewer must not have authored or modified the reviewed scope/version or participated in its repair. Disclose any overlap explicitly and label it self-review or limited review; a second pass by the author is not independent review. The reviewer does not edit the version being approved and does not add unrelated standards.

Use one of these outcomes:

- **PASS:** the reviewed scope and version meet their criteria. Close the overall task when no other required deliverable remains.
- **PASS with nonblocking notes:** record the notes and close if the promised result is usable. Do not create a repair phase for preferences or optional improvements.
- **FAIL:** identify the unmet criterion, concrete cause, and smallest repair that could resolve it.
- **HOLD:** state whether the cause is missing evidence, an external dependency, or a user decision. Do not rewrite a correct result while waiting for approval.
- **STOP:** state whether it stops an attempt, a deliverable, or the authorized objective. Do not infer broader closure from the label.

A verdict covers only its named version and scope. A partial PASS, idle worker, or successful service state never proves that the whole objective is complete.

## 5. Repair, then stop

Classify every finding before changing anything:

1. **Blocking:** the result is wrong, incomplete, unsafe, unauthorized, or unusable for the promised purpose. Repair it before delivery.
2. **Material:** it affects an important claim, dependency, mapping, or acceptance condition. Repair it when the correction is within scope and has a credible path.
3. **Minor:** it does not affect the promised use. Fix it only if the change is cheap and local; otherwise disclose it briefly.
4. **Optional:** style, preference, extra robustness, or future improvement. Do not add it to the current task.

For a repair, change the smallest responsible part, then rerun only the checks affected by that change and the prior blocker. The default for Direct and Assisted work is one targeted repair and recheck. After every repair in any mode, compare remaining findings with the locked acceptance contract. Continue only for an in-scope mandatory finding with a concrete repair and evidence of material improvement. Repeating a patch without new information, or naming a new finding without changing the acceptance need, is a workflow failure, not diligence. New phases, reports, or findings do not restart the workflow or expand its scope.

Close as soon as all mandatory criteria pass. Do not pursue speculative completeness, historical cleanup, or “nice to have” hardening after acceptance. If the same finding persists, the repair has no credible path, or the next remedy changes objectives, cost, risk, or authorization, stop the affected work and present the concrete choice. Preserve the current result and evidence; do not accumulate patches to avoid acknowledging a boundary.

## 6. Coordinate only active Assisted or Reviewed work

For a delegated deliverable, send a minimum task packet: outcome, constraints, named inputs and versions, acceptance criteria, owned scope, expected evidence, and a natural checkpoint. Keep one compact status/evidence entry for that deliverable. Do not create a new report for every update.

Monitor evidence rather than forcing messages. Quiet thinking or editing is not a hang; a PID, `running` label, or timestamp is not proof of progress. Send one targeted inquiry after a genuinely missed checkpoint, then allow a response window while doing independent authorized work. Reuse a worker only through a host operation that actually starts a new turn; never promise background monitoring the host cannot provide.

After a worker or reviewer event, ask only:

1. Is the named deliverable present at the version being discussed?
2. Which acceptance item is still blocking it?
3. Is there an authorized next action, or is a real external/user decision required?

If the answer to the second question is “none” and no required deliverable remains, close. Do not keep the session open to improve the process itself.

## 7. Authorization boundaries and unexpected events

Proceed with ordinary corrections and verification already covered by the task. Pause dependent work before a new external side effect, possible loss of unique data, conflicting authoritative instructions, or a change to objective, cost, commitment, or acceptance criteria.

Preserve recoverable state and evidence, finish safe preparation, and report the verified impact, uncertainty, recommended action, alternatives, and exact decision needed. Wait for explicit user direction for the dependent action; silence is not approval. Existing authorization remains valid, so do not ask again for work it already covers.

## 8. Closure and handoff

A result is closed when its mandatory criteria have evidence, blocking findings are resolved, and no required deliverable or review is missing. The final response states what was delivered, the checks that matter, material limitations, and any genuine open dependency. Optional suggestions are not new work.

For an ongoing handoff, preserve the authoritative task reference, current result/version, verified facts, relevant evidence and provenance locations (including material negative results and failures), open findings, authorization, owner/state, and next executable action. Inspect current state on resumption because another worker may have changed it.

### Portable archives

Use this subsection only when the delivery promises an archive or portable handoff:

1. Define the current required inputs, outputs, evidence, and portability claim. Historical references do not automatically become current dependencies.
2. For a complex result handoff, review content, critical mappings, and promised portability. Any claim of independent recomputation or portable execution must be tested from an isolated extraction without reads from the original workspace, regardless of archive complexity.
3. Finish required content reports before freezing the delivery directory. Keep build logs, temporary files, and acceptance receipts outside it. Do not modify the directory while archiving.
4. Build the archive and check the members, relevant hashes, and extraction usability promised by the task. Simple compression needs only the checks its promise requires.
5. If an acceptance receipt is produced, keep it outside the archive. For a complex handoff, bind it to the archive hash, size, checked scope, and verdict. Never reopen an accepted archive merely to insert its own final receipt.

Environment migration preserves task semantics: verify conditions that affect behavior and record identity when useful, but do not invent universal UUID, hostname, or absolute-path equality. Hardware and topology constraints come from the task's contract.

## 9. What this skill does not require

It does not require three agents, a repository, code tests, a phase file, a formal report, a fixed polling interval, a fixed number of review rounds, or a separate approval document for every task. Add those only when the current deliverable's risk or acceptance criteria make them useful.
