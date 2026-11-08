# Project Dashboard & Progress Checklist
## Agency Client Intake & Scope Synthesis AI Workflow

> **Target Company:** Chromatix (Melbourne, Australia — Web Design & Conversion Optimization)  
> **Target Role:** AI Automation Developer (OnlineJobs.ph ID: 1758708)  
> **Applicant:** Marc Neil Zapanta  
> **Primary Directory:** `C:\Users\marcn\OneDrive\Desktop\Applications\Chromatix - AI Automation Developer\projects\agency-client-intake-workflow\`  
> **Google Drive Cloud Mirror:** `I:\My Drive\Job-Application-DB\Applications\Chromatix - AI Automation Developer\projects\agency-client-intake-workflow\`  
> **Last Synced Checkpoint:** 2026-11-02 15:30 AEST  
> **Live Portfolio URL:** `https://marc-portfolio-sigma.vercel.app/projects/agency-client-intake-workflow`  

---

## 🚦 Live Execution Dashboard

```text
[1. Webhook] ──► [2. HTTP REST + Retry] ──► [3. Parse JSON] ──► [4. Webhook Response 200] ──► [5. Router]
                                                                                                  ├── (Route 1: Needs Clarification) ──► [6. Gmail Draft]                 (VERIFIED ✅)
                                                                                                  └── (Route 2: Ready for Proposal)  ──► [7. Google Docs Brief]           (VERIFIED ✅)
                                                                                                                                           └──► [8. Gmail Team Alert]     (VERIFIED ✅)
```

| Checkpoint Phase | Status | Completed At | Verification Artifacts |
| :--- | :---: | :---: | :--- |
| **CP 1: Webhook Ingestion** | ✅ Complete | 2026-11-01 | Custom Webhook listening (`200 Accepted`); schema registered |
| **CP 2: AI REST API Integration** | ✅ Complete | 2026-11-01 | Direct HTTP POST to OpenRouter with raw JSON body & Bearer auth |
| **CP 3: Entity Normalization** | ✅ Complete | 2026-11-01 | Parse JSON extracting 8 discrete scoping schema fields |
| **CP 4: Intelligent Routing** | ✅ Complete | 2026-11-01 | Dual-branch router with `Equal to (boolean)` filters |
| **CP 5: Action Endpoints** | ✅ Complete | 2026-11-01 | Gmail (Create Draft) + Google Docs (Create Document in Drive) |
| **CP 6: QA & Edge Case Debugging** | ✅ Complete | 2026-11-01 | 2 live test cases verified; Gmail 403 & AI boundary tuned; `DEBUG_CASE_STUDIES.md` |
| **CP 7: Production Hardening Triad** | ✅ Complete | 2026-11-01 | `Retry` Directive (3x/1min), Webhook Response (200 JSON), Team Alert (Gmail) |
| **CP 8: Blueprint & Package Export** | ✅ Complete | 2026-11-01 | `scenario_blueprint.json` (61 KB) exported and verified |
| **CP 8b: Live Portfolio Showcase** | ✅ Complete | 2026-11-02 | Published to Vercel at `https://marc-portfolio-sigma.vercel.app/projects/agency-client-intake-workflow` |
| **CP 9: Loom Video Walkthrough** | 🔄 Next Step | Pending | 2-min Loom recording (`loom_video_script.md`) |
| **CP 10: Final Application Submission** | 🔄 Pending | Pending | Email package to `careers@chromatix.com.au` |

---

## 📝 Detailed Checkpoint Checklist

### ✅ Completed Checkpoints

- [x] **CP 1: Ingestion & Trigger Architecture**
  - [x] Created Make scenario: `Chromatix - Client Intake Scope Synthesis`
  - [x] Generated custom webhook URL: `https://hook.eu1.make.com/3wpxdnxtla596csibkygxrhda25xjqht`
  - [x] Created Python automated test trigger: `send_test_webhook.py`
  - [x] Sent initial handshake payload to determine data structure

