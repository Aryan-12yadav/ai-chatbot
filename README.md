# AI Chatbot — RAG + LangChain + FastAPI

A full-stack AI chatbot demonstration using Python, FastAPI, REST APIs, LangChain, OpenAI LLM APIs, Retrieval-Augmented Generation (RAG), Chroma vector database, SQLAlchemy/SQLite, and HTML/CSS/JavaScript.

## Architecture

Browser (HTML/CSS/JS) → FastAPI REST API → RAG retriever → Chroma vector DB → LangChain prompt → OpenAI LLM → JSON response

Conversation messages are persisted with SQLAlchemy. SQLite is used by default; PostgreSQL can be configured with `DATABASE_URL`.

## Run locally

```bash
python -m venv venv
# Windows: venv\\Scripts\\activate
# Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Add OPENAI_API_KEY to .env
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000` for the web UI or `/docs` for Swagger API documentation.

## AWS EC2

On Ubuntu EC2, install Python/Git, copy or clone this project, create a virtual environment, install requirements, set `OPENAI_API_KEY`, then run:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Allow TCP 8000 in the EC2 security group for a temporary recruiter demo. For production, use HTTPS/reverse proxy, authentication, rate limiting and a managed secrets solution.

## Docker

```bash
docker compose up --build
```

## Project explanation

“I built a full-stack AI chatbot where the frontend is HTML, CSS and JavaScript and the backend is Python FastAPI. For AI, I integrated an OpenAI LLM through LangChain. I used RAG so the user's question is converted into a retrieval query, relevant chunks are fetched from a Chroma vector database, and that context is passed to the LLM before generating the answer. I also added REST endpoints, health checks, conversation persistence using SQLAlchemy/SQLite, and Docker support. The application can be deployed on Ubuntu EC2 with Uvicorn.”
