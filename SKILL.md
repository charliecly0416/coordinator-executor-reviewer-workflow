---
name: coordinator-executor-reviewer-workflow
description: Coordinate tasks through a coordinator, executor, and reviewer across any domain. Use when the user explicitly requests this role framework, independent review, or complex delegated work that needs sustained coordination and acceptance decisions. Apply to technical and nontechnical work; adapt verification to the task. Do not trigger a multi-agent workflow merely because an ordinary task has several steps.
---

# Coordinator Executor Reviewer Workflow

## Choose the Smallest Sufficient Execution Mode

Start each task or subtask by asking whether the current agent can complete it directly and self-check. Choose the mode from its actual content, consequences, and existing requirements; do not ask the user to classify routine work.

| Mode | Typical work | Default execution and verification |
|---|---|---|
| **Direct execution** | Status queries, routine requests for missing materials, organizing confirmed information, existing launch commands, copying verified files | The coordinator completes and self-checks the work. Check facts, paths, commands, and required files as relevant; the deliverable and a brief result are enough. No automatic subagents. |
| **Local verification** | Routine code fixes, format conversion, environment preparation for an agreed plan, packaging with real dependencies | One worker, normally the current agent, completes the work and tests the affected scope. Delegate only when useful; independent review needs a concrete risk or existing requirement. |
| **Independent review of critical deliverables** | Experiment-rule changes, logic affecting scientific results, important conclusions, complex result handoffs, explicitly required independent review | Separate execution from review. Review a stable deliverable and its core evidence; the coordinator accepts the result and routes repairs by impact. |

File type alone does not determine the mode. An ordinary instruction document can be delivered directly; a document changing evaluation metrics or authorization boundaries needs stronger checks. A simple archive is lightweight; a handoff promising independent recomputation needs dependency and portability verification.

A top-level request for this framework does **not** require independent approval of every internal action. Identify the deliverables and substantive changes that need independent review at the start. Routine notes, progress queries, path explanations, and summaries of agreed commands do not inherit review gates from the larger project. Continue authorized work that does not depend on a pending review.

Add roles only for substantive work that can proceed independently, a requirement for independent review, or important consequences of an unnoticed error. The benefit must justify dispatch, context transfer, and waiting. Do not create three agents merely to mirror three responsibilities or upgrade a small task because it belongs to a large project.

User requirements and acceptance criteria still apply. If independence is required but unavailable, preserve that gap and use only an authorized fallback. Label an author's check **self-review**; changing role names or making another pass is not independent approval.

For direct execution: read the necessary facts, produce the deliverable, check its accuracy and scope, then deliver it. Do not add execution locks, unrelated review waits, phase files, or renewed authorization for already approved work. The collaboration loop below applies only where delegation or independent review is actually needed.

## Purpose and Responsibilities

Use three responsibilities to carry an authorized task to a verified outcome:

- **Coordinator:** owns the objective, scope, dependencies, assignments when needed, user communication, acceptance, and continuation decisions.
- **Executor:** produces the assigned deliverable, verifies it appropriately, and reports evidence, gaps, and material uncertainty while continuing unaffected work.
- **Reviewer:** independently inspects the actual deliverable and evidence against the same requirements, ties findings to a version and method, distinguishes blocking from nonblocking findings, and recommends repairs or next work. The reviewer must not edit the deliverable and then call approval of those changes independent.

This framework applies to technical and nontechnical work. The actual task and relevant specialist skills determine domain standards, tools, and deliverables. It requires no particular repository, experiment, technology, code tests, or document structure. Follow the user's choice of agents, people, or self-execution.

## Establish the Task Contract

Identify the intended outcome, existing authorization, constraints, inputs, and definition of done from applicable instructions and evidence. Do not invent missing approval gates or guess authority from filenames.

