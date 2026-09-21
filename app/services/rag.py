from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from app.config import CHROMA_DIR, EMBEDDING_MODEL

COLLECTION = 'ai_chatbot_knowledge'

def get_vector_store():
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    return Chroma(collection_name=COLLECTION, embedding_function=embeddings, persist_directory=CHROMA_DIR)

def build_index(reset=False):
    Path(CHROMA_DIR).mkdir(parents=True, exist_ok=True)
    store = get_vector_store()
    if reset:
        try: store.reset_collection()
        except Exception: pass
    docs = []
    for path in Path('data').glob('*.txt'):
        docs.extend(TextLoader(str(path), encoding='utf-8').load())
    if not docs: return 0
    splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=120)
    chunks = splitter.split_documents(docs)
    store.add_documents(chunks)
    return len(chunks)

def retrieve(query, k=4):
    return get_vector_store().similarity_search(query, k=k)
