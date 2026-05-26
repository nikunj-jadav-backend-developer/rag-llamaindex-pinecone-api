from fastapi import APIRouter, UploadFile, File

from app.services.document_service import DocumentService

router = APIRouter()


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    service = DocumentService()
    return await service.upload_document(file)