# FastAPI Service Template

![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-009688)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-red)
![uv](https://img.shields.io/badge/uv-package_manager-blueviolet)
![Ruff](https://img.shields.io/badge/code_style-ruff-black)
![License](https://img.shields.io/badge/license-MIT-green)
[![CI](https://github.com/nijat-akhundzada/fastapi-service-template/actions/workflows/ci.yml/badge.svg)](https://github.com/nijat-akhundzada/fastapi-service-template/actions/workflows/ci.yml)



A production-ready, opinionated **Python backend service template** built with
FastAPI, async SQLAlchemy, clean architecture, and Unit of Work pattern.

Designed for long-lived, maintainable systems and team collaboration.

---

## Architecture

This service follows **clean layered architecture**:

- `api/` — HTTP endpoints, request/response schemas, validation
- `business/` — use-cases and domain rules (business logic)
- `data/` — database models, repositories, unit of work
- `core/` — configuration, logging, errors, middleware

### Architectural Rules

- API layer must **not** access the database directly
- Business layer must **not** import SQLAlchemy models
- All database writes must go through **Unit of Work**
- Database sessions must never be used in API routes

These rules are enforced to keep the codebase maintainable and safe to refactor.

---

## Tooling

This template uses modern Python tooling:

- **uv** — fast dependency management and virtual environments
- **Ruff** — fast linting and formatting

These tools are recommended but can be replaced if needed.

---


## Local Development

### Requirements

- Python **3.12**
- Docker (for infrastructure such as Postgres, RabbitMQ, etc.)
- `uv` package manager

---

### Setup

```bash
cp .env.example .env
make install
make migrate
make dev
```

Service runs at:

```
http://127.0.0.1:8000
```

Health check endpoint:

```
GET /api/v1/health
```

---

## Adding a New Feature

Always follow this order:

1. Define a repository interface in `business/repositories.py`
2. Implement the repository in `data/repositories_sql/`
3. Create a use-case in `business/usecases/`
4. Call the use-case from an API endpoint in `api/`

Do **not** skip steps.
Do **not** put business logic in API routes.

---

## Database Migrations

Create a migration:

```bash
make revision m="add something"
```

Apply migrations:

```bash
make migrate
```

---

## Tests

Run all tests:

```bash
make test
```

---

## Common Mistakes

* Putting business logic in API routes
* Accessing the database directly from API layer
* Forgetting to commit inside Unit of Work
* Returning raw exceptions instead of structured errors

---

## Philosophy

This template is intentionally designed to be:

* **Boring**
* **Explicit**
* **Predictable**

Correctness, clarity, and maintainability are more important than cleverness.