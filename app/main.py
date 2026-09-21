from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.database import init_db
from app.routers.chat import router as chat_router
from app.routers.admin import router as admin_router
from app.config import OPENAI_API_KEY
from app.services.rag import build_index

Path('storage').mkdir(exist_ok=True)
init_db()
app = FastAPI(title='AI Chatbot | RAG + LangChain', version='1.0.0', description='Production-style AI chatbot demo')
app.include_router(chat_router)
app.include_router(admin_router)
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/', include_in_schema=False)
def root(): return FileResponse('static/index.html')

@app.get('/health')
def health(): return {'status':'healthy', 'llm_configured': bool(OPENAI_API_KEY)}

@app.on_event('startup')
def startup():
    if OPENAI_API_KEY:
        try:
            # Build a small demo index if it is empty; reindex from the UI/API when needed.
            build_index(reset=False)
        except Exception as e:
            print('RAG index warning:', e)
