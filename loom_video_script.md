# 2-Minute Loom Walkthrough Script: Agency Client Intake & Scope Synthesis AI Workflow

> **Goal:** 2-minute high-impact video walking through the Make.com scenario, demonstrating the business problem, live dual-route data flow, production hardening, and debugging reliability.
> **Target Audience:** Chromatix Hiring Team (Melbourne, Australia)  
> **Target Role:** AI Automation Developer  
> **Speaker:** Marc Neil Zapanta  

---

### 1. The Hook & Agency Problem (0:00 – 0:20)
*(Camera on face or split-screen with Make.com canvas)*

> "Hi Chromatix team, I'm Marc Neil Zapanta. Having spent over 5 years optimizing customer operations and CRM pipelines, I know firsthand that one of the biggest hidden costs for web design and conversion agencies is manual pre-sales scoping. When prospective clients submit messy, incomplete inquiry forms, account managers spend 45 to 60 minutes per lead manually triaging CMS platforms, identifying missing assets, and writing follow-up emails.
> 
> Today, I'm excited to walk you through an AI intake and scope synthesis workflow I engineered on Make.com—built to turn unstructured client inquiries into structured, production-ready proposals in under two minutes."

---

### 2. The Architecture & Hardened Pipeline (0:20 – 0:50)
*(Screen: Make.com scenario canvas)*

> "Here is the full 8-module pipeline:
> - It triggers via a **Custom Webhook** receiving the client submission.
> - The payload feeds directly into an **HTTP Module** executing raw REST calls to OpenRouter with Bearer authentication. *(I intentionally engineered this with direct HTTP rather than a vendor-specific wrapper to prove raw API protocol mastery and keep our architecture model-agnostic—whether connecting to Claude, Gemini, or private agency endpoints).*
> - To make this enterprise-ready, I attached a **`Retry` error directive** that automatically retries up to three times with backoff, ensuring zero dropped leads during third-party API rate limits.
> - A **JSON Parser** extracts eight discrete schema variables, and a **Webhook Response** immediately acknowledges the submission back to the website form with HTTP 200 and structured JSON metadata.
> - Next, our **Router** evaluates the client's readiness."

---

### 3. Dual-Route Logic & Real-World Debugging Proof (0:50 – 1:35)
*(Screen: Zoom in on Router branches, then show Gmail draft and Google Doc brief)*

> "The router operates on two deterministic paths:
> - **Route 1 (Needs Clarification):** If critical pre-sales requirements are missing—like Sarah Jenkins submitting an e-commerce inquiry without brand guidelines—the system halts quotation and automatically drafts a personalized Australian-English clarification email in Gmail for the account manager to review with one click.
> - **Route 2 (Ready for Proposal):** If commercial viability is established—like David Ross's 7-page WordPress B2B website—it automatically generates a formatted **Technical Scope Brief in Google Docs** and immediately alerts our internal sales team via email with a direct link.
> 
> During development, I pressure-tested this against real-world edge cases. I resolved a granular Google OAuth 403 scope permission error by decoupling settings API dependencies, and fine-tuned our prompt into a **Two-Stage Scoping Taxonomy**—ensuring post-contract secrets like hosting logins never block pre-sales quoting, while automatically embedding contractual asset verification caveats directly into the generated brief."

---

### 4. Competitive Moat & Call to Action (1:35 – 2:00)
*(Screen: Brief switch back to camera or summary screen)*

> "Because the prompt architecture follows strict Anthropic XML boundaries and JSON Schema validation, this entire workflow is 100% portable into Claude workspaces and MCP tool servers on day one.
> 
> What I bring to Chromatix isn't just workflow building—it's defensive architecture, deep API proficiency, and 5+ years of frontline customer intuition to ensure automations actually drive conversion. I'm available full-time during Melbourne business hours, and I'd love to discuss how I can help streamline Chromatix's internal operations.
> 
> Thanks for watching!"
