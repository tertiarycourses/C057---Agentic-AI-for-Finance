# Lab 7 — Build the Scenario Insight and Visualisation Agent

**Course:** Agentic AI for Finance<br>
**Course Code:** C057<br>
**Version:** v1.0 (29 July 2026)<br>
**Topic 3:** Analysis and Insights with AI Agents<br>
**Maps to:** LO3: analyse risk scenarios and communicate evidence-backed recommendations with an honest visual<br>
**Duration:** 55 minutes<br>
**Tools:** Spreadsheet with chart capability · text editor · approved AI assistant · Lab 4 forecast · Lab 6 verified analysis

---

## Goal

Turn the three forecast scenarios into a risk register, actionable insight chain and reconciled visual decision pack.

## What You Will Do

You will verify September scenario results, calculate one sensitivity, define monitoring triggers and create a chart that makes the range visible without implying probabilities. The agent supports explanation and action design; the spreadsheet owns the numbers.

## What You Will Build

03-analysis/scenario-summary.csv, scenario-risk-register.csv, scenario-insights.md, scenario-chart.xlsx or equivalent spreadsheet, chart-specification.md and run-evidence/L07-scenario-run.md.

## Prerequisites

- Completed Forecast v1.0 and Verified Analysis v1.0.
- If rejoining, recreate the Base, Downside and Upside assumptions from Lab 4.
- Use the same July–September horizon and SGD units for all scenarios.

> **Data note.** Use only the supplied synthetic Northstar Components data or information you are authorised to process. Do not paste credentials, personal data, customer records or confidential financial information into an unapproved AI service. A named finance owner verifies every material figure, classification and action.

## Steps

### 1. (10 minutes) Copy the nine Lab 4 forecast rows into scenario-summary.csv. Recalculate September revenue, COGS, operating expense and operating profit for all scenarios. Round display values to two decimals but preserve formulas and unrounded values.

```text
Expected September operating profit:
Base = SGD 20,099.99 | Downside = SGD 5,059.60 | Upside = SGD 29,483.42
```

### 2. (8 minutes) Add one sensitivity row: increase Base September COGS percentage from 56% to 57% while holding other drivers constant. Calculate the operating-profit change and label it sensitivity, not scenario.

```text
Base September revenue = SGD 136,590.88
A 1 percentage-point COGS increase reduces operating profit by SGD 1,365.91
```

### 3. (10 minutes) Create scenario-risk-register.csv with Risk_ID, Cause, Event, Effect, Indicator, Trigger, Scenario_Evidence, Preventive_Action, Contingent_Action, Owner and Review_Cadence. Include revenue contraction, COGS pressure and fixed operating-cost rigidity. Use observable triggers; do not attach scenario probabilities.

```text
Risk statement: Because <cause>, <uncertain event> may occur, leading to <effect>.
Trigger pattern: metric + threshold + period + action owner
```

### 4. (8 minutes) Give the assistant the verified scenario summary, sensitivity and risk register. Ask for scenario-insights.md with Claim, Evidence, Calculation, Limitation, Trigger, Recommended action, Owner, Due date and Success measure. Require at least one alternative action and state that scenarios are assumption sets.

```text
Rank by downside protection and decision relevance.
Do not assign likelihood or claim causation beyond the supplied driver model.
Cite Scenario + Month + Metric for every value.
```

### 5. (12 minutes) Select the tidy Scenario, Month and Operating_Profit_SGD columns and insert a PivotTable/PivotChart. Put Month in Rows/Axis, Scenario in Columns/Legend and Operating_Profit_SGD in Values; set aggregation to Sum and confirm one row per month-scenario. Choose a line chart titled 'Operating Profit by Scenario, July–September 2026', set y-axis to SGD and show the legend and end labels. Use a dashed Downside line and note: 'Scenarios are assumption sets, not probabilities.'

```text
PivotChart contract: Rows/Axis = Month | Columns/Legend = Scenario | Values = Sum of Operating_Profit_SGD
Equivalent method: first pivot to a wide Month, Base, Downside, Upside table, then insert the line chart.
Visible: units + legend + end labels + scenario caveat + source/as-of note
```

### 6. (7 minutes) Write chart-specification.md with source range, PivotChart fields, formulas, axis, series, line styles, title, caveat and accessibility description. Preserve raw model output, record a raw-to-final change log, reconcile all nine plotted values, run Test It, answer the Reflection and save the final decision pack in L07-scenario-run.md.

```text
Evidence order: raw output → reviewer change log → final output → Test It result → Reflection
Release gate: 9/9 plotted values match | 3 series visible | September checks 3/3 PASS | sensitivity correct | 0 probability claims
```

## Test It

September operating profit must be SGD 20,099.99 Base, SGD 5,059.60 Downside and SGD 29,483.42 Upside. The one-point COGS sensitivity must reduce Base September profit by SGD 1,365.91. The risk register must include three owned risks with observable triggers. The chart must visibly encode Scenario, show SGD and month, reconcile all nine values and state that scenarios are not probabilities.

## Checkpoint and Rejoin Point

Freeze Scenario Decision Pack v1.0. Lab 9 uses its output and controls in the deployment demonstration. To rejoin, reproduce the three September values and one-point sensitivity above.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The September value differs by a few cents. | Compound and calculate with unrounded values, then round only the displayed result to two decimals. |
| The chart title says 'by scenario' but only one line is visible. | Bind Scenario as the series field and keep all three scenario rows for each month in the source range. |
| The recommendation treats Downside as the most likely outcome. | Remove likelihood language and describe it as a coherent assumption set used for preparedness. |

## Challenge

Create a small-multiple or table alternative for a colour-blind reader and explain which version better supports exact financial comparison.

## Reflection

Which visual choice most reduced the risk of readers treating a scenario as a prediction?

---

[← Lab 6](lab-06-build-the-verified-financial-analysis-agent.md) · [Lab 8 →](lab-08-build-the-finance-agent-governance-and-evidence-pack.md)
