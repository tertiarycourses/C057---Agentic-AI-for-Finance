"""Single source of truth for the C057 non-WSQ courseware package."""

TITLE = "Agentic AI for Finance"
SHORT_TITLE = "Agentic AI for Finance"
COURSE_CODE = "C057"
VERSION = "v1.0"
VERSION_DATE = "29 July 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Assigned Tertiary Infotech Academy Trainer"
COURSE_URL = "https://www.tertiarycourses.com.sg/agentic-ai-for-finance.html"
DAYS = 2
DAY_MINUTES = 480
INSTRUCTIONAL_MINUTES = 450
MODE = "Instructor-led, hands-on practical labs"
DAILY_TIMING = (
    "9:30 am–6:30 pm (1-hour lunch; two 15-minute tea breaks; "
    "7.5 instructional hours)"
)
DARK_THEME = False

LEARNING_OUTCOMES = [
    "LO1: Design a bounded finance agent with clear instructions, approved data connections, tool permissions and human review points.",
    "LO2: Automate reporting, reconciliation, forecasting and invoice workflows while preserving deterministic checks and human approval.",
    "LO3: Produce traceable financial analysis, scenarios, recommendations and visualisations from verified data.",
    "LO4: Deploy and govern finance agents with security, auditability, evaluation, monitoring and scalable operating controls.",
]

LO_TITLES = [
    "Design the Agent",
    "Automate Workflows",
    "Analyse & Explain",
    "Deploy & Govern",
]

