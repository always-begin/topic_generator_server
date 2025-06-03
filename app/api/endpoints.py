from fastapi import APIRouter, Request
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.chat_service import process_chat

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    result = process_chat(request.message)
    return ChatResponse(response=result)