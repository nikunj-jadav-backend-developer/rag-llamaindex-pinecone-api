from fastapi import UploadFile, HTTPException

from app.core.config import get_settings
from app.repositories.file_repository import FileRepository
from app.services.llamaindex_service import LlamaIndexService

class DocumentService:
    def __init__(self):
        self.settings = get_settings()
        self.file_repository = FileRepository()
        self.llamaindex_service = LlamaIndexService()

    def validate_file_extension(self, file: UploadFile) -> None:
        extension = file.filename.split(".")[-1].lower()

        if extension not in self.settings.ALLOWED_FILE_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail=f"Only {self.settings.ALLOWED_FILE_EXTENSIONS} files are allowed",
            )

    def validate_file_size(self, file: UploadFile) -> None:
        file.file.seek(0, 2)
        file_size = file.file.tell()
        file.file.seek(0)

        if file_size > self.settings.max_upload_size_bytes:
            raise HTTPException(
                status_code=400,
                detail=f"File size must be less than {self.settings.MAX_UPLOAD_SIZE_MB} MB",
            )

    async def upload_document(self, file: UploadFile):
        self.validate_file_extension(file)
        self.validate_file_size(file)

        file_path = await self.file_repository.save_file(file)

        self.llamaindex_service.ingest_document(file_path)

        return {
            "status": "success",
            "message": "Document uploaded successfully",
            "file_name": file.filename,
            "file_path": file_path,
        }