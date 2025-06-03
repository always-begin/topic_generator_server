from fastapi import FastAPI
from app.api.endpoints import router as chat_router
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
app.include_router(chat_router)
