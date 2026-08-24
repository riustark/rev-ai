# pyrefly: ignore [missing-import]
from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):
        self.model = SentenceTransformer("BAAI/bge-small-en-v1.5")

    def create_embeddings(self,chunked_repository):
        embeddings =[]

        for chunk in chunked_repository["chunks"]:
            embedded_chunk = self._embed_chunk(chunk)
            embeddings.append(embedded_chunk)

        return {
            "repository" : chunked_repository["repository"],
            "total_embeddings" : len(embeddings),
            "dimensions" : len(embeddings[0]["embedding"]) if embeddings else 0,
            "embeddings" :embeddings,
        }

    def _embed_chunk(self,chunk):
        embedding = self.model.encode(
            chunk["content"],
            convert_to_numpy=True
        )

        return {
            **chunk,
            "embedding" : embedding.tolist()
        }


embedding_service = EmbeddingService()