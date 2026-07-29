# Lab 4 — Build the Driver-Based Forecasting Agent

**Course:** Agentic AI for Finance<br>
**Course Code:** C057<br>
**Version:** v1.0 (29 July 2026)<br>
**Topic 2:** Automating Financial Workflows with AI Agents<br>
**Maps to:** LO2: build a planning agent that calculates transparent scenarios and preserves assumption ownership<br>
**Duration:** 45 minutes<br>
**Tools:** Spreadsheet · text editor · approved AI assistant · historical-monthly.csv · forecast-drivers.csv

---

## Goal

Produce a three-month base, downside and upside forecast with deterministic formulas and model-supported challenge.

## What You Will Do

You will turn the verified June actual into a July–September driver model. The spreadsheet owns every calculation; the agent compares scenarios, challenges missing assumptions and drafts decision questions without silently changing the approved drivers.

## What You Will Build

02-automation/forecast-assumptions.csv, scenario-forecast.csv, forecast-challenge.md, forecast-pack.md and run-evidence/L04-forecast-run.md.

## Prerequisites

- Completed Lab 3 or use the verified June actual revenue of SGD 125,000.
- Open labs/assets/historical-monthly.csv and labs/assets/forecast-drivers.csv.
- Use Revenue growth, COGS percent and Operating expense as the only scenario drivers.

> **Data note.** Use only the supplied synthetic Northstar Components data or information you are authorised to process. Do not paste credentials, personal data, customer records or confidential financial information into an unapproved AI service. A named finance owner verifies every material figure, classification and action.

## Steps

### 1. (7 minutes) Copy forecast-drivers.csv to forecast-assumptions.csv. Add Assumption_Owner, Source, Approved_YN, Review_Date and Trigger. Confirm Base = 3% monthly revenue growth, 56% COGS and SGD 40,000 operating expense; Downside = -2%, 60% and SGD 42,000; Upside = 6%, 54% and SGD 39,000.

```text
Every driver requires value + unit + scenario + owner + source + approval + review date + trigger
```

### 2. (15 minutes) Create scenario-forecast.csv with Scenario, Month, Revenue_SGD, COGS_SGD, Operating_Expense_SGD and Operating_Profit_SGD. For July, multiply June revenue by 1 + growth. For August and September, compound from the prior month within the same scenario. Calculate COGS as revenue times the scenario rate and profit as revenue minus COGS minus expense.

```text
Revenue_t = Revenue_t-1 × (1 + growth)
COGS_t = Revenue_t × COGS_percent
Operating profit_t = Revenue_t - COGS_t - Operating expense_t
```

### 3. (7 minutes) Verify the first month before continuing. Base July revenue must be SGD 128,750 and operating profit SGD 16,650. Downside July profit must be SGD 7,000 and Upside July profit SGD 21,950. Record PASS or FAIL beside each formula.

```text
Base: 125,000 × 1.03 = 128,750; 128,750 - 72,100 - 40,000 = 16,650
Downside: 122,500 - 73,500 - 42,000 = 7,000
Upside: 132,500 - 71,550 - 39,000 = 21,950
```

### 4. (8 minutes) Give the assistant the approved assumptions, historical-monthly.csv and verified scenario table. Ask for forecast-challenge.md with Assumption, Evidence, Sensitivity, Missing dependency, Validation question and Trigger. Require it to preserve all approved values and to label any proposed alternative as OPTION.

```text
Challenge, do not rewrite. Return one row per driver.
Distinguish supplied evidence, calculation, option and unknown.
Do not assign probability to a scenario.
```

### 5. (8 minutes) Create forecast-pack.md with baseline, scenario table, sensitivities, assumptions, limitations, trigger and decisions requested. Preserve the raw model draft, record a raw-to-final change log and your decision on each OPTION, run Test It, answer the Reflection and save all evidence in L04-forecast-run.md.

```text
Evidence order: raw output → reviewer change log → final output → Test It result → Reflection
Release gate: 9 month-scenario rows | first-month checks 3/3 PASS | assumptions unchanged unless human decision recorded | 0 probability claims
```

## Test It

The assumption file must contain all nine scenario-driver rows with owner, source, approval, date and trigger. The forecast must contain nine month-scenario rows using one formula pattern. July operating profit must be SGD 16,650 Base, SGD 7,000 Downside and SGD 21,950 Upside. The challenge must preserve approved values and label alternatives as OPTION, not prediction.

## Checkpoint and Rejoin Point

Freeze Forecast v1.0 with the assumptions and nine-row scenario table. Lab 7 uses it for risk and visualisation. To rejoin, recreate the three July checks above.

## Troubleshooting

| If this happens | Fix |
|---|---|
| August revenue is calculated from June instead of July. | Within each scenario, reference the immediately prior month's revenue so growth compounds. |
| The assistant changes the COGS percentage. | Restore the approved value and record the suggestion only as an OPTION with owner and decision. |
| Scenario results are described as probabilities. | Replace probability language with named assumption sets and state that scenarios are not likelihood estimates. |

## Challenge

Calculate the revenue-growth breakpoint at which September downside operating profit becomes zero, holding the other downside drivers constant.

## Reflection

Which driver has the clearest management owner, and which one needs better evidence before workplace use?

---

[← Lab 3](lab-03-build-the-reconciliation-and-close-reporting-agent.md) · [Lab 5 →](lab-05-design-the-invoice-exception-and-human-review-agent.md)
