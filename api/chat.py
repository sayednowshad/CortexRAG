from fastapi import APIRouter

from models.request_models import (
    ChatRequest
)

from services.answer_service import (
    AnswerService
)

router = APIRouter()


@router.post("/chat")
def chat(
    request: ChatRequest
):

    return (
        AnswerService
        .answer_question(
            request.question
        )
    )