SHELL := /bin/bash

.PHONY: help venv install dev test lint fmt revision migrate downgrade

help:
	@echo "Targets:"
	@echo "  venv        - create .venv"
	@echo "  install     - install deps (dev)"
	@echo "  dev         - run fastapi in reload mode"
	@echo "  test        - run tests"
	@echo "  lint        - ruff check"
	@echo "  fix         - ruff check and fix"
	@echo "  fmt         - ruff format"
	@echo "  revision m= - create alembic revision"
	@echo "  migrate     - alembic upgrade head"
	@echo "  downgrade   - alembic downgrade -1"

venv:
	uv venv

install:
	uv sync --no-dev

dev:
	uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

test:
	uv run pytest -q

lint:
	uv run ruff check .

fix:
	uv run ruff check . --fix

fmt:
	uv run ruff format .

revision:
	@if [ -z "$(m)" ]; then echo "Usage: make revision m=\"message\""; exit 1; fi
	uv run alembic revision -m "$(m)" --autogenerate

migrate:
	uv run alembic upgrade head

downgrade:
	uv run alembic downgrade -1
