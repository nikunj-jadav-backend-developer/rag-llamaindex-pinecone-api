from functools import lru_cache
from pydantic import Field,SecretStr,field_validator
from pydantic_settings import BaseSettings,SettingsConfigDict
from typing import List

class Settings(BaseSettings):

    # -------------------------------------------------------------------------
    # Application
    # -------------------------------------------------------------------------
    APP_NAME : str = Field(default="RAG LlamaIndex Pinecone API")
    APP_VERSION : str = Field(default="1.0.0")
    APP_ENV : str = Field(default="local")
    APP_DEBUG: bool = Field(default=True)
    API_V1_PREFIX: str = Field(default="/api/v1")

    # -------------------------------------------------------------------------
    # Pinecone
    # -------------------------------------------------------------------------
    
    PINECONE_API_KEY: SecretStr = Field(default=...)
    PINECONE_INDEX: str = Field(default=...)
    PINECONE_EMBEDDING_DIMENSION: int = Field(default=1536)
    PINECONE_METRIC: str = Field(default="cosine")
    PINECONE_CLOUD: str = Field(default="aws")
    PINECONE_REGION: str = Field(default="us-east-1")

    # -------------------------------------------------------------------------
    # Groq LLM
    # -------------------------------------------------------------------------
    GROQ_API_KEY: SecretStr = Field(default=...),
    GROQ_LLM_MODEL: str = Field(default="gpt-4o"),
    GROQ_LLM_TEMPERATURE: float = Field(default=0.4)

    # -------------------------------------------------------------------------
    # HuggingFace Embeddings
    # -------------------------------------------------------------------------
    HF_EMBEDDING_MODEL: str = Field(
        default="sentence-transformers/all-MiniLM-L6-v2"
    )
    EMBEDDING_DIMENSION: int = Field(default=384)

    # -------------------------------------------------------------------------
    # CORS
    # -------------------------------------------------------------------------
    BACKEND_CORS_ORIGINS: List[str] = Field(default=[
        "http://localhost",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        ]
    )

    # -------------------------------------------------------------------------
    # Logging
    # -------------------------------------------------------------------------

    LOG_LEVEL: str = Field(default="INFO")

    # -------------------------------------------------------------------------
    # File Upload
    # -------------------------------------------------------------------------
    UPLOAD_DIR: str = Field(default="storage/uploads")
    MAX_UPLOAD_SIZE_MB: int = Field(default=20)
    ALLOWED_FILE_EXTENSIONS: List[str] = Field(default=["pdf", "txt"])


    # -------------------------------------------------------------------------
    # RAG
    # -------------------------------------------------------------------------
    CHUNK_SIZE: int = Field(default=1024)
    CHUNK_OVERLAP: int = Field(default=100)
    SIMILARITY_TOP_K: int = Field(default=5)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    @field_validator("APP_ENV")
    @classmethod
    def validate_app_env(cls, value):
        allowed_envs = ["local", "development", "production"]
        if value not in allowed_envs:
            raise ValueError(f"APP_ENV must be one of {allowed_envs}")
        return value

    @field_validator("PINECONE_METRIC")
    @classmethod
    def validate_pinecone_metric(cls, value):
        allowed_metrics = ["cosine", "euclidean", "dotproduct"]
        if value not in allowed_metrics:
            raise ValueError(f"PINECONE_METRIC must be one of {allowed_metrics}")
        return value
    
    @field_validator("MAX_UPLOAD_SIZE_MB")
    @classmethod
    def validate_upload_size(cls, value: int) -> int:
        if value <= 0:
            raise ValueError("MAX_UPLOAD_SIZE_MB must be greater than 0")

        return value

    @field_validator("GROQ_LLM_TEMPERATURE")
    @classmethod
    def validate_temperature(cls, value: float) -> float:
        if not (0.0 <= value <= 1.0):
            raise ValueError("GROQ_LLM_TEMPERATURE must be between 0.0 and 1.0")
        return value

    @field_validator("SIMILARITY_TOP_K")
    @classmethod
    def validate_similarity_top_k(cls, value: int) -> int:
        if value <= 0:
            raise ValueError("SIMILARITY_TOP_K must be greater than 0")

        return value

    @property
    def is_production(self)->bool:
        return self.APP_ENV == "production"

    @property
    def get_groq_api_key(self) -> str:
        return self.GROQ_API_KEY.get_secret_value()
    @property
    def get_pinecone_api_key(self) -> str:
        return self.PINECONE_API_KEY.get_secret_value()

    @property
    def max_upload_size_bytes(self) -> int:
        return self.MAX_UPLOAD_SIZE_MB * 1024 * 1024

@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()