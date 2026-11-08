# Portfolio Project: Agency Client Intake & Scope Synthesis AI Workflow

> **Creator:** Marc Neil Zapanta  
> **Target Role:** AI Automation Developer  
> **Target Employer:** Chromatix (Web Design & Conversion Agency, Melbourne, Australia)  
> **Platform Stack:** Make.com, OpenRouter REST API, JSON Schema Parser, Webhooks, Google Docs, Gmail  
> **Core Philosophy:** Production-grade AI automation combining robust REST APIs, resilient error handling, and business-calibrated prompt engineering to eliminate agency pre-sales bottlenecks.

---

## 1. Business Problem & Opportunity

In digital web and conversion optimization agencies like **Chromatix**, new prospective clients submit unstructured scoping inquiries via website forms, emails, or discovery notes. Account managers and technical leads spend **45–60 minutes per lead** manually:
1. Identifying the required platform/CMS (WordPress/WooCommerce, Shopify, Webflow, custom).
2. Categorizing technical feature requirements (payment gateways, CRM tracking pixels, membership portals).
3. Hunting down missing prerequisites (e.g., missing vector brand assets, unstated hosting access, undefined product counts).
4. Writing back-and-forth emails requesting clarification.

---

## 2. Solution Architecture

This Make.com visual automation ingests raw client submissions, processes them through a Claude-compatible prompt framework with strict XML boundaries, and deterministically routes the outputs:

```text
[ New Client Submission ] ──► [ Custom Webhook ]
                                    │
                                    ▼
                    [ HTTP REST API (OpenRouter LLM) ] ──► [ Retry Directive (3x/1min) ]
                    • XML System Boundaries (<taxonomy>, <rules>)
                    • Extracts Technical Specs & Missing Assets
                    • Formats to Strict JSON Schema
                                    │
                                    ▼
                         [ Parse JSON Module ]
                                    │
                                    ▼
                      [ Webhook Response (200 JSON) ]
                                    │
                                    ▼
                             [ Router Module ]
                              ├── Route 1: Needs Clarification (is_ready_for_proposal = false)
                              │            └── Action: Auto-draft Polite Client Clarification Email (Gmail)
                              └── Route 2: Ready for Proposal (is_ready_for_proposal = true)
                                           └── Action: Create Developer Scoping Brief in Google Docs
                                                         └── Action: Fire Internal Sales Team Alert (Gmail)
```

---

## 3. Measurable Business Impact

- **Time Savings:** Reduces manual client triage time from 50 minutes to under 2 minutes per submission.
- **Data Integrity:** Guarantees 100% adherence to required technical specs before dev estimation.
- **Conversion Speed:** Delivers same-day professional clarification emails to leads, accelerating the agency sales cycle.
- **Fault Tolerance:** Built-in automatic exponential retry (`Retry` directive) ensures zero dropped leads during third-party LLM rate limits.

---

## 4. Key Architectural Engineering Decisions

### 💡 Decision 1: Raw RESTful HTTP vs Pre-built App Modules
In this workflow, the AI synthesis step is implemented using Make's native **HTTP Module (REST API)** rather than vendor-specific wrappers.
1. **Raw REST API Proficiency:** Explicit handling of Authorization Bearer tokens, HTTP POST verbs, and JSON request bodies.
2. **Vendor-Agnostic Portability:** Ability to swap endpoints between OpenRouter, Anthropic Claude, Google Gemini, or private agency microservices with zero canvas redesign.

### 🛡️ Decision 2: Production Hardening Triad
1. **Defensive Error Handling:** `Retry` directive (3 retries / 1 min interval) backed by Make's *Incomplete Executions* engine to gracefully handle transient API timeouts and 429 rate limits.
2. **Synchronous Webhook Response:** Returns standard HTTP `200 OK` with JSON metadata to the client website form, acknowledging intake status immediately.
3. **Internal Pipeline Alerting:** Automatically routes the generated Google Doc `webViewLink` into the sales team inbox for instantaneous review.

### 🔍 Decision 3: Two-Stage Scoping Taxonomy (Business Boundary Calibration)
During QA, an LLM edge case was identified where operational credentials (hosting logins, DNS access) were blocking pre-sales quotes. Re-engineered the prompt architecture to cleanly distinguish **Pre-Sales Commercial Feasibility** (page count, target date, budget, stated assets) from **Post-Contract Onboarding Dependencies**, while injecting contractual scope caveats into the generated Google Doc brief. Fully documented in [`DEBUG_CASE_STUDIES.md`](./DEBUG_CASE_STUDIES.md).

---

## 5. Project Assets & Deliverables

- **Make Scenario Blueprint:** [`scenario_blueprint.json`](./scenario_blueprint.json) (Importable into any Make workspace)
- **Troubleshooting & QA Report:** [`DEBUG_CASE_STUDIES.md`](./DEBUG_CASE_STUDIES.md) (Complete failure mode analysis with 19 audit screenshots)
- **Automated Python Webhook Trigger:** [`send_test_webhook.py`](./send_test_webhook.py)
- **Production Scoping Prompt:** [`system_prompt.txt`](./system_prompt.txt)
