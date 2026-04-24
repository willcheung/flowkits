# FlowKits.ai — Messaging & Positioning Decisions
## Documented April 23, 2026

---

## The Core Pain Point

**Setting up AI automation from scratch is a huge time sink.** Founders and devs know they should automate (email triage, meeting prep, outbound campaigns) but every time they sit down to build it, it's a weekend of prompt engineering, API wiring, and error handling. They want the workflow, not the project.

This is broader than "n8n is bad." It applies to:
- People who've never heard of n8n
- People who tried n8n and bounced off it
- People who could build it themselves but don't have time
- People who want pre-built AI workflows and don't want to learn a platform

---

## The Operating Model: AI Agent as Operator

Users don't run these workflows manually. Their AI agent does.

Every FlowKit includes an AGENTS.md file — the operating manual that tells Claude, Cursor, Copilot (or any AI coding agent) how to:
- **Run** the workflow on a schedule or trigger
- **Monitor** execution and report results
- **Diagnose** failures by reading logs and error output
- **Fix** issues by modifying the Python code directly
- **Extend** the workflow with new capabilities

This is why Python beats n8n for this use case: AI agents can read, modify, and debug Python. They can't do that with n8n's visual JSON editor.

The "hosting" is the AI agent itself. No n8n server, no Docker, no platform to self-host. The paid tier adds monitoring and auto-healing infrastructure on top of the AI agent's autonomous operation.

---

## Key Messaging Decisions

### 1. n8n is a credibility signal, not a punching bag

**Before:** The entire landing page was anti-n8n ("n8n workflows are where automation goes to die"). This only resonated with the ~50K people who know what n8n is and have been burned by it.

**After:** n8n is used as social proof. "Built from n8n's most popular templates" tells visitors these are proven patterns with thousands of users, not random scripts. This serves both audiences:
- **n8n-aware visitors** think "I don't need to learn n8n"
- **n8n-unaware visitors** see social proof (popular templates, thousands of users)

**Where n8n appears:**
- Hero badge: "Built from n8n's most popular templates"
- Why FlowKits subheader: mentions templates with thousands of users
- Workflow cards: "Based on n8n template #XXXX"
- Comparison strip reframed as "Building it yourself / low-code" vs FlowKits

### 2. "Battle-tested" is warranted

The workflows are built from n8n templates that have thousands of real users. They're proven automation patterns, rebuilt in Python with AI reasoning added. This isn't marketing fluff — it's a factual description of the provenance.

### 3. Show the product before the pitch

**Before:** The page was ~90% problem, ~10% solution, 0% product. No workflow names, no code previews, no categories.

**After:** Workflow Showcase section shows 3 concrete workflows immediately after the hero:
- Gmail AI Labeler (Free)
- Pre-Meeting Briefing ($15)
- Sheets Email Campaign ($19)

Each card includes: name, category, price, one-line description, tech stack, n8n basis, and a placeholder for workflow visualization (to be added from n8ntocode repo).

### 4. Two value props, not four

**Before:** 4 feature cards (Real Python, AI reasoning, Error handling, Debuggable). "AI reasoning built in" and "Production error handling" sounded like code features, but they're implementation details.

**After:** 2 cards that capture the actual value:
1. "Just Python. No platform to learn." — you don't need to learn n8n or any visual editor
2. "Your AI agent keeps it running." — AGENTS.md lets Claude/Cursor/Copilot operate the workflow autonomously

Error handling, retry logic, structured logging — those are real, but they belong in the workflow READMEs, not the landing page headline. The landing page sells the outcome, the README sells the engineering.

### 5. Surface the open-source + paid monitoring model

**Before:** The Terraform-like model (free code, paid monitoring) — the strongest differentiator — was invisible on the page.

**After:** Dedicated "Code is free. Monitoring is the product." section explains:
- Free: open-source code, AI agent runs it
- Paid: execution dashboard, success rates, duration tracking
- Paid: auto-healing — AI agent diagnoses, fixes, and retries

This builds trust with technical buyers and makes the business model transparent.

### 6. Widen the target audience

**Before:** Only resonated with frustrated n8n users (~50K people).

**After:** Targets anyone who wants production AI automation without building from scratch. The headline "AI workflows you'd build yourself — if you had the weekend" is relatable to any developer or founder, regardless of n8n familiarity.

---

## Page Structure (Current)

1. **Hero** — Pain point + n8n credibility badge + CTAs (Browse workflows / Get early access)
2. **Workflow Showcase** — 3 concrete workflow cards with prices and visualization placeholders
3. **Why FlowKits** — 4 feature cards + "Building it yourself vs FlowKits" comparison
4. **Open Source Model** — Free code / Paid monitoring / Paid alerts
5. **Email Capture** — Waitlist signup
6. **Footer** — Links + credits

---

## Planned Visual Additions

- Workflow node visualizations from n8ntocode repo (static renders of workflow graphs alongside Python code)
- To be wired up in workflow showcase cards where the placeholder currently sits

---

## What We're NOT Saying

- We don't claim to be an n8n replacement (different category)
- We don't bash low-code tools directly (they're "great for prototyping")
- We don't promise features we haven't built yet (no mention of marketplace, creator program, or subscription tier on the landing page)
- We don't overstate the team size or traction
- We don't say "no self-hosting" — the hosting model IS self-hosting, but via AI agent (which is the whole point)

---

*Decisions by Will + TARS — April 23, 2026*
