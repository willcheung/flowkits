# FlowKits.ai — Startup Execution Plan
## Weeks 1-3: Ship or Die
### Created April 17, 2026

---

## Where We Are (Day 0)

**Assets we own:**
- `n8ntocode.com` — LIVE, working product. Converts n8n → Python + AGENTS.md. $5/conversion. Has auth, dashboard, visualization.
- `FlowKits.ai` — Squarespace placeholder. Nothing built.
- `@FlowKitsAI` on X — Premium account, ~70 followers, 3 tweets/day pipeline working
- `VibeCodingDad.com` — Existing product site (Chrome exts, ebook)
- `Expert Tweeter` kit on JourneyKits.ai — published, approved

**What's missing:**
- Zero FlowKits product shipped
- Zero email list
- Zero converted workflows to sell
- FlowKits.ai is a blank page
- No Stripe integration for FlowKits
- No content tying n8ntocode → FlowKits narrative

**Core thesis:** n8ntocode.com converts n8n workflows to Python. FlowKits.ai sells verified, AI-enhanced versions. Funnel: n8ntocode (free first taste) → FlowKits (premium). Sell the recipe, not the kitchen.

---

## WEEK 1: Foundation & Content (Apr 17-23)

### Goal: Lay groundwork, build narrative, start driving traffic

**PRODUCT TASKS:**

| # | Task | Owner | Done? |
|---|------|-------|-------|
| 1.1 | Convert top 5 n8n workflows with n8ntocode, verify they work end-to-end | TARS | |
| 1.2 | Enhance those 5 with AI reasoning, error handling, autonomous operation | TARS | |
| 1.3 | Set up FlowKits.ai on Vercel/Next.js (replace Squarespace) | Will/TARS | |
| 1.4 | Create FlowKits landing page with: value prop, email capture, "coming soon" | TARS | |
| 1.5 | Set up Stripe Checkout for FlowKits (individual product purchases) | Will | |
| 1.6 | Add "Convert on FlowKits.ai" CTA to n8ntocode.com | Will/TARS | |

**CONTENT TASKS:**

| # | Task | Type | Slot |
|---|------|------|------|
| 1.7 | "I converted n8n's #1 marketing workflow to Python. Here's what broke." | Build-in-public | Morning |
| 1.8 | "n8n workflows are deterministic. AI agents are not. That's the whole game." | Insight | Afternoon |
| 1.9 | Show real n8ntocode before/after (screenshot thread or long tweet) | Product demo | Evening |
| 1.10 | n8n pain point thread — "5 ways n8n workflows fail in production" | Build-in-public | Any |
| 1.11 | Firsthand tool review — something we're actually using | Tool review | Any |
| 1.12 | Founder case study — find an AI founder doing something interesting | Case study | Any |

**ENGAGEMENT:**
- Reply to every @ mention (already automated)
- Proactive engagement: 3 genuine replies/day on AI founder/build-in-public tweets
- Follow 10 AI builder accounts per day

**METRICS TO TRACK:**
- n8ntocode conversions this week (baseline)
- @FlowKitsAI follower count
- Email signups on FlowKits.ai (once live)
- Best performing tweet topic

**WEEK 1 EXIT CRITERIA:**
- [ ] 5 verified, AI-enhanced workflows ready to sell
- [ ] FlowKits.ai landing page live with email capture
- [ ] At least 2 build-in-public tweets about the conversion process
- [ ] n8ntocode → FlowKits funnel direction established in content

---

## WEEK 2: The Upgrade Narrative (Apr 24-30)

### Goal: Convert n8ntocode users → FlowKits early adopters

**PRODUCT TASKS:**

| # | Task | Owner | Done? |
|---|------|-------|-------|
| 2.1 | List 5 workflows on FlowKits.ai with Stripe checkout | TARS | |
| 2.2 | 3 free workflows (lead gen: simple email, scheduling, webhook) | TARS | |
| 2.3 | 2 premium workflows ($15-25): AI-enhanced with reasoning, retry logic, autonomous | TARS | |
| 2.4 | Product page template: description, features, code preview, compatibility badges | TARS | |
| 2.5 | "How to install" guide for each workflow (README + AGENTS.md) | TARS | |
| 2.6 | Test full purchase flow end-to-end (buy, download, run) | Will/TARS | |
| 2.7 | Add FlowKits link to n8ntocode conversion confirmation page | Will/TARS | |
| 2.7a | Build heartbeat webhook receiver (Cloudflare Worker) + Supabase table — logging only, no dashboard UI | TARS | |
| 2.7b | Define public heartbeat schema: kit_id, execution_id, status, duration, timestamp — publish in docs | TARS | |
| 2.7c | Embed heartbeat hook in all premium kits — zero config, pings on start/success/fail | TARS | |

**CONTENT TASKS:**

