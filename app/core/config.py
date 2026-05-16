from functools import lru_cache
from pydantic import Field,SecretStr,field_validator
from pydantic_settings import BaseSettings,SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    APP_NAME : str = Field(default="RAG LlamaIndex Pinecone API"),
    APP_VERSION : str = Field(default="1.0.0"),
    APP_ENV : str = Field(default="local"),
    APP_DEBUG: bool = Field(default=True),
    API_V1_PREFIX: str = Field(default="/api/v1")
    PINECONE_API_KEY: SecretStr = Field(default=...),
    PINECONE_INDEX: str = Field(default=...),
    PINECONE_EMBEDDING_DIMENSION: int = Field(default=1536),
    PINECONE_METRIC: str = Field(default="cosine"),
    PINECONE_CLOUD: str = Field(default="aws"),
    PINECONE_REGION: str = Field(default="us-east-1"),
    GROQ_API_KEY: SecretStr = Field(default=...),
    GROQ_LLM_MODEL: str = Field(default="gpt-4o"),
    BACKEND_CORS_ORIGINS: List[str] = Field(default=[
        "http://localhost",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        ]
    )
    LOG_LEVEL: str = Field(default="INFO")
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

    @property
    def is_production(self)->bool:
        return self.APP_ENV == "production"

    def get_groq_api_key(self) -> str:
        return self.GROQ_API_KEY.get_secret_value()

    def get_pinecone_api_key(self) -> str:
        return self.PINECONE_API_KEY.get_secret_value()

@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()