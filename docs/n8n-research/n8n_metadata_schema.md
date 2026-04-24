# n8n Workflow Metadata Schema

## Fields from n8n API (source of truth)

Every workflow entry from the API contains:

```json
{
  "id": 5338,
  "name": "Generate AI Viral Videos...",
  "user": {
    "name": "Dr. Firas",
    "username": "drfiras",
    "verified": true,
    "avatar": "https://..."
  },
  "totalViews": 214907,
  "createdAt": "2025-06-25T20:50:20.762Z",
  "nodes": [
    {"displayName": "Google Sheets", "name": "n8n-nodes-base.googleSheets"},
    {"displayName": "HTTP Request", "name": "n8n-nodes-base.httpRequest"},
    {"displayName": "Merge", "name": "n8n-nodes-base.merge"}
  ],
  "categories": [
    {"name": "Marketing"},
    {"name": "Content Creation"}
  ],
  "description": "Full description text...",
  "url": "https://n8n.io/workflows/5338-..."
}
```

## Key Fields for FlowKits Assessment

| Field | API Key | Why It Matters |
|-------|---------|----------------|
| Workflow ID | `id` | Primary key, needed to fetch JSON later |
| Title | `name` | Product naming |
| URL | `url` | Direct link to n8n template |
| Creator | `user.name` / `user.username` / `user.verified` | Quality signal — verified creators tend to be better |
| Views | `totalViews` | Popularity/demand signal |
| Created | `createdAt` | Recency — newer = more relevant |
| Nodes | `nodes[].displayName` | What integrations it uses — determines feasibility for Python conversion |
| Node count | `nodes.length` | Complexity indicator |
| Categories | `categories[].name` | Parent + subcategory |
| Description | `description` | Full text — what it does, who it's for |

## Output Format

```json
{
  "category": "marketing",
  "scraped_at": "2026-04-17",
  "total_unique_workflows": 47,
  "subcategories": {
    "content-creation": {
      "total_from_api": 287,
      "workflows_collected": 18,
      "workflows": [ ... ]
    },
    "market-research": { ... },
    "social-media": { ... }
  }
}
```

## Storage

- Source of truth: `~/.hermes/workspace/flowkits/n8n_workflows_{category-slug}.json`
- Quick reference: `~/.hermes/workspace/flowkits/n8n_workflows_{category-slug}_index.md`
