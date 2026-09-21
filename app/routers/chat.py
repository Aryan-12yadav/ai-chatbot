from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.services.chat import generate_answer
from app.database import SessionLocal, Message

router = APIRouter(prefix='/api', tags=['Chat'])

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)
    session_id: str = Field(default='demo', max_length=100)

@router.post('/chat')
def chat(req: ChatRequest):
    try:
        answer, sources = generate_answer(req.message)
        db = SessionLocal()
        db.add(Message(session_id=req.session_id, role='user', content=req.message))
        db.add(Message(session_id=req.session_id, role='assistant', content=answer))
        db.commit(); db.close()
        return {'response': answer, 'sources': sources, 'session_id': req.session_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/history/{session_id}')
def history(session_id: str):
    db = SessionLocal()
    rows = db.query(Message).filter(Message.session_id == session_id).order_by(Message.id).all()
    result = [{'role': r.role, 'content': r.content, 'created_at': r.created_at.isoformat()} for r in rows]
    db.close()
    return {'messages': result}