- [x] **CP 2: Direct RESTful AI Integration (OpenRouter)**
  - [x] Architectural decision: Used Make's generic HTTP module rather than pre-built vendor wrappers to prove raw API capability.
  - [x] Configured endpoint: `https://openrouter.ai/api/v1/chat/completions` (POST).
  - [x] Configured Authorization header: `Bearer sk-or-v1-...` and `Content-Type: application/json`.
  - [x] Mapped dynamic variables: `{{1.client_name}}`, `{{1.client_email}}`, `{{1.inquiry_text}}`.

- [x] **CP 3: Structured JSON Parsing**
  - [x] Connected Make's `JSON: Parse JSON` module.
  - [x] Mapped JSON string to `4.Data.choices[ ]: message.content`.
  - [x] Extracted variables: `client_name`, `project_category`, `recommended_cms`, `key_features_requested`, `missing_critical_prerequisites`, `is_ready_for_proposal`, `draft_client_email`, `internal_scoping_brief`.

- [x] **CP 4: Router & Conditional Logic**
  - [x] Configured Router with 2 discrete operational paths.
  - [x] Set Top Filter (`Needs Clarification`): `5.is_ready_for_proposal` Equal to (boolean) `false`.
  - [x] Set Bottom Filter (`Ready for Proposal`): `5.is_ready_for_proposal` Equal to (boolean) `true`.

- [x] **CP 5: Action Endpoints Configuration**
  - [x] Route 1: Connected **Gmail** (`Create a Draft`). Mapped recipient, dynamic subject, and `draft_client_email`.
  - [x] Route 2: Connected **Google Docs** (`Create a Document`). Set target Drive location to `/Job-Application-DB/Applications/Chromatix - AI Automation Developer/projects/Test/`.

- [x] **CP 6: Live Verification & Debugging Case Studies**
  - [x] Test Case 1 Run (Sarah Jenkins): Triggered top branch; generated Australian-English clarification draft in Gmail.
  - [x] Resolved Bug 1: Google OAuth v2 scope limitation (`403 Insufficient Scopes`) & decoupled Settings API signature check.
  - [x] Test Case 2 Run (David Ross): Discovered over-eager AI gating on post-contract secrets (API keys/hosting logins).
  - [x] Resolved Bug 2: Re-engineered system prompt with Two-Stage Scoping Taxonomy & Commercial Assumption Safeguard.
  - [x] Re-tested Test Case 2: Bottom route illuminated `(1)`; verified live Google Doc created in Drive (`1DcemCQWCtlobi8YCdXS7TZb2YdTgwbVcREgELwRbIHs`).
  - [x] Compiled `DEBUG_CASE_STUDIES.md` with What, Why, How, Fix format and 11 screenshot assets.

- [x] **CP 7: Production Hardening Triad (Verified Live ✅)**
  - [x] **7a. Error Handling (`Retry` Directive):** Attached `Retry` directive (formerly `Break` in legacy Make UI) to Module 2 (OpenRouter HTTP) with 3 retries / 1-minute interval. Enabled "Allow storing of incomplete executions" in bottom Scenario Settings.
  - [x] **7b. Webhook Response (Synchronous Acknowledgment):** Added `Webhook Response` module returning HTTP 200 with structured JSON acknowledgement (`status: success`, `client_name`, `project_category`, `is_ready_for_proposal`) and header `Content-Type: application/json` back to the calling website form.
  - [x] **7c. Team Notification (Sales Pipeline Alert):** Added internal email alert module on Route 2 after Google Docs creation, notifying `marczapanta0@gmail.com` of newly generated briefs with direct clickable Google Doc `webViewLink`. Verified email delivered to inbox.

---

- [x] **CP 8: Scenario Blueprint Export (Complete ✅)**
  - [x] Clicked `...` on Make bottom toolbar and exported blueprint JSON.
  - [x] Verified scenario blueprint structure: `scenario_blueprint.json` (61,042 bytes) containing all 8 operational modules, `builtin:Break` error handler (`retry: true, count: 3, interval: 1`), and dual-route branching.
  - [x] Synchronized to Google Drive cloud.

---

