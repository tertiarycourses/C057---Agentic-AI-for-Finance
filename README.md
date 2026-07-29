# C057 — Agentic AI for Finance

Aligned non-WSQ courseware for Tertiary Infotech Academy.

- Course code: C057
- Version: v1.0
- Duration: 2 days, 15 instructional hours
- Delivery: instructor-led with nine connected hands-on labs

## Courseware

- `courseware/Agentic AI for Finance-v1.0.pptx` and PDF
- `courseware/LG-Agentic AI for Finance.docx` and PDF
- `courseware/LP-Agentic AI for Finance.docx` and PDF
- `LG-Agentic AI for Finance.md`
- `labs/README.md`, nine lab manuals and synthetic lab assets

The canonical content is held in:

```text
.agents/skills/non-wsq-courseware-build/build/
  course_data.py
  data_domain1.py
  data_domain2.py
  data_domain3.py
  data_domain4.py
```

These modules generate the slide deck, Learner Guide, Lesson Plan and lab manuals so the course identity, outcomes, topics, schedule and lab sequence stay aligned.

## Build

From Git Bash on Windows:

```bash
COURSE_REPO="$PWD" bash ".agents/skills/non-wsq-courseware-build/build/build_courseware.sh"
```

Run the courseware QA gate before publishing:

```bash
python ".agents/skills/non-wsq-courseware-qa/scan_prohibited.py" "$PWD"
```
