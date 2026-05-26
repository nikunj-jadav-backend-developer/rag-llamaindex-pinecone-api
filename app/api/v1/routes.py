from fastapi import APIRouter
from app.api.v1.health_routes import router as health_router
from app.api.v1.document_routes import router as document_router
from app.api.v1.rag_routes import router as rag_router

api_router = APIRouter()

api_router.include_router(health_router,tags=["Health"])

api_router.include_router(
    document_router,
    prefix="/documents",
    tags=["Documents"]
)

api_router.include_router(
    rag_router,
    prefix="/rag",
    tags=["RAG"]
)