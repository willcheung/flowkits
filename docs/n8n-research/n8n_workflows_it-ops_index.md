# n8n IT Ops Workflows Index

Scraped: 2026-04-20 | Total unique: 784 | Queries: 501

API total: 1,055 | Coverage: 74.3%

## Summary by Subcategory

| Subcategory | Workflows | Avg Views | Max Views |
|---|---|---|---|
| Engineering | 659 | 3,504 | 422,411 |
| DevOps | 107 | 1,037 | 21,003 |
| SecOps | 15 | 553 | 3,704 |
| Other | 3 | 1,512 | 1,747 |

## Engineering
(659 workflows)

### [Creating an API endpoint](https://n8n.io/workflows/1750-creating-an-api-endpoint)
- **ID:** 1750 | **Creator:** @jon-n8n ✓ | **Views:** 422,411 | **Nodes:** 0
- **Nodes:** 
- Task:
Create a simple API endpoint using the Webhook and Respond to Webhook nodes

Why:
You can prototype or replace a backend process with a single workflow

Main use cases:
Replace backend logic wit...

### [AI agent that can scrape webpages](https://n8n.io/workflows/2006-ai-agent-that-can-scrape-webpages)
- **ID:** 2006 | **Creator:** @eduard ✓ | **Views:** 211,623 | **Nodes:** 4
- **Nodes:** HTTP Request, AI Agent, OpenAI Chat Model +1 more
- ⚙️🛠️🚀🤖🦾

This template is a PoC of a ReAct AI Agent capable of fetching random pages (not only Wikipedia or Google search results).

On the top part there's a manual chat node connected to a LangCha...

### [Pulling data from services that n8n doesn’t have a pre-built integration for](https://n8n.io/workflows/1748-pulling-data-from-services-that-n8n-doesnt-have-a-pre-built)
- **ID:** 1748 | **Creator:** @jon-n8n ✓ | **Views:** 194,346 | **Nodes:** 1
- **Nodes:** HTTP Request
- You still can use the app in a workflow even if we don’t have a node for that or the existing operation for that. With the HTTP Request node, it is possible to call any API point and use the incoming...

### [Scrape and store data from multiple website pages](https://n8n.io/workflows/1073-scrape-and-store-data-from-multiple-website-pages)
- **ID:** 1073 | **Creator:** @mcolomer ✓ | **Views:** 80,004 | **Nodes:** 3
- **Nodes:** HTTP Request, MongoDB, uProc
- This workflow allows extracting data from multiple pages website.

The workflow:
1) Starts in a country list at https://www.theswiftcodes.com/browse-by-country/.
2) Loads every country page (https://w...

### [Chat with local LLMs using n8n and Ollama](https://n8n.io/workflows/2384-chat-with-local-llms-using-n8n-and-ollama)
- **ID:** 2384 | **Creator:** @mihailtd ✓ | **Views:** 77,672 | **Nodes:** 2
- **Nodes:** Basic LLM Chain, Ollama Chat Model
- Chat with local LLMs using n8n and Ollama
This n8n workflow allows you to seamlessly interact with your self-hosted Large Language Models (LLMs) through a user-friendly chat interface. By connecting t...

### [🎓 Learn JSON Basics with an Interactive Step-by-Step Tutorial for Beginners](https://n8n.io/workflows/5170-learn-json-basics-with-an-interactive-step-by-step-tutorial)
- **ID:** 5170 | **Creator:** @lucaspeyrin ✓ | **Views:** 74,178 | **Nodes:** 0
- **Nodes:** 
- How it works

This workflow is an interactive, hands-on tutorial designed to teach you the absolute basics of JSON (JavaScript Object Notation) and, more importantly, how to use it within n8n. It's pe...

### [Preparing data to be sent to a service](https://n8n.io/workflows/1751-preparing-data-to-be-sent-to-a-service)
- **ID:** 1751 | **Creator:** @jon-n8n ✓ | **Views:** 63,641 | **Nodes:** 2
- **Nodes:** Google Sheets, Customer Datastore (n8n training)
- Task:
Make sure that data is in the right format before injecting it into a database/spreadsheet/CRM/etc.

Why:
Spreadsheets and databases require the incoming data to have the same fields as the head...

### [Build an MCP Server with Google Calendar and Custom Functions](https://n8n.io/workflows/3514-build-an-mcp-server-with-google-calendar-and-custom-function)
- **ID:** 3514 | **Creator:** @solomon ✓ | **Views:** 49,155 | **Nodes:** 7
- **Nodes:** HTTP Request, DebugHelper, AI Agent +4 more
- Learn how to build an MCP Server and Client in n8n with official nodes.

&gt; ⚠ Requires n8n version 1.88.0 or higher.

In this example, we use Google Calendar and custom functions as two separate MCP...

### [Build your own N8N Workflows MCP Server](https://n8n.io/workflows/3770-build-your-own-n8n-workflows-mcp-server)
- **ID:** 3770 | **Creator:** @jimleuk ✓ | **Views:** 45,504 | **Nodes:** 6
- **Nodes:** Redis, AI Agent, OpenAI Chat Model +3 more
- This n8n template shows you how to create an MCP server out of your existing n8n workflows. With this, any MCP client connected can get more done with powerful end-to-end workflows rather than just si...

### [N8N for Beginners: Looping over Items](https://n8n.io/workflows/2896-n8n-for-beginners-looping-over-items)
- **ID:** 2896 | **Creator:** @dom | **Views:** 38,818 | **Nodes:** 1
- **Nodes:** Code
- N8N for Beginners: Looping Over Items

Description

This workflow is designed for n8n beginners to understand how n8n handles looping (iteration) over multiple items. It highlights two key behaviors:...

### [Generate SQL queries from schema only - AI-powered](https://n8n.io/workflows/2508-generate-sql-queries-from-schema-only-ai-powered)
- **ID:** 2508 | **Creator:** @yulia ✓ | **Views:** 38,321 | **Nodes:** 4
- **Nodes:** MySQL, AI Agent, OpenAI Chat Model +1 more
- This workflow is a modification of the previous template on how to create an SQL agent with LangChain and SQLite.

The key difference – the agent has access only to the database schema, not to the act...

### [Use an open-source LLM (via HuggingFace)](https://n8n.io/workflows/1980-use-an-open-source-llm-via-huggingface)
- **ID:** 1980 | **Creator:** @n8n-team ✓ | **Views:** 37,276 | **Nodes:** 2
- **Nodes:** Basic LLM Chain, Hugging Face Inference Model
- This workflow demonstrates how to connect an open-source model to a Basic LLM node.

The workflow is triggered when a new manual chat message appears. The message is then run through a Language Model...

### [🐋DeepSeek V3 Chat & R1 Reasoning Quick Start](https://n8n.io/workflows/2777-deepseek-v3-chat-and-r1-reasoning-quick-start)
- **ID:** 2777 | **Creator:** @joe ✓ | **Views:** 36,793 | **Nodes:** 6
- **Nodes:** HTTP Request, AI Agent, Basic LLM Chain +3 more
- This n8n workflow demonstrates multiple ways to harness DeepSeek's AI models in your automation pipeline! 🌟

Core Features

Multiple Integration Methods 🔌
Local deployment using Ollama for DeepSeek-R1...

### [Proxmox AI Agent with n8n and Generative AI Integration](https://n8n.io/workflows/2749-proxmox-ai-agent-with-n8n-and-generative-ai-integration)
- **ID:** 2749 | **Creator:** @amjid ✓ | **Views:** 32,346 | **Nodes:** 7
- **Nodes:** HTTP Request, Code, AI Agent +4 more
- Proxmox AI Agent with n8n and Generative AI Integration

This template automates IT operations on a Proxmox Virtual Environment (VE) using an AI-powered conversational agent built with n8n. By integra...

### [Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI](https://n8n.io/workflows/2440-building-rag-chatbot-for-movie-recommendations-with-qdrant-a)
- **ID:** 2440 | **Creator:** @mrscoopers ✓ | **Views:** 31,111 | **Nodes:** 10
- **Nodes:** GitHub, HTTP Request, AI Agent +7 more
- Create a recommendation tool without hallucinations based on RAG with the Qdrant Vector database. This example is based on movie recommendations on the IMDB-top1000 dataset. You can provide your wishe...

### [ChatGPT Automatic Code Review in Gitlab MR](https://n8n.io/workflows/2167-chatgpt-automatic-code-review-in-gitlab-mr)
- **ID:** 2167 | **Creator:** @assert | **Views:** 28,555 | **Nodes:** 4
- **Nodes:** HTTP Request, Code, Basic LLM Chain +1 more
- Who this template is for
This template is for every engineer who wants to automate their code reviews or just get a 2nd opinion on their PR.

How it works
This workflow will automatically review your...

### [🎓 Learn n8n Expressions with an Interactive Step-by-Step Tutorial for Beginners](https://n8n.io/workflows/5271-learn-n8n-expressions-with-an-interactive-step-by-step-tuto)
- **ID:** 5271 | **Creator:** @lucaspeyrin ✓ | **Views:** 27,902 | **Nodes:** 0
- **Nodes:** 
- How it works

This template is an interactive, step-by-step tutorial designed to teach you the most important skill in n8n: using expressions to access and manipulate data.

If you know what JSON is b...

### [Phishing Analysis - URLScan.io and VirusTotal](https://n8n.io/workflows/1992-phishing-analysis-urlscanio-and-virustotal)
- **ID:** 1992 | **Creator:** @n8n-team ✓ | **Views:** 26,877 | **Nodes:** 5
- **Nodes:** HTTP Request, Slack, Microsoft Outlook +2 more
- This n8n workflow automates the analysis of email messages received in a Microsoft Outlook inbox to identify indicators of compromise (IOCs), specifically suspicious URLs. It can be triggered manually...

### [API Schema Extractor](https://n8n.io/workflows/2658-api-schema-extractor)
- **ID:** 2658 | **Creator:** @polina-n8n ✓ | **Views:** 23,830 | **Nodes:** 11
- **Nodes:** Google Sheets, HTTP Request, Google Drive +8 more
- This workflow automates the process of discovering and extracting APIs from various services, followed by generating custom schemas. It works in three distinct stages: research, extraction, and schema...

### [WebSecScan: AI-Powered Website Security Auditor](https://n8n.io/workflows/3314-websecscan-ai-powered-website-security-auditor)
- **ID:** 3314 | **Creator:** @daledunlop | **Views:** 18,206 | **Nodes:** 5
- **Nodes:** HTTP Request, Gmail, Code +2 more
- WebSecScan: AI-Powered Website Security Auditor

This n8n workflow provides comprehensive website security analysis by leveraging OpenAI's models to detect vulnerabilities, configuration issues, and s...

### [🛠️ AI Prompt Maker](https://n8n.io/workflows/5289-ai-prompt-maker)
- **ID:** 5289 | **Creator:** @lucaspeyrin ✓ | **Views:** 17,337 | **Nodes:** 2
- **Nodes:** Basic LLM Chain, Google Gemini Chat Model
- How it works

This template provides a complete, ready-to-use web application for generating high-quality AI prompts. It features a user-friendly web form where you can describe your goal, and it leve...

### [Scrape any web page into structured JSON data with ScrapeNinja and AI](https://n8n.io/workflows/2812-scrape-any-web-page-into-structured-json-data-with-scrapenin)
- **ID:** 2812 | **Creator:** @scrapeninja ✓ | **Views:** 17,135 | **Nodes:** 2
- **Nodes:** Basic LLM Chain, Google Gemini Chat Model
- Disclaimer: This template only works on self-hosted for now, as it uses a community node.

Use Case
Web scrapers often break due to web page layout changes.
This workflow attempts to mitigate this pro...

### [AI Agent to chat with Supabase/PostgreSQL DB](https://n8n.io/workflows/2612-ai-agent-to-chat-with-supabase-postgresql-db)
- **ID:** 2612 | **Creator:** @lowcodingdev ✓ | **Views:** 16,571 | **Nodes:** 2
- **Nodes:** AI Agent, OpenAI Chat Model
- Video Guide

I prepared a detailed guide that showed the whole process of building a resume analyzer.

Who is this for?
This workflow is ideal for developers, data analysts, and business owners who wa...

### [Visualize your SQL Agent queries with OpenAI and Quickchart.io](https://n8n.io/workflows/2559-visualize-your-sql-agent-queries-with-openai-and-quickcharti)
- **ID:** 2559 | **Creator:** @agentstudio ✓ | **Views:** 14,128 | **Nodes:** 6
- **Nodes:** HTTP Request, AI Agent, OpenAI Chat Model +3 more
- Overview  
This workflow aims to provide data visualization capabilities to a native SQL Agent.  
Together, they can help foster data analysis and data visualization within a team.  
It uses the nativ...

### [SSL Expiry Alert with SSL-Checker.io](https://n8n.io/workflows/2694-ssl-expiry-alert-with-ssl-checkerio)
- **ID:** 2694 | **Creator:** @vishalquantana ✓ | **Views:** 14,056 | **Nodes:** 3
- **Nodes:** Google Sheets, HTTP Request, Gmail
- Use Case

Managing SSL certificates manually can be time-consuming and error-prone, often leading to unexpected downtime or security risks due to expired certificates.

What This Workflow Does

This...

### [Import CSV into MySQL](https://n8n.io/workflows/1839-import-csv-into-mysql)
- **ID:** 1839 | **Creator:** @eduard ✓ | **Views:** 13,484 | **Nodes:** 1
- **Nodes:** MySQL
- This workflow demonstrates how CSV file can be automatically imported into existing MySQL database.



Before running the workflow please make sure you have a file on the server:
/home/node/.n8n/conce...

### [Insert a document in MongoDB](https://n8n.io/workflows/503-insert-a-document-in-mongodb)
- **ID:** 503 | **Creator:** @sm-amudhan ✓ | **Views:** 13,145 | **Nodes:** 1
- **Nodes:** MongoDB
- Companion workflow for MongoDB node docs

### [Scalable Multi-Agent Chat Using @mentions](https://n8n.io/workflows/3473-scalable-multi-agent-chat-using-mentions)
- **ID:** 3473 | **Creator:** @jondoran | **Views:** 12,969 | **Nodes:** 4
- **Nodes:** Code, AI Agent, Simple Memory +1 more
- Summary

Engage multiple, uniquely configured AI agents (using different models via OpenRouter) in a single conversation. Trigger specific agents with @mentions or let them all respond. Easily scalabl...

### [Insert Excel data to Postgres](https://n8n.io/workflows/1-insert-excel-data-to-postgres)
- **ID:** 1 | **Creator:** @jan ✓ | **Views:** 11,991 | **Nodes:** 1
- **Nodes:** Postgres
- Read XLS from file
Convert it to JSON
Insert it in Postgres

### [🔐🦙Private & Local Ollama Self-Hosted + Dynamic LLM Router](https://n8n.io/workflows/3139-private-and-local-ollama-self-hosted-dynamic-llm-router)
- **ID:** 3139 | **Creator:** @joe ✓ | **Views:** 11,663 | **Nodes:** 3
- **Nodes:** AI Agent, Ollama Chat Model, Simple Memory
- Who is this for?
This workflow template is designed for AI enthusiasts, developers, and privacy-conscious users who want to leverage the power of local large language models (LLMs) without sending dat...

### [Use any LangChain module in n8n (with the LangChain code node)](https://n8n.io/workflows/2082-use-any-langchain-module-in-n8n-with-the-langchain-code-node)
- **ID:** 2082 | **Creator:** @davidn8n ✓ | **Views:** 10,878 | **Nodes:** 2
- **Nodes:** LangChain Code, OpenAI Chat Model
- LangChain is a framework for building AI functionality that users large language models. By leveraging the functionality of LangChain, you can write even more powerful workflows.

This workflow shows...

### [Save your workflows into a GitHub repository](https://n8n.io/workflows/817-save-your-workflows-into-a-github-repository)
- **ID:** 817 | **Creator:** @hikerspath | **Views:** 10,459 | **Nodes:** 2
- **Nodes:** GitHub, HTTP Request
- Basics

Provides a mechanism to save all your workflows into a github repository and path (of your choosing).  These can then be shared through your entire org and used to track changes (if you make a...

### [Send Email if server has upgradable packages](https://n8n.io/workflows/2925-send-email-if-server-has-upgradable-packages)
- **ID:** 2925 | **Creator:** @hostinger ✓ | **Views:** 9,813 | **Nodes:** 2
- **Nodes:** Send Email, Code
- This workflow automates the routine check for upgradable packages on your Ubuntu server, ensuring you stay updated with the latest software patches and security improvements. By running a daily script...

### [Monitor Data Breaches in Real-time with Have I Been Pwned](https://n8n.io/workflows/3205-monitor-data-breaches-in-real-time-with-have-i-been-pwned)
- **ID:** 3205 | **Creator:** @xqus ✓ | **Views:** 9,118 | **Nodes:** 1
- **Nodes:** HTTP Request
- Who is this for?
Security professionals
Developers
Individuals interested in data breach awareness

Use Case
Automated monitoring for new breaches
Proactive identity protection
Demonstration of simpl...

### [🦅 Get a bird's-eye view of your n8n instance with the Workflow Dashboard!](https://n8n.io/workflows/2269-get-a-birds-eye-view-of-your-n8n-instance-with-the-workflow)
- **ID:** 2269 | **Creator:** @eduard ✓ | **Views:** 8,839 | **Nodes:** 2
- **Nodes:** Code, HTML
- ⚡ UPDATE on May 2025 – added section with all n8n instance webhooks

Using n8n a lot?

Soar above the limitations of the default n8n dashboard! This template gives you an overview of your workflows, n...

### [Merge multiple runs into one](https://n8n.io/workflows/1814-merge-multiple-runs-into-one)
- **ID:** 1814 | **Creator:** @mutedjam ✓ | **Views:** 8,839 | **Nodes:** 2
- **Nodes:** Customer Datastore (n8n training), Code
- This is a workflow that might come handy after using loops. They usually leave you with items spread across different "runs". The Code node in this example workflow merges them into a single run, so y...

### [URL and IP lookups through Greynoise and VirusTotal](https://n8n.io/workflows/1971-url-and-ip-lookups-through-greynoise-and-virustotal)
- **ID:** 1971 | **Creator:** @n8n-team ✓ | **Views:** 8,572 | **Nodes:** 4
- **Nodes:** HTTP Request, Slack, Gmail +1 more
- This n8n workflow serves as a powerful cybersecurity and threat intelligence tool to look up URLs or IP addresses through industry standard threat intelligence vendors. It starts with either a form su...

### [RAG:Context-Aware Chunking | Google Drive to Pinecone via OpenRouter & Gemini](https://n8n.io/workflows/2871-ragcontext-aware-chunking-google-drive-to-pinecone-via-open)
- **ID:** 2871 | **Creator:** @ailistmaster ✓ | **Views:** 8,468 | **Nodes:** 7
- **Nodes:** Google Drive, Code, AI Agent +4 more
- Workflow based on the following article.
https://www.anthropic.com/news/contextual-retrieval

This n8n automation is designed to extract, process, and store content from documents into a Pinecone vect...

### [Pattern for Parallel Sub-Workflow Execution Followed by Wait-For-All Loop](https://n8n.io/workflows/2536-pattern-for-parallel-sub-workflow-execution-followed-by-wait)
- **ID:** 2536 | **Creator:** @hubschrauber ✓ | **Views:** 8,144 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- What this workflow does
This (set of) workflow(s) shows how to start multiple sub-workflows, asynchronously, in parallel, and then wait for all of them to complete.  Normally sub-workflows would need...

### [Sync Google Sheets data with MySQL](https://n8n.io/workflows/1964-sync-google-sheets-data-with-mysql)
- **ID:** 1964 | **Creator:** @n8n-team ✓ | **Views:** 7,760 | **Nodes:** 2
- **Nodes:** Google Sheets, MySQL
- This workflow performs several data integration and synchronization tasks between Google Sheets and a MySQL database.

Here is a step-by-step description of what this workflow does:

Manual Trigger: T...

### [Split Test Different Agent Prompts with Supabase and OpenAI](https://n8n.io/workflows/2992-split-test-different-agent-prompts-with-supabase-and-openai)
- **ID:** 2992 | **Creator:** @chriscarr ✓ | **Views:** 7,697 | **Nodes:** 4
- **Nodes:** Supabase, AI Agent, OpenAI Chat Model +1 more
- Split Test Agent Prompts with Supabase and OpenAI
Use Case
Oftentimes, it's useful to test different settings for a large language model in production against various metrics. Split testing is a good...

### [Generating Image Embeddings via Textual Summarisation](https://n8n.io/workflows/2344-generating-image-embeddings-via-textual-summarisation)
- **ID:** 2344 | **Creator:** @jimleuk ✓ | **Views:** 7,286 | **Nodes:** 7
- **Nodes:** Edit Image, Google Drive, Embeddings OpenAI +4 more
- This n8n template demonstrates an approach to image embeddings for purpose of building a quick image contextual search. Use-cases could for a personal photo library, product recommendations or searchi...

### [Turn on a light to a specific color on any update in GitHub repository](https://n8n.io/workflows/1856-turn-on-a-light-to-a-specific-color-on-any-update-in-github)
- **ID:** 1856 | **Creator:** @n8n-team ✓ | **Views:** 6,985 | **Nodes:** 1
- **Nodes:** Home Assistant
- This workflow turns a light red when an update is made to a GitHub repository. By default, updates include pull requests, issues, pushes just to name a few.

Prerequisites

GitHub credentials.
Home As...

### [Create, update, and get a document in Google Cloud Firestore](https://n8n.io/workflows/839-create-update-and-get-a-document-in-google-cloud-firestore)
- **ID:** 839 | **Creator:** @harshil1712 ✓ | **Views:** 6,934 | **Nodes:** 1
- **Nodes:** Google Cloud Firestore
- This example workflow allows you to create, update, and get a document in Google Cloud Firestore. 

The workflow uses the Set node to set the data, however, you might receive data from a different s...

### [Analyze & Sort Suspicious Email Contents with ChatGPT](https://n8n.io/workflows/2666-analyze-and-sort-suspicious-email-contents-with-chatgpt)
- **ID:** 2666 | **Creator:** @djangelic ✓ | **Views:** 6,716 | **Nodes:** 4
- **Nodes:** HTTP Request, Jira Software, Code +1 more
- Analyze & Sort Suspicious Email Contents with ChatGPT and Jira

Who is this for?
This workflow is tailored for IT security teams, managed service providers (MSPs), and organizations aiming to streamli...

### [Automate Web Interactions with Claude 3.5 Haiku and Airtop Browser Agent](https://n8n.io/workflows/3592-automate-web-interactions-with-claude-35-haiku-and-airtop-br)
- **ID:** 3592 | **Creator:** @cesar-at-airtop ✓ | **Views:** 6,534 | **Nodes:** 6
- **Nodes:** Slack, AI Agent, Anthropic Chat Model +3 more
- About this AI Agent

This workflow is designed to automate web interactions by simulating a human user, using a combination of the Agent node and AI tools powered by Airtop.

How does this workflow wo...

### [Anthropic AI Agent: Claude Sonnet 4 and Opus 4 with Think and Web Search tool](https://n8n.io/workflows/4399-anthropic-ai-agent-claude-sonnet-4-and-opus-4-with-think-and)
- **ID:** 4399 | **Creator:** @n3witalia ✓ | **Views:** 6,524 | **Nodes:** 6
- **Nodes:** AI Agent, Anthropic Chat Model, Simple Memory +3 more
- This workflow dynamically chooses between two new powerful Anthropic models — Claude Opus 4 and Claude Sonnet 4 — to handle user queries, based on their complexity and nature, maintaining scalability...

### [Build Your Own Image Search Using AI Object Detection, CDN and ElasticSearch](https://n8n.io/workflows/2331-build-your-own-image-search-using-ai-object-detection-cdn-an)
- **ID:** 2331 | **Creator:** @jimleuk ✓ | **Views:** 6,369 | **Nodes:** 3
- **Nodes:** Edit Image, HTTP Request, Elasticsearch
- This n8n workflow demonstrates how to automate indexing of images to build a object-based image search.

By utilising a Detr-Resnet-50 Object Classification model, we can identify objects within an im...

### [Build an MCP Server with Airtable](https://n8n.io/workflows/3879-build-an-mcp-server-with-airtable)
- **ID:** 3879 | **Creator:** @aitoralonso ✓ | **Views:** 6,123 | **Nodes:** 4
- **Nodes:** AI Agent, OpenAI Chat Model, Simple Memory +1 more
- Who is this for?
This template is designed for anyone who wants to integrate MCP with their AI Agents using Airtable. Whether you're a developer, a data analyst, or an automation enthusiast, if you're...

### [Synchronize your Google Sheets with Postgres](https://n8n.io/workflows/2081-synchronize-your-google-sheets-with-postgres)
- **ID:** 2081 | **Creator:** @bwiertz ✓ | **Views:** 6,087 | **Nodes:** 2
- **Nodes:** Google Sheets, Postgres
- Sync your Google Sheets Data with your Postgres database table, requiring minimal adjustments. Follow these steps:

Retrieve Data: Pull data from Google Sheets and PostgreSQL.
Compare Datasets: Identi...

### [Rate limiting and waiting for external events](https://n8n.io/workflows/1749-rate-limiting-and-waiting-for-external-events)
- **ID:** 1749 | **Creator:** @jon-n8n ✓ | **Views:** 5,969 | **Nodes:** 2
- **Nodes:** Customer Datastore (n8n training), Customer Messenger (n8n training)
- Task:
Control your data flow with rate limits and external cues

Main use cases:
Control the rate of items flow into one or more services in your workflow
Wait for external events to occur before cont...

### [Monitor Multiple Github Repos via Webhook](https://n8n.io/workflows/2435-monitor-multiple-github-repos-via-webhook)
- **ID:** 2435 | **Creator:** @jay ✓ | **Views:** 5,876 | **Nodes:** 3
- **Nodes:** HTTP Request, Slack, Telegram
- What this workflow does
This workflow allows you to monitor multiple Github repos simultaneously without polling due to use of Webhooks. It programmatically allows for adding and deleting of repos to...

### [Analyze Email Headers for IP Reputation and Spoofing Detection - Gmail](https://n8n.io/workflows/2677-analyze-email-headers-for-ip-reputation-and-spoofing-detecti)
- **ID:** 2677 | **Creator:** @djangelic ✓ | **Views:** 5,700 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- Analyze Emails for Security Insights

Who is this for?

This workflow is ideal for IT professionals, security analysts, and organizations looking to enhance their email security practices. It is parti...

### [Merge data for multiple executions](https://n8n.io/workflows/1160-merge-data-for-multiple-executions)
- **ID:** 1160 | **Creator:** @harshil1712 ✓ | **Views:** 5,679 | **Nodes:** 0
- **Nodes:** 
- This workflow demonstrates how to merge data for different executions.



The Merge Data Function node fetches the data from different executions of the RSS Feed Read node and merges them under a sing...

### [Build your own PostgreSQL MCP server](https://n8n.io/workflows/3631-build-your-own-postgresql-mcp-server)
- **ID:** 3631 | **Creator:** @jimleuk ✓ | **Views:** 5,672 | **Nodes:** 2
- **Nodes:** Postgres, Call n8n Workflow Tool
- This n8n demonstrates how to build a simple PostgreSQL MCP server to manage your PostgreSQL database such as HR, Payroll, Sale, Inventory and More!

This MCP example is based off an official MCP refer...

### [Backup all n8n workflows to Google Drive every 4 hours](https://n8n.io/workflows/2886-backup-all-n8n-workflows-to-google-drive-every-4-hours)
- **ID:** 2886 | **Creator:** @imperolq ✓ | **Views:** 5,511 | **Nodes:** 1
- **Nodes:** Google Drive
- This workflow takes off the task of backing up workflows regularly on Github and uses Google Drive as the main tool to host these. 

This can be a good way to keep track of your workflows so that you...

### [AI Orchestrator: dynamically Selects Models Based on Input Type](https://n8n.io/workflows/7004-ai-orchestrator-dynamically-selects-models-based-on-input-ty)
- **ID:** 7004 | **Creator:** @n3witalia ✓ | **Views:** 5,438 | **Nodes:** 9
- **Nodes:** AI Agent, Basic LLM Chain, Anthropic Chat Model +6 more
- This workflow is designed to intelligently route user queries to the most suitable large language model (LLM) based on the type of request received in a chat environment. It uses structured classifica...

### [Weekly Shodan Query - Report Accidents](https://n8n.io/workflows/1977-weekly-shodan-query-report-accidents)
- **ID:** 1977 | **Creator:** @n8n-team ✓ | **Views:** 5,359 | **Nodes:** 3
- **Nodes:** HTTP Request, TheHive, HTML
- This n8n workflow, which runs every Monday at 5:00 AM, initiates a comprehensive process to monitor and analyze network security by scrutinizing IP addresses and their associated ports. It begins by f...

### [🗲 Creating a Secure Webhook - MUST HAVE](https://n8n.io/workflows/5174-creating-a-secure-webhook-must-have)
- **ID:** 5174 | **Creator:** @lucaspeyrin ✓ | **Views:** 5,267 | **Nodes:** 1
- **Nodes:** HTTP Request
- How it works

This workflow demonstrates a fundamental pattern for securing a webhook by requiring an API key. It acts as a gatekeeper, checking for a valid key in the request header before allowing t...

### [Restore backed up workflows from GitHub to n8n](https://n8n.io/workflows/2289-restore-backed-up-workflows-from-github-to-n8n)
- **ID:** 2289 | **Creator:** @agentstudio ✓ | **Views:** 4,987 | **Nodes:** 1
- **Nodes:** GitHub
- Restore backed up workflows from GitHub to your n8n workspace.
This workflow was inspired by this one that lets you back up your n8n workflows to GitHub.
It will let you restore your backed up workflo...

### [Push and update files in GitHub](https://n8n.io/workflows/1942-push-and-update-files-in-github)
- **ID:** 1942 | **Creator:** @n8n-team ✓ | **Views:** 4,976 | **Nodes:** 2
- **Nodes:** GitHub, Code
- This workflow performs various Git operations. It starts with a manual trigger, sets the local repository path, decodes a file and then updates a file's content, adds, commits, and pushes changes to a...

### [Backup your workflows to GitHub -- in (subfolders)](https://n8n.io/workflows/2868-backup-your-workflows-to-github-in-subfolders)
- **ID:** 2868 | **Creator:** @islamnazmi ✓ | **Views:** 4,897 | **Nodes:** 3
- **Nodes:** GitHub, HTTP Request, Code
- Based on Jonathan & Solomon work.

&gt; The only addition I've made is a Set node. This node organizes workflows into subfolders within the GitHub repository based on their respective tags.

How it wo...

### [Filtering and branching data](https://n8n.io/workflows/1746-filtering-and-branching-data)
- **ID:** 1746 | **Creator:** @jon-n8n ✓ | **Views:** 4,817 | **Nodes:** 1
- **Nodes:** Customer Datastore (n8n training)
- Task:
Conditional filtering and branching items

Why:
Filtering and branching data based on conditions allows you to build complex workflows that work with more than one data flow scenario

Main use c...

### [Visual Regression Testing with Apify and AI Vision Model](https://n8n.io/workflows/2419-visual-regression-testing-with-apify-and-ai-vision-model)
- **ID:** 2419 | **Creator:** @jimleuk ✓ | **Views:** 4,738 | **Nodes:** 7
- **Nodes:** Google Sheets, HTTP Request, Google Drive +4 more
- This n8n workflow is a proof-of-concept template exploring how we might work with multimodal LLMs and their multi-image analysis capabilities. In this demo, we compare 2 screenshots of a webpage taken...

### [Save your workflows into a Gitlab repository](https://n8n.io/workflows/2385-save-your-workflows-into-a-gitlab-repository)
- **ID:** 2385 | **Creator:** @juliendelrio ✓ | **Views:** 4,702 | **Nodes:** 2
- **Nodes:** GitLab, Code
- This template is inspired by Save your workflows into a GitHub repository by hikerspath and Back Up Your n8n Workflows To Github by jon-n8n.

Basic

Retrieve all workflows from an n8n instance and sav...

### [Automated PR Code Reviews with GitHub, GPT-4, and Google Sheets Best Practices](https://n8n.io/workflows/3804-automated-pr-code-reviews-with-github-gpt-4-and-google-sheet)
- **ID:** 3804 | **Creator:** @jiheneme | **Views:** 4,545 | **Nodes:** 5
- **Nodes:** GitHub, HTTP Request, Code +2 more
- AI-Agent Code Review for GitHub Pull Requests 

Description:

This n8n workflow automates the process of reviewing code changes in GitHub pull requests using an OpenAI-powered agent. 

It connects you...

### [API queries data from GraphQL](https://n8n.io/workflows/216-api-queries-data-from-graphql)
- **ID:** 216 | **Creator:** @jan ✓ | **Views:** 4,485 | **Nodes:** 1
- **Nodes:** GraphQL
- Simpe API which queries the received country code via GraphQL and returns it.

Example URL: https://n8n.exampl.ecom/webhook/1/webhook/webhook?code=DE

Receives country code from an incoming HTTP Req...

### [GitLab Merge Request Review & Risk Analysis with Claude/GPT AI](https://n8n.io/workflows/3997-gitlab-merge-request-review-and-risk-analysis-with-claude-gp)
- **ID:** 3997 | **Creator:** @vishalquantana ✓ | **Views:** 4,457 | **Nodes:** 7
- **Nodes:** HTTP Request, Gmail, Code +4 more
- Trigger

The workflow runs when a GitLab Merge Request (MR) is created or updated.

Extract & Analyze

It retrieves the code diff and sends it to Claude AI or GPT-4o for risk assessment and issue dete...

### [Web Site Scraper for LLMs with Airtop](https://n8n.io/workflows/4252-web-site-scraper-for-llms-with-airtop)
- **ID:** 4252 | **Creator:** @cesar-at-airtop ✓ | **Views:** 4,403 | **Nodes:** 4
- **Nodes:** Google Sheets, Google Docs, Code +1 more
- Recursive Web Scraping 

Use Case  
Automating web scraping with recursive depth is ideal for collecting content across multiple linked pages—perfect for content aggregation, lead generation, or resea...

### [Build Custom Workflows Automatically with GPT-4o, RAG, and Web Search](https://n8n.io/workflows/5024-build-custom-workflows-automatically-with-gpt-4o-rag-and-web)
- **ID:** 5024 | **Creator:** @agents-by-franz ✓ | **Views:** 4,344 | **Nodes:** 10
- **Nodes:** HTTP Request, Code, AI Agent +7 more
- 🚀 What the “Agent Builder” template does

Need to turn a one-line chat request into a fully-wired n8n workflow template—complete with AI agents, RAG, and web-search super-powers—without lifting a fing...

### [Meraki Packet Loss and Latency Alerts to Microsoft Teams](https://n8n.io/workflows/2054-meraki-packet-loss-and-latency-alerts-to-microsoft-teams)
- **ID:** 2054 | **Creator:** @sniped-you-fool | **Views:** 4,324 | **Nodes:** 4
- **Nodes:** HTTP Request, Redis, Microsoft Teams +1 more
- This Template gives the ability to monitor all uplinks for your Meraki Dashboard and then alert your team in a method you prefer. This example is a Teams notification to our Dispatch Channel



Setup...

### [Analyze CrowdStrike Detections - Search for IOCs in VirusTotal - Create a Ticket in Jira, and Post a Message in Slack](https://n8n.io/workflows/1973-analyze-crowdstrike-detections-search-for-iocs-in-virustot)
- **ID:** 1973 | **Creator:** @n8n-team ✓ | **Views:** 4,201 | **Nodes:** 3
- **Nodes:** HTTP Request, Slack, Jira Software
- This n8n workflow automates the handling of security detections from CrowdStrike, streamlining incident response and notification processes. The workflow is triggered daily at midnight by the Schedule...

### [Avoid rate limiting by batching HTTP requests](https://n8n.io/workflows/1243-avoid-rate-limiting-by-batching-http-requests)
- **ID:** 1243 | **Creator:** @harshil1712 ✓ | **Views:** 4,069 | **Nodes:** 2
- **Nodes:** HTTP Request, Customer Datastore (n8n training)
- This workflow demonstrates the use of the Split In Batches node and the Wait node to avoid API rate limits.

Customer Datastore node: The workflow fetches data from the Customer Datastore node. Based...

### [🚨 Report n8n workflow errors to Telegram](https://n8n.io/workflows/2159-report-n8n-workflow-errors-to-telegram)
- **ID:** 2159 | **Creator:** @mutasem ✓ | **Views:** 4,043 | **Nodes:** 1
- **Nodes:** Telegram
- Use case
Error workflows are an important part of running workflows in production. Make sure to set them up for all your important workflows. The message links directly to the execution.

How to setup...

### [Get details of a GitLab repository](https://n8n.io/workflows/465-get-details-of-a-gitlab-repository)
- **ID:** 465 | **Creator:** @shraddha ✓ | **Views:** 3,985 | **Nodes:** 1
- **Nodes:** GitLab

### [Intelligent AI Digest for Security, Privacy, and Compliance Feeds](https://n8n.io/workflows/4678-intelligent-ai-digest-for-security-privacy-and-compliance-fe)
- **ID:** 4678 | **Creator:** @niranjan ✓ | **Views:** 3,892 | **Nodes:** 4
- **Nodes:** Gmail, Code, AI Agent +1 more
- How it works
This workflow acts like your own personal AI assistant, automatically fetching and summarizing the most relevant Security, Privacy, and Compliance news from curated RSS feeds. It processe...

### [Build an MCP Server with Google Calendar](https://n8n.io/workflows/3569-build-an-mcp-server-with-google-calendar)
- **ID:** 3569 | **Creator:** @sun-guannan | **Views:** 3,823 | **Nodes:** 4
- **Nodes:** AI Agent, OpenAI Chat Model, Simple Memory +1 more
- Who is this for?
This template is designed for anyone who wants to integrate MCP with their AI Agents. Whether you're a developer, a data analyst, or an automation enthusiast, if you're looking to lev...

### [Build an endpoint to perform CRUD operations with multiple HTTP methods](https://n8n.io/workflows/2490-build-an-endpoint-to-perform-crud-operations-with-multiple-h)
- **ID:** 2490 | **Creator:** @gandreini | **Views:** 3,764 | **Nodes:** 1
- **Nodes:** Airtable
- This n8n workflow template allows you to create a CRUD endpoint that performs the following actions:

Create a new record
Get a record
Get many records
Update a record
Delete a record

This template i...

### [Automated daily workflow backup to GitHub](https://n8n.io/workflows/4064-automated-daily-workflow-backup-to-github)
- **ID:** 4064 | **Creator:** @hugop | **Views:** 3,755 | **Nodes:** 1
- **Nodes:** GitHub
- This workflow provides a robust solution for automatically backing up all your n8n workflows to a designated GitHub repository on a daily basis. By leveraging the n8n API and GitHub API, it ensures yo...

### [Import CSV files from Filesystem into Postgres](https://n8n.io/workflows/2926-import-csv-files-from-filesystem-into-postgres)
- **ID:** 2926 | **Creator:** @rpshu1 | **Views:** 3,729 | **Nodes:** 1
- **Nodes:** Postgres
- -- Disclaimer: This template is mainly made for self-hosted users who can reach CSV files in their file system. For Cloud users, just replace the first few nodes with your file system of choice, like...

### [Low-code API for Flutterflow apps](https://n8n.io/workflows/2274-low-code-api-for-flutterflow-apps)
- **ID:** 2274 | **Creator:** @matheusweck | **Views:** 3,724 | **Nodes:** 1
- **Nodes:** Customer Datastore (n8n training)
- Flow Start: The flow starts upon receiving an HTTP GET call.
Webhook: Receives the HTTP GET call and triggers the flow.
Database: Connects to the database (Customer Datastore) to retrieve all necessar...

### [Dynamic AI Model Router for Query Optimization with OpenRouter](https://n8n.io/workflows/4237-dynamic-ai-model-router-for-query-optimization-with-openrout)
- **ID:** 4237 | **Creator:** @n3witalia ✓ | **Views:** 3,671 | **Nodes:** 5
- **Nodes:** AI Agent, OpenAI Chat Model, Auto-fixing Output Parser +2 more
- The Agent Decisioner is a dynamic, AI-powered routing system that automatically selects the most appropriate large language model (LLM) to respond to a user's query based on the query’s content and pu...

### [Natural Language Database Queries with Dual-Agent AI & PostgreSQL Integration](https://n8n.io/workflows/5012-natural-language-database-queries-with-dual-agent-ai-and-pos)
- **ID:** 5012 | **Creator:** @diagopl ✓ | **Views:** 3,658 | **Nodes:** 8
- **Nodes:** Postgres, Telegram, AI Agent +5 more
- AI Database Assistant with Smart Query's & PostgreSQL Integration

Description:

🚀 Transform Your Database into an Intelligent AI Assistant

This workflow creates a smart database assistant that safe...

### [Load data into spreadsheet or database](https://n8n.io/workflows/980-load-data-into-spreadsheet-or-database)
- **ID:** 980 | **Creator:** @maxt ✓ | **Views:** 3,615 | **Nodes:** 0
- **Nodes:** 
- This workflow is a generic example of how to load data from your workflow into a destination that stores tabular data. For example, a Google Sheets or Airtable sheet, a .CSV file, or any relational da...

### [🚀 Local Multi-LLM Testing & Performance Tracker](https://n8n.io/workflows/2442-local-multi-llm-testing-and-performance-tracker)
- **ID:** 2442 | **Creator:** @davidmoneil | **Views:** 3,614 | **Nodes:** 5
- **Nodes:** Google Sheets, HTTP Request, Code +2 more
- 🚀 Local Multi-LLM Testing & Performance Tracker

This workflow is perfect for developers, researchers, and data scientists benchmarking multiple LLMs with LM Studio. It dynamically fetches active mode...

### [Automated End-to-End Fine-Tuning of OpenAI Models with Google Drive Integration](https://n8n.io/workflows/2781-automated-end-to-end-fine-tuning-of-openai-models-with-googl)
- **ID:** 2781 | **Creator:** @n3witalia ✓ | **Views:** 3,590 | **Nodes:** 5
- **Nodes:** HTTP Request, Google Drive, AI Agent +2 more
- 1. How it Works  
This n8n workflow automates fine-tuning OpenAI models through these key steps:  
Manual Trigger**:  
  Starts with the "When clicking ‘Test workflow’" event to initiate the process....

### [Webhook returning XML](https://n8n.io/workflows/119-webhook-returning-xml)
- **ID:** 119 | **Creator:** @jan ✓ | **Views:** 3,553 | **Nodes:** 0
- **Nodes:** 
- Receives data from an incoming HTTP Request (set up to use respond to webhook node)
Create dummy data
Convert JSON to XML which gets returned 
Respond to Webhook which returns the data and the conte...

### [Make OpenAI Citation for File Retrieval RAG](https://n8n.io/workflows/2693-make-openai-citation-for-file-retrieval-rag)
- **ID:** 2693 | **Creator:** @frkr ✓ | **Views:** 3,456 | **Nodes:** 4
- **Nodes:** HTTP Request, Code, Simple Memory +1 more
- Make OpenAI Citation for File Retrieval RAG

Use case

In this example, we will ensure that all texts from the OpenAI assistant search for citations and sources in the vector store files. We can also...

### [Receive messages from a topic via Kafka and send an SMS](https://n8n.io/workflows/814-receive-messages-from-a-topic-via-kafka-and-send-an-sms)
- **ID:** 814 | **Creator:** @harshil1712 ✓ | **Views:** 3,304 | **Nodes:** 1
- **Nodes:** Vonage

### [Receive updates for GitLab events](https://n8n.io/workflows/528-receive-updates-for-gitlab-events)
- **ID:** 528 | **Creator:** @sm-amudhan ✓ | **Views:** 3,269 | **Nodes:** 0
- **Nodes:** 
- Companion workflow for GitLab Trigger docs

### [itemMatching() usage example](https://n8n.io/workflows/1966-itemmatching-usage-example)
- **ID:** 1966 | **Creator:** @n8n-team ✓ | **Views:** 3,256 | **Nodes:** 2
- **Nodes:** Customer Datastore (n8n training), Code
- This workflow provides a simple example of how to use itemMatching(itemIndex: Number) in the Code node to retrieve linked items from earlier in the workflow.

### [Receive messages for a MQTT queue](https://n8n.io/workflows/657-receive-messages-for-a-mqtt-queue)
- **ID:** 657 | **Creator:** @harshil1712 ✓ | **Views:** 3,247 | **Nodes:** 0
- **Nodes:** 

### [Vector Database as a Big Data Analysis Tool for AI Agents [1/3 anomaly][1/2 KNN]](https://n8n.io/workflows/2654-vector-database-as-a-big-data-analysis-tool-for-ai-agents-1)
- **ID:** 2654 | **Creator:** @mrscoopers ✓ | **Views:** 3,240 | **Nodes:** 3
- **Nodes:** HTTP Request, Google Cloud Storage, Code
- Vector Database as a Big Data Analysis Tool for AI Agents

Workflows from the webinar "Build production-ready AI Agents with Qdrant and n8n".

This series of workflows shows how to build big data anal...

### [Docker Registry Cleanup Workflow](https://n8n.io/workflows/2835-docker-registry-cleanup-workflow)
- **ID:** 2835 | **Creator:** @victorious | **Views:** 3,221 | **Nodes:** 3
- **Nodes:** Send Email, HTTP Request, Code
- Docker Registry Cleanup Template

This template is designed to automatically clean up old image tags in the Docker registry and perform garbage collection.

Features
List all images in the registry
Pr...

### [Count the items returned by a node](https://n8n.io/workflows/1913-count-the-items-returned-by-a-node)
- **ID:** 1913 | **Creator:** @mutedjam ✓ | **Views:** 3,203 | **Nodes:** 1
- **Nodes:** Customer Datastore (n8n training)
- This workflow provides a simple approach to counting the items returned by a node.

It uses a Set node with the Execute Once option:



The expression uses $input.all() (documented here) to fetch all...

### [🛠️ Process AI Output to Structured JSON with Robust JSON Parser](https://n8n.io/workflows/5146-process-ai-output-to-structured-json-with-robust-json-parse)
- **ID:** 5146 | **Creator:** @lucaspeyrin ✓ | **Views:** 3,170 | **Nodes:** 1
- **Nodes:** Code
- How it works

This workflow is a robust and forgiving JSON parser designed to handle malformed or "dirty" JSON strings often returned by AI models or scraped from web pages. It takes a text string as...

### [Automate NPM Package Installation and Updates for Self-Hosted Environments](https://n8n.io/workflows/3293-automate-npm-package-installation-and-updates-for-self-hoste)
- **ID:** 3293 | **Creator:** @joachimbrindeau | **Views:** 3,154 | **Nodes:** 0
- **Nodes:** 
- Are you looking to install external libraries for your self-hosted N8N instance? This automated workflow makes adding npm packages to your N8N environment quick and effortless.



Beware, this workflo...

### [Evaluate tool usage accuracy in multi-agent AI workflows using Evaluation nodes](https://n8n.io/workflows/5523-evaluate-tool-usage-accuracy-in-multi-agent-ai-workflows-usi)
- **ID:** 5523 | **Creator:** @djangelic ✓ | **Views:** 3,134 | **Nodes:** 7
- **Nodes:** AI Agent, Embeddings OpenAI, Calculator +4 more
- Who's it for
This workflow is ideal for AI developers running multi-agent systems in n8n who need to quantitatively evaluate tool usage behavior. If you're building autonomous agents and want to verif...

### [AI Prompt Generator Workflow](https://n8n.io/workflows/5045-ai-prompt-generator-workflow)
- **ID:** 5045 | **Creator:** @anuragmerndev | **Views:** 3,120 | **Nodes:** 4
- **Nodes:** Basic LLM Chain, Auto-fixing Output Parser, Structured Output Parser +1 more
- 🧠 AI Prompt Generator Workflow – n8n Documentation

Who is this for?

This workflow is for AI builders, prompt engineers, developers, marketers, and no-code creators who want to convert rough user inp...

### [Execute multiple Command Lines based on Text File Inputs](https://n8n.io/workflows/913-execute-multiple-command-lines-based-on-text-file-inputs)
- **ID:** 913 | **Creator:** @tephlon ✓ | **Views:** 3,065 | **Nodes:** 0
- **Nodes:** 
- This workflow takes a text file as input. It pulls the information from the text file and used it as a parameter to execute a command for each text line.

This workflow references a file /home/n8n/fil...

### [Conversing with Data: Transforming Text into SQL Queries and Visual Curves](https://n8n.io/workflows/3497-conversing-with-data-transforming-text-into-sql-queries-and)
- **ID:** 3497 | **Creator:** @hippolyte-hu ✓ | **Views:** 2,904 | **Nodes:** 5
- **Nodes:** Postgres, AI Agent, OpenAI Chat Model +2 more
- Conversational Data Retrieval and Visualization Workflow

This workflow enables users to interact with a PostgreSQL database using natural language. It translates text inputs into SQL queries, retriev...

### [Vector Database as a Big Data Analysis Tool for AI Agents [3/3 - anomaly]](https://n8n.io/workflows/2656-vector-database-as-a-big-data-analysis-tool-for-ai-agents-3)
- **ID:** 2656 | **Creator:** @mrscoopers ✓ | **Views:** 2,850 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- Vector Database as a Big Data Analysis Tool for AI Agents

Workflows from the webinar "Build production-ready AI Agents with Qdrant and n8n".

This series of workflows shows how to build big data anal...

### [Monitor SSL certificate of any domain with uProc](https://n8n.io/workflows/861-monitor-ssl-certificate-of-any-domain-with-uproc)
- **ID:** 861 | **Creator:** @mcolomer ✓ | **Views:** 2,697 | **Nodes:** 2
- **Nodes:** Telegram, uProc
- Do you want to check the SSL certificate expiration dates of your customers or servers?

This workflow gets information of an SSL certificate using the uProc Get Certificate by domain tool.
You can us...

### [Monitor if a page is alive and notify via Twilio SMS if not](https://n8n.io/workflows/2524-monitor-if-a-page-is-alive-and-notify-via-twilio-sms-if-not)
- **ID:** 2524 | **Creator:** @rpb-dev ✓ | **Views:** 2,663 | **Nodes:** 2
- **Nodes:** HTTP Request, Twilio
- Workflow Purpose

This workflow periodically checks a service's availability and sends an SMS notification if the service is down.

High-Level Steps

Schedule Trigger: The workflow is triggered at a s...

### [Prompt-based Object Detection with Gemini 2.0](https://n8n.io/workflows/2649-prompt-based-object-detection-with-gemini-20)
- **ID:** 2649 | **Creator:** @jimleuk ✓ | **Views:** 2,590 | **Nodes:** 3
- **Nodes:** Edit Image, HTTP Request, Code
- This n8n template demonstrates how to get started with Gemini 2.0's new Bounding Box detection capabilities in your workflows.

The key difference being this enables prompt-based object detection for...

### [Send HTTP Requests to a list of URLs](https://n8n.io/workflows/2276-send-http-requests-to-a-list-of-urls)
- **ID:** 2276 | **Creator:** @ericfrancis | **Views:** 2,523 | **Nodes:** 1
- **Nodes:** HTTP Request
- How it works
This workflow reads a list of URLs every 15 minutes, and sends an HTTP request to every URL on the list.

Set up steps
Schedule the workflow to run at your desired frequency (default is e...

### [Qualys Vulnerability Trigger Scan SubWorkflow](https://n8n.io/workflows/2511-qualys-vulnerability-trigger-scan-subworkflow)
- **ID:** 2511 | **Creator:** @djangelic ✓ | **Views:** 2,444 | **Nodes:** 2
- **Nodes:** HTTP Request, Slack
- This workflow is triggered by a parent workflow initiated via a Slack shortcut. Upon activation, it collects input from a modal window in Slack and initiates a vulnerability scan using the Qualys API....

### [Monitor Server Uptime & Get Email Alerts with Google Sheets](https://n8n.io/workflows/3880-monitor-server-uptime-and-get-email-alerts-with-google-sheet)
- **ID:** 3880 | **Creator:** @khaled | **Views:** 2,438 | **Nodes:** 3
- **Nodes:** Google Sheets, HTTP Request, Gmail
- 🌐 Web Server Monitor & Alert System

This automation pings web servers at regular intervals, logs their status, and sends email alerts if a server goes down. It’s perfect for maintaining visibility ov...

### [MongoDB AI Agent - Intelligent Movie Recommendations](https://n8n.io/workflows/2554-mongodb-ai-agent-intelligent-movie-recommendations)
- **ID:** 2554 | **Creator:** @pash | **Views:** 2,428 | **Nodes:** 4
- **Nodes:** AI Agent, OpenAI Chat Model, Simple Memory +1 more
- Who is this for?
This workflow is designed for:
Database administrators and developers working with MongoDB
Content managers handling movie databases
Organizations looking to implement AI-powered sea...

### [Parse DMARC reports, save them in database and notify on DKIM or SPF error](https://n8n.io/workflows/2369-parse-dmarc-reports-save-them-in-database-and-notify-on-dkim)
- **ID:** 2369 | **Creator:** @lukaszpp ✓ | **Views:** 2,424 | **Nodes:** 4
- **Nodes:** Send Email, Slack, MySQL +1 more
- Who is it for
If you are a postmaster or you manage email server, you can set up DKIM and SPF records to ensure that spoofing your email address is hard. On your domain you can also set up DMARC recor...

### [Generate AI Prompts with Google Gemini and store them in Airtable](https://n8n.io/workflows/3027-generate-ai-prompts-with-google-gemini-and-store-them-in-air)
- **ID:** 3027 | **Creator:** @imperolq ✓ | **Views:** 2,370 | **Nodes:** 5
- **Nodes:** Airtable, Basic LLM Chain, Auto-fixing Output Parser +2 more
- This workflow is designed to generate prompts for AI agents and store them in Airtable. 


It starts by receiving a chat message, processes it to create a structured prompt, categorizes the prompt, an...

### [Create Unique Jira tickets from Splunk alerts](https://n8n.io/workflows/1970-create-unique-jira-tickets-from-splunk-alerts)
- **ID:** 1970 | **Creator:** @n8n-team ✓ | **Views:** 2,321 | **Nodes:** 1
- **Nodes:** Jira Software
- The workflow is an automated process designed for incident management and tracking, specifically by integrating Splunk alerts with a Jira ticketing system using n8n. The initial step in the workflow i...

### [XML to SQL database import](https://n8n.io/workflows/1948-xml-to-sql-database-import)
- **ID:** 1948 | **Creator:** @n8n-team ✓ | **Views:** 2,311 | **Nodes:** 1
- **Nodes:** Code
- This is an example workflow that imports an XML file into an SQL database.
The ReadBinaryFiles node loads the XML file from the server.
Then the Code node extracts the file content from the binary buf...

### [MCP Supabase Agent – Manage Your Database with AI](https://n8n.io/workflows/3641-mcp-supabase-agent-manage-your-database-with-ai)
- **ID:** 3641 | **Creator:** @amanda ✓ | **Views:** 2,308 | **Nodes:** 4
- **Nodes:** AI Agent, OpenAI Chat Model, Simple Memory +1 more
- Hi, I’m Amanda 🌷
This workflow was built with love to help you manage your Supabase database using natural language, powered by the MCP (Multi-Channel Protocol) AI Agent on n8n.

With just a message l...

### [🛠️ Auto Workflow Positioning](https://n8n.io/workflows/2667-auto-workflow-positioning)
- **ID:** 2667 | **Creator:** @lucaspeyrin ✓ | **Views:** 2,276 | **Nodes:** 9
- **Nodes:** HTTP Request, AI Agent, Question and Answer Chain +6 more
- Check Online Version !
[https://n8n-tools.streamlit.app/](https://n8n-tools.streamlit.app/
)
Who is it for?  
This workflow is perfect for n8n users who want to maintain clean and organized workflows...

### [MFA Multi-factor authentication (Voice call and Email) with ClickSend and SMTP](https://n8n.io/workflows/3142-mfa-multi-factor-authentication-voice-call-and-email-with-cl)
- **ID:** 3142 | **Creator:** @n3witalia ✓ | **Views:** 2,238 | **Nodes:** 3
- **Nodes:** Send Email, HTTP Request, Code
- This workflow automates the process of sending voice calls for verification purposes and combines it with email verification. It uses the ClickSend API for voice calls and integrates with SMTP for ema...

### [Receive server-sent events](https://n8n.io/workflows/639-receive-server-sent-events)
- **ID:** 639 | **Creator:** @harshil1712 ✓ | **Views:** 2,154 | **Nodes:** 0
- **Nodes:** 
- Companion workflow for SSE Trigger node docs

### [Use Redis to rate-limit your low-code API](https://n8n.io/workflows/1236-use-redis-to-rate-limit-your-low-code-api)
- **ID:** 1236 | **Creator:** @harshil1712 ✓ | **Views:** 2,146 | **Nodes:** 2
- **Nodes:** Airtable, Redis
- This workflow demonstrates how to can use Redis to implement rate limits to your API.



The workflow uses the incoming API key to uniquely identify the user and use it as a key in Redis. Every time a...

### [🛠️ Auto n8n Updater (Docker)](https://n8n.io/workflows/5198-auto-n8n-updater-docker)
- **ID:** 5198 | **Creator:** @lucaspeyrin ✓ | **Views:** 2,116 | **Nodes:** 4
- **Nodes:** HTTP Request, Telegram, Basic LLM Chain +1 more
- How it works

This workflow automates the process of checking for and applying updates to a self-hosted n8n instance running on Docker. It runs on a schedule, checks for new versions, summarizes the r...

### [Check if workflows contain build-in nodes that are not of the latest version](https://n8n.io/workflows/2301-check-if-workflows-contain-build-in-nodes-that-are-not-of-th)
- **ID:** 2301 | **Creator:** @mkret | **Views:** 2,110 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- How it works
it will return workflows that have buil-in nodes not of latest version with information of node name, type, current version and latest version for that type

Set up steps:
You need to hav...

### [Create OpenAI-Compatible API Using GitHub Models for Free AI Access](https://n8n.io/workflows/4217-create-openai-compatible-api-using-github-models-for-free-ai)
- **ID:** 4217 | **Creator:** @jimleuk ✓ | **Views:** 2,084 | **Nodes:** 3
- **Nodes:** HTTP Request, Basic LLM Chain, OpenAI Chat Model
- This n8n template shows you how to connect Github's Free Models to your existing n8n AI workflows.

Whilst it is possible to use HTTP nodes to access Github Models, The aim of this template is to use...

### [Load data into Snowflake](https://n8n.io/workflows/1918-load-data-into-snowflake)
- **ID:** 1918 | **Creator:** @n8n-team ✓ | **Views:** 2,061 | **Nodes:** 2
- **Nodes:** HTTP Request, Snowflake
- This workflow automatically downloads a CSV from the web, and parses it in a format that n8n can access. It then ensures that the data from the CSV is matched to the names of the columns in the databa...

### [Build an On-Premises AI Kaggle Competition Assistant with Qdrant RAG and Ollama](https://n8n.io/workflows/3967-build-an-on-premises-ai-kaggle-competition-assistant-with-qd)
- **ID:** 3967 | **Creator:** @jac2325057 | **Views:** 2,052 | **Nodes:** 10
- **Nodes:** AI Agent, Summarization Chain, Ollama Chat Model +7 more
- LLM/RAG Kaggle Development Assistant

An on-premises, domain-specific AI assistant for Kaggle (tested on binary disaster-tweet classification), combining LLM, an n8n workflow engine, and Qdrant-backed...

### [Generate n8n Forms from Airtable and BaseRow Tables ](https://n8n.io/workflows/2603-generate-n8n-forms-from-airtable-and-baserow-tables)
- **ID:** 2603 | **Creator:** @jimleuk ✓ | **Views:** 2,047 | **Nodes:** 3
- **Nodes:** Airtable, HTTP Request, Code
- This n8n template showcases a cool feature of n8n Forms where the form itself can be defined dynamically using the form fields schema.

It may be debateable how useful this template actually is since...

### [Evaluation metric example: RAG document relevance](https://n8n.io/workflows/4273-evaluation-metric-example-rag-document-relevance)
- **ID:** 4273 | **Creator:** @davidn8n ✓ | **Views:** 2,022 | **Nodes:** 9
- **Nodes:** Google Sheets, AI Agent, Embeddings OpenAI +6 more
- AI evaluation in n8n

This is a template for n8n's evaluation feature. 

Evaluation is a technique for getting confidence that your AI workflow performs reliably, by running a test dataset containing...

### [Mark outdated workflow nodes on canvas and send a summary with Gmail (add-on)](https://n8n.io/workflows/2477-mark-outdated-workflow-nodes-on-canvas-and-send-a-summary-wi)
- **ID:** 2477 | **Creator:** @octionic ✓ | **Views:** 1,983 | **Nodes:** 2
- **Nodes:** Gmail, Code
- This is an add-on for the template Check if workflows contain build-in nodes that are not of the latest version

Purpose

This workflow highlights outdated nodes within all workflows of a single n8n i...

### [🛠️ State Management System for Long-Running Workflows with Wait Nodes](https://n8n.io/workflows/6269-state-management-system-for-long-running-workflows-with-wai)
- **ID:** 6269 | **Creator:** @lucaspeyrin ✓ | **Views:** 1,972 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- How it works

This template is a powerful, reusable utility for managing stateful, long-running processes. It allows a main workflow to be paused indefinitely at "checkpoints" and then be resumed by e...

### [🚨 Report n8n workflow errors to Slack](https://n8n.io/workflows/2150-report-n8n-workflow-errors-to-slack)
- **ID:** 2150 | **Creator:** @mutasem ✓ | **Views:** 1,957 | **Nodes:** 1
- **Nodes:** Slack
- Use case
Error workflows are an important part of running workflows in production.

How to setup
Add Slack creds
Add this error workflow to other workflows (docs)

### [🛠️ Transform JSON to XML for Enhanced AI Prompt Formatting](https://n8n.io/workflows/5144-transform-json-to-xml-for-enhanced-ai-prompt-formatting)
- **ID:** 5144 | **Creator:** @lucaspeyrin ✓ | **Views:** 1,943 | **Nodes:** 1
- **Nodes:** Code
- Overview

This template provides a powerful and configurable utility to convert JSON data into a clean, well-structured XML format. It is designed for developers, data analysts, and n8n users who need...

### [Send DingTalk message on new Azure DevOps Pull Request](https://n8n.io/workflows/2034-send-dingtalk-message-on-new-azure-devops-pull-request)
- **ID:** 2034 | **Creator:** @wuliang | **Views:** 1,937 | **Nodes:** 3
- **Nodes:** HTTP Request, MySQL, Code
- This template automates sending a DingTalk message on new Azure Dev Ops Pull Request Created Events. It uses a MySQL database to store mappings between Azure users and DingTalk users; so the right use...

### [Build your own Qdrant Vector Store MCP server](https://n8n.io/workflows/3636-build-your-own-qdrant-vector-store-mcp-server)
- **ID:** 3636 | **Creator:** @jimleuk ✓ | **Views:** 1,880 | **Nodes:** 7
- **Nodes:** HTTP Request, Code, Embeddings OpenAI +4 more
- This n8n demonstrates how to build your own Qdrant MCP server to extend its functionality beyond that of the official implementation.

This n8n implementation exposes other cool API features from Qdra...

### [Conversational PostgreSQL Agent with Visuals, Multi-KPI, and Data Editing (MCP)](https://n8n.io/workflows/3903-conversational-postgresql-agent-with-visuals-multi-kpi-and-d)
- **ID:** 3903 | **Creator:** @hippolyte-hu ✓ | **Views:** 1,878 | **Nodes:** 7
- **Nodes:** Postgres, AI Agent, Anthropic Chat Model +4 more
- Ask your PostgreSQL database complex questions and receive clear summaries, charts, and even update or insert data — all through one smart agent powered by n8n’s Model Context Protocol (MCP).

Suppo...

### [Create AI-Ready Vector Datasets for LLMs with Bright Data, Gemini & Pinecone](https://n8n.io/workflows/3542-create-ai-ready-vector-datasets-for-llms-with-bright-data-ge)
- **ID:** 3542 | **Creator:** @ranjancse ✓ | **Views:** 1,869 | **Nodes:** 10
- **Nodes:** HTTP Request, AI Agent, Basic LLM Chain +7 more
- Who this is for?
This workflow enables automated, scalable collection of high-quality, AI-ready data from websites using Bright Data’s Web Unlocker, with a focus on preparing that data for LLM trainin...

### [n8n Subworkflow Dependency Graph & Auto-Tagging](https://n8n.io/workflows/2939-n8n-subworkflow-dependency-graph-and-auto-tagging)
- **ID:** 2939 | **Creator:** @ludwig ✓ | **Views:** 1,859 | **Nodes:** 3
- **Nodes:** HTTP Request, Code, QuickChart
- How it Works
As n8n instances scale, teams often lose track of sub-workflows—who uses them, where they are referenced, and whether they can be safely updated. This leads to inefficiencies like unneces...

### [Restore your credentials from GitHub](https://n8n.io/workflows/3097-restore-your-credentials-from-github)
- **ID:** 3097 | **Creator:** @bangank36 ✓ | **Views:** 1,844 | **Nodes:** 2
- **Nodes:** GitHub, HTTP Request
- This workflow restores all n8n instance credentials from GitHub backups using the n8n API node. It complements the Backup Your Credentials to GitHub template by allowing users to seamlessly restore pr...

### [Incident Response Workflow - Part 3](https://n8n.io/workflows/355-incident-response-workflow-part-3)
- **ID:** 355 | **Creator:** @tanay1337 ✓ | **Views:** 1,832 | **Nodes:** 3
- **Nodes:** Mattermost, Jira Software, PagerDuty
- This workflow is the third of three. You can find the other workflkows here:

Incident Response Workflow - Part 1
Incident Response Workflow - Part 2
Incident Response Workflow - Part 3

We have the f...

### [Invoke an AWS Lambda function](https://n8n.io/workflows/510-invoke-an-aws-lambda-function)
- **ID:** 510 | **Creator:** @sm-amudhan ✓ | **Views:** 1,819 | **Nodes:** 1
- **Nodes:** AWS Lambda
- Companion workflow for AWS Lambda docs

### [Track AI Agent token usage and estimate costs in Google Sheets](https://n8n.io/workflows/5541-track-ai-agent-token-usage-and-estimate-costs-in-google-shee)
- **ID:** 5541 | **Creator:** @solomon ✓ | **Views:** 1,818 | **Nodes:** 6
- **Nodes:** Google Sheets, AI Agent, Anthropic Chat Model +3 more
- This n8n template demonstrates how to obtain token usage from AI Agents and places the data into a spreadsheet that calculates the estimated cost of the execution.

Obtaining the token usage from AI...

### [Notify User in Slack of Quarantined Email and Create Jira Ticket if Opened](https://n8n.io/workflows/1975-notify-user-in-slack-of-quarantined-email-and-create-jira-ti)
- **ID:** 1975 | **Creator:** @n8n-team ✓ | **Views:** 1,812 | **Nodes:** 4
- **Nodes:** HTTP Request, Slack, Jira Software +1 more
- This n8n workflow serves as an incident response and notification system for handling potentially malicious emails flagged by Sublime Security. It begins with a Webhook trigger that Sublime Security u...

### [Automate Docker Container Updates with Telegram Approval System](https://n8n.io/workflows/3386-automate-docker-container-updates-with-telegram-approval-sys)
- **ID:** 3386 | **Creator:** @j4b3r | **Views:** 1,808 | **Nodes:** 2
- **Nodes:** HTTP Request, Telegram
- Who is this for?
This workflow is for DevOps engineers, system administrators, and Docker users who want to automate the process of checking for updates, verifying them, and applying updates to their...

### [Release a new version via Telegram bot command](https://n8n.io/workflows/1134-release-a-new-version-via-telegram-bot-command)
- **ID:** 1134 | **Creator:** @harshil1712 ✓ | **Views:** 1,782 | **Nodes:** 1
- **Nodes:** GitHub
- This workflow allows you to release a new version via a Telegram bot command. This workflow can be used in your Continous Delivery pipeline.



Telegram Trigger node: This node will trigger the workfl...

### [Better Oauth2.0 workflow for Pipedrive CRM with Supabase](https://n8n.io/workflows/2319-better-oauth20-workflow-for-pipedrive-crm-with-supabase)
- **ID:** 2319 | **Creator:** @processease | **Views:** 1,780 | **Nodes:** 3
- **Nodes:** HTTP Request, Supabase, Code
- This workflow provides an OAuth 2.0 auth token refresh process for better control. Developers can utilize it as an alternative to n8n's built-in OAuth flow to achieve improved control and visibility....

### [n8n workflow backup management with Dropbox and Airtable](https://n8n.io/workflows/823-n8n-workflow-backup-management-with-dropbox-and-airtable)
- **ID:** 823 | **Creator:** @shrey-42 | **Views:** 1,760 | **Nodes:** 3
- **Nodes:** Airtable, Dropbox, HTTP Request
- This workflow can be used to save all of your workflows in:
a raw state (as a json file in Dropbox)
an Airtable base, in a pre-designed format.

It runs periodically (currently, every 30 minutes) and...

### [Backup Tag-Selected Workflows to Gitlab](https://n8n.io/workflows/2376-backup-tag-selected-workflows-to-gitlab)
- **ID:** 2376 | **Creator:** @hubschrauber ✓ | **Views:** 1,718 | **Nodes:** 1
- **Nodes:** GitLab
- Fetches workflow definitions from within n8n, selecting only the ones that have one or more (configurable) assigned tags and then:
Derives a suitable backup filename by reducing the workflow name to a...

### [👲 Monitor & debug n8n workflows with Claude AI assistant and MCP server](https://n8n.io/workflows/10779-monitor-and-debug-n8n-workflows-with-claude-ai-assistant-an)
- **ID:** 10779 | **Creator:** @samirsaci ✓ | **Views:** 1,710 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- Tags*: AI Agent, MCP Server, n8n API, Monitoring, Debugging, Workflow Analytics, Automation

Context

Hi! I’m Samir — a Supply Chain Engineer and Data Scientist based in Paris, and founder of LogiGree...

### [Get the value of a key from Redis](https://n8n.io/workflows/557-get-the-value-of-a-key-from-redis)
- **ID:** 557 | **Creator:** @sm-amudhan ✓ | **Views:** 1,710 | **Nodes:** 1
- **Nodes:** Redis
- Companion workflow for Redis node docs

### [Merge greetings with the users based on the language](https://n8n.io/workflows/655-merge-greetings-with-the-users-based-on-the-language)
- **ID:** 655 | **Creator:** @n8n-team ✓ | **Views:** 1,703 | **Nodes:** 0
- **Nodes:** 
- Who this is for
Every who's interested in seeing how merging items works in n8n

What this workflow does
This workflow generates two sets of sample data: one with names and corresponding languages, an...

### [Send location updates of the ISS every minute to a table in Google BigQuery](https://n8n.io/workflows/1049-send-location-updates-of-the-iss-every-minute-to-a-table-in)
- **ID:** 1049 | **Creator:** @harshil1712 ✓ | **Views:** 1,701 | **Nodes:** 2
- **Nodes:** HTTP Request, Google BigQuery
- This workflow allows you to send position updates of the ISS every minute to a table in Google BigQuery.



Cron node: The Cron node will trigger the workflow every minute.

HTTP Request node: This no...

### [Email Assistant: Convert Natural Language to SQL Queries with Phi4-mini and PostgreSQL](https://n8n.io/workflows/3761-email-assistant-convert-natural-language-to-sql-queries-with)
- **ID:** 3761 | **Creator:** @acorretti ✓ | **Views:** 1,672 | **Nodes:** 3
- **Nodes:** Postgres, AI Agent, Ollama Chat Model
- Who is this for?

🧑🏻🫱🏻‍🫲🏻🤖 Humans and Robots alike.

This workflow can be used as a Chat Trigger, as well as a Workflow Trigger.

It will take a natural language request, and then generate a SQL query...

### [SSL Certificate Expiry Notifier (No Paid APIs)](https://n8n.io/workflows/4643-ssl-certificate-expiry-notifier-no-paid-apis)
- **ID:** 4643 | **Creator:** @evoortsolutions ✓ | **Views:** 1,652 | **Nodes:** 3
- **Nodes:** Send Email, Google Sheets, HTTP Request
- Great — here’s a complete Workflow Description for your n8n Creator submission based on the JSON you shared:

🔒 SSL Expiry Notifier (No Paid APIs)

🧩 How it Works

This workflow automatically checks S...

### [Conversational Kubernetes Management with GPT-4o and MCP Integration](https://n8n.io/workflows/4023-conversational-kubernetes-management-with-gpt-4o-and-mcp-int)
- **ID:** 4023 | **Creator:** @reza-gholizade | **Views:** 1,642 | **Nodes:** 4
- **Nodes:** AI Agent, OpenAI Chat Model, Simple Memory +1 more
- This n8n workflow template uses community nodes and is only compatible with the self-hosted version of n8n. 

Conversational Kubernetes Management with GPT-4o and MCP Integration

This workflow enable...

### [Receive updates for Bitbucket events](https://n8n.io/workflows/529-receive-updates-for-bitbucket-events)
- **ID:** 529 | **Creator:** @sm-amudhan ✓ | **Views:** 1,612 | **Nodes:** 0
- **Nodes:** 
- Companion workflow for Bitbucket Trigger node docs

### [🚨 Report n8n workflow errors directly to your email](https://n8n.io/workflows/2160-report-n8n-workflow-errors-directly-to-your-email)
- **ID:** 2160 | **Creator:** @mutasem ✓ | **Views:** 1,570 | **Nodes:** 1
- **Nodes:** Gmail
- Use case
Error workflows are an important part of running workflows in production. Get alerts for errors directly in your inbox.

How to setup
Add your Gmail creds
Add your target email
Add this error...

### [Provide Real-Time Updates for Notion Databases via Webhooks with Supabase](https://n8n.io/workflows/2284-provide-real-time-updates-for-notion-databases-via-webhooks)
- **ID:** 2284 | **Creator:** @octionic ✓ | **Views:** 1,551 | **Nodes:** 4
- **Nodes:** HTTP Request, Notion, Supabase +1 more
- Purpose

This enables webhooks for nearly realtime updates (every 5 seconds) from Notion Databases.

Problem

Notion does not offer webhooks. Even worse, the “Last edited time” property, we could use...

### [Deploy site when new content gets added](https://n8n.io/workflows/1254-deploy-site-when-new-content-gets-added)
- **ID:** 1254 | **Creator:** @harshil1712 ✓ | **Views:** 1,548 | **Nodes:** 1
- **Nodes:** Netlify
- This workflow demonstrates how to create a new deployment when new content gets added to the database. This example workflow can be used when building a JAMstack site.



Webhook node: This node trigg...

### [Send Slack notifications when a new release is published for public Github repos](https://n8n.io/workflows/2353-send-slack-notifications-when-a-new-release-is-published-for)
- **ID:** 2353 | **Creator:** @dkarzon | **Views:** 1,525 | **Nodes:** 3
- **Nodes:** HTTP Request, Slack, Code
- This workflow checks a configured list of Github repositories daily to see if a new release has been published.

How it works:
Workflow has a daily trigger
RepoConfig node is a JSON array that defines...

### [Get the last five SpaceX launches from the spacex.land API using GraphQL](https://n8n.io/workflows/558-get-the-last-five-spacex-launches-from-the-spacexland-api-us)
- **ID:** 558 | **Creator:** @sm-amudhan ✓ | **Views:** 1,508 | **Nodes:** 1
- **Nodes:** GraphQL
- Companion workflow for GraphQL node docs

### [Get DNS entries of any domain with uProc](https://n8n.io/workflows/862-get-dns-entries-of-any-domain-with-uproc)
- **ID:** 862 | **Creator:** @mcolomer ✓ | **Views:** 1,499 | **Nodes:** 1
- **Nodes:** uProc
- Do you want to control the DNS domain entries of your customers or servers?

This workflow gets DNS information of any domain using the uProc Get Domain DNS records tool.

You can use this workflow to...

### [Daily GitHub Release notification by Email](https://n8n.io/workflows/2590-daily-github-release-notification-by-email)
- **ID:** 2590 | **Creator:** @dionysus | **Views:** 1,498 | **Nodes:** 2
- **Nodes:** Send Email, HTTP Request
- Automating daily notifications of the latest releases from a GitHub repository. This template is ideal for developers and project managers looking to stay up-to-date with software updates.

How it Wor...

### [Prevent simultaneous workflow executions with Redis](https://n8n.io/workflows/2270-prevent-simultaneous-workflow-executions-with-redis)
- **ID:** 2270 | **Creator:** @octionic ✓ | **Views:** 1,484 | **Nodes:** 1
- **Nodes:** Redis
- Purpose
This ensures that executions of scheduled workflows do not overlap when they take longer than expected.

How it works
This is a separate workflow which monitors the execution of the main workf...

### [Incident Response Workflow - Part 2](https://n8n.io/workflows/354-incident-response-workflow-part-2)
- **ID:** 354 | **Creator:** @tanay1337 ✓ | **Views:** 1,477 | **Nodes:** 2
- **Nodes:** Mattermost, PagerDuty
- This workflow is the second of three. You can find the other workflkows here:

Incident Response Workflow - Part 1
Incident Response Workflow - Part 2
Incident Response Workflow - Part 3


We have the...

### [Report phishing websites to Steam and CloudFlare](https://n8n.io/workflows/122-report-phishing-websites-to-steam-and-cloudflare)
- **ID:** 122 | **Creator:** @chauffer | **Views:** 1,476 | **Nodes:** 1
- **Nodes:** Mailgun
- Webhook to report through Mailgun phishing websites to Steam and CloudFlare (if the domain is on CloudFlare)

You have to set the Credentials for webhook and Mailgun.

You have to set the email from f...

### [Send updates about the position of the ISS every minute to a topic in RabbitMQ](https://n8n.io/workflows/844-send-updates-about-the-position-of-the-iss-every-minute-to-a)
- **ID:** 844 | **Creator:** @harshil1712 ✓ | **Views:** 1,449 | **Nodes:** 2
- **Nodes:** HTTP Request, RabbitMQ
- This workflow allows you to send updates about the position of the ISS every minute to a topic in RabbitMQ

### [Trigger a build in Travis CI when code changes are push to a GitHub repo](https://n8n.io/workflows/1132-trigger-a-build-in-travis-ci-when-code-changes-are-push-to-a)
- **ID:** 1132 | **Creator:** @harshil1712 ✓ | **Views:** 1,447 | **Nodes:** 1
- **Nodes:** TravisCI
- This workflow allows you to trigger a build in Travis CI when code changes are pushed to a GitHub repo or a pull request gets opened.



GitHub Trigger node: This node will trigger the workflow when c...

### [Send updates about the position of the ISS every minute to a topic in Kafka](https://n8n.io/workflows/750-send-updates-about-the-position-of-the-iss-every-minute-to-a)
- **ID:** 750 | **Creator:** @harshil1712 ✓ | **Views:** 1,425 | **Nodes:** 2
- **Nodes:** HTTP Request, Kafka

### [🧠 *NEW* Claude 3.7 Extended Thinking AI Agent 🤖 – Unlock Ultimate Intelligence](https://n8n.io/workflows/3009-new-claude-37-extended-thinking-ai-agent-unlock-ultimate)
- **ID:** 3009 | **Creator:** @jonasbusch ✓ | **Views:** 1,417 | **Nodes:** 1
- **Nodes:** HTTP Request
- 🧠 NEW Claude 3.7 Extended Thinking AI Agent 🤖 – Unlock Ultimate Intelligence

Supercharge Claude 3.7 with full customization & deeper reasoning!  

Who is this for? 🎯  
✅ AI Enthusiasts & Researchers:...

### [Error handling: Send email via Gmail on execution or trigger-level errors](https://n8n.io/workflows/3075-error-handling-send-email-via-gmail-on-execution-or-trigger)
- **ID:** 3075 | **Creator:** @olek | **Views:** 1,411 | **Nodes:** 3
- **Nodes:** Gmail, Code, HTML
- This error handling workflow emails detailed notifications on workflow execution and trigger errors.

It extends Send email via Gmail on workflow error template by covering trigger-level errors.

Feat...

### [Compare Sequential, Agent-Based, and Parallel LLM Processing with Claude 3.7](https://n8n.io/workflows/3527-compare-sequential-agent-based-and-parallel-llm-processing-w)
- **ID:** 3527 | **Creator:** @eduard ✓ | **Views:** 1,406 | **Nodes:** 6
- **Nodes:** HTTP Request, AI Agent, Basic LLM Chain +3 more
- This workflow demonstrates three distinct approaches to chaining LLM operations using Claude 3.7 Sonnet. Connect to any section to experience the differences in implementation, performance, and capabi...

### [Get workflows affected by 0.214.3 migration](https://n8n.io/workflows/1892-get-workflows-affected-by-02143-migration)
- **ID:** 1892 | **Creator:** @oleg | **Views:** 1,402 | **Nodes:** 2
- **Nodes:** Code, HTML
- If you previously upgraded to n8n version 0.214.3, some of your workflows might have been accidentally rewired in the wrong way. This issue affected nodes with more than one output, such as If, Switch...

### [Automate Google OAuth2 Credential Creation in n8n](https://n8n.io/workflows/2909-automate-google-oauth2-credential-creation-in-n8n)
- **ID:** 2909 | **Creator:** @jordan | **Views:** 1,355 | **Nodes:** 0
- **Nodes:** 
- Overview: Automate Your Google OAuth2 Credential Creation

This workflow template streamlines the process of creating and naming individual Google OAuth2  credentials for multiple Google services wit...

### [Weekly N8N executions failures report to Telegram](https://n8n.io/workflows/2177-weekly-n8n-executions-failures-report-to-telegram)
- **ID:** 2177 | **Creator:** @manu-n8n | **Views:** 1,329 | **Nodes:** 1
- **Nodes:** Telegram
- How it works
Weekly triggered
Fetches all previous executions of a given workflow
Filter for failures and aggregate them into a single report
Sends them to a given Telegram chat.

Set up steps
Create...

### [Auto-Notify on New Major n8n Releases via RSS, Email & Telegram](https://n8n.io/workflows/736-auto-notify-on-new-major-n8n-releases-via-rss-email-and-tele)
- **ID:** 736 | **Creator:** @mcolomer ✓ | **Views:** 1,327 | **Nodes:** 2
- **Nodes:** Telegram, AWS SES
- This n8n workflow template checks for new major releases (tagged with .0) of the n8n project using its official GitHub releases feed. It runs multiple times a day and sends notifications via email a...

### [Test Webhooks in n8n Without Changing WEBHOOK_URL (PostBin & BambooHR Example)](https://n8n.io/workflows/2869-test-webhooks-in-n8n-without-changing-webhookurl-postbin-and)
- **ID:** 2869 | **Creator:** @ludwig ✓ | **Views:** 1,308 | **Nodes:** 9
- **Nodes:** HTTP Request, Slack, BambooHR +6 more
- Using PostBin to Test Webhooks Without Changing WEBHOOK_URL  

How it Works  
Many new n8n users struggle with testing webhooks when running n8n on localhost, as external services cannot reach localho...

### [Triage alerts from Syncro and submit to OpsGenie](https://n8n.io/workflows/1491-triage-alerts-from-syncro-and-submit-to-opsgenie)
- **ID:** 1491 | **Creator:** @jon-n8n ✓ | **Views:** 1,304 | **Nodes:** 1
- **Nodes:** HTTP Request
- This workflow will take an alert from Syncro, determine if it's an agent_offline_trigger type, then determine if it's a new alert or a close to an existing alert, and then submit it to OpsGenie. New a...

### [Automate GitHub, JIRA release notes with Google Gemini & notification over email](https://n8n.io/workflows/6129-automate-github-jira-release-notes-with-google-gemini-and-no)
- **ID:** 6129 | **Creator:** @intuz ✓ | **Views:** 1,298 | **Nodes:** 6
- **Nodes:** Send Email, Jira Software, Code +3 more
- This n8n template from Intuz provides a complete and automated solution for creating and distributing sophisticated release notes. 

It connects to GitHub and JIRA to gather data from recent commits a...

### [KV - Cloudflare Key-Value Database Full API Integration Workflow](https://n8n.io/workflows/2046-kv-cloudflare-key-value-database-full-api-integration-work)
- **ID:** 2046 | **Creator:** @nskha ✓ | **Views:** 1,293 | **Nodes:** 1
- **Nodes:** HTTP Request
- This n8n template provides a comprehensive solution for managing Key-Value (KV) pairs using Cloudflare's KV storage. It's designed to simplify the interaction with Cloudflare's KV storage APIs, enab...

### [Preconfigured nodes for Systeme.io API requests](https://n8n.io/workflows/2368-preconfigured-nodes-for-systemeio-api-requests)
- **ID:** 2368 | **Creator:** @solomon ✓ | **Views:** 1,270 | **Nodes:** 1
- **Nodes:** HTTP Request
- Using the Systeme API can be challenging due to its pagination settings and low rate limit. This requires a bit more knowledge about API requests than a beginner might have.

This template provides pr...

### [Get Real-Time Security Insights with NixGuard RAG and Wazuh Integration](https://n8n.io/workflows/4693-get-real-time-security-insights-with-nixguard-rag-and-wazuh)
- **ID:** 4693 | **Creator:** @nex ✓ | **Views:** 1,247 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- Effortlessly integrate NixGuard API into your n8n workflows for real-time security insights using your API key. This connector enables seamless interaction with Nix, providing rapid Retrieval-Augmente...

### [Receive updates for GitHub events](https://n8n.io/workflows/527-receive-updates-for-github-events)
- **ID:** 527 | **Creator:** @sm-amudhan ✓ | **Views:** 1,242 | **Nodes:** 0
- **Nodes:** 
- Companion workflow for Github Trigger node docs

### [Manage changes using the Git node](https://n8n.io/workflows/1115-manage-changes-using-the-git-node)
- **ID:** 1115 | **Creator:** @harshil1712 ✓ | **Views:** 1,241 | **Nodes:** 0
- **Nodes:** 
- This workflow allows you to add, commit, and push changes to a git repository.



Git node: This node will add the README.md file to the staging area. If you want to add a different file, enter the pa...

### [Restore your workflows from GitHub](https://n8n.io/workflows/3096-restore-your-workflows-from-github)
- **ID:** 3096 | **Creator:** @bangank36 ✓ | **Views:** 1,240 | **Nodes:** 2
- **Nodes:** GitHub, HTTP Request
- This workflow restores all n8n instance workflows from GitHub backups using the n8n API node. It complements the Backup Your Workflows to GitHub template by allowing users to seamlessly restore previo...

### [🔄 Workflow Repos8r: Github Version Control User Interface for n8n Workflows](https://n8n.io/workflows/3014-workflow-repos8r-github-version-control-user-interface-for)
- **ID:** 3014 | **Creator:** @joeperes ✓ | **Views:** 1,226 | **Nodes:** 3
- **Nodes:** GitHub, Code, HTML
- 🔥 n8n Members Sale – n8n Community Members Get ideoGener8r for Just $10! (Reg. $15)
Use Coupon Code: FeelinTheFlowgramming
(Valid for n8n community members)

💪 How it works
Seamlessly track, manage, a...

### [Create a new DigitalOcean Droplet](https://n8n.io/workflows/435-create-a-new-digitalocean-droplet)
- **ID:** 435 | **Creator:** @sm-amudhan ✓ | **Views:** 1,207 | **Nodes:** 1
- **Nodes:** HTTP Request
- Uses a DigitalOcean Personal Access Token to create a new Droplet.

Add your personal access token and change the parameters to create droplets of different sizes.

You can also specify more options;...

### [Batch Process Prompts with Anthropic Claude API](https://n8n.io/workflows/3409-batch-process-prompts-with-anthropic-claude-api)
- **ID:** 3409 | **Creator:** @greg ✓ | **Views:** 1,201 | **Nodes:** 4
- **Nodes:** HTTP Request, Code, Simple Memory +1 more
- This workflow template provides a robust solution for efficiently sending multiple prompts to Anthropic's Claude models in a single batch request and retrieving the results. It leverages the Anthropic...

### [Compare Different LLM Responses Side-by-Side with Google Sheets](https://n8n.io/workflows/3711-compare-different-llm-responses-side-by-side-with-google-she)
- **ID:** 3711 | **Creator:** @dataki ✓ | **Views:** 1,197 | **Nodes:** 5
- **Nodes:** Google Sheets, AI Agent, Simple Memory +2 more
- This workflow allows you to easily evaluate and compare the outputs of two language models (LLMs) before choosing one for production.

In the chat interface, both model outputs are shown side by side....

### [Pattern for Multiple Triggers Combined to Continue Workflow](https://n8n.io/workflows/2857-pattern-for-multiple-triggers-combined-to-continue-workflow)
- **ID:** 2857 | **Creator:** @hubschrauber ✓ | **Views:** 1,190 | **Nodes:** 1
- **Nodes:** HTTP Request
- Overview

This template describes a possible approach to handle a pseudo-callback/trigger from an independent, external process (initiated from a workflow) and combine the received input with the work...

### [Sum or aggregate a column of spreadsheet or table data](https://n8n.io/workflows/1497-sum-or-aggregate-a-column-of-spreadsheet-or-table-data)
- **ID:** 1497 | **Creator:** @maxt ✓ | **Views:** 1,148 | **Nodes:** 0
- **Nodes:** 
- This workflow shows how to sum multiple items of data, like you would in Excel or Airtable when summing up the total of a column. It uses a Function node with some javascript to perform the aggregatio...

### [🥇 Token Estim8r -Sub Workflow to track AI Model Token Usage and cost with JinaAI](https://n8n.io/workflows/3513-token-estim8r-sub-workflow-to-track-ai-model-token-usage-a)
- **ID:** 3513 | **Creator:** @joeperes ✓ | **Views:** 1,129 | **Nodes:** 3
- **Nodes:** Google Sheets, HTTP Request, Code
- Save Your Tokens from Evil King Browser
&gt; Image Generated with ideoGener8r 
n8n workflow template
🔍 Estimate token usage and AI model cost from any workflow in n8n

🙋‍♂️ Who is this for?
This work...

### [Create a table, and insert and update data in the table in Snowflake](https://n8n.io/workflows/824-create-a-table-and-insert-and-update-data-in-the-table-in-sn)
- **ID:** 824 | **Creator:** @harshil1712 ✓ | **Views:** 1,127 | **Nodes:** 1
- **Nodes:** Snowflake

### [Collect and label images and send to Google Sheets](https://n8n.io/workflows/1401-collect-and-label-images-and-send-to-google-sheets)
- **ID:** 1401 | **Creator:** @lorenanda ✓ | **Views:** 1,122 | **Nodes:** 3
- **Nodes:** Google Sheets, HTTP Request, AWS Rekognition
- This workflow collects images from web search on a specific query, detects labels in them, and stores this information in a Google Sheet.

### [Enhance Security Operations with the Qualys Slack Shortcut Bot!](https://n8n.io/workflows/2510-enhance-security-operations-with-the-qualys-slack-shortcut-b)
- **ID:** 2510 | **Creator:** @djangelic ✓ | **Views:** 1,116 | **Nodes:** 1
- **Nodes:** HTTP Request
- Enhance Security Operations with the Qualys Slack Shortcut Bot!

Our Qualys Slack Shortcut Bot is strategically designed to facilitate immediate security operations directly from Slack. This powerful...

### [Get Daily Weather and Save It in Airtable](https://n8n.io/workflows/2730-get-daily-weather-and-save-it-in-airtable)
- **ID:** 2730 | **Creator:** @weblineindia ✓ | **Views:** 1,099 | **Nodes:** 2
- **Nodes:** Airtable, HTTP Request
- This smart automation workflow created by the AI development team at WeblineIndia, helps with the daily collection and storage of weather data. Using the OpenWeatherMap API and Airtable, this solution...

### [Automatic Workflow & Credentials Backup to GitHub with Change Detection](https://n8n.io/workflows/4609-automatic-workflow-and-credentials-backup-to-github-with-cha)
- **ID:** 4609 | **Creator:** @hamed-nickmehr | **Views:** 1,097 | **Nodes:** 2
- **Nodes:** GitHub, Crypto
- This n8n workflow template uses community nodes and is only compatible with the self-hosted version of n8n. 

Title: n8n Credentials and Workflows Backup on Change Detection

Purpose:
Never lose track...

### [Elastic Alert Notification via Microsoft Graph API](https://n8n.io/workflows/2523-elastic-alert-notification-via-microsoft-graph-api)
- **ID:** 2523 | **Creator:** @autom8r ✓ | **Views:** 1,082 | **Nodes:** 1
- **Nodes:** HTTP Request
- Who is this template for?

This template is for teams and administrators who use n8n to monitor Elastic alerts and want to receive automated email notifications when an alert is triggered. It leverage...

### [Qualys Scan Slack Report Subworkflow](https://n8n.io/workflows/2512-qualys-scan-slack-report-subworkflow)
- **ID:** 2512 | **Creator:** @djangelic ✓ | **Views:** 1,054 | **Nodes:** 2
- **Nodes:** HTTP Request, Slack
- Introducing the Qualys Scan Slack Report Subworkflow—a robust solution designed to automate the generation and retrieval of security reports from the Qualys API.

This workflow is a sub workflow of th...

### [Loading JSON via FTP to Qdrant Vector Database Embedding Pipeline](https://n8n.io/workflows/3495-loading-json-via-ftp-to-qdrant-vector-database-embedding-pip)
- **ID:** 3495 | **Creator:** @gsirawan | **Views:** 1,049 | **Nodes:** 5
- **Nodes:** FTP, Embeddings OpenAI, Character Text Splitter +2 more
- 🧠 This workflow is designed for one purpose only, to bulk-upload structured JSON articles from an FTP server into a Qdrant vector database for use in LLM-powered semantic search, RAG systems, or AI as...

### [MCP Server with AI Agent as a Tool Context Reducer](https://n8n.io/workflows/4475-mcp-server-with-ai-agent-as-a-tool-context-reducer)
- **ID:** 4475 | **Creator:** @fibonacci | **Views:** 1,046 | **Nodes:** 5
- **Nodes:** AI Agent, OpenAI Chat Model, Simple Memory +2 more
- Overview

Transform your LLM into a powerful GitHub automation specialist with this n8n workflow template. In a world where multiple MCP servers can overwhelm LLMs with context, this streamlined solut...

### [Automated lead generation & qualification with Google Maps, GPT-4 & HubSpot](https://n8n.io/workflows/4824-automated-lead-generation-and-qualification-with-google-maps)
- **ID:** 4824 | **Creator:** @dae221 ✓ | **Views:** 1,043 | **Nodes:** 6
- **Nodes:** Google Sheets, HTTP Request, Slack +3 more
- 🚀 AI Lead Machine Pro: Google Maps → Slack → HubSpot → $$$

This n8n workflow automates end-to-end lead generation, from scraping local businesses to qualifying and sending high-quality prospects dire...

### [Backup Workflows to Git Repository on Gitea](https://n8n.io/workflows/2820-backup-workflows-to-git-repository-on-gitea)
- **ID:** 2820 | **Creator:** @octoleo | **Views:** 1,032 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- Overview
This workflow automates the backup of all workflows from your system to a Git repository hosted on Gitea. It runs on a scheduled trigger, fetching, encoding, and committing workflow data, ens...

### [Watchdog: Update All Workflows With Default Error Workflow](https://n8n.io/workflows/2169-watchdog-update-all-workflows-with-default-error-workflow)
- **ID:** 2169 | **Creator:** @dkindlund | **Views:** 1,026 | **Nodes:** 1
- **Nodes:** Postgres
- Do you consistently forget to set a Default Error Workflow when creating new workflows?  Then this helper workflow is for you!

When activated, this helper workflow will:
Scan ALL other workflows ever...

### [Backup n8n Workflows to Bitbucket](https://n8n.io/workflows/2787-backup-n8n-workflows-to-bitbucket)
- **ID:** 2787 | **Creator:** @garethbdavies ✓ | **Views:** 1,020 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- An automated backup solution designed for self-hosted n8n users to automatically backup their workflows to Bitbucket, leveraging Bitbucket's free private repository offering.

Perfect for maintaining...

### [Send notification when deployment fails](https://n8n.io/workflows/1255-send-notification-when-deployment-fails)
- **ID:** 1255 | **Creator:** @harshil1712 ✓ | **Views:** 1,011 | **Nodes:** 1
- **Nodes:** Slack
- This workflow sends a message on Slack when site deployment fails.



Netlify Trigger node: This node triggers the workflow when the site deployment fails.

Slack node: This node sends a message on Sl...

### [Multi-Channel Workflow Error Alerts with Telegram, Gmail & Messaging Apps](https://n8n.io/workflows/5629-multi-channel-workflow-error-alerts-with-telegram-gmail-and)
- **ID:** 5629 | **Creator:** @khmuhtadin ✓ | **Views:** 1,010 | **Nodes:** 6
- **Nodes:** Slack, Telegram, Discord +3 more
- The Error Notification workflow is designed to instantly notify you whenever any other n8n workflow encounters an error, using popular communication channels like Telegram and Gmail—with optional supp...

### [Auto Workflow Backup to Google Drive – Automated Export of All Your Workflows](https://n8n.io/workflows/4090-auto-workflow-backup-to-google-drive-automated-export-of-al)
- **ID:** 4090 | **Creator:** @lukaszb ✓ | **Views:** 1,004 | **Nodes:** 1
- **Nodes:** Google Drive
- n8n Workflow Backup to Google Drive – Automated Export of All Your Workflows

This workflow is designed to automatically create backups of all your workflows in n8n and store them as individual .json...

### [Receive updates for the position of the ISS and push it to a Firbase](https://n8n.io/workflows/787-receive-updates-for-the-position-of-the-iss-and-push-it-to-a)
- **ID:** 787 | **Creator:** @harshil1712 ✓ | **Views:** 978 | **Nodes:** 2
- **Nodes:** HTTP Request, Google Cloud Realtime Database
- 

### [OpenAI Responses API Adapter for LLM and AI Agent Workflows](https://n8n.io/workflows/4218-openai-responses-api-adapter-for-llm-and-ai-agent-workflows)
- **ID:** 4218 | **Creator:** @jimleuk ✓ | **Views:** 974 | **Nodes:** 4
- **Nodes:** HTTP Request, Code, AI Agent +1 more
- This n8n template demonstrates how to use OpenAI's Responses API with existing LLM and AI Agent nodes.

Though I would recommend just waiting for official support, if you're impatient and would like a...

### [Save Qualys Reports to TheHive](https://n8n.io/workflows/2531-save-qualys-reports-to-thehive)
- **ID:** 2531 | **Creator:** @djangelic ✓ | **Views:** 971 | **Nodes:** 2
- **Nodes:** HTTP Request, TheHive 5
- Automate Report Generation with n8n & Qualys

Introducing the Save Qualys Reports to TheHive Workflow—a robust solution designed to automate the retrieval and storage of Qualys reports in TheHive.

T...

### [🛠️ TheHive Tool MCP Server](https://n8n.io/workflows/5365-thehive-tool-mcp-server)
- **ID:** 5365 | **Creator:** @cfomodz ✓ | **Views:** 960 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing all TheHive Tool operations to...

### [Track CVE Vulnerability Details & History with NVD API and Google Sheets](https://n8n.io/workflows/4797-track-cve-vulnerability-details-and-history-with-nvd-api-and)
- **ID:** 4797 | **Creator:** @niranjan ✓ | **Views:** 949 | **Nodes:** 3
- **Nodes:** Google Sheets, HTTP Request, Code
- Who is this for?

NVD (National Vulnerability Database) data is essential for security analysts, vulnerability managers, and DevSecOps professionals who need to perform both CVE lookups and monitor hi...

### [Venafi Cloud Slack Cert Bot](https://n8n.io/workflows/2422-venafi-cloud-slack-cert-bot)
- **ID:** 2422 | **Creator:** @djangelic ✓ | **Views:** 944 | **Nodes:** 4
- **Nodes:** HTTP Request, Slack, Venafi TLS Protect Cloud +1 more
- Enhance Security Operations with the Venafi Slack CertBot!

Venafi Presentation  - Watch Video

Our Venafi Slack CertBot is strategically designed to facilitate immediate security operations directly...

### [Watchdog: Auto Resume Workflows](https://n8n.io/workflows/2166-watchdog-auto-resume-workflows)
- **ID:** 2166 | **Creator:** @dkindlund | **Views:** 917 | **Nodes:** 0
- **Nodes:** 
- If you have multiple users managing workflows, there may come a time where a user “accidentally” turns off a workflow. Or, if you have workflows that automatically turn off other workflows, that code...

### [Access Control for AI Agents (RBAC) using Airtable and Telegram](https://n8n.io/workflows/3988-access-control-for-ai-agents-rbac-using-airtable-and-telegra)
- **ID:** 3988 | **Creator:** @octionic ✓ | **Views:** 914 | **Nodes:** 11
- **Nodes:** Airtable, Telegram, AI Agent +8 more
- Purpose

This workflow allows granular control over the access to tools connected to AI Agents (including Multi-Agent setups) using Role Based Access Control.

Demo & Explanation

How it works

User p...

### [Receive updates when an event occurs in TheHive](https://n8n.io/workflows/810-receive-updates-when-an-event-occurs-in-thehive)
- **ID:** 810 | **Creator:** @harshil1712 ✓ | **Views:** 892 | **Nodes:** 0
- **Nodes:** 

### [Manage incident reporting in PagerDuty and CrateDB](https://n8n.io/workflows/609-manage-incident-reporting-in-pagerduty-and-cratedb)
- **ID:** 609 | **Creator:** @harshil1712 ✓ | **Views:** 888 | **Nodes:** 2
- **Nodes:** PagerDuty, CrateDB
- This workflow automatically monitors the functionality of a factory. The workflow logs machine data coming from factory sensors in a CrateDB database, generates an incident report in PagerDuty, and no...

### [Subscribe to new releases of a Github repository via Gmail](https://n8n.io/workflows/2278-subscribe-to-new-releases-of-a-github-repository-via-gmail)
- **ID:** 2278 | **Creator:** @riascho ✓ | **Views:** 882 | **Nodes:** 2
- **Nodes:** HTTP Request, Gmail
- This is a very simple workflow that lets you subscribe to any github repository for the latest release (using n8n as example).

How it works: 
daily poll to Github repository for release for latest (...

### [IOT device control with MQTT and webhook](https://n8n.io/workflows/4211-iot-device-control-with-mqtt-and-webhook)
- **ID:** 4211 | **Creator:** @tduffy | **Views:** 867 | **Nodes:** 1
- **Nodes:** MQTT
- . 

IOT device control with MQTT and webhook


This workflow is for users wanting a practical example of how to control IOT systems using the MQTT protocol in an an n8n environment.

The template prov...

### [Push your public IP to Namecheaps Dynamic DNS](https://n8n.io/workflows/1576-push-your-public-ip-to-namecheaps-dynamic-dns)
- **ID:** 1576 | **Creator:** @mariosemes | **Views:** 855 | **Nodes:** 1
- **Nodes:** HTTP Request
- Template to get your public IP address and push it to Namecheaps Dynamic DNS per subdomain.

Open "yourdomain.com"
Insert your domain and your Namecheap DDNS password
Open "subdomains"
Replaces and in...

### [Sync GitHub Workflows to n8n After Pull Request Merges](https://n8n.io/workflows/4500-sync-github-workflows-to-n8n-after-pull-request-merges)
- **ID:** 4500 | **Creator:** @duynb ✓ | **Views:** 844 | **Nodes:** 2
- **Nodes:** GitHub, HTTP Request
- Who is this for?

This template is ideal for developers, DevOps engineers, and automation managers who manage their n8n workflows using GitHub. It helps teams streamline their CI/CD automation by sync...

### [Summarize Microsoft 365 Outage Alerts with ChatGPT and Send to Slack](https://n8n.io/workflows/3353-summarize-microsoft-365-outage-alerts-with-chatgpt-and-send)
- **ID:** 3353 | **Creator:** @ozskywalker | **Views:** 835 | **Nodes:** 4
- **Nodes:** Slack, Microsoft Outlook, Code +1 more
- Built this for a dedicated Slack outage-notifications channel — works well on both desktop and mobile.

This is for:

IT Administrators & small MSPs looking to streamline M365 alerts from one or multi...

### [Automatically document and backup N8N workflows](https://n8n.io/workflows/3354-automatically-document-and-backup-n8n-workflows)
- **ID:** 3354 | **Creator:** @ozskywalker | **Views:** 824 | **Nodes:** 5
- **Nodes:** GitHub, HTTP Request, Slack +2 more
- Automatically backs up your workflows to Github and generates documentation in a Notion database.

Weekly run, uses the "internal-infra" tag to look for new or recently modified workflows
Uses a Notio...

### [Build an MCP Server which answers questions with Retrieval Augmented Generation](https://n8n.io/workflows/5403-build-an-mcp-server-which-answers-questions-with-retrieval-a)
- **ID:** 5403 | **Creator:** @thomasjanssen-tech ✓ | **Views:** 819 | **Nodes:** 3
- **Nodes:** Default Data Loader, Qdrant Vector Store, Embeddings Ollama
- Build an MCP Server which has access to a semantic database to perform Retrieval Augmented Generation (RAG)

Tutorial

Click here to watch the full tutorial on YouTube

How it works
This MCP Server ha...

### [v1 helper - Find params with affected expressions](https://n8n.io/workflows/1929-v1-helper-find-params-with-affected-expressions)
- **ID:** 1929 | **Creator:** @n8n-team ✓ | **Views:** 806 | **Nodes:** 1
- **Nodes:** Code
- v1 Helper

ℹ️ This workflow is to be run after upgrading to n8n v1.

This workflow returns all locations where a node in an active workflow contains a parameter using an expression extension affected...

### [Import Productboard Notes, Companies and Features into Snowflake](https://n8n.io/workflows/2576-import-productboard-notes-companies-and-features-into-snowfl)
- **ID:** 2576 | **Creator:** @rjouhann ✓ | **Views:** 792 | **Nodes:** 3
- **Nodes:** HTTP Request, Slack, Snowflake
- This workflow imports Productboard data into Snowflake, automating data extraction, mapping, and updates for features, companies, and notes. It supports scheduled weekly updates, data cleansing, and S...

### [PostgreSQL Conversational Agent with Claude & DeepSeek (Multi-KPI, Secure)](https://n8n.io/workflows/3892-postgresql-conversational-agent-with-claude-and-deepseek-mul)
- **ID:** 3892 | **Creator:** @hippolyte-hu ✓ | **Views:** 789 | **Nodes:** 7
- **Nodes:** Postgres, AI Agent, Anthropic Chat Model +4 more
- 🧠 Conversational PostgreSQL Agent 

Enable AI-driven conversations with your PostgreSQL database using a secure and visual-free agent powered by n8n’s Model Context Protocol (MCP). This template allow...

### [Access data from bubble application](https://n8n.io/workflows/879-access-data-from-bubble-application)
- **ID:** 879 | **Creator:** @tephlon ✓ | **Views:** 783 | **Nodes:** 1
- **Nodes:** HTTP Request
- This is a proof of concept workflow showing how you would connect n8n to a Bubble data collection.

### [Push Multiple Files to GitHub Repository via Github REST API](https://n8n.io/workflows/3308-push-multiple-files-to-github-repository-via-github-rest-api)
- **ID:** 3308 | **Creator:** @customworkflowsai ✓ | **Views:** 760 | **Nodes:** 1
- **Nodes:** HTTP Request
- Introduction
This workflow offers a streamlined solution for uploading multiple files to a GitHub repository simultaneously using GitHub's REST API. It addresses a significant limitation of n8n's nati...

### [Track LLM Token Costs per Customer Using the Langchain Code Node ](https://n8n.io/workflows/3440-track-llm-token-costs-per-customer-using-the-langchain-code)
- **ID:** 3440 | **Creator:** @jimleuk ✓ | **Views:** 760 | **Nodes:** 4
- **Nodes:** Google Sheets, Gmail, LangChain Code +1 more
- Note: This template only works for self-hosted n8n.

This n8n template demonstrates how to use the Langchain code node to track token usage and cost for every LLM call.

This is useful if your templ...

### [Remote IOT Sensor monitoring via MQTT and InfluxDB](https://n8n.io/workflows/4004-remote-iot-sensor-monitoring-via-mqtt-and-influxdb)
- **ID:** 4004 | **Creator:** @tduffy | **Views:** 759 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- . 

Read and store IOT sensor data with the MQTT Trigger and InfluxDB

tonyduffy@protonmail.com


This workflow is for users wanting a practical example of how to obtain data from remote IOT systems u...

### [Receive messages for an ActiveMQ queue](https://n8n.io/workflows/513-receive-messages-for-an-activemq-queue)
- **ID:** 513 | **Creator:** @tanay1337 ✓ | **Views:** 759 | **Nodes:** 0
- **Nodes:** 

### [Discover Hidden Website API Endpoints Using Regex and AI](https://n8n.io/workflows/4627-discover-hidden-website-api-endpoints-using-regex-and-ai)
- **ID:** 4627 | **Creator:** @yulia ✓ | **Views:** 752 | **Nodes:** 7
- **Nodes:** HTTP Request, HTML, AI Agent +4 more
- 💡 What it is for

This workflow helps to automatically discover undocumented API endpoints by analysing JavaScript files from the website's HTML code.

When building automation for platforms without p...

### [Automatically update n8n version](https://n8n.io/workflows/4335-automatically-update-n8n-version)
- **ID:** 4335 | **Creator:** @lun | **Views:** 745 | **Nodes:** 1
- **Nodes:** HTTP Request
- 🔄 n8n Workflow: Check and Update n8n Version

This workflow automatically checks if the local n8n version is outdated and, if so, creates a file to signal an update is needed.

🖥️ Working Environment...

### [Automated Daily Backup of n8n Workflows to GitLab Repositories](https://n8n.io/workflows/4035-automated-daily-backup-of-n8n-workflows-to-gitlab-repositori)
- **ID:** 4035 | **Creator:** @akhilv7 ✓ | **Views:** 731 | **Nodes:** 2
- **Nodes:** GitLab, Code
- n8n Workflow: Sync Workflows with GitLab

How It Works

This workflow ensures that your self-hosted n8n workflows are version-controlled in a GitLab repository. It compares each current workflow from...

### [Paul Graham Essay Search & Chat with Milvus Vector Database](https://n8n.io/workflows/3576-paul-graham-essay-search-and-chat-with-milvus-vector-databas)
- **ID:** 3576 | **Creator:** @zc277584121 ✓ | **Views:** 731 | **Nodes:** 8
- **Nodes:** HTTP Request, HTML, AI Agent +5 more
- Paul Graham Essay Search & Chat with Milvus Vector Database
How It Works

This workflow creates a RAG (Retrieval-Augmented Generation) system using Milvus vector database to search Paul Graham essays:...

### [Backup N8N Workflows to Github](https://n8n.io/workflows/3990-backup-n8n-workflows-to-github)
- **ID:** 3990 | **Creator:** @datproto | **Views:** 684 | **Nodes:** 3
- **Nodes:** GitHub, Discord, Code
- Introduction
This workflow will backup all of your existed workflows to a single Github repository.

The Backup folders' name are based on the current backup date and have default format: "yyyy/MM/dd"...

### [Get contributors information from GitHub in Slack](https://n8n.io/workflows/563-get-contributors-information-from-github-in-slack)
- **ID:** 563 | **Creator:** @harshil1712 ✓ | **Views:** 677 | **Nodes:** 2
- **Nodes:** Slack, GraphQL
- Get your contributors GitHub information with a slash command in your Slack Workspace.

### [Get a pipeline in CircleCI](https://n8n.io/workflows/454-get-a-pipeline-in-circleci)
- **ID:** 454 | **Creator:** @tanay1337 ✓ | **Views:** 673 | **Nodes:** 1
- **Nodes:** CircleCI

### [Website Downtime Alert via LINE + Supabase Log](https://n8n.io/workflows/4379-website-downtime-alert-via-line-supabase-log)
- **ID:** 4379 | **Creator:** @sayamol | **Views:** 671 | **Nodes:** 6
- **Nodes:** HTTP Request, UptimeRobot, Supabase +3 more
- This workflow automatically checks the status of your websites using UptimeRobot API. If any site is down or unstable, it will:
Generate a natural-language alert message using GPT-4o
Push the message...

### [Get the community profile of a repository](https://n8n.io/workflows/450-get-the-community-profile-of-a-repository)
- **ID:** 450 | **Creator:** @shraddha ✓ | **Views:** 669 | **Nodes:** 1
- **Nodes:** GitHub

### [Create a Paul Graham Essay Q&A System with OpenAI and Milvus Vector Database](https://n8n.io/workflows/3574-create-a-paul-graham-essay-qanda-system-with-openai-and-milv)
- **ID:** 3574 | **Creator:** @zc277584121 ✓ | **Views:** 661 | **Nodes:** 9
- **Nodes:** HTTP Request, HTML, Question and Answer Chain +6 more
- Create a Paul Graham Essay Q&A System with OpenAI and Milvus Vector Database
How It Works

This workflow creates a question-answering system based on Paul Graham essays. It has two main steps:

Data C...

### [Security Reconnaissance with Google Dorks, Parsera Scraping, and Gmail Reports](https://n8n.io/workflows/5980-security-reconnaissance-with-google-dorks-parsera-scraping-a)
- **ID:** 5980 | **Creator:** @knute ✓ | **Views:** 657 | **Nodes:** 2
- **Nodes:** Gmail, Code
- This workflow contains community nodes that are only compatible with the self-hosted version of n8n.

How it Works:
- Accepts a domain from a web form
- Generates a list of Google dorks targeting that...

### [Send location updates of the ISS every minute to a queue in AWS SQS](https://n8n.io/workflows/1047-send-location-updates-of-the-iss-every-minute-to-a-queue-in)
- **ID:** 1047 | **Creator:** @harshil1712 ✓ | **Views:** 656 | **Nodes:** 2
- **Nodes:** HTTP Request, AWS SQS
- This workflow allows you to send position updates of the ISS every minute to a queue using the AWS SQS node.



Cron node: The Cron node will trigger the workflow every minute.

HTTP Request node: Thi...

### [Evaluate RAG Response Accuracy with OpenAI: Document Groundedness Metric](https://n8n.io/workflows/4426-evaluate-rag-response-accuracy-with-openai-document-grounded)
- **ID:** 4426 | **Creator:** @jimleuk ✓ | **Views:** 638 | **Nodes:** 10
- **Nodes:** HTTP Request, AI Agent, Basic LLM Chain +7 more
- This n8n template demonstrates how to calculate the evaluation metric "RAG document groundedness" which in this scenario, measures the ability to provide or reference information included only in retr...

### [Intelligent Web & Local Search with Brave Search API and Google Gemini MCP Server](https://n8n.io/workflows/4559-intelligent-web-and-local-search-with-brave-search-api-and-g)
- **ID:** 4559 | **Creator:** @jez ✓ | **Views:** 634 | **Nodes:** 4
- **Nodes:** AI Agent, Simple Memory, Call n8n Workflow Tool +1 more
- Summary
This n8n workflow implements an AI-powered agent that intelligently uses the Brave Search API (via an external MCP service like Smithery) to perform both web and local searches. It understands...

### [Fetch Scriptures Dynamically from get Bible API](https://n8n.io/workflows/2818-fetch-scriptures-dynamically-from-get-bible-api)
- **ID:** 2818 | **Creator:** @christian | **Views:** 628 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- Overview
The Get Bible Query Workflow is a modular and self-standing workflow designed to retrieve scriptures dynamically based on structured input. It serves as an intermediary layer that extracts re...

### [Get all releases in Sentry](https://n8n.io/workflows/643-get-all-releases-in-sentry)
- **ID:** 643 | **Creator:** @harshil1712 ✓ | **Views:** 613 | **Nodes:** 1
- **Nodes:** Sentry.io

### [Send structured logs to BetterStack from any workflow using HTTP Request](https://n8n.io/workflows/3400-send-structured-logs-to-betterstack-from-any-workflow-using)
- **ID:** 3400 | **Creator:** @xqus ✓ | **Views:** 581 | **Nodes:** 1
- **Nodes:** HTTP Request
- Send structured logs to BetterStack from any workflow using HTTP Request

Who is this for?

This workflow is perfect for automation builders, developers, and DevOps teams using n8n who want to send st...

### [Automated SSL Certificate Monitoring and Renewal with Notion and Telegram](https://n8n.io/workflows/4973-automated-ssl-certificate-monitoring-and-renewal-with-notion)
- **ID:** 4973 | **Creator:** @frankchen | **Views:** 576 | **Nodes:** 4
- **Nodes:** HTTP Request, Telegram, Notion +1 more
- Automatically fetch existing domains from Notion's Database and verify the validity of SSL certificates through SSL-Checker. If the validity period is less than 14 days, send a Telegram message notifi...

### [Track n8n Workflow Changes Over Time with Compare Dataset & Google Sheets](https://n8n.io/workflows/5013-track-n8n-workflow-changes-over-time-with-compare-dataset-an)
- **ID:** 5013 | **Creator:** @jimleuk ✓ | **Views:** 573 | **Nodes:** 1
- **Nodes:** Google Sheets
- This n8n template runs daily to track and report on any changes made to workflows  on any n8n instance.

Useful if a team is working within a single instance and you want to be notified of what workfl...

### [Process Multiple Prompts in Parallel with Azure OpenAI Batch API](https://n8n.io/workflows/3537-process-multiple-prompts-in-parallel-with-azure-openai-batch)
- **ID:** 3537 | **Creator:** @greg ✓ | **Views:** 572 | **Nodes:** 4
- **Nodes:** HTTP Request, Code, Simple Memory +1 more
- Process Multiple Prompts in Parallel with Azure OpenAI Batch API

Who is this for?
This workflow is designed for developers and data scientists who want to efficiently send multiple prompts to the Azu...

### [Lookup IP Geolocation Details with IP-API.com via Webhook](https://n8n.io/workflows/4599-lookup-ip-geolocation-details-with-ip-apicom-via-webhook)
- **ID:** 4599 | **Creator:** @ist00dent ✓ | **Views:** 563 | **Nodes:** 1
- **Nodes:** HTTP Request
- This n8n template enables you to instantly retrieve detailed geolocation information for any given IP address by simply sending a webhook request. Leverage the power of IP-API.com to gain insights int...

### [Automatic Jest Test Generation for GitHub PRs with Dual AI Review](https://n8n.io/workflows/4013-automatic-jest-test-generation-for-github-prs-with-dual-ai-r)
- **ID:** 4013 | **Creator:** @varritech ✓ | **Views:** 553 | **Nodes:** 6
- **Nodes:** GitHub, HTTP Request, Code +3 more
- Workflow: Automatic Unit Test Creator from GitHub

🏗️ Architecture Overview
This workflow listens for GitHub pull-request events, analyzes changed React/TypeScript files, auto-generates Jest tests via...

### [Run Apache Airflow DAG and Retrieve XCom Value](https://n8n.io/workflows/3026-run-apache-airflow-dag-and-retrieve-xcom-value)
- **ID:** 3026 | **Creator:** @windoac | **Views:** 548 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- Run Apache Airflow DAG and Retrieve XCom Value

What this workflow does

This workflow integrates the Apache Airflow API DAGRun and XCom. It enables n8n to trigger Airflow DAGs and retrieve the execut...

### [Generate and queue factory sensor data in AMQP](https://n8n.io/workflows/608-generate-and-queue-factory-sensor-data-in-amqp)
- **ID:** 608 | **Creator:** @harshil1712 ✓ | **Views:** 516 | **Nodes:** 1
- **Nodes:** AMQP Sender
- This workflow generates sensor data, which is used in another workflow for managing factory incident reports.

Read more about this use case and how to build both workflows with step-by-step instructi...

### [💾 Backup Automation for n8n Workflows to Google Drive (Daily or Manual)](https://n8n.io/workflows/3918-backup-automation-for-n8n-workflows-to-google-drive-daily-o)
- **ID:** 3918 | **Creator:** @amanda ✓ | **Views:** 511 | **Nodes:** 1
- **Nodes:** Google Drive
- 💾 Backup Automation for n8n Workflows to Google Drive – No Risk, No Stress

Hi! I’m Amanda,
I build automation workflows for n8n and Make.  
This ready-to-use workflow is designed to automatically exp...

### [Monitor SSL Certificate Expiry with Google Sheets and Email Alerts](https://n8n.io/workflows/5768-monitor-ssl-certificate-expiry-with-google-sheets-and-email)
- **ID:** 5768 | **Creator:** @agusnarestha | **Views:** 511 | **Nodes:** 4
- **Nodes:** Send Email, Google Sheets, HTTP Request +1 more
- 🔒 SSL Certificate Monitoring & Expiry Alert with Spreadsheet [FREE APIs]

✅ What This Workflow Does

This n8n template automatically monitors SSL certificates of websites listed in a Google Sheet and...

### [New TheHive Case Slack Notification Bot](https://n8n.io/workflows/2577-new-thehive-case-slack-notification-bot)
- **ID:** 2577 | **Creator:** @djangelic ✓ | **Views:** 510 | **Nodes:** 3
- **Nodes:** HTTP Request, Slack, TheHive 5
- Streamline Case Management in TheHive via Slack!

Our TheHive Slack Integration empowers SOC analysts by allowing them to efficiently manage and update case attributes directly within Slack, reducing...

### [AI-Powered Knowledge Assistant using Google Sheets, OpenAI, and Supabase Vector Search](https://n8n.io/workflows/4477-ai-powered-knowledge-assistant-using-google-sheets-openai-an)
- **ID:** 4477 | **Creator:** @akhilv7 ✓ | **Views:** 510 | **Nodes:** 6
- **Nodes:** HTTP Request, Gmail, Code +3 more
- AI-Powered GitHub Commit Reviewer

Overview

Workflow Name: AI-Powered GitHub Commit Reviewer  
Author: Akhil  
Purpose: This n8n workflow triggers on a GitHub push event, fetches commit diffs, format...

### [Secure API Endpoint with Bearer Token Authentication and Field Validation](https://n8n.io/workflows/3970-secure-api-endpoint-with-bearer-token-authentication-and-fie)
- **ID:** 3970 | **Creator:** @xqus ✓ | **Views:** 509 | **Nodes:** 1
- **Nodes:** Code
- A reusable and production-ready n8n workflow that secures public webhooks using Bearer Token authentication and dynamic request validation.

✨ What It Does

Verifies Bearer Token**  
  Compares the Au...

### [Scheduled Workflow Backups from n8n to Google Drive with Auto Cleanup](https://n8n.io/workflows/4515-scheduled-workflow-backups-from-n8n-to-google-drive-with-aut)
- **ID:** 4515 | **Creator:** @danielng ✓ | **Views:** 508 | **Nodes:** 1
- **Nodes:** Google Drive
- Auto Backup n8n Workflows to Google Drive

Imagine the sinking feeling: hours, weeks, or even months of meticulous work building your n8n workflows, suddenly gone. A server crash, an accidental deleti...

### [JSON String Validator via Webhook](https://n8n.io/workflows/4704-json-string-validator-via-webhook)
- **ID:** 4704 | **Creator:** @ist00dent ✓ | **Views:** 500 | **Nodes:** 1
- **Nodes:** Code
- This n8n template provides a simple yet powerful utility for validating if a given string input is a valid JSON format. You can use this to pre-validate data received from external sources, ensure dat...

### [Trigger a build using the TravisCI node](https://n8n.io/workflows/658-trigger-a-build-using-the-travisci-node)
- **ID:** 658 | **Creator:** @harshil1712 ✓ | **Views:** 498 | **Nodes:** 1
- **Nodes:** TravisCI

### [Evaluation Metric: Summarization](https://n8n.io/workflows/4428-evaluation-metric-summarization)
- **ID:** 4428 | **Creator:** @jimleuk ✓ | **Views:** 496 | **Nodes:** 6
- **Nodes:** Google Drive, Basic LLM Chain, OpenAI Chat Model +3 more
- This n8n template demonstrates how to calculate the evaluation metric "Summarization" which in this scenario, measures the LLM's accuracy and faithfulness in producing summaries which are based on an...

### [Receive updates of the position of the ISS and add it to a table in TimescaleDB](https://n8n.io/workflows/917-receive-updates-of-the-position-of-the-iss-and-add-it-to-a-t)
- **ID:** 917 | **Creator:** @harshil1712 ✓ | **Views:** 482 | **Nodes:** 2
- **Nodes:** HTTP Request, TimescaleDB
- This workflow allows you to receive updates about the positiong of the ISS and add it to a table in TimescaleDB.



Cron node: The Cron node triggers the workflow every minute. You can configure the t...

### [Automate n8n User Invitations from a Google Spreadsheet](https://n8n.io/workflows/3233-automate-n8n-user-invitations-from-a-google-spreadsheet)
- **ID:** 3233 | **Creator:** @bangank36 ✓ | **Views:** 470 | **Nodes:** 3
- **Nodes:** Google Sheets, HTTP Request, Code
- This workflow retrieves all users from n8n, compares them against entries in a Google Sheets spreadsheet, and automatically creates new users when needed.  

Once new users are created, invitation ema...

### [AI Agent that updates its own rules to modify behavior](https://n8n.io/workflows/4694-ai-agent-that-updates-its-own-rules-to-modify-behavior)
- **ID:** 4694 | **Creator:** @giosegar ✓ | **Views:** 468 | **Nodes:** 5
- **Nodes:** Google Sheets, Postgres, AI Agent +2 more
- Video walkthrough

https://www.youtube.com/watch?v=OwIFK-r-NtQ

Summary of agent
This agent can write and rewrite its own rules, allowing you to mold its behavior. It receives rules from a database as...

### [Backup Clockify to Github based on monthly reports](https://n8n.io/workflows/3147-backup-clockify-to-github-based-on-monthly-reports)
- **ID:** 3147 | **Creator:** @octionic ✓ | **Views:** 465 | **Nodes:** 3
- **Nodes:** GitHub, HTTP Request, Clockify
- Purpose

This workflow creates a versioned backup of an entire Clockify workspace split up into monthly reports.

How it works

This backup routine runs daily by default
The Clockify reports API endpo...

### [📊 AI Token Tracker for WhatsApp & Telegram – Save AI Usage to Google Sheets](https://n8n.io/workflows/3963-ai-token-tracker-for-whatsapp-and-telegram-save-ai-usage-t)
- **ID:** 3963 | **Creator:** @amanda ✓ | **Views:** 464 | **Nodes:** 7
- **Nodes:** Google Sheets, HTTP Request, Telegram +4 more
- 💸 GPT-4o Token Tracker – Measure AI Usage and Cost via WhatsApp or Telegram

Hi! I'm Amanda — I create smart, useful AI automations for n8n and Make.  
This workflow helps you monitor how many tokens...

### [Query-to-Action Automation with Bright Data MCP & OpenAI GPT](https://n8n.io/workflows/4077-query-to-action-automation-with-bright-data-mcp-and-openai-g)
- **ID:** 4077 | **Creator:** @cngaspar ✓ | **Views:** 462 | **Nodes:** 6
- **Nodes:** AI Agent, OpenAI Chat Model, Simple Memory +3 more
- 📌 AI Agent Template with Bright Data MCP Tool Integration

This template obtains all the possible tools from Bright Data MCP, process this through chatbot, then run any tool based on the user's query...

### [Auto Update n8n to Latest Version with Coolify](https://n8n.io/workflows/4360-auto-update-n8n-to-latest-version-with-coolify)
- **ID:** 4360 | **Creator:** @gemboran | **Views:** 453 | **Nodes:** 1
- **Nodes:** HTTP Request
- Automatically detect new n8n releases (stable or beta) from GitHub, update Coolify environment variables, and trigger deployments.

Functionality  
This workflow automates deployment of n8n releases t...

### [Prevent Concurrent Workflow Runs Using Redis](https://n8n.io/workflows/3976-prevent-concurrent-workflow-runs-using-redis)
- **ID:** 3976 | **Creator:** @hpstock ✓ | **Views:** 449 | **Nodes:** 1
- **Nodes:** Redis
- What does this template do?  
This workflow sets a small "lock" value in Redis so that only one copy of a long job can run at the same time. If another trigger fires while the job is still busy, the w...

### [OAuth2 Settings Finder with OpenRouter Chat Model and Llama 3.3](https://n8n.io/workflows/3279-oauth2-settings-finder-with-openrouter-chat-model-and-llama)
- **ID:** 3279 | **Creator:** @h3rx | **Views:** 447 | **Nodes:** 4
- **Nodes:** Code, Basic LLM Chain, Structured Output Parser +1 more
- Find OAuth URIs with AI Llama

Overview:
The AI agent identifies:
Authorization URI
Token URI
Audience

Methodology:
Confidence scoring is utilized to assess the trustworthiness of extracted data:
Sco...

### [Automatic monitoring of multiple URLs with downtime alerts](https://n8n.io/workflows/5298-automatic-monitoring-of-multiple-urls-with-downtime-alerts)
- **ID:** 5298 | **Creator:** @oxsr11 ✓ | **Views:** 441 | **Nodes:** 4
- **Nodes:** Google Sheets, HTTP Request, Gmail +1 more
- This n8n workflow allows you to automatically monitor the status of multiple URLs in a simple and efficient way. You just need to enter the URLs you want to scan and run the workflow (either manually...

### [Restore and Recover n8n Credentials from Google Drive Backups with Duplication Protection](https://n8n.io/workflows/4518-restore-and-recover-n8n-credentials-from-google-drive-backup)
- **ID:** 4518 | **Creator:** @danielng ✓ | **Views:** 440 | **Nodes:** 2
- **Nodes:** Google Drive, Code
- This n8n workflow template uses community nodes and is only compatible with the self-hosted version of n8n. 

Restore n8n Credentials from Google Drive Backup

This template enables you to restore you...

### [Automated GitHub Scanner for Exposed AWS IAM Keys](https://n8n.io/workflows/5021-automated-github-scanner-for-exposed-aws-iam-keys)
- **ID:** 5021 | **Creator:** @niranjan ✓ | **Views:** 419 | **Nodes:** 3
- **Nodes:** HTTP Request, Slack, Code
- Automated GitHub Scanner for Exposed AWS IAM Keys

Overview

This n8n workflow automatically scans GitHub for exposed AWS IAM access keys associated with your AWS account, helping security teams quick...

### [Configure Telegram Bot Webhooks with Form Automation](https://n8n.io/workflows/4856-configure-telegram-bot-webhooks-with-form-automation)
- **ID:** 4856 | **Creator:** @untalcamilomedina | **Views:** 414 | **Nodes:** 0
- **Nodes:** 
- 🤖 Telegram Bot Webhook Configuration Tool

This workflow creates a simple web form that helps you configure Telegram bot webhooks quickly. Instead of manually constructing the Telegram API URL, this t...

### [🤖 Build Resilient AI Workflows with Automatic GPT and Gemini Failover Chain](https://n8n.io/workflows/5160-build-resilient-ai-workflows-with-automatic-gpt-and-gemini)
- **ID:** 5160 | **Creator:** @lucaspeyrin ✓ | **Views:** 411 | **Nodes:** 4
- **Nodes:** AI Agent, LangChain Code, OpenAI Chat Model +1 more
- This workflow contains community nodes that are only compatible with the self-hosted version of n8n.

How it works

This workflow demonstrates how to create a resilient AI Agent that automatically fal...

### [AI-Powered Vendor Policy & RSS Feed Analysis with Integrated Risk Scoring](https://n8n.io/workflows/5103-ai-powered-vendor-policy-and-rss-feed-analysis-with-integrat)
- **ID:** 5103 | **Creator:** @kamalraj | **Views:** 411 | **Nodes:** 5
- **Nodes:** HTTP Request, Gmail, Code +2 more
- 🧠 Overview

A dual-engine, AI-driven n8n workflow that automates the monitoring of both vendor policy webpages and compliance-related RSS feeds. It intelligently detects recent updates, evaluates thei...

### [Deploy Docker MinIO, API Backend for WHMCS/WISECP](https://n8n.io/workflows/3198-deploy-docker-minio-api-backend-for-whmcs-wisecp)
- **ID:** 3198 | **Creator:** @puqcloud ✓ | **Views:** 409 | **Nodes:** 1
- **Nodes:** Code
- Setting up n8n workflow

Overview

The Docker MinIO WHMCS module uses a specially designed workflow for n8n to automate deployment processes. The workflow provides an API interface for the module, rec...

### [Track an event in Segment](https://n8n.io/workflows/495-track-an-event-in-segment)
- **ID:** 495 | **Creator:** @tanay1337 ✓ | **Views:** 406 | **Nodes:** 1
- **Nodes:** Segment

### [Automated Workflow Backups to GitHub with PR Creation & Slack Notifications](https://n8n.io/workflows/4463-automated-workflow-backups-to-github-with-pr-creation-and-sl)
- **ID:** 4463 | **Creator:** @duynb ✓ | **Views:** 381 | **Nodes:** 3
- **Nodes:** GitHub, HTTP Request, Slack
- Who is this for?

This template is ideal for DevOps engineers, automation specialists, and n8n users who manage multiple workflows and want a reliable version control system for backups. It’s especial...

### [Monitor GitHub Releases with Gemini AI Chinese Translation & Slack Notifications](https://n8n.io/workflows/3452-monitor-github-releases-with-gemini-ai-chinese-translation-a)
- **ID:** 3452 | **Creator:** @tbphp | **Views:** 375 | **Nodes:** 5
- **Nodes:** Redis, Slack, Code +2 more
- Overview

This n8n template monitors specified GitHub repositories. When a new release is published, it automatically fetches the information, uses AI (Google Gemini by default) to summarize and tran...

### [Error Handling System with PostgreSQL Logging and Rate-Limited Notifications](https://n8n.io/workflows/3882-error-handling-system-with-postgresql-logging-and-rate-limit)
- **ID:** 3882 | **Creator:** @frkr ✓ | **Views:** 370 | **Nodes:** 4
- **Nodes:** Send Email, Postgres, Pushover +1 more
- Log errors and avoid sending too many emails

Use case

Most of the time, it’s necessary to log all errors that occur. However, in some cases, a scheduled task or service consuming excessive resources...

### [Evaluation metric example: String similarity](https://n8n.io/workflows/4274-evaluation-metric-example-string-similarity)
- **ID:** 4274 | **Creator:** @davidn8n ✓ | **Views:** 361 | **Nodes:** 4
- **Nodes:** HTTP Request, Code, OpenAI +1 more
- AI evaluation in n8n

This is a template for n8n's evaluation feature. 

Evaluation is a technique for getting confidence that your AI workflow performs reliably, by running a test dataset containing...

### [Reusable and Independently Testable Sub-workflow](https://n8n.io/workflows/5032-reusable-and-independently-testable-sub-workflow)
- **ID:** 5032 | **Creator:** @vklepikovskyi ✓ | **Views:** 345 | **Nodes:** 0
- **Nodes:** 
- Reusable and Independently Testable Sub-workflow
This n8n workflow provides a standardized structure for building and testing sub-workflows in isolation. Its purpose is to help you create robust, reus...

### [Export Wordpress to PineCone Vector Store](https://n8n.io/workflows/3557-export-wordpress-to-pinecone-vector-store)
- **ID:** 3557 | **Creator:** @theomarcadet ✓ | **Views:** 329 | **Nodes:** 5
- **Nodes:** HTTP Request, Embeddings OpenAI, Token Splitter +2 more
- Click here to access this Workflow for free.

Make your website the knowledge base of your LLM chatbot


This workflow automatically syncs your WordPress content (Pages and Posts) into a vector databa...

### [AWS Cost & Usage Report Management for AI Agents](https://n8n.io/workflows/5502-aws-cost-and-usage-report-management-for-ai-agents)
- **ID:** 5502 | **Creator:** @cfomodz ✓ | **Views:** 328 | **Nodes:** 0
- **Nodes:** 
- Complete MCP server exposing 4 AWS Cost and Usage Report Service API operations to AI agents.

⚡ Quick Setup

Need help? Want access to more workflows and even live Q&A sessions with a top verified n8...

### [Deploy Docker n8n, API Backend for WHMCS/WISECP](https://n8n.io/workflows/3197-deploy-docker-n8n-api-backend-for-whmcs-wisecp)
- **ID:** 3197 | **Creator:** @puqcloud ✓ | **Views:** 322 | **Nodes:** 1
- **Nodes:** Code
- Setting up n8n workflow

Overview

The Docker n8n WHMCS module uses a specially designed workflow for n8n to automate deployment processes. The workflow provides an API interface for the module, recei...

### [Self update Docker-based n8n with email approval and SSH](https://n8n.io/workflows/10471-self-update-docker-based-n8n-with-email-approval-and-ssh)
- **ID:** 10471 | **Creator:** @anasn-farooq ✓ | **Views:** 321 | **Nodes:** 2
- **Nodes:** Send Email, HTTP Request
- n8n Self-Updater Workflow

&gt; An automated n8n workflow originally built for DigitalOcean-based n8n deployments, but fully compatible with any VPS or cloud hosting (e.g., AWS, Google Cloud, Hetzner,...

### [Batch Airtable requests to send data 9x faster](https://n8n.io/workflows/2831-batch-airtable-requests-to-send-data-9x-faster)
- **ID:** 2831 | **Creator:** @brahimh | **Views:** 310 | **Nodes:** 1
- **Nodes:** HTTP Request
- Watch Demo YouTube Video

Optimized Airtable Bulk Data Workflow

This workflow is specifically designed to address the challenges of upserting or inserting large volumes of data into Airtable. By leve...

### [Redis Locking for Concurrent Task Handling](https://n8n.io/workflows/3444-redis-locking-for-concurrent-task-handling)
- **ID:** 3444 | **Creator:** @geffy | **Views:** 305 | **Nodes:** 2
- **Nodes:** Redis, Code
- 👤 Who is this for?

This workflow is great for n8n users who want to prevent duplicate or overlapping workflow runs. If you're a developer, DevOps engineer, or automation enthusiast managing tasks lik...

### [🛠️ Grafana Tool MCP Server 💪 all 16 operations](https://n8n.io/workflows/5245-grafana-tool-mcp-server-all-16-operations)
- **ID:** 5245 | **Creator:** @cfomodz ✓ | **Views:** 303 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing all Grafana Tool operations to...

### [Monitor AI Chat Interactions with Gemini 2.5 and Langfuse Tracing](https://n8n.io/workflows/4972-monitor-ai-chat-interactions-with-gemini-25-and-langfuse-tra)
- **ID:** 4972 | **Creator:** @ehales | **Views:** 300 | **Nodes:** 4
- **Nodes:** AI Agent, LangChain Code, Simple Memory +1 more
- This workflow contains community nodes that are only compatible with the self-hosted version of n8n.

How it works

This workflow is a simple AI Agent that connects to Langfuse so send tracing data to...

### [Flexible Currency Rate Uploads for SAP B1 with AI Validation & Multiple Sources](https://n8n.io/workflows/4931-flexible-currency-rate-uploads-for-sap-b1-with-ai-validation)
- **ID:** 4931 | **Creator:** @raquelgiugliano ✓ | **Views:** 293 | **Nodes:** 4
- **Nodes:** Google Sheets, HTTP Request, Microsoft SQL +1 more
- This workflow automates currency rate uploads into SAP Business One via Service Layer, using flexible input sources such as JSON (API), SQL Server, Google Sheets, or manual values. It leverages logic...

### [Control Your 3D Printer with GPT-4o and OctoPrint API Conversations](https://n8n.io/workflows/4222-control-your-3d-printer-with-gpt-4o-and-octoprint-api-conver)
- **ID:** 4222 | **Creator:** @unit98 | **Views:** 283 | **Nodes:** 5
- **Nodes:** HTTP Request, Discord, AI Agent +2 more
- Ever wanted to just tell your 3d printer what to do remotely? 

This game changer let's you converse with OpenAI agents to manage OctoPrint connected 3d printers. Great for remote management and monit...

### [🛠️ Strapi Tool MCP Server 💪 5 operations](https://n8n.io/workflows/5362-strapi-tool-mcp-server-5-operations)
- **ID:** 5362 | **Creator:** @cfomodz ✓ | **Views:** 283 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing all Strapi Tool operations to...

### [AI Agent Integration for Bubble Apps with MCP Protocol Data Access](https://n8n.io/workflows/4952-ai-agent-integration-for-bubble-apps-with-mcp-protocol-data)
- **ID:** 4952 | **Creator:** @salama | **Views:** 281 | **Nodes:** 0
- **Nodes:** 
- Let AI agents fetch communicate with your Bubble app automatically. It connects direcly with your Bubble data API. This workflow is designed for teams building AI tools or copilots that need seamless...

### [Readable Workflow Export & Deployment Pipeline for Multi-Environment CI/CD](https://n8n.io/workflows/3994-readable-workflow-export-and-deployment-pipeline-for-multi-e)
- **ID:** 3994 | **Creator:** @voortwis | **Views:** 279 | **Nodes:** 0
- **Nodes:** 
- This n8n workflow template uses community nodes and is only compatible with the self-hosted version of n8n. 

Export workflows with readable names, tagged for different environments

To ensure underst...

### [Manage Cloudflare DNS Records with AI-powered Chat Assistant](https://n8n.io/workflows/6844-manage-cloudflare-dns-records-with-ai-powered-chat-assistant)
- **ID:** 6844 | **Creator:** @kres | **Views:** 276 | **Nodes:** 6
- **Nodes:** HTTP Request, Code, AI Agent +3 more
- This n8n flow demos basic dev-ops operation task, dns records management. 

AI agent with light and basic prompt functions like getter and setter for DNS records. 

In this special case, we are manag...

### [Automate GPT-4o Fine-Tuning with Google Sheets or Airtable Data](https://n8n.io/workflows/4853-automate-gpt-4o-fine-tuning-with-google-sheets-or-airtable-d)
- **ID:** 4853 | **Creator:** @mattyreed1 ✓ | **Views:** 274 | **Nodes:** 5
- **Nodes:** Airtable, Google Sheets, HTTP Request +2 more
- Who is this for?  
Anyone curating before/after text examples in a spreadsheet and wanting a push-button path to a fine-tuned GPT model—without touching curl. Works with Google Sheets or Airtable.

Wh...

### [Comprehensive SSL Certificate Monitoring with Discord Alerts and Notion Integration](https://n8n.io/workflows/5673-comprehensive-ssl-certificate-monitoring-with-discord-alerts)
- **ID:** 5673 | **Creator:** @tomcao | **Views:** 271 | **Nodes:** 4
- **Nodes:** HTTP Request, Discord, Notion +1 more
- 🔐 Advanced SSL Health Monitor
👤 Who is this for?
This workflow is designed for DevOps engineers, IT administrators, and security professionals who need comprehensive SSL certificate monitoring and he...

### [Build Production-Ready User Authentication with Airtable and JWT](https://n8n.io/workflows/4444-build-production-ready-user-authentication-with-airtable-and)
- **ID:** 4444 | **Creator:** @nanabrown ✓ | **Views:** 271 | **Nodes:** 2
- **Nodes:** Airtable, Crypto
- This n8n workflow provides a comprehensive solution for user authentication and management, leveraging Airtable as the backend database. It includes flows for user sign-up and login, aswell as the sam...

### [Github Webhook-Based n8n Workflow Import Template](https://n8n.io/workflows/4471-github-webhook-based-n8n-workflow-import-template)
- **ID:** 4471 | **Creator:** @dbern | **Views:** 271 | **Nodes:** 1
- **Nodes:** GitHub
- This n8n workflow template uses community nodes and is only compatible with the self-hosted version of n8n. 

This template aims to ease the process of deploying workflows from github. It has a compan...

### [Export Cloudflare Domains with DNS Records and Settings to Google Sheets](https://n8n.io/workflows/4850-export-cloudflare-domains-with-dns-records-and-settings-to-g)
- **ID:** 4850 | **Creator:** @kres | **Views:** 271 | **Nodes:** 3
- **Nodes:** Google Sheets, HTTP Request, Code
- How it works

This workflow simply exports all your CloudFlare domains to Google Sheet to get high overview of all of your settings. This could help for easy debugging, searching or similar needs. 
In...

### [Simple Eval for Legal Benchmarking](https://n8n.io/workflows/4712-simple-eval-for-legal-benchmarking)
- **ID:** 4712 | **Creator:** @adamjanes ✓ | **Views:** 265 | **Nodes:** 5
- **Nodes:** Google Sheets, Google Drive, Basic LLM Chain +2 more
- This workflow demonstrates a simple way to run evals on a set of test cases stored in a Google Sheet.

The example we are using comes from an info extraction task dataset, where we tested 6 different...

### [Automated n8n Credential Backups to Google Drive with Scheduled Execution](https://n8n.io/workflows/4517-automated-n8n-credential-backups-to-google-drive-with-schedu)
- **ID:** 4517 | **Creator:** @danielng ✓ | **Views:** 263 | **Nodes:** 2
- **Nodes:** Google Drive, Code
- This n8n workflow template uses community nodes and is only compatible with the self-hosted version of n8n. 
Auto Backup n8n Credentials to Google Drive

This workflow automates the backup of all your...

### [Deploy Docker NextCloud, API Backend for WHMCS/WISECP](https://n8n.io/workflows/4015-deploy-docker-nextcloud-api-backend-for-whmcs-wisecp)
- **ID:** 4015 | **Creator:** @puqcloud ✓ | **Views:** 254 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- Overview

The Docker NextCloud WHMCS module leverages a sophisticated workflow for n8n, designed to automate the comprehensive deployment, configuration, and management processes for NextCloud and Ne...

### [🛠️ Cloudflare Tool MCP Server](https://n8n.io/workflows/5322-cloudflare-tool-mcp-server)
- **ID:** 5322 | **Creator:** @cfomodz ✓ | **Views:** 249 | **Nodes:** 0
- **Nodes:** 
- Complete MCP server exposing all Cloudflare Tool operations to AI agents. Zero configuration needed - all 4 operations pre-built.

⚡ Quick Setup

Need help? Want access to more workflows and even live...

### [SAP Service Layer Login](https://n8n.io/workflows/4932-sap-service-layer-login)
- **ID:** 4932 | **Creator:** @raquelgiugliano ✓ | **Views:** 244 | **Nodes:** 1
- **Nodes:** HTTP Request
- This minimal utility workflow connects to the SAP Business One Service Layer API to verify login credentials and return the session ID. It's ideal for testing access or using as a sub-workflow to retr...

### [Website Scam Risk Detector with GPT-4o and SerpAPI](https://n8n.io/workflows/5614-website-scam-risk-detector-with-gpt-4o-and-serpapi)
- **ID:** 5614 | **Creator:** @lifehacks ✓ | **Views:** 241 | **Nodes:** 3
- **Nodes:** AI Agent, OpenAI Chat Model, SerpApi (Google Search)
- What It Does
This intelligent workflow simplifies the complex task of determining whether a website is legitimate or potentially a scam. By simply submitting a URL through a form, the system initiates...

### [Airtable Batch Update / Insert rows (send faster + save API call requests)](https://n8n.io/workflows/3394-airtable-batch-update-insert-rows-send-faster-save-api-ca)
- **ID:** 3394 | **Creator:** @s3n | **Views:** 240 | **Nodes:** 3
- **Nodes:** HTTP Request, Code, DebugHelper
- This workflow allows you to batch update/insert Airtable rows in groups of 10, significantly reducing the number of API calls and increasing performance.

🚀 How It Works

Copy the 3 Nodes  
   Copy th...

### [Get Scaleway Server Info with Dynamic Filtering](https://n8n.io/workflows/3571-get-scaleway-server-info-with-dynamic-filtering)
- **ID:** 3571 | **Creator:** @pablobarrier | **Views:** 240 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- Get Scaleway Server Info with Dynamic Filtering

Description

This workflow is designed for developers, system administrators, and DevOps engineers who need to retrieve and filter Scaleway server info...

### [Automated n8n Workflows Backup on GitLab with Username Organization](https://n8n.io/workflows/5616-automated-n8n-workflows-backup-on-gitlab-with-username-organ)
- **ID:** 5616 | **Creator:** @oneclick-ai ✓ | **Views:** 236 | **Nodes:** 2
- **Nodes:** Send Email, GitLab
- Overview
This solution ensures the secure backup and version control of your self-hosted n8n workflows by storing them in a GitLab repository. It compares current workflows with their GitLab counterpa...

### [Unix Timestamp to ISO Date Converter](https://n8n.io/workflows/4623-unix-timestamp-to-iso-date-converter)
- **ID:** 4623 | **Creator:** @ist00dent ✓ | **Views:** 236 | **Nodes:** 0
- **Nodes:** 
- This n8n workflow provides a simple yet powerful utility to convert Unix timestamps (seconds since epoch) into the universally recognized ISO 8601 date and time format. This is crucial for harmonizing...

### [Generate Interactive Quantity Reports from Revit and IFC Projects to HTML](https://n8n.io/workflows/5869-generate-interactive-quantity-reports-from-revit-and-ifc-pro)
- **ID:** 5869 | **Creator:** @datadrivenconstruction ✓ | **Views:** 236 | **Nodes:** 0
- **Nodes:** 
- Revit to HTML Quantity Takeoff Generator

Automates extraction of wall quantities from Revit models and creates a professional interactive HTML report.

Key Features

Automated wall quantity analysis...

### [Automated AWS IAM Key Compromise Response with Slack & Claude AI](https://n8n.io/workflows/5123-automated-aws-iam-key-compromise-response-with-slack-and-cla)
- **ID:** 5123 | **Creator:** @niranjan ✓ | **Views:** 224 | **Nodes:** 6
- **Nodes:** HTTP Request, Slack, Code +3 more
- 🛡️ Automated AWS Key Compromise Remediation

Description

This n8n workflow provides a secure, enterprise-grade response system for AWS IAM access key compromises with built-in form submission and hum...

### [Validate CAD and BIM Files Against Excel Standards (Revit, IFC, AutoCAD, DGN)](https://n8n.io/workflows/5868-validate-cad-and-bim-files-against-excel-standards-revit-ifc)
- **ID:** 5868 | **Creator:** @datadrivenconstruction ✓ | **Views:** 222 | **Nodes:** 1
- **Nodes:** Code
- This workflow contains community nodes that are only compatible with the self-hosted version of n8n.

CAD-BIM Multi-Format Validation Pipeline

This workflow enables automated validation of CAD and BI...

### [Restore n8n Workflows from Google Drive Backups](https://n8n.io/workflows/4516-restore-n8n-workflows-from-google-drive-backups)
- **ID:** 4516 | **Creator:** @danielng ✓ | **Views:** 219 | **Nodes:** 1
- **Nodes:** Google Drive
- Restore All n8n Workflows from Google Drive Backups

Restoring multiple n8n workflows manually, especially when migrating your n8n instance to another host or server, can be an incredibly daunting and...

### [Network Vulnerability Scanner with NMAP and Automated CVE Reporting](https://n8n.io/workflows/11007-network-vulnerability-scanner-with-nmap-and-automated-cve-re)
- **ID:** 11007 | **Creator:** @vighsandor ✓ | **Views:** 213 | **Nodes:** 3
- **Nodes:** Send Email, Telegram, Code
- Network Vulnerability Scanner (used NMAP as engine) with Automated CVE Report

Workflow Overview

This n8n workflow provides comprehensive network vulnerability scanning with automated CVE enrichment...

### [Benchmark LLM Performance on Legal Documents with Google Sheets and OpenRouter](https://n8n.io/workflows/5066-benchmark-llm-performance-on-legal-documents-with-google-she)
- **ID:** 5066 | **Creator:** @adamjanes ✓ | **Views:** 210 | **Nodes:** 6
- **Nodes:** Google Sheets, HTTP Request, Google Drive +3 more
- This workflow demonstrates a simple way to run evals on a set of test cases stored in a Google Sheet.

The example we are using comes from an info extraction task dataset, where we tested 6 different...

### [Amazon CloudWatch Application Insights API with 27 Operations](https://n8n.io/workflows/5498-amazon-cloudwatch-application-insights-api-with-27-operation)
- **ID:** 5498 | **Creator:** @cfomodz ✓ | **Views:** 203 | **Nodes:** 0
- **Nodes:** 
- Complete MCP server exposing 27 Amazon CloudWatch Application Insights API operations to AI agents.

⚡ Quick Setup

Need help? Want access to more workflows and even live Q&A sessions with a top verif...

### [Manage User Authentication with Telegram, Redis Cache and Google Sheets](https://n8n.io/workflows/4548-manage-user-authentication-with-telegram-redis-cache-and-goo)
- **ID:** 4548 | **Creator:** @architjn ✓ | **Views:** 199 | **Nodes:** 3
- **Nodes:** Google Sheets, Redis, Code
- How It Works

Telegram bot listens for messages and uses chat ID as the unique user identifier.
Checks Google Sheets for existing users; registers new users if not found.
Caches active sessions in Red...

### [Version Control n8n Workflows in GitLab with Customer Tag Organization](https://n8n.io/workflows/8042-version-control-n8n-workflows-in-gitlab-with-customer-tag-or)
- **ID:** 8042 | **Creator:** @kennouche-omar | **Views:** 194 | **Nodes:** 2
- **Nodes:** GitLab, Code
- How it works
Triggers manually or on schedule (03:00 daily by default)  
Fetches workflows tagged backup-workflows via n8n API  
Normalizes workflow names and applies [client: NAME] tag convention  
P...

### [Automatic Backup of Workflows to GitHub with Email/Telegram Notifications](https://n8n.io/workflows/4923-automatic-backup-of-workflows-to-github-with-email-telegram)
- **ID:** 4923 | **Creator:** @buildscool | **Views:** 192 | **Nodes:** 4
- **Nodes:** HTTP Request, Telegram, Gmail +1 more
- Why?

Have you ever updated your n8n instance, or moved from one instance to the other and lost all your workflows? I suggest NOT DOING THAT! Especially if you have very complex workflows that would t...

### [Unlimited Website Down Checker - Uptime Robot Alternative](https://n8n.io/workflows/5887-unlimited-website-down-checker-uptime-robot-alternative)
- **ID:** 5887 | **Creator:** @vasarmilan ✓ | **Views:** 190 | **Nodes:** 3
- **Nodes:** HTTP Request, Telegram, Gmail
- Video Introduction

Want to automate your inbox or need a custom workflow? 📞 Book a Call | 💬 DM me on Linkedin

Get Alerted When Your Website Is Down – n8n as an Uptime Robot Alternative



If you man...

### [Search and Retrieve eBay Product Data with Catalog API for AI Agents](https://n8n.io/workflows/5566-search-and-retrieve-ebay-product-data-with-catalog-api-for-a)
- **ID:** 5566 | **Creator:** @cfomodz ✓ | **Views:** 184 | **Nodes:** 0
- **Nodes:** 
- Complete MCP server exposing 2 Catalog API operations to AI agents.

⚡ Quick Setup

Need help? Want access to more workflows and even live Q&A sessions with a top verified n8n creator.. All 100% free?...

### [Deploy Docker Grafana, API Backend for WHMCS/WISECP](https://n8n.io/workflows/4011-deploy-docker-grafana-api-backend-for-whmcs-wisecp)
- **ID:** 4011 | **Creator:** @puqcloud ✓ | **Views:** 182 | **Nodes:** 1
- **Nodes:** Code
- Setting up n8n workflow

Overview

The Docker Grafana WHMCS module uses a specially designed workflow for n8n to automate deployment processes. The workflow provides an API interface for the module, r...

### [Automated DNS Records Lookup for Subdomains with HackerTarget API Reports](https://n8n.io/workflows/6355-automated-dns-records-lookup-for-subdomains-with-hackertarge)
- **ID:** 6355 | **Creator:** @adnantariq ✓ | **Views:** 182 | **Nodes:** 3
- **Nodes:** HTTP Request, Gmail, Code
- 🧠 EnumX: Auto DNS Lookup for Subdomains with Markdown Export

Who’s it for

Security engineers, red teamers, or automation-curious teams looking to enhance passive reconnaissance with minimal effort....

### [Host Your Own JWT Authentication System with Data Tables and Token Management](https://n8n.io/workflows/9660-host-your-own-jwt-authentication-system-with-data-tables-and)
- **ID:** 9660 | **Creator:** @zivkovic58 ✓ | **Views:** 178 | **Nodes:** 2
- **Nodes:** Crypto, Code
- Description
A production-ready authentication workflow implementing secure user registration, login, token verification, and refresh token mechanisms. Perfect for adding authentication to any applicat...

### [Automate GitHub PR Linting with Google Gemini AI and Auto-Fix PRs](https://n8n.io/workflows/4073-automate-github-pr-linting-with-google-gemini-ai-and-auto-fi)
- **ID:** 4073 | **Creator:** @adbertram ✓ | **Views:** 175 | **Nodes:** 4
- **Nodes:** HTTP Request, Code, AI Agent +1 more
- LintGuardian: Automated PR Linting with n8n & AI

What It Does

LintGuardian is an n8n workflow template that automates code quality enforcement for GitHub repositories. When a pull request is created...

### [🛠️ Microsoft SharePoint Tool MCP Server 💪 all 11 operations](https://n8n.io/workflows/5178-microsoft-sharepoint-tool-mcp-server-all-11-operations)
- **ID:** 5178 | **Creator:** @cfomodz ✓ | **Views:** 170 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing all Microsoft SharePoint Tool...

### [Monitor SSL certificate expiry dates with Google Sheets & Slack alerts](https://n8n.io/workflows/5172-monitor-ssl-certificate-expiry-dates-with-google-sheets-and)
- **ID:** 5172 | **Creator:** @customjs ✓ | **Views:** 166 | **Nodes:** 2
- **Nodes:** Google Sheets, Slack
- This n8n workflow illustrates how to monitor and track SSL certificate expiration dates for any domain using the SSL Checker node from customJS. It automatically updates a Google Sheet with the numb...

### [Get Any Image: Standard Fetch with BrightData Web Unblocker Failover](https://n8n.io/workflows/5905-get-any-image-standard-fetch-with-brightdata-web-unblocker-f)
- **ID:** 5905 | **Creator:** @phil ✓ | **Views:** 158 | **Nodes:** 1
- **Nodes:** HTTP Request
- This workflow is your ultimate solution for reliable image retrieval from any web source, including those heavily protected. 

It operates with a smart, cost-effective strategy: it first attempts to f...

### [Expose Translate a language endpoint to AI Agents with DeepL Tool MCP Server](https://n8n.io/workflows/5313-expose-translate-a-language-endpoint-to-ai-agents-with-deepl)
- **ID:** 5313 | **Creator:** @cfomodz ✓ | **Views:** 157 | **Nodes:** 0
- **Nodes:** 
- Complete MCP server exposing all DeepL Tool operations to AI agents. Zero configuration needed - all 1 operations pre-built.

⚡ Quick Setup

Need help? Want access to more workflows and even live Q&A...

### [Website Uptime Monitoring with GPT-4 Analysis and Gmail Notifications](https://n8n.io/workflows/7194-website-uptime-monitoring-with-gpt-4-analysis-and-gmail-noti)
- **ID:** 7194 | **Creator:** @ca7ai ✓ | **Views:** 154 | **Nodes:** 3
- **Nodes:** HTTP Request, Gmail, OpenAI
- How it works
Checks if a website is up, sends the HTTP result to an AI model (ChatGPT) for analysis, and emails a clear success or failure message. Great for a quick “is this site up?” check you can t...

### [Compare Lists and Identify Common Items & Differences Using Custom Keys](https://n8n.io/workflows/5033-compare-lists-and-identify-common-items-and-differences-usin)
- **ID:** 5033 | **Creator:** @tenkay | **Views:** 148 | **Nodes:** 1
- **Nodes:** Code
- This workflow compares two lists of objects (List A and List B) using a user-specified key (e.g. email, id, domain) and returns:

Items common to both lists (based on the key)
Items only in List A
Ite...

### [Monitor Software Compliance with Jamf Patch Summaries in Slack](https://n8n.io/workflows/5529-monitor-software-compliance-with-jamf-patch-summaries-in-sla)
- **ID:** 5529 | **Creator:** @mrrobot ✓ | **Views:** 147 | **Nodes:** 3
- **Nodes:** HTTP Request, Slack, Code
- 🧩 Jamf Patch Summary to Slack
Stay on top of software patch compliance by automatically posting Jamf patch summaries to Slack.
This helps IT and security teams quickly identify outdated installs and t...

### [IP2WHOIS Domain Lookup MCP Server](https://n8n.io/workflows/5583-ip2whois-domain-lookup-mcp-server)
- **ID:** 5583 | **Creator:** @cfomodz ✓ | **Views:** 145 | **Nodes:** 0
- **Nodes:** 
- Complete MCP server exposing 1 IP2WHOIS Domain Lookup API operations to AI agents.

⚡ Quick Setup
Need help? Want access to more workflows and even live Q&A sessions with a top verified n8n creator.....

### [WordPress context backup to github](https://n8n.io/workflows/5288-wordpress-context-backup-to-github)
- **ID:** 5288 | **Creator:** @boagolden | **Views:** 143 | **Nodes:** 4
- **Nodes:** GitHub, HTTP Request, Wordpress +1 more
- This template can backup WordPress context github。

### [AI-powered document search with Oracle and ONNX embeddings for recruiting](https://n8n.io/workflows/10273-ai-powered-document-search-with-oracle-and-onnx-embeddings-f)
- **ID:** 10273 | **Creator:** @sudarshansoma | **Views:** 141 | **Nodes:** 2
- **Nodes:** Code, Oracle Database
- How it works

Create a user for doing Hybrid Search.
Clear Existing Data, if present.
Add Documents into the table.
Create a hybrid index.
Run Semantic search on the Documents table for "prioritize te...

### [Deploy Docker InfluxDB, API Backend for WHMCS/WISECP](https://n8n.io/workflows/4014-deploy-docker-influxdb-api-backend-for-whmcs-wisecp)
- **ID:** 4014 | **Creator:** @puqcloud ✓ | **Views:** 137 | **Nodes:** 1
- **Nodes:** Code
- Overview

The Docker InfluxDB WHMCS module uses a specially designed workflow for n8n to automate deployment processes. The workflow provides an API interface for the module, receives specific command...

### [🛠️ PagerDuty Tool MCP Server 💪 all 9 operations](https://n8n.io/workflows/5343-pagerduty-tool-mcp-server-all-9-operations)
- **ID:** 5343 | **Creator:** @cfomodz ✓ | **Views:** 136 | **Nodes:** 0
- **Nodes:** 
- Complete MCP server exposing all PagerDuty Tool operations to AI agents. Zero configuration needed - all 9 operations pre-built.

⚡ Quick Setup

Need help? Want access to more workflows and even live...

### [Bidirectional GitHub Workflow Sync & Version Control for n8n Workflows](https://n8n.io/workflows/5081-bidirectional-github-workflow-sync-and-version-control-for-n)
- **ID:** 5081 | **Creator:** @rustedviking | **Views:** 134 | **Nodes:** 2
- **Nodes:** GitHub, Code
- Who is this for?
This template is ideal for n8n administrators, automation engineers, and DevOps teams who want to maintain bidirectional synchronization between their n8n workflows and GitHub reposit...

### [Automated Server Log Cleanup via Email Alerts with SSH - Nginx, Docker, System](https://n8n.io/workflows/5406-automated-server-log-cleanup-via-email-alerts-with-ssh-ngi)
- **ID:** 5406 | **Creator:** @oneclick-ai ✓ | **Views:** 121 | **Nodes:** 1
- **Nodes:** Code
- This n8n workflow monitors email alerts for disk utilization exceeding 80%, extracts the server IP, logs into the server, and purges logs from Nginx, PM2, Docker, and system files to clear disk space....

### [AI Agent Integration with eBay Buy Marketing API](https://n8n.io/workflows/5567-ai-agent-integration-with-ebay-buy-marketing-api)
- **ID:** 5567 | **Creator:** @cfomodz ✓ | **Views:** 119 | **Nodes:** 0
- **Nodes:** 
- Complete MCP server exposing 1 Buy Marketing API operations to AI agents.

⚡ Quick Setup

Need help? Want access to more workflows and even live Q&A sessions with a top verified n8n creator.. All 100%...

### [XOR Encryption and Decryption with Base64 Encoding for Workflow Data](https://n8n.io/workflows/5025-xor-encryption-and-decryption-with-base64-encoding-for-workf)
- **ID:** 5025 | **Creator:** @tenkay | **Views:** 114 | **Nodes:** 1
- **Nodes:** Code
- This workflow performs basic XOR-based encryption and decryption using a custom password. It is intended to be triggered by another workflow and processes structured input in JSON format.

Input Struc...

### [Connect AI Agents to eBay Seller Metrics API via MCP Server](https://n8n.io/workflows/5572-connect-ai-agents-to-ebay-seller-metrics-api-via-mcp-server)
- **ID:** 5572 | **Creator:** @cfomodz ✓ | **Views:** 111 | **Nodes:** 0
- **Nodes:** 
- Complete MCP server exposing 4  Seller Service Metrics API  API operations to AI agents.

⚡ Quick Setup

Need help? Want access to more workflows and even live Q&A sessions with a top verified n8n cre...

### [🛠️ Splunk Tool MCP Server 💪 all 16 operations](https://n8n.io/workflows/5359-splunk-tool-mcp-server-all-16-operations)
- **ID:** 5359 | **Creator:** @cfomodz ✓ | **Views:** 108 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing all Splunk Tool operations to...

### [Auto-Start Tagged Workflows Using n8n API after Deployment](https://n8n.io/workflows/3996-auto-start-tagged-workflows-using-n8n-api-after-deployment)
- **ID:** 3996 | **Creator:** @voortwis | **Views:** 106 | **Nodes:** 0
- **Nodes:** 
- Auto Starter

On importing workflows these will not be auto started, even if the old version was running. To fix this we created this workflow that can be run after n8n starts. It fits in our auto dep...

### [Simulate Debates Between AI Agents Using Mistral to Optimize Answers](https://n8n.io/workflows/5682-simulate-debates-between-ai-agents-using-mistral-to-optimize)
- **ID:** 5682 | **Creator:** @hybroht ✓ | **Views:** 104 | **Nodes:** 4
- **Nodes:** AI Agent, Simple Memory, Structured Output Parser +1 more
- This workflow contains community nodes that are only compatible with the self-hosted version of n8n. 

AI Arena - Debate of AI Agents to Optimize Answers and Simulate Diverse Scenarios

Overview 
Vers...

### [Notion API MCP Server](https://n8n.io/workflows/5655-notion-api-mcp-server)
- **ID:** 5655 | **Creator:** @cfomodz ✓ | **Views:** 100 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing 13 Notion API operations to AI...

### [🛠️ Microsoft Graph Security Tool MCP Server 💪 all 5 operations](https://n8n.io/workflows/5180-microsoft-graph-security-tool-mcp-server-all-5-operations)
- **ID:** 5180 | **Creator:** @cfomodz ✓ | **Views:** 90 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing all Microsoft Graph Security T...

### [Expose Translate endpoint to AI Agents via 🛠️ Google Translate Tool MCP Server](https://n8n.io/workflows/5248-expose-translate-endpoint-to-ai-agents-via-google-translate)
- **ID:** 5248 | **Creator:** @cfomodz ✓ | **Views:** 89 | **Nodes:** 0
- **Nodes:** 
- Complete MCP server exposing all Google Translate Tool operations to AI agents. Zero configuration needed - all 1 operations pre-built.

⚡ Quick Setup
Need help? Want access to more workflows and even...

### [Safely Update n8n with Version Checks and Telegram Notifications](https://n8n.io/workflows/9792-safely-update-n8n-with-version-checks-and-telegram-notificat)
- **ID:** 9792 | **Creator:** @davidhluj | **Views:** 88 | **Nodes:** 3
- **Nodes:** HTTP Request, Telegram, Code
- Who’s it for
This workflow is for system administrators or self-hosted n8n users who want to automatically check and update their n8n instance to the latest version — with Telegram notifications for e...

### [GitHub Fork Status Monitor](https://n8n.io/workflows/4878-github-fork-status-monitor)
- **ID:** 4878 | **Creator:** @manish | **Views:** 86 | **Nodes:** 4
- **Nodes:** GitHub, HTTP Request, Telegram +1 more
- This workflow helps you keep an eye on your GitHub forks, notifying you when they fall behind or pull ahead of their upstream repositories.

How It Works
Fetches All Your Repos: The workflow starts by...

### [🛠️ NocoDB Tool MCP Server 💪 all 5 operations](https://n8n.io/workflows/5115-nocodb-tool-mcp-server-all-5-operations)
- **ID:** 5115 | **Creator:** @cfomodz ✓ | **Views:** 86 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing all NocoDB Tool operations to...

### [Advanced Retry and Delay Logic](https://n8n.io/workflows/5447-advanced-retry-and-delay-logic)
- **ID:** 5447 | **Creator:** @vklepikovskyi ✓ | **Views:** 85 | **Nodes:** 1
- **Nodes:** HTTP Request
- Advanced Retry and Delay Logic

This template provides a robust solution for handling API rate limits and temporary service outages in n8n workflows. It overcomes the limitations of the default node r...

### [🛠️ Metabase Tool MCP Server 💪 all 10 operations](https://n8n.io/workflows/5183-metabase-tool-mcp-server-all-10-operations)
- **ID:** 5183 | **Creator:** @cfomodz ✓ | **Views:** 85 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing all Metabase Tool operations t...

### [🛠️ Google Cloud Firestore Tool MCP Server 💪 all 7 operations](https://n8n.io/workflows/5252-google-cloud-firestore-tool-mcp-server-all-7-operations)
- **ID:** 5252 | **Creator:** @cfomodz ✓ | **Views:** 80 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing all Google Cloud Firestore Too...

### [Proxy Detection by IP2Proxy - MCP Server](https://n8n.io/workflows/5582-proxy-detection-by-ip2proxy-mcp-server)
- **ID:** 5582 | **Creator:** @cfomodz ✓ | **Views:** 80 | **Nodes:** 0
- **Nodes:** 
- Complete MCP server exposing 1 IP2Proxy Proxy Detection API operations to AI agents.

⚡ Quick Setup

Need help? Want access to more workflows and even live Q&A sessions with a top verified n8n creator...

### [📊 Token Estim8r UI – Visualize Token Usage analytics Dashboard in n8n](https://n8n.io/workflows/3529-token-estim8r-ui-visualize-token-usage-analytics-dashboard)
- **ID:** 3529 | **Creator:** @joeperes ✓ | **Views:** 78 | **Nodes:** 4
- **Nodes:** Google Sheets, HTTP Request, Code +1 more
- 📊 Visualize all your AI Token Usage analytics Dashboard using a single n8n Workflow

Artwork Generated with ✨ ideoGener8r n8n workflow template

Token Estim8r UI is the premium version of our token tr...

### [Build & Deploy MVPs from Text Prompts with AI, GitHub & Vercel](https://n8n.io/workflows/6164-build-and-deploy-mvps-from-text-prompts-with-ai-github-and-v)
- **ID:** 6164 | **Creator:** @varritech ✓ | **Views:** 76 | **Nodes:** 9
- **Nodes:** GitHub, HTTP Request, Code +6 more
- ⚡ Instant MVP Builder  
Idea, Build, and Deploy — in Minutes, with AI  
by Varritech Technologies

🏗️ What Is It?

Instant MVP Builder is a plug-and-play n8n workflow that takes a plain-English app id...

### [Automated Airtable to Postgres Migration with n8n](https://n8n.io/workflows/4772-automated-airtable-to-postgres-migration-with-n8n)
- **ID:** 4772 | **Creator:** @imperolq ✓ | **Views:** 72 | **Nodes:** 3
- **Nodes:** HTTP Request, Code, HTML
- Overview

This ETL system automates the process of migrating data from Airtable to PostgreSQL with a single API request.

It maps your Airtable schema into a Postgres-compatible structure.
Automatica...

### [Internet Archive Wayback Machine API for AI Assistants](https://n8n.io/workflows/5536-internet-archive-wayback-machine-api-for-ai-assistants)
- **ID:** 5536 | **Creator:** @cfomodz ✓ | **Views:** 71 | **Nodes:** 0
- **Nodes:** 
- Complete MCP server exposing 2 Wayback API operations to AI agents.

⚡ Quick Setup

Need help? Want access to more workflows and even live Q&A sessions with a top verified n8n creator.. All 100% free?...

### [File Hash Verification for AI Agents with hashlookup CIRCL API](https://n8n.io/workflows/5554-file-hash-verification-for-ai-agents-with-hashlookup-circl-a)
- **ID:** 5554 | **Creator:** @cfomodz ✓ | **Views:** 71 | **Nodes:** 0
- **Nodes:** 
- Complete MCP server exposing 11 hashlookup CIRCL API operations to AI agents.

⚡ Quick Setup

Need help? Want access to more workflows and even live Q&A sessions with a top verified n8n creator.. All...

### [Decodo SaaS pricing intelligence workflow (B2B pricing radar)](https://n8n.io/workflows/7626-decodo-saas-pricing-intelligence-workflow-b2b-pricing-radar)
- **ID:** 7626 | **Creator:** @trungtran ✓ | **Views:** 70 | **Nodes:** 7
- **Nodes:** HTTP Request, Slack, Google Drive +4 more
- SaaS Pricing Brief Generator (Decodo → LLM → Google Docs → PDF → Slack)
🚀 Try Decodo — Web Scraping & Data API (Coupon: TRUNG)

Decodo is a powerful public data access platform offering managed web sc...

### [Convert CAD & BIM (Revit, IFC, AutoCAD) in DataBase (DataFrame)](https://n8n.io/workflows/5867-convert-cad-and-bim-revit-ifc-autocad-in-database-dataframe)
- **ID:** 5867 | **Creator:** @datadrivenconstruction ✓ | **Views:** 66 | **Nodes:** 0
- **Nodes:** 
- A minimal workflow to convert a Revit/IFC/DWG project into analysis-ready XLSX (and optional DAE) with a single run. Set two variables, execute, and the converter does the rest.

What it does
Inputs:*...

### [🛠️ Okta Tool MCP Server 💪 all 5 operations](https://n8n.io/workflows/5342-okta-tool-mcp-server-all-5-operations)
- **ID:** 5342 | **Creator:** @cfomodz ✓ | **Views:** 66 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing all Okta Tool operations to AI...

### [Backup n8n Workflows with Versioning and Notion Tracking](https://n8n.io/workflows/6947-backup-n8n-workflows-with-versioning-and-notion-tracking)
- **ID:** 6947 | **Creator:** @stephaneheckel ✓ | **Views:** 65 | **Nodes:** 1
- **Nodes:** Notion
- Copy n8n workflows to a slave n8n repository

Inspired by Alex Kim's workflow, this version adds the ability to keep multiple versions of the same workflow on the destination instance. Each copied wor...

### [BIN Card Information Lookup API Connector for AI Agents with Balance Check](https://n8n.io/workflows/5542-bin-card-information-lookup-api-connector-for-ai-agents-with)
- **ID:** 5542 | **Creator:** @cfomodz ✓ | **Views:** 65 | **Nodes:** 0
- **Nodes:** 
- Complete MCP server exposing 2 BIN Lookup API operations to AI agents.

⚡ Quick Setup

Need help? Want access to more workflows and even live Q&A sessions with a top verified n8n creator.. All 100% fr...

### [Google Cloud Natural Language Tool MCP Server](https://n8n.io/workflows/5257-google-cloud-natural-language-tool-mcp-server)
- **ID:** 5257 | **Creator:** @cfomodz ✓ | **Views:** 63 | **Nodes:** 0
- **Nodes:** 
- 🛠️ Google Cloud Natural Language Tool MCP Server

Complete MCP server exposing all Google Cloud Natural Language Tool operations to AI agents. Zero configuration needed - all 1 operations pre-built....

### [🛠️ Sentry.io Tool MCP Server 💪 all 25 operations](https://n8n.io/workflows/5358-sentryio-tool-mcp-server-all-25-operations)
- **ID:** 5358 | **Creator:** @cfomodz ✓ | **Views:** 63 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community



Complete MCP server exposing all Sentry.io Tool operation...

### [[New York Times] Article Search API MCP Server](https://n8n.io/workflows/5649-new-york-times-article-search-api-mcp-server)
- **ID:** 5649 | **Creator:** @cfomodz ✓ | **Views:** 61 | **Nodes:** 0
- **Nodes:** 
- Complete MCP server exposing 1 Article Search API operations to AI agents.

⚡ Quick Setup
Need help? Want access to more workflows and even live Q&A sessions with a top verified n8n creator.. All 100%...

### [AI Agent Managed Tables and Views with 🛠️ Coda Tool MCP Server 💪 18 operations](https://n8n.io/workflows/5319-ai-agent-managed-tables-and-views-with-coda-tool-mcp-server)
- **ID:** 5319 | **Creator:** @cfomodz ✓ | **Views:** 61 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing all Coda Tool operations to AI...

### [Auto Generate Descriptive Node Names with AI for Workflow Readability](https://n8n.io/workflows/10889-auto-generate-descriptive-node-names-with-ai-for-workflow-re)
- **ID:** 10889 | **Creator:** @mohamed3nan | **Views:** 60 | **Nodes:** 3
- **Nodes:** Basic LLM Chain, Structured Output Parser, OpenRouter Chat Model
- ⚡Auto Rename n8n Workflow Nodes with AI✨
This workflow uses AI to automatically generate clear and descriptive names for every node in your n8n workflows.
It analyzes each node's type, parameters, and...

### [🛠️ CircleCI Tool MCP Server](https://n8n.io/workflows/5325-circleci-tool-mcp-server)
- **ID:** 5325 | **Creator:** @cfomodz ✓ | **Views:** 60 | **Nodes:** 0
- **Nodes:** 
- 🛠️ CircleCI Tool MCP Server

Complete MCP server exposing all CircleCI Tool operations to AI agents. Zero configuration needed - all 3 operations pre-built.

⚡ Quick Setup
Need help? Want access to mo...

### [eBay Analytics API Rate Limit Monitoring for AI Agents](https://n8n.io/workflows/5570-ebay-analytics-api-rate-limit-monitoring-for-ai-agents)
- **ID:** 5570 | **Creator:** @cfomodz ✓ | **Views:** 57 | **Nodes:** 0
- **Nodes:** 
- Complete MCP server exposing 2 Analytics API operations to AI agents.

⚡ Quick Setup

Need help? Want access to more workflows and even live Q&A sessions with a top verified n8n creator.. All 100% fre...

### [🛠️ Google Cloud Storage Tool MCP Server 💪 all 10 operations](https://n8n.io/workflows/5256-google-cloud-storage-tool-mcp-server-all-10-operations)
- **ID:** 5256 | **Creator:** @cfomodz ✓ | **Views:** 55 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing all Google Cloud Storage Tool...

### [🛠️ Npm Tool MCP Server 💪 all 5 operations](https://n8n.io/workflows/5341-npm-tool-mcp-server-all-5-operations)
- **ID:** 5341 | **Creator:** @cfomodz ✓ | **Views:** 55 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing all Npm Tool operations to AI...

### [Create an eBay Item Feed Service API Gateway for AI Agents](https://n8n.io/workflows/5568-create-an-ebay-item-feed-service-api-gateway-for-ai-agents)
- **ID:** 5568 | **Creator:** @cfomodz ✓ | **Views:** 54 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing 4 Item Feed Service API operat...

### [EPA Environmental Compliance Data API for AI Agents with MCP Server](https://n8n.io/workflows/5636-epa-environmental-compliance-data-api-for-ai-agents-with-mcp)
- **ID:** 5636 | **Creator:** @cfomodz ✓ | **Views:** 54 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing 16 U.S. EPA Enforcement and Co...

### [NPR Station Finder Service MCP Server](https://n8n.io/workflows/5654-npr-station-finder-service-mcp-server)
- **ID:** 5654 | **Creator:** @cfomodz ✓ | **Views:** 51 | **Nodes:** 0
- **Nodes:** 
- Complete MCP server exposing 2 NPR Station Finder Service API operations to AI agents.

⚡ Quick Setup
Need help? Want access to more workflows and even live Q&A sessions with a top verified n8n creato...

### [Complete eBay Feed API Integration for AI Agents with MCP Server](https://n8n.io/workflows/5578-complete-ebay-feed-api-integration-for-ai-agents-with-mcp-se)
- **ID:** 5578 | **Creator:** @cfomodz ✓ | **Views:** 50 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing 23 Feed API operations to AI a...

### [INST - The n8n Installer: Deploy Workflows with Automatic Credential Mapping](https://n8n.io/workflows/7028-inst-the-n8n-installer-deploy-workflows-with-automatic-cre)
- **ID:** 7028 | **Creator:** @wyeth ✓ | **Views:** 49 | **Nodes:** 3
- **Nodes:** GitHub, HTTP Request, Code
- INST: The n8n Workflow Installer

This workflow provides everything you need to package and deploy multiple workflows from a single workflow you distribute.

That's right, now you can package up dozen...

### [Automated Repository Migration from GitLab Groups to Gitea Organizations](https://n8n.io/workflows/4947-automated-repository-migration-from-gitlab-groups-to-gitea-o)
- **ID:** 4947 | **Creator:** @nepomuc | **Views:** 48 | **Nodes:** 1
- **Nodes:** HTTP Request
- This flow migrates all repositories of a Gitlab group to a Gitea organization by triggering Gitea's integrated migration tool.

Set up steps:
Copy this workflow
Create an empty Gitea-organization you...

### [🧑‍🎓 Test Your Data Access Techniques with Progressive Expression Challenges](https://n8n.io/workflows/6236-test-your-data-access-techniques-with-progressive-expressio)
- **ID:** 6236 | **Creator:** @lucaspeyrin ✓ | **Views:** 47 | **Nodes:** 1
- **Nodes:** HTML
- How it works

This template is a hands-on, practical exam designed to help you master n8n Expressions—the key to accessing and manipulating data in your workflows.

If the 🎓 Expressions Tutorial Templ...

### [NPR Listening Service MCP Server](https://n8n.io/workflows/5650-npr-listening-service-mcp-server)
- **ID:** 5650 | **Creator:** @cfomodz ✓ | **Views:** 46 | **Nodes:** 0
- **Nodes:** 
- Complete MCP server exposing 9 NPR Listening Service API operations to AI agents.

⚡ Quick Setup
Need help? Want access to more workflows and even live Q&A sessions with a top verified n8n creator.. A...

### [EPA Clean Water Act Data Access & Compliance Monitoring API Integration](https://n8n.io/workflows/5623-epa-clean-water-act-data-access-and-compliance-monitoring-ap)
- **ID:** 5623 | **Creator:** @cfomodz ✓ | **Views:** 46 | **Nodes:** 0
- **Nodes:** 
- ⚠️ ADVANCED USE ONLY - U.S. EPA Enforcement and Compliance History Online (ECHO) - Clean Water Act (CWA) Rest Services MCP Server (36 operations)

🚨 This workflow is for advanced users only!

Need hel...

### [🛠️ Quick Base Tool MCP Server 💪 all 10 operations](https://n8n.io/workflows/5353-quick-base-tool-mcp-server-all-10-operations)
- **ID:** 5353 | **Creator:** @cfomodz ✓ | **Views:** 45 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing all Quick Base Tool operations...

### [Expose File, Form, & Hook Operations to AI Agents - KoBoToolbox Tool MCP Server](https://n8n.io/workflows/5235-expose-file-form-and-hook-operations-to-ai-agents-kobotool)
- **ID:** 5235 | **Creator:** @cfomodz ✓ | **Views:** 45 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing all KoBoToolbox Tool operation...

### [Query Bicycle Incident Data with BikeWise API through MCP Server](https://n8n.io/workflows/5540-query-bicycle-incident-data-with-bikewise-api-through-mcp-se)
- **ID:** 5540 | **Creator:** @cfomodz ✓ | **Views:** 44 | **Nodes:** 0
- **Nodes:** 
- Complete MCP server exposing 4 BikeWise API v2 API operations to AI agents.

⚡ Quick Setup
Need help? Want access to more workflows and even live Q&A sessions with a top verified n8n creator.. All 100...

### [🛠️ Netlify Tool MCP Server 💪 all 7 operations](https://n8n.io/workflows/5117-netlify-tool-mcp-server-all-7-operations)
- **ID:** 5117 | **Creator:** @cfomodz ✓ | **Views:** 44 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing all Netlify Tool operations to...

### [🛠️ Baserow Tool MCP Server 💪 5 operations](https://n8n.io/workflows/5328-baserow-tool-mcp-server-5-operations)
- **ID:** 5328 | **Creator:** @cfomodz ✓ | **Views:** 43 | **Nodes:** 0
- **Nodes:** 
- Need help? Want access to this workflow + many more paid workflows + live Q&A sessions with a top verified n8n creator?

Join the community

Complete MCP server exposing all Baserow Tool operations to...

### [Automated Hazard Analysis for ISO 26262 Compliance Using GPT-4](https://n8n.io/workflows/5594-automated-hazard-analysis-for-iso-26262-compliance-using-gpt)
- **ID:** 5594 | **Creator:** @manirajan | **Views:** 38 | **Nodes:** 3
- **Nodes:** AI Agent, OpenAI Chat Model, Simple Memory
- Modular Hazard Analysis Workflow : Free Version

Business Value Proposition
Accelerates ISO 26262 compliance for automotive/industrial systems by automating safety analysis while maintaining rigorous...

### [Automate GoDaddy Subdomain Management via Email Requests](https://n8n.io/workflows/5401-automate-godaddy-subdomain-management-via-email-requests)
- **ID:** 5401 | **Creator:** @oneclick-ai ✓ | **Views:** 37 | **Nodes:** 3
- **Nodes:** Send Email, HTTP Request, Code
- This n8n workflow automates subdomain creation and deletion on GoDaddy using their API, triggered via email requests. This empowers developers to manage subdomains directly without involving DevOps fo...

### [Back up n8n workflows to google drive while preserving folder structure](https://n8n.io/workflows/13245-back-up-n8n-workflows-to-google-drive-while-preserving-folde)
- **ID:** 13245 | **Creator:** @adamabdelmoumni | **Views:** 36 | **Nodes:** 4
- **Nodes:** Google Sheets, HTTP Request, Google Drive +1 more
- Back up & restore n8n workflows with preserved folder structure with GoogleDrive

A. Backup workflows solution to google Drive

✅ What problem does this workflow solve?

If you’re building and managin...

### [CYBERPULSE AI BlueOps: Asset Enrichment Engine](https://n8n.io/workflows/6410-cyberpulse-ai-blueops-asset-enrichment-engine)
- **ID:** 6410 | **Creator:** @adnantariq ✓ | **Views:** 36 | **Nodes:** 2
- **Nodes:** Send Email, Google Sheets
- 👤 Who it’s for
Blue teamers, SOC operators, cyber analysts, and SME defenders who want to automatically enrich daily CVE/IOC threats by matching them to their internal asset database.
Ideal for compli...

### [n8n Enterprise AI Security Firewall — Guardrails for Secure Agents](https://n8n.io/workflows/11025-n8n-enterprise-ai-security-firewall-guardrails-for-secure-a)
- **ID:** 11025 | **Creator:** @sandy4v ✓ | **Views:** 35 | **Nodes:** 3
- **Nodes:** Google Sheets, Google Gemini Chat Model, Guardrails
- 🛡️ n8n Guardrails: Risk Ranking

This workflow provides a complete testing rig for evaluating text against seven essential AI guardrails used in production systems.  
It helps you detect jailbreak att...

### [Back up and restore n8n workflows with GitHub sync](https://n8n.io/workflows/12721-back-up-and-restore-n8n-workflows-with-github-sync)
- **ID:** 12721 | **Creator:** @anasn-farooq ✓ | **Views:** 34 | **Nodes:** 3
- **Nodes:** GitHub, HTTP Request, Code
- n8n Workflows GitHub Manager

&gt; A comprehensive n8n workflow that provides complete bidirectional sync between your n8n instance and GitHub - automatically backs up all your workflows with intellig...

### [CYBERPULSE AI RedOps: Phishing Simulation with Redirect Tracking ](https://n8n.io/workflows/6509-cyberpulse-ai-redops-phishing-simulation-with-redirect-track)
- **ID:** 6509 | **Creator:** @adnantariq ✓ | **Views:** 33 | **Nodes:** 1
- **Nodes:** Google Sheets
- Description:
Simulate cloaked phishing links that redirect through a controlled proxy. This module tracks if secure email gateways (SEGs) or sandboxes trigger the redirect before users do. Logs access...

### [Paginate Shopify Products with GraphQL Cursor-based Navigation](https://n8n.io/workflows/5663-paginate-shopify-products-with-graphql-cursor-based-navigati)
- **ID:** 5663 | **Creator:** @elricho ✓ | **Views:** 33 | **Nodes:** 1
- **Nodes:** GraphQL
- Shopify GraphQL cursor loop

Many Shopify GraphQL queries have the ability to return a cursor which you can loop over, however the N8N GraphQL node does not natively have the ability to fetch pages....

### [CYBERPULSE AI RedOps: Internal Phishing Simulation for Security Training](https://n8n.io/workflows/6506-cyberpulse-ai-redops-internal-phishing-simulation-for-securi)
- **ID:** 6506 | **Creator:** @adnantariq ✓ | **Views:** 30 | **Nodes:** 4
- **Nodes:** Google Sheets, Gmail, AI Agent +1 more
- Description:

Simulate phishing awareness campaigns using OpenAI-generated emails. Send to target lists, log clicks with a webhook, and store results in Google Sheets. Built for internal testing and c...

### [Auto-Rename Workflow Nodes with AI (Gemini/Claude) for Better Readability (beta)](https://n8n.io/workflows/10317-auto-rename-workflow-nodes-with-ai-gemini-claude-for-better)
- **ID:** 10317 | **Creator:** @upfastai | **Views:** 29 | **Nodes:** 5
- **Nodes:** Code, Basic LLM Chain, Structured Output Parser +2 more
- Rename Workflow Nodes with AI for Clarity

This workflow automates the tedious process of renaming nodes in your n8n workflows. Instead of manually editing each node, it uses an AI language model to a...

### [Automated Website Monitoring & Performance Checks with Alerting System](https://n8n.io/workflows/13009-automated-website-monitoring-and-performance-checks-with-ale)
- **ID:** 13009 | **Creator:** @spagreen ✓ | **Views:** 27 | **Nodes:** 5
- **Nodes:** Google Sheets, HTTP Request, Discord +2 more
- Who it's for
This n8n workflow is designed for website administrators, digital marketers, SEO specialists, and business owners who want to continuously monitor their website performance metrics. It pr...

### [Automate External Attack Surface Mapping with Shodan API and DNS Lookups](https://n8n.io/workflows/10740-automate-external-attack-surface-mapping-with-shodan-api-and)
- **ID:** 10740 | **Creator:** @knute ✓ | **Views:** 25 | **Nodes:** 3
- **Nodes:** Google Sheets, HTTP Request, Code
- The Bug Bounty Target Recon n8n workflow is a powerful automation tool for security professionals and ethical hackers.

It efficiently automates the time-consuming process of external attack surface m...

### [Collect API User Data and Store in Google Sheets with CSV backup](https://n8n.io/workflows/10725-collect-api-user-data-and-store-in-google-sheets-with-csv-ba)
- **ID:** 10725 | **Creator:** @n8nwizard ✓ | **Views:** 24 | **Nodes:** 2
- **Nodes:** Google Sheets, HTTP Request
- 🧾 Overview

This n8n workflow automates the process of fetching user data from an API, verifying its validity, transforming the response, and then saving it to Google Sheets for team collaboration. Ad...

### [Automated error monitoring and reporting system using data tables](https://n8n.io/workflows/12724-automated-error-monitoring-and-reporting-system-using-data-t)
- **ID:** 12724 | **Creator:** @harshalpatil | **Views:** 21 | **Nodes:** 5
- **Nodes:** Gmail, HTML, AI Agent +2 more
- Automated error monitoring and reporting system using data tables

This template helps you monitor workflow failures by automatically logging every error to a data table, then sending periodic summari...

### [Design scalable sync workflows with Data Tables, ProspectPro and HubSpot](https://n8n.io/workflows/13536-design-scalable-sync-workflows-with-data-tables-prospectpro)
- **ID:** 13536 | **Creator:** @olivier-nl ✓ | **Views:** 20 | **Nodes:** 4
- **Nodes:** HTTP Request, Telegram, HubSpot +1 more
- This template is a pattern library (one importable workflow) that shows a repeatable way to structure n8n automations so they remain easy to extend, cheaper to run, and safer to scale.

It’s intention...

### [Generate consensus-based answers using Claude, GPT, Grok and Gemini](https://n8n.io/workflows/12471-generate-consensus-based-answers-using-claude-gpt-grok-and-g)
- **ID:** 12471 | **Creator:** @egm-systems ✓ | **Views:** 19 | **Nodes:** 11
- **Nodes:** Slack, Telegram, Gmail +8 more
- The original LLM Council concept was introduced by Andrej Karpathy and published as an open-source repository demonstrating multi-model consensus and ranking.
This workflow is my adaptation of that or...

### [Learn JavaScript Data Processing with Code Node: Filtering, Analysis & Export Examples](https://n8n.io/workflows/5729-learn-javascript-data-processing-with-code-node-filtering-an)
- **ID:** 5729 | **Creator:** @dae221 ✓ | **Views:** 19 | **Nodes:** 1
- **Nodes:** Code
- Overview
A comprehensive educational workflow that demonstrates practical JavaScript usage in n8n's Code node through real-world business scenarios. Perfect for learning data manipulation, transformat...

### [Analyze GitLab CI job failures with GPT-5.3 and send reports to Slack](https://n8n.io/workflows/14129-analyze-gitlab-ci-job-failures-with-gpt-53-and-send-reports)
- **ID:** 14129 | **Creator:** @javdet ✓ | **Views:** 18 | **Nodes:** 6
- **Nodes:** HTTP Request, Slack, Code +3 more
- Overview
This workflow helps automatically analyze the causes of build failures in Gitlab CI and propose solutions without involving DevOps engineers.
See detailed setup guide

How it work
Checks whet...

### [Predict incidents and run autonomous remediation with GPT-4 and Slack](https://n8n.io/workflows/12686-predict-incidents-and-run-autonomous-remediation-with-gpt-4)
- **ID:** 12686 | **Creator:** @cschin ✓ | **Views:** 18 | **Nodes:** 11
- **Nodes:** Send Email, HTTP Request, Postgres +8 more
- How It Works
This workflow automates end-to-end customer journey management by intelligently routing queries through multiple AI models (OpenAI, Claude) based on complexity and context. Designed for c...

### [Deduplicate Data Records Using JavaScript Array Methods](https://n8n.io/workflows/5730-deduplicate-data-records-using-javascript-array-methods)
- **ID:** 5730 | **Creator:** @dae221 ✓ | **Views:** 17 | **Nodes:** 1
- **Nodes:** Code
- How It Works – Data Deduplication in n8n

This tutorial demonstrates how to remove duplicate records from a dataset using JavaScript logic inside n8n's Code nodes. It simulates real-world data cleanin...

### [Learn Secure Webhook APIs with Authentication and Supabase Integration](https://n8n.io/workflows/8258-learn-secure-webhook-apis-with-authentication-and-supabase-i)
- **ID:** 8258 | **Creator:** @nocodecreative ✓ | **Views:** 16 | **Nodes:** 1
- **Nodes:** Supabase
- This template is a practical introduction to n8n Webhooks with built-in examples for all major HTTP methods and authentication types. It is designed as a learning resource to help you understand how w...

### [Track Azure API and Service Bus failures with Application Insights correlation](https://n8n.io/workflows/12803-track-azure-api-and-service-bus-failures-with-application-in)
- **ID:** 12803 | **Creator:** @kramatic85 | **Views:** 16 | **Nodes:** 1
- **Nodes:** Code
- Track Azure API failures with Application Insights correlation

Template Name
Track Azure API failures with App Insights, APIM, and Service Bus correlation

Description

Troubleshoot failed API calls...

### [Analyze failed workflows with Claude via OpenRouter and log to Sheets with Slack, Email, Discord alerts](https://n8n.io/workflows/12502-analyze-failed-workflows-with-claude-via-openrouter-and-log)
- **ID:** 12502 | **Creator:** @openpaws ✓ | **Views:** 15 | **Nodes:** 8
- **Nodes:** Google Sheets, HTTP Request, Slack +5 more
- Who is this for

This workflow is designed for n8n users who manage multiple production workflows and want to:
Receive intelligent, actionable error alerts instead of raw stack traces
Understand root...

### [Build a full REST-API with n8n webhooks](https://n8n.io/workflows/12789-build-a-full-rest-api-with-n8n-webhooks)
- **ID:** 12789 | **Creator:** @cknoflac | **Views:** 15 | **Nodes:** 1
- **Nodes:** Code
- What is it?
A clean, extensible REST-style API routing template for n8n webhooks with up to 3 path levels.

How does it work?
Serves API routes via Webhooks with path variables

Normalizes incoming re...

### [Analyze domain threats via Telegram with VirusTotal, AbuseCH, and Gemini AI](https://n8n.io/workflows/13656-analyze-domain-threats-via-telegram-with-virustotal-abusech)
- **ID:** 13656 | **Creator:** @mtns | **Views:** 14 | **Nodes:** 3
- **Nodes:** HTTP Request, Telegram, Google Gemini
- Domain AI Analysis via Telegram, AbuseCH and VirusTotal

Workflow Description
This workflow allows Telegram users to submit a domain for quick threat intelligence analysis. It queries VirusTotal, Abu...

### [Auto-heal failing workflows with Azure OpenAI, n8n API, and Slack alerts](https://n8n.io/workflows/13791-auto-heal-failing-workflows-with-azure-openai-n8n-api-and-sl)
- **ID:** 13791 | **Creator:** @rahul08 ✓ | **Views:** 14 | **Nodes:** 6
- **Nodes:** HTTP Request, Slack, Code +3 more
- 📊 Description
Eliminate manual troubleshooting with an AI-powered autonomous recovery engine for n8n 🤖. This system monitors your entire n8n instance for failures, analyzes the root cause using Azure...

### [Add TypeScript Intellisense Support to Code Nodes with JSDoc](https://n8n.io/workflows/5602-add-typescript-intellisense-support-to-code-nodes-with-jsdoc)
- **ID:** 5602 | **Creator:** @wyeth ✓ | **Views:** 14 | **Nodes:** 1
- **Nodes:** Code
- Are you writing complex Code nodes and need Intellisense support? Follow this simple pattern to get autocomplete for any n8n or custom classes.

### [Production AI Playbook: Deterministic Steps & AI Steps (4 of 5)](https://n8n.io/workflows/13853-production-ai-playbook-deterministic-steps-and-ai-steps-4-of)
- **ID:** 13853 | **Creator:** @elvissaravia ✓ | **Views:** 13 | **Nodes:** 4
- **Nodes:** Code, AI Agent, OpenAI Chat Model +1 more
- Protect your workflows with n8n's native Guardrails node, placed before and after your AI step. The input guardrails catch jailbreak attempts and PII before they reach your model. The output guardrail...

### [Dynamic AI Model Selector with GDPR Compliance via Requesty and Google Sheets](https://n8n.io/workflows/5862-dynamic-ai-model-selector-with-gdpr-compliance-via-requesty)
- **ID:** 5862 | **Creator:** @stefan ✓ | **Views:** 12 | **Nodes:** 5
- **Nodes:** Google Sheets, HTTP Request, Code +2 more
- Overview
This comprehensive n8n workflow provides a sophisticated solution for dynamically selecting and using AI models while maintaining GDPR compliance. It leverages Requesty's European-based AI ro...

### [Scan Gmail links with VirusTotal and send alerts to WhatsApp, Teams, and Sheets](https://n8n.io/workflows/13581-scan-gmail-links-with-virustotal-and-send-alerts-to-whatsapp)
- **ID:** 13581 | **Creator:** @spagreen ✓ | **Views:** 12 | **Nodes:** 4
- **Nodes:** Google Sheets, HTTP Request, Microsoft Teams +1 more
- Who it's for
This n8n workflow is designed for IT security professionals, email administrators, and organizations that want to automatically scan URLs received in emails for potential security threats...

### [Daily Workflow Backups to GitHub with Slack Notifications](https://n8n.io/workflows/5851-daily-workflow-backups-to-github-with-slack-notifications)
- **ID:** 5851 | **Creator:** @boanse ✓ | **Views:** 11 | **Nodes:** 4
- **Nodes:** GitHub, HTTP Request, Slack +1 more
- Who is this for?
This workflow is ideal for n8n self-hosted users, DevOps engineers, and automation developers who want to automatically back up their n8n workflows to GitHub on a regular basis.

What...

### [Manage healthcare resource allocation and conflicts with Anthropic Claude](https://n8n.io/workflows/12794-manage-healthcare-resource-allocation-and-conflicts-with-ant)
- **ID:** 12794 | **Creator:** @cschin ✓ | **Views:** 10 | **Nodes:** 7
- **Nodes:** HTTP Request, Code, AI Agent +4 more
- How It Works
This workflow automates end-to-end marketing campaign management for digital marketing teams and agencies executing multi-channel strategies. It solves the complex challenge of coordinati...

### [Generate Security Vulnerability Reports with Google Dorks, SerpAPI and PDF4me](https://n8n.io/workflows/11195-generate-security-vulnerability-reports-with-google-dorks-se)
- **ID:** 11195 | **Creator:** @knute ✓ | **Views:** 9 | **Nodes:** 2
- **Nodes:** Gmail, Code
- Google Dorks with SerpAPI

How it Works:
Accepts a domain from a web form
Generates a list of Google dorks targeting that domain
Scrapes Google search results for each dork using SerpAPI
Filters out j...

### [Orchestrate AI risk analysis and severity-based routing with Anthropic and OpenAI](https://n8n.io/workflows/12992-orchestrate-ai-risk-analysis-and-severity-based-routing-with)
- **ID:** 12992 | **Creator:** @cschin ✓ | **Views:** 9 | **Nodes:** 7
- **Nodes:** HTTP Request, Code, AI Agent +4 more
- How It Works
This workflow automates complex data engineering operations by orchestrating multiple specialized AI agents to analyze datasets, calculate risk metrics, and route findings based on severi...

### [IP Threat Intelligence Report Generator with VirusTotal, OpenAI and Google Docs](https://n8n.io/workflows/10868-ip-threat-intelligence-report-generator-with-virustotal-open)
- **ID:** 10868 | **Creator:** @knute ✓ | **Views:** 8 | **Nodes:** 4
- **Nodes:** HTTP Request, Google Docs, AI Agent +1 more
- Cybersec IP Intelligence Gatherer
This project utilizes the VirusTotal node and Geolocation node to thoroughly gather data on a provided IP address. 

From there a LLM AI assistant will assess the gat...

### [UptimeRobot Alerts to Telegram with Visual Verification](https://n8n.io/workflows/5780-uptimerobot-alerts-to-telegram-with-visual-verification)
- **ID:** 5780 | **Creator:** @vminev ✓ | **Views:** 7 | **Nodes:** 5
- **Nodes:** HTTP Request, Telegram, Crypto +2 more
- UptimeRobot Alerts to Telegram with Visual Verification
Automatically sends Telegram notifications with optional screenshots when monitors change status (✅ UP/🔴 DOWN/⏸️ PAUSED)

Example Message in Tel...

### [Generate Dynamic JSON Output Formats for AI Agents with Mistral](https://n8n.io/workflows/5829-generate-dynamic-json-output-formats-for-ai-agents-with-mist)
- **ID:** 5829 | **Creator:** @hybroht ✓ | **Views:** 7 | **Nodes:** 3
- **Nodes:** AI Agent, Structured Output Parser, Mistral Cloud Chat Model
- This workflow contains community nodes that are only compatible with the self-hosted version of n8n.

JSON Architect - Dynamically Generate JSON Output Formats for Any AI Agent

Overview 
Version: 1.0...

### [Automated Website Uptime Monitor with Email Alerts & GitHub Status Page Update](https://n8n.io/workflows/8624-automated-website-uptime-monitor-with-email-alerts-and-githu)
- **ID:** 8624 | **Creator:** @linearloop | **Views:** 6 | **Nodes:** 4
- **Nodes:** GitHub, HTTP Request, Gmail +1 more
- 🖥️ Automated Website Uptime Monitor with Email Alerts & GitHub Status Page Update  

This n8n workflow continuously monitors your website’s availability, sends email alerts when the server goes down,...

### [Monitor & Manage Docker Containers with Telegram Bot & AI Log Analysis](https://n8n.io/workflows/10476-monitor-and-manage-docker-containers-with-telegram-bot-and-a)
- **ID:** 10476 | **Creator:** @macoso | **Views:** 5 | **Nodes:** 3
- **Nodes:** Telegram, Code, OpenAI
- Monitor and manage Docker containers from Telegram with AI log analysis

This workflow gives you a smart Telegram command center for your homelab. It lets you monitor Docker containers, get alerts the...

### [Generate Google Sheets test script from Pega Agile Studio user stories with AI](https://n8n.io/workflows/13093-generate-google-sheets-test-script-from-pega-agile-studio-us)
- **ID:** 13093 | **Creator:** @rnijsten ✓ | **Views:** 5 | **Nodes:** 5
- **Nodes:** Google Sheets, HTTP Request, Code +2 more
- Generate Google Spreadsheets Testscript with AI using Pega Agile Studio
When working as a functional Pega Software tester, this workflow will create a Google Spreadsheet with acceptance criteria and t...

### [Secure User Emails with AES-256 Encryption and Verification System](https://n8n.io/workflows/5733-secure-user-emails-with-aes-256-encryption-and-verification)
- **ID:** 5733 | **Creator:** @dae221 ✓ | **Views:** 4 | **Nodes:** 1
- **Nodes:** Code
- 🔐 Email Encryption Masterclass
Professional-Grade AES-256 Data Protection for n8n

How It Works

This comprehensive workflow demonstrates enterprise-level email encryption using industry-standard AES-...

### [Get domain expiry reminders with Google Sheets, WHOIS, Telegram, and Ollama AI](https://n8n.io/workflows/12387-get-domain-expiry-reminders-with-google-sheets-whois-telegra)
- **ID:** 12387 | **Creator:** @cahya ✓ | **Views:** 4 | **Nodes:** 6
- **Nodes:** Google Sheets, HTTP Request, Telegram +3 more
- This workflow helps you monitor domain expiration dates and send automated reminders via Telegram when a domain is about to expire or has already expired, using WHOIS data and AI-powered information e...

### [Create an Offline DIGIPIN Microservice API for Precise Location Mapping in India](https://n8n.io/workflows/5836-create-an-offline-digipin-microservice-api-for-precise-locat)
- **ID:** 5836 | **Creator:** @srinivasankb ✓ | **Views:** 4 | **Nodes:** 1
- **Nodes:** Code
- This workflow contains community nodes that are only compatible with the self-hosted version of n8n.

What is DIGIPIN?
DIGIPIN (Digital Pincode) is a 10-character alphanumeric code introduced by India...

### [Unify multiple triggers into a single workflow](https://n8n.io/workflows/7784-unify-multiple-triggers-into-a-single-workflow)
- **ID:** 7784 | **Creator:** @duv ✓ | **Views:** 4 | **Nodes:** 3
- **Nodes:** Slack, Basic LLM Chain, OpenAI Chat Model
- Stop duplicating your work! This template demonstrates a powerful design pattern to handle multiple triggers (e.g., Form, Webhook, Sub-workflow) within a single, unified workflow. 

By using a "norma...

### [Monitor Workflow Audits and Failures with InfluxDB Dashboard](https://n8n.io/workflows/5873-monitor-workflow-audits-and-failures-with-influxdb-dashboard)
- **ID:** 5873 | **Creator:** @lukaszpp ✓ | **Views:** 4 | **Nodes:** 1
- **Nodes:** HTTP Request
- Who is it for
This workflow is for anyone who is using N8N. It's especially helpful if you are a DevOps and your N8N instance is self hosted. If you carea lot about security and number of failed execu...

### [ETL: Extract and Parse Revit Model Data to Structured Excel](https://n8n.io/workflows/7654-etl-extract-and-parse-revit-model-data-to-structured-excel)
- **ID:** 7654 | **Creator:** @datadrivenconstruction ✓ | **Views:** 4 | **Nodes:** 0
- **Nodes:** 
- Convert a Revit model to Excel and parse it into structured items ready for downstream ETL.
This minimal template runs a local RvtExporter.exe, checks success, derives the expected *_rvt.xlsx filename...

### [Fetch Hierarchical Data Records from Airtable with Multi-level Relationships](https://n8n.io/workflows/5750-fetch-hierarchical-data-records-from-airtable-with-multi-lev)
- **ID:** 5750 | **Creator:** @valerian | **Views:** 4 | **Nodes:** 3
- **Nodes:** Airtable, HTTP Request, Code
- Airtable Hierarchical Record Fetcher

Description

This n8n workflow retrieves an Airtable record along with its related child records in a hierarchical structure. It can fetch up to 3 levels of linke...

### [Automate Security Alert Triage with NixGuard AI and Route to Slack or Jira](https://n8n.io/workflows/5896-automate-security-alert-triage-with-nixguard-ai-and-route-to)
- **ID:** 5896 | **Creator:** @nex ✓ | **Views:** 3 | **Nodes:** 2
- **Nodes:** Slack, Code
- Are you drowning in a sea of security notifications? Do your analysts spend more time sifting through low-level logs than investigating real threats? This workflow transforms n8n into an autonomous SO...

### [Web Security Scanner for OWASP Compliance with Markdown Reports](https://n8n.io/workflows/10898-web-security-scanner-for-owasp-compliance-with-markdown-repo)
- **ID:** 10898 | **Creator:** @knute ✓ | **Views:** 3 | **Nodes:** 3
- **Nodes:** HTTP Request, Gmail, Code
- How the n8n OWASP Scanner Works & How to Set It Up

How It Works (Simple Flow):
Input**: Enter target URL + endpoint (e.g., https://example.com, /login)
Scan**: This workflow executes 5 parallel HTTP...

### [Automatic Google Cloud Run Auth with JWT Token Management (sub-workflow)](https://n8n.io/workflows/7569-automatic-google-cloud-run-auth-with-jwt-token-management-su)
- **ID:** 7569 | **Creator:** @marcocassar ✓ | **Views:** 3 | **Nodes:** 2
- **Nodes:** HTTP Request, JWT
- Who it’s for? 
Anyone calling a Google Cloud Run service from n8n who wants a small, reusable auth layer instead of wiring tokens in every workflow.

What it does / How it works
This sub-workflow chec...

### [Generate workflow JSON files from webhook prompts using Azure OpenAI GPT-4o-mini](https://n8n.io/workflows/13787-generate-workflow-json-files-from-webhook-prompts-using-azur)
- **ID:** 13787 | **Creator:** @rahul08 ✓ | **Views:** 3 | **Nodes:** 3
- **Nodes:** Code, AI Agent, Azure OpenAI Chat Model
- 📊 Description
Automate the creation of production-ready n8n workflows using AI 🤖. This template receives a plain-text automation idea via webhook, processes it with Azure OpenAI, and instantly generat...

### [Sync Android env config to Gradle files with GitHub and Slack alerts](https://n8n.io/workflows/12873-sync-android-env-config-to-gradle-files-with-github-and-slac)
- **ID:** 12873 | **Creator:** @weblineindia ✓ | **Views:** 3 | **Nodes:** 4
- **Nodes:** GitHub, HTTP Request, Slack +1 more
- Environment Config Diff & Propagate for Android Builds

This workflow automatically detects changes in the .env.staging file in a GitHub repository and keeps Android configuration files (build.gradle...

### [Perform Multi-type DNS Lookups with Google's Free Public DNS Service](https://n8n.io/workflows/10200-perform-multi-type-dns-lookups-with-googles-free-public-dns)
- **ID:** 10200 | **Creator:** @ossian ✓ | **Views:** 3 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- This n8n template makes it easy to perform DNS lookups directly within your n8n workflow using dns.google, without any API credentials.

Use Cases

Track changes:** Schedule execution and log DNS answ...

### [Securely Call Private Google Cloud Run APIs with JWT Authentication (Simplified)](https://n8n.io/workflows/7571-securely-call-private-google-cloud-run-apis-with-jwt-authent)
- **ID:** 7571 | **Creator:** @marcocassar ✓ | **Views:** 2 | **Nodes:** 2
- **Nodes:** HTTP Request, JWT
- Who it’s for? 
Anyone who wants a dead-simple, free-tier friendly way to run custom API logic on Google Cloud Run and call it securely from n8n—no public exposure, no local hosting.

What it does 
Min...

### [Automatic Typebot Flows Two-Way Sync with GitHub using Typebot API](https://n8n.io/workflows/5899-automatic-typebot-flows-two-way-sync-with-github-using-typeb)
- **ID:** 5899 | **Creator:** @marskdev | **Views:** 2 | **Nodes:** 3
- **Nodes:** GitHub, HTTP Request, Code
- Remixed Backup your workflows to GitHub from Solomon's work. Check out his templates.

How it works
This workflow will backup your typebots to GitHub. It uses the Typebot API to export all typebots....

### [Automated n8n Workflow Backup to GitHub with Deletion Tracking](https://n8n.io/workflows/5898-automated-n8n-workflow-backup-to-github-with-deletion-tracki)
- **ID:** 5898 | **Creator:** @marskdev | **Views:** 2 | **Nodes:** 3
- **Nodes:** GitHub, HTTP Request, Code
- Remixed Backup your workflows to GitHub from Solomon's work. Check out his templates.

How it works
This workflow will backup your workflows to GitHub. It uses the n8n API node to export all workflows...

### [Convert Revit Projects to Database with Drawings & Specifications using DDC](https://n8n.io/workflows/7649-convert-revit-projects-to-database-with-drawings-and-specifi)
- **ID:** 7649 | **Creator:** @datadrivenconstruction ✓ | **Views:** 2 | **Nodes:** 0
- **Nodes:** 
- Turn a .rvt project into open, analysis-ready data (XLSX + optional DAE/PDF) using the RvtExporter.exe from the DDC Revit toolkit. This n8n template provides a Form UI to set paths and flags, then run...

### [Monitor Azure subscription resources with cost and usage tracking and reports](https://n8n.io/workflows/12802-monitor-azure-subscription-resources-with-cost-and-usage-tra)
- **ID:** 12802 | **Creator:** @kramatic85 | **Views:** 2 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- Monitor Azure subscription resources with cost and usage tracking

Template Name
Monitor Azure subscription resources with cost and usage tracking

Description

Automatically connect to your Azure sub...

### [Magento Maintenance via Natural Language with GPT and Telegram/WhatsApp](https://n8n.io/workflows/10268-magento-maintenance-via-natural-language-with-gpt-and-telegr)
- **ID:** 10268 | **Creator:** @kmyprojects ✓ | **Views:** 2 | **Nodes:** 6
- **Nodes:** HTTP Request, Telegram, WhatsApp Business Cloud +3 more
- The Magento 2 Smart Maintenance AI Agent revolutionises how you interact with your store’s backend — allowing you to safely run critical maintenance and cache operations using plain natural language v...

### [Automated Error Notifications with Optional GPT-4o Diagnostics via Email](https://n8n.io/workflows/11507-automated-error-notifications-with-optional-gpt-4o-diagnosti)
- **ID:** 11507 | **Creator:** @coolchandan62 ✓ | **Views:** 2 | **Nodes:** 2
- **Nodes:** Send Email, OpenAI
- ++Who’s it for++

This template is ideal for anyone who needs reliable, real-time visibility into failed executions in n8n. Whether you’re a developer, operator, founder, or part of a small team, this...

### [Prevent duplicate webhook executions with AARI idempotency gate](https://n8n.io/workflows/13863-prevent-duplicate-webhook-executions-with-aari-idempotency-g)
- **ID:** 13863 | **Creator:** @neshkito | **Views:** 2 | **Nodes:** 1
- **Nodes:** HTTP Request
- Who this template is for

This template is for anyone running n8n workflows that receive webhooks and perform side effects such as payments, emails, database inserts, or API calls.

Webhook providers...

### [Auto CVE & IOC Feed Ingestor with OpenAI Risk Triage & Email Alerts](https://n8n.io/workflows/6356-auto-cve-and-ioc-feed-ingestor-with-openai-risk-triage-and-e)
- **ID:** 6356 | **Creator:** @adnantariq ✓ | **Views:** 2 | **Nodes:** 4
- **Nodes:** Send Email, Google Sheets, HTTP Request +1 more
- How it works  
This Blue Team workflow ingests threat intelligence from public CVE and IOC feeds, merges the data, performs automated triage using OpenAI, and routes actionable alerts via email.

📥 CV...

### [Validate student progress and orchestrate interventions with Claude and email](https://n8n.io/workflows/13156-validate-student-progress-and-orchestrate-interventions-with)
- **ID:** 13156 | **Creator:** @cschin ✓ | **Views:** 2 | **Nodes:** 6
- **Nodes:** Send Email, HTTP Request, Code +3 more
- How It Works
This workflow automates student progress monitoring and academic intervention orchestration through intelligent AI-driven analysis. Designed for educational institutions, learning managem...

### [Generate multi-pass Seedance AI roto mattes with QC and Nuke handoff](https://n8n.io/workflows/14390-generate-multi-pass-seedance-ai-roto-mattes-with-qc-and-nuke)
- **ID:** 14390 | **Creator:** @rahul08 ✓ | **Views:** 2 | **Nodes:** 6
- **Nodes:** HTTP Request, Slack, Telegram +3 more
- 📘 Description
This workflow is an AI-powered roto matte generation and first-pass compositing pipeline designed for VFX production. It transforms structured roto requests into multiple high-precision...

### [Subdomain Enumeration with Subfinder, HTTPX & GPT-4-Mini for Security Reconnaissance](https://n8n.io/workflows/9735-subdomain-enumeration-with-subfinder-httpx-and-gpt-4-mini-fo)
- **ID:** 9735 | **Creator:** @pyus3r ✓ | **Views:** 1 | **Nodes:** 3
- **Nodes:** HTTP Request, Code, OpenAI
- Generates a wordlist of 1,000–15,000 subdomains created by an AI agent by correlating detected technologies and recurring patterns.
Objective
Assist security researchers, bug bounty hunters, and web p...

### [Score DNS threats with VirusTotal, Abuse.ch, HashiCorp Vault and Gemini](https://n8n.io/workflows/14127-score-dns-threats-with-virustotal-abusech-hashicorp-vault-an)
- **ID:** 14127 | **Creator:** @lukaszfd | **Views:** 1 | **Nodes:** 7
- **Nodes:** Send Email, HTTP Request, MongoDB +4 more
- Stop fighting alerts and start orchestrating intelligence.

This workflow is a complete ecosystem designed to combat network threats in real-time. It transforms raw DNS logs into structured knowledge,...

### [Predictive Health Monitoring & Alert System with GPT-4o-mini](https://n8n.io/workflows/10457-predictive-health-monitoring-and-alert-system-with-gpt-4o-mi)
- **ID:** 10457 | **Creator:** @cschin ✓ | **Views:** 1 | **Nodes:** 11
- **Nodes:** Send Email, HTTP Request, Postgres +8 more
- How It Works
The system collects real-time wearable health data, normalizes it, and uses AI to analyze trends and risk scores. It detects anomalies by comparing with historical patterns and automatica...

### [Back up self-hosted workflows to Google Drive daily with change detection](https://n8n.io/workflows/12242-back-up-self-hosted-workflows-to-google-drive-daily-with-cha)
- **ID:** 12242 | **Creator:** @coolchandan62 ✓ | **Views:** 1 | **Nodes:** 4
- **Nodes:** HTTP Request, Google Drive, Crypto +1 more
- This workflow creates a daily, automated backup of all workflows in a self-hosted n8n instance and stores them in Google Drive. Instead of exporting every workflow on every run, it uses content hashin...

### [Securely Call Google Cloud Run APIs with Service Account Auth (main-workflow)](https://n8n.io/workflows/7568-securely-call-google-cloud-run-apis-with-service-account-aut)
- **ID:** 7568 | **Creator:** @marcocassar ✓ | **Views:** 1 | **Nodes:** 1
- **Nodes:** HTTP Request
- Who it’s for? 
Anyone who wants a simple, secure way to call a Google Cloud Run endpoint from n8n—without exposing it publicly. 

People who want a cheap/free-tier way to run custom API logic without...

### [Check workflow templates against Creator Hub guidelines with Gemini and Gmail](https://n8n.io/workflows/13769-check-workflow-templates-against-creator-hub-guidelines-with)
- **ID:** 13769 | **Creator:** @okp29 ✓ | **Views:** 1 | **Nodes:** 5
- **Nodes:** HTTP Request, Gmail, Code +2 more
- Who is this for

Template creators who want to validate their n8n workflows against the official Creator Hub approval criteria before submitting. Useful for both new and verified creators looking to r...

### [Convert Task Ideas to Implementation Plans with GPT-4o, Slack & Google Sheets](https://n8n.io/workflows/11362-convert-task-ideas-to-implementation-plans-with-gpt-4o-slack)
- **ID:** 11362 | **Creator:** @nakayama ✓ | **Views:** 1 | **Nodes:** 6
- **Nodes:** Google Sheets, Slack, Google Tasks +3 more
- 🚀 Turn your random ideas into concrete automation specs

This workflow acts as your interactive "n8n Consultant." Simply write down a rough automation idea in Google Tasks (e.g., "Send weather updates...

### [Monitor GitHub repo access and push events with GitHub and Slack alerts](https://n8n.io/workflows/12336-monitor-github-repo-access-and-push-events-with-github-and-s)
- **ID:** 12336 | **Creator:** @rams1005 ✓ | **Views:** 1 | **Nodes:** 3
- **Nodes:** HTTP Request, Slack, Code
- Monitor GitHub Repositories for Unauthorized Actions

How it works:

This workflow monitors GitHub for high-risk activities to ensure that only authorized users can modify the repository. It periodic...

### [Enrich IP addresses with country attribution using IPinfo and Slack alerts](https://n8n.io/workflows/13239-enrich-ip-addresses-with-country-attribution-using-ipinfo-an)
- **ID:** 13239 | **Creator:** @eedson ✓ | **Views:** 1 | **Nodes:** 3
- **Nodes:** HTTP Request, Slack, Code
- 🧩 Template Description

IP Enrichment & Country Attribution is a lightweight cybersecurity automation that enriches IP addresses with geographic and network intelligence. It validates incoming IPs, fi...

### [Discord Server Anti-Impersonation / Scammer Tracker with Data Tables](https://n8n.io/workflows/11812-discord-server-anti-impersonation-scammer-tracker-with-dat)
- **ID:** 11812 | **Creator:** @elijahbuilds-ai ✓ | **Views:** 1 | **Nodes:** 1
- **Nodes:** Discord
- Discord Member Change Tracker

This n8n template demonstrates how to automatically monitor and track username and nickname changes across your Discord server members. Perfect for community moderation,...

### [Monitor [PROD] workflows in real time with the n8n Public API dashboard](https://n8n.io/workflows/13665-monitor-prod-workflows-in-real-time-with-the-n8n-public-api)
- **ID:** 13665 | **Creator:** @lucashideki ✓ | **Views:** 1 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- A real-time monitoring dashboard for your n8n production workflows, accessible directly from the browser via webhook.

Tag any workflow with [PROD] and it will automatically appear on the dashboard sh...

### [Decide multi‑agent vs simple workflows using Azure OpenAI GPT‑4o‑mini](https://n8n.io/workflows/13792-decide-multiagent-vs-simple-workflows-using-azure-openai-gpt)
- **ID:** 13792 | **Creator:** @rahul08 ✓ | **Views:** 1 | **Nodes:** 3
- **Nodes:** Code, AI Agent, Azure OpenAI Chat Model
- 📘 Description
This workflow acts as an AI Multi-Agent Architecture Advisor for n8n. It receives a problem statement via webhook, uses Azure OpenAI (gpt-4o-mini) to decide whether the problem needs a m...

### [Evaluate AI workflows using Google Sheets, Gemini, Claude, GPT, and Perplexity](https://n8n.io/workflows/12644-evaluate-ai-workflows-using-google-sheets-gemini-claude-gpt)
- **ID:** 12644 | **Creator:** @ryanandmattdatascience | **Views:** 1 | **Nodes:** 8
- **Nodes:** Gmail, AI Agent, Summarization Chain +5 more
- This template and YouTube video goes over
5 different implementations of evaluations within n8n.

Categorization
Correctness
Tools used
String similarity
Helpfulness

You’ll learn when to use each typ...

### [Compare GPT-4, Claude & Gemini Responses with Contextual AI's LMUnit Evaluation](https://n8n.io/workflows/11618-compare-gpt-4-claude-and-gemini-responses-with-contextual-ai)
- **ID:** 11618 | **Creator:** @jinash ✓ | **Views:** 1 | **Nodes:** 4
- **Nodes:** Code, OpenAI, Google Gemini +1 more
- PROBLEM  
Evaluating and comparing responses from multiple LLMs (OpenAI, Claude, Gemini) can be challenging when done manually.  
Each model produces outputs that differ in clarity, tone, and reasonin...

### [Convert CDP Network Topology to Lucidchart Prompts with AWX and Gemini AI](https://n8n.io/workflows/11537-convert-cdp-network-topology-to-lucidchart-prompts-with-awx)
- **ID:** 11537 | **Creator:** @gustavo-dorantes | **Views:** 1 | **Nodes:** 4
- **Nodes:** HTTP Request, Google Docs, Code +1 more
- AI NETWORK DIAGRAM PROMPT GENERATOR

Template Description

This workflow automates the creation of network diagram prompts using AI. It retrieves Layer-2 topology data from AWX, parses device relation...

### [Multi-AI Agent Router: Compare OpenAI, Anthropic & Groq Responses with Webhooks](https://n8n.io/workflows/10287-multi-ai-agent-router-compare-openai-anthropic-and-groq-resp)
- **ID:** 10287 | **Creator:** @cschin ✓ | **Views:** 1 | **Nodes:** 6
- **Nodes:** Code, AI Agent, Anthropic Chat Model +3 more
- Introduction
This workflow connects to OpenAI, Anthropic, and Groq, processing requests in parallel with automatic performance metrics. Ideal for testing speed, cost, and quality across models.
How It...

### [Secure AI agent webhook with HMAC, replay protection, and OpenAI GPT-5](https://n8n.io/workflows/14486-secure-ai-agent-webhook-with-hmac-replay-protection-and-open)
- **ID:** 14486 | **Creator:** @dataki ✓ | **Views:** 1 | **Nodes:** 4
- **Nodes:** Crypto, Code, AI Agent +1 more
- ⚠️ Disclaimer: 
&gt; I am not a cybersecurity expert. 
This workflow was built through research and with the assistance of an LLM (Claude Opus 4.6). 
While it implements well-established security patt...

### [Complete AI Safety Suite: Test 9 Guardrail Layers with Groq LLM](https://n8n.io/workflows/11141-complete-ai-safety-suite-test-9-guardrail-layers-with-groq-l)
- **ID:** 11141 | **Creator:** @shaheer03 ✓ | **Views:** 1 | **Nodes:** 2
- **Nodes:** Groq Chat Model, Guardrails
- Who's It For
AI developers, automation engineers, and teams building chatbots, AI agents, or workflows that process user input. Perfect for those concerned about security, compliance, and content safe...

### [Route AI tasks between OpenAI agents with confidence-based email fallback](https://n8n.io/workflows/13965-route-ai-tasks-between-openai-agents-with-confidence-based-e)
- **ID:** 13965 | **Creator:** @rnair1996 ✓ | **Views:** 1 | **Nodes:** 5
- **Nodes:** Send Email, AI Agent, OpenAI Chat Model +2 more
- Overview

This workflow demonstrates an AI task routing system using multiple agents in n8n. It analyzes incoming user requests, determines their complexity, and routes them to the most appropriate AI...

### [Migrate large Hugging Face datasets to MongoDB with a looping subworkflow](https://n8n.io/workflows/12338-migrate-large-hugging-face-datasets-to-mongodb-with-a-loopin)
- **ID:** 12338 | **Creator:** @mohelwah ✓ | **Views:** 1 | **Nodes:** 3
- **Nodes:** HTTP Request, MongoDB, Code
- This n8n template provides a production-ready, memory-safe pipeline for ingesting large Hugging Face datasets into MongoDB using batch pagination.  
It is designed as a reusable data ingestion layer...

### [Process multiple requests in FIFO using OpenAI Batch API and Supabase/Postgres](https://n8n.io/workflows/13238-process-multiple-requests-in-fifo-using-openai-batch-api-and)
- **ID:** 13238 | **Creator:** @twh | **Views:** 1 | **Nodes:** 4
- **Nodes:** HTTP Request, Postgres, Supabase +1 more
- How it works
You provide a list of prompts and a system instruction, the workflow batches them into a single OpenAI Batch API request.
The batch job is tracked in a Supabase openai_batches table.
A cr...

### [Automatically Optimize AI Prompts with OpenAI Using OPRO & DSPy Methodology](https://n8n.io/workflows/11495-automatically-optimize-ai-prompts-with-openai-using-opro-and)
- **ID:** 11495 | **Creator:** @nakayama ✓ | **Views:** 1 | **Nodes:** 4
- **Nodes:** Code, AI Agent, OpenAI Chat Model +1 more
- This workflow implements cutting-edge concepts from Google DeepMind's OPRO (Optimization by PROmpting) and Stanford's DSPy to automatically refine AI prompts. It iteratively generates, evaluates, and...

### [Automate Vulnerability Triage from Snyk with Jira, Slack & Airtable Integration](https://n8n.io/workflows/11824-automate-vulnerability-triage-from-snyk-with-jira-slack-and)
- **ID:** 11824 | **Creator:** @weblineindia ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Airtable, Slack, Jira Software +1 more
- Snyk Vulnerability Automation Workflow with Webhook, Jira, Slack & Airtable

This workflow receives vulnerability data(e.g., Snyk, Dependabot or any security scanner) from Snyk through a webhook, stan...

### [Monitor CISA Critical Vulnerability Alerts with RSS Feed & Slack Notifications](https://n8n.io/workflows/6724-monitor-cisa-critical-vulnerability-alerts-with-rss-feed-and)
- **ID:** 6724 | **Creator:** @marth ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** Slack, Code
- How It Works: The 5-Node Monitoring Flow

This concise workflow efficiently captures, filters, and delivers crucial cybersecurity-related mentions.

1. Monitor: Cybersecurity Keywords (X/Twitter Trigg...

### [Aggregate Endpoint Security Risk Scores with EDR, Vulnerability Data & Google Sheets](https://n8n.io/workflows/6411-aggregate-endpoint-security-risk-scores-with-edr-vulnerabili)
- **ID:** 6411 | **Creator:** @adnantariq ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** Google Sheets, HTTP Request
- 👤 Who it’s for
Security teams, SOC analysts, and small-to-mid IT teams looking to automatically assess endpoint risk by combining known vulnerabilities with internal asset value and dynamic threat ind...

### [AI-Powered Vulnerability Scanner with Nessus, Risk Triage & Google Sheets Reporting](https://n8n.io/workflows/6293-ai-powered-vulnerability-scanner-with-nessus-risk-triage-and)
- **ID:** 6293 | **Creator:** @adnantariq ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Send Email, Google Sheets, HTTP Request +1 more
- 🛡 CyberScan – AI-Powered Vulnerability Scanner with Nessus, OpenAI, and Google Sheets

👤 Who’s it for

Security teams, DevOps engineers, vulnerability analysts, and automation builders who want to eli...

### [Real-Time Security Threat Dashboard with Google Sheets, AI Risk Analysis & Email Alerts](https://n8n.io/workflows/6415-real-time-security-threat-dashboard-with-google-sheets-ai-ri)
- **ID:** 6415 | **Creator:** @adnantariq ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Send Email, Google Sheets, HTTP Request +1 more
- 👤 Who it’s for
Blue Team leads, CISOs, and SOC managers who want automated visibility into threat metrics, endpoint alerts, and response actions — without needing a full SIEM or BI platform.

Great fo...

### [Monitor zero-day threats with Anthropic Claude, Airtable, Slack and Jira](https://n8n.io/workflows/13692-monitor-zero-day-threats-with-anthropic-claude-airtable-slac)
- **ID:** 13692 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 7
- **Nodes:** Airtable, Send Email, Google Sheets +4 more
- This workflow continuously monitors CVE databases, threat intelligence feeds, and public security advisories to surface emerging zero-day threats, correlates them against your registered infrastructur...

### [Scan URLs for Security Threats with urlscan.io and GPT-4o mini](https://n8n.io/workflows/7159-scan-urls-for-security-threats-with-urlscanio-and-gpt-4o-min)
- **ID:** 7159 | **Creator:** @ca7ai ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Gmail, urlscan.io, OpenAI
- How it works
• Webhook → urlscan.io → GPT-4o mini → Gmail  
• Payload example: { "url": "https://example.com" }  
• urlscan.io returns a Scan ID and raw JSON.  
• AI node classifies the scan as malici...

### [Real-Time IoT Incident Management with Jira & Slack Technician Alerts](https://n8n.io/workflows/11946-real-time-iot-incident-management-with-jira-and-slack-techni)
- **ID:** 11946 | **Creator:** @weblineindia ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Slack, Jira Software, Code
- Webhook from IoT Devices → Jira Maintenance Ticket → Slack Factory Alert


This workflow automates predictive maintenance by receiving IoT machine-failure webhooks, creating Jira maintenance tickets,...

### [Automate Security Incident Response with Google Sheets, Email Alerts and EDR Isolation](https://n8n.io/workflows/6413-automate-security-incident-response-with-google-sheets-email)
- **ID:** 6413 | **Creator:** @adnantariq ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Send Email, Google Sheets, HTTP Request
- 👤 Who it’s for
SOC teams, incident responders, or solo defenders who need to automatically act on critical threats without manual triage.

Ideal for BlueOps users who’ve already classified alerts via...

### [Monitor workflow errors with n8n API, log to Google Sheets, and alert via Slack](https://n8n.io/workflows/14964-monitor-workflow-errors-with-n8n-api-log-to-google-sheets-an)
- **ID:** 14964 | **Creator:** @ahmadbukhari | **Views:** 0 | **Nodes:** 3
- **Nodes:** HTTP Request, Slack, Code
- Who is this for?

This workflow is built for n8n admins, automation agencies, solopreneurs, and ops teams running multiple workflows in production who need to know the moment something breaks.

If you...

### [Review GitHub pull requests with AI and log results to PostgreSQL and Slack](https://n8n.io/workflows/13652-review-github-pull-requests-with-ai-and-log-results-to-postg)
- **ID:** 13652 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** HTTP Request, Postgres, Code
- Automatically detects new GitHub Pull Requests, analyzes changed code with AI, generates detailed review comments (quality, security, performance, best practices), posts suggestions back to the PR, st...

### [Check phishing URL reputation with VirusTotal and log to Google Sheets](https://n8n.io/workflows/13448-check-phishing-url-reputation-with-virustotal-and-log-to-goo)
- **ID:** 13448 | **Creator:** @eedson ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Google Sheets, HTTP Request, Code
- 🐟 Phishing URL Reputation Checker with VirusTotal

This n8n template helps you automatically analyze URLs for phishing and malicious activity using VirusTotal’s multi-engine threat intelligence platfo...

### [Validate GitHub Configurations with GPT-4o-mini and Log Issues to Sheets and Slack](https://n8n.io/workflows/10329-validate-github-configurations-with-gpt-4o-mini-and-log-issu)
- **ID:** 10329 | **Creator:** @rahul08 ✓ | **Views:** 0 | **Nodes:** 8
- **Nodes:** GitHub, Google Sheets, Slack +5 more
- 📊 Description
Ensure your GitHub repositories stay configuration-accurate and documentation-compliant with this intelligent AI-powered validation workflow. 🤖
This automation monitors repository update...

### [Audit workflow credential usage to Google Sheets using Google Drive and SQLite3](https://n8n.io/workflows/14423-audit-workflow-credential-usage-to-google-sheets-using-googl)
- **ID:** 14423 | **Creator:** @zmglobalit ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Google Sheets, HTTP Request, Google Drive +1 more
- Workflow Introduction 

This workflow is specifically for Self-Hosted N8N Docker users.

The purpose of this workflow is to: 
Take an inventory of all workflows with credentials (Workflow -&gt; Creden...

### [Route IAM events with GPT-4o-mini, forgeLLM, Slack, email, and audit logs](https://n8n.io/workflows/14409-route-iam-events-with-gpt-4o-mini-forgellm-slack-email-and-a)
- **ID:** 14409 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 5
- **Nodes:** AI Agent, OpenAI Chat Model, Simple Memory +2 more
- How It Works
This workflow automates Identity and Access Management (IAM) event governance using an AI agent, targeting security operations teams, compliance officers, and IT governance teams managing...

### [Audit browser and proxy fingerprint/IP integrity with GPT-4o, Sheets and Slack](https://n8n.io/workflows/13375-audit-browser-and-proxy-fingerprint-ip-integrity-with-gpt-4o)
- **ID:** 13375 | **Creator:** @madame-ai ✓ | **Views:** 0 | **Nodes:** 5
- **Nodes:** Google Sheets, Slack, AI Agent +2 more
- Audit browser & Proxies fingerprint and IP integrity to Slack reports

Introduction

This workflow performs a comprehensive security audit on your web scraping infrastructure to detect potential IP le...

### [Audit Confluence space permissions and public links for compliance](https://n8n.io/workflows/12239-audit-confluence-space-permissions-and-public-links-for-comp)
- **ID:** 12239 | **Creator:** @alexschnabl ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, GraphQL
- Audit permissions in Confluence to ensure compliance

This workflow scans selected Confluence spaces for public exposure risks, helping teams identify unintended access and potential data leakage.

Wh...

### [AI-Powered Security Analysis for n8n with Google Gemini and n8n audit API](https://n8n.io/workflows/11975-ai-powered-security-analysis-for-n8n-with-google-gemini-and)
- **ID:** 11975 | **Creator:** @hatemgifaeeri | **Views:** 0 | **Nodes:** 5
- **Nodes:** HTTP Request, Code, Basic LLM Chain +2 more
- Generate a security audit report from an n8n instance to a web form
This workflow provides a deep-dive security assessment of an n8n instance using the native Audit API and AI analysis.

Who’s it for...

### [Triage fleet telemetry and route safety compliance with GPT-4o, Gmail and Sheets](https://n8n.io/workflows/14425-triage-fleet-telemetry-and-route-safety-compliance-with-gpt)
- **ID:** 14425 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 7
- **Nodes:** Google Sheets, HTTP Request, AI Agent +4 more
- How It Works
This workflow automates intelligent fleet operations management for transport operators, logistics companies, and smart mobility teams. It solves the problem of manually triaging high-vol...

### [Auto-Classify Security Incidents with GPT-4 and Google Sheets for SOC Teams](https://n8n.io/workflows/6412-auto-classify-security-incidents-with-gpt-4-and-google-sheet)
- **ID:** 6412 | **Creator:** @adnantariq ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** Google Sheets, HTTP Request
- 👤 Who it’s for
Blue Team leads, SOC analysts, and IT responders looking to automatically classify security alerts using AI-driven logic and asset-based risk signals.

Ideal for teams already scoring t...

### [IP Reputation Check & SOC Alerts with Splunk, VirusTotal and AlienVault](https://n8n.io/workflows/6037-ip-reputation-check-and-soc-alerts-with-splunk-virustotal-an)
- **ID:** 6037 | **Creator:** @rajneeshgupta | **Views:** 0 | **Nodes:** 6
- **Nodes:** HTTP Request, Slack, Gmail +3 more
- IP Reputation Check & Threat Summary using Splunk + VirusTotal + AlienVault + n8n

This workflow automates IP reputation analysis using Splunk alerts, enriches data via VirusTotal and AlienVault OTX,...

### [Automate CVE Detection with AI-Powered Nuclei Template Generation & Google Drive](https://n8n.io/workflows/10446-automate-cve-detection-with-ai-powered-nuclei-template-gener)
- **ID:** 10446 | **Creator:** @pyus3r ✓ | **Views:** 0 | **Nodes:** 5
- **Nodes:** HTTP Request, Google Drive, Code +2 more
- Short description
Automates collection, technical extraction, and automatic generation of Nuclei templates from public CVE PoCs.  
Converts verified PoCs into reproducible detection templates ready fo...

### [Automatic Workflow Backups to GitLab with GPT-4.1 Documentation Generation](https://n8n.io/workflows/6731-automatic-workflow-backups-to-gitlab-with-gpt-41-documentati)
- **ID:** 6731 | **Creator:** @shohani ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** GitLab, Code, OpenAI
- Auto backup n8n workflows to GitLab with AI-generated documentation

This n8n template automatically backs up your workflows to a GitLab repository whenever they're updated or activated, and generates...

### [Verify Property Ownership with Blockchain, GPT-4 Fraud Detection, and Compliance Tracking](https://n8n.io/workflows/12036-verify-property-ownership-with-blockchain-gpt-4-fraud-detect)
- **ID:** 12036 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** Google Sheets, HTTP Request, Code +3 more
- How It Works
This workflow automates property registration verification, fraud detection, and blockchain-based compliance tracking by systematically assessing fraud risk, validating transactions, ensu...

### [IoT Sensor Monitoring with GPT-4o Anomaly Detection, MQTT & Multi-Channel Alerts](https://n8n.io/workflows/11909-iot-sensor-monitoring-with-gpt-4o-anomaly-detection-mqtt-and)
- **ID:** 11909 | **Creator:** @tomo-0310 ✓ | **Views:** 0 | **Nodes:** 7
- **Nodes:** Google Sheets, Slack, Crypto +4 more
- {
  "name": "IoT Sensor Data Aggregation with AI-Powered Anomaly Detection",
  "nodes": [
    {
      "parameters": {
        "content": "## How it works\nThis workflow monitors IoT sensors in real-ti...

### [Intelligent Real-Time Financial Fraud Detection and Risk Scoring Engine](https://n8n.io/workflows/11862-intelligent-real-time-financial-fraud-detection-and-risk-sco)
- **ID:** 11862 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 7
- **Nodes:** Send Email, Google Sheets, HTTP Request +4 more
- How It Works
Automates fraud risk detection for financial transactions by analyzing real-time webhook events through AI-powered scoring. Target audience: fintech companies, payment processors, and ban...

### [Automated Failed Login Detection with Jira Tasks, Slack Alerts & Notion Logging](https://n8n.io/workflows/11220-automated-failed-login-detection-with-jira-tasks-slack-alert)
- **ID:** 11220 | **Creator:** @weblineindia ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Slack, Jira Software, Notion +1 more
- Automated Failed Login Detection with Jira Security Tasks, Slack Notifications

Webhook: Failed Login Attempts → Jira Security Case → Slack Warnings

This n8n workflow monitors failed login attempts f...

### [Create a Complete User Authentication System with PostgreSQL & Webhooks](https://n8n.io/workflows/10040-create-a-complete-user-authentication-system-with-postgresql)
- **ID:** 10040 | **Creator:** @convosoft | **Views:** 0 | **Nodes:** 1
- **Nodes:** Postgres
- Generate Secure User Authentication with One Webhook

Streamline user onboarding and security for your applications using this n8n workflow. This template handles signup, login, and password resets th...

### [Track and sync workflow status in Notion from the n8n API](https://n8n.io/workflows/12958-track-and-sync-workflow-status-in-notion-from-the-n8n-api)
- **ID:** 12958 | **Creator:** @abdallahh13 | **Views:** 0 | **Nodes:** 2
- **Nodes:** Notion, Code
- Who this template is for

This template is for n8n users who want clear visibility
into their workflows by maintaining a simple inventory in Notion.

It’s ideal for:
Automation engineers tracking mult...

### [Track Software Security Patents with ScrapeGraphAI, Notion, and Pushover Alerts](https://n8n.io/workflows/11635-track-software-security-patents-with-scrapegraphai-notion-an)
- **ID:** 11635 | **Creator:** @vinci-king-01 ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** HTTP Request, Pushover, Notion +1 more
- Software Vulnerability Tracker with Pushover and Notion



⚠️ COMMUNITY TEMPLATE DISCLAIMER: This is a community-contributed template that uses ScrapeGraphAI (a community node). Please ensure you have...

### [Automate Release Notes from ClickUp to Notion & Slack with GPT-4o](https://n8n.io/workflows/10332-automate-release-notes-from-clickup-to-notion-and-slack-with)
- **ID:** 10332 | **Creator:** @rahul08 ✓ | **Views:** 0 | **Nodes:** 8
- **Nodes:** Google Sheets, Slack, ClickUp +5 more
- 📘 Description:
This workflow automates the entire release note creation and announcement process whenever a task status changes in ClickUp.
Using Azure OpenAI GPT-4o, Notion, Slack, Gmail, and Google...

### [Track SDK Documentation Drift with GitHub, Notion, Google Sheets, and Slack](https://n8n.io/workflows/10337-track-sdk-documentation-drift-with-github-notion-google-shee)
- **ID:** 10337 | **Creator:** @rahul08 ✓ | **Views:** 0 | **Nodes:** 5
- **Nodes:** GitHub, Google Sheets, Slack +2 more
- 📊 Description
Automatically track SDK releases from GitHub, compare documentation freshness in Notion, and send Slack alerts when docs lag behind. This workflow ensures documentation stays in sync wit...

### [Auto-Answer GitHub PR Questions with GPT-4o, Notion & Slack for Dev Teams](https://n8n.io/workflows/10331-auto-answer-github-pr-questions-with-gpt-4o-notion-and-slack)
- **ID:** 10331 | **Creator:** @rahul08 ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** Google Sheets, Slack, Notion +3 more
- 📘 Description:
This workflow automates developer Q&A handling by connecting GitHub, GPT-4o (Azure OpenAI), Notion, Google Sheets, and Slack.
 Whenever a developer comments on a pull request with a “ho...

### [Multi-channel Website Downtime Alerts with UptimeRobot, Slack, WhatsApp & Notion](https://n8n.io/workflows/6645-multi-channel-website-downtime-alerts-with-uptimerobot-slack)
- **ID:** 6645 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Send Email, Slack, Notion +1 more
- Description
Automates website downtime detection and notifications using UptimeRobot.
Triggers alerts via Slack, WhatsApp, or Email when a website goes down.
Creates a task in Notion and tags the resp...

### [Automate Website Performance Analysis and Comparison using Gemini and PageSpeed Insights](https://n8n.io/workflows/6166-automate-website-performance-analysis-and-comparison-using-g)
- **ID:** 6166 | **Creator:** @khmuhtadin ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Discord, Code, Basic LLM Chain +1 more
- The Page Speed Insight workflow automates website performance analysis by integrating Google PageSpeed Insights API with Discord messaging and Gemini. This n8n workflow provides expert-level performan...

### [Automate Daily Signup Stats from PostgreSQL to Slack, Teams & Telegram](https://n8n.io/workflows/8362-automate-daily-signup-stats-from-postgresql-to-slack-teams-a)
- **ID:** 8362 | **Creator:** @itechnotion ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Postgres, Slack, Telegram +1 more
- How it works
This workflow automatically pulls daily signup stats from your PostgreSQL database and shares them with your team across multiple channels. Every morning, it counts the number of new sign...

### [Turn new Jira tickets into CloudCLI AI coding sessions with Claude Code](https://n8n.io/workflows/14070-turn-new-jira-tickets-into-cloudcli-ai-coding-sessions-with)
- **ID:** 14070 | **Creator:** @simos | **Views:** 0 | **Nodes:** 1
- **Nodes:** Jira Software
- Turn new Jira tickets into automated AI coding sessions. When a ticket is created, this workflow runs an AI coding agent (Claude Code, Cursor CLI, or Codex) on the task inside a CloudCLI cloud dev env...

### [Monitor partner API usage with Slack, Jira and Gmail alerts](https://n8n.io/workflows/14709-monitor-partner-api-usage-with-slack-jira-and-gmail-alerts)
- **ID:** 14709 | **Creator:** @weblineindia ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Slack, Jira Software, Gmail +1 more
- Smart Partner API Usage Monitoring with Slack, Jira & Gmail Alerts

This workflow monitors partner API usage in real time and triggers alerts based on usage thresholds. It validates incoming data, cal...

### [Turn support tickets into developer insights with OpenAI, Postgres, Slack and Jira](https://n8n.io/workflows/14684-turn-support-tickets-into-developer-insights-with-openai-pos)
- **ID:** 14684 | **Creator:** @rnair1996 ✓ | **Views:** 0 | **Nodes:** 8
- **Nodes:** Send Email, Postgres, Slack +5 more
- Overview
This workflow transforms raw support tickets into actionable developer insights using AI and data processing. It automatically detects recurring issues, identifies root causes, ranks severit...

### [Aggregate error alerts and send consolidated reports via Email and Jira](https://n8n.io/workflows/12989-aggregate-error-alerts-and-send-consolidated-reports-via-ema)
- **ID:** 12989 | **Creator:** @vinci-king-01 ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Send Email, HTTP Request, Jira Software +1 more
- Error Alert Aggregator – Email and Jira

This workflow aggregates error logs arriving from multiple sources, deduplicates identical events within a configurable time-window, and sends a single consoli...

### [Real-Time Uptime Alerts to Jira with Smart Slack On-Call Routing](https://n8n.io/workflows/12060-real-time-uptime-alerts-to-jira-with-smart-slack-on-call-rou)
- **ID:** 12060 | **Creator:** @weblineindia ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Slack, Jira Software, Code
- Real-Time Uptime Alerts to Jira with Smart Slack On-Call Routing

This workflow automatically converts uptime monitoring alerts received via webhook into Jira incident tasks and intelligently notifies...

### [Detect Unused Android Feature Flags with GitLab, LaunchDarkly, Jira & Slack](https://n8n.io/workflows/7985-detect-unused-android-feature-flags-with-gitlab-launchdarkly)
- **ID:** 7985 | **Creator:** @weblineindia ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** Google Sheets, HTTP Request, Slack +3 more
- Android Feature Flag Cleanup Bot (GitLab + LaunchDarkly)

This n8n automation detects unused (“dead”) feature flags in an Android Kotlin/Java codebase by comparing your GitLab repository code against...

### [Keep Supabase free plan projects alive with scheduled database pings](https://n8n.io/workflows/14745-keep-supabase-free-plan-projects-alive-with-scheduled-databa)
- **ID:** 14745 | **Creator:** @lukaszb ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** Supabase, Code
- Supabase Free Plan Keep-Alive

Prevents Supabase from pausing an inactive project by writing randomised pings to a database table on a recurring schedule.

Overview

The workflow runs every 4 days and...

### [AI-Powered Code Review with Linting, Red-Marked Corrections in Google Sheets & Slack](https://n8n.io/workflows/10034-ai-powered-code-review-with-linting-red-marked-corrections-i)
- **ID:** 10034 | **Creator:** @kazushi ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Google Sheets, Slack, AI Agent +1 more
- Advanced Code Review Automation (AI + Lint + Slack)

Who’s it for
For software engineers, QA teams, and tech leads who want to automate intelligent code reviews with both AI-driven suggestions and rul...

### [Generate, review, and optimize code with Cursor AI, GitHub, Google, and Slack](https://n8n.io/workflows/13827-generate-review-and-optimize-code-with-cursor-ai-github-goog)
- **ID:** 13827 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** Google Sheets, HTTP Request, Slack +3 more
- A smart, fully automated coding pipeline built inside n8n that leverages Cursor AI to write, refactor, review, and optimize code projects — triggered by a webhook, schedule, or manual prompt. Every ou...

### [Review GitLab merge requests with parallel Azure OpenAI reviewers](https://n8n.io/workflows/14338-review-gitlab-merge-requests-with-parallel-azure-openai-revi)
- **ID:** 14338 | **Creator:** @kazunori-kasajima | **Views:** 0 | **Nodes:** 5
- **Nodes:** HTTP Request, Code, AI Agent +2 more
- Who this template is for

This template is for teams that use GitLab merge requests and want a practical AI-assisted review workflow in n8n. It is useful for engineering teams that want faster first-p...

### [Review GitHub pull requests with Gemini and post feedback automatically](https://n8n.io/workflows/13563-review-github-pull-requests-with-gemini-and-post-feedback-au)
- **ID:** 13563 | **Creator:** @okp29 ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** Google Sheets, HTTP Request, Slack +3 more
- Review GitHub pull requests with Gemini AI and post feedback automatically

Who is this for

Development teams and tech leads who want to maintain consistent code quality without manual review bottlen...

### [Automated Kubernetes Testing with Robot Framework, ArgoCD & With KinD Lifecycle](https://n8n.io/workflows/10302-automated-kubernetes-testing-with-robot-framework-argocd-and)
- **ID:** 10302 | **Creator:** @vighsandor ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** Telegram, GitLab
- Overview

This n8n workflow provides automated CI/CD testing for Kubernetes applications using KinD (Kubernetes in Docker). It creates temporary infrastructure, runs tests, and cleans up everything au...

### [Validate Mobile App Deep Links in GitHub PRs with Automated Testing](https://n8n.io/workflows/7124-validate-mobile-app-deep-links-in-github-prs-with-automated)
- **ID:** 7124 | **Creator:** @weblineindia ✓ | **Views:** 0 | **Nodes:** 1
- **Nodes:** GitHub
- GitHub PR Deep-Link & Routing Validator (ExecuteCommand + GitHub Comment)

🚀 Quick-Start TL;DR

Import the workflow JSON into n8n (Cloud or self-hosted). 
Create a GitHub Personal Access Token with re...

### [Automate LLM Testing with GPT-4 Judge & Google Sheets Tracking](https://n8n.io/workflows/6041-automate-llm-testing-with-gpt-4-judge-and-google-sheets-trac)
- **ID:** 6041 | **Creator:** @adamjanes ✓ | **Views:** 0 | **Nodes:** 5
- **Nodes:** Google Sheets, HTTP Request, Basic LLM Chain +2 more
- How it works
The workflow loads a list of test cases from a Google Sheet (previous results stored from an LLM)
For each test case, we execute a call to an LLM judge in parallel (using HTTP Request + W...

### [Build, test and deploy AI projects with Windsurf CI/CD and Vercel](https://n8n.io/workflows/13823-build-test-and-deploy-ai-projects-with-windsurf-ci-cd-and-ve)
- **ID:** 13823 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, Slack
- This is a conceptual / starter workflow that triggers on git events (or schedule), runs Windsurf-powered build & test steps (via API or CLI wrapper), builds Docker if needed, pushes to registry, deplo...

### [Automated Wazuh Rule Deployment Pipeline with GitHub, XML Validation & Telegram Alerts](https://n8n.io/workflows/7226-automated-wazuh-rule-deployment-pipeline-with-github-xml-val)
- **ID:** 7226 | **Creator:** @mariskarthick ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** HTTP Request, Telegram, Code
- 🚀 Say Goodbye to Manual Rule Deployments in Wazuh!

Just Commit— Let Your Pipeline Auto‑Deploy via GitHub + n8n 🎯

👨‍💻 Tired of This Endless Cycle?

Create rule → Validate → Copy to server → Restart W...

### [Generate Data Pipeline Blueprints with Claude 3.5, Slack, and Tavily Search](https://n8n.io/workflows/5740-generate-data-pipeline-blueprints-with-claude-35-slack-and-t)
- **ID:** 5740 | **Creator:** @humbleturtle ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Slack, AI Agent, Anthropic Chat Model +1 more
- Architecture Agent

Overview
The Architect Agent listens to Slack messages and generates full data architecture blueprints in response. Powered by Claude 3.5 (Anthropic) for reasoning and design, and...

### [Weekly ETL Pipeline: QuickBooks Financial Data to Google BigQuery](https://n8n.io/workflows/6493-weekly-etl-pipeline-quickbooks-financial-data-to-google-bigq)
- **ID:** 6493 | **Creator:** @fahmiiireza ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** QuickBooks Online, Google BigQuery, Code
- This template sets up a weekly ETL (Extract, Transform, Load) pipeline that pulls financial data from QuickBooks Online into Google BigQuery. It not only transfers data, but also cleans, classifies, a...

### [Train and deploy ML models with Claude and Slack approval](https://n8n.io/workflows/13781-train-and-deploy-ml-models-with-claude-and-slack-approval)
- **ID:** 13781 | **Creator:** @suryayalavarthi ✓ | **Views:** 0 | **Nodes:** 5
- **Nodes:** HTTP Request, Slack, Code +2 more
- What this workflow does

This workflow automates the full machine learning lifecycle end-to-end using Claude AI as the intelligent decision-maker at every stage. Send one HTTP request with a dataset U...

### [Deploy Code to GitHub with Natural Language via Slack & Claude 3.5](https://n8n.io/workflows/5753-deploy-code-to-github-with-natural-language-via-slack-and-cl)
- **ID:** 5753 | **Creator:** @humbleturtle ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Slack, AI Agent, Anthropic Chat Model +1 more
- Github Deployer Agent
Overview
The Github Deployer Agent is an intelligent automation tool that integrates with Slack to streamline code deployment workflows. Powered by Anthropic's Claude 3.5 and Tav...

### [Gate deployments on WAF scan results with WAFtester](https://n8n.io/workflows/13445-gate-deployments-on-waf-scan-results-with-waftester)
- **ID:** 13445 | **Creator:** @qandil ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- What it does

A CI/CD quality gate that blocks deployments when WAF protection is insufficient. Your pipeline sends a webhook with the target URL, the workflow runs WAFtester scans, and returns a pass...

### [Automatic Self-Hosted Application Updates with Coolify Deployments](https://n8n.io/workflows/8118-automatic-self-hosted-application-updates-with-coolify-deplo)
- **ID:** 8118 | **Creator:** @mredodos ✓ | **Views:** 0 | **Nodes:** 1
- **Nodes:** HTTP Request
- Auto-update n8n instance with Coolify  

Who’s it for  
This workflow is designed for self-hosted n8n administrators who want to keep their instance automatically updated to the latest stable release....

### [Start an AI coding agent from Linear issues with CloudCLI](https://n8n.io/workflows/14071-start-an-ai-coding-agent-from-linear-issues-with-cloudcli)
- **ID:** 14071 | **Creator:** @simos | **Views:** 0 | **Nodes:** 1
- **Nodes:** Linear
- Turn new Linear issues into automated AI coding sessions. When an issue is created, this workflow runs an AI coding agent (Claude Code, Cursor CLI, Gemini or Codex) on the task inside a CloudCLI cloud...

### [Scan code repositories for governance issues with GPT-4o and severity-based reports](https://n8n.io/workflows/13900-scan-code-repositories-for-governance-issues-with-gpt-4o-and)
- **ID:** 13900 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** AI Agent, OpenAI Chat Model, Structured Output Parser +1 more
- How It Works
This workflow automates end-to-end code repository governance scanning using a multi-agent AI orchestration system. Designed for engineering leads, DevSecOps teams, and CTOs, it replaces...

### [Automated CVE Scanning of Bug Bounty Programs with Nuclei and Project Discovery](https://n8n.io/workflows/10054-automated-cve-scanning-of-bug-bounty-programs-with-nuclei-an)
- **ID:** 10054 | **Creator:** @pyus3r ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, Gmail
- Description
Automates daily CVE-driven scanning against bug bounty scopes. It fetches bug-bounty domains, pulls newly published Project Discovery templates, converts them to Nuclei rules, runs targete...

### [Generate GitHub Release Notes with AI Comparison](https://n8n.io/workflows/11569-generate-github-release-notes-with-ai-comparison)
- **ID:** 11569 | **Creator:** @rtblack | **Views:** 0 | **Nodes:** 5
- **Nodes:** GitHub, HTTP Request, Code +2 more
- Generate GitHub Release Notes with AI

Automatically generate GitHub release notes using AI. 

This workflow compares your latest two GitHub releases, summarises the changes, and produces a clean, rea...

### [Compare Your n8n Version with Latest Release using n8n API](https://n8n.io/workflows/7797-compare-your-n8n-version-with-latest-release-using-n8n-api)
- **ID:** 7797 | **Creator:** @rbreen ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** HTTP Request, Code, HTML
- 🧑‍💻 Description
This workflow automatically compares the version of your n8n instance with the latest release available.  

Keeping your n8n instance up-to-date is essential for security patches, bug...

### [Auto-Generate GitHub Release Notes and Notify via Slack](https://n8n.io/workflows/6763-auto-generate-github-release-notes-and-notify-via-slack)
- **ID:** 6763 | **Creator:** @weblineindia ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- Auto-Generate GitHub Release Notes and Notify via Slack (n8n Workflow)

This n8n workflow automates the process of:
Generating structured GitHub release notes from merged pull requests since the last...

### [Sync self-hosted workflow backups to GitHub for version control](https://n8n.io/workflows/14925-sync-self-hosted-workflow-backups-to-github-for-version-cont)
- **ID:** 14925 | **Creator:** @ucartz | **Views:** 0 | **Nodes:** 2
- **Nodes:** GitHub, Code
- Automatically back up and sync your n8n workflows to GitHub with unlimited version control. This workflow ensures your repository always reflects the latest state of your n8n instance by creating, upd...

### [GitHub Workflow Version Control Dashboard with Commit History and Rollbacks](https://n8n.io/workflows/8105-github-workflow-version-control-dashboard-with-commit-histor)
- **ID:** 8105 | **Creator:** @eduard ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** GitHub, HTTP Request, Code +1 more
- This n8n template provides enterprise-level version control for your workflows using GitHub integration. Stop losing hours to broken workflows and manual exports – get proper commit history, visual di...

### [Monitor PostgreSQL data quality and generate remediation alerts with Slack](https://n8n.io/workflows/14035-monitor-postgresql-data-quality-and-generate-remediation-ale)
- **ID:** 14035 | **Creator:** @rnair1996 ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Postgres, Slack, Code
- Autonomous PostgreSQL Data Quality Monitoring & Remediation

Overview

This workflow automatically monitors PostgreSQL database data quality and detects structural or statistical anomalies before they...

### [Orchestrate quality event risk assessment with Claude, Gmail and Slack for human approval](https://n8n.io/workflows/13426-orchestrate-quality-event-risk-assessment-with-claude-gmail)
- **ID:** 13426 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 7
- **Nodes:** Send Email, Slack, Code +4 more
- How It Works
This workflow automates quality event risk assessment through AI-powered multi-agent analysis with mandatory human oversight for critical decisions. Designed for quality managers, complia...

### [Monitor Kubernetes Services & Pods with Prometheus and Send Alerts to Slack](https://n8n.io/workflows/7665-monitor-kubernetes-services-and-pods-with-prometheus-and-sen)
- **ID:** 7665 | **Creator:** @johnpranay ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- 🧩 Short Summary

Proactively alert to service endpoint changes and pod/container issues (Pending, Not Ready, Restart spikes) using Prometheus metrics, formatted and sent to Slack.

🗂️ Category

DevOps...

### [Kubernetes Management with Natural Language using GPT-4o and MCP Tools](https://n8n.io/workflows/7236-kubernetes-management-with-natural-language-using-gpt-4o-and)
- **ID:** 7236 | **Creator:** @aadarsh-jain | **Views:** 0 | **Nodes:** 2
- **Nodes:** AI Agent, OpenAI Chat Model
- Who is this for?

This workflow is designed for DevOps engineers, platform engineers, and Kubernetes administrators who want to interact with their Kubernetes clusters through natural language queries...

### [Automate AWS IAM User Management Through Email](https://n8n.io/workflows/7241-automate-aws-iam-user-management-through-email)
- **ID:** 7241 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Send Email, Code, AWS IAM
- This automated n8n workflow manages AWS IAM users (create, delete, update, assign to groups) directly from email commands with automatic confirmation responses.

Good to Know
The workflow processes em...

### [Convert Make.com blueprints to workflows with Azure OpenAI and Google Sheets](https://n8n.io/workflows/13794-convert-makecom-blueprints-to-workflows-with-azure-openai-an)
- **ID:** 13794 | **Creator:** @rahul08 ✓ | **Views:** 0 | **Nodes:** 5
- **Nodes:** Google Sheets, Google Drive, Code +2 more
- 📘 Description
 This workflow converts a Make.com blueprint JSON into a directly importable n8n workflow JSON. It searches a Google Drive folder for the target blueprint file, downloads it, extracts th...

### [Optimize n8n workflow JSON using Azure OpenAI GPT-4o-mini](https://n8n.io/workflows/13788-optimize-n8n-workflow-json-using-azure-openai-gpt-4o-mini)
- **ID:** 13788 | **Creator:** @rahul08 ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Code, AI Agent, Azure OpenAI Chat Model
- 📊 Description
Automate the optimization of your n8n workflows using AI-powered analysis and restructuring 🤖. This workflow receives any existing n8n JSON via webhook, analyzes it using Azure OpenAI, a...

### [Monitor Website Uptime with Google Sheets, Slack, Email & Phone Call Alerts](https://n8n.io/workflows/11655-monitor-website-uptime-with-google-sheets-slack-email-and-ph)
- **ID:** 11655 | **Creator:** @pixcelsthemes ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Google Sheets, HTTP Request, Slack +1 more
- Who’s it for
This template is ideal for developers, agencies, hosting providers, and website owners who need real-time alerts when a website goes down. It helps teams react quickly to downtime by send...

### [API Uptime Monitoring with WhatsApp Alerts & Google Sheets Management](https://n8n.io/workflows/6747-api-uptime-monitoring-with-whatsapp-alerts-and-google-sheets)
- **ID:** 6747 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Google Sheets, HTTP Request, WhatsApp Business Cloud +1 more
- This automated n8n workflow monitors API uptime by periodically checking API availability and sending instant WhatsApp alerts if any service goes down. It retrieves API details from a Google Sheet and...

### [Scheduled Website Uptime Monitor with Slack Alert](https://n8n.io/workflows/6467-scheduled-website-uptime-monitor-with-slack-alert)
- **ID:** 6467 | **Creator:** @dae221 ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, Slack
- Overview
This workflow periodically checks the status of a website. If the website is not reachable (returns an error or non-2xx status code), it sends an alert to a specified Slack channel.

Use Case...

### [Automate GitHub Trending Data Collection with FireCrawl, GPT and Supabase](https://n8n.io/workflows/7394-automate-github-trending-data-collection-with-firecrawl-gpt)
- **ID:** 7394 | **Creator:** @caiyongji | **Views:** 0 | **Nodes:** 2
- **Nodes:** AI Agent, OpenAI Chat Model
- GitHub Trending to Supabase (Daily, Weekly, Monthly)

Who is this for?

This workflow is for developers, researchers, founders, and data analysts who want a historical dataset of GitHub Trending repos...

### [Query MySQL Database with Natural Language using GPT AI](https://n8n.io/workflows/6291-query-mysql-database-with-natural-language-using-gpt-ai)
- **ID:** 6291 | **Creator:** @moe-ahad ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** AI Agent, OpenAI Chat Model, Simple Memory
- This workflow contains community nodes that are only compatible with the self-hosted version of n8n.

How it works
Using chat node, ask a question pertaining to information stored in your MySQL databa...

### [Gate AI Slack DevOps bot actions with OpenAI and Permit.io RBAC](https://n8n.io/workflows/14087-gate-ai-slack-devops-bot-actions-with-openai-and-permitio-rb)
- **ID:** 14087 | **Creator:** @taofiq | **Views:** 0 | **Nodes:** 3
- **Nodes:** HTTP Request, Slack, OpenAI
- &gt; This n8n workflow template uses a community node and is only compatible with the self-hosted version of n8n.

Who's it for

DevOps teams, platform engineers, and ops leads who use Slack bots for...

### [Automate Wazuh Alert Triage and Reporting with GPT-4o-mini and Telegram](https://n8n.io/workflows/6978-automate-wazuh-alert-triage-and-reporting-with-gpt-4o-mini-a)
- **ID:** 6978 | **Creator:** @mariskarthick ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Telegram, Summarization Chain, OpenAI Chat Model
- 🚨Are alert storms overwhelming your Security Operations workflows?

This n8n workflow supercharges your SOC by fully automating triage, analysis, and notification for Wazuh alerts—blending event-drive...

### [Monitor Core Web Vitals with Lighthouse, Gemini AI, Telegram Alerts & Google Sheets](https://n8n.io/workflows/6490-monitor-core-web-vitals-with-lighthouse-gemini-ai-telegram-a)
- **ID:** 6490 | **Creator:** @rullysaputra15 ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** Google Sheets, HTTP Request, Telegram +3 more
- Automate Lighthouse report alerts to messenger and Google Sheets

Who’s it for
This workflow is ideal for developers, SEO specialists, performance engineers, and digital agencies who want to continuou...

### [Maintain RAG embeddings with OpenAI, Postgres and auto drift rollback](https://n8n.io/workflows/14036-maintain-rag-embeddings-with-openai-postgres-and-auto-drift)
- **ID:** 14036 | **Creator:** @rnair1996 ✓ | **Views:** 0 | **Nodes:** 9
- **Nodes:** HTTP Request, Postgres, Code +6 more
- Overview

This workflow implements a self-healing Retrieval-Augmented Generation (RAG) maintenance system that automatically updates document embeddings, evaluates retrieval quality, detects embedding...

### [AI-powered RAG Configuration Assistant: From Form to Email Recommendations](https://n8n.io/workflows/11990-ai-powered-rag-configuration-assistant-from-form-to-email-re)
- **ID:** 11990 | **Creator:** @edupuganti ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Gmail, Code, AI Agent +1 more
- Description
An intelligent RAG Configuration Assistant that analyzes your retrieval-augmented generation requirements and delivers AI-powered recommendations via email. Get expert guidance on embeddin...

### [Extract Context from Voice Notes with OpenRouter AI & Milvus for RAG Systems](https://n8n.io/workflows/7430-extract-context-from-voice-notes-with-openrouter-ai-and-milv)
- **ID:** 7430 | **Creator:** @danielrosehill ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** AI Agent, Embeddings OpenAI, Structured Output Parser +3 more
- Voice Note Context Extraction Pipeline with AI Agent & Vector Storage

This n8n template demonstrates how to automatically extract and store contextual information from voice notes using AI agents and...

### [Monetize Your Private LLM Models with x402 & Ollama](https://n8n.io/workflows/6597-monetize-your-private-llm-models-with-x402-and-ollama)
- **ID:** 6597 | **Creator:** @oneshotapi ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Code, Basic LLM Chain, Ollama Model
- This workflow contains community nodes that are only compatible with the self-hosted version of n8n.

Monetize Your Private LLM Models with x402 and Ollama

Self-hosting custom LLMs is becoming more p...

### [Track Jura Coffee Machine Data with Webhook API and Google Sheets](https://n8n.io/workflows/5771-track-jura-coffee-machine-data-with-webhook-api-and-google-s)
- **ID:** 5771 | **Creator:** @halfbit ✓ | **Views:** 0 | **Nodes:** 1
- **Nodes:** Google Sheets
- Jura Coffee Counter: Webhook API & Google Sheets Logger ☕️

Track how many coffees your Jura E8 espresso machine makes — fully automated via webhook and Google Sheets.

This workflow exposes a custom...

### [Real-time IoT Anomaly Detection with MQTT, GPT-4o-mini AI, and Multi-channel Alerts](https://n8n.io/workflows/10759-real-time-iot-anomaly-detection-with-mqtt-gpt-4o-mini-ai-and)
- **ID:** 10759 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 7
- **Nodes:** Send Email, HTTP Request, Postgres +4 more
- How It Works

MQTT ingests real-time sensor data from connected devices. The workflow normalizes the values and trains or retrains machine learning models on a defined schedule. An AI agent detects an...

### [Singapore Lottery Predictive Analytics and Pattern Mining System](https://n8n.io/workflows/10890-singapore-lottery-predictive-analytics-and-pattern-mining-sy)
- **ID:** 10890 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** HTTP Request, Code, AI Agent +3 more
- How It Works
A scheduled trigger initiates automated retrieval of TOTO/4D data, including both current and historical records. The datasets are merged and validated to ensure structural consistency be...

### [Monitor Solar Energy Production & Send Alerts with Gmail, Google Sheets, and Slack](https://n8n.io/workflows/7125-monitor-solar-energy-production-and-send-alerts-with-gmail-g)
- **ID:** 7125 | **Creator:** @weblineindia ✓ | **Views:** 0 | **Nodes:** 5
- **Nodes:** Google Sheets, HTTP Request, Slack +2 more
- Solar Energy Production Monitoring Alert Workflow

This workflow automatically monitors solar energy production every 2 hours by fetching data from the Energidataservice API. If the energy output fall...

### [Real-time Error Detection with Slack Alerts and Jira Ticket Creation for Production](https://n8n.io/workflows/6644-real-time-error-detection-with-slack-alerts-and-jira-ticket)
- **ID:** 6644 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** Slack, Jira Software
- Description
Automates error detection and notification to prevent production downtime.
Monitors incoming webhooks, filters critical errors, and triggers alerts or bug reports.
Ensures rapid response t...

### [AI-Powered Domain & IP Security Check Automation](https://n8n.io/workflows/7189-ai-powered-domain-and-ip-security-check-automation)
- **ID:** 7189 | **Creator:** @garri ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** Google Sheets, HTTP Request, Code +3 more
- Description

This workflow is designed to automate the security reputation check of domains and IP addresses using multiple APIs such as VirusTotal, AbuseIPDB, and Google DNS. It assesses potential...

### [Backup and Delete Workflows to Google Drive with n8n API and Form Trigger](https://n8n.io/workflows/6751-backup-and-delete-workflows-to-google-drive-with-n8n-api-and)
- **ID:** 6751 | **Creator:** @arlindeveloper ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Telegram, Google Drive, Code
- 🔍 Description:
Effortlessly delete unused or inactive workflows from your n8n instance while automatically backing them up as .json files into your Google Drive. Keep your instance clean, fast, and or...

### [Automated Zalo OA Token Management with OAuth and Webhook Integration](https://n8n.io/workflows/8675-automated-zalo-oa-token-management-with-oauth-and-webhook-in)
- **ID:** 8675 | **Creator:** @leeseifer ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- Description (How it works)
This workflow keeps your Zalo Official Account access token valid and easy to reuse across other flows—no external server required.

High-level steps
Scheduled refresh runs...

### [Scheduled n8n Workflow Backups to Google Drive using n8n API](https://n8n.io/workflows/7707-scheduled-n8n-workflow-backups-to-google-drive-using-n8n-api)
- **ID:** 7707 | **Creator:** @tonyciencia | **Views:** 0 | **Nodes:** 1
- **Nodes:** Google Drive
- Overview
This template provides an automatic backup solution for all your n8n workflows, saving them directly to Google Drive.
It’s designed for freelancers, agencies, and businesses that want to keep...

### [Automated Weekly Security Audit Reports with Gmail Delivery](https://n8n.io/workflows/10112-automated-weekly-security-audit-reports-with-gmail-delivery)
- **ID:** 10112 | **Creator:** @neon8n | **Views:** 0 | **Nodes:** 2
- **Nodes:** Gmail, Code
- 🔒 N8N Security Audit Report - Automated Weekly Email

🎯 What does this workflow do?

This workflow automatically generates and emails a comprehensive security audit report for your N8N instance every...

### [Monitor Remote Server File Integrity with SSH and Slack Alerts](https://n8n.io/workflows/6814-monitor-remote-server-file-integrity-with-ssh-and-slack-aler)
- **ID:** 6814 | **Creator:** @marth ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** Slack, Code
- How It Works: The 5-Node Security Flow

This workflow efficiently performs a scheduled file integrity audit.

1. Scheduled Check (Cron Node)
This is the workflow's trigger. It schedules the workflow t...

### [Live Airport Delay Dashboard with FlightStats, Google Sheets & Slack Alerts](https://n8n.io/workflows/6648-live-airport-delay-dashboard-with-flightstats-google-sheets)
- **ID:** 6648 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Google Sheets, HTTP Request, Slack
- Live Airport Delay Dashboard with FlightStats & Team Alerts

Description
Automates live monitoring of airport delays using FlightStats API.
Stores and displays delay data, with Slack alerts for severe...

### [Weekly Website Link Checker with Slack Alerts for Broken URLs](https://n8n.io/workflows/6647-weekly-website-link-checker-with-slack-alerts-for-broken-url)
- **ID:** 6647 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, Slack
- Description
Automates weekly checks for broken links on a website.
Scans the site using HTTP requests and filters broken links.
Sends Slack alerts for detected broken URLs and creates a list for track...

### [Distribute Workflow Execution with Round-Robin Logic using Data Tables](https://n8n.io/workflows/10048-distribute-workflow-execution-with-round-robin-logic-using-d)
- **ID:** 10048 | **Creator:** @akendall1966 | **Views:** 0 | **Nodes:** 1
- **Nodes:** Code
- Key Features

Implements a simple round-robin distribution mechanism using a Data Table to track the last route used.

Supports multiple downstream workflows or resources, balancing workload across th...

### [Create Personal Data Vector Store from Google Sheets with OpenAI & Gemini AI](https://n8n.io/workflows/7299-create-personal-data-vector-store-from-google-sheets-with-op)
- **ID:** 7299 | **Creator:** @mpolat | **Views:** 0 | **Nodes:** 7
- **Nodes:** Google Sheets, AI Agent, Embeddings OpenAI +4 more
- This workflow integrates Google Sheets with Supabase Vector Store for storing personal data as vectors. It utilizes OpenAI and Google Gemini AI models for enhanced data processing and querying.

The w...

### [Sync workflow schedules between Google Sheets and Google Calendar](https://n8n.io/workflows/14397-sync-workflow-schedules-between-google-sheets-and-google-cal)
- **ID:** 14397 | **Creator:** @paoloronco ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Google Sheets, Google Calendar, Code
- Sync n8n Workflow Schedules to Google Calendar

Reads every workflow on your n8n instance every 30 minutes, extracts their schedule triggers, and keeps a matching recurring event on Google Calendar —...

### [Generate your GitLab year-in-review wrapped report automatically](https://n8n.io/workflows/12394-generate-your-gitlab-year-in-review-wrapped-report-automatic)
- **ID:** 12394 | **Creator:** @jnnklhmnn | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- GitLab Wrapped Generator

  ✨ Automatically generate your personalized GitLab Wrapped, a stunning year-in-review of your contributions, activity, and stats.

  Powered by gitlab-wrapped by @michaelang...

### [Route AI queries cost‑efficiently with GPT‑4o‑mini, GPT‑4o and confidence scoring](https://n8n.io/workflows/13966-route-ai-queries-costefficiently-with-gpt4omini-gpt4o-and-co)
- **ID:** 13966 | **Creator:** @rnair1996 ✓ | **Views:** 0 | **Nodes:** 5
- **Nodes:** Code, AI Agent, OpenAI Chat Model +2 more
- This workflow implements a cost-optimized AI routing system using n8n. It intelligently decides whether a request should be handled by a low-cost model or escalated to a higher-quality model based o...

### [Automated APK Security Scanning & PDF Reporting with MobSF, AI & Google Drive](https://n8n.io/workflows/12024-automated-apk-security-scanning-and-pdf-reporting-with-mobsf)
- **ID:** 12024 | **Creator:** @weblineindia ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** HTTP Request, Google Drive, Code +1 more
- APK Security Scanner & PDF Report Generator

This workflow automatically analyzes any newly uploaded APK file and produces a clean, professional PDF security report. When an APK appears in Google Driv...

### [IP Geolocation & HTTP Port Scanning with Google Sheets](https://n8n.io/workflows/8674-ip-geolocation-and-http-port-scanning-with-google-sheets)
- **ID:** 8674 | **Creator:** @iranserver ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Google Sheets, HTTP Request, Code
- Automate IP geolocation and HTTP port scanning with Google Sheets trigger

This n8n template automatically enriches IP addresses with geolocation data and performs HTTP port scanning when new IPs are...

### [Summarize daily Jenkins test runs with Google Sheets, HTTP and Gemini AI](https://n8n.io/workflows/13808-summarize-daily-jenkins-test-runs-with-google-sheets-http-an)
- **ID:** 13808 | **Creator:** @rnijsten ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** Google Sheets, HTTP Request, Gmail +3 more
- Automate daily Jenkins test reports with AI and HTTP Requests
As a test automation engineer, staying on top of daily test runs in Jenkins is essential. This workflow automates that process: it pulls s...

### [Automate CVE Monitoring with OpenAI Processing for ServiceNow Security Incidents](https://n8n.io/workflows/7224-automate-cve-monitoring-with-openai-processing-for-serviceno)
- **ID:** 7224 | **Creator:** @yajna ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** HTTP Request, ServiceNow, OpenAI Chat Model +1 more
- This n8n workflow automatically fetches the latest CVE data at scheduled intervals, extracts relevant security details, and creates a corresponding Security Incident in ServiceNow for each new vulnera...

### [Malicious File Detection & Response: Wazuh to VirusTotal with Slack Alerts](https://n8n.io/workflows/5997-malicious-file-detection-and-response-wazuh-to-virustotal-wi)
- **ID:** 5997 | **Creator:** @rajneeshgupta | **Views:** 0 | **Nodes:** 6
- **Nodes:** HTTP Request, Slack, Gmail +3 more
- Malicious File Detection & Threat Summary Automation using Wazuh + VirusTotal + n8n

This workflow helps SOC teams automate the detection and reporting of potentially malicious files using Wazuh alert...

### [Clean and Log IoT Sensor Data to InfluxDB (Webhook | Function | HTTP)](https://n8n.io/workflows/7248-clean-and-log-iot-sensor-data-to-influxdb-webhook-function)
- **ID:** 7248 | **Creator:** @weblineindia ✓ | **Views:** 0 | **Nodes:** 1
- **Nodes:** HTTP Request
- 🌡 IoT Sensor Data Cleaner + InfluxDB Logger (n8n | Webhook | Function | InfluxDB)

This workflow accepts raw sensor data from IoT devices via webhook, applies basic cleaning and transformation logic,...

### [CI Artifact Completeness Gate (Git Push, Sentry Artifact Verification, Commit)](https://n8n.io/workflows/11828-ci-artifact-completeness-gate-git-push-sentry-artifact-verif)
- **ID:** 11828 | **Creator:** @weblineindia ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- CI Artifact Completeness Gate (GitHub Push → Sentry Release Files → Artifact Validation → GitHub Commit Status Update)

This workflow acts as a CI/CD quality gate for mobile app crash-symbolication ar...

### [Monitor SSL certificate expiry with Google Sheets and SMTP email alerts](https://n8n.io/workflows/12607-monitor-ssl-certificate-expiry-with-google-sheets-and-smtp-e)
- **ID:** 12607 | **Creator:** @mayoub ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Send Email, Google Sheets, Code
- Who is this for?

DevOps engineers, sysadmins, and website owners who manage multiple domains and need proactive SSL certificate expiration monitoring without manual checks.

What it does

Automatical...

### [Monitor SSL certificates for brand-impersonating domains with crt.sh, Urlscan.io and Slack](https://n8n.io/workflows/12221-monitor-ssl-certificates-for-brand-impersonating-domains-wit)
- **ID:** 12221 | **Creator:** @rams1005 ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** HTTP Request, Slack, urlscan.io +1 more
- Phishing Lookout (Typosquatting) and Brand Domain Monitor
This workflow monitors SSL certificate logs to find and scan new domains that might be impersonating your brand.

Background
In modern cyberse...

### [SSL/TLS Certificate Expiry Monitor with Slack Alert](https://n8n.io/workflows/6957-ssl-tls-certificate-expiry-monitor-with-slack-alert)
- **ID:** 6957 | **Creator:** @marth ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** HTTP Request, Slack, Code
- How It Works: The 5-Node Certificate Management Flow 🗓️

This workflow efficiently monitors your domains for certificate expiry.

Scheduled Check (Cron Node): This is the workflow's trigger. It's conf...

### [Generate Domain Insights with WHOIS Lookup and GPT-5-Nano via RapidAPI](https://n8n.io/workflows/8672-generate-domain-insights-with-whois-lookup-and-gpt-5-nano-vi)
- **ID:** 8672 | **Creator:** @oxsr11 ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, OpenAI
- This template allows you to automatically fetch WHOIS data for any domain and display it in a clean, modern HTML card. It doesn’t just stop at showing raw registry data — it also uses a lightweight AI...

### [Prevent Duplicate Processing with Redis Item State Tracking](https://n8n.io/workflows/6828-prevent-duplicate-processing-with-redis-item-state-tracking)
- **ID:** 6828 | **Creator:** @reklaim ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Google Sheets, Redis, Code
- I built this tool because we faced a real, recurring problem: managing hundreds of client projects in a weekly automated loop. 

There was a time when a single error in that process could create a com...

### [Create a Secure MongoDB Data Retrieval API with Input Validation and HTTP Responses](https://n8n.io/workflows/7674-create-a-secure-mongodb-data-retrieval-api-with-input-valida)
- **ID:** 7674 | **Creator:** @sheredia ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** MongoDB, Code
- Data Extraction from MongoDB

Overview
This workflow exposes a public HTTP GET endpoint to read all documents from a MongoDB collection, with:

Strict validation of the collection name

Error handling...

### [Document Q&A System with Voyage-Context-3 Embeddings and MongoDB Atlas](https://n8n.io/workflows/6819-document-qanda-system-with-voyage-context-3-embeddings-and-m)
- **ID:** 6819 | **Creator:** @jimleuk ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** HTTP Request, MongoDB, Code +3 more
- On my never-ending quest to find the best embeddings model, I was intrigued to come across Voyage-Context-3 by MongoDB and was excited to give it a try.

This template implements the embedding model o...

### [Create an automated workitem(incident/bug/userstory) in azure devops](https://n8n.io/workflows/2500-create-an-automated-workitemincident-bug-userstory-in-azure)
- **ID:** 2500 | **Creator:** @autom8r ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, Elasticsearch
- Who is this template for?

This template can be used by any automator who wants to create a workitem(incident/user story/bugs) in azure devops whenever an alert raised by systems.

How it works

Each...

### [Route engineering risks with Anthropic multi-agents and Slack alerts](https://n8n.io/workflows/13698-route-engineering-risks-with-anthropic-multi-agents-and-slac)
- **ID:** 13698 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 7
- **Nodes:** HTTP Request, Slack, Code +4 more
- How It Works
This workflow automates engineering governance by deploying a multi-agent AI system that validates designs, checks compliance, optimises safety, and predicts maintenance needs. Designed f...

### [Route MCP tool calls through an intelligent gateway with Claude AI](https://n8n.io/workflows/13590-route-mcp-tool-calls-through-an-intelligent-gateway-with-cla)
- **ID:** 13590 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** Send Email, Google Sheets, HTTP Request +3 more
- This workflow transforms traditional REST APIs into structured, AI-accessible MCP (Model Context Protocol) tools. It provides a unified gateway that allows Claude AI to safely, granularly, and auditib...

### [OAuth Token Management System with Airtable Storage](https://n8n.io/workflows/6253-oauth-token-management-system-with-airtable-storage)
- **ID:** 6253 | **Creator:** @islamnazmi ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Airtable, HTTP Request, Code
- This workflow contains community nodes that are only compatible with the self-hosted version of n8n.

OAuth Token Generator and Validator

This n8n template helps you generate, validate, and store tok...

### [Server & Network Monitoring Alerts via WhatsApp using HetrixTools](https://n8n.io/workflows/8650-server-and-network-monitoring-alerts-via-whatsapp-using-hetr)
- **ID:** 8650 | **Creator:** @syam785 | **Views:** 0 | **Nodes:** 0
- **Nodes:** 
- This workflow integrates HetrixTools with WhatsApp via the GOWA API to automate notifications about server monitoring events. It distinguishes between Uptime Monitoring and Resource Usage Monitoring e...

### [Monitor Docker host health via SSH with GPT-4o-mini and alerts to Discord](https://n8n.io/workflows/13565-monitor-docker-host-health-via-ssh-with-gpt-4o-mini-and-aler)
- **ID:** 13565 | **Creator:** @dyllank ✓ | **Views:** 0 | **Nodes:** 5
- **Nodes:** Google Sheets, HTTP Request, Code +2 more
- This n8n template builds an automated health monitoring dashboard for your homelab Docker host.

It SSHs into your server, collects 30+ system and container metrics, analyzes trends with AI, and deliv...

### [Automated Credentials Backup to Google Drive via SSH and Docker](https://n8n.io/workflows/11842-automated-credentials-backup-to-google-drive-via-ssh-and-doc)
- **ID:** 11842 | **Creator:** @elitiv | **Views:** 0 | **Nodes:** 1
- **Nodes:** Google Drive
- This workflow automates the backup of decrypted n8n credentials from a self-hosted Docker instance to Google Drive. It allows you to export credentials on n8n versions 2.x.x (where old CLI commands ma...

### [Error Log Monitor with SSH, Slack Alerts & Jira Ticket Creation](https://n8n.io/workflows/6677-error-log-monitor-with-ssh-slack-alerts-and-jira-ticket-crea)
- **ID:** 6677 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Slack, Jira Software, Code
- Description
Automates monitoring of error logs and notifies developers of critical errors.
Sends Slack alerts for critical and non-critical errors, with auto-creation of Jira tickets for critical issu...

### [Check file hash reputation with VirusTotal and Slack alerts](https://n8n.io/workflows/13229-check-file-hash-reputation-with-virustotal-and-slack-alerts)
- **ID:** 13229 | **Creator:** @eedson ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** HTTP Request, Slack, Code
- 🧩 Template Description
File Hash Reputation Checker is a security automation workflow that validates file hashes (MD5, SHA1, SHA256) and checks their reputation using the VirusTotal API. It is design...

### [Scan Single URLs for Security Vulnerabilities with GPT-4 (JS, PHP, Python)](https://n8n.io/workflows/10801-scan-single-urls-for-security-vulnerabilities-with-gpt-4-js)
- **ID:** 10801 | **Creator:** @pyus3r ✓ | **Views:** 0 | **Nodes:** 5
- **Nodes:** Google Drive, Code, HTML +2 more
- Overview
This workflow automates static security analysis for JavaScript, PHP, and Python codebases.  
It’s designed for bug bounty hunters and security researchers who need fast, structured, and AI-a...

### [Generate and Split Sample Data Records using JavaScript and Python](https://n8n.io/workflows/8230-generate-and-split-sample-data-records-using-javascript-and)
- **ID:** 8230 | **Creator:** @rbreen ✓ | **Views:** 0 | **Nodes:** 1
- **Nodes:** Code
- A minimal, plug-and-play workflow that generates sample data using n8n’s Code node (both JavaScript and Python versions included) and then fans out those records into individual items with Split Out....

### [Create a CRUD REST API with Google Sheets Database](https://n8n.io/workflows/8085-create-a-crud-rest-api-with-google-sheets-database)
- **ID:** 8085 | **Creator:** @vklepikovskyi ✓ | **Views:** 0 | **Nodes:** 1
- **Nodes:** Google Sheets
- Simple REST API with Google Sheets

Introduction

This workflow template demonstrates how to quickly and easily create a simple REST API using n8n and a Google Sheet as a no-code database. It's a perf...

### [Compare LLM Token Costs Across 350+ Models with OpenRouter](https://n8n.io/workflows/12100-compare-llm-token-costs-across-350-models-with-openrouter)
- **ID:** 12100 | **Creator:** @philflow | **Views:** 0 | **Nodes:** 4
- **Nodes:** HTTP Request, Code, LangChain Code +1 more
- This n8n template lets you run prompts against 350+ LLM models and see exactly what each request costs with real-time pricing from OpenRouter

  Use cases are many: Compare costs across different mode...

### [Comprehensive API Integration Suite with Health, Webhook, Auth & Rate Limit Monitoring](https://n8n.io/workflows/6607-comprehensive-api-integration-suite-with-health-webhook-auth)
- **ID:** 6607 | **Creator:** @grace-bola ✓ | **Views:** 0 | **Nodes:** 1
- **Nodes:** Call n8n Workflow Tool
- How it works

This workflow creates a complete MCPserver that provides comprehensive API integration monitoring and testing capabilities. The server exposes five specialized tools through a single MCP...

### [Protect public webhooks with Ainoflow Guard rate limiting](https://n8n.io/workflows/13491-protect-public-webhooks-with-ainoflow-guard-rate-limiting)
- **ID:** 13491 | **Creator:** @dmitrijz ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- Webhook Rate Limiter (Ainoflow Guard)

Stop webhook flooding before it starts. Add production-grade rate limiting to any n8n webhook in minutes - reject abusive traffic before expensive workflow logic...

### [MCP Employee Performance & Productivity Insights Engine with Automated Manager  ](https://n8n.io/workflows/11855-mcp-employee-performance-and-productivity-insights-engine-wi)
- **ID:** 11855 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** HTTP Request, Gmail, Code +3 more
- How It Works
This workflow automates performance monitoring by aggregating data from PM tools, code repositories, meeting logs, and CRM systems. It processes team metrics using AI-powered analysis via...

### [Track AI Model Executions with LangFuse Observability for Better Performance Insights](https://n8n.io/workflows/9971-track-ai-model-executions-with-langfuse-observability-for-be)
- **ID:** 9971 | **Creator:** @makarovartyom | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- About this template
This template is to demonstrate how to  trace the observations per execution ID in Langfuse via ingestion API.

Good to know
Endpoint: https://cloud.langfuse.com/api/public/ingesti...

### [Build Persistent Chat Memory with GPT-4o-mini and Qdrant Vector Database](https://n8n.io/workflows/6829-build-persistent-chat-memory-with-gpt-4o-mini-and-qdrant-vec)
- **ID:** 6829 | **Creator:** @einarcesar ✓ | **Views:** 0 | **Nodes:** 8
- **Nodes:** AI Agent, Embeddings OpenAI, OpenAI Chat Model +5 more
- 🧠 Long-Term Memory System for AI Agents with Vector Database

Transform your AI assistants into intelligent agents with persistent memory capabilities. This production-ready workflow implements a soph...

### [Batch Process Data with Redis-powered Debouncing System](https://n8n.io/workflows/11045-batch-process-data-with-redis-powered-debouncing-system)
- **ID:** 11045 | **Creator:** @gregory ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** Redis, Crypto
- How it works
This implementation aggregates incoming data into a Redis list from potentially concurrent workflow executions. It buffers the data for a set period before a single execution retrieves an...

### [Collect API User Data and Store in Google Sheets with CSV Backup](https://n8n.io/workflows/10017-collect-api-user-data-and-store-in-google-sheets-with-csv-ba)
- **ID:** 10017 | **Creator:** @pridevel | **Views:** 0 | **Nodes:** 2
- **Nodes:** Google Sheets, HTTP Request
- 🧠 Overview

This workflow automatically fetches user data from an API, formats it, and stores it in Google Sheets and CSV files.

💡 Use Cases

Collect user records for analytics or reporting
Maintain...

### [Track GitHub Node Definitions and Export to Google Sheets](https://n8n.io/workflows/5814-track-github-node-definitions-and-export-to-google-sheets)
- **ID:** 5814 | **Creator:** @stefan ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Google Sheets, HTTP Request, Code
- Track n8n Node Definitions from GitHub and Export to Google Sheets

Overview
This workflow automatically retrieves and processes metadata from the official n8n GitHub repository, filters all available...

### [Service Health Monitoring with Double-Verification & Slack Alerts](https://n8n.io/workflows/8130-service-health-monitoring-with-double-verification-and-slack)
- **ID:** 8130 | **Creator:** @tuguidragos ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, Slack
- How it works  
This workflow checks the health of your web services or APIs on a schedule, prevents false alerts with a second verification, and sends confirmed failure alerts directly to Slack.  

Pe...

### [Convert POML to AI-Ready Prompts & Chat Messages with Zero Dependencies](https://n8n.io/workflows/7609-convert-poml-to-ai-ready-prompts-and-chat-messages-with-zero)
- **ID:** 7609 | **Creator:** @joeperes ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Code, AI Agent, OpenAI Chat Model
- POML → Prompt/Messages (No-Deps)

What this does

Turns POML markup into either a single Markdown prompt or chat-style messages\[] — using a zero-dependency n8n Code node. It supports variable substit...

### [Assess blockchain smart contract and tokenomics risk with GPT-4o and Gmail](https://n8n.io/workflows/14413-assess-blockchain-smart-contract-and-tokenomics-risk-with-gp)
- **ID:** 14413 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 7
- **Nodes:** Gmail, AI Agent, OpenAI Chat Model +4 more
- How It Works
This workflow automates blockchain risk assessment using a multi-agent AI architecture, targeting DeFi developers, blockchain auditors, and Web3 project teams who need rigorous smart cont...

### [Assess credential risk and route mitigation actions with GPT-4o-mini](https://n8n.io/workflows/13331-assess-credential-risk-and-route-mitigation-actions-with-gpt)
- **ID:** 13331 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 5
- **Nodes:** Code, AI Agent, OpenAI Chat Model +2 more
- How It Works
This workflow automates comprehensive enterprise risk assessment and mitigation planning for organizations managing complex operational, financial, and compliance risks. Designed for risk...

### [Watch GitHub releases and Docker tags, analyze changelogs with Claude Haiku, and send update digests to Slack, Discord, Telegram, and ntfy](https://n8n.io/workflows/13677-watch-github-releases-and-docker-tags-analyze-changelogs-wit)
- **ID:** 13677 | **Creator:** @dyllank ✓ | **Views:** 0 | **Nodes:** 7
- **Nodes:** HTTP Request, Postgres, Slack +4 more
- This n8n template monitors your self-hosted apps for new releases across GitHub and container registries, uses Claude AI to analyze changelogs, and delivers color-coded update digests to Discord, Tele...

### [Dependency Update Risk Analysis with GPT-4o, Slack, Jira & Google Sheets](https://n8n.io/workflows/9835-dependency-update-risk-analysis-with-gpt-4o-slack-jira-and-g)
- **ID:** 9835 | **Creator:** @rahul08 ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** Google Sheets, Slack, Jira Software +3 more
- 📘 Description
This workflow automates dependency update risk analysis and reporting using Jira, GPT-4o, Slack, and Google Sheets.
It continuously monitors Jira for new package or dependency update tic...

### [Generate Weekly Workflow Analytics Reports with n8n API & Email Delivery](https://n8n.io/workflows/10226-generate-weekly-workflow-analytics-reports-with-n8n-api-and)
- **ID:** 10226 | **Creator:** @uuessel ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Gmail, Microsoft Outlook, Code
- Generate Weekly n8n Execution Report and Email Summary

Description:
How it works
Automatically runs every 7 days to pull all n8n workflow executions from the past week
Merges execution data with work...

### [Generate QA Test Cases from Figma Designs to Google Sheets using GPT-4o-mini](https://n8n.io/workflows/10326-generate-qa-test-cases-from-figma-designs-to-google-sheets-u)
- **ID:** 10326 | **Creator:** @rahul08 ✓ | **Views:** 0 | **Nodes:** 7
- **Nodes:** Google Sheets, HTTP Request, Code +4 more
- Description
Transform Figma design files into detailed QA test cases with AI-driven analysis and structured export to Google Sheets. This workflow helps QA and product teams streamline design validati...

### [Sync Android drawable assets from Figma to GitHub via PR (multi-density PNG)](https://n8n.io/workflows/8112-sync-android-drawable-assets-from-figma-to-github-via-pr-mul)
- **ID:** 8112 | **Creator:** @weblineindia ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- Sync Android drawable assets from Figma to GitHub via PR (multi‑density PNG)

This n8n workflow automatically fetches design assets (icons, buttons) from Figma, exports them into Android drawable fold...

### [Bypass Cloudflare Turnstile for Web Scraping with 2captcha](https://n8n.io/workflows/7151-bypass-cloudflare-turnstile-for-web-scraping-with-2captcha)
- **ID:** 7151 | **Creator:** @ludwig ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- This workflow contains community nodes that are only compatible with the self-hosted version of n8n.

Bypass Cloudflare Turnstile for Web Scraping with n8n
How It Works
This workflow automatically sol...

### [Manage engineering change requests via webhooks and Slack approvals](https://n8n.io/workflows/13932-manage-engineering-change-requests-via-webhooks-and-slack-ap)
- **ID:** 13932 | **Creator:** @onepiceace ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** Slack, Crypto
- ⚙️ Manage Engineering Change Requests (ECR) via Slack

📋 Overview
Streamline your engineering change management process by integrating generic webhooks with Slack interactive approvals. This workflow...

### [Automated Workflow Backup with Intelligent Change Detection using GitHub](https://n8n.io/workflows/7304-automated-workflow-backup-with-intelligent-change-detection)
- **ID:** 7304 | **Creator:** @j2h4u | **Views:** 0 | **Nodes:** 3
- **Nodes:** GitHub, Telegram, Code
- Advanced n8n Workflow Sync with GitHub

A robust workflow to back up and synchronize your n8n workflows to a GitHub repository, with intelligent change detection and support for file renames.

🎯 Who's...

### [Orchestrate enterprise MCP AI tool access with Claude and Google Sheets](https://n8n.io/workflows/13592-orchestrate-enterprise-mcp-ai-tool-access-with-claude-and-go)
- **ID:** 13592 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** Send Email, Google Sheets, HTTP Request +3 more
- A secure, scalable enterprise AI orchestration layer built on the Model Context Protocol (MCP). This workflow standardizes tool access across all business systems, enforces permission-based data handl...

### [Automate n8n Updates with Version Checking and Portainer Webhook](https://n8n.io/workflows/7061-automate-n8n-updates-with-version-checking-and-portainer-web)
- **ID:** 7061 | **Creator:** @dominic | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- 🔄 Purpose of the Workflow:
The Update-N8N workflow is designed to automatically trigger a (Portainer) webhook to update an N8N container, but only if a new version of N8N is available.

⚙️ Detailed Wo...

### [Set Up Complete MERN Stack Development Environment on Linux Server](https://n8n.io/workflows/6131-set-up-complete-mern-stack-development-environment-on-linux)
- **ID:** 6131 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 0
- **Nodes:** 
- This automated n8n workflow sets up a complete MERN Stack development environment on a Linux server by installing core technologies, development tools, package managers, global npm packages, deploymen...

### [Complete LAMP Stack (Linux, Apache, MySQL, PHP) Automated Server Setup](https://n8n.io/workflows/6136-complete-lamp-stack-linux-apache-mysql-php-automated-server)
- **ID:** 6136 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 0
- **Nodes:** 
- This automated n8n workflow enables the rapid setup of a complete LAMP (Linux, Apache, MySQL, PHP) stack on a Linux server, executing the entire process in approximately 10 seconds. It configures the...

### [🐟 Smart Fish Feeder: Weather-Based Feeding System with BMKG & Telegram Alerts](https://n8n.io/workflows/8667-smart-fish-feeder-weather-based-feeding-system-with-bmkg-an)
- **ID:** 8667 | **Creator:** @tegarkaruniailham ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** HTTP Request, Telegram, Code
- 🌦️ Intelligent Aquaculture Automation for Indonesia

Transform your fish farming operation with this cutting-edge n8n workflow that combines Indonesia's official BMKG weather data with IoT-powered fee...

### [Daily Postgres Table Backup to GitHub in CSV Format](https://n8n.io/workflows/7419-daily-postgres-table-backup-to-github-in-csv-format)
- **ID:** 7419 | **Creator:** @jay-emp0 ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** GitHub, Postgres, Code
- This workflow automatically backs up all public Postgres tables into a GitHub repository as CSV files every 24 hours.  
It ensures your database snapshots are always up to date updating existing files...

### [Export Jamf Policies to Slack as CSV for Instant Auditing](https://n8n.io/workflows/6440-export-jamf-policies-to-slack-as-csv-for-instant-auditing)
- **ID:** 6440 | **Creator:** @mrrobot ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, Slack
- 🧩 Jamf Policies Export to Slack
Quickly export and review your entire Jamf policy configuration—including triggers, frequencies, and scope—directly in Slack.
This enables IT and security teams to audi...

### [Export Jamf Smart Group Membership to Slack as Viewable CSV Reports](https://n8n.io/workflows/6040-export-jamf-smart-group-membership-to-slack-as-viewable-csv)
- **ID:** 6040 | **Creator:** @mrrobot ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** HTTP Request, Slack, Code
- 🧩 Jamf Smart Group Membership to Slack
Automatically export Jamf smart group membership to Slack in CSV format.
Perfect for IT and security teams who need fast visibility into device grouping—without...

### [Audit Website Security Headers with AI Remediation and Google Sheets Reporting](https://n8n.io/workflows/10990-audit-website-security-headers-with-ai-remediation-and-googl)
- **ID:** 10990 | **Creator:** @just-aristides ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** Google Sheets, HTTP Request, Gmail +3 more
- What It Is

  An automated workflow for auditing website security headers and generating
  comprehensive security reports.

  The workflow consists of three main phases:

  Perform Security Scan
  Sav...

### [Coordinate patient care and alerts with EHR/FHIR, GPT-4, Twilio, Gmail and Slack](https://n8n.io/workflows/12734-coordinate-patient-care-and-alerts-with-ehr-fhir-gpt-4-twili)
- **ID:** 12734 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 9
- **Nodes:** Send Email, HTTP Request, Postgres +6 more
- How It Works
This workflow automates end-to-end patient care coordination by monitoring appointment schedules, clinical events, and care milestones while orchestrating personalized communications acro...

### [Monitor Amadeus & Booking.com API Health with WhatsApp SLA Alerts](https://n8n.io/workflows/6263-monitor-amadeus-and-bookingcom-api-health-with-whatsapp-sla)
- **ID:** 6263 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** HTTP Request, WhatsApp Business Cloud, Code +1 more
- This guide details the setup and functionality of an automated workflow designed to monitor the health, uptime, and SLA compliance of travel supplier APIs, specifically the Amadeus Flight API and Book...

### [Automated Hourly n8n Error Monitoring with Slack Notifications](https://n8n.io/workflows/7076-automated-hourly-n8n-error-monitoring-with-slack-notificatio)
- **ID:** 7076 | **Creator:** @julinho ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** Slack, Code
- Who is this template for?

This template is ideal for n8n instance administrators, developers, and DevOps teams who need a proactive and organized way to monitor the health of their automations. If yo...

### [IPL Cricket Rules Q&A Chat Bot using RAG and Google Gemini API](https://n8n.io/workflows/7413-ipl-cricket-rules-qanda-chat-bot-using-rag-and-google-gemini)
- **ID:** 7413 | **Creator:** @p10siddarthap | **Views:** 0 | **Nodes:** 8
- **Nodes:** HTTP Request, AI Agent, Simple Memory +5 more
- This workflow has 2 Broad Steps
Step 1 - Vector store creation with set of ipl rules using Google Gemini Embedding. This will we used to drive RAG for model grouding    
Step 2 - Connecting the vector...

### [Cybersecurity Assistant with GPT-4, Telegram Bot & Command Execution](https://n8n.io/workflows/7023-cybersecurity-assistant-with-gpt-4-telegram-bot-and-command)
- **ID:** 7023 | **Creator:** @mariskarthick ✓ | **Views:** 0 | **Nodes:** 5
- **Nodes:** Telegram, AI Agent, OpenAI Chat Model +2 more
- QuantumDefender AI is a next-generation intelligent cybersecurity assistant designed to harness the symbolic strength of quantum computing’s promise alongside cutting-edge AI capabilities. This sophis...

### [Daily Sync of NFL Players from Sleeper API to Airtable for Fantasy Football](https://n8n.io/workflows/6602-daily-sync-of-nfl-players-from-sleeper-api-to-airtable-for-f)
- **ID:** 6602 | **Creator:** @patjennings916 ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** Airtable, HTTP Request
- Sleeper NFL Players Sync 

This template uses the Sleeper API to fetch the complete list of NFL players and stores them in an Airtable base. It’s built to run daily and ensures you have the most up-to...

### [Automated MySQL to Google Sheets Sync with Duplicate Prevention](https://n8n.io/workflows/6261-automated-mysql-to-google-sheets-sync-with-duplicate-prevent)
- **ID:** 6261 | **Creator:** @ahmedsaadawi ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** Google Sheets, MySQL
- 📝 Sync MySQL Rows to Google Sheet

Description:

This n8n template automates the process of syncing new records from a MySQL database table into a Google Sheet, ideal for reporting, backup, or lightwe...

### [Syncing iOS Localization Gaps with Google Sheets and GitHub PR Placeholders](https://n8n.io/workflows/7577-syncing-ios-localization-gaps-with-google-sheets-and-github)
- **ID:** 7577 | **Creator:** @weblineindia ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Google Sheets, HTTP Request, Code
- Fill iOS localization gaps from .strings → Google Sheets and PR with placeholders (GitHub)

This n8n workflow automatically identifies missing translations in .strings files across iOS localizations (...

### [Data Analytics Department with AI Team: CDO & Specialists Using OpenAI O3](https://n8n.io/workflows/6912-data-analytics-department-with-ai-team-cdo-and-specialists-u)
- **ID:** 6912 | **Creator:** @yaron-nofluff ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** AI Agent, OpenAI Chat Model, Think Tool +1 more
- CDO Agent with Data Analytics Team

Description
Complete AI-powered data analytics department with a Chief Data Officer (CDO) agent orchestrating specialized data team members for comprehensive data s...

### [Sync QuickBooks Chart of Accounts to Google BigQuery](https://n8n.io/workflows/6554-sync-quickbooks-chart-of-accounts-to-google-bigquery)
- **ID:** 6554 | **Creator:** @fahmiiireza ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** HTTP Request, Google BigQuery, Code
- Sync QuickBooks Chart of Accounts to Google BigQuery
Keep a historical, structured copy of your QuickBooks Chart of Accounts in BigQuery. This n8n workflow runs weekly, syncing new or updated accounts...

### [Automate Power BI Dataset Refreshes with History Monitoring](https://n8n.io/workflows/7336-automate-power-bi-dataset-refreshes-with-history-monitoring)
- **ID:** 7336 | **Creator:** @rbreen ✓ | **Views:** 0 | **Nodes:** 0
- **Nodes:** 
- This workflow contains community nodes that are only compatible with the self-hosted version of n8n.

This n8n workflow provides automated Power BI dataset refresh capabilities with built-in refresh h...

### [JSON Data Utility: Extract Key-Value Pairs by Index](https://n8n.io/workflows/6615-json-data-utility-extract-key-value-pairs-by-index)
- **ID:** 6615 | **Creator:** @weblineindia ✓ | **Views:** 0 | **Nodes:** 1
- **Nodes:** Code
- Extract a key–value pair by index from JSON to fields in n8n

This template takes a JSON object and a row index and returns exactly one key–value pair at that index. It’s a handy helper when you only...

### [Create Custom Reasoning Patterns for AI Agents with GraphRAG & Knowledge Ontology](https://n8n.io/workflows/6816-create-custom-reasoning-patterns-for-ai-agents-with-graphrag)
- **ID:** 6816 | **Creator:** @infranodus ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** AI Agent, OpenAI Chat Model, Simple Memory
- Teach your AI agent HOW to think, not WHAT to think



This workflow demonstrates how you can build an AI agent in n8n that uses the reasoning logic you define. So an LLM learns a way of thinking, whi...

### [Automated Security Alert Analysis with Sophos, Gemini AI, and VirusTotal](https://n8n.io/workflows/6296-automated-security-alert-analysis-with-sophos-gemini-ai-and)
- **ID:** 6296 | **Creator:** @rizkyriyan | **Views:** 0 | **Nodes:** 6
- **Nodes:** HTTP Request, Telegram, Code +3 more
- How It Works
This workflow automates the analysis of security alerts from Sophos Central, turning raw events into actionable intelligence. It uses the official Sophos SIEM integration tool to fetch da...

### [Automatic Email Notifications for n8n Version Releases with Gmail](https://n8n.io/workflows/11005-automatic-email-notifications-for-n8n-version-releases-with)
- **ID:** 11005 | **Creator:** @mohamed3nan | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, Gmail
- 📢 Monitor n8n releases and get notifications for new versions 🆕

This workflow automatically monitors n8n’s release channels (latest and beta) and sends you email notifications whenever a new version...

### [Send end-of-life software alerts using NocoDB, endoflife.date, and Slack](https://n8n.io/workflows/14309-send-end-of-life-software-alerts-using-nocodb-endoflifedate)
- **ID:** 14309 | **Creator:** @lukaszpp ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** HTTP Request, Slack, NocoDB +1 more
- What Is This?

This workflow is an automated system that tracks End-of-Life (EOL) dates for software and technologies used across your projects. It eliminates the need to manually monitor EOL dates in...

### [Email reports on expiring Microsoft Entra ID app secrets and certificates with Microsoft Graph](https://n8n.io/workflows/12399-email-reports-on-expiring-microsoft-entra-id-app-secrets-and)
- **ID:** 12399 | **Creator:** @alexschnabl ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Send Email, HTTP Request, HTML
- Monitor expiring EntraID application secrets and notify responsible

Stay ahead of credential expirations by automatically detecting Entra ID application client secrets and certificates that are abou...

### [Automate Demand Forecasting & Inventory Ordering with AI, MySQL & Optimal Supplier Selection](https://n8n.io/workflows/12158-automate-demand-forecasting-and-inventory-ordering-with-ai-m)
- **ID:** 12158 | **Creator:** @riorio ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** HTTP Request, Slack, MySQL +1 more
- This workflow streamlines the entire inventory replenishment process by leveraging AI for demand forecasting and intelligent logic for supplier selection. It aggregates data from multiple sources—POS...

### [Back up workflows to Google Drive daily with automatic cleanup](https://n8n.io/workflows/13866-back-up-workflows-to-google-drive-daily-with-automatic-clean)
- **ID:** 13866 | **Creator:** @evilasioffilho ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** HTTP Request, Google Drive, Code
- This workflow automatically creates daily backups of all n8n workflows and stores them in Google Drive, using the n8n API to export workflows and a scheduled retention policy to keep storage organized...

### [Automated Execution Cleanup System with n8n API and Custom Retention Rules](https://n8n.io/workflows/6833-automated-execution-cleanup-system-with-n8n-api-and-custom-r)
- **ID:** 6833 | **Creator:** @arlindeveloper ✓ | **Views:** 0 | **Nodes:** 1
- **Nodes:** Code
- Make your n8n instance faster, cleaner, and more efficient by deleting old workflow executions — while keeping only the most recent ones you actually need. Whether you're using n8n Cloud or self-hoste...

### [Test WAF security interactively with an AI agent and WAFtester MCP](https://n8n.io/workflows/13443-test-waf-security-interactively-with-an-ai-agent-and-waftest)
- **ID:** 13443 | **Creator:** @qandil ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** AI Agent, OpenAI Chat Model, MCP Client Tool
- What it does

A conversational AI agent that connects to WAFtester via MCP (Model Context Protocol) for interactive Web Application Firewall security testing. Type natural language requests — the agen...

### [Create a Complete AI Engineering Department with OpenAI O3 and Specialized Agents](https://n8n.io/workflows/6911-create-a-complete-ai-engineering-department-with-openai-o3-a)
- **ID:** 6911 | **Creator:** @yaron-nofluff ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** AI Agent, OpenAI Chat Model, Think Tool +1 more
- CTO Agent with Engineering Team

Description
Complete AI-powered engineering department with a Chief Technology Officer (CTO) agent orchestrating specialized engineering team members for comprehensive...

## DevOps
(107 workflows)

### [Host your own Uptime Monitoring with Scheduled Triggers](https://n8n.io/workflows/2327-host-your-own-uptime-monitoring-with-scheduled-triggers)
- **ID:** 2327 | **Creator:** @jimleuk ✓ | **Views:** 21,003 | **Nodes:** 4
- **Nodes:** Google Sheets, HTTP Request, Slack +1 more
- This n8n workflow demonstrates how to build a simple uptime monitoring service using scheduled triggers.

Useful for webmasters with a handful of sites who want a cost-effective solution without the n...

### [Automate SIEM Alert Enrichment with MITRE ATT&CK, Qdrant & Zendesk in n8n](https://n8n.io/workflows/2840-automate-siem-alert-enrichment-with-mitre-attandck-qdrant-an)
- **ID:** 2840 | **Creator:** @djangelic ✓ | **Views:** 12,446 | **Nodes:** 10
- **Nodes:** Google Drive, Zendesk, AI Agent +7 more
- n8n Workflow: Automate SIEM Alert Enrichment with MITRE ATT&CK & Qdrant  

Who is this for?  
This workflow is ideal for:  
Cybersecurity teams & SOC analysts* who want to automate *SIEM alert enrichm...

### [Nightly n8n backup to Dropbox](https://n8n.io/workflows/2075-nightly-n8n-backup-to-dropbox)
- **ID:** 2075 | **Creator:** @jdana ✓ | **Views:** 6,308 | **Nodes:** 1
- **Nodes:** Dropbox
- This template will create a nightly backup of all your n8n workflows to a Dropbox folder. Each night, the previous night's backups are moved into an "old" folder, and renamed with the date they were t...

### [Split In Batches node noItemsLeft example](https://n8n.io/workflows/995-split-in-batches-node-noitemsleft-example)
- **ID:** 995 | **Creator:** @harshil1712 ✓ | **Views:** 5,813 | **Nodes:** 0
- **Nodes:** 
- This workflow demonstrates how to use noItemsLeft to check if there are items left to be processed by the SplitInBatches node.



Function node: This node generates mock data for the workflow. Replace...

### [Backup workflows to git repository on Github](https://n8n.io/workflows/2532-backup-workflows-to-git-repository-on-github)
- **ID:** 2532 | **Creator:** @shashikanth | **Views:** 5,778 | **Nodes:** 2
- **Nodes:** GitHub, Code
- Source code, I maintain this worflow here.

Usage Guide

This workflow backs up all workflows as JSON files named in the [workflow_name].json format.

Steps

Create GitHub Repository  
   Skip this st...

### [Monitor Security Advisories](https://n8n.io/workflows/1974-monitor-security-advisories)
- **ID:** 1974 | **Creator:** @n8n-team ✓ | **Views:** 5,581 | **Nodes:** 3
- **Nodes:** Jira Software, Gmail, Customer Datastore (n8n training)
- This n8n workflow automates the monitoring and notification of Palo Alto Networks security advisories. It is triggered manually from within the n8n UI or scheduled to run daily at midnight using the S...

### [🎓 Learn Workflow Logic with Merge, IF & Switch Operations](https://n8n.io/workflows/5996-learn-workflow-logic-with-merge-if-and-switch-operations)
- **ID:** 5996 | **Creator:** @lucaspeyrin ✓ | **Views:** 3,812 | **Nodes:** 0
- **Nodes:** 
- How it works

Ever wonder how to make your workflows smarter? How to handle different types of data in different ways? This template is a hands-on tutorial that teaches you the three most fundamental...

### [Check VPS resource usage every 15 minutes](https://n8n.io/workflows/2951-check-vps-resource-usage-every-15-minutes)
- **ID:** 2951 | **Creator:** @hostinger ✓ | **Views:** 3,681 | **Nodes:** 1
- **Nodes:** Send Email
- This n8n workflow template is designed to help system administrators and DevOps professionals monitor key resource usage metrics — CPU, RAM, and Disk — on a VPS (Virtual Private Server). The workflow...

### [Attach a default error handler to all active workflows](https://n8n.io/workflows/2312-attach-a-default-error-handler-to-all-active-workflows)
- **ID:** 2312 | **Creator:** @bartv | **Views:** 3,658 | **Nodes:** 2
- **Nodes:** Gmail, Code
- How it works:

Did you ever miss any errors in your workflow executions? I did! And I usually only realised a few days or weeks later. 🙈

This template attaches a default error workflow to all your ac...

### [Analyze Email Headers for IP Reputation and Spoofing Detection - Outlook](https://n8n.io/workflows/2676-analyze-email-headers-for-ip-reputation-and-spoofing-detecti)
- **ID:** 2676 | **Creator:** @djangelic ✓ | **Views:** 3,549 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- Analyze Emails for Security Insights

Who is this for?

This workflow is ideal for security teams, IT Ops professionals, and managed service providers (MSPs) responsible for monitoring and validating...

### [Send SMS alerts based on database queries (Twilio and Postgres)](https://n8n.io/workflows/357-send-sms-alerts-based-on-database-queries-twilio-and-postgre)
- **ID:** 357 | **Creator:** @tanay1337 ✓ | **Views:** 3,185 | **Nodes:** 2
- **Nodes:** Postgres, Twilio
- This workflow automatically queries a Postgres database to find outlier readings for which SMS notifications have not been sent.
This is Workflow 2 in the blog tutorial Database activity monitoring an...

### [Multiple Websites Monitoring with Notifications including Phone Calls](https://n8n.io/workflows/4833-multiple-websites-monitoring-with-notifications-including-ph)
- **ID:** 4833 | **Creator:** @infyom ✓ | **Views:** 2,840 | **Nodes:** 6
- **Nodes:** Google Sheets, HTTP Request, Slack +3 more
- ✅ What problem does this workflow solve?
Automatically monitor multiple websites every 5 minutes, log downtime, notify your team instantly via multiple channels, and track uptime/downtime in a Google...

### [Manage custom incident response in PagerDuty and Jira](https://n8n.io/workflows/353-manage-custom-incident-response-in-pagerduty-and-jira)
- **ID:** 353 | **Creator:** @tanay1337 ✓ | **Views:** 2,624 | **Nodes:** 2
- **Nodes:** Mattermost, Jira Software
- This workflow automatically follows the steps in a custom incident response playbook and manages incidents in PagerDuty, Jira tickets, and notifies the on-call team in Mattermost.

This workflow consi...

### [Health Check Websites with Google Sheets & Telegram Alerts](https://n8n.io/workflows/3352-health-check-websites-with-google-sheets-and-telegram-alerts)
- **ID:** 3352 | **Creator:** @hpstock ✓ | **Views:** 2,597 | **Nodes:** 3
- **Nodes:** Google Sheets, HTTP Request, Telegram
- What does this template do ? 

This workflow performs scheduled health checks on a list of URLs stored in a Google Sheet. Every X minutes, it retrieves the URLs, sends HTTP requests to check their ava...

### [Error Handler send Telegram: Real-Time Workflow Failure Alerts](https://n8n.io/workflows/3038-error-handler-send-telegram-real-time-workflow-failure-alert)
- **ID:** 3038 | **Creator:** @meow-cde | **Views:** 2,324 | **Nodes:** 1
- **Nodes:** Telegram
- This workflow acts as an error handler, sending real-time notifications to Telegram when another workflow fails. It provides detailed error information, including workflow name, timestamp, execution U...

### [Get Long Lived Facebook User or Page Access Token](https://n8n.io/workflows/2535-get-long-lived-facebook-user-or-page-access-token)
- **ID:** 2535 | **Creator:** @siraekabut ✓ | **Views:** 2,218 | **Nodes:** 1
- **Nodes:** HTTP Request
- Facebook access tokens expire quickly, requiring regular updates for continued API access. This workflow simplifies the process of exchanging short-lived tokens for long-lived ones, saving time and re...

### [🎓 Learn Data Synchronization: Warehouse Inventory Audit Tutorial](https://n8n.io/workflows/5999-learn-data-synchronization-warehouse-inventory-audit-tutori)
- **ID:** 5999 | **Creator:** @lucaspeyrin ✓ | **Views:** 2,199 | **Nodes:** 0
- **Nodes:** 
- How it works

This template is a hands-on tutorial for one of n8n's most powerful data tools: the Compare Datasets node. It's the perfect next step after learning basic logic, showing you how to build...

### [Create Snapshot of Contabo VPS instances on a daily basis](https://n8n.io/workflows/2403-create-snapshot-of-contabo-vps-instances-on-a-daily-basis)
- **ID:** 2403 | **Creator:** @dubcom | **Views:** 2,080 | **Nodes:** 1
- **Nodes:** HTTP Request
- Workflow: Snapshot Contabo

How it Works
This workflow automates daily backups (snapshots) of VPS instances hosted on Contabo. Each day at midnight, it checks for existing snapshots and ensures that o...

### [Get local datetime into Function node using moment.js](https://n8n.io/workflows/695-get-local-datetime-into-function-node-using-momentjs)
- **ID:** 695 | **Creator:** @trey ✓ | **Views:** 1,724 | **Nodes:** 0
- **Nodes:** 
- A quick example showing how to get the local date and time into a Function node using moment.js.

This relies on the GENERIC_TIMEZONE environment variable being correctly configured (see the docs he...

### [Control Your n8n Instance Remotely with Telegram Bot Commands](https://n8n.io/workflows/4928-control-your-n8n-instance-remotely-with-telegram-bot-command)
- **ID:** 4928 | **Creator:** @arthurmb ✓ | **Views:** 1,479 | **Nodes:** 2
- **Nodes:** Telegram, Code
- This workflow contains community nodes that are only compatible with the self-hosted version of n8n.

Your n8n Command Center in a Telegram Chat
Remotely manage and operate your n8n instance from Tele...

### [Send n8n automation errors to a Monday.com board](https://n8n.io/workflows/2074-send-n8n-automation-errors-to-a-mondaycom-board)
- **ID:** 2074 | **Creator:** @jdana ✓ | **Views:** 1,376 | **Nodes:** 2
- **Nodes:** Monday.com, Code
- This template is an error handler that will log n8n workflow errors to a Monday.com board for troubleshooting and tracking.

Prerequisites
Monday account and Monday credential
Create a board on Monday...

### [Reduce LLM Costs with Semantic Caching using Redis Vector Store and HuggingFace](https://n8n.io/workflows/10887-reduce-llm-costs-with-semantic-caching-using-redis-vector-st)
- **ID:** 10887 | **Creator:** @tishun | **Views:** 1,229 | **Nodes:** 8
- **Nodes:** Code, AI Agent, Embeddings Hugging Face Inference +5 more
- Stop Paying for the Same Answer Twice 

Your LLM is answering the same questions over and over. "What's the weather?" "How's the weather today?" "Tell me about the weather." Same answer, three API cal...

### [Improve AI Agent System Prompts with GPT-4o Feedback Analysis and Email Delivery](https://n8n.io/workflows/4197-improve-ai-agent-system-prompts-with-gpt-4o-feedback-analysi)
- **ID:** 4197 | **Creator:** @danielrosehill ✓ | **Views:** 1,027 | **Nodes:** 4
- **Nodes:** Gmail, AI Agent, OpenAI Chat Model +1 more
- AI Agent System Prompt 'Auto-Tuner'

 This workflow configures an AI agent which provides an edited system prompt for an autonomous AI agent Based on the following pieces of information provided by th...

### [Retry on fail except for known error](https://n8n.io/workflows/2719-retry-on-fail-except-for-known-error)
- **ID:** 2719 | **Creator:** @octionic ✓ | **Views:** 940 | **Nodes:** 0
- **Nodes:** 
- Purpose

This workflow snippet allows for advanced error catching during retry attempts.

There are cases, where you want to check if an item exists first, so you can determine the following actions....

### [Manage group members in Bitwarden automatically](https://n8n.io/workflows/1001-manage-group-members-in-bitwarden-automatically)
- **ID:** 1001 | **Creator:** @harshil1712 ✓ | **Views:** 938 | **Nodes:** 1
- **Nodes:** Bitwarden
- This workflow allows you to create a group, add members to the group, and get the members of the group.



Bitwarden node: This node will create a new group called documentation in Bitwarden.

Bitward...

### [Centralized n8n Error Management System with Automated Email Alerts via Gmail](https://n8n.io/workflows/4519-centralized-n8n-error-management-system-with-automated-email)
- **ID:** 4519 | **Creator:** @danielng ✓ | **Views:** 877 | **Nodes:** 3
- **Nodes:** Gmail, Code, HTML
- Advanced n8n Error Handling: Automated Email Alerts & Global Error Workflow Configuration

In any automated environment, n8n workflows, while powerful, can sometimes encounter unexpected issues or fai...

### [🧠 FloWatch 👁️ Analyze and Diagnose n8n Workflow Errors via OpenAI and Email](https://n8n.io/workflows/3595-flowatch-analyze-and-diagnose-n8n-workflow-errors-via-open)
- **ID:** 3595 | **Creator:** @joeperes ✓ | **Views:** 838 | **Nodes:** 5
- **Nodes:** Gmail, Code, AI Agent +2 more
- 🧠 Analyze and Diagnose n8n Workflow Errors Automatically via OpenAI and Email



&gt; ⚠️ This template is available on ☁️ Cloud & 🖥️ self-hosted n8n instances with the OpenAI node enabled.

👤 Who is t...

### [Receive updates for AWS SNS Events](https://n8n.io/workflows/509-receive-updates-for-aws-sns-events)
- **ID:** 509 | **Creator:** @sm-amudhan ✓ | **Views:** 795 | **Nodes:** 0
- **Nodes:** 
- Companion workflow for AWS SNS Trigger node docs

### [AI Chatbot Call Center: General Exception Flow (Production-Ready, Part 8)](https://n8n.io/workflows/4052-ai-chatbot-call-center-general-exception-flow-production-rea)
- **ID:** 4052 | **Creator:** @chatpaylabs ✓ | **Views:** 766 | **Nodes:** 1
- **Nodes:** Slack
- Workflow Name: 👻 Exception Flow

Template was created in n8n v1.90.2

Skill Level: Low

Categories: n8n, Chatbot

Stacks

Error Trigger
Slack node

What this workflow does?

This is a n8n Error Workfl...

### [n8n Workflow Error Alerts with Google Sheets, Telegram, and Gmail](https://n8n.io/workflows/4407-n8n-workflow-error-alerts-with-google-sheets-telegram-and-gm)
- **ID:** 4407 | **Creator:** @aitoralonso ✓ | **Views:** 754 | **Nodes:** 3
- **Nodes:** Google Sheets, Telegram, Gmail
- This n8n workflow provides a robust error handling and notification system for your n8n workflows. When an error occurs, it automatically logs the error details to Google Sheets, sends a notification...

### [Auto-Retry Engine: Error Recovery Workflow](https://n8n.io/workflows/3144-auto-retry-engine-error-recovery-workflow)
- **ID:** 3144 | **Creator:** @gatura ✓ | **Views:** 747 | **Nodes:** 1
- **Nodes:** HTTP Request
- Workflow Documentation: Auto-Retry Engine – Error Recovery Workflow  

Detailed Description  

The Auto-Retry Engine: Error Recovery Workflow is designed to automate the process of identifying and ret...

### [Get the job details using the Cortex node](https://n8n.io/workflows/809-get-the-job-details-using-the-cortex-node)
- **ID:** 809 | **Creator:** @harshil1712 ✓ | **Views:** 680 | **Nodes:** 1
- **Nodes:** Cortex

### [Benchmark content safety guardrails with automated test suite & reports](https://n8n.io/workflows/10729-benchmark-content-safety-guardrails-with-automated-test-suit)
- **ID:** 10729 | **Creator:** @patrickn8n ✓ | **Views:** 660 | **Nodes:** 4
- **Nodes:** Gmail, Code, OpenAI Chat Model +1 more
- 🛡️ Evaluate Guardrails Node Accuracy with Automated Test Suite

This workflow benchmarks the n8n Guardrails node across multiple safety categories -including PII, NSFW, jailbreak attempts, secret keys...

### [Automate Droplet Snapshots on DigitalOcean](https://n8n.io/workflows/2485-automate-droplet-snapshots-on-digitalocean)
- **ID:** 2485 | **Creator:** @optimus01 ✓ | **Views:** 615 | **Nodes:** 1
- **Nodes:** HTTP Request
- This workflow automates the management of DigitalOcean Droplet snapshots by listing all droplets, filtering based on the number of snapshots, and deleting excess snapshots before creating new ones. It...

### [Create, update, and get an incident on PagerDuty](https://n8n.io/workflows/411-create-update-and-get-an-incident-on-pagerduty)
- **ID:** 411 | **Creator:** @tanay1337 ✓ | **Views:** 576 | **Nodes:** 1
- **Nodes:** PagerDuty

### [Set DevOps Infrastructure with Docker, K3s, Jenkins & Grafana for Linux Servers](https://n8n.io/workflows/6140-set-devops-infrastructure-with-docker-k3s-jenkins-and-grafan)
- **ID:** 6140 | **Creator:** @oneclick-ai ✓ | **Views:** 561 | **Nodes:** 0
- **Nodes:** 
- This automated n8n workflow delivers an instant DevOps toolkit by installing Docker, K3s, Jenkins, Grafana, and more on a Linux server within 10 seconds. It optimizes performance, enhances security, a...

### [Automated Workflow Backup System with Google Drive, Gmail and Discord Alerts'](https://n8n.io/workflows/3787-automated-workflow-backup-system-with-google-drive-gmail-and)
- **ID:** 3787 | **Creator:** @hochien-chang | **Views:** 541 | **Nodes:** 4
- **Nodes:** Google Drive, Discord, Gmail +1 more
- How it works

This workflow automates the backup of all your n8n workflows to a specified Google Drive folder. It operates in two main phases:

Orchestration (Scheduled Task):
    The workflow is init...

### [LLM Usage Tracker & Cost Monitor with Node-Level Analytics (v2)](https://n8n.io/workflows/7398-llm-usage-tracker-and-cost-monitor-with-node-level-analytics)
- **ID:** 7398 | **Creator:** @amirsafavi | **Views:** 509 | **Nodes:** 1
- **Nodes:** Code
- LLM Cost Monitor & Usage Tracker for n8n

&gt; v2: Now it can read multiple types of LLM usages. Better dynamic approach for reading model usage. 

🎯 What This Workflow Does

This workflow provides co...

### [Hostinger Daily VPS Snapshot and server metrics](https://n8n.io/workflows/3807-hostinger-daily-vps-snapshot-and-server-metrics)
- **ID:** 3807 | **Creator:** @lsmelo | **Views:** 352 | **Nodes:** 0
- **Nodes:** 
- Keep your Hostinger VPS servers secure with automated backups! This n8n (self-hosted) workflow for is designed to create daily snapshots and send server metrics effortlessly, ensuring you always have...

### [Generate Azure VM Timeline Reports with Google Gemini AI Chat Assistant](https://n8n.io/workflows/4513-generate-azure-vm-timeline-reports-with-google-gemini-ai-cha)
- **ID:** 4513 | **Creator:** @adbertram ✓ | **Views:** 349 | **Nodes:** 5
- **Nodes:** AI Agent, Simple Memory, Code Tool +2 more
- An AI-powered chat assistant that analyzes Azure virtual machine activity and generates detailed timeline reports showing VM state changes, performance metrics, and operational events over time.

How...

### [Website Monitoring, Scheduling, and Email Alerts Template](https://n8n.io/workflows/5067-website-monitoring-scheduling-and-email-alerts-template)
- **ID:** 5067 | **Creator:** @anandicon | **Views:** 292 | **Nodes:** 2
- **Nodes:** Send Email, HTTP Request
- 🛠 Website Downtime Monitoring with Scheduled Checks and Email Alerts

Easily monitor your website uptime and receive instant email alerts when it becomes unreachable — using this no-code template powe...

### [ Validate Seatable Webhooks with HMAC SHA256 Authentication](https://n8n.io/workflows/3439-validate-seatable-webhooks-with-hmac-sha256-authentication)
- **ID:** 3439 | **Creator:** @vquie ✓ | **Views:** 286 | **Nodes:** 1
- **Nodes:** Crypto
- 📌 Validate Seatable Webhooks with HMAC SHA256 Authentication

This mini workflow is designed to securely validate incoming Seatable webhooks using HMAC SHA256 signature verification.

🔐 What it does:...

### [Auto-Backup n8n Workflows to OneDrive with Cleanup & Email Notifications](https://n8n.io/workflows/8451-auto-backup-n8n-workflows-to-onedrive-with-cleanup-and-email)
- **ID:** 8451 | **Creator:** @uuessel ✓ | **Views:** 264 | **Nodes:** 3
- **Nodes:** Microsoft OneDrive, Microsoft Outlook, Code
- Automatically BackUp Your n8n Workflows to OneDrive

This workflow automates the backup of your self-hosted n8n instance by exporting all workflows and saving them as individual .json files to a desig...

### [Automated Workflow Backup to Google Drive with Smart Cleanup](https://n8n.io/workflows/7512-automated-workflow-backup-to-google-drive-with-smart-cleanup)
- **ID:** 7512 | **Creator:** @lucaolovrap | **Views:** 19 | **Nodes:** 2
- **Nodes:** Google Drive, Code
- How it works

This workflow provides a complete, automated backup solution for your n8n instance, running on a daily schedule to ensure your automations are always safe.

Automatic cleanup:** It first...

### [Create Debug Breakpoints and Logs with Slack Interactive Messages](https://n8n.io/workflows/5490-create-debug-breakpoints-and-logs-with-slack-interactive-mes)
- **ID:** 5490 | **Creator:** @wyeth ✓ | **Views:** 15 | **Nodes:** 2
- **Nodes:** Slack, DebugHelper
- How it Works:
You can now use the Slack node to create conditional breakpoints! This example shows the loop stop on 4 (of 10) and then you can hit "continue" in Slack when you are ready. 

You could e...

### [Report spam and phishing URLs from IMAP mailboxes to Spamhaus](https://n8n.io/workflows/12846-report-spam-and-phishing-urls-from-imap-mailboxes-to-spamhau)
- **ID:** 12846 | **Creator:** @vquie ✓ | **Views:** 14 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- This workflow automates URL reporting to Spamhaus based on incoming spam/phishing sample emails. It watches one or more IMAP folders, extracts URLs from each email body, removes duplicates and common...

### [Send Slack Alerts for AWS IAM Access Keys Older Than 365 Days](https://n8n.io/workflows/7501-send-slack-alerts-for-aws-iam-access-keys-older-than-365-day)
- **ID:** 7501 | **Creator:** @trungtran ✓ | **Views:** 12 | **Nodes:** 3
- **Nodes:** HTTP Request, Slack, AWS IAM
- AWS IAM Access Key Rotation Reminder Automation Workflow
Watch the demo video below:

Who’s it for
DevOps/SRE teams responsible for AWS account security.  
Security/compliance officers ensuring key ro...

### [Monitor Jamf Policy Integrity and Send Slack Alerts for Changes](https://n8n.io/workflows/9287-monitor-jamf-policy-integrity-and-send-slack-alerts-for-chan)
- **ID:** 9287 | **Creator:** @mrrobot ✓ | **Views:** 7 | **Nodes:** 4
- **Nodes:** HTTP Request, Slack, Crypto +1 more
- 🛡️ Jamf Policy Integrity Monitor

🎯 Overview

A security-focused n8n workflow that monitors Jamf Pro policies for any unauthorized or accidental modification. It delivers configuration integrity and r...

### [Send real-time Kubernetes(EKS/GKE/AKS) CPU spike alerts from Prometheus to Slack](https://n8n.io/workflows/7145-send-real-time-kuberneteseks-gke-aks-cpu-spike-alerts-from-p)
- **ID:** 7145 | **Creator:** @johnpranay ✓ | **Views:** 4 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- 🧾 Summary
This workflow monitors Kubernetes pod CPU usage using Prometheus, and sends real-time Slack alerts when CPU consumption crosses a threshold (e.g., 0.8 cores). It groups pods by application n...

### [Analyze global supply chain sustainability and risk with GPT-4o and email alerts](https://n8n.io/workflows/12988-analyze-global-supply-chain-sustainability-and-risk-with-gpt)
- **ID:** 12988 | **Creator:** @cschin ✓ | **Views:** 3 | **Nodes:** 6
- **Nodes:** Send Email, HTTP Request, AI Agent +3 more
- How It Works
This workflow automates supply chain monitoring and risk management by deploying multiple specialized AI agents to analyze different supply chain dimensions simultaneously. Designed for s...

### [AI Privacy-Minded Router: PII Detection for Privacy, Security, & Compliance](https://n8n.io/workflows/5874-ai-privacy-minded-router-pii-detection-for-privacy-security)
- **ID:** 5874 | **Creator:** @codetender | **Views:** 2 | **Nodes:** 5
- **Nodes:** Code, AI Agent, Ollama Chat Model +2 more
- Modern AI systems are powerful but pose privacy risks when handling sensitive data. 

Organizations need AI capabilities while ensuring:

✅ Sensitive data never leaves secure environments
✅ Compliance...

### [Workflow Error Logging and Alerts with Google Sheets and Gmail](https://n8n.io/workflows/7876-workflow-error-logging-and-alerts-with-google-sheets-and-gma)
- **ID:** 7876 | **Creator:** @billy ✓ | **Views:** 2 | **Nodes:** 2
- **Nodes:** Google Sheets, Gmail
- What this workflow does

This workflow creates a comprehensive error monitoring system for your n8n instance by automatically capturing workflow failures, logging them to Google Sheets, and sending im...

### [Monitor TP-Link Omada Network Disconnections with Gmail & Pushover](https://n8n.io/workflows/7886-monitor-tp-link-omada-network-disconnections-with-gmail-and)
- **ID:** 7886 | **Creator:** @krade1027 | **Views:** 2 | **Nodes:** 3
- **Nodes:** Google Sheets, Pushover, Code
- Monitor device disconnections from Omada emails to Google Sheets with Pushover alerts

Who’s it for
This workflow is designed for IT admins, network engineers, or small business owners who need to aut...

### [Monitor n8n Workflow Errors with Telegram Alerts (Multi-language Setup)](https://n8n.io/workflows/5939-monitor-n8n-workflow-errors-with-telegram-alerts-multi-langu)
- **ID:** 5939 | **Creator:** @vadym-nahornyi ✓ | **Views:** 2 | **Nodes:** 1
- **Nodes:** Telegram
- How it works

Automatically sends Telegram notifications when any n8n workflow fails. Includes workflow name, error message, and execution ID in the alert.

Setup

Complete setup instructions included...

### [Monitor backup and sync logs with Google Cloud Storage, GitHub, Gmail, OpenAI, and GLPI](https://n8n.io/workflows/12880-monitor-backup-and-sync-logs-with-google-cloud-storage-githu)
- **ID:** 12880 | **Creator:** @paoloronco ✓ | **Views:** 2 | **Nodes:** 6
- **Nodes:** GitHub, HTTP Request, Gmail +3 more
- Reliable Backup & Sync Execution Validation (Log-Driven)

This workflow monitors filesystem sync and backup jobs by validating their execution logs, not by running or inspecting the jobs themselves....

### [Send severity-based error alerts using Telegram, email and Google Sheets](https://n8n.io/workflows/12890-send-severity-based-error-alerts-using-telegram-email-and-go)
- **ID:** 12890 | **Creator:** @abdallahh13 | **Views:** 2 | **Nodes:** 4
- **Nodes:** Google Sheets, Telegram, Gmail +1 more
- Who this template is for

This template is designed for n8n users running workflows in production
who need reliable and structured error monitoring, not just basic alerts.

It’s especially useful for:...

### [Automate Incident Response with Jira, Slack, Google Sheets & Drive](https://n8n.io/workflows/9826-automate-incident-response-with-jira-slack-google-sheets-and)
- **ID:** 9826 | **Creator:** @rahul08 ✓ | **Views:** 1 | **Nodes:** 5
- **Nodes:** Google Sheets, Slack, Google Drive +2 more
- 📘 Description:
This workflow automates the incident response lifecycle — from creation to communication and archival.
It instantly creates Jira tickets for new incidents, alerts the on-call Slack team...

### [Modify Liveblocks storage with JSON Patch and Anthropic Claude](https://n8n.io/workflows/14301-modify-liveblocks-storage-with-json-patch-and-anthropic-clau)
- **ID:** 14301 | **Creator:** @liveblocks ✓ | **Views:** 1 | **Nodes:** 3
- **Nodes:** AI Agent, Anthropic Chat Model, Structured Output Parser
- Modify Liveblocks Storage with JSON Patch

This example uses Liveblocks Storage, a sync engine created by Liveblocks that allows you to create collaborative applications like Figma, Pitch, and Spline....

### [Monitor cybersecurity compliance and send weekly reports via SIEM, Jira, PostgreSQL, Slack and email](https://n8n.io/workflows/10597-monitor-cybersecurity-compliance-and-send-weekly-reports-via)
- **ID:** 10597 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Send Email, HTTP Request, Postgres +1 more
- This n8n workflow automates continuous compliance monitoring across IT, OT, and cloud environments by aggregating security controls, validating policies (ISO 27001, NIST, GDPR, SOC2), detecting anomal...

### [Detect and route cybersecurity threats with SIEM, Slack, email and PagerDuty](https://n8n.io/workflows/10591-detect-and-route-cybersecurity-threats-with-siem-slack-email)
- **ID:** 10591 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 5
- **Nodes:** Send Email, HTTP Request, Postgres +2 more
- This n8n workflow proactively scans and aggregates threat intelligence, network logs, and vulnerability data every 15 minutes to detect emerging risks across the infrastructure. It analyzes anomalies,...

### [Automate cybersecurity threat analysis with GPT-4o, CVSS scoring and risk routing](https://n8n.io/workflows/14410-automate-cybersecurity-threat-analysis-with-gpt-4o-cvss-scor)
- **ID:** 14410 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** AI Agent, OpenAI Chat Model, Structured Output Parser +3 more
- How It Works
This workflow automates end-to-end cybersecurity threat analysis using a multi-agent AI architecture, targeting Security Operations Centre (SOC) analysts, security engineers, and IT risk...

### [Automate Incident Management with PagerDuty, Port AI, Jira & Slack](https://n8n.io/workflows/11610-automate-incident-management-with-pagerduty-port-ai-jira-and)
- **ID:** 11610 | **Creator:** @portio ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Slack, Jira Software, OpenAI
- Complete incident workflow from detection through resolution to post-mortem, with full organizational context from Port's catalog. This template handles both incident triggered and resolved events fro...

### [Monitor Zoho CRM Changes & Alert on Suspicious Activity with Google Sheets](https://n8n.io/workflows/11488-monitor-zoho-crm-changes-and-alert-on-suspicious-activity-wi)
- **ID:** 11488 | **Creator:** @weblineindia ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Google Sheets, HTTP Request, Gmail
- 📄 Zoho CRM Change Tracking & Automated Suspicious Activity Alerts Workflow

This n8n workflow automatically monitors selected Zoho CRM modules for record changes, identifies suspicious modification pa...

### [AI Qwen-Vl-Plus Powered Car Fleet Maintenance Alert System](https://n8n.io/workflows/10620-ai-qwen-vl-plus-powered-car-fleet-maintenance-alert-system)
- **ID:** 10620 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 5
- **Nodes:** Postgres, Slack, Code +2 more
- How It Works

Daily triggers automatically fetch fleet data and simulate key performance metrics for each vehicle. An AI agent analyzes maintenance requirements, detects potential issues, and routes a...

### [Monitor & Alert on Inactive AWS IAM Users with Slack Notifications](https://n8n.io/workflows/7500-monitor-and-alert-on-inactive-aws-iam-users-with-slack-notif)
- **ID:** 7500 | **Creator:** @trungtran ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** HTTP Request, Slack, AWS IAM
- AWS IAM Inactive User Automation Alert Workflow

&gt; Weekly job that finds IAM users with no activity for &gt; 90 days and notifies a Slack channel.  
&gt; ⚠️ Important: AWS SigV4 for IAM must be sco...

### [Orchestrate multi-agent compliance monitoring and audit logging with GPT-4o and Slack](https://n8n.io/workflows/15026-orchestrate-multi-agent-compliance-monitoring-and-audit-logg)
- **ID:** 15026 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 7
- **Nodes:** Send Email, AI Agent, OpenAI Chat Model +4 more
- How It Works
This workflow automates enterprise compliance governance using a multi-agent AI architecture. It targets compliance officers, legal teams, and risk managers who need continuous, jurisdict...

### [Log workflow errors to Slack and Google Sheets](https://n8n.io/workflows/13789-log-workflow-errors-to-slack-and-google-sheets)
- **ID:** 13789 | **Creator:** @pixcelsthemes ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** Google Sheets, Slack
- Who’s it for
This template is for teams using n8n in production who want immediate visibility into workflow failures. It’s ideal for DevOps teams, automation engineers, and operations teams who need r...

### [Log n8n workflow errors to your REST API with Slack alerts and metrics](https://n8n.io/workflows/13198-log-n8n-workflow-errors-to-your-rest-api-with-slack-alerts-a)
- **ID:** 13198 | **Creator:** @manu ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** HTTP Request, Slack, Code
- Track all n8n workflow failures with automatic error capture, severity classification, duplicate detection, Slack alerting, performance metrics, and log retention.

WHAT IT DOES:

Runs as an error sub...

### [Monitor Compliance with GPT-4 Analysis of System Logs and Generate Audit Reports](https://n8n.io/workflows/11775-monitor-compliance-with-gpt-4-analysis-of-system-logs-and-ge)
- **ID:** 11775 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** HTTP Request, Gmail, Code +3 more
- How It Works
This solution centralizes communication data from Slack, Microsoft Teams, Gmail, and GitHub into a unified AI-powered analysis and documentation workflow for teams managing distributed k...

### [Automated n8n Workflow Audit & Export Tool (JSON + Excel)](https://n8n.io/workflows/10852-automated-n8n-workflow-audit-and-export-tool-json-excel)
- **ID:** 10852 | **Creator:** @v3codestudio ✓ | **Views:** 0 | **Nodes:** 1
- **Nodes:** Code
- Automated n8n Workflow Audit & Export Tool (JSON + Excel)

Stop Auditing Workflows Manually — Automate Your n8n Reports.
This workflow delivers complete visibility across every automation in your n8n...

### [Monitor grid telemetry and automate compliance alerts with GPT-4o and Slack](https://n8n.io/workflows/13915-monitor-grid-telemetry-and-automate-compliance-alerts-with-g)
- **ID:** 13915 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 7
- **Nodes:** Send Email, AI Agent, OpenAI Chat Model +4 more
- How It Works
This workflow automates real-time energy grid telemetry ingestion, compliance validation, and multi-channel reporting for grid operators, energy managers, and compliance teams. Telemetry...

### [Centralized Error Monitoring & Alerts via Telegram, Slack & Other Messengers](https://n8n.io/workflows/5852-centralized-error-monitoring-and-alerts-via-telegram-slack-a)
- **ID:** 5852 | **Creator:** @boanse ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** Slack, Telegram, Discord +3 more
- Who is this for?
This workflow is designed for developers, DevOps engineers, and automation specialists who manage multiple n8n workflows and need a reliable way to monitor for failures and receive al...

### [Alert on Equipment Health Issues with Google Sheets and MS Teams Integration](https://n8n.io/workflows/6958-alert-on-equipment-health-issues-with-google-sheets-and-ms-t)
- **ID:** 6958 | **Creator:** @weblineindia ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** HTTP Request, Google Drive, Microsoft Teams
- ⚙️ Advanced Equipment Health Monitor with MS Teams Integration (n8n | API | Google Sheets | MSTeams)

This n8n workflow automatically monitors equipment health by fetching real-time metrics like tempe...

### [Automate ETL Error Monitoring with AI Classification, Sheets Logging & Jira Alerts](https://n8n.io/workflows/11039-automate-etl-error-monitoring-with-ai-classification-sheets)
- **ID:** 11039 | **Creator:** @weblineindia ✓ | **Views:** 0 | **Nodes:** 7
- **Nodes:** Google Sheets, Slack, Jira Software +4 more
- ETL Monitoring & Alert Automation: Jira & Slack Integration

This workflow automatically processes ETL errors, extracts important details, generates a preview, creates a log URL, classifies the issue...

### [Send deduplicated Kubernetes(EKS/GKE/AKS) error logs from Grafana Loki to Slack](https://n8n.io/workflows/7021-send-deduplicated-kuberneteseks-gke-aks-error-logs-from-graf)
- **ID:** 7021 | **Creator:** @johnpranay ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** HTTP Request, Code
- ✨ Summary 
Efficiently monitor Kubernetes environments by sending only unique error logs from Grafana Loki to Slack. Reduces alert fatigue while keeping your team informed about critical log events....

### [Detect AWS Orphaned Resources & Send Cost Reports to Slack, Email, and Sheets](https://n8n.io/workflows/11612-detect-aws-orphaned-resources-and-send-cost-reports-to-slack)
- **ID:** 11612 | **Creator:** @chadmcrowell | **Views:** 0 | **Nodes:** 5
- **Nodes:** Google Sheets, Slack, AWS Lambda +2 more
- How it works

This workflow automatically scans AWS accounts for orphaned resources (unattached EBS volumes, old snapshots &gt;90 days, unassociated Elastic IPs) that waste money. It calculates cost i...

### [IAM Compliance Automation: Enforce MFA and Clean Up Access Keys in AWS](https://n8n.io/workflows/7598-iam-compliance-automation-enforce-mfa-and-clean-up-access-ke)
- **ID:** 7598 | **Creator:** @trungtran ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** HTTP Request, Slack, Code +1 more
- Automated AWS IAM Compliance Workflow for MFA Enforcement and Access Key Deactivation
&gt; This workflow leverages AWS IAM APIs and n8n automation to ensure strict security compliance by continuously...

### [Auto-Renew AWS Certificates with Slack Approval Workflow](https://n8n.io/workflows/7490-auto-renew-aws-certificates-with-slack-approval-workflow)
- **ID:** 7490 | **Creator:** @trungtran ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** Slack, AWS Certificate Manager
- AWS Certificate Manager (ACM) Auto-Renew with Slack notify & approval

Who’s it for
SRE/DevOps teams managing many ACM certs.
Cloud ops who want hands-off renewals with an approval step in Slack.
MSPs...

### [AWS Azure GCP Multi-Cloud Cost Monitoring & Alerts for Budget Control](https://n8n.io/workflows/7374-aws-azure-gcp-multi-cloud-cost-monitoring-and-alerts-for-bud)
- **ID:** 7374 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 5
- **Nodes:** Send Email, HTTP Request, Slack +2 more
- This automated n8n workflow tracks hourly cloud spending across AWS, Azure, and GCP. It detects cost spikes or budget overruns in real time, tags affected resources, and sends alerts via email, WhatsA...

### [Launch AWS EC2 Instances from Google Sheets using Terraform](https://n8n.io/workflows/7295-launch-aws-ec2-instances-from-google-sheets-using-terraform)
- **ID:** 7295 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** Google Sheets, Gmail
- This automated n8n workflow enables launching AWS EC2 instances directly from a Google Sheets document. Users can specify instance details (e.g., region, instance type, key pair) in a Google Sheet, tr...

### [Create & Delete AWS RDS Databases via Email Commands with Terraform](https://n8n.io/workflows/7294-create-and-delete-aws-rds-databases-via-email-commands-with)
- **ID:** 7294 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Google Sheets, Gmail, Code
- This automated n8n workflow enables the creation and management of AWS RDS databases through email interactions. Users can send emails with commands such as "Create RDS" or "Delete RDS," including det...

### [Monitor website uptime and diagnose errors with Gemini and Slack alerts](https://n8n.io/workflows/13672-monitor-website-uptime-and-diagnose-errors-with-gemini-and-s)
- **ID:** 13672 | **Creator:** @okp29 ✓ | **Views:** 0 | **Nodes:** 7
- **Nodes:** Google Sheets, HTTP Request, Slack +4 more
- Who is this for

DevOps engineers, site reliability teams, and business owners who need to know the moment their website goes down — and want AI-powered diagnostics instead of just a ping alert.

What...

### [Monitor scheduled workflow health in n8n with automatic trigger checks](https://n8n.io/workflows/13290-monitor-scheduled-workflow-health-in-n8n-with-automatic-trig)
- **ID:** 13290 | **Creator:** @jksr ✓ | **Views:** 0 | **Nodes:** 1
- **Nodes:** Code
- Automatically detect when your scheduled or polling-trigger workflows stop running. Unlike error handlers that catch failures when workflows execute, this catches the silent killer: workflows that sim...

### [Automated Telegram UserBot Session Monitoring & Recovery with TelePilot](https://n8n.io/workflows/5872-automated-telegram-userbot-session-monitoring-and-recovery-w)
- **ID:** 5872 | **Creator:** @ivancore | **Views:** 0 | **Nodes:** 1
- **Nodes:** Telegram
- Disclaimer: This workflow contains community nodes that are only compatible with the self-hosted version of n8n.

Important distinction: This template manages Telegram Copilot's UserBots (client acco...

### [Error Workflow: AI Powered (GPT 4.1): Universal](https://n8n.io/workflows/10066-error-workflow-ai-powered-gpt-41-universal)
- **ID:** 10066 | **Creator:** @sandy4v ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Telegram, Gmail, AI Agent +1 more
- AI-Powered n8n Error Debugger & Notifier
Automatically analyze any workflow failure with AI, get actionable solutions, and receive a detailed report directly in your inbox.

Stop wasting time decipher...

### [Score telematics driving risk with Claude and adjust insurance premiums via HTTP, Gmail, and Slack](https://n8n.io/workflows/12279-score-telematics-driving-risk-with-claude-and-adjust-insuran)
- **ID:** 12279 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** HTTP Request, Slack, Gmail +3 more
- How It Works
This workflow automates insurance premium adjustments by analyzing telematics data with AI-driven risk assessment and syncing changes across underwriting systems. Designed for carriers, a...

### [Route revenue transactions and assess AI outputs with Anthropic Claude and OpenAI](https://n8n.io/workflows/13341-route-revenue-transactions-and-assess-ai-outputs-with-anthro)
- **ID:** 13341 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** Code, AI Agent, Anthropic Chat Model +3 more
- How It Works
This workflow automates intelligent routing of user queries to optimal AI models (Anthropic, OpenAI) based on complexity analysis, then validates outputs through multi-stage quality asses...

### [Monitor Domains & IPs on AbuseIPDB Blacklist with Slack Alerts](https://n8n.io/workflows/6836-monitor-domains-and-ips-on-abuseipdb-blacklist-with-slack-al)
- **ID:** 6836 | **Creator:** @marth ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** HTTP Request, Slack, Code
- ⚙ How It Works 

The automated blacklist monitor is designed to be a proactive, not reactive, tool. Here is the high-level process:

Scheduled Checks: At regular intervals (e.g., every 30 minutes or e...

### [AWS Lambda Manager with GPT-4.1 & Google Sheets Audit Logging via Chat](https://n8n.io/workflows/8623-aws-lambda-manager-with-gpt-41-and-google-sheets-audit-loggi)
- **ID:** 8623 | **Creator:** @trungtran ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** AI Agent, OpenAI Chat Model, Simple Memory
- Chat-Based AWS Lambda Manager with Automated Audit Logging (GPT-4.1 mini + Google Sheet)
&gt; This workflow provides a chat-based AI agent to manage AWS Lambda functions. It allows users to list, invo...

### [Monitor & Auto-Heal AWS EC2 Instances with Multi-Channel Alerts](https://n8n.io/workflows/10348-monitor-and-auto-heal-aws-ec2-instances-with-multi-channel-a)
- **ID:** 10348 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Send Email, Google Sheets, HTTP Request +1 more
- This n8n workflow automates the monitoring, health assessment, and self-healing of AWS EC2 instances in production environments. It runs periodic checks, identifies unhealthy instances based on status...

### [Automate Workflow & Credentials Backup to S3 with Retention Management](https://n8n.io/workflows/6436-automate-workflow-and-credentials-backup-to-s3-with-retentio)
- **ID:** 6436 | **Creator:** @tobim | **Views:** 0 | **Nodes:** 1
- **Nodes:** S3
- This n8n template automates daily backups of workflows and credentials to S3-compatible storage with automatic retention management. Designed for self-hosted n8n instances requiring disaster recovery...

### [Route AI tasks between Anthropic Claude models with Postgres policies and SLA](https://n8n.io/workflows/14039-route-ai-tasks-between-anthropic-claude-models-with-postgres)
- **ID:** 14039 | **Creator:** @rnair1996 ✓ | **Views:** 0 | **Nodes:** 5
- **Nodes:** Postgres, Code, AI Agent +2 more
- Overview

This workflow implements a policy-driven LLM orchestration system that dynamically routes AI tasks to different language models based on task complexity, policies, and performance constraint...

### [Track and Monitor AI Token Usage Metrics for OpenAI and Gemini Models](https://n8n.io/workflows/7265-track-and-monitor-ai-token-usage-metrics-for-openai-and-gemi)
- **ID:** 7265 | **Creator:** @elimeleth | **Views:** 0 | **Nodes:** 5
- **Nodes:** Code, AI Agent, OpenAI Chat Model +2 more
- 📊 Token Usage Metrics Workflow

Descripción:
Este flujo de trabajo en n8n extrae y resume las métricas de uso de tokens (prompt, completion y total) y los modelos utilizados en una ejecución específic...

### [Track OpenAI Token Usage and AI Agent Metrics with Google Sheets Dashboard](https://n8n.io/workflows/7231-track-openai-token-usage-and-ai-agent-metrics-with-google-sh)
- **ID:** 7231 | **Creator:** @hun-yao ✓ | **Views:** 0 | **Nodes:** 3
- **Nodes:** Google Sheets, AI Agent, LangChain Code
- What it does
Captures token usage and cost from your AI Agent/LLM. Logs model, tokens, cost, tool use, and conversation I/O to Google Sheets for simple observability and billing.

Perfect for
Develope...

### [Evaluate supply chain risk and orchestrate contingencies with Claude, Google Sheets, Gmail and Slack](https://n8n.io/workflows/13316-evaluate-supply-chain-risk-and-orchestrate-contingencies-wit)
- **ID:** 13316 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 7
- **Nodes:** Google Sheets, Slack, Code +4 more
- How It Works
This workflow automates enterprise risk management by intelligently routing risks across three severity tiers. Built for compliance teams and risk managers, it eliminates manual evaluatio...

### [Automate Gradle Dependency Updates with Slack Notifications](https://n8n.io/workflows/8516-automate-gradle-dependency-updates-with-slack-notifications)
- **ID:** 8516 | **Creator:** @weblineindia ✓ | **Views:** 0 | **Nodes:** 2
- **Nodes:** Slack, Code
- Gradle Project Dependency & Version Update - Smart Tracker

This workflow automatically checks your project’s libraries for updates. It identifies outdated dependencies, flags major version changes, a...

### [Detect transaction fraud and manage compliance with GPT-4 and Airtable](https://n8n.io/workflows/13598-detect-transaction-fraud-and-manage-compliance-with-gpt-4-an)
- **ID:** 13598 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 5
- **Nodes:** Airtable, AI Agent, OpenAI Chat Model +2 more
- How It Works
This workflow automates financial transaction monitoring, fraud detection, and regulatory compliance using OpenAI GPT-4 across coordinated specialist agents. It targets compliance officer...

### [Analyze mobile app build-time hotspots with Gradle, CocoaPods, Airtable, GitHub, Gmail and GPT-4.1-mini](https://n8n.io/workflows/12368-analyze-mobile-app-build-time-hotspots-with-gradle-cocoapods)
- **ID:** 12368 | **Creator:** @weblineindia ✓ | **Views:** 0 | **Nodes:** 7
- **Nodes:** Airtable, GitHub, Gmail +4 more
- Mobile App Build Time Hotspot Tracker - Gradle/CocoaPods Analyzer Alerting

This workflow automates the monitoring and analysis of CI/CD build performance for mobile projects using Gradle and CocoaPod...

### [Monitor IoT sustainability compliance and ESG reports with OpenAI, Airtable, Slack and Gmail](https://n8n.io/workflows/12198-monitor-iot-sustainability-compliance-and-esg-reports-with-o)
- **ID:** 12198 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 7
- **Nodes:** Airtable, Slack, Gmail +4 more
- How It Works

This workflow automates IoT device compliance monitoring and anomaly detection for industrial operations. Designed for facility managers, quality assurance teams, and regulatory complian...

### [Filter Cybersecurity News for Your Tech Stack (OpenAI + Pinecone RAG)](https://n8n.io/workflows/7017-filter-cybersecurity-news-for-your-tech-stack-openai-pineco)
- **ID:** 7017 | **Creator:** @will-carlson | **Views:** 0 | **Nodes:** 8
- **Nodes:** Gmail, Code, AI Agent +5 more
- What it does:
Collects cybersecurity news from trusted RSS feeds and uses OpenAI’s Retrieval-Augmented Generation (RAG) capabilities with Pinecone to filter for content that is directly relevant to yo...

### [Orchestrate sustainability lifecycle analytics with GPT-4o, Slack, Gmail and Google Docs](https://n8n.io/workflows/14433-orchestrate-sustainability-lifecycle-analytics-with-gpt-4o-s)
- **ID:** 14433 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 9
- **Nodes:** HTTP Request, Slack, Gmail +6 more
- How It Works
This workflow automates end-to-end sustainability lifecycle management for corporate sustainability teams, ESG governance officers, and circular economy programme leads. It addresses the...

### [Real-time Error Monitoring with WhatsApp Alerts & Multi-language Setup](https://n8n.io/workflows/6327-real-time-error-monitoring-with-whatsapp-alerts-and-multi-la)
- **ID:** 6327 | **Creator:** @vadym-nahornyi ✓ | **Views:** 0 | **Nodes:** 1
- **Nodes:** WhatsApp Business Cloud
- &gt; ⚠️ Multi-language WhatsApp Error Notifier  

Get instant WhatsApp alerts when any workflow fails — perfect for mobile-first monitoring and fast incident response.

✅ No coding required  
✅ Works...

### [Automated Workflow Backups with Google Drive and Slack Notifications](https://n8n.io/workflows/7850-automated-workflow-backups-with-google-drive-and-slack-notif)
- **ID:** 7850 | **Creator:** @omerfayyaz ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Slack, Google Drive, Compression +1 more
- Efficient loop-less N8N Workflow Backup Automation to Google Drive


This workflow eliminates traditional loop-based processing entirely, delivering unprecedented performance and reliability even when...

### [Monitor asset health and predict maintenance with Anthropic Claude and Slack](https://n8n.io/workflows/13595-monitor-asset-health-and-predict-maintenance-with-anthropic)
- **ID:** 13595 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 8
- **Nodes:** Send Email, Slack, Code +5 more
- How It Works
This workflow automates industrial asset health monitoring and predictive maintenance using Anthropic Claude across coordinated specialist agents. It targets facility managers, maintenanc...

### [Automate inventory replenishment and purchase orders with Mistral AI and ERP](https://n8n.io/workflows/10535-automate-inventory-replenishment-and-purchase-orders-with-mi)
- **ID:** 10535 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 7
- **Nodes:** Send Email, Postgres, Slack +4 more
- This AI-powered workflow monitors warehouse stock levels and sales velocity in real-time, uses machine learning to forecast demand, automatically generates optimized purchase orders with intelligent q...

### [Generate daily multi-cloud FinOps cost and carbon reports with OpenAI GPT-4o](https://n8n.io/workflows/14003-generate-daily-multi-cloud-finops-cost-and-carbon-reports-wi)
- **ID:** 14003 | **Creator:** @cschin ✓ | **Views:** 0 | **Nodes:** 7
- **Nodes:** HTTP Request, AI Agent, OpenAI Chat Model +4 more
- How It Works
This workflow automates multi-cloud billing analysis and FinOps reporting using a supervised multi-agent AI architecture. It targets cloud finance teams, FinOps practitioners, DevOps lea...

### [Monitor n8n workflows with Watchflow dead man’s switch and error alerts](https://n8n.io/workflows/14988-monitor-n8n-workflows-with-watchflow-dead-mans-switch-and-er)
- **ID:** 14988 | **Creator:** @customjs ✓ | **Views:** 0 | **Nodes:** 0
- **Nodes:** 
- 🚀 Your n8n Workflows Monitoring Best Practices Template

Are you running critical processes in n8n and relying on hope that they finish successfully? Stop guessing and start monitoring. 

This templa...

## SecOps
(15 workflows)

### [Analyze Suspicious Email Contents with ChatGPT Vision](https://n8n.io/workflows/2665-analyze-suspicious-email-contents-with-chatgpt-vision)
- **ID:** 2665 | **Creator:** @djangelic ✓ | **Views:** 3,704 | **Nodes:** 4
- **Nodes:** HTTP Request, Jira Software, Code +1 more
- Phishing Email Detection and Reporting with n8n

Who is this for?
This workflow is designed for IT teams, security professionals, and managed service providers (MSPs) looking to automate the process o...

### [Audit Google Drive File Permissions for Access Control Management](https://n8n.io/workflows/3549-audit-google-drive-file-permissions-for-access-control-manag)
- **ID:** 3549 | **Creator:** @jimleuk ✓ | **Views:** 1,857 | **Nodes:** 3
- **Nodes:** Google Sheets, Google Drive, Gmail
- This n8n template reviews and audits recently active Google Drive files and reports on files with excessively open permissions. This shows how you can automate simple compliance tasks for access contr...

### [Monitor SSL Certificate Expiry with Google Sheets and Multi-Channel Alert](https://n8n.io/workflows/3493-monitor-ssl-certificate-expiry-with-google-sheets-and-multi)
- **ID:** 3493 | **Creator:** @cultrix | **Views:** 1,791 | **Nodes:** 4
- **Nodes:** Google Sheets, HTTP Request, Telegram +1 more
- SSL Expiry Alert System

Who is this for?
This workflow is ideal for administrators or IT professionals responsible for monitoring SSL certificates of multiple websites to ensure they do not expire un...

### [Monitor Authentication IPs from SaaS Alerts & Email Reports via SMTP2Go](https://n8n.io/workflows/3126-monitor-authentication-ips-from-saas-alerts-and-email-report)
- **ID:** 3126 | **Creator:** @benjones-saasalerts | **Views:** 880 | **Nodes:** 1
- **Nodes:** HTTP Request
- Collect and Email Authentication IP Addresses from SaaS Alerts (Last 24 Hours)

Description  
This n8n workflow automates the process of collecting sign-in IP addresses from SaaS Alerts over the past...

### [CYBERPULSE AI GRC: Automate PCI DSS Control Evaluation and Compliance Tracking ](https://n8n.io/workflows/7077-cyberpulse-ai-grc-automate-pci-dss-control-evaluation-and-co)
- **ID:** 7077 | **Creator:** @adnantariq ✓ | **Views:** 32 | **Nodes:** 2
- **Nodes:** Google Sheets, Code
- Description

Automatically evaluates PCI DSS control responses using logic or AI. Designed to speed up compliance workflows, reduce audit fatigue, and flag non-compliance early.

Who’s It For:

Intern...

### [CYBERPULSE AI GRC: Automate Security Questionnaire Responses](https://n8n.io/workflows/7349-cyberpulse-ai-grc-automate-security-questionnaire-responses)
- **ID:** 7349 | **Creator:** @adnantariq ✓ | **Views:** 16 | **Nodes:** 5
- **Nodes:** Google Sheets, Google Drive, Gmail +2 more
- Description

Automates vendor/customer security questionnaire responses. It ingests a questionnaire (Sheet/CSV/XLSX), matches each question to your approved answers and evidence, and writes a clean “...

### [Create Executive Security Briefings with NixGuard AI & Wazuh Alerts](https://n8n.io/workflows/5895-create-executive-security-briefings-with-nixguard-ai-and-waz)
- **ID:** 5895 | **Creator:** @nex ✓ | **Views:** 6 | **Nodes:** 2
- **Nodes:** Send Email, Code
- Drowning in security alerts? Spending hours translating technical logs from Wazuh, your SIEM, or other tools into business-friendly reports for leadership? This n8n workflow is your automated Security...

### [Automated URL Phishing & Threat Analysis with NixGuard AI](https://n8n.io/workflows/5937-automated-url-phishing-and-threat-analysis-with-nixguard-ai)
- **ID:** 5937 | **Creator:** @nex ✓ | **Views:** 3 | **Nodes:** 1
- **Nodes:** Slack
- Stop manually checking suspicious links. This free n8n workflow provides the foundation for a powerful, automated URL analysis pipeline. Using the NixGuard AI engine, you can instantly analyze suspici...

### [Automate Free IP Analysis: NixGuard AI Summaries & Wazuh Integration](https://n8n.io/workflows/5928-automate-free-ip-analysis-nixguard-ai-summaries-and-wazuh-in)
- **ID:** 5928 | **Creator:** @nex ✓ | **Views:** 2 | **Nodes:** 1
- **Nodes:** Slack
- Supercharge Your Security Operations for Free

Stop wasting time manually investigating suspicious IP addresses. This workflow template is your launchpad to automating real-time IP cybersecurity analy...

### [Automate AI Vulnerability Monitoring with GPT-4 and ServiceNow Incident Creation](https://n8n.io/workflows/7225-automate-ai-vulnerability-monitoring-with-gpt-4-and-servicen)
- **ID:** 7225 | **Creator:** @yajna ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** ServiceNow, OpenAI Chat Model, Information Extractor +1 more
- This n8n workflow automatically monitors RSS feeds for the latest AI vulnerability news, extracts key threat details, and creates a corresponding Security Incident in ServiceNow for each item.

Schedu...

### [Detect and isolate ransomware with Claude (Anthropic), EDR, SIEM and Slack](https://n8n.io/workflows/13706-detect-and-isolate-ransomware-with-claude-anthropic-edr-siem)
- **ID:** 13706 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 7
- **Nodes:** Send Email, Google Sheets, HTTP Request +4 more
- This workflow provides real-time detection of ransomware encryption patterns using Claude AI, with automated system isolation and incident response.

How it works

File System Monitoring - Continuousl...

### [Automate cybersecurity incident response with Claude AI, VirusTotal and Slack](https://n8n.io/workflows/10587-automate-cybersecurity-incident-response-with-claude-ai-viru)
- **ID:** 10587 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 5
- **Nodes:** Google Sheets, HTTP Request, Code +2 more
- This workflow automates end-to-end cybersecurity incident response by ingesting alerts from multiple sources, enriching threat intelligence, assessing severity with Claude AI, executing containment ac...

### [Prevent phishing emails with GPT-4, VirusTotal, Slack, and Google Sheets](https://n8n.io/workflows/10595-prevent-phishing-emails-with-gpt-4-virustotal-slack-and-goog)
- **ID:** 10595 | **Creator:** @oneclick-ai ✓ | **Views:** 0 | **Nodes:** 6
- **Nodes:** Send Email, Google Sheets, HTTP Request +3 more
- This n8n workflow automates real-time phishing detection by ingesting incoming emails, extracting indicators, analyzing content with AI (GPT-4), calculating risk scores, and taking immediate action—qu...

### [Auto Remediate Endpoint Infections with Wazuh, ClamAV, and GPT-4](https://n8n.io/workflows/7022-auto-remediate-endpoint-infections-with-wazuh-clamav-and-gpt)
- **ID:** 7022 | **Creator:** @mariskarthick ✓ | **Views:** 0 | **Nodes:** 4
- **Nodes:** Telegram, AI Agent, Summarization Chain +1 more
- Reduce human delays between malware detection and remediation in MSSP/SOC environments. This workflow automates full endpoint antivirus scanning immediately after high-severity endpoint infection wazu...

### [Automate Risk Treatment Tasks with Google Sheets for GRC Compliance](https://n8n.io/workflows/7858-automate-risk-treatment-tasks-with-google-sheets-for-grc-com)
- **ID:** 7858 | **Creator:** @adnantariq ✓ | **Views:** 0 | **Nodes:** 1
- **Nodes:** Google Sheets
- Description

Automatically assigns and escalates risk treatment tasks based on severity, organizational unit, and asset class.
Removes manual owner-assignment steps, ensures consistent routing, speeds...

## Other
(3 workflows)

### [Execute a command that gives the hard disk memory used on the host machine](https://n8n.io/workflows/716-execute-a-command-that-gives-the-hard-disk-memory-used-on-th)
- **ID:** 716 | **Creator:** @harshil1712 ✓ | **Views:** 1,747 | **Nodes:** 1
- **Nodes:** Twilio

### [Sample error workflow](https://n8n.io/workflows/359-sample-error-workflow)
- **ID:** 359 | **Creator:** @tanay1337 ✓ | **Views:** 1,422 | **Nodes:** 2
- **Nodes:** Twilio, Mattermost
- A sample error workflow which when triggered sends a notification to the specified Mattermost channel as well as an SMS to the specified mobile number.

### [Send an SMS when a workflow fails](https://n8n.io/workflows/665-send-an-sms-when-a-workflow-fails)
- **ID:** 665 | **Creator:** @harshil1712 ✓ | **Views:** 1,367 | **Nodes:** 1
- **Nodes:** Twilio

## Top Verified Creators

| Creator | Workflows | Total Views |
|---|---|---|
| @jon-n8n (Jonathan) | 6 | 692,488 |
| @eduard (Eduard) | 5 | 235,352 |
| @lucaspeyrin (Lucas Peyrin) | 13 | 142,630 |
| @n8n-team (n8n Team) | 16 | 121,857 |
| @jimleuk (Jimleuk) | 17 | 104,471 |
| @mcolomer (Miquel Colomer) | 4 | 85,527 |
| @mihailtd (Mihai Farcas) | 1 | 77,672 |
| @harshil1712 (Harshil Agrawal) | 30 | 57,009 |
| @solomon (Solomon) | 3 | 52,243 |
| @joe (Joseph LePage) | 2 | 48,456 |
| @djangelic (Angel Menendez) | 12 | 42,288 |
| @yulia (Yulia) | 2 | 39,073 |
| @mrscoopers (Jenny ) | 3 | 37,201 |
| @amjid (Amjid Ali) | 1 | 32,346 |
| @sm-amudhan (amudhan) | 9 | 26,307 |
| @polina-n8n (Polina Medvedieva) | 1 | 23,830 |
| @n3witalia (Davide Boizza) | 5 | 21,461 |
| @jan (Jan Oberhauser) | 3 | 20,029 |
| @agentstudio (Agent Studio) | 2 | 19,115 |
| @vishalquantana (Vishal Kumar) | 2 | 18,513 |
| @scrapeninja (Anthony) | 1 | 17,135 |
| @lowcodingdev (Mark Shcherbakov) | 1 | 16,571 |
| @hostinger (Hostinger) | 2 | 13,494 |
| @davidn8n (David Roberts) | 3 | 13,261 |
| @tanay1337 (tanaypant) | 9 | 12,954 |
