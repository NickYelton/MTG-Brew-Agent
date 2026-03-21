# MTG Brew Assistant

A Commander deck-building tool that generates opinionated, strategy-driven card recommendations powered by an LLM layer. Unlike popularity-based tools, MTG Brew Assistant builds a coherent gameplan around your commander and explains *why* each card earns its slot.

---

## Features

- **Commander-driven brewing** — input a commander and receive a full gameplan with categorized card suggestions
- **Reasoned recommendations** — every card includes a concise explanation of its role in the strategy
- **On-demand deep analysis** — request an in-depth breakdown of any individual card's contribution to the deck
- **Conversational refinement** — follow up in natural language to adjust the brew ("make it more aggressive", "add more interaction")
- **Image input** — upload a photo or screenshot of a card instead of typing the name
- **Brew history** — save and revisit past brews, track preferences across commanders

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI + PostgreSQL (SQLAlchemy + Alembic) |
| Frontend | Svelte (via Vite) |
| LLM | OpenRouter |
| Card Data | Scryfall API |
| Package Manager | uv |
| Backend Testing | pytest + pytest-asyncio |
| Frontend Testing | Vitest |

---

## Project Structure

```
mtg_brew_assistant/
├── backend/
│   ├── app/
│   │   ├── api/        # Route handlers
│   │   ├── core/       # Config and settings
│   │   ├── db/         # Database session management
│   │   └── models/     # SQLAlchemy models
│   └── tests/          # pytest test suite
├── frontend/           # Svelte SPA (via Vite)
├── .python-version
├── pyproject.toml
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- [Docker](https://www.docker.com/) (for running PostgreSQL locally)
- An [OpenRouter](https://openrouter.ai/) API key

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/mtg-brew-assistant.git
cd mtg-brew-assistant

# Install dependencies
uv sync

# Copy and configure environment variables
cp .env.example .env
```

### Environment Variables

```env
DATABASE_URL=postgresql://user:password@localhost:5432/mtg_brew
OPENROUTER_API_KEY=your_openrouter_api_key
```

The `DATABASE_URL` credentials must match the values defined in `docker-compose.yml`.

### Starting the Database

```bash
docker compose up -d
```

### Running the Backend

```bash
uv run fastapi dev backend/app/main.py
```

### Running Tests

```bash
uv run pytest backend/tests/
```

---

## Database Migrations

This project uses Alembic for schema migrations.

```bash
# Apply all migrations
uv run alembic upgrade head

# Generate a new migration
uv run alembic revision --autogenerate -m "description"
```

On first run, a seed script populates the `cards` table from Scryfall's bulk data export.

---

## Roadmap

- [x] Phase 1 — Project setup, database schema, Scryfall bulk seed
- [ ] Phase 2 — Core brew engine (Scryfall query builder + LLM integration)
- [ ] Phase 3 — Svelte frontend + chat interface
- [ ] Phase 4 — Brew saving, history, and preferences
- [ ] Phase 5 — On-demand deep card reasoning
- [ ] Phase 6 — Multi-user support

---

## Contributing

Contributions are welcome. Please open an issue before submitting a pull request to discuss the proposed change.

---

## License

MIT