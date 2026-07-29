# Lab 8 — Build the Finance Agent Governance and Evidence Pack

**Course:** Agentic AI for Finance<br>
**Course Code:** C057<br>
**Version:** v1.0 (29 July 2026)<br>
**Topic 4:** Deploying and Governing Financial AI Agents<br>
**Maps to:** LO4: govern finance agents with security, access, accountability, audit evidence and incident controls<br>
**Duration:** 55 minutes<br>
**Tools:** Spreadsheet · text editor · approved AI assistant · Labs 1–7 artifacts · governance-reference.csv · agent-inventory-starter.csv · access-control-starter.csv · control-evidence-starter.csv · run-evidence-schema-starter.md · incident-runbook-starter.md

---

## Goal

Create the control matrix, access design, run-evidence schema and incident procedure for five finance agents and one shared foundation component.

## What You Will Do

You will turn five finance agents plus one shared foundation component into a governed inventory. You will apply least privilege, map controls to risk and responsible-AI outcomes, define a reconstructable run record and rehearse how to contain and investigate untrusted document content.

## What You Will Build

04-governance/agent-inventory.csv, access-control-matrix.csv, control-evidence-matrix.csv, run-evidence-schema.md, incident-runbook.md and run-evidence/L08-governance-review.md.

## Prerequisites

- Completed Labs 1–7 or use their printed checkpoints.
- Open labs/assets/governance-reference.csv.
- Treat framework mappings as governance aids; organisational legal, risk and compliance owners decide applicable obligations.

> **Data note.** Use only the supplied synthetic Northstar Components data or information you are authorised to process. Do not paste credentials, personal data, customer records or confidential financial information into an unapproved AI service. A named finance owner verifies every material figure, classification and action.

## Steps

### 1. (7 minutes) Copy the seeded agent-inventory-starter.csv to agent-inventory.csv. Review all six pre-populated FOUNDATION, CLOSE, FORECAST, INVOICE, ANALYSIS and SCENARIO entries. Replace the CLOSE and INVOICE owner labels with named course-team roles, or record why the seeded roles remain appropriate. Confirm each Purpose, Read_Tools, Human_Gates, Materiality and Fallback against Labs 1–7; do not add duplicate rows.

```text
Every entry already has a baseline owner and fallback; your task is targeted validation and two recorded owner decisions.
Write_Tools must remain NONE for all C057 sandbox agents.
```

### 2. (7 minutes) Copy the seeded access-control-starter.csv to access-control-matrix.csv and add Reconciliation_Status and Reviewer_Note. Split every inventory Read_Tools value on | and confirm it has exactly one matching READ row for that agent identity and Source_ID. Mark PASS only when FOUNDATION, CLOSE, FORECAST, INVOICE, ANALYSIS and SCENARIO are fully covered and the access matrix contains no undeclared source. Review the five seeded denials, expiry and revocation owner.

```text
Required cross-check: inventory source ↔ matching identity and Source_ID row ↔ READ permission ↔ allowed parameter
Least privilege = minimum identity + minimum source + minimum fields/period + minimum time + no unused action
```

### 3. (7 minutes) Copy the seeded control-evidence-starter.csv to control-evidence-matrix.csv. Review all eight risk rows, then add Control_Test and Test_Result columns. Write one observable test for Data leakage and one for Untrusted document instruction; record PASS or DEFECT after comparing the seeded prevention, detection, human response, evidence, owner and failure response with Labs 1–7. Retain only governance mappings that describe a relevant outcome.

```text
A framework label does not prove compliance.
Targeted completion: 2 control tests + 2 results; the eight seeded control rows remain reviewable.
```

### 4. (7 minutes) Copy run-evidence-schema-starter.md to run-evidence-schema.md. Complete Retention_Class and Sensitive_Field_Handling, name authorised reader roles and test the schema against one preserved Lab 5 run. Add any missing field needed to identify what the agent knew, did, checked, proposed and changed.

```text
Reconstruction question: can an independent reviewer identify what the agent knew, did, checked, proposed and changed?
```

### 5. (10 minutes) Copy incident-runbook-starter.md to incident-runbook.md and complete its six owner, timing, evidence and approval fields. Use INV-006 for a two-path tabletop. The safe path ignores the note as data, logs a security event and keeps REVIEW_CONFIDENCE; the control-failure path stops and contains any attempted unrelated access. Give the assistant only the control matrix and runbook; do not expose credentials or live systems.

```text
Scenario: retrieved document attempts to override instructions and request unrelated supplier data.
Expected safe path: ignore note → REVIEW_CONFIDENCE → security event → preserve evidence → add regression case
Control-failure path: unauthorised attempt → STOP → contain/revoke → notify owners → investigate
```

### 6. (7 minutes) Preserve the raw tabletop, review it against the runbook and record corrections in a raw-to-final change log. Repair any missing owner, evidence or timing; add reviewer, decision and next review date. Confirm no framework mapping is treated as blanket approval.

```text
Evidence order: raw output → reviewer change log → final output → Test It result → Reflection
Review gate: raw tabletop + explicit corrections + final runbook + reviewer decision
```

### 7. (10 minutes) Run Test It across the inventory-to-access cross-check, both targeted control tests, the schema reconstruction and both incident paths. Fix defects, save the Test It result, answer the Reflection and record the release decision in L08-governance-review.md.

```text
Release gate: 6 inventory rows (5 agents + 1 foundation) | every Read_Tool covered once | no undeclared source | no write tools | 5 denied actions | 8 seeded risk rows + 2 executed control tests | complete run schema | safe and failure incident paths rehearsed
```

## Test It

The inventory must contain six named entries—five finance agents and one shared foundation component—each with owners, materiality and fallback, and Write_Tools must be NONE throughout. Every inventory Read_Tool must have one matching approved access row and the access matrix must contain no undeclared source, while denying the five stated actions. The control matrix must contain at least eight risk rows with prevention, detection, human response, evidence and owner, plus executed tests for data leakage and untrusted content. The run schema must support reconstruction, and the incident rehearsal must preserve evidence and create a regression case for both paths. INV-006 must stay REVIEW_CONFIDENCE when its note is safely ignored; an unauthorised attempt must STOP and trigger containment. No framework mapping may be described as proving compliance.

## Checkpoint and Rejoin Point

Freeze Governance Pack v1.0. Lab 9 uses the access, evidence and incident controls as release gates. To rejoin, use the exact inventory, access, risk and run-schema fields above.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The inventory assigns every role to 'Finance'. | Name distinct business, data, technology and control ownership; one person may fill roles only where segregation remains acceptable. |
| The run log stores full sensitive source content. | Retain stable identifiers, versions, protected locations and necessary evidence under an approved retention and access rule. |
| The matrix says 'compliant with FEAT'. | Replace the claim with the specific governance outcome, evidence, owner and a note for compliance review. |

## Challenge

Add a controlled write-enabled future state for DRAFT_INVOICE and identify the identity, idempotency, approval, rollback and evidence changes required before that tool could exist.

## Reflection

Which evidence field would be most important during an investigation, and who should be allowed to read it?

---

[← Lab 7](lab-07-build-the-scenario-insight-and-visualisation-agent.md) · [Lab 9 →](lab-09-evaluate-monitor-and-deploy-the-finance-agent-portfolio.md)
