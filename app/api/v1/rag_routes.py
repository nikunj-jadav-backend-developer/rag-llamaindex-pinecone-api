from fastapi import APIRouter
from app.schemas.rag_schema import RagQueryRequest
from app.services.rag_service import RagService

router = APIRouter()

@router.post("/query")
def query_rag(request: RagQueryRequest):
    service = RagService()
    return service.ask_question(request.question)