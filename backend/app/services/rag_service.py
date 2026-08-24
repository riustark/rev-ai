from app.services.search_service import search_service
from app.services.prompt_service import PromptService
from app.services.llm_service import LLMService


class RAGService:
    """
    Orchestrates the complete RAG pipeline.
    """

    def __init__(self):
        self.search_service = search_service
        self.llm_service = LLMService()

    def ask(self, question: str):

        # Step 1 : Retrieve relevant chunks
        search_results = self.search_service.search(question)

        # Step 2 : Build Prompt
        prompt = PromptService.build_prompt(
            question=question,
            search_results=search_results
        )

        # Step 3 : Generate AI Answer
        answer = self.llm_service.generate_answer(prompt)

        # Step 4 : Return response
        return {
            "question": question,
            "answer": answer,
            "sources": [
                {
                    "repository": chunk["repository"],
                    "file_name": chunk["file_name"],
                    "score": round(chunk["score"], 3)
                }
                for chunk in search_results
            ]
        }


rag_service = RAGService()