For substantial work, keep one compact, coordinator-owned plan or existing task record covering the objective and non-goals, authoritative references, facts and assumptions, deliverables and dependencies, owners where needed, acceptance evidence, authorization boundaries, and remaining work. Use durable storage when available; otherwise state the persistence limits of a conversational record. Small tasks need only their deliverable and brief result.

No role may expand the objective or invent a new route beyond authorization. Resolve routine implementation choices within scope. If a material requirement is unclear, pause only dependent work and first resolve it from existing instructions before asking the user.

A meaningful phase has one primary outcome and clear acceptance criteria. Avoid vague assignments and artificial micro-phases that merely rename unfinished work. Keep unresolved requirements visible until met or explicitly revised within authorization. A service's `completed` label, preliminary analysis, or narrow passing check proves only what its evidence covers.

## Collaboration Loop for Delegated or Independently Reviewed Deliverables

Apply this loop to meaningful deliverables, **not every action**. Self-checked work does not require a reviewer verdict, dispatch acknowledgement, or separate acceptance file.

1. Dispatch a bounded outcome with relevant inputs and versions, constraints, owned scope, acceptance criteria, expected evidence, and a natural checkpoint. Verify that delegated work was accepted; do not describe rejected work as running.
2. Monitor relevant evidence and incorporate user steering. If no worker is active, resume/reassign required work or use authorized fallback; never wait for nonexistent output.
3. Inspect the actual completed deliverable and retain unmet criteria. Do not substitute a progress note for the requested result.
4. When required, review a stable version. A reviewer may prepare earlier but cannot approve unseen later work. Prevent conflicting edits and recheck changes by their impact.
5. Route findings by cause: `FAIL_NEEDS_REPAIR` requires correction; `HOLD` may mean repair, missing verification, an external input, or a user decision; assess each condition in `PASS_WITH_CONDITIONS`; `PASS` supports only the reviewed scope/version. Do not rework correct deliverables while waiting for external approval.
6. Continue executable authorized work until the whole objective is satisfied or a genuine decision boundary requires yielding.

### Coordinator session lifetime

A worker's verdict or terminal state is an event, not an instruction to end the coordinator session. After a material event, check which mandatory deliverables, dependencies, repairs, and reviews remain and what can execute next. A `STOP` may refer to one attempt, one phase, or the whole objective; determine its scope and authority before acting. A partial `PASS` does not close the overall task.

Keep one authoritative status and evidence entry per substantive phase. Update it at meaningful transitions with the owner, state, relevant observation time, evidence, open findings, and next action. States such as `executing`, `awaiting_review`, `repair_required`, `verified`, or `blocked_external` can help; no fixed state schema or separate state file is mandatory. Routine polls and user updates need no new reports or approval records.

Before the final answer, reconcile the whole authorized scope with verified evidence and remaining work. Attempt ordinary authorized repairs and alternatives first. End on completion, explicit user pause/handoff, or a genuine authorization, user-decision, or external dependency boundary. If the host forces interruption, preserve a truthful handoff; do not invent a session time limit or promise unverified background monitoring.

### Agent lifecycle and fallback

Use only capabilities and status semantics the host actually exposes. If agents, waits, progress channels, or persistent execution are unavailable, use supported equivalents and state material limitations.

Prefer reusing a suitable existing worker through a tool that starts a new turn; a plain message may not resume an idle agent. Interrupting activity does not imply thread deletion or slot reclamation. Use close/release only if available and verify its result. For thread-limit failures, try reuse or authorized fallback rather than spinning on unchanged errors. Continue independent work when a real dependency remains blocked.

## Monitoring and Context Economy

Read [Monitoring and decision examples](references/monitoring-and-decisions.md) only when managing delegated work, recovering a stall, or needing an optional report example.

Agree on natural evidence milestones and a reasonable silence window for delegated work. Completion depends on acceptance criteria, not a coordinator reply deadline. Context pressure calls for a truthful handoff, not omitted verification.

