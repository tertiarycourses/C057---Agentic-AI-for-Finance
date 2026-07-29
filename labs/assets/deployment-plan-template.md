# C057 Finance Agent Deployment Plan

## Use Case and Release Owner

- Agent: CLOSE
- Business owner: Financial Controller
- Data owner: Finance Data Owner
- Technology owner: AI Platform Owner
- Control owner: Finance Control Owner
- Manual fallback owner: Close Process Owner

## Stage 1 — Synthetic Sandbox

- Data: Supplied C057 synthetic snapshots only.
- Identity and permissions: C057-CLOSE-SANDBOX; read-only allowlist.
- Users: Course team and named builder.
- Capabilities: Reconcile and draft; no write actions.
- Evaluation gate: Ten-case suite passes all high-risk and arithmetic gates.
- Monitoring: Deterministic pass rate, exception accuracy, unsupported claims, latency, service failures.
- Support: AI Platform Owner and Close Process Owner.
- Approval: Finance Control Owner.
- Exit criteria: Evidence pack complete and zero unresolved high-risk defect.

## Stage 2 — Read-Only Shadow

- Data: Approved read-only finance snapshots for one entity and one closed period.
- Identity and permissions: Dedicated shadow identity; read-only allowlist; no posting.
- Users: Named close analysts and reviewers.
- Capabilities: Compare draft output with the approved manual close.
- Evaluation gate: Synthetic gate remains passed and one shadow-cycle reconciliation is complete.
- Monitoring: All Stage 1 metrics plus reviewer-change rate.
- Support: Close team and AI support route.
- Approval: Financial Controller and Finance Control Owner.
- Exit criteria: Material figures reconcile and fallback rehearsal passes.

## Stage 3 — Limited Pilot

- Data: Approved read-only snapshots for one entity and current close period.
- Identity and permissions: Dedicated pilot identity with time-limited read access.
- Users: Small named analyst group and named approvers.
- Capabilities: Draft reconciliation and close commentary; no posting.
- Evaluation gate: Two shadow cycles meet thresholds with no unresolved high-risk issue.
- Monitoring: Per-run controls plus weekly operational scorecard.
- Support: Defined service hours and manual fallback capacity.
- Approval: Financial Controller, Data Owner, Technology Owner, and Control Owner.
- Exit criteria: Pilot objectives met and rollback tabletop passes.

## Stage 4 — Controlled Production

- Data: Approved in-scope read-only finance products for one entity.
- Identity and permissions: Production identity with least privilege, expiry, and revocation owner.
- Users: Trained named analysts and approvers.
- Capabilities: Draft-only support with mandatory human decision.
- Evaluation gate: Release suite passes after every material change.
- Monitoring: Per-run evidence, threshold alerts, weekly review, and monthly control review.
- Support: Named business, technology, control, and manual-process owners.
- Approval: Formal release approval by all four owners.
- Exit criteria: Continued operation only while thresholds, evidence, fallback, and support remain healthy.

## Rollback and Manual Fallback

- Disable trigger: Any failed high-risk route, wrong material figure, prohibited action attempt, or unresolved severe incident.
- Decision authority: Finance Control Owner with Financial Controller.
- Access revocation: AI Platform Owner disables the identity and tokens.
- In-flight queue: Freeze, label, and preserve every item.
- Manual process: Return work to the approved close checklist.
- Reconciliation: Reconcile every in-flight item before restart.
- Evidence: Preserve run records, events, reviewer changes, and decisions.
- Restart approval: Retest and obtain Financial Controller plus Finance Control Owner approval.
