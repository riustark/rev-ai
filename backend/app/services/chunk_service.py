class ChunkService:

    def __init__(self,chunk_size=1000):
        self.chunk_size=chunk_size


    def create_chunks(self,indexed_repository):
        chunks=[]

        for file_data in indexed_repository["files"]:
            file_chunks = self.chunk_file(
                
                repository = indexed_repository["repository"],
                file_data = file_data,
            )
            chunks.extend(file_chunks)
        
        return {
            "repository" : indexed_repository["repository"],
            "total_chunks": len(chunks),
            "chunks": chunks,
        
        }

    def chunk_file(self, repository, file_data):
        content = file_data["content"]

        chunks = []

        for start in range(0, len(content), self.chunk_size):
            chunk_content = content[start:start + self.chunk_size]

            chunk = self._build_chunk(
                repository=repository,
                file_data=file_data,
                chunk_index=len(chunks),
                content=chunk_content,
            )
            chunks.append(chunk)

        return chunks

    def _build_chunk(
        self,
        repository,
        file_data,
        chunk_index,
        content,
    ):
        return {
            "chunk_id": f"{file_data['path']}:{chunk_index}",
            "chunk_index": chunk_index,
            "repository": repository,
            "file_name": file_data["name"],
            "file_path": file_data["path"],
            "extension": file_data["extension"],
            "size": len(content),
            "content": content,
        }
            
chunk_service = ChunkService()



    