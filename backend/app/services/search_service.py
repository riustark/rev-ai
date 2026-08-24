from app.services.embedding_service import embedding_service
from app.services.vector_service import vector_service

class SearchService:

    def __init__(self):
        self.embedding_service = embedding_service
        self.vector_service = vector_service

    def search(self, question: str):
        question_embedding = self.embedding_service.model.encode(
            question,
            convert_to_numpy=True
        ).tolist()

        results = self.vector_service.client.query_points(
            collection_name="rev_ai_repositories",
            query=question_embedding,
            limit=5
        )

        formatted_results = []

        for result in results.points:
            formatted_results.append({
                "score" : result.score,
                "repository": result.payload["repository"],
                "file_name": result.payload["file_name"],
                "chunk_index":result.payload["chunk_index"],
                "content" : result.payload["content"]
            })

        return formatted_results

search_service = SearchService()