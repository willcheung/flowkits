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
web/
├── app/          # Next.js App Router
│   ├── api/      # API routes (auth, subscribe)
│   └── page.tsx  # Landing page
├── components/   # React components (shadcn + landing)
├── lib/          # DB, auth, utils
└── drizzle.config.ts
```

## Deployment

Deployed to Vercel as `flowkits-site` project. Custom domain: `flowkits.ai`.
