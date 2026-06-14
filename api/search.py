from fastapi import APIRouter

from models.request_models import (
    SearchRequest
)

from services.retrieval_service import (
    RetrievalService
)

router = APIRouter()


@router.post("/search")
def search_documents(
    request: SearchRequest
):

    results = RetrievalService.search(
        query=request.query,
        top_k=request.top_k
    )

    if not results:
        return {
            "query": request.query,
            "message": "No relevant results found",
            "results": []
        }

    return {
        "query": request.query,
        "results": results
    } 