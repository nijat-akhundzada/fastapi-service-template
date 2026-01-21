SHELL := /bin/bash

.PHONY: help install dev test lint fmt check up down revision migrate downgrade

help:
	@echo "Targets:"
	@echo "  install     	- install deps (dev)"
	@echo "  install-prod	- install deps (prod, frozen)"
	@echo "  dev         	- run fastapi in reload mode"
	@echo "  test        	- run tests"
	@echo "  lint        	- ruff check"
	@echo "  fix         	- ruff check and fix"
	@echo "  fmt         	- ruff format"
	@echo "  check       	- lint + test"
	@echo "  up          	- run docker-compose up"
	@echo "  down        	- run docker-compose down"
	@echo "  revision m= 	- create alembic revision"
	@echo "  migrate     	- alembic upgrade head"
	@echo "  downgrade   	- alembic downgrade -1"

install:
	uv sync --group dev

install-prod:
	uv sync --no-dev --frozen

dev:
	uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

test:
	uv run pytest -v

lint:
	uv run ruff check .

fix:
	uv run ruff check . --fix

fmt:
	uv run ruff format .

check: lint test

up:
	docker compose up --build -d

down:
	docker compose down

revision:
	@if [ -z "$(m)" ]; then echo "Usage: make revision m=\"message\""; exit 1; fi
	uv run alembic revision -m "$(m)" --autogenerate

migrate:
	uv run alembic upgrade head

downgrade:
	uv run alembic downgrade -1
