# Lab 2 — Connect and Profile Approved Financial Data

**Course:** Agentic AI for Finance<br>
**Course Code:** C057<br>
**Version:** v1.0 (29 July 2026)<br>
**Topic 1:** Getting Started with Agentic AI for Finance<br>
**Maps to:** LO1: connect an agent to approved financial data with quality, lineage and least-privilege controls<br>
**Duration:** 50 minutes<br>
**Tools:** Spreadsheet · text editor · approved AI assistant · cash-ledger.csv · bank-statement.csv · budget-actual.csv

---

## Goal

Create reproducible data contracts and a validated read-only source package for the finance agent.

## What You Will Do

You will connect the foundation to three synthetic snapshots: cash ledger, bank statement and budget-versus-actual. Before any model sees the data, you will document grain and sign conventions, verify keys and control totals, remove unneeded fields and test whether the assistant cites stable Source_ID values.

## What You Will Build

01-foundation/source-manifest.csv, data-contracts.md, data-quality-report.md, approved-source-package.md and run-evidence/L02-grounding-test.md.

## Prerequisites

- Completed Agent Foundation v0.1 from Lab 1, or the printed rejoin fields.
- Open labs/assets/cash-ledger.csv, bank-statement.csv and budget-actual.csv.
- Confirm that Amount_SGD is signed: receipts and income are positive; payments and expenses are negative only in transaction files.

> **Data note.** Use only the supplied synthetic Northstar Components data or information you are authorised to process. Do not paste credentials, personal data, customer records or confidential financial information into an unapproved AI service. A named finance owner verifies every material figure, classification and action.

## Steps

### 1. (8 minutes) Copy the three CSV files into 01-foundation/source-snapshots/ without editing them. Create source-manifest.csv with Source_ID, File, Owner, Period_End, Grain, Currency, Sign_Convention, Row_Count, Control_Total and Retrieved_At. Use CASH_LEDGER_JUN, BANK_JUN and BUDGET_ACTUAL_JUN as Source_ID values.

```text
Expected row counts: CASH_LEDGER_JUN = 8 | BANK_JUN = 9 | BUDGET_ACTUAL_JUN = 6
Expected signed movement: cash ledger = SGD 14,700 | bank = SGD 15,530
Expected June operating profit: actual = SGD 17,500 | budget = SGD 16,500
```

### 2. (10 minutes) Validate each snapshot in the spreadsheet. Check that Transaction_ID for CASH_LEDGER_JUN, Bank_ID for BANK_JUN and Account for BUDGET_ACTUAL_JUN are complete and unique at the stated grain, dates are in June 2026, currency is SGD and numeric columns contain numbers. Record PASS or FAIL, observed value and repair owner in data-quality-report.md. Do not repair a source by silently deleting a row.

```text
Quality checks: required key complete | key unique | period valid | currency valid | numeric valid | row count | control total
Failure route: quarantine source → record defect → notify Data Owner → rerun all checks
```

### 3. (10 minutes) Create one data-contracts.md section per Source_ID. Record Purpose, Authoritative owner, Grain, Primary key, Fields, Units, Sign convention, Period, Refresh, Quality rules, Allowed use, Prohibited use, Retention and Lineage. State that all sources are synthetic, read-only snapshots for C057.

```text
Contract minimum: source + owner + grain + key + schema + unit + period + quality + permission + retention + lineage
```

### 4. (7 minutes) Create approved-source-package.md. Include only the source manifest, field definitions and the minimum rows needed for the FIN-01 prototype. Exclude Retrieved_At from prompts if it is not needed for analysis, and never include local paths, credentials or unrelated files. Update READ_GL and READ_BUDGET in the tool register with exact allowed Source_ID values.

```text
READ_GL allowed: CASH_LEDGER_JUN only
READ_BUDGET allowed: BUDGET_ACTUAL_JUN only
BANK_JUN is available only to the reconciliation workflow in Lab 3
```

### 5. (10 minutes) Give the assistant the C-L-E-A-R prompt and the approved source package. Ask for the three row counts, two signed movements and operating-profit values. Require Source_ID beside every result and UNKNOWN for any field not supplied. Save the raw response and your verification in L02-grounding-test.md.

```text
Return Metric, Value_SGD_or_Count, Formula_or_rule, Source_ID and Status.
Use only the supplied package. If a value is not present or derivable, return UNKNOWN and the missing Source_ID.
```

### 6. (5 minutes) Preserve the raw response, compare every returned value with the manifest and formulas, and record a raw-to-final change log. Mark each result VERIFIED or REJECTED, run Test It, answer the Reflection and promote the source package to v0.2 only if all seven expected values are correct and cited.

```text
Evidence order: raw output → reviewer change log → final output → Test It result → Reflection
Promotion gate: 3 row counts + 2 movements + 2 operating-profit values correct; 7/7 Source_ID citations; 0 invented values
```

## Test It

The manifest must contain exactly three Source_ID rows and the expected counts and totals. Each data contract must contain all 13 required fields. The quality report must show a result for every stated check. The grounding test must return seven correct values with seven valid Source_ID citations and zero unsupported fields. The tool register must restrict BANK_JUN to reconciliation.

## Checkpoint and Rejoin Point

Freeze Agent Foundation v0.2 with the three source snapshots, manifest, contracts and quality report. Lab 3 uses the cash and bank snapshots. To rejoin, reproduce the expected counts, movements and operating-profit checks above.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The spreadsheet imports amounts as text. | Use the application's Text to Columns or number conversion, then rerun numeric and control-total checks without changing source values. |
| The assistant cites a filename instead of Source_ID. | Require the stable Source_ID column in the output schema and reject any material value without it. |
| The manifest total differs from the expected value. | Check the signed Amount_SGD column and include each unique source row once; quarantine the source if the difference remains. |

## Challenge

Design a live-query version of CASH_LEDGER_JUN with parameters Entity, Period_End and Account, then name the validation and rate-limit controls required before it could replace the snapshot.

## Reflection

Which data-contract field would most quickly expose a comparison between incompatible financial values?

---

[← Lab 1](lab-01-design-the-finance-agent-charter-and-prompt-contract.md) · [Lab 3 →](lab-03-build-the-reconciliation-and-close-reporting-agent.md)
