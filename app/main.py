from fastapi import FastAPI
from app.api.v1.routes import api_router

app = FastAPI(
    title="RAG LlamaIndex Pinecone API",
    description="This is a sample FastAPI application.",
    version="1.0.0",
)

app.include_router(api_router, prefix="/api/v1")