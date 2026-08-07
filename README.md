# Cat Cafe Backend

FastAPI is the single source of truth for accounts, teas, availability, reservations, and external identity links. The Fresh and Slack clients only call this API.

## Run locally

```bash
cp .env.example .env
docker compose up -d db
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
uvicorn app.main:app --reload --port 8080
```

Open `http://localhost:8080/docs`. The starter uses an in-memory service so it runs before PostgreSQL models are wired to repositories; `app/models/` and Alembic establish the production persistence boundary.

## API

- `POST /api/v1/auth/register`
- `GET /api/v1/teas`
- `GET /api/v1/availability?date=YYYY-MM-DD`
- CRUD under `/api/v1/reservations`
- Slack linking under `/api/v1/integrations/slack/users`

