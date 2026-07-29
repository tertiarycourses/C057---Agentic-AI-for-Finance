"""Topic 3 labs for C057."""

DOMAIN3 = [
    dict(
        num=6,
        topic=3,
        title="Build the Verified Financial Analysis Agent",
        duration=55,
        objective="LO3: produce traceable financial analysis from reconciled metrics and evidence",
        goal="Calculate the June performance metrics and turn them into a fact–calculation–hypothesis insight chain.",
        workflow=["Define metrics", "Reconcile inputs", "Calculate results", "Build evidence chains", "Review the narrative"],
        desc=(
            "You will define metric contracts before calculating trends, margins and variances. The agent then organises the verified results "
            "into material findings and validation questions, while unsupported causes remain explicitly labelled hypotheses."
        ),
        build=(
            "03-analysis/metric-contracts.csv, verified-analysis.csv, insight-evidence-chain.md, "
            "finance-analysis-brief.md and run-evidence/L06-analysis-run.md."
        ),
        services="Spreadsheet · text editor · approved AI assistant · historical-monthly.csv · budget-actual.csv · Lab 3 close proof",
        prerequisites=[
            "Completed Lab 3 or use the verified June actual and budget operating-profit values.",
            "Open labs/assets/historical-monthly.csv and labs/assets/budget-actual.csv.",
            "Use the same period, SGD units and account definitions in every comparison.",
        ],
        steps=[
            (
                "(10 minutes) Create metric-contracts.csv with Metric_ID, Metric, Decision_Question, Formula, Numerator, Denominator, Period, "
                "Unit, Comparator, Exclusions, Source_ID, Owner and Materiality. Add Revenue, Gross_profit, Operating_profit, Gross_margin, "
                "Operating_margin, Revenue_MoM and Budget_variance.",
                "Gross profit = Revenue - COGS\n"
                "Operating profit = Revenue - COGS - Payroll - Cloud - Marketing - Other\n"
                "Gross margin = Gross profit / Revenue\n"
                "Operating margin = Operating profit / Revenue\n"
                "Revenue MoM = (June revenue - May revenue) / May revenue",
            ),
            (
                "(12 minutes) Recalculate the six-month rows in historical-monthly.csv and reconcile June to budget-actual.csv. Create "
                "verified-analysis.csv with Metric_ID, Period, Value, Unit, Comparator_Value, Change, Formula, Source_ID and Status. Mark "
                "a metric VERIFIED only when the source and calculation agree.",
                "Expected June: Revenue 125,000 | Gross profit 55,000 | Operating profit 17,500\n"
                "Gross margin 44.0% | Operating margin 14.0% | Revenue MoM 5.93%",
            ),
            (
                "(8 minutes) Calculate material June variances. For revenue use Actual minus Budget; for expenses use Budget minus Actual "
                "so positive means favourable. Calculate Cloud versus May separately. Add materiality status using absolute budget variance "
                "of at least SGD 2,000.",
                "Revenue budget variance = SGD 5,000 favourable\n"
                "COGS budget variance = SGD 4,000 unfavourable\n"
                "Cloud budget variance = SGD 2,000 unfavourable = 50.0% over budget\n"
                "Cloud versus May = SGD 1,800 increase = 42.86%",
            ),
            (
                "(10 minutes) Create insight-evidence-chain.md with Claim, Source evidence, Calculation, Limitation, Implication, Validation "
                "question, Owner and Due date. Give the assistant only verified-analysis.csv and the metric contracts. Ask it to rank three "
                "findings by materiality and decision relevance. Require UNKNOWN where operating-driver evidence is absent.",
                "Do not infer causes from timing alone.\n"
                "Every amount or percentage requires Metric_ID and Source_ID.\n"
                "Use HYPOTHESIS for a possible driver and name the evidence needed to validate it.",
            ),
            (
                "(8 minutes) Draft finance-analysis-brief.md with Executive view, Verified results, Material drivers, Hypotheses and unknowns, "
                "Recommendations, Decisions requested and Source ledger. Each recommendation must include Owner, Due date, Expected effect, "
                "Risk and Success measure.",
                "Insight chain: claim → evidence → calculation → limitation → implication → owned action\n"
                "No recommendation may create a posting, payment or commitment.",
            ),
            (
                "(7 minutes) Preserve the raw brief, review it against metric contracts and record corrections in a raw-to-final change log. "
                "Remove unsupported causes, correct figures, record reviewer and decision time, run Test It, answer the Reflection, and save "
                "the complete evidence sequence in L06-analysis-run.md.",
                "Evidence order: raw output → reviewer change log → final output → Test It result → Reflection\n"
                "Release gate: all six core metrics correct | four material variance checks correct | every claim cited | 0 unsupported causal statements",
            ),
        ],
        test=(
            "Metric contracts must define formula, period, unit, comparator, exclusions, source, owner and materiality. June revenue must be "
            "SGD 125,000, gross profit SGD 55,000, operating profit SGD 17,500, gross margin 44.0%, operating margin 14.0% and revenue growth "
            "5.93%. Cloud must be reported as SGD 2,000 and 50.0% over budget and SGD 1,800 or 42.86% above May. Every material narrative claim "
            "must cite a Metric_ID and Source_ID; unverified causes must remain HYPOTHESIS or UNKNOWN."
        ),
        checkpoint=(
            "Freeze Verified Analysis v1.0. Lab 7 combines these results with the forecast scenarios. To rejoin, reproduce the ten exact "
            "metrics and variance checks printed above."
        ),
        troubleshooting=[
            (
                "Expense variance direction is reversed.",
                "Use Budget minus Actual for expenses when positive is defined as favourable, and state that convention in the metric contract.",
            ),
            (
                "Operating margin is calculated from gross profit.",
                "Use operating profit as the numerator and June revenue as the denominator.",
            ),
            (
                "The brief says cloud migration caused the increase.",
                "Change the statement to HYPOTHESIS and request workload or project evidence from the named owner.",
            ),
        ],
        challenge=(
            "Add a contribution-margin metric only after defining which costs are variable, then explain why the supplied data may not support "
            "that classification."
        ),
        reflection="Which metric became more useful after its decision question and materiality threshold were made explicit?",
    ),
    dict(
        num=7,
        topic=3,
        title="Build the Scenario Insight and Visualisation Agent",
        duration=55,
        objective="LO3: analyse risk scenarios and communicate evidence-backed recommendations with an honest visual",
        goal="Turn the three forecast scenarios into a risk register, actionable insight chain and reconciled visual decision pack.",
        workflow=["Verify scenarios", "Measure sensitivity", "Define triggers", "Draft actions", "Build and reconcile the chart"],
        desc=(
            "You will verify September scenario results, calculate one sensitivity, define monitoring triggers and create a chart that makes "
            "the range visible without implying probabilities. The agent supports explanation and action design; the spreadsheet owns the numbers."
        ),
        build=(
            "03-analysis/scenario-summary.csv, scenario-risk-register.csv, scenario-insights.md, "
            "scenario-chart.xlsx or equivalent spreadsheet, chart-specification.md and run-evidence/L07-scenario-run.md."
        ),
        services="Spreadsheet with chart capability · text editor · approved AI assistant · Lab 4 forecast · Lab 6 verified analysis",
        prerequisites=[
            "Completed Forecast v1.0 and Verified Analysis v1.0.",
            "If rejoining, recreate the Base, Downside and Upside assumptions from Lab 4.",
            "Use the same July–September horizon and SGD units for all scenarios.",
        ],
        steps=[
            (
                "(10 minutes) Copy the nine Lab 4 forecast rows into scenario-summary.csv. Recalculate September revenue, COGS, operating expense "
                "and operating profit for all scenarios. Round display values to two decimals but preserve formulas and unrounded values.",
                "Expected September operating profit:\n"
                "Base = SGD 20,099.99 | Downside = SGD 5,059.60 | Upside = SGD 29,483.42",
            ),
            (
                "(8 minutes) Add one sensitivity row: increase Base September COGS percentage from 56% to 57% while holding other drivers constant. "
                "Calculate the operating-profit change and label it sensitivity, not scenario.",
                "Base September revenue = SGD 136,590.88\n"
                "A 1 percentage-point COGS increase reduces operating profit by SGD 1,365.91",
            ),
            (
                "(10 minutes) Create scenario-risk-register.csv with Risk_ID, Cause, Event, Effect, Indicator, Trigger, Scenario_Evidence, "
                "Preventive_Action, Contingent_Action, Owner and Review_Cadence. Include revenue contraction, COGS pressure and fixed operating-cost "
                "rigidity. Use observable triggers; do not attach scenario probabilities.",
                "Risk statement: Because <cause>, <uncertain event> may occur, leading to <effect>.\n"
                "Trigger pattern: metric + threshold + period + action owner",
            ),
            (
                "(8 minutes) Give the assistant the verified scenario summary, sensitivity and risk register. Ask for scenario-insights.md with "
                "Claim, Evidence, Calculation, Limitation, Trigger, Recommended action, Owner, Due date and Success measure. Require at least one "
                "alternative action and state that scenarios are assumption sets.",
                "Rank by downside protection and decision relevance.\n"
                "Do not assign likelihood or claim causation beyond the supplied driver model.\n"
                "Cite Scenario + Month + Metric for every value.",
            ),
            (
                "(12 minutes) Select the tidy Scenario, Month and Operating_Profit_SGD columns and insert a PivotTable/PivotChart. Put Month in "
                "Rows/Axis, Scenario in Columns/Legend and Operating_Profit_SGD in Values; set aggregation to Sum and confirm one row per "
                "month-scenario. Choose a line chart titled 'Operating Profit by Scenario, July–September 2026', set y-axis to SGD and show "
                "the legend and end labels. Use a dashed Downside line and note: 'Scenarios are assumption sets, not probabilities.'",
                "PivotChart contract: Rows/Axis = Month | Columns/Legend = Scenario | Values = Sum of Operating_Profit_SGD\n"
                "Equivalent method: first pivot to a wide Month, Base, Downside, Upside table, then insert the line chart.\n"
                "Visible: units + legend + end labels + scenario caveat + source/as-of note",
            ),
            (
                "(7 minutes) Write chart-specification.md with source range, PivotChart fields, formulas, axis, series, line styles, title, caveat "
                "and accessibility description. Preserve raw model output, record a raw-to-final change log, reconcile all nine plotted values, "
                "run Test It, answer the Reflection and save the final decision pack in L07-scenario-run.md.",
                "Evidence order: raw output → reviewer change log → final output → Test It result → Reflection\n"
                "Release gate: 9/9 plotted values match | 3 series visible | September checks 3/3 PASS | sensitivity correct | 0 probability claims",
            ),
        ],
        test=(
            "September operating profit must be SGD 20,099.99 Base, SGD 5,059.60 Downside and SGD 29,483.42 Upside. The one-point COGS sensitivity "
            "must reduce Base September profit by SGD 1,365.91. The risk register must include three owned risks with observable triggers. The chart "
            "must visibly encode Scenario, show SGD and month, reconcile all nine values and state that scenarios are not probabilities."
        ),
        checkpoint=(
            "Freeze Scenario Decision Pack v1.0. Lab 9 uses its output and controls in the deployment demonstration. To rejoin, reproduce the "
            "three September values and one-point sensitivity above."
        ),
        troubleshooting=[
            (
                "The September value differs by a few cents.",
                "Compound and calculate with unrounded values, then round only the displayed result to two decimals.",
            ),
            (
                "The chart title says 'by scenario' but only one line is visible.",
                "Bind Scenario as the series field and keep all three scenario rows for each month in the source range.",
            ),
            (
                "The recommendation treats Downside as the most likely outcome.",
                "Remove likelihood language and describe it as a coherent assumption set used for preparedness.",
            ),
        ],
        challenge=(
            "Create a small-multiple or table alternative for a colour-blind reader and explain which version better supports exact financial comparison."
        ),
        reflection="Which visual choice most reduced the risk of readers treating a scenario as a prediction?",
    ),
]