- **User updates:** follow host requirements and report material progress, uncertainty, and the next action. A user update does not require polling or messaging every agent.
- **Passive monitoring:** use relevant status, mailbox, artifacts, logs, and resource information. Avoid busy polling; use bounded waits that allow user steering.
- **Worker contact:** send new evidence, user steering, a scope correction, a real dependency, or one targeted inquiry after a missed checkpoint. Allow a reasonable response window while doing independent work. Do not demand premature reports or a quick `PASS`.

Quiet output or absence of a PID is not proof of a hang; a running label or timestamp is not proof of progress. Correlate relevant evidence over time. Intervene for user steering, verified safety/resource problems, unauthorized scope drift, or conflicting work, and record the reason. Resource limits protect the environment; they are not invented delivery deadlines.

Send the minimum sufficient task packet, then changed facts, evidence references, and open findings. Do not fork full history by default. Preserve access to original evidence; summaries do not replace it. Reuse unchanged instructions, read references only when relevant, and limit tool output to what informs the decision. Preserve full logs when actually required.

When cost matters, inspect available usage at meaningful checkpoints and reassess duplication or task boundaries. Do not impose arbitrary report lengths or drop acceptance criteria to save tokens. Word counts are not exact billing-token measurements.

## Evidence Integrity and Proportionate Verification

Acceptance criteria are requirements to verify, not obstacles to disable. Investigate failures using actual inputs and outputs. Do not delete required checks, invent defaults, hide failures or scientific negative results, or relabel incomplete work to obtain a positive verdict. Preserve meaningful failure history and provenance. Correcting a genuinely mistaken requirement needs justification within authorization and evidence that the revised check distinguishes valid from invalid outcomes.

Before adding a check, identify the specific error it could detect, the requirement it protects, and the deliverable affected by failure. A sentence or internal judgment is enough; do not create a document for every check. Prefer existing evidence and mature tools. Checks without a concrete risk or acceptance purpose do not become mandatory workflow.

Fit verification to the work: source checks for claims, reconciliation for calculations, factual accuracy and usability for documents, feasibility for plans, functional tests for software. Do not write code tests merely to satisfy a documentation formality. A successful exit or confident summary alone is insufficient.

Bind evidence to the relevant input, implementation, and output versions. After a fix, recheck the change, prior blockers, and affected dependencies; unaffected evidence remains valid. Expand verification when shared semantics, inputs, interfaces, assumptions, or uncertain impact invalidate earlier evidence. For example:

- Document formatting: check the document; do not rerun experiments.
- Additional result-table fields: verify the fields and table consistency; unchanged calculations need no new compute run.
- Result-calculation logic: recompute affected results and review that logic.
- Recompression of unchanged files: verify archive members and contents; scientific conclusions need no new review.
- Shared execution semantics: check all affected tasks, even if only one source file changed.

Adding a status file or review report does not automatically trigger full tests or experiments. Claims must match the scope and conditions of the evidence. Distinguish observations from assumptions, estimates from measurements, and findings from recommendations. Mark invalidated evidence superseded in the existing record and inform the user of material changes.

### Dependency scope and environment migration

Let the current delivery promise define required inputs, source, results, and evidence. Discover dependencies recursively when needed, but historical references do not automatically become current runtime dependencies. Repair missing necessary dependencies; accurately disclose missing historical material without claiming completeness. Never exclude a necessary current input merely by calling it historical.

Distinguish conditions that affect behavior, environment identities worth recording, and identities explicitly required to match. For migration to an environment meeting the necessary conditions, reuse existing inputs and configuration and verify what changed. Do not invent universal UUID, hostname, or absolute-path equality requirements. If such identity binding is necessary, explain its technical reason and applicable requirement. Hardware and topology constraints come from the task, not this workflow.

## Repeated Repairs and Workflow Rework

