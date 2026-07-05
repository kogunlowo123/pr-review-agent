# Pull Request Review Agent

[![CI](https://github.com/kogunlowo123/pr-review-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/pr-review-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Software Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Automated pull request reviewer that performs deep code analysis including security vulnerability detection, performance anti-pattern identification, test coverage gaps, style violations, and architectural conformance checks with inline review comments.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `analyze_diff` | Analyze a PR diff for issues, risks, and improvements |
| `check_security` | Scan diff for security vulnerabilities (OWASP Top 10, CWE) |
| `check_performance` | Identify performance anti-patterns in changed code |
| `check_test_coverage` | Verify test coverage for changed code paths |
| `post_review_comment` | Post an inline review comment on a PR |
| `approve_or_request_changes` | Submit final review verdict |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/review` | Submit a PR for automated review |
| `GET` | `/api/v1/review/{pr_id}` | Get review results for a PR |
| `GET` | `/api/v1/review/{pr_id}/comments` | List review comments |
| `POST` | `/api/v1/security-scan` | Run security-focused scan on diff |
| `POST` | `/api/v1/webhooks/github` | GitHub webhook for PR events |
| `POST` | `/api/v1/webhooks/gitlab` | GitLab webhook for MR events |

## Features

- Diff Analysis
- Security Scanning
- Performance Review
- Style Enforcement
- Coverage Analysis
- Inline Comments

## Integrations

- Github Connector
- Gitlab Connector
- Sonarqube
- Snyk

## Architecture

```
pr-review-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── pr_review_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 6 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 6 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 4 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**GitHub/GitLab API + LLM**

---

Built as part of the Enterprise AI Agent Platform.
