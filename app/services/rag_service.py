from app.services.llamaindex_service import LlamaIndexService


class RagService:
    def __init__(self):
        self.llamaindex_service = LlamaIndexService()

    def ask_question(self, question: str):
        answer = self.llamaindex_service.query(question)

        return {
            "status": "success",
            "answer": answer,
        }