Reassess when the same blocker survives substantive repairs, progress stops converging, or evidence contradicts the approach. Retry limits and checkpoints come from the task contract; this template adds no fixed attempt cap or automatic stop quota. Renaming a phase does not erase unresolved findings.

Check whether the work still serves the authorized objective, whether the diagnosis explains the evidence, whether acceptance targets have shifted, whether dependencies or conflicting work caused the problem, and whether cost or risk exceeds agreed bounds. Record the diagnosis and next executable action in the existing task record. Continue credible in-scope corrections without redundant authorization.

Also inspect the workflow itself: waiting for roles, repeatedly reading the same evidence, repeated packaging, and chasing irrelevant historical dependencies can create avoidable rework. Fix boundaries and dependency order without weakening acceptance. Catching a workflow-induced defect is necessary repair, not proof that every added process step was beneficial. Do not claim precise savings without measurements.

If evidence shows no credible in-scope path, or a remedy requires changed objectives, constraints, costs, or authorization, pause affected work and present a concrete decision. Do not repeat ineffective repairs merely to avoid acknowledging a dead end.

## Unexpected Events and User Decisions

Pause dependent work when a material unexpected event falls outside the agreed repair/risk envelope or the next action genuinely needs new authorization. Examples include possible loss of important information, conflicting authoritative instructions, or new commitments beyond agreed bounds. Ordinary verification failures, expected repairs, worker silence, and complexity alone do not require renewed permission.

Preserve evidence and recoverable state; verify what is paused or still active. Complete safe preparation for a reviewable proposal, then explain the verified impact, uncertainty, recommended action, alternatives, and exact decision needed. Name the restriction or explain how the event exceeds the agreed scope. Await an explicit reply for dependent actions; elapsed time and silence are not approval. Existing authorization remains valid. Continue unaffected authorized work and resume dependent work from the preserved state after the decision.

## Closure and Handoff

Close when all mandatory criteria have verified evidence, blockers are resolved (or the user explicitly narrows scope), and no required work or review is unaccounted for. Nonblocking deferrals need a rationale, owner, and verification plan; they cannot hide unmet requirements. State the completed work, evidence, limitations, and actual follow-up. Optional suggestions are not new mandatory tasks.

### Archives and portable handoffs

Use this sequence only when the delivery includes an archive or portable handoff, with checks proportional to its promise:

1. Define the current dependency scope and acceptance criteria; finish necessary checks and produce a stable delivery directory.
2. For complex result handoffs, independently review content, critical mappings, and promised portability. If independent recomputation is promised, verify it from an isolated extraction without relying on the original workspace. Recheck repairs by impact.
3. If a content review report must be included, add it before freezing the directory. Keep build logs, temporary files, and final archive acceptance receipts outside it. Prevent concurrent edits while archiving.
4. Build the archive and check members, contents/hashes, and extraction usability as required. Repair real mismatches; fewer packaging rounds do not justify skipping acceptance.
5. For complex result handoffs, produce a final archive acceptance receipt. Save any **final archive acceptance receipt outside the archive**, bound to its SHA-256, size, checked scope, and verdict. A simple compression task does not need a separate receipt unless required by its acceptance criteria. Do not reopen an accepted archive merely to include its own final receipt. A task-specific requirement to embed a report must use a clearly defined inner-content scope; verification of the final archive bytes remains external.

For a simple compression task, member/content checks can suffice; do not automatically demand scientific recomputation or a portable-runtime audit.

For handoff of ongoing work, preserve authoritative references, remaining deliverables, accepted authorization, verified facts versus claims, active owners and last observed state, evidence versions, open findings, and the next action. Inspect current state on resumption because others may have changed it.

## Optional Report Examples

Use the [report examples](references/monitoring-and-decisions.md#optional-report-examples) only when they help a real reader or handoff. They are not a checklist of files to create. Small tasks need a deliverable plus a brief result; substantial work can update its existing record. Never add empty sections, approval documents, or duplicate summaries to satisfy a template.
