# C057 Untrusted-Content Incident Runbook Starter

## Safe path: note is ignored

1. Detect `UNTRUSTED_OVERRIDE_REQUEST` as document data.
2. Preserve the approved instruction hierarchy and source boundary.
3. Keep the invoice on its deterministic route (`REVIEW_CONFIDENCE` for INV-006).
4. Log a security event and preserve the raw note, route, control, reviewer, and time.
5. Add the case to the regression suite.

## Control-failure path: attempted unauthorised access or action

1. Stop the affected run and block further tool calls.
2. Contain access and ask the AI Platform Owner to revoke the run identity if necessary.
3. Preserve the prompt, source identifiers, tool request, denial event, output, and timestamps.
4. Notify the Finance Control Owner, Data Owner, and affected Business Owner.
5. Investigate the cause, correct the control, retest the regression suite, and obtain restart approval.

## Lab 8 fields to complete

- Detection owner:
- Notification time target:
- Evidence location:
- Decision authority:
- Retest owner:
- Restart approvers:
