# n8ntocode

Convert n8n workflow JSON exports into clean, runnable Python projects.

**Live:** [n8ntocode.com](https://n8ntocode.com)

## Features

- **Paste & convert** — Drop in n8n workflow JSON and get a Python project with `workflow.py`, `config.py`, `requirements.txt`, and metadata
- **45+ supported node types** — HTTP Request, Webhook, Google Sheets, Slack, Gmail, OpenAI, Anthropic, Postgres, MySQL, Airtable, and more
- **LLM fallback for custom nodes** — Any node type not natively supported is automatically handled by Gemini, which generates Python code based on the node's configuration. Results are cached in Postgres for fast repeat conversions.
- **Python syntax validation** — After conversion, all generated `.py` files are validated with `ast.parse()` via a Vercel Python serverless function. Results appear as a green/red badge in the UI.
- **Auto-fix syntax errors** — If validation detects syntax errors, Gemini automatically attempts to fix them. The UI shows "Fixing syntax errors..." and re-validates after the fix.
- **Workflow visualization** — Interactive graph view of your workflow using React Flow
- **Download as ZIP** — One-click download of the entire generated project

## Tech Stack

- **Frontend:** Next.js 16 (App Router), React 19, Tailwind CSS v4, React Flow
- **Backend:** Next.js API routes, Vercel Python serverless functions
- **Database:** Neon Postgres + Drizzle ORM
- **LLM:** Google Gemini (`gemini-3-flash-preview`) for unsupported node code generation
- **Auth:** NextAuth.js with GitHub provider
- **Payments:** Stripe Checkout

## Getting Started

```bash
# Install dependencies
npm install

# Set up environment variables (copy from Vercel or create manually)
cp .env.example .env.local

# Run database migrations
npx drizzle-kit push

# Start dev server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

## Environment Variables

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | Neon Postgres connection string |
| `GEMINI_API_KEY` | Google Gemini API key for LLM fallback |
| `NEXTAUTH_SECRET` | NextAuth.js secret |
| `GITHUB_ID` | GitHub OAuth app client ID |
| `GITHUB_SECRET` | GitHub OAuth app client secret |
| `STRIPE_SECRET_KEY` | Stripe secret key |
| `STRIPE_WEBHOOK_SECRET` | Stripe webhook signing secret |

## Project Structure

```
web/
├── app/
│   ├── api/
│   │   ├── convert/route.ts      # Main conversion endpoint
│   │   ├── fix-syntax/route.ts   # Gemini-powered syntax error fixer
│   │   ├── auth/                  # NextAuth.js routes
│   │   └── stripe/                # Stripe checkout & webhooks
│   ├── convert/page.tsx           # Converter UI (split-pane editor)
│   └── page.tsx                   # Landing page
├── api/
│   └── validate.py                # Python serverless function (ast.parse validation)
├── components/
│   ├── convert/                   # JSON input, code output components
│   └── visualize/                 # React Flow workflow graph
├── lib/
│   ├── converter/
│   │   ├── parser.ts              # n8n JSON → ParsedWorkflow
│   │   ├── generators/            # Code generators per node type
│   │   └── types.ts               # TypeScript types
│   ├── db/
│   │   └── schema.ts              # Drizzle schema (users, conversions, node_code_cache)
│   ├── llm/
│   │   ├── gemini.ts              # Gemini API client
│   │   └── node-fallback.ts       # Cache-first LLM fallback for custom nodes
│   └── validate.ts                # Client-side validation caller
└── drizzle.config.ts
```

## How It Works

1. **Parse** — The n8n workflow JSON is parsed into steps and edges
2. **Generate** — Each step is mapped to a Python code generator. 45+ node types have hand-written generators; all others are handled by Gemini LLM with Postgres caching.
3. **Validate** — Generated Python files are syntax-checked with `ast.parse()` (no execution)
4. **Auto-fix** — If syntax errors are found, Gemini receives the broken code + error details and fixes them (1 attempt per file, capped)
5. **Download** — The project is bundled as a ZIP with `workflow.py`, `config.py`, `requirements.txt`, and metadata

## Deployment

Deployed on Vercel. The convert API has a 300s max duration (Pro plan) to handle complex workflows with many LLM-generated nodes.

```bash
vercel --prod
```
