# {{SERVICE_NAME}}

Backend service built using the **FastAPI Service Template**.

---

## Architecture

This service follows **clean layered architecture**:

- `api/` — HTTP endpoints, request/response schemas, validation
- `business/` — use-cases and domain rules
- `data/` — database models, repositories, unit of work
- `core/` — configuration, logging, errors, middleware

### Rules

- API layer must not access the database directly
- Business layer must not import SQLAlchemy models
- All database writes must go through Unit of Work

---

## Local Development

### Requirements

- Python 3.12
- Docker (for infrastructure)
- uv

### Setup

```bash
cp .env.example .env
make venv
source .venv/bin/activate
make install
make migrate
make dev
````

Service runs at:

```
http://127.0.0.1:8000
```

Health check:

```
GET /api/v1/health
```

---

## Adding a New Feature

Follow this order strictly:

1. Define repository interface in `business/repositories.py`
2. Implement repository in `data/repositories_sql/`
3. Create use-case in `business/usecases/`
4. Call use-case from API endpoint in `api/`

---

## Database Migrations

Create migration:

```bash
make revision m="add something"
```

Apply migration:

```bash
make migrate
```

---

## Tests

```bash
make test
```

---

## Common Mistakes

* Business logic in API routes
* Direct database access in API
* Forgetting to commit Unit of Work
* Returning raw exceptions

---

## Philosophy

This service is designed to be:

* Boring
* Explicit
* Predictable

Correctness is more important than cleverness.