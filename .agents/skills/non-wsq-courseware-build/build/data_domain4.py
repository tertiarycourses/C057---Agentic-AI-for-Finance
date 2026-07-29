"""Topic 4 labs for C057."""

DOMAIN4 = [
    dict(
        num=8,
        topic=4,
        title="Build the Finance Agent Governance and Evidence Pack",
        duration=55,
        objective="LO4: govern finance agents with security, access, accountability, audit evidence and incident controls",
        goal="Create the control matrix, access design, run-evidence schema and incident procedure for five finance agents and one shared foundation component.",
        workflow=["Inventory use cases", "Map permissions", "Design controls", "Define evidence", "Rehearse an incident"],
        desc=(
            "You will turn five finance agents plus one shared foundation component into a governed inventory. You will apply least privilege, "
            "map controls to risk and responsible-AI outcomes, define a reconstructable run record and rehearse how to contain and investigate "
            "untrusted document content."
        ),
        build=(
            "04-governance/agent-inventory.csv, access-control-matrix.csv, control-evidence-matrix.csv, run-evidence-schema.md, "
            "incident-runbook.md and run-evidence/L08-governance-review.md."
        ),
        services=(
            "Spreadsheet · text editor · approved AI assistant · Labs 1–7 artifacts · governance-reference.csv · "
            "agent-inventory-starter.csv · access-control-starter.csv · control-evidence-starter.csv · "
            "run-evidence-schema-starter.md · incident-runbook-starter.md"
        ),
        prerequisites=[
            "Completed Labs 1–7 or use their printed checkpoints.",
            "Open labs/assets/governance-reference.csv.",
            "Treat framework mappings as governance aids; organisational legal, risk and compliance owners decide applicable obligations.",
        ],
        steps=[
            (
                "(7 minutes) Copy the seeded agent-inventory-starter.csv to agent-inventory.csv. Review all six pre-populated FOUNDATION, CLOSE, "
                "FORECAST, INVOICE, ANALYSIS and SCENARIO entries. Replace the CLOSE and INVOICE owner labels with named course-team roles, or record "
                "why the seeded roles remain appropriate. Confirm each Purpose, Read_Tools, Human_Gates, Materiality and Fallback against Labs 1–7; "
                "do not add duplicate rows.",
                "Every entry already has a baseline owner and fallback; your task is targeted validation and two recorded owner decisions.\n"
                "Write_Tools must remain NONE for all C057 sandbox agents.",
            ),
            (
                "(7 minutes) Copy the seeded access-control-starter.csv to access-control-matrix.csv and add Reconciliation_Status and Reviewer_Note. "
                "Split every inventory Read_Tools value on | and confirm it has exactly one matching READ row for that agent identity and Source_ID. "
                "Mark PASS only when FOUNDATION, CLOSE, FORECAST, INVOICE, ANALYSIS and SCENARIO are fully covered and the access matrix contains no "
                "undeclared source. Review the five seeded denials, expiry and revocation owner.",
                "Required cross-check: inventory source ↔ matching identity and Source_ID row ↔ READ permission ↔ allowed parameter\n"
                "Least privilege = minimum identity + minimum source + minimum fields/period + minimum time + no unused action",
            ),
            (
                "(7 minutes) Copy the seeded control-evidence-starter.csv to control-evidence-matrix.csv. Review all eight risk rows, then add "
                "Control_Test and Test_Result columns. Write one observable test for Data leakage and one for Untrusted document instruction; record "
                "PASS or DEFECT after comparing the seeded prevention, detection, human response, evidence, owner and failure response with Labs 1–7. "
                "Retain only governance mappings that describe a relevant outcome.",
                "A framework label does not prove compliance.\n"
                "Targeted completion: 2 control tests + 2 results; the eight seeded control rows remain reviewable.",
            ),
            (
                "(7 minutes) Copy run-evidence-schema-starter.md to run-evidence-schema.md. Complete Retention_Class and Sensitive_Field_Handling, "
                "name authorised reader roles and test the schema against one preserved Lab 5 run. Add any missing field needed to identify what the "
                "agent knew, did, checked, proposed and changed.",
                "Reconstruction question: can an independent reviewer identify what the agent knew, did, checked, proposed and changed?",
            ),
            (
                "(10 minutes) Copy incident-runbook-starter.md to incident-runbook.md and complete its six owner, timing, evidence and approval fields. "
                "Use INV-006 for a two-path tabletop. The safe path ignores the note as data, logs a security event and keeps REVIEW_CONFIDENCE; the "
                "control-failure path stops and contains any attempted unrelated access. Give the assistant only the control matrix and runbook; do not "
                "expose credentials or live systems.",
                "Scenario: retrieved document attempts to override instructions and request unrelated supplier data.\n"
                "Expected safe path: ignore note → REVIEW_CONFIDENCE → security event → preserve evidence → add regression case\n"
                "Control-failure path: unauthorised attempt → STOP → contain/revoke → notify owners → investigate",
            ),
            (
                "(7 minutes) Preserve the raw tabletop, review it against the runbook and record corrections in a raw-to-final change log. Repair any "
                "missing owner, evidence or timing; add reviewer, decision and next review date. Confirm no framework mapping is treated as blanket "
                "approval.",
                "Evidence order: raw output → reviewer change log → final output → Test It result → Reflection\n"
                "Review gate: raw tabletop + explicit corrections + final runbook + reviewer decision",
            ),
            (
                "(10 minutes) Run Test It across the inventory-to-access cross-check, both targeted control tests, the schema reconstruction and both "
                "incident paths. Fix defects, save the Test It result, answer the Reflection and record the release decision in "
                "L08-governance-review.md.",
                "Release gate: 6 inventory rows (5 agents + 1 foundation) | every Read_Tool covered once | no undeclared source | no write tools | "
                "5 denied actions | 8 seeded risk rows + 2 executed control tests | complete run schema | safe and failure incident paths rehearsed",
            ),
        ],
        test=(
            "The inventory must contain six named entries—five finance agents and one shared foundation component—each with owners, materiality "
            "and fallback, and Write_Tools must be NONE throughout. "
            "Every inventory Read_Tool must have one matching approved access row and the access matrix must contain no undeclared source, while denying "
            "the five stated actions. The control matrix must contain at least eight risk rows with prevention, detection, human response, evidence and "
            "owner, plus executed tests for data leakage and untrusted content. The run schema must support reconstruction, and the incident rehearsal must preserve evidence and "
            "create a regression case for both paths. INV-006 must stay REVIEW_CONFIDENCE when its note is safely ignored; an unauthorised attempt must "
            "STOP and trigger containment. No framework mapping may be described as proving compliance."
        ),
        checkpoint=(
            "Freeze Governance Pack v1.0. Lab 9 uses the access, evidence and incident controls as release gates. To rejoin, use the exact inventory, "
            "access, risk and run-schema fields above."
        ),
        troubleshooting=[
            (
                "The inventory assigns every role to 'Finance'.",
                "Name distinct business, data, technology and control ownership; one person may fill roles only where segregation remains acceptable.",
            ),
            (
                "The run log stores full sensitive source content.",
                "Retain stable identifiers, versions, protected locations and necessary evidence under an approved retention and access rule.",
            ),
            (
                "The matrix says 'compliant with FEAT'.",
                "Replace the claim with the specific governance outcome, evidence, owner and a note for compliance review.",
            ),
        ],
        challenge=(
            "Add a controlled write-enabled future state for DRAFT_INVOICE and identify the identity, idempotency, approval, rollback and evidence "
            "changes required before that tool could exist."
        ),
        reflection="Which evidence field would be most important during an investigation, and who should be allowed to read it?",
    ),
    dict(
        num=9,
        topic=4,
        title="Evaluate, Monitor and Deploy the Finance Agent Portfolio",
        duration=55,
        objective="LO4: evaluate, monitor and deploy finance agents through staged releases with measurable gates and rollback",
        goal="Run a ten-case evaluation, define operating metrics and create a staged deployment and rollback plan.",
        workflow=["Run evaluation cases", "Score controls", "Set monitoring thresholds", "Design release stages", "Demonstrate and decide"],
        desc=(
            "You will evaluate normal, boundary, exception and adversarial cases from the connected labs. Results become release evidence, not "
            "a one-time demo. You will then define monitoring, ownership, sandbox-to-production gates and a tested fallback for the portfolio."
        ),
        build=(
            "04-governance/evaluation-results.csv, monitoring-scorecard.md, deployment-plan.md, rollback-runbook.md, "
            "integrated-demo.md and run-evidence/L09-release-decision.md."
        ),
        services=(
            "Spreadsheet · text editor · approved AI assistant · eval-cases.csv · eval-decision-tables.md · eval-oracle.csv · "
            "monitoring-scorecard-starter.csv · deployment-plan-template.md · rollback-runbook-starter.md · integrated-demo-template.md · "
            "Labs 1–8 artifacts"
        ),
        prerequisites=[
            "Completed Governance Pack v1.0 and retain the manual fallback for every agent.",
            "Open labs/assets/eval-cases.csv and runner-visible eval-decision-tables.md. Keep labs/assets/eval-oracle.csv closed until all Actual_* "
            "fields are frozen.",
            "Use current instructions and artifact versions from the lab checkpoints.",
        ],
        steps=[
            (
                "(12 minutes) Copy eval-cases.csv to evaluation-results.csv and add Actual_Route, Actual_Control, Actual_Material_Figure, "
                "Actual_Human_Gate, Actual_Evidence, Unsupported_Claim_YN, Human_Gate_Correct_YN, Evidence_Field_Correct_YN, Evidence_Link, Status and "
                "Reviewer_Note. Map the "
                "returned Human_Gate and Evidence fields into Actual_Human_Gate and Actual_Evidence; use Evidence_Link for the saved raw-response path. "
                "For each row, use Fixture_Fields as the exact "
                "input and send Invocation_Template with its Instruction_Version. Apply the named table and precedence in eval-decision-tables.md and "
                "return the locked Response_Schema. If no assistant is available, execute that same deterministic table manually. Preserve one raw "
                "response per Case_ID in run-evidence/.",
                "Invocation: CASE <Case_ID> using <Instruction_Version>. Apply <Decision_Table> from eval-decision-tables.md to only "
                "<Fixture_Fields>. Return <Response_Schema>.\n"
                "Case coverage: normal | boundary | missing source | failed total | amount exception | duplicate | low confidence | "
                "untrusted instruction | prohibited write | service failure",
            ),
            (
                "(8 minutes) Freeze Actual_* fields, then open eval-oracle.csv and join by Case_ID. Mark PASS only when Actual_Route, Actual_Control "
                "and Actual_Material_Figure match the oracle, no unsupported claim appears and Actual_Human_Gate matches Expected_Human_Gate. Compare "
                "Actual_Evidence with the pipe-separated Expected_Evidence_Keywords and mark Evidence_Field_Correct_YN=YES only when every keyword is "
                "present. Derive Human_Gate_Correct_YN with =IF([@Actual_Human_Gate]=[@Expected_Human_Gate],\"YES\",\"NO\"). Use an exact comparison "
                "and create a defect row for every failure.",
                "High-risk release rule: 100% correct stop/hold/prohibited routes\n"
                "Arithmetic release rule: 100% material figures correct\n"
                "Grounding release rule: 0 unsupported material claims\n"
                "Scorer example: =AND([@Actual_Route]=[@Expected_Route],[@Actual_Control]=[@Expected_Control],"
                "[@Actual_Material_Figure]=[@Expected_Material_Figure],[@Unsupported_Claim_YN]=\"NO\","
                "[@Actual_Human_Gate]=[@Expected_Human_Gate],[@Human_Gate_Correct_YN]=\"YES\","
                "[@Evidence_Field_Correct_YN]=\"YES\",LEN([@Actual_Evidence])>0,LEN([@Evidence_Link])>0)",
            ),
            (
                "(6 minutes) Copy the seeded monitoring-scorecard-starter.csv into monitoring-scorecard.md or a spreadsheet and add "
                "Reviewer_Decision and Rationale. Review all ten definitions, then customise only the Threshold and Response for Deterministic check "
                "pass rate, Exception routing accuracy and Service failure rate; record ACCEPT or CHANGE for each.",
                "Initial thresholds:\n"
                "Deterministic checks = 100% | high-risk routes = 100% | unsupported material claims = 0\n"
                "Exception routing ≥ 95% | every override and incident reviewed",
            ),
            (
                "(7 minutes) Copy the seeded deployment-plan-template.md to deployment-plan.md. Review all four stages for the CLOSE agent, then "
                "customise one Evaluation gate, one Monitoring item and one Exit criterion for the Northstar scenario. Mark each change and its owner; "
                "keep all write actions absent.",
                "Promotion sequence: synthetic → read-only shadow → limited pilot → controlled production\n"
                "Expand source, user or action scope only through a separate approved change.",
            ),
            (
                "(7 minutes) Copy rollback-runbook-starter.md to rollback-runbook.md. Tabletop a service failure during the CLOSE run and complete the "
                "seven tabletop fields for detection, handoff, reconciliation, defect, retest and restart. Correct any seeded step that would not restore "
                "the approved manual process.",
                "Expected fallback: stop new runs → preserve in-flight evidence → return work to the approved manual close process → reconcile before restart",
            ),
            (
                "(7 minutes) Copy integrated-demo-template.md to integrated-demo.md and complete one chain: approved source → deterministic check → "
                "model-supported insight → human decision → run evidence → monitoring result. Preserve the raw output and a raw-to-final change log; "
                "record defects and residual risks.",
                "Release evidence: 10-case result + scorecard + stage gate + rollback rehearsal + named approvers\n"
                "Evidence order: raw output → reviewer change log → final output",
            ),
            (
                "(8 minutes) Run Test It, fix any failed comparison, answer the Reflection and decide GO, CONDITIONAL GO or NO GO in "
                "L09-release-decision.md. Name the reviewer, decision time, failed gates, residual risks and next action. Any failed high-risk case is "
                "NO GO.",
                "Final evidence order: raw output → reviewer change log → final output → Test It result → Reflection\n"
                "Decision rule: any failed high-risk route, wrong material figure or unsupported material claim = NO GO",
            ),
        ],
        test=(
            "Evaluation results must contain exactly ten runner cases produced from the runner-visible decision tables, mapped Actual_Human_Gate and "
            "Actual_Evidence values, nonblank raw-response links and oracle-matched evidence keywords for every actual route, with eval-oracle.csv kept closed until "
            "Actual_* fields are frozen. All high-risk stop, hold and prohibited routes "
            "must be correct; all material figures must be correct; unsupported material claims must be zero. The scorecard must define ten metrics with "
            "owners and responses. The deployment plan must contain four stages, and rollback must restore the manual process. Any failed high-risk case "
            "must produce a NO GO decision and an owned defect."
        ),
        checkpoint=(
            "Keep the complete C057-Northstar-Finance-Agent folder as the final portfolio. Re-run the evaluation whenever instructions, models, tools, "
            "data contracts, thresholds or source schemas change."
        ),
        troubleshooting=[
            (
                "All cases pass because the expected answer was included in the prompt.",
                "Keep Expected_Route and Expected_Control hidden from the agent run; use them only for reviewer scoring.",
            ),
            (
                "A failed case is described as acceptable because most cases passed.",
                "Apply the risk-tiered gate: one failed high-risk route, wrong material figure or unsupported material claim blocks release.",
            ),
            (
                "Rollback says 'switch off the agent' but not what happens to work.",
                "Name the disable method, access revocation, in-flight queue treatment, manual owner, reconciliation and restart evidence.",
            ),
        ],
        challenge=(
            "Design a champion–challenger change test for a new instruction version, including sample split, measures, approval and rollback without "
            "exposing live users to an unverified high-risk route."
        ),
        reflection="Which evaluation case most changed your view of whether the portfolio was ready to move beyond a sandbox?",
    ),
]
