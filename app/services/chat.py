from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from app.config import OPENAI_API_KEY, OPENAI_MODEL
from app.services.rag import retrieve

SYSTEM = '''You are an AI assistant for a software engineering demo.
Use the supplied context when it is relevant. Do not invent facts about the
knowledge base. If the answer is not in the context, say that the information
is not available in the knowledge base, then provide a general answer only if
it is clearly useful. Keep responses concise and professional.

Context:
{context}'''

def generate_answer(question: str):
    if not OPENAI_API_KEY:
        raise RuntimeError('OPENAI_API_KEY is not configured. Add it to .env.')
    docs = retrieve(question)
    context = '\n\n'.join(d.page_content for d in docs)
    prompt = ChatPromptTemplate.from_messages([('system', SYSTEM), ('human', '{question}')])
    llm = ChatOpenAI(model=OPENAI_MODEL, temperature=0.2, api_key=OPENAI_API_KEY)
    result = llm.invoke(prompt.format_messages(context=context, question=question))
    sources = list(dict.fromkeys(d.metadata.get('source', 'knowledge base') for d in docs))
    return result.content, sources
