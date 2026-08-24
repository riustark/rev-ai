# pyrefly: ignore [missing-import]
from qdrant_client import QdrantClient

client = QdrantClient(host="localhost", port=6333)

print(dir(client))