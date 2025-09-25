from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.llm_manager import llm_manager

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    try:
        resp = await llm_manager.generate(req.query)
        return ChatResponse(response=resp)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
