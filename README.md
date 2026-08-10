# Cat Cafe Backend

FastAPI is the single source of truth for accounts, teas, availability, reservations, and external identity links. The Fresh and Slack clients only call this API.

## Run locally

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then run:

```bash
cp .env.example .env
docker compose up -d db
uv sync --extra dev
uv run uvicorn app.main:app --reload --port 8444
```

Open `http://localhost:8444/docs`. The starter uses an in-memory service so it runs before PostgreSQL models are wired to repositories; `app/models/` and Alembic establish the production persistence boundary.

## Development checks

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

## API

- `POST /api/v1/auth/register`
- `GET /api/v1/teas`
- `GET /api/v1/availability?date=YYYY-MM-DD`
- CRUD under `/api/v1/reservations`
- Slack linking under `/api/v1/integrations/slack/users`
