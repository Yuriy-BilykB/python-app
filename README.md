# Beginner FastAPI CRUD API

A small project for learning Python, FastAPI, and how a backend can be divided into clear responsibilities.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open <http://127.0.0.1:8000/docs> to try the API. The data lives only in memory, so it resets when the server stops.

## Project structure

```text
app/
├── main.py                    # Creates the FastAPI app and connects routes
├── api/routes/items.py        # HTTP endpoints: URL, request, and response
├── schemas/item.py            # Validates incoming data and shapes responses
├── services/item_service.py   # Coordinates operations and handles app rules
└── repositories/item_repository.py  # Reads and writes the in-memory data
```

The request flow is **route → service → repository**. The response comes back through the same layers. This is similar to a controller → service → repository arrangement in .NET or NestJS.

## CRUD routes

| Action | Method | Path | Purpose |
| --- | --- | --- | --- |
| Create | POST | `/items` | Add an item |
| Read | GET | `/items` | List all items |
| Read | GET | `/items/{item_id}` | Get one item |
| Update | PUT | `/items/{item_id}` | Replace an item's fields |
| Delete | DELETE | `/items/{item_id}` | Remove an item |
