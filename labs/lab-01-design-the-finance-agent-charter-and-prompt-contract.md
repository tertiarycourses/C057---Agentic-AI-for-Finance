# Lab 1 — Design the Finance Agent Charter and Prompt Contract

**Course:** Agentic AI for Finance<br>
**Course Code:** C057<br>
**Version:** v1.0 (29 July 2026)<br>
**Topic 1:** Getting Started with Agentic AI for Finance<br>
**Maps to:** LO1: design a bounded finance agent with instructions, tools, limits and human review<br>
**Duration:** 55 minutes<br>
**Tools:** Spreadsheet · text editor · approved AI assistant · agent-use-case-register.csv · data-dictionary.csv

---

## Goal

Turn one finance use case into a testable agent charter, tool-risk register and C-L-E-A-R prompt contract.

## What You Will Do

You will select the monthly-close reporting use case from the supplied register and define what the agent may read, calculate and draft. You will separate deterministic controls from model judgement, specify stop conditions and create a reusable prompt contract that preserves finance ownership.

## What You Will Build

01-foundation/finance-agent-charter.md, tool-risk-register.csv, prompt-contract.md and run-evidence/L01-tabletop-run.md for a read-only June close-report agent.

## Prerequisites

- Create the C057-Northstar-Finance-Agent folder structure shown in the Learner Guide setup section.
- Open labs/assets/agent-use-case-register.csv and labs/assets/data-dictionary.csv.
- Use only the synthetic Northstar Components scenario; do not substitute workplace data.

> **Data note.** Use only the supplied synthetic Northstar Components data or information you are authorised to process. Do not paste credentials, personal data, customer records or confidential financial information into an unapproved AI service. A named finance owner verifies every material figure, classification and action.

## Steps

### 1. (8 minutes) Copy row FIN-01 from agent-use-case-register.csv into finance-agent-charter.md. Add headings Goal, Authorised user, Trigger, Completion condition, In scope, Out of scope, Source boundary, Deterministic controls, Model judgement, Human owner, Stop conditions, Evidence retained and Manual fallback.

```text
Selected use case: FIN-01 — Draft the June monthly-close variance brief
Completion condition: reconciled figures + cited draft + finance-manager review queue
Out of scope: journal posting | payment | supplier-master change | external distribution
```

### 2. (10 minutes) Complete every charter heading. State that arithmetic, transaction matching, thresholds and adjusted balances are deterministic. Limit model work to planning, exception classification, questions and narrative drafting. Add stop conditions for missing source, failed control total, unclear currency, tool error, maximum five turns and any write request.

```text
Stop and escalate when: source missing | total fails | currency unknown | confidence insufficient | write requested | 5 turns reached | permission denied
```

### 3. (10 minutes) Create tool-risk-register.csv with columns Tool_ID, Tool, Access_Mode, Data_Class, Financial_Impact, Reversible, Allowed_Parameters, Prohibited_Parameters, Human_Gate and Evidence. Add READ_GL, READ_BUDGET, CALCULATE, DRAFT_BRIEF and PUBLISH_BRIEF. Allow the first four only in read or draft mode; mark PUBLISH_BRIEF prohibited for the pilot.

```text
Risk rule:
Read + synthetic/restricted view + no external effect = LOW
Draft record + no posting = MEDIUM and review required
Post, pay, master-data change or external send = HIGH and prohibited in this pilot
```

### 4. (12 minutes) Write prompt-contract.md using C-L-E-A-R: Context, Ledger sources, Execution steps, Acceptance checks and Reviewer/escalation. Require output sections Source manifest, Verified calculations, Material variances, Hypotheses, Unknowns, Proposed commentary and Reviewer checklist. Require a Source_ID beside every material figure.

```text
CONTEXT: Northstar Components June close; SGD; draft only.
LEDGER SOURCES: use only <SOURCE_ID> blocks supplied below.
EXECUTION: validate → calculate with stated formulas → classify → draft.
ACCEPTANCE: totals reconcile; no unsupported figure; FACT/HYPOTHESIS/UNKNOWN separated.
REVIEWER: route to Finance Manager; stop on failed check or write request.
```

### 5. (10 minutes) Give the charter, tool register and prompt contract to the approved assistant. Ask it to simulate one run with a missing budget source and a request to post a journal. Record each planned step, selected tool and stop reason in run-evidence/L01-tabletop-run.md. Do not provide any real data.

```text
Tabletop only. Scenario A: BUDGET_ACTUAL_JUN is missing.
Scenario B: user says 'post the correcting journal now'.
Return Run_step, Proposed_tool, Allowed_YN, Control, Outcome and Escalation. Do not execute tools.
```

### 6. (5 minutes) Preserve the raw simulation, review it yourself and record every correction in a raw-to-final change log. Add Human decision, Reviewer, Decision time and Next action, then run the Test It checks and answer the Reflection before marking the charter v0.1 — sandbox.

```text
Evidence order: raw output → reviewer change log → final output → Test It result → Reflection
Expected: both scenarios STOP; no figure is invented; no write tool is called; Finance Manager receives a clear next action.
```

## Test It

The charter must contain all 13 headings and one measurable completion condition. The tool register must contain exactly five Tool_ID rows, with PUBLISH_BRIEF prohibited and every non-read action assigned a human gate. The prompt must contain all five C-L-E-A-R sections and require Source_ID, FACT/HYPOTHESIS/UNKNOWN separation and a reviewer checklist. Both tabletop scenarios must stop with no invented data and no write action.

## Checkpoint and Rejoin Point

Keep the four files as Agent Foundation v0.1. Lab 2 adds governed source contracts. To rejoin, use FIN-01 and the exact charter, tool-register and C-L-E-A-R fields printed in this lab.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The agent charter says 'analyse finance data' without a finish condition. | Name the period, output, control checks, review queue and final status that prove completion. |
| Every tool is labelled low risk. | Rate data sensitivity, financial impact, reversibility and external effect separately; draft and publish are not equivalent. |
| The assistant continues after a missing source. | Move the source check before calculation and state STOP, UNKNOWN and the named escalation route. |

## Challenge

Add an alternative FIN-02 reconciliation charter and identify exactly which instructions, tools and controls can be reused without copying FIN-01 assumptions.

## Reflection

Which single boundary most reduced the risk of a fluent but financially unsafe result?

---

[← Labs index](README.md) · [Lab 2 →](lab-02-connect-and-profile-approved-financial-data.md)
