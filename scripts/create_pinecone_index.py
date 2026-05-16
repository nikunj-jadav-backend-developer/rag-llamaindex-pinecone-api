import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from pinecone import Pinecone, ServerlessSpec
from app.core.config import settings

def create_pinecone_index():
    pc = Pinecone(api_key=settings.get_pinecone_api_key())

    existing_indexes = [index["name"] for index in pc.list_indexes()]

    if settings.PINECONE_INDEX not in existing_indexes:
        pc.create_index(
            name=settings.PINECONE_INDEX_NAME,
            dimension=settings.EMBEDDING_DIMENSION,
            metric=settings.PINECONE_METRIC,
            spec=ServerlessSpec(
                cloud=settings.PINECONE_CLOUD,
                region=settings.PINECONE_REGION,
            ),
        )
        print(f"Created Pinecone index: {settings.PINECONE_INDEX}")
    else:
        print(f"Pinecone index '{settings.PINECONE_INDEX}' already exists.")

if __name__ == "__main__":
    create_pinecone_index()