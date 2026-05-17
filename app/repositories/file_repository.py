import os
import uuid

from fastapi import UploadFile

from app.core.config import get_settings


class FileRepository:
    def __init__(self):
        self.settings = get_settings()

    async def save_file(self, file: UploadFile) -> str:
        os.makedirs(self.settings.UPLOAD_DIR, exist_ok=True)

        extension = file.filename.split(".")[-1].lower()
        unique_file_name = f"{uuid.uuid4()}.{extension}"

        file_path = os.path.join(
            self.settings.UPLOAD_DIR,
            unique_file_name
        )

        content = await file.read()

        with open(file_path, "wb") as buffer:
            buffer.write(content)

        return file_path