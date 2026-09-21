import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
EMBEDDING_MODEL = os.getenv('EMBEDDING_MODEL', 'text-embedding-3-small')
CHROMA_DIR = os.getenv('CHROMA_DIR', 'storage/chroma')
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./storage/chatbot.db')
