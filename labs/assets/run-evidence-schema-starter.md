# C057 Run-Evidence Schema Starter

Use one record per run.

| Field | Required | Seeded definition |
|---|---|---|
| Run_ID | Yes | Unique immutable run identifier |
| Agent_ID | Yes | Inventory identifier |
| Requester | Yes | Approved requesting identity |
| Purpose | Yes | In-scope task and decision supported |
| Source_ID | Yes | Approved source identifier or identifiers |
| Source_Version | Yes | Snapshot date or immutable version |
| Instruction_Version | Yes | Approved instruction version |
| Model_Configuration | Yes | Approved model and material settings |
| Tool_Call | Yes | Tool name and parameters; `NONE` when unused |
| Validation_Result | Yes | Deterministic checks and outcomes |
| Output_Hash_or_Location | Yes | Protected pointer to raw output |
| Human_Decision | Yes | Reviewer, decision, reason, and time |
| Final_Action | Yes | Terminal route; no unauthorised action |
| Error | Yes | Error code or `NONE` |
| Start_Time | Yes | ISO 8601 timestamp |
| End_Time | Yes | ISO 8601 timestamp |
| Retention_Class | Complete in Lab 8 | Approved retention class and period |
| Sensitive_Field_Handling | Complete in Lab 8 | Redaction, protected location, and reader roles |

Lab 8 task: complete the last two definitions, name the authorised readers, and test whether an independent reviewer can reconstruct one Lab 5 run.
