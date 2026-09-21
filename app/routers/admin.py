from fastapi import APIRouter, HTTPException
from app.config import OPENAI_API_KEY
from app.services.rag import build_index

router = APIRouter(prefix='/api/admin', tags=['RAG'])

@router.post('/reindex')
def reindex():
    if not OPENAI_API_KEY:
        raise HTTPException(status_code=500, detail='OPENAI_API_KEY is not configured.')
    count = build_index(reset=True)
    return {'status': 'indexed', 'chunks': count}
