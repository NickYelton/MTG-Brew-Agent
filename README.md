# 🧪 MTG Brew Assistant

> Opinionated Commander deck-building advice powered by FastAPI, PostgreSQL, and an LLM layer via OpenRouter.

EDHRec tells you what's popular. MTG Brew Assistant tells you *why* a card belongs in your deck — and builds you a coherent gameplan around your commander.

---

## ✨ Features

- **Commander-driven brewing** — input a commander, receive a full gameplan with categorized card suggestions
- **Reasoned recommendations** — every card comes with a concise explanation of why it fits the strategy
- **On-demand deep reasoning** — click any card for an in-depth analysis of its role in the deck
- **Conversational refinement** — follow up with natural language to adjust the brew ("make it more aggressive", "add more interaction")
- **Image input** — upload a photo or screenshot of a card instead of typing the name
- **Brew history** — save and revisit past brews, track commander preferences over time

---

## 🛠️ Tech Stack

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

## 🏗️ Project Structure

```
mtg_brew_assistant/
├── backend/
│   ├── app/
│   │   ├── api/        # Route handlers
│   │   ├── core/       # Config and settings
│   │   ├── db/         # Database session management
│   │   └── models/     # SQLAlchemy models
│   └── tests/          # pytest test suite
├── frontend/           # Svelte SPA (scaffolded in Phase 3)
├── .python-version
├── pyproject.toml
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) — fast Python package manager
- PostgreSQL (local instance or Docker)
- An [OpenRouter](https://openrouter.ai/) API key

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/mtg-brew-assistant.git
cd mtg-brew-assistant

# Install dependencies
uv sync

# Copy environment variables
cp .env.example .env
# Fill in your values in .env
```

### Environment Variables

```
DATABASE_URL=postgresql://user:password@localhost:5432/mtg_brew
OPENROUTER_API_KEY=your_openrouter_api_key
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

## 🗄️ Database

This project uses Alembic for database migrations.

```bash
# Run migrations
uv run alembic upgrade head

# Create a new migration
uv run alembic revision --autogenerate -m "description"
```

On first run, the Scryfall bulk data seed script will populate the `cards` table.

---

## 🧪 Development Approach

This project follows a **TDD (Test-Driven Development)** workflow throughout:

1. Write a failing test that describes the desired behaviour (**Red**)
2. Write the minimum code to make it pass (**Green**)
3. Refactor for clarity and quality (**Refactor**)

Development is broken into six phases, from foundation and core brew engine through to frontend, persistence, deep reasoning, and eventual multi-user support.

---

## 🗺️ Roadmap

- [x] Phase 1 — Project setup, DB schema, Scryfall bulk seed
- [ ] Phase 2 — Core brew engine (Scryfall query builder + LLM integration)
- [ ] Phase 3 — Svelte frontend + chat interface
- [ ] Phase 4 — Brew saving, history, and preferences
- [ ] Phase 5 — On-demand deep card reasoning
- [ ] Phase 6 — Multi-user auth

---

## 📄 License

MIT