TOPICS = [
    dict(
        num=1,
        code="01",
        title="Getting Started with Agentic AI for Finance",
        subtitle=(
            "agent foundations · tools and platforms · finance prompting · "
            "safe data connections"
        ),
        weighting="Day 1 morning · 2 connected labs",
        concepts=[
            ("Agentic workflow", "A model uses instructions and tools in a bounded loop to pursue a goal, observe results and decide the next step."),
            ("Finance control boundary", "Define permitted data, actions, limits, owners, stop conditions and evidence before the first run."),
            ("Tool architecture", "Separate read tools, calculation tools and action tools; grant only the access required for the task."),
            ("Finance prompt contract", "State the source boundary, method, output schema, acceptance checks, uncertainty rules and reviewer."),
            ("Data contract", "Document grain, fields, units, period, ownership, quality checks, lineage and refresh time."),
            ("Deterministic truth", "Use formulas and source-system rules for arithmetic, matching and posting; use the model for language and exceptions."),
        ],
        sections=[
            dict(
                title="Introduction to Agentic AI in Finance",
                definition=(
                    "An AI agent is a system in which a model controls part of a multi-step workflow, selects approved tools, observes results "
                    "and continues until it reaches a defined completion or stop condition. A chatbot answers a turn; a deterministic automation "
                    "follows fixed rules; an agent chooses among bounded next actions."
                ),
                why=(
                    "Finance work mixes repeatable calculations with ambiguous exceptions and narrative judgement. Agents can coordinate those "
                    "steps, but fluent output must never replace ledgers, policies, formulas or accountable decisions. The useful design question "
                    "is not how autonomous the system can be, but which decisions it may make safely."
                ),
                how=[
                    "Define one measurable goal, an authorised user and an explicit completion condition.",
                    "Provide instructions, approved source data and narrowly described tools.",
                    "Run a plan–act–observe loop with maximum turns, timeouts and failure handling.",
                    "Validate figures and high-impact actions with deterministic rules and named human review.",
                    "Persist the inputs, tool calls, outputs, approvals and final status as the run record.",
                ],
                example=[
                    "Goal: prepare a draft month-end variance brief from the approved June extract.",
                    "The agent reads the extract, invokes a calculation step, requests clarification for an unmapped account and drafts commentary.",
                    "The finance manager checks the figures and approves the brief; the agent has no permission to post a journal or send externally.",
                ],
                use_when=[
                    "The workflow has multiple steps, exceptions or unstructured inputs that fixed rules alone handle poorly.",
                    "A reliable source boundary, measurable checks and a human owner can be defined.",
                ],
                avoid_when=[
                    "A spreadsheet formula, database query or fixed rule completes the task more simply and predictably.",
                    "The agent would make an irreversible financial commitment without an authorised approval gate.",
                ],
                quality=[
                    ("Bounded", "Purpose, inputs, tools, limits, exit conditions and fallback are explicit."),
                    ("Grounded", "Every material figure traces to an approved source or deterministic calculation."),
                    ("Owned", "A named role reviews exceptions and remains accountable for the final decision."),
                ],
                sources=[
                    "https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/",
                    "https://www.nist.gov/itl/ai-risk-management-framework",
                ],
            ),
            dict(
                title="Popular AI Agent Tools and Platforms",
                definition=(
                    "Agent platforms range from browser assistants and configurable workspace agents to low-code workflow builders and software "
                    "development kits. All combine a model, instructions and tools; they differ in integration depth, observability, deployment "
                    "control, cost and the skill needed to operate them."
                ),
                why=(
                    "Choosing a platform before defining the workflow often produces an expensive demonstration with weak controls. Finance teams "
                    "should first classify the data, actions and evidence required, then select the least complex platform that can satisfy security, "
                    "integration, evaluation and operating needs."
                ),
                how=[
                    "Use a browser assistant for supervised analysis of approved files and prompt prototypes.",
                    "Use a configurable workspace agent when reusable instructions and approved knowledge sources are sufficient.",
                    "Use low-code orchestration for event triggers, connectors, approvals and business-user maintenance.",
                    "Use an SDK when custom tools, version control, test automation, telemetry or deployment isolation are required.",
                    "Start with one agent; split responsibilities only when instructions or tool choice remain unmanageably complex.",
                ],
                example=[
                    "A finance analyst prototypes variance commentary in an approved browser assistant with a synthetic CSV.",
                    "A process owner then maps the same prompt contract into a low-code flow with a read-only data connector and manager approval.",
                    "The engineering team uses an SDK only when the workflow needs custom identity, detailed tracing and controlled release gates.",
                ],
                use_when=[
                    "Comparing implementation options against an already defined finance workflow and control matrix.",
                    "A proof of value needs a clear path from supervised prototype to monitored operation.",
                ],
                avoid_when=[
                    "Selecting a platform because it has the most connectors or appears most autonomous.",
                    "Allowing a connector to inherit broad user permissions without a tool-by-tool risk review.",
                ],
                quality=[
                    ("Fit", "Workflow complexity and control requirements drive the platform choice."),
                    ("Visibility", "Runs, tool calls, versions, failures and approvals can be inspected."),
                    ("Portability", "Instructions, schemas, tests and data contracts are not trapped in one interface."),
                ],
                sources=[
                    "https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/",
                    "https://learn.microsoft.com/en-us/power-platform/architecture/reference-architectures/ai-document-processing",
                ],
            ),
            dict(
                title="Writing Effective Prompts for Finance",
                definition=(
                    "A finance prompt is an operating contract for a model. It identifies the role and objective, delimits authorised evidence, "
                    "specifies the method and tools, defines a machine-checkable output, states acceptance criteria and tells the model when to "
                    "ask, stop or escalate."
                ),
                why=(
                    "A vague request such as 'analyse the numbers' invites inconsistent calculations, unsupported causes and hidden assumptions. "
                    "A structured prompt makes the evidence boundary and review process observable, so a useful draft can be reproduced and tested."
                ),
                how=[
                    "Use C-L-E-A-R: Context, Ledger sources, Execution steps, Acceptance checks and Reviewer or escalation.",
                    "Place instructions before source material and delimit each source with a stable label.",
                    "Require a fixed schema with separate fields for fact, calculation, assumption, limitation and recommended action.",
                    "Give examples for classifications that are easy to confuse, such as timing difference versus data error.",
                    "Require UNKNOWN and a clarification question when evidence is missing; never reward confident guessing.",
                ],
                example=[
                    "The prompt names the June close, approved files and SGD units, then supplies the exact variance formula.",
                    "The output schema requires Account, Actual, Budget, Variance, Direction, Evidence and Reviewer_note.",
                    "An account without a budget mapping is returned as UNKNOWN and routed to the controller instead of being invented.",
                ],
                use_when=[
                    "A model must transform, explain, classify or critique financial information in a repeatable format.",
                    "The output will be checked against source evidence and deterministic acceptance rules.",
                ],
                avoid_when=[
                    "The prompt contains secrets, personal data or restricted information not approved for the service.",
                    "The model is asked to calculate totals without a deterministic reconciliation step.",
                ],
                quality=[
                    ("Specific", "Task, scope, units, period, schema and thresholds are explicit."),
                    ("Testable", "Acceptance checks can be evaluated without interpreting the prose."),
                    ("Fail-safe", "Missing evidence triggers UNKNOWN, clarification or escalation."),
                ],
                sources=[
                    "https://help.openai.com/en/articles/6654000-comprehensive-list-of-prompt-engineering-techniques",
                    "https://help.openai.com/en/articles/9358033-key-guidelines-for-writing-instructions-for-custom-gpts",
                ],
            ),
            dict(
                title="Connecting Agents to Financial Data",
                definition=(
                    "A financial data connection is a governed interface to a defined dataset, not unrestricted access to a drive or ledger. "
                    "Its contract records source owner, grain, schema, units, accounting period, refresh time, permitted use, quality rules, "
                    "lineage and access mode."
                ),
                why=(
                    "Many apparent model failures are data failures: duplicate rows, mixed periods, stale extracts, mismatched currencies or "
                    "unclear sign conventions. A read-only snapshot and manifest make the analysis reproducible and reduce the blast radius of "
                    "prompt injection, accidental writes and over-broad access."
                ),
                how=[
                    "Classify the data and minimise fields before granting access.",
                    "Begin with a versioned read-only snapshot; add live retrieval only after tests are stable.",
                    "Document grain, keys, sign conventions, currency, period, timezone and authoritative owner.",
                    "Validate row counts, uniqueness, completeness, control totals and cross-source reconciliations before model use.",
                    "Return source identifiers and timestamps with every retrieved record so outputs can preserve lineage.",
                ],
                example=[
                    "The agent receives a June general-ledger extract and a budget table through separate read-only tools.",
                    "A manifest records 30 June cut-off, SGD units, account grain and control totals; duplicate Journal_ID values fail ingestion.",
                    "The prompt references source labels rather than copying an entire finance drive into context.",
                ],
                use_when=[
                    "The agent needs repeatable access to structured finance data or approved documents.",
                    "Data owners can define quality checks, permissions, retention and lineage.",
                ],
                avoid_when=[
                    "The connector exposes unrelated folders, credentials or write permissions.",
                    "The source has no stable key, period, unit or owner and cannot be reconciled.",
                ],
                quality=[
                    ("Minimal", "Only necessary rows, fields and periods are exposed."),
                    ("Reconciled", "Control totals and key constraints pass before analysis."),
                    ("Traceable", "Every output can identify its source, version and retrieval time."),
                ],
                sources=[
                    "https://www.pdpc.gov.sg/guidelines-and-consultation/2024/02/advisory-guidelines-on-use-of-personal-data-in-ai-recommendation-and-decision-systems",
                    "https://www.nist.gov/itl/ai-risk-management-framework",
                ],
            ),
        ],
    ),
    dict(
        num=2,
        code="02",
        title="Automating Financial Workflows with AI Agents",
        subtitle=(
            "reporting and reconciliation · forecasting and planning · "
            "invoice processing · human-in-the-loop controls"
        ),
        weighting="Day 1 afternoon · 3 connected labs",
        concepts=[
            ("Control-first workflow", "Map source, calculation, exception, approval, record update and evidence before adding a model."),
            ("Reconciliation", "Match records by approved keys and tolerances, explain only the remaining exception set and preserve adjusted balances."),
            ("Driver-based forecast", "Translate explicit volume, price, rate and cost assumptions into formulas and comparable scenarios."),
            ("Document pipeline", "Capture, extract, validate, match, route, review and record without letting extraction confidence authorise payment."),
            ("Human gate", "Route material, unusual, low-confidence or irreversible actions to an authorised role."),
            ("Idempotent action", "A repeated run must not create duplicate records, payments or notifications."),
        ],
        sections=[
            dict(
                title="Automating Reporting and Reconciliation",
                definition=(
                    "A reporting agent assembles verified calculations and narrative from approved sources. A reconciliation compares two records "
                    "of the same economic activity, applies exact or authorised tolerant matches, isolates exceptions and proves that adjusted "
                    "balances agree."
                ),
                why=(
                    "Language models are useful for classifying exception descriptions and drafting commentary, but matching logic and control "
                    "totals should remain deterministic. Combining both prevents a persuasive narrative from hiding an unreconciled difference."
                ),
                how=[
                    "Freeze the period, source versions, opening balances and sign conventions.",
                    "Match exact keys first, then apply documented amount and date tolerances only where authorised.",
                    "Classify unmatched items as timing, bank-only, ledger-only, duplicate, mapping or investigation needed.",
                    "Calculate adjusted balances independently and require equality before completion.",
                    "Draft commentary from the verified exception table and retain links to every source row.",
                ],
                example=[
                    "Seven bank and ledger transactions match by reference and amount.",
                    "One outstanding payment reduces the adjusted bank balance; a bank fee and interest item adjust the ledger.",
                    "Both adjusted balances equal SGD 64,680, so the agent drafts a close note and routes the bank-only items for posting review.",
                ],
                use_when=[
                    "The workflow has stable matching keys, tolerances and a defined exception owner.",
                    "Narrative is generated only after control totals and adjusted balances pass.",
                ],
                avoid_when=[
                    "The model is allowed to 'make the balances agree' by deleting or inventing transactions.",
                    "Matching rules, cut-off or sign conventions are undocumented.",
                ],
                quality=[
                    ("Complete", "Every source row is matched once or appears in an owned exception queue."),
                    ("Balanced", "Independent adjusted balances agree exactly or within an approved tolerance."),
                    ("Explainable", "Each match rule and exception classification is visible."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/account-reconciliation",
                    "https://www.sec.gov/newsroom/speeches-statements/munter-statement-cash-flows-120423",
                ],
            ),
            dict(
                title="Building Forecasting and Planning Agents",
                definition=(
                    "A forecasting agent converts explicit business drivers and assumptions into a time-phased projection, compares scenarios, "
                    "explains sensitivities and records who approved each assumption. The numerical engine is deterministic; the model supports "
                    "assumption discovery, challenge and communication."
                ),
                why=(
                    "A single forecast can create false precision. Driver-based scenarios expose how revenue growth, cost rates and operating "
                    "expenses affect outcomes. Backtesting and assumption ownership make forecast error a learning signal rather than a reason "
                    "to rewrite history."
                ),
                how=[
                    "Define the forecast grain, horizon, baseline date and driver formulas.",
                    "Create base, downside and upside assumptions with owners and rationale.",
                    "Calculate every scenario with the same formula structure and preserve units.",
                    "Backtest prior forecasts using absolute error and document structural breaks or missing drivers.",
                    "Ask the model to challenge assumptions and explain sensitivity without changing approved values.",
                ],
                example=[
                    "June revenue of SGD 125,000 is the base; July base growth is 3%, cost of goods is 56% of revenue and operating expense is SGD 40,000.",
                    "The deterministic July operating-profit calculation is SGD 16,650.",
                    "The agent compares downside and upside cases, names the largest driver and presents the assumption owner and review date.",
                ],
                use_when=[
                    "The organisation can identify controllable drivers and maintain scenario assumptions.",
                    "Decision-makers need ranges, sensitivities and triggers rather than one unsupported point estimate.",
                ],
                avoid_when=[
                    "The agent invents future events, probabilities or market data that were not supplied.",
                    "Forecast outputs are written back as an approved plan without owner review.",
                ],
                quality=[
                    ("Formula-led", "Scenarios share transparent formulas and units."),
                    ("Assumption-owned", "Every material driver has a source, owner and review trigger."),
                    ("Backtested", "Error is measured on prior periods and feeds the next revision."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/dynamics365/finance/budgeting/position-forecasting",
                    "https://www.sec.gov/rules-regulations/2003/12/commission-guidance-regarding-managements-discussion-analysis-financial-condition-results-operations",
                ],
            ),
            dict(
                title="Document and Invoice Processing",
                definition=(
                    "An invoice agent captures a document, extracts fields, validates the supplier and invoice identity, checks purchase and receipt "
                    "evidence, applies tolerances, routes exceptions and creates a draft record for approval. Extraction is evidence capture, not "
                    "authority to post or pay."
                ),
                why=(
                    "Invoices are semi-structured and arrive in many formats, making extraction a good AI use case. Financial commitment, duplicate "
                    "prevention, tax treatment and payment remain high-impact controls that require deterministic validation and explicit human authority."
                ),
                how=[
                    "Capture the original document with a stable hash or identifier.",
                    "Extract supplier, invoice, date, currency, purchase order, totals and line items with field-level confidence.",
                    "Validate supplier master data, duplicate keys, arithmetic, tax, purchase order and receipt status.",
                    "Route low-confidence, missing, mismatched or unusual items to an exception queue.",
                    "Create a draft only; require authorised approval before posting or payment.",
                ],
                example=[
                    "An invoice total matches its purchase order and receipt, but another record exceeds the amount tolerance by SGD 400.",
                    "A missing purchase order, a duplicate flag and a low-confidence total each take different exception routes.",
                    "The workflow preserves the source document and reviewer correction so extraction performance can be improved.",
                ],
                use_when=[
                    "Documents follow known business processes and reviewers can correct exceptions efficiently.",
                    "The system can preserve originals, extracted fields, confidence, validation results and approvals.",
                ],
                avoid_when=[
                    "The agent may create a supplier, change bank details, post or pay without independent verification.",
                    "Confidence score alone is treated as proof that the transaction is valid.",
                ],
                quality=[
                    ("Source-preserved", "Original document and extracted fields remain linked."),
                    ("Three-way checked", "Invoice, purchase order and receipt are compared where applicable."),
                    ("Draft-only", "Irreversible actions remain behind authorised approval."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/dynamics365/business-central/faqs-payables-agent",
                    "https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/invoice",
                    "https://learn.microsoft.com/en-us/power-platform/architecture/reference-architectures/ai-document-processing",
                ],
            ),
            dict(
                title="Human-in-the-Loop Controls",
                definition=(
                    "Human-in-the-loop control inserts a named person at a defined decision point to review evidence, correct the record, approve "
                    "an action or take over a failed run. It is a designed operating role with thresholds and service levels, not a generic instruction "
                    "to 'check the output'."
                ),
                why=(
                    "Finance actions vary sharply in impact and reversibility. A read-only draft can tolerate more automation than a journal, "
                    "supplier-master change or payment. Risk-tiered gates protect segregation of duties while still allowing low-risk work to move quickly."
                ),
                how=[
                    "Rate tools and actions by data sensitivity, financial impact, reversibility and external effect.",
                    "Define automatic, review-required and prohibited routes with explicit thresholds.",
                    "Show the reviewer source evidence, model output, rule results and proposed action in one queue.",
                    "Require reason codes for approve, correct, reject and escalate decisions.",
                    "Set timeout, retry and handoff behaviour; make writes idempotent and auditable.",
                ],
                example=[
                    "Read-only variance drafting proceeds automatically after reconciled totals pass.",
                    "An invoice within tolerance creates a draft, while a missing purchase order or bank-detail change is held for independent review.",
                    "A retry uses the same idempotency key, so the workflow cannot create a second draft invoice.",
                ],
                use_when=[
                    "A task is valuable to automate but exceptions or actions can create material impact.",
                    "Authorised reviewers, thresholds, evidence and response times can be assigned.",
                ],
                avoid_when=[
                    "The reviewer sees only a recommendation and cannot inspect evidence or change the outcome.",
                    "Approval is performed by the same identity that initiated a restricted action without segregation.",
                ],
                quality=[
                    ("Risk-tiered", "Review strength rises with sensitivity, impact and irreversibility."),
                    ("Actionable", "The reviewer has evidence, choices, reason codes and a deadline."),
                    ("Independent", "Segregation of duties is maintained for restricted actions."),
                ],
                sources=[
                    "https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/",
                    "https://learn.microsoft.com/en-us/dynamics365/business-central/faqs-payables-agent",
                ],
            ),
        ],
    ),
    dict(
        num=3,
        code="03",
        title="Analysis and Insights with AI Agents",
        subtitle=(
            "financial analysis · risk and scenarios · evidence-backed recommendations · "
            "financial visualisation"
        ),
        weighting="Day 2 morning · 2 connected labs",
        concepts=[
            ("Statement logic", "Read income, balance-sheet and cash-flow information together; no single statement tells the complete story."),
            ("Verified metric", "Name formula, period, units, denominator and exclusions before interpreting a result."),
            ("Variance bridge", "Separate price, volume, mix, timing and one-off drivers where evidence permits."),
            ("Scenario discipline", "Hold formulas constant, change named assumptions and compare outcomes against triggers."),
            ("Insight chain", "Claim → evidence → calculation → limitation → implication → owned action."),
            ("Visual grammar", "Match chart form to question and preserve scale, units, baselines and uncertainty."),
        ],
        sections=[
            dict(
                title="Financial Analysis with AI",
                definition=(
                    "Financial analysis connects statements, operational drivers, ratios and period comparisons to answer a defined question. "
                    "An agent can assemble evidence and draft explanations, while formulas, accounting definitions and source reconciliations "
                    "remain controlled outside the model."
                ),
                why=(
                    "An accurate ratio can still mislead when its period, denominator or business context is wrong. Finance analysis therefore "
                    "starts with a question and metric contract, then separates what the data shows from possible causes that require operating evidence."
                ),
                how=[
                    "State the decision question, period, comparator, currency and materiality threshold.",
                    "Reconcile source totals and define every formula, denominator and sign convention.",
                    "Calculate trend, variance, margin, liquidity or efficiency measures deterministically.",
                    "Ask the agent to identify patterns and questions, citing the exact rows behind each claim.",
                    "Validate causes with operational evidence and label unverified explanations as hypotheses.",
                ],
                example=[
                    "June revenue is SGD 125,000 and operating profit is SGD 17,500, giving a 14.0% operating margin.",
                    "Revenue rose 5.9% from May, but cloud expense exceeded budget by 50%; both calculations are visible.",
                    "The agent may ask whether migration activity drove cloud cost, but it cannot state that cause without evidence.",
                ],
                use_when=[
                    "A defined business question can be answered from reconciled statements and operational drivers.",
                    "The audience needs an evidence-led explanation and follow-up questions.",
                ],
                avoid_when=[
                    "Metrics with different periods, currencies or definitions are compared without normalisation.",
                    "Correlation or timing is presented as a causal explanation.",
                ],
                quality=[
                    ("Defined", "Formula, period, unit, denominator and material exclusions are visible."),
                    ("Reconciled", "Inputs tie to approved totals before interpretation."),
                    ("Separated", "Facts, calculations, hypotheses and decisions are distinct."),
                ],
                sources=[
                    "https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements",
                    "https://www.sec.gov/rules-regulations/2003/12/commission-guidance-regarding-managements-discussion-analysis-financial-condition-results-operations",
                ],
            ),
            dict(
                title="Risk and Scenario Analysis",
                definition=(
                    "Sensitivity analysis changes one driver to show exposure; scenario analysis changes a coherent set of assumptions; stress "
                    "analysis explores severe but plausible conditions. A finance agent organises assumptions, calculations, triggers and responses "
                    "without treating a scenario as a prediction."
                ),
                why=(
                    "Point forecasts hide the range of possible outcomes. Structured scenarios reveal which assumptions dominate cash, margin or "
                    "covenant exposure and let managers pre-agree actions before a trigger is crossed."
                ),
                how=[
                    "Choose the decision, horizon, baseline and outcome measures.",
                    "Define coherent base, upside and downside assumptions with owners and evidence.",
                    "Calculate outcomes through one controlled model and run one-at-a-time sensitivities.",
                    "Identify breakpoints, leading indicators and action triggers.",
                    "Record limitations, missing dependencies and management responses for each scenario.",
                ],
                example=[
                    "The downside case combines −2% monthly revenue growth, 60% cost of goods and SGD 42,000 operating expense.",
                    "The agent compares September operating profit across scenarios and identifies the revenue-growth breakpoint for a negative result.",
                    "Management selects a monitoring trigger; the scenario remains a planning construct, not a forecast certainty.",
                ],
                use_when=[
                    "A decision is sensitive to uncertain but expressible drivers.",
                    "Leaders need ranges, breakpoints and contingent actions.",
                ],
                avoid_when=[
                    "Arbitrary assumptions are presented without owners, sources or coherence.",
                    "A severe scenario is labelled likely, or a scenario is used as a substitute for a controlled forecast.",
                ],
                quality=[
                    ("Coherent", "Assumptions form internally consistent business conditions."),
                    ("Comparable", "Scenarios use the same formulas, grain and horizon."),
                    ("Action-linked", "Indicators and thresholds connect outcomes to named responses."),
                ],
                sources=[
                    "https://www.nist.gov/itl/ai-risk-management-framework",
                    "https://www.sec.gov/rules-regulations/2003/12/commission-guidance-regarding-managements-discussion-analysis-financial-condition-results-operations",
                ],
            ),
            dict(
                title="Generating Insights and Recommendations",
                definition=(
                    "An insight explains a material pattern in context; a recommendation proposes a proportionate action with owner, timing, expected "
                    "effect and risk. A defensible agent output links every claim through evidence and calculation to a limitation and decision."
                ),
                why=(
                    "A list of variances is not an insight, and confident advice is not a recommendation unless the mechanism and trade-off are visible. "
                    "A structured chain prevents the model from jumping from a number to a decision."
                ),
                how=[
                    "Rank findings by decision relevance and materiality, not novelty.",
                    "Build a claim–evidence–calculation–limitation chain for each finding.",
                    "Distinguish observed driver, supported cause, plausible hypothesis and unknown.",
                    "For each action, name owner, deadline, expected effect, cost or risk and success measure.",
                    "Present alternatives and escalation conditions when uncertainty is material.",
                ],
                example=[
                    "Claim: cloud expense is SGD 2,000 above budget and 42.9% above May.",
                    "Evidence: June actual, June budget and May actual rows; limitation: workload-volume data is not supplied.",
                    "Recommendation: the technology owner validates usage and reserved-capacity options by Friday; finance monitors cost per workload unit.",
                ],
                use_when=[
                    "The output supports a known audience, decision cadence and action process.",
                    "Evidence and calculation are available for each material statement.",
                ],
                avoid_when=[
                    "The model is asked for strategic advice without business constraints or decision rights.",
                    "A polished explanation masks missing operational evidence.",
                ],
                quality=[
                    ("Material", "The finding matters to the stated decision or threshold."),
                    ("Traceable", "Evidence and calculation can be reproduced."),
                    ("Operable", "Action, owner, date, expected effect and measure are explicit."),
                ],
                sources=[
                    "https://www.sec.gov/rules-regulations/2003/12/commission-guidance-regarding-managements-discussion-analysis-financial-condition-results-operations",
                    "https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements",
                ],
            ),
            dict(
                title="Visualising Financial Data",
                definition=(
                    "Financial visualisation encodes a defined comparison using position, length, colour or annotation. The chart must preserve "
                    "period, unit, scale, baseline, grouping and uncertainty so a reader can verify the message from the underlying table."
                ),
                why=(
                    "A chart can amplify insight or manufacture it. Truncated axes, mixed units, excessive categories and decorative colour can make "
                    "immaterial changes look decisive. Finance visuals should make the decision and the evidence easier to inspect."
                ),
                how=[
                    "Choose one question: trend, comparison, composition, relationship or distribution.",
                    "Use lines for ordered time, bars for categorical comparison and tables when exact values dominate.",
                    "Keep units and period in the title or axes; start bar axes at zero and label scenario assumptions.",
                    "Use colour for a meaningful status or group, not decoration, and pair colour with direct labels.",
                    "Reconcile plotted values to the reviewed table and include source, as-of date and caveat.",
                ],
                example=[
                    "A three-line chart compares monthly operating profit under base, downside and upside assumptions.",
                    "The legend names each scenario; axes show SGD and month; a note states that scenarios are assumption sets, not probabilities.",
                    "A compact table beneath the chart gives exact values and the trigger selected by management.",
                ],
                use_when=[
                    "A visual pattern materially improves a reader's understanding of a decision.",
                    "The reviewed source table and encoding can be supplied together.",
                ],
                avoid_when=[
                    "A short table is clearer or exact values are the primary need.",
                    "Dual axes or selective ranges imply a relationship the data does not support.",
                ],
                quality=[
                    ("Honest", "Scale, baseline, units and exclusions are not misleading."),
                    ("Focused", "One visible comparison answers one reader question."),
                    ("Reproducible", "Every mark ties to the reviewed data table."),
                ],
                sources=[
                    "https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements",
                    "https://www.nist.gov/itl/ai-risk-management-framework",
                ],
            ),
        ],
    ),
    dict(
        num=4,
        code="04",
        title="Deploying and Governing Financial AI Agents",
        subtitle=(
            "data security and access · compliance and auditability · "
            "monitoring and improvement · deployment and scale"
        ),
        weighting="Day 2 afternoon · 2 connected labs",
        concepts=[
            ("Least privilege", "Give each identity and tool the minimum data and action rights for the shortest necessary time."),
            ("Layered guardrails", "Combine access control, deterministic validation, content checks, approval gates and runtime limits."),
            ("Run evidence", "Record source versions, prompts, tools, calculations, outputs, approvals, actions and errors."),
            ("Evaluation set", "Use representative normal, boundary, exception and adversarial cases with observable expected results."),
            ("Operational metrics", "Monitor task quality, exception rate, override rate, unsupported claims, latency, cost and incidents."),
            ("Controlled scale", "Promote versioned releases from sandbox to pilot to production with rollback and accountable ownership."),
        ],
        sections=[
            dict(
                title="Securing Financial Data and Access",
                definition=(
                    "Secure agent design applies data classification, minimisation, identity, least privilege, network and storage protection, "
                    "secret management, tool validation and incident response across the full run. The model is one component inside the security boundary."
                ),
                why=(
                    "An agent can combine trusted data with untrusted instructions and can call tools at machine speed. A malicious document, excessive "
                    "connector permission or exposed secret can turn a useful workflow into data leakage or an unauthorised financial action."
                ),
                how=[
                    "Classify data and remove fields not needed for the use case.",
                    "Use separate service identities, read-only tools by default and allow-listed parameters.",
                    "Keep secrets in approved secret storage; never place credentials in prompts, files or repositories.",
                    "Treat retrieved content as data, not instructions; validate tool inputs and outputs against schemas.",
                    "Limit turns, spend, destinations and write scope; log denied actions and rehearse revocation.",
                ],
                example=[
                    "The reporting agent may read one period's finance view but cannot browse the entire shared drive.",
                    "A text inside an uploaded invoice that asks the agent to reveal another supplier's data is ignored as untrusted content.",
                    "Payment and supplier-master tools are absent; access can be revoked through one service identity.",
                ],
                use_when=[
                    "Before any finance data or tool is connected and whenever permissions change.",
                    "Designing sandbox, pilot and production identities and network boundaries.",
                ],
                avoid_when=[
                    "Relying on prompt wording as the only security control.",
                    "Sharing a broad human account or long-lived key across multiple agents.",
                ],
                quality=[
                    ("Least-privileged", "Identity, data, tool and parameter scope are minimal."),
                    ("Layered", "Preventive, detective and recovery controls do not depend on one model."),
                    ("Revocable", "Access, runs and releases can be stopped quickly and completely."),
                ],
                sources=[
                    "https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/",
                    "https://www.nist.gov/itl/ai-risk-management-framework",
                    "https://learn.microsoft.com/en-us/power-platform/architecture/reference-architectures/ai-document-processing",
                ],
            ),
            dict(
                title="Compliance and Auditability",
                definition=(
                    "Auditability is the ability to reconstruct what an agent was intended to do, which data and version it used, which tools it called, "
                    "what checks ran, who approved the result and what record changed. Compliance maps that evidence to applicable obligations and internal policy."
                ),
                why=(
                    "A chat transcript alone cannot establish lineage, segregation, approvals or completeness. Finance governance needs a use-case inventory, "
                    "accountability, change records and evidence proportionate to materiality, while legal and compliance teams determine applicable requirements."
                ),
                how=[
                    "Register purpose, owner, affected parties, data classes, decisions, tools and materiality.",
                    "Map policy and regulatory obligations to controls and retained evidence.",
                    "Version instructions, schemas, data contracts, models, tools, evaluation sets and approval thresholds.",
                    "Log source identifiers, tool calls, validation results, human decisions and final actions with timestamps.",
                    "Define retention, access, incident, contestability and change-approval procedures.",
                ],
                example=[
                    "The finance-agent register maps fairness, ethics, accountability and transparency controls to the use case.",
                    "A run record shows the June source hash, prompt version, calculation check, reviewer and approved final brief.",
                    "A policy exception has an owner and expiry date rather than being hidden in the prompt.",
                ],
                use_when=[
                    "An agent supports financial reporting, customer or supplier decisions, operational control or a regulated process.",
                    "Internal audit, compliance, risk or management needs reconstructable evidence.",
                ],
                avoid_when=[
                    "Claiming that a framework automatically proves legal compliance.",
                    "Logging sensitive content without purpose, access control or retention limits.",
                ],
                quality=[
                    ("Reconstructable", "A reviewer can replay the decision path from retained evidence."),
                    ("Proportionate", "Controls reflect data sensitivity, decision materiality and affected parties."),
                    ("Accountable", "Business, data, technology, risk and approval roles are named."),
                ],
                sources=[
                    "https://www.mas.gov.sg/publications/monographs-or-information-paper/2018/FEAT",
                    "https://www.pdpc.gov.sg/guidelines-and-consultation/2024/02/advisory-guidelines-on-use-of-personal-data-in-ai-recommendation-and-decision-systems",
                    "https://airc.nist.gov/airmf-resources/airmf/5-sec-core/",
                ],
            ),
            dict(
                title="Monitoring and Improving Agents",
                definition=(
                    "Agent monitoring combines pre-release evaluations with production telemetry and sampled review. It measures whether tasks complete correctly, "
                    "controls trigger when needed, outputs remain grounded and the workflow stays within quality, cost, latency and risk tolerances."
                ),
                why=(
                    "Model behaviour, source data, policies and workflows change. A successful demonstration does not predict performance on boundary cases or "
                    "future data. A maintained evaluation set turns failures, corrections and incidents into controlled improvement."
                ),
                how=[
                    "Create normal, boundary, exception and adversarial cases with observable expected outcomes.",
                    "Measure deterministic accuracy, unsupported-claim rate, exception routing, human override, latency and cost.",
                    "Trace prompts, tools and checks so a failed result can be diagnosed by component.",
                    "Sample production runs by risk and investigate threshold breaches or drift.",
                    "Change one component at a time, rerun the evaluation set, approve and retain rollback evidence.",
                ],
                example=[
                    "Ten cases include matched transactions, duplicates, low-confidence invoices, missing sources and a malicious instruction in a document.",
                    "Release requires all high-risk routes to stop correctly, all arithmetic checks to pass and no unsupported material figure.",
                    "A reviewer correction becomes a new regression case before the next prompt version is approved.",
                ],
                use_when=[
                    "Before pilot, after any material component change and continuously in production.",
                    "A failure can affect reports, records, counterparties or financial decisions.",
                ],
                avoid_when=[
                    "Using user satisfaction as the only quality measure.",
                    "Optimising cost or speed before the accuracy and control baseline is met.",
                ],
                quality=[
                    ("Representative", "Cases cover normal work, boundaries, exceptions and attacks."),
                    ("Diagnostic", "Traces identify whether data, instruction, tool, model or control failed."),
                    ("Regression-safe", "Every correction becomes a retained test before release."),
                ],
                sources=[
                    "https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/",
                    "https://airc.nist.gov/",
                ],
            ),
            dict(
                title="Deploying and Scaling in Finance",
                definition=(
                    "Deployment promotes a versioned agent through isolated environments with tested data, identities, approvals, telemetry and rollback. Scaling "
                    "means reusing controlled components and operating practices across suitable workflows, not simply granting one agent more access."
                ),
                why=(
                    "Finance value depends on adoption, reliability and control over time. A staged release exposes workflow and operating issues at limited scale, "
                    "while reusable prompt contracts, tools, data products and evaluation patterns reduce the cost of later use cases."
                ),
                how=[
                    "Prioritise use cases by value, feasibility, data readiness and residual risk.",
                    "Move from synthetic sandbox to read-only pilot, shadow operation and controlled production.",
                    "Separate development, test and production data, identities, configurations and approvals.",
                    "Define business owner, product owner, data owner, control owner, support route and service levels.",
                    "Scale reusable components only after evaluation, incident and change processes are working.",
                ],
                example=[
                    "The close-report agent first runs on synthetic data, then shadows one reporting cycle without publishing.",
                    "A read-only pilot compares its output with the approved manual process and records reviewer corrections.",
                    "Production begins with one entity and rollback to the manual workflow; later entities reuse the tested contract and evaluation suite.",
                ],
                use_when=[
                    "A prototype has a measurable baseline, accountable owner and reliable fallback.",
                    "The organisation can operate versions, telemetry, incidents and change approval.",
                ],
                avoid_when=[
                    "Expanding data or action permissions to compensate for an unclear workflow.",
                    "Removing the manual fallback before stability and recovery have been demonstrated.",
                ],
                quality=[
                    ("Staged", "Capability and exposure grow through explicit release gates."),
                    ("Operated", "Owners, service levels, support, incidents and fallback are defined."),
                    ("Reusable", "Data contracts, tools, prompts and tests can be applied without copying hidden assumptions."),
                ],
                sources=[
                    "https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/",
                    "https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/automate-document-processing-azure-ai-document-intelligence",
                    "https://www.nist.gov/itl/ai-risk-management-framework",
                ],
            ),
        ],
    ),
]

DAY_THEMES = {
    1: "Design and Automate — build controlled finance-agent foundations and workflows",
    2: "Analyse and Govern — produce evidence-backed decisions and a deployable operating model",
}


def SCHEDULE(lab_titles):
    return {
        1: (
            DAY_THEMES[1],
            [
                ("9:30", "9:50", 20, "admin", "Welcome, course orientation, synthetic scenario and responsible-use ground rules"),
                ("9:50", "10:35", 45, "topic", "Topic 1 — agent foundations, control boundaries and platform choices"),
                ("10:35", "10:50", 15, "break", "Tea break"),
                ("10:50", "11:45", 55, "lab", "Hands-on: " + lab_titles([1])),
                ("11:45", "12:20", 35, "topic", "Topic 1 — finance prompt contracts and governed data connections"),
                ("12:20", "13:10", 50, "lab", "Hands-on: " + lab_titles([2])),
                ("13:10", "14:10", 60, "lunch", "Lunch break"),
                ("14:10", "14:50", 40, "topic", "Topic 2 — reporting, reconciliation and deterministic controls"),
                ("14:50", "15:45", 55, "lab", "Hands-on: " + lab_titles([3])),
                ("15:45", "16:00", 15, "break", "Tea break"),
                ("16:00", "16:35", 35, "topic", "Topic 2 — forecasting, document processing and human review"),
                ("16:35", "17:20", 45, "lab", "Hands-on: " + lab_titles([4])),
                ("17:20", "18:00", 40, "lab", "Hands-on: " + lab_titles([5])),
                ("18:00", "18:30", 30, "recap", "Day 1 LO1–LO2 recap, portfolio checkpoint and Q&A"),
            ],
        ),
        2: (
            DAY_THEMES[2],
            [
                ("9:30", "10:15", 45, "topic", "Topic 3 — financial analysis, metrics and evidence chains"),
                ("10:15", "11:10", 55, "lab", "Hands-on: " + lab_titles([6])),
                ("11:10", "11:25", 15, "break", "Tea break"),
                ("11:25", "12:05", 40, "topic", "Topic 3 — scenarios, recommendations and visualisation"),
                ("12:05", "13:00", 55, "lab", "Hands-on: " + lab_titles([7])),
                ("13:00", "13:45", 45, "topic", "Topic 4 — security, access, compliance and auditability"),
                ("13:45", "14:45", 60, "lunch", "Lunch break"),
                ("14:45", "15:40", 55, "lab", "Hands-on: " + lab_titles([8])),
                ("15:40", "16:20", 40, "topic", "Topic 4 — evaluation, monitoring, deployment and scale"),
                ("16:20", "16:35", 15, "break", "Tea break"),
                ("16:35", "17:30", 55, "lab", "Hands-on: " + lab_titles([9])),
                ("17:30", "18:30", 60, "recap", "LO3–LO4 integrated demonstration, governance review, recap and next steps"),
            ],
        ),
    }


COURSE_OVERVIEW = dict(
    section_title="Course Fundamentals",
    concepts_title="The Controlled Finance-Agent System",
    concepts=[
        ("Ground", "Use approved, versioned finance evidence with explicit grain, period, units and ownership."),
        ("Calculate", "Keep arithmetic, matching, thresholds and write rules deterministic and independently testable."),
        ("Reason", "Use the model to plan, classify exceptions, challenge assumptions and draft explanations."),
        ("Approve", "Route material decisions and irreversible actions to an authorised human with visible evidence."),
    ],
    framework_title="One Agent Run",
    framework=[
        ("Receive", "Validate goal, identity, inputs and permission."),
        ("Plan", "Select the next bounded step and approved tool."),
        ("Act", "Read, calculate, classify or draft within limits."),
        ("Observe", "Check tool result, totals, exceptions and stop conditions."),
        ("Review", "Approve, correct, escalate or close with a complete run record."),
    ],
    statement=dict(
        headline="Let the model manage ambiguity; let controls own financial truth.",
        body="Every material number is sourced or calculated, every exception is owned and every consequential action is approved.",
        kicker="COURSE OPERATING PRINCIPLE",
    ),
    pillars_title="What You Will Build",
    pillars=[
        ("Agent Foundation", ["use-case and tool-risk register", "finance prompt and data contracts"]),
        ("Workflow Portfolio", ["reconciliation and close brief", "forecast and invoice exception routes"]),
        ("Decision Pack", ["verified financial analysis", "scenario insight and chart specification"]),
        ("Operating Model", ["security and evidence controls", "evaluation, monitoring and deployment plan"]),
    ],
    arc_title="How Every Lab Progresses",
    arc=[
        "Open the approved synthetic Northstar Finance checkpoint.",
        "Apply a bounded prompt or deterministic finance rule.",
        "Separate source facts, calculations, model judgement and human decisions.",
        "Test the output against exact control totals or observable routing rules.",
        "Save the run evidence and the next rejoin checkpoint.",
    ],
    deep_dives=[
        dict(
            title="Agent, Assistant or Automation?",
            kicker="CONCEPT DEEP DIVE",
            items=[
                ("Assistant", "A person chooses each request and decides what to do with the answer."),
                ("Automation", "Fixed rules execute a known sequence with predictable branches."),
                ("Agent", "A model chooses among approved next actions inside a bounded workflow."),
                ("Control rule", "Use the least autonomous pattern that meets the business need."),
            ],
        ),
        dict(
            title="The Finance Truth Stack",
            kicker="CONCEPT DEEP DIVE",
            items=[
                ("System of record", "Authoritative ledger, document or approved business source."),
                ("Deterministic layer", "Queries, formulas, matching rules, thresholds and validations."),
                ("Model layer", "Planning, classification, drafting, critique and exception explanation."),
                ("Decision layer", "Named human authority, rationale and controlled record update."),
            ],
        ),
        dict(
            title="The Four Permission Questions",
            kicker="CONCEPT DEEP DIVE",
            items=[
                ("Read what?", "Specific data classes, rows, fields, periods and documents."),
                ("Act how?", "Allowed tools, parameters, destinations and financial limits."),
                ("Stop when?", "Completion, uncertainty, failure, budget and risk thresholds."),
                ("Who approves?", "Role, evidence, segregation, response time and fallback."),
            ],
        ),
    ],
)

LAB_SHOTS = {}

LG_INTRO = (
    "This guide teaches a control-first method for designing, applying and governing agentic AI in finance. "
    "It follows the approved C057 topic spine: foundations and data, workflow automation, analysis and insight, "
    "then secure deployment and governance. Concepts come first; nine connected Northstar Components labs apply them."
)
LG_INTRO2 = (
    "Use the guide as a post-course reference. Every concept explains what the practice is, why it matters, how it works, "
    "a worked finance example, a decision guide and practitioner controls. Source links point to primary AI, finance and "
    "Singapore governance guidance. The materials are educational and do not replace organisational accounting, legal, "
    "risk, security or compliance review."
)

LG_SETUP = dict(
    needs=[
        "A Windows or macOS laptop with a modern browser and spreadsheet application.",
        "Access to one organisation-approved AI assistant such as ChatGPT, Claude or Copilot.",
        "A text editor and the supplied synthetic CSV files in labs/assets/.",
        "A local folder named C057-Northstar-Finance-Agent for all lab outputs.",
    ],
    verify_text=(
        "Create the workspace, open every supplied CSV and confirm that dates and signed SGD amounts display correctly. "
        "If no AI assistant is available, use the printed prompt templates, complete all deterministic calculations and "
        "perform the classification and review steps manually."
    ),
    verify_code=(
        "C057-Northstar-Finance-Agent/\n"
        "  01-foundation/\n"
        "  02-automation/\n"
        "  03-analysis/\n"
        "  04-governance/\n"
        "  run-evidence/"
    ),
    conventions=[
        "Replace placeholders such as <PERIOD> and <SOURCE_ID>; never leave placeholders in a final record.",
        "Use SGD unless a source explicitly states another currency, and preserve the source sign convention.",
        "Label SOURCE FACT, CALCULATION, HYPOTHESIS, UNKNOWN and HUMAN DECISION separately.",
        "Save the model draft, deterministic check and human-approved version for material outputs.",
    ],
)

LAB_NOTE = (
    "Use only the supplied synthetic Northstar Components data or information you are authorised to process. "
    "Do not paste credentials, personal data, customer records or confidential financial information into an unapproved AI service. "
    "A named finance owner verifies every material figure, classification and action."
)

LG_WRAPUP = dict(
    title="Wrap-Up — Operate the Controlled Portfolio",
    intro=(
        "The nine labs create one connected finance-agent portfolio. Its value is not a collection of prompts; it is the traceable "
        "chain from approved data and deterministic checks to model-supported judgement, human authority and monitored operation."
    ),
    sections=[
        dict(
            title="The Five Questions Before Every Run",
            text="Use the same questions when moving a lab pattern into workplace use.",
            bullets=[
                "What exact decision or work product is in scope?",
                "Which source, period, grain, unit and owner define financial truth?",
                "Which steps must remain deterministic and independently reconciled?",
                "Which exceptions or actions require a named human decision?",
                "Which evidence proves what happened and supports rollback or improvement?",
            ],
        ),
        dict(
            title="A Safe Workplace Handoff",
            text="Adapt the synthetic patterns to organisational controls before using live finance data.",
            bullets=[
                "Confirm approved services, data classifications, retention, access and cross-border requirements.",
                "Replace synthetic files only with authorised, reconciled data products and documented owners.",
                "Pilot read-only, compare with the current process and add corrections to the evaluation set.",
                "Assign business, data, technology, control and support ownership before production.",
            ],
        ),
    ],
)

LG_NEXT_STEPS = [
    "Select one low-risk, read-only finance workflow and write its goal, source boundary, deterministic checks and human gate.",
    "Build ten representative evaluation cases before connecting the workflow to a live source.",
    "Measure one quality metric and one control metric, such as unsupported-claim rate and exception-routing accuracy.",
    "Pilot in shadow mode for one cycle, retain reviewer corrections and decide whether the residual risk is acceptable.",
]

LG_GLOSSARY = [
    ("Agent", "A system in which a model manages part of a workflow and selects approved tools inside explicit limits."),
    ("Agent run", "One traceable execution from validated request through tools, checks, human decisions and final status."),
    ("Control total", "An independently known count or amount used to verify completeness and accuracy."),
    ("Data contract", "A documented agreement on source, grain, schema, unit, quality, ownership, lineage and permitted use."),
    ("Deterministic check", "A rule or calculation that produces the same result from the same inputs."),
    ("Exception queue", "Owned records that failed a match, threshold, completeness or confidence rule."),
    ("Grounding", "Constraining an output to supplied or retrieved evidence and preserving links to that evidence."),
    ("Human-in-the-loop", "A defined human decision point with evidence, choices, authority and response expectations."),
    ("Idempotency", "The property that repeating an action does not create a duplicate effect."),
    ("Least privilege", "Granting only the data and action permissions required for a task."),
    ("Lineage", "The trace from an output back to source records, versions, calculations and transformations."),
    ("Materiality", "The significance of information or an error to the decision in context."),
    ("Operating margin", "Operating profit divided by revenue for the same period."),
    ("Prompt contract", "Structured instructions defining objective, sources, method, output, checks and escalation."),
    ("Reconciliation", "Comparison of two records of the same activity until adjusted balances agree and exceptions are owned."),
    ("Scenario", "A coherent set of assumptions used to explore possible outcomes, not a prediction."),
    ("Segregation of duties", "Splitting initiation, approval, custody or recording responsibilities to reduce error and misuse."),
    ("Tool", "A governed function or connector an agent may call to retrieve data, calculate or take an action."),
    ("Variance", "The difference between an actual value and a defined comparator such as budget or prior period."),
    ("Write action", "A tool operation that changes a record, sends information or creates a financial or external effect."),
]

TRAINER_TEAM = [
    (
        "Assigned Tertiary Infotech Academy Trainer",
        "Finance-automation and agentic-AI facilitator who guides control-first design, deterministic verification, "
        "evidence-backed analysis and hands-on application to the synthetic Northstar Components scenario.",
    ),
]

NEXT_STEPS = dict(
    title="Continue with a Read-Only Pilot",
    items=[
        "Choose one bounded finance workflow with an accountable owner and reconciled source.",
        "Create a prompt contract, tool-risk register and ten-case evaluation set.",
        "Run in shadow mode, compare with the approved process and capture every correction.",
        "Expand only when quality, control, support and rollback thresholds are met.",
    ],
)

THANK_YOU = dict(
    body=(
        "You can now design, test and govern finance agents that keep data, calculations, exceptions and decisions traceable."
    ),
    kicker="C057 · KEEP FINANCIAL TRUTH HUMAN-OWNED",
)

VERSION_HISTORY = [
    (
        "1.0",
        VERSION_DATE,
        "Initial aligned release of the slide deck, Learner Guide, Lesson Plan and nine connected labs.",
        TRAINER,
    ),
]
