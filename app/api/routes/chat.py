from fastapi import APIRouter

from app.api.schemas.chat import ChatRequest, ChatResponse
from app.api.services.assistant_service import BootstrapAssistantService


router = APIRouter(
    prefix="/api/v1/chat",
    tags=["chat"],
)

service = BootstrapAssistantService()


@router.post(
    "",
    response_model=ChatResponse,
)
async def chat(
    payload: ChatRequest,
) -> ChatResponse:
    return await service.answer(payload.question)