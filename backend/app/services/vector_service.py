# pyrefly: ignore [missing-import]
from qdrant_client import QdrantClient

# pyrefly: ignore [missing-import]
from qdrant_client.models import VectorParams, Distance

# pyrefly: ignore [missing-import]
from qdrant_client.models import PointStruct

class VectorService:

    def __init__(self):
        self.client = QdrantClient(
            host = "localhost",
            port=6333
        )

    def check_connection(self):
        return self.client.get_collections()

    def create_collection(self):

        self.client.recreate_collection(
            collection_name = "rev_ai_repositories",

            vectors_config = VectorParams(
                size = 384,
                distance = Distance.COSINE
            )
        )
        return {
            "message" : "Collection created successfully"
        }
    
    def store_embeddings(self,embedded_repository):

        points =[]
        for index,embedding in enumerate(embedded_repository["embeddings"]):
            point = PointStruct(
                id =index,
                vector=embedding["embedding"],
                payload={
                    "repository" :embedding["repository"],
                    "file_name":embedding["file_name"],
                    "file_path":embedding["file_path"],
                    "chunk_index": embedding["chunk_index"],
                    "content": embedding["content"]
                    }
            )
            points.append(point)
        
        self.client.upsert(
            collection_name="rev_ai_repositories",
            points=points
        )


        return {
            "repository": embedded_repository["repository"],
            "stored_vectors": len(points),
            "status": "success"
        }


vector_service = VectorService()