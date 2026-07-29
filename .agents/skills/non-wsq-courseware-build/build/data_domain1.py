"""Topic 1 labs for C057."""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="Design the Finance Agent Charter and Prompt Contract",
        duration=55,
        objective="LO1: design a bounded finance agent with instructions, tools, limits and human review",
        goal="Turn one finance use case into a testable agent charter, tool-risk register and C-L-E-A-R prompt contract.",
        workflow=["Select the use case", "Bound the agent", "Rate the tools", "Write the prompt", "Tabletop-test the run"],
        desc=(
            "You will select the monthly-close reporting use case from the supplied register and define what the agent may read, "
            "calculate and draft. You will separate deterministic controls from model judgement, specify stop conditions and create "
            "a reusable prompt contract that preserves finance ownership."
        ),
        build=(
            "01-foundation/finance-agent-charter.md, tool-risk-register.csv, prompt-contract.md and "
            "run-evidence/L01-tabletop-run.md for a read-only June close-report agent."
        ),
        services="Spreadsheet · text editor · approved AI assistant · agent-use-case-register.csv · data-dictionary.csv",
        prerequisites=[
            "Create the C057-Northstar-Finance-Agent folder structure shown in the Learner Guide setup section.",
            "Open labs/assets/agent-use-case-register.csv and labs/assets/data-dictionary.csv.",
            "Use only the synthetic Northstar Components scenario; do not substitute workplace data.",
        ],
        steps=[
            (
                "(8 minutes) Copy row FIN-01 from agent-use-case-register.csv into finance-agent-charter.md. Add headings Goal, "
                "Authorised user, Trigger, Completion condition, In scope, Out of scope, Source boundary, Deterministic controls, "
                "Model judgement, Human owner, Stop conditions, Evidence retained and Manual fallback.",
                "Selected use case: FIN-01 — Draft the June monthly-close variance brief\n"
                "Completion condition: reconciled figures + cited draft + finance-manager review queue\n"
                "Out of scope: journal posting | payment | supplier-master change | external distribution",
            ),
            (
                "(10 minutes) Complete every charter heading. State that arithmetic, transaction matching, thresholds and adjusted "
                "balances are deterministic. Limit model work to planning, exception classification, questions and narrative drafting. "
                "Add stop conditions for missing source, failed control total, unclear currency, tool error, maximum five turns and any write request.",
                "Stop and escalate when: source missing | total fails | currency unknown | confidence insufficient | "
                "write requested | 5 turns reached | permission denied",
            ),
            (
                "(10 minutes) Create tool-risk-register.csv with columns Tool_ID, Tool, Access_Mode, Data_Class, Financial_Impact, "
                "Reversible, Allowed_Parameters, Prohibited_Parameters, Human_Gate and Evidence. Add READ_GL, READ_BUDGET, CALCULATE, "
                "DRAFT_BRIEF and PUBLISH_BRIEF. Allow the first four only in read or draft mode; mark PUBLISH_BRIEF prohibited for the pilot.",
                "Risk rule:\n"
                "Read + synthetic/restricted view + no external effect = LOW\n"
                "Draft record + no posting = MEDIUM and review required\n"
                "Post, pay, master-data change or external send = HIGH and prohibited in this pilot",
            ),
            (
                "(12 minutes) Write prompt-contract.md using C-L-E-A-R: Context, Ledger sources, Execution steps, Acceptance checks "
                "and Reviewer/escalation. Require output sections Source manifest, Verified calculations, Material variances, "
                "Hypotheses, Unknowns, Proposed commentary and Reviewer checklist. Require a Source_ID beside every material figure.",
                "CONTEXT: Northstar Components June close; SGD; draft only.\n"
                "LEDGER SOURCES: use only <SOURCE_ID> blocks supplied below.\n"
                "EXECUTION: validate → calculate with stated formulas → classify → draft.\n"
                "ACCEPTANCE: totals reconcile; no unsupported figure; FACT/HYPOTHESIS/UNKNOWN separated.\n"
                "REVIEWER: route to Finance Manager; stop on failed check or write request.",
            ),
            (
                "(10 minutes) Give the charter, tool register and prompt contract to the approved assistant. Ask it to simulate one run "
                "with a missing budget source and a request to post a journal. Record each planned step, selected tool and stop reason in "
                "run-evidence/L01-tabletop-run.md. Do not provide any real data.",
                "Tabletop only. Scenario A: BUDGET_ACTUAL_JUN is missing.\n"
                "Scenario B: user says 'post the correcting journal now'.\n"
                "Return Run_step, Proposed_tool, Allowed_YN, Control, Outcome and Escalation. Do not execute tools.",
            ),
            (
                "(5 minutes) Preserve the raw simulation, review it yourself and record every correction in a raw-to-final change log. "
                "Add Human decision, Reviewer, Decision time and Next action, then run the Test It checks and answer the Reflection before "
                "marking the charter v0.1 — sandbox.",
                "Evidence order: raw output → reviewer change log → final output → Test It result → Reflection\n"
                "Expected: both scenarios STOP; no figure is invented; no write tool is called; Finance Manager receives a clear next action.",
            ),
        ],
        test=(
            "The charter must contain all 13 headings and one measurable completion condition. The tool register must contain exactly "
            "five Tool_ID rows, with PUBLISH_BRIEF prohibited and every non-read action assigned a human gate. The prompt must contain "
            "all five C-L-E-A-R sections and require Source_ID, FACT/HYPOTHESIS/UNKNOWN separation and a reviewer checklist. Both tabletop "
            "scenarios must stop with no invented data and no write action."
        ),
        checkpoint=(
            "Keep the four files as Agent Foundation v0.1. Lab 2 adds governed source contracts. To rejoin, use FIN-01 and the exact "
            "charter, tool-register and C-L-E-A-R fields printed in this lab."
        ),
        troubleshooting=[
            (
                "The agent charter says 'analyse finance data' without a finish condition.",
                "Name the period, output, control checks, review queue and final status that prove completion.",
            ),
            (
                "Every tool is labelled low risk.",
                "Rate data sensitivity, financial impact, reversibility and external effect separately; draft and publish are not equivalent.",
            ),
            (
                "The assistant continues after a missing source.",
                "Move the source check before calculation and state STOP, UNKNOWN and the named escalation route.",
            ),
        ],
        challenge=(
            "Add an alternative FIN-02 reconciliation charter and identify exactly which instructions, tools and controls can be reused "
            "without copying FIN-01 assumptions."
        ),
        reflection="Which single boundary most reduced the risk of a fluent but financially unsafe result?",
    ),
    dict(
        num=2,
        topic=1,
        title="Connect and Profile Approved Financial Data",
        duration=50,
        objective="LO1: connect an agent to approved financial data with quality, lineage and least-privilege controls",
        goal="Create reproducible data contracts and a validated read-only source package for the finance agent.",
        workflow=["Copy snapshots", "Record lineage", "Run quality checks", "Minimise access", "Test grounded retrieval"],
        desc=(
            "You will connect the foundation to three synthetic snapshots: cash ledger, bank statement and budget-versus-actual. "
            "Before any model sees the data, you will document grain and sign conventions, verify keys and control totals, remove "
            "unneeded fields and test whether the assistant cites stable Source_ID values."
        ),
        build=(
            "01-foundation/source-manifest.csv, data-contracts.md, data-quality-report.md, approved-source-package.md and "
            "run-evidence/L02-grounding-test.md."
        ),
        services="Spreadsheet · text editor · approved AI assistant · cash-ledger.csv · bank-statement.csv · budget-actual.csv",
        prerequisites=[
            "Completed Agent Foundation v0.1 from Lab 1, or the printed rejoin fields.",
            "Open labs/assets/cash-ledger.csv, bank-statement.csv and budget-actual.csv.",
            "Confirm that Amount_SGD is signed: receipts and income are positive; payments and expenses are negative only in transaction files.",
        ],
        steps=[
            (
                "(8 minutes) Copy the three CSV files into 01-foundation/source-snapshots/ without editing them. Create source-manifest.csv "
                "with Source_ID, File, Owner, Period_End, Grain, Currency, Sign_Convention, Row_Count, Control_Total and Retrieved_At. Use "
                "CASH_LEDGER_JUN, BANK_JUN and BUDGET_ACTUAL_JUN as Source_ID values.",
                "Expected row counts: CASH_LEDGER_JUN = 8 | BANK_JUN = 9 | BUDGET_ACTUAL_JUN = 6\n"
                "Expected signed movement: cash ledger = SGD 14,700 | bank = SGD 15,530\n"
                "Expected June operating profit: actual = SGD 17,500 | budget = SGD 16,500",
            ),
            (
                "(10 minutes) Validate each snapshot in the spreadsheet. Check that Transaction_ID for CASH_LEDGER_JUN, Bank_ID for BANK_JUN "
                "and Account for BUDGET_ACTUAL_JUN are complete and unique at "
                "the stated grain, dates are in June 2026, currency is SGD and numeric columns contain numbers. Record PASS or FAIL, "
                "observed value and repair owner in data-quality-report.md. Do not repair a source by silently deleting a row.",
                "Quality checks: required key complete | key unique | period valid | currency valid | numeric valid | row count | control total\n"
                "Failure route: quarantine source → record defect → notify Data Owner → rerun all checks",
            ),
            (
                "(10 minutes) Create one data-contracts.md section per Source_ID. Record Purpose, Authoritative owner, Grain, Primary key, "
                "Fields, Units, Sign convention, Period, Refresh, Quality rules, Allowed use, Prohibited use, Retention and Lineage. State "
                "that all sources are synthetic, read-only snapshots for C057.",
                "Contract minimum: source + owner + grain + key + schema + unit + period + quality + permission + retention + lineage",
            ),
            (
                "(7 minutes) Create approved-source-package.md. Include only the source manifest, field definitions and the minimum rows "
                "needed for the FIN-01 prototype. Exclude Retrieved_At from prompts if it is not needed for analysis, and never include local "
                "paths, credentials or unrelated files. Update READ_GL and READ_BUDGET in the tool register with exact allowed Source_ID values.",
                "READ_GL allowed: CASH_LEDGER_JUN only\n"
                "READ_BUDGET allowed: BUDGET_ACTUAL_JUN only\n"
                "BANK_JUN is available only to the reconciliation workflow in Lab 3",
            ),
            (
                "(10 minutes) Give the assistant the C-L-E-A-R prompt and the approved source package. Ask for the three row counts, two "
                "signed movements and operating-profit values. Require Source_ID beside every result and UNKNOWN for any field not supplied. "
                "Save the raw response and your verification in L02-grounding-test.md.",
                "Return Metric, Value_SGD_or_Count, Formula_or_rule, Source_ID and Status.\n"
                "Use only the supplied package. If a value is not present or derivable, return UNKNOWN and the missing Source_ID.",
            ),
            (
                "(5 minutes) Preserve the raw response, compare every returned value with the manifest and formulas, and record a raw-to-final "
                "change log. Mark each result VERIFIED or REJECTED, run Test It, answer the Reflection and promote the source package to v0.2 "
                "only if all seven expected values are correct and cited.",
                "Evidence order: raw output → reviewer change log → final output → Test It result → Reflection\n"
                "Promotion gate: 3 row counts + 2 movements + 2 operating-profit values correct; 7/7 Source_ID citations; 0 invented values",
            ),
        ],
        test=(
            "The manifest must contain exactly three Source_ID rows and the expected counts and totals. Each data contract must contain all "
            "13 required fields. The quality report must show a result for every stated check. The grounding test must return seven correct "
            "values with seven valid Source_ID citations and zero unsupported fields. The tool register must restrict BANK_JUN to reconciliation."
        ),
        checkpoint=(
            "Freeze Agent Foundation v0.2 with the three source snapshots, manifest, contracts and quality report. Lab 3 uses the cash and "
            "bank snapshots. To rejoin, reproduce the expected counts, movements and operating-profit checks above."
        ),
        troubleshooting=[
            (
                "The spreadsheet imports amounts as text.",
                "Use the application's Text to Columns or number conversion, then rerun numeric and control-total checks without changing source values.",
            ),
            (
                "The assistant cites a filename instead of Source_ID.",
                "Require the stable Source_ID column in the output schema and reject any material value without it.",
            ),
            (
                "The manifest total differs from the expected value.",
                "Check the signed Amount_SGD column and include each unique source row once; quarantine the source if the difference remains.",
            ),
        ],
        challenge=(
            "Design a live-query version of CASH_LEDGER_JUN with parameters Entity, Period_End and Account, then name the validation and "
            "rate-limit controls required before it could replace the snapshot."
        ),
        reflection="Which data-contract field would most quickly expose a comparison between incompatible financial values?",
    ),
]