| # | Task | Type | Slot |
|---|------|------|------|
| 2.8 | "n8n workflow → AI agent workflow. Same automation, completely different brain." | Product | Morning |
| 2.9 | ClawMart quality audit tweet (from competitive research) | Hot take | Afternoon |
| 2.10 | "What if your automation could think, not just route?" | Insight | Evening |
| 2.11 | Behind the scenes: how we verify workflows (the testing process) | Build-in-public | Any |
| 2.12 | n8ntocode real conversion demo (screencast or screenshots) | Product demo | Any |
| 2.13 | "FlowKits is coming. Here's why." — first public mention of FlowKits | Announcement | Any |

**GROWTH:**
- Post n8n conversion content to Reddit (r/n8n, r/Automate) — careful, add value don't spam
- First FlowKits email to waitlist (if we have signups): "what we're building"
- Consider Product Hunt "upcoming" page

**WEEK 2 EXIT CRITERIA:**
- [ ] 5 workflows listed on FlowKits.ai (3 free + 2 premium)
- [ ] Stripe purchase flow working end-to-end
- [ ] At least 1 paying customer (even if it's Will testing)
- [ ] First public FlowKits mention on X
- [ ] Email list started (even if small)

---

## WEEK 3: Soft Launch (May 1-7)

### Goal: First real revenue, validate the model

**PRODUCT TASKS:**

| # | Task | Owner | Done? |
|---|------|-------|-------|
| 3.1 | Expand to 10 total workflows (add 5 more) | TARS | |
| 3.2 | Add 2 more premium workflows ($25-50 range) | TARS | |
| 3.3 | Bundle deal: "AI Agent Starter Pack" (3-5 workflows, $49-79) | TARS | |
| 3.4 | Improve FlowKits.ai discovery: search, categories, tags | TARS | |
| 3.5 | Add customer testimonials section (even if just early beta users) | TARS | |
| 3.6 | Set up analytics: track page views, conversion rate, revenue | Will/TARS | |
| 3.6a | Build execution dashboard UI (run count, success rate, failure log) — only after 1+ week of heartbeat data exists | TARS | |
| 3.6b | Add failure alerting (email/webhook) to dashboard | TARS | |

**CONTENT TASKS:**

| # | Task | Type | Slot |
|---|------|------|------|
| 3.7 | "Building FlowKits: week 1" — architecture, decisions, mistakes | Build-in-public | Morning |
| 3.8 | "Why we're not another ClawMart" — quality > quantity positioning | Positioning | Afternoon |
| 3.9 | Share real numbers: conversions, sales, lessons | Metrics | Evening |
| 3.10 | "The 3 things we learned from ClawMart's $100K marketplace" | Insight | Any |
| 3.11 | Workflow spotlight tweet — feature one specific workflow with demo | Product | Any |
| 3.12 | "What workflow would your AI agent buy?" — engagement bait (good kind) | Engagement | Any |

**LAUNCH MOMENTS:**
- "FlowKits is live. Here's what it is." — main announcement tweet
- Multi-tweet story arc over 2-3 days (not one tweet and done)
- Share every sale publicly (build-in-public)
- Reply to EVERY comment on launch tweets

**GROWTH:**
- Hacker News "Show HN" post
- Reddit: r/SideProject, r/Entrepreneur, r/ArtificialIntelligence
- Cross-post to any AI builder communities
- Email to waitlist with launch announcement

**WEEK 3 EXIT CRITERIA:**
- [ ] 10 workflows listed (5+ premium)
- [ ] Bundle deal available
- [ ] Public launch tweet posted
- [ ] Analytics tracking revenue and conversion
- [ ] First real external customer
- [ ] Revenue > $0 (even $15 counts)

---

## RISK MATRIX

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| n8ntocode conversions are broken | Low | High | Test all 5 conversions in Week 1 before promoting |
| Nobody wants to pay for workflows | Medium | Critical | Free tier + bundle deal; pivot to subscription if needed |
| ClawMart crushes us | Low | Medium | Different positioning (quality + AI-native, not personas) |
| FlowKits.ai build takes too long | Medium | High | Start with Gumroad if needed — sell first, build storefront later |
| X algorithm kills our reach | Medium | Medium | Diversify to Reddit, HN, email list |
| n8n licensing issues | Low | High | n8n is MIT-licensed; credit authors, don't redistribute their JSON |

## DECISIONS NEEDED FROM WILL

1. **FlowKits.ai hosting** — Vercel/Next.js (my recommendation) or something else?
2. **Stripe** — Can you set up Stripe Checkout, or should I use Gumroad/LemonSqueezy as interim?
3. **First 5 n8n workflows** — Should I pick the top from n8n template gallery, or do you have specific ones in mind?
4. **Time commitment** — How many hours/week can you put into this? Sets the pace.
5. **n8ntocode traffic** — Do we have any analytics on current n8ntocode usage? Conversions per week?

---

*Plan by TARS (AI cofounder) — April 17, 2026*
*Strategy doc: `~/.hermes/workspace/memory/flowkits-strategy-2026-04-15.md`*