### 🔄 Remaining Checkpoints (To Complete Before Submission)

- [ ] **CP 9: Loom Video Recording**
  - Follow the 2-minute structure in `loom_video_script.md`:
    - 0:00 - 0:10: The Hook & Agency Problem (Messy briefs cost 1 hr/lead).
    - 0:10 - 1:15: Canvas Walkthrough (Webhook ➔ HTTP ➔ JSON ➔ Webhook Response ➔ Router ➔ Gmail / Google Docs + Team Alert).
    - 1:15 - 1:45: Production Reliability Proof (Walk through the 2 debug case studies: OAuth scopes & Pre-sales prompt boundaries).
    - 1:45 - 2:00: Competitive Moat & Call to Action.
  - Paste Loom link into `README.md` and application email.

- [ ] **CP 10: Final Application Submission**
  - Send email package to `careers@chromatix.com.au` with tailored resume, cover letter, Loom link, and GitHub/Google Drive portfolio link.

---

## 🔍 QA Architectural Audit & Production Hardening Roadmap

| Production Layer Flagged by QA | Purpose & Real-World Impact | Sprint Phase Decision | Implementation Path |
|---|---|---|---|
| **1. Error Handling (`Retry` Directive)** | Prevents losing leads on OpenRouter 429 rate limits or timeouts. | **P1: Implemented & Verified ✅** | Attached `Retry` directive to Module 2 with 3 retries / 1-min interval. |
| **2. Webhook Response / Acknowledgment** | Returns structured JSON to the website form (e.g. Gravity Forms) confirming receipt. | **P1: Implemented & Verified ✅** | Added `Webhook Response` returning 200 JSON with lead metadata. |
| **3. Team Success Notification** | Alerts account executive/tech lead when a Google Doc proposal brief is generated on Route 2. | **P1: Implemented & Verified ✅** | Added internal Gmail alert on Route 2 with clickable Google Doc link. |
| **4. Input Validation / Pre-Processing** | Rejects blank emails, phone spam, or malformed webhook payloads before calling AI. | **P2: Document in Roadmap** | Highlight in Loom video & README as Next-Sprint enhancement. |
| **5. Audit / Logging Layer** | Appends every raw lead and triage outcome to a centralized Google Sheet / BigQuery. | **P2: Document in Roadmap** | Showcase as an architectural talking point to avoid canvas clutter. |
| **6. Environment Variable Management** | Stores OpenRouter Bearer tokens in Make Custom Variables instead of hardcoded strings. | **P2: Document in Roadmap** | Demonstrate awareness of secrets management in interview prep. |

---

## 🧠 Marc's Learning Memory & Skill Build-Up Ledger
*(Auto-saved for review at the beginning of the next session)*

