```md
# FastAPI Items API

Simple FastAPI backend used by the React frontend to list and create items.

## Tech Stack
- Python
- FastAPI
- Uvicorn

## Features
- List items (GET /items)
- Create items (POST /items)
- In-memory data storage
- CORS configured for local frontend development

## Requeriments
- Python 3.10+ recommended

## Setup
Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt

Run
Start the server:
uvicorn main:app --reload

Server will be available at:
http://127.0.0.1:8000

API Endpoints
GET /items
Returns the list of items.

POST /items
Creates a new item.

Example request body:
{
    "title": "Apple",
    "description": "Fruit"
}

CORS
CORS is configured to allow requests from the Vite dev server:
http://localhost:5173
http://127.0.0.1:5173
