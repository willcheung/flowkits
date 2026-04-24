# FlowKits.ai

Battle-tested AI workflows in Python. Not n8n JSON you can't debug.

## Setup

```bash
cd web
npm install
npm run dev
```

## Environment Variables

See Vercel project for production values. Local development needs:

- `DATABASE_URL` — NeonDB connection string
- `AUTH_SECRET` — NextAuth secret
- `AUTH_GITHUB_ID` / `AUTH_GITHUB_SECRET` — GitHub OAuth

## Tech Stack

- Next.js 16, React 19, TypeScript, Tailwind CSS v4
- shadcn/ui, next-themes (dark mode)
- NextAuth v5 + Drizzle ORM + NeonDB
- Stripe (ready, not yet configured)
- Vercel deployment

## Project Structure

```
web/                     # Next.js app (landing page + API)
├── app/                 # App Router (page.tsx, api/)
├── components/          # React components (shadcn + landing)
├── lib/                 # DB, auth, utils
└── drizzle.config.ts
docs/                    # Business docs & workflow catalog
├── strategy.md          # CEO strategy (Apr 15, 2026)
├── execution-plan-weeks-1-3.md  # Week-by-week execution plan
├── workflow-catalog.md  # Full catalog of all workflows
├── workflows/           # Workflow source code
│   ├── gmail-ai-labeler/
│   ├── landing-page-analyzer/
│   ├── human-in-loop-email/
│   ├── pre-meeting-briefing/
│   └── sheets-email-campaign/
└── n8n-research/        # Competitive research on n8n templates
```

## Deployment

Deployed to Vercel as `flowkits-site` project. Custom domain: `flowkits.ai`.
