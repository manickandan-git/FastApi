# FastAPI Example Project

This repository is a small, opinionated example API built with FastAPI, SQLAlchemy and Pydantic. It demonstrates
user authentication (JWT), CRUD operations for posts, voting, and database migrations with Alembic.

**Quick links**
- Project: [README.md](README.md)
- App entry: [app/main.py](app/main.py)
- Configuration: [app/config.py](app/config.py)
- Routers: [app/routers](app/routers)

## Features

- JWT authentication (login, token creation)
- Users: create, read, update, delete
- Posts: create, read, update, delete, list with search/pagination
- Votes: add/remove vote on posts
- Alembic migrations for schema management

## Requirements

- Python 3.10+
- See `requirements.txt` for full dependency list

## Environment

This project uses a `.env` file (configured in `app/config.py`). Example `.env` keys:

```
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=yourpassword
DATABASE_NAME=fastapi_db
DATABASE_USERNAME=youruser
SECRET_KEY=changeme
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Create a `.env` file in the project root and set the values before running.

## Installation

1. Create and activate a virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

## Database & Migrations

Configure your database connection in `.env` then run Alembic migrations:

```bash
alembic upgrade head
```

Migrations are stored in the `alembic/versions` folder.

## Running Locally

Start the development server with Uvicorn:

```bash
uvicorn app.main:app --reload
```

API will be available at http://127.0.0.1:8000 and automatic docs at http://127.0.0.1:8000/docs

## API Endpoints

Authentication:
- `POST /login` — obtain access token (OAuth2 password flow)

Users (`/users`):
- `POST /users/` — create user
- `GET /users/` — list users
- `GET /users/{id}` — get user by id
- `PUT /users/{id}` — update user
- `DELETE /users/{id}` — delete user

Posts (`/posts`):
- `GET /posts/` — list posts (query: `limit`, `skip`, `search`)
- `POST /posts/` — create post (authenticated)
- `GET /posts/{id}` — get post by id
- `PUT /posts/{id}` — update post (owner only)
- `DELETE /posts/{id}` — delete post (owner only)

Votes (`/vote`):
- `POST /vote/` — cast or remove a vote (authenticated)

Note: Many endpoints require a valid bearer token in the `Authorization` header.

## Docker

There are `docker-compose-dev.yml` and `docker-compose-prod.yml` files included for containerized development and production setups.

## Deployment

This repo includes a `Dockerfile`, `gunicorn.service` and a `Procfile` for different deployment targets. Adjust environment variables and secrets before deploying.

## Tests

No test suite is included in this example. Add tests under a `tests/` folder and run with `pytest`.

## Next steps

- Add automated tests
- Harden authentication and input validation
- Add CI/CD pipeline and container registry publishing

If you'd like, I can also run tests, add a `.env.example`, or scaffold a simple `docker-compose` development setup.




