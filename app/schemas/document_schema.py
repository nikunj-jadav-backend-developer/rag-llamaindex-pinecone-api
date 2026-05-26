from pydantic import BaseModel

class DocumentUploadRequestSchema(BaseModel):
    status : str
    message : str
    file_name : str
    file_path: str