import os

from pinecone import Pinecone

from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    Settings as LlamaSettings,
)
from llama_index.core.node_parser import SentenceSplitter
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq

from app.core.config import settings


class LlamaIndexService:
    def __init__(self):
        """
        Initialize Pinecone, HuggingFace embedding model,
        Groq LLM, and LlamaIndex global settings.
        """

        # Groq API key is used by Groq LLM.
        os.environ["GROQ_API_KEY"] = settings.get_groq_api_key

        # Pinecone client
        self.pc = Pinecone(
            api_key=settings.get_pinecone_api_key
        )

        # Pinecone index
        self.pinecone_index = self.pc.Index(
            settings.PINECONE_INDEX
        )

        # LlamaIndex Pinecone vector store
        self.vector_store = PineconeVectorStore(
            pinecone_index=self.pinecone_index
        )

        # Storage context tells LlamaIndex where vectors are stored
        self.storage_context = StorageContext.from_defaults(
            vector_store=self.vector_store
        )

        # HuggingFace embedding model
        self.embed_model = HuggingFaceEmbedding(
            model_name=settings.HF_EMBEDDING_MODEL
        )

        # Groq LLM
        self.llm = Groq(
            model=settings.GROQ_LLM_MODEL,
            api_key=settings.get_groq_api_key,
            temperature=settings.GROQ_LLM_TEMPERATURE,
        )

        # Global LlamaIndex settings
        LlamaSettings.embed_model = self.embed_model
        LlamaSettings.llm = self.llm
        LlamaSettings.node_parser = SentenceSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
        )

    def ingest_document(self, file_path: str) -> bool:
        """
        Load document, split into chunks, create embeddings,
        and store vectors into Pinecone.
        """

        documents = SimpleDirectoryReader(
            input_files=[file_path]
        ).load_data()

        VectorStoreIndex.from_documents(
            documents,
            storage_context=self.storage_context,
            embed_model=self.embed_model,
        )

        return True

    def query(self, question: str) -> str:
        """
        Search relevant chunks from Pinecone and generate answer using Groq LLM.
        """

        index = VectorStoreIndex.from_vector_store(
            vector_store=self.vector_store,
            embed_model=self.embed_model,
        )

        query_engine = index.as_query_engine(
            llm=self.llm,
            similarity_top_k=settings.SIMILARITY_TOP_K,
        )

        response = query_engine.query(question)

        return str(response)