| # | Topic / Concept | What Felt Challenging | The Technical Reality | How to Review Next Session |
|---|---|---|---|---|
| 1 | **Data Typing (Boolean vs String/Number)** | Wondering why `is_ready_for_proposal` needed a Boolean operator and why no preview text appeared next to the purple tag in Make. | In JSON, `false` is a literal primitive, not the text `"false"` or integer `0`. In Make, `false` often has no text label in pill previews. Using text operators can cause silent capitalization comparison bugs. | Quick quiz: Given a JSON payload with `"status": true` vs `"status": "true"`, which operator in Make should be selected and why? |
| 2 | **OAuth 2.0 Scope Architecture** | Encountering `403 Insufficient Scopes` even though Google login succeeded; signature dropdown failing to load. | Authentication (knowing who you are) is distinct from Authorization (what you are permitted to do). Gmail compose requires `gmail.compose`, while signatures call `gmail.settings.basic`. Decoupling optional dropdowns via `Map` prevents cascading failures. | Practice setting up a third-party Google or Slack integration and auditing requested scopes in the consent dialog. |
| 3 | **Prompt Scoping Boundaries** | Why the AI marked David Ross as `false` even though he provided a comprehensive brief. | LLMs follow rules literally. Without an explicit boundary, the AI demanded API keys and server passwords during an initial pre-sales inquiry. Establishing a Two-Stage Taxonomy (Pre-Sales Gates vs Post-Contract Onboarding) gives sales speed without delivery risk. | Review prompt rules: How do you balance strictness in entity extraction while preventing pre-sales friction? |
| 4 | **Error Handling & Architecture Staging** | Understanding why error handling was omitted during initial scenario assembly and where it belongs. | "Build Happy Path First, Then Harden." Adding error handlers prematurely obscures core logic debugging. In production, Make error directives (`Retry`, `Resume`, `Skip`) provide resilience against API rate limits and invalid JSON. | Design the error recovery plan: Where would a `Retry` directive attach, and what should a Router Fallback route do with malformed payloads? |
| 5 | **Make UI Directive Evolution & Incomplete Executions** | Looking for the classic `Break` directive and seeing error: `Directive requires storing of incomplete executions`. | Make modernized its terminology: `Break` ➔ `Retry`, `Ignore` ➔ `Skip`. Furthermore, `Retry` requires the scenario engine to persist failed bundles in state, requiring the bottom Scenario Settings toggle "Allow storing of incomplete executions" = Yes. | Explain the difference between `Retry` (storing bundle to try again) vs `Skip` (discarding erroneous bundle and moving on). |
| 6 | **HTTP Status Code Protocols** | Asking why status code `200` is used rather than custom numbers like `150`, `130`, or `120`. | HTTP status codes are strict RFC specifications: `2xx` = Success (200 OK, 201 Created), `4xx` = Client Error, `5xx` = Server Error. Non-standard codes cause client libraries and browser form handlers to throw connection faults. | Name the 3 most common HTTP response codes used in REST webhooks and their meanings. |
| 7 | **Synchronous vs Asynchronous Webhooks** | Python test script timing out (10s read timeout) once `Webhook Response` was added. | Without a `Webhook Response`, Make answers immediately with `200 Accepted` (asynchronous). Adding a `Webhook Response` turns the scenario into a synchronous pipeline where Make holds the HTTP socket open until the response module fires. | When would an agency choose an immediate 200 Accepted vs a synchronous Webhook Response? |

---

## 📁 Project Artifact Directory Map

```text
projects/agency-client-intake-workflow/
├── DEBUG_CASE_STUDIES.md         <-- Comprehensive failure-mode report (What/Why/How/Fix)
├── PROJECT_DASHBOARD_CHECKLIST.md <-- This live dashboard & progress tracker
├── PROJECT_CHECKPOINT.md         <-- Technical scenario architecture snapshot
├── README.md                     <-- High-level portfolio presentation overview
├── loom_video_script.md          <-- 2-minute video presentation script
├── sample_payloads.json          <-- Test payloads (Sarah Jenkins & David Ross)
├── send_test_webhook.py          <-- Automated Python trigger script
├── system_prompt.txt             <-- Production-tested two-stage scoping prompt
└── screenshots/                  <-- 19 high-res audit screenshots
    ├── 01_gmail_signature_403_warning.png
    ├── 02_gmail_error_403_insufficient_permissions.png
    ├── 03_gmail_fix_execution_success.png
    ├── 04_gmail_fix_draft_inbox.png
    ├── 05_david_ross_unexpected_route_canvas.png
    ├── 06_david_ross_ai_strict_false_output.png
    ├── 07_david_ross_generated_email_draft.png
    ├── 08_fixed_canvas_gdocs_route2_green.png
    ├── 09_gdocs_execution_bundle_success.png
    ├── 10_gdocs_file_in_google_drive.png
    ├── 11_gdocs_rendered_scoping_brief.png
    ├── 12_canvas_with_retry_error_handler.png
    ├── 13_webhook_response_configured.png
    ├── 14_webhook_response_with_headers.png
    ├── 15_team_notification_module_configured.png
    ├── 16_webhook_response_live_execution.png
    ├── 17_gdocs_live_execution_with_caveats.png
    ├── 18_gmail_team_alert_execution_inspector.png
    └── 19_gmail_team_alert_received_inbox.png
```
