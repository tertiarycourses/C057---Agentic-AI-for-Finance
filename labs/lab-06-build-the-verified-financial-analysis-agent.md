# Lab 6 — Build the Verified Financial Analysis Agent

**Course:** Agentic AI for Finance<br>
**Course Code:** C057<br>
**Version:** v1.0 (29 July 2026)<br>
**Topic 3:** Analysis and Insights with AI Agents<br>
**Maps to:** LO3: produce traceable financial analysis from reconciled metrics and evidence<br>
**Duration:** 55 minutes<br>
**Tools:** Spreadsheet · text editor · approved AI assistant · historical-monthly.csv · budget-actual.csv · Lab 3 close proof

---

## Goal

Calculate the June performance metrics and turn them into a fact–calculation–hypothesis insight chain.

## What You Will Do

You will define metric contracts before calculating trends, margins and variances. The agent then organises the verified results into material findings and validation questions, while unsupported causes remain explicitly labelled hypotheses.

## What You Will Build

03-analysis/metric-contracts.csv, verified-analysis.csv, insight-evidence-chain.md, finance-analysis-brief.md and run-evidence/L06-analysis-run.md.

## Prerequisites

- Completed Lab 3 or use the verified June actual and budget operating-profit values.
- Open labs/assets/historical-monthly.csv and labs/assets/budget-actual.csv.
- Use the same period, SGD units and account definitions in every comparison.

> **Data note.** Use only the supplied synthetic Northstar Components data or information you are authorised to process. Do not paste credentials, personal data, customer records or confidential financial information into an unapproved AI service. A named finance owner verifies every material figure, classification and action.

## Steps

### 1. (10 minutes) Create metric-contracts.csv with Metric_ID, Metric, Decision_Question, Formula, Numerator, Denominator, Period, Unit, Comparator, Exclusions, Source_ID, Owner and Materiality. Add Revenue, Gross_profit, Operating_profit, Gross_margin, Operating_margin, Revenue_MoM and Budget_variance.

```text
Gross profit = Revenue - COGS
Operating profit = Revenue - COGS - Payroll - Cloud - Marketing - Other
Gross margin = Gross profit / Revenue
Operating margin = Operating profit / Revenue
Revenue MoM = (June revenue - May revenue) / May revenue
```

### 2. (12 minutes) Recalculate the six-month rows in historical-monthly.csv and reconcile June to budget-actual.csv. Create verified-analysis.csv with Metric_ID, Period, Value, Unit, Comparator_Value, Change, Formula, Source_ID and Status. Mark a metric VERIFIED only when the source and calculation agree.

```text
Expected June: Revenue 125,000 | Gross profit 55,000 | Operating profit 17,500
Gross margin 44.0% | Operating margin 14.0% | Revenue MoM 5.93%
```

### 3. (8 minutes) Calculate material June variances. For revenue use Actual minus Budget; for expenses use Budget minus Actual so positive means favourable. Calculate Cloud versus May separately. Add materiality status using absolute budget variance of at least SGD 2,000.

```text
Revenue budget variance = SGD 5,000 favourable
COGS budget variance = SGD 4,000 unfavourable
Cloud budget variance = SGD 2,000 unfavourable = 50.0% over budget
Cloud versus May = SGD 1,800 increase = 42.86%
```

### 4. (10 minutes) Create insight-evidence-chain.md with Claim, Source evidence, Calculation, Limitation, Implication, Validation question, Owner and Due date. Give the assistant only verified-analysis.csv and the metric contracts. Ask it to rank three findings by materiality and decision relevance. Require UNKNOWN where operating-driver evidence is absent.

```text
Do not infer causes from timing alone.
Every amount or percentage requires Metric_ID and Source_ID.
Use HYPOTHESIS for a possible driver and name the evidence needed to validate it.
```

### 5. (8 minutes) Draft finance-analysis-brief.md with Executive view, Verified results, Material drivers, Hypotheses and unknowns, Recommendations, Decisions requested and Source ledger. Each recommendation must include Owner, Due date, Expected effect, Risk and Success measure.

```text
Insight chain: claim → evidence → calculation → limitation → implication → owned action
No recommendation may create a posting, payment or commitment.
```

### 6. (7 minutes) Preserve the raw brief, review it against metric contracts and record corrections in a raw-to-final change log. Remove unsupported causes, correct figures, record reviewer and decision time, run Test It, answer the Reflection, and save the complete evidence sequence in L06-analysis-run.md.

```text
Evidence order: raw output → reviewer change log → final output → Test It result → Reflection
Release gate: all six core metrics correct | four material variance checks correct | every claim cited | 0 unsupported causal statements
```

## Test It

Metric contracts must define formula, period, unit, comparator, exclusions, source, owner and materiality. June revenue must be SGD 125,000, gross profit SGD 55,000, operating profit SGD 17,500, gross margin 44.0%, operating margin 14.0% and revenue growth 5.93%. Cloud must be reported as SGD 2,000 and 50.0% over budget and SGD 1,800 or 42.86% above May. Every material narrative claim must cite a Metric_ID and Source_ID; unverified causes must remain HYPOTHESIS or UNKNOWN.

## Checkpoint and Rejoin Point

Freeze Verified Analysis v1.0. Lab 7 combines these results with the forecast scenarios. To rejoin, reproduce the ten exact metrics and variance checks printed above.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Expense variance direction is reversed. | Use Budget minus Actual for expenses when positive is defined as favourable, and state that convention in the metric contract. |
| Operating margin is calculated from gross profit. | Use operating profit as the numerator and June revenue as the denominator. |
| The brief says cloud migration caused the increase. | Change the statement to HYPOTHESIS and request workload or project evidence from the named owner. |

## Challenge

Add a contribution-margin metric only after defining which costs are variable, then explain why the supplied data may not support that classification.

## Reflection

Which metric became more useful after its decision question and materiality threshold were made explicit?

---

[← Lab 5](lab-05-design-the-invoice-exception-and-human-review-agent.md) · [Lab 7 →](lab-07-build-the-scenario-insight-and-visualisation-agent.md)
