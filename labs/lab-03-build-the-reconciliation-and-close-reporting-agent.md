# Lab 3 — Build the Reconciliation and Close-Reporting Agent

**Course:** Agentic AI for Finance<br>
**Course Code:** C057<br>
**Version:** v1.0 (29 July 2026)<br>
**Topic 2:** Automating Financial Workflows with AI Agents<br>
**Maps to:** LO2: automate reporting and reconciliation with deterministic matching, adjusted balances and owned exceptions<br>
**Duration:** 55 minutes<br>
**Tools:** Spreadsheet · text editor · approved AI assistant · CASH_LEDGER_JUN · BANK_JUN · BUDGET_ACTUAL_JUN

---

## Goal

Reconcile the June cash ledger to the bank and draft a source-led close brief from verified figures.

## What You Will Do

You will use deterministic matching before asking the model to classify or explain anything. The completed reconciliation must account for every source row, prove equal adjusted balances and feed only verified exceptions and budget variances into the close-report prompt.

## What You Will Build

02-automation/reconciliation-june.csv, exception-queue.csv, adjusted-balance-proof.md, june-close-brief.md and run-evidence/L03-reconciliation-run.md.

## Prerequisites

- Completed Agent Foundation v0.2, including the three PASS source checks.
- Opening cash balance is SGD 50,000 in both records.
- Exact match rule: Reference and Amount_SGD must both agree; do not use a tolerance in this synthetic case.

> **Data note.** Use only the supplied synthetic Northstar Components data or information you are authorised to process. Do not paste credentials, personal data, customer records or confidential financial information into an unapproved AI service. A named finance owner verifies every material figure, classification and action.

## Steps

### 1. (12 minutes) Import cash-ledger.csv and bank-statement.csv into separate spreadsheet tables. Add Match_Count and Match_Status to each table. Use COUNTIFS on Reference and Amount_SGD against the other table. Mark MATCHED only when Match_Count = 1; route zero or multiple matches to the exception queue.

```text
Ledger example: =COUNTIFS(Bank[Reference],[@Reference],Bank[Amount_SGD],[@Amount_SGD])
Bank example: =COUNTIFS(Ledger[Reference],[@Reference],Ledger[Amount_SGD],[@Amount_SGD])
Expected exact matched pairs = 7
```

### 2. (10 minutes) Create reconciliation-june.csv with Ledger_ID, Bank_ID, Reference, Ledger_Amount_SGD, Bank_Amount_SGD, Match_Rule and Status. Create exception-queue.csv for every unmatched row with Exception_ID, Source_ID, Source_Row_ID, Amount_SGD, Category, Evidence, Owner, Required_Action and Due_Date. Use only Outstanding payment, Bank fee, Bank interest or Investigation needed as categories.

```text
Expected exceptions:
Ledger L008 NS-1008 SGD -850 = Outstanding payment
Bank B008 BANK-FEE SGD -45 = Bank fee
Bank B009 BANK-INT SGD 25 = Bank interest
```

### 3. (8 minutes) Write adjusted-balance-proof.md. Calculate ledger ending balance and bank ending balance from the opening balance plus each signed movement. Adjust the bank for the outstanding payment and adjust the ledger for bank fee and interest. Show every formula and Source_ID.

```text
Ledger ending = 50,000 + 14,700 = 64,700
Bank ending = 50,000 + 15,530 = 65,530
Adjusted bank = 65,530 - 850 = 64,680
Adjusted ledger = 64,700 - 45 + 25 = 64,680
```

### 4. (8 minutes) Import budget-actual.csv. Add Variance_SGD and Direction. Use Actual minus Budget for revenue and Budget minus Actual for expenses so positive means favourable. Recalculate actual and budget operating profit independently. Mark the cloud and cost-of-goods rows as material because absolute variance is at least SGD 2,000.

```text
Revenue favourable variance = 125,000 - 120,000 = 5,000
COGS variance score = 66,000 - 70,000 = -4,000 (unfavourable)
Cloud variance score = 4,000 - 6,000 = -2,000 (unfavourable)
Operating profit variance = 17,500 - 16,500 = 1,000 favourable
```

### 5. (10 minutes) Give the assistant only the adjusted-balance proof, verified variance table and exception queue. Ask it to draft june-close-brief.md with Status, Reconciliation result, Material variances, Exceptions and owners, Hypotheses requiring evidence, Decisions requested and Source ledger. Prohibit journal text and unsupported causes.

```text
Draft from VERIFIED tables only. Cite Source_ID and row or Exception_ID for every amount.
Use SOURCE FACT, CALCULATION, HYPOTHESIS and UNKNOWN labels.
Do not propose or format a journal. Route bank-only items to Finance Manager review.
```

### 6. (7 minutes) Preserve the raw brief, review it against the spreadsheet and record every correction in a raw-to-final change log. Add reviewer and review time, run Test It, answer the Reflection, then record all tools, checks, exceptions and decisions in L03-reconciliation-run.md.

```text
Evidence order: raw output → reviewer change log → final output → Test It result → Reflection
Release gate: 7 matched pairs | 3 exceptions | both adjusted balances 64,680 | operating-profit variance +1,000 | 0 unsupported causes
```

## Test It

The reconciliation must contain seven one-to-one matched pairs and the exception queue exactly three source rows. Ledger ending balance must be SGD 64,700, bank ending SGD 65,530 and both adjusted balances SGD 64,680. The close brief must cite every material amount, report operating-profit variance of SGD 1,000 favourable and contain no journal, payment or unsupported causal claim.

## Checkpoint and Rejoin Point

Freeze Reconciliation and Close v1.0. Labs 6–7 reuse the verified June results. To rejoin, use the exact match and adjusted-balance figures printed in this lab.

## Troubleshooting

| If this happens | Fix |
|---|---|
| One transaction matches more than once. | Do not pick the first row; route it to Investigation needed and inspect duplicate keys in both sources. |
| Adjusted balances differ by SGD 830. | Apply the SGD 850 outstanding payment to the bank side and the net SGD -20 bank-only movement to the ledger side. |
| The narrative invents a cause for cloud cost. | Relabel it HYPOTHESIS, state that workload evidence is missing and assign a validation action. |

## Challenge

Add a documented three-day date tolerance for a second-pass match and explain why amount, reference uniqueness and review evidence are still required.

## Reflection

Why should the model see the exception table only after deterministic matching and balance proof?

---

[← Lab 2](lab-02-connect-and-profile-approved-financial-data.md) · [Lab 4 →](lab-04-build-the-driver-based-forecasting-agent.md)
