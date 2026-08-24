from fastapi import APIRouter

from app.services.github_service import GitHubService

from app.services.repository_service import repository_service

from app.services.file_service import file_service

from app.services.index_service import index_service

from app.services.chunk_service import chunk_service

from app.services.embedding_service import EmbeddingService

from app.services.vector_service import vector_service

from app.services.search_service import search_service

from app.schemas.search_schema import SearchRequest

from app.schemas.ask_schema import AskRequest

from app.services.rag_service import rag_service

from app.schemas.answer_schema import AskResponse



router= APIRouter(
    prefix="/github",
    tags=["Github"]
)

github_service = GitHubService()
embedding_service =EmbeddingService()


@router.get("/me")
def get_me():
    return github_service.get_authenticated_user()


@router.get("/repos")
def get_repositories():
    return github_service.get_repositories()

@router.get("/repos/{owner}/{repo}")
def get_repository(owner: str, repo: str):
    return github_service.get_repository(owner,repo)

@router.get("/repos/{owner}/{repo}/tree")
def get_repository_tree(owner: str, repo: str):
    return github_service.get_repository_tree(owner,repo)

@router.get("/repos/{owner}/{repo}/file")
def get_file(owner :str,repo:str,path:str):
    return file_service.get_file_content(owner,repo,path)

@router.get("/repos/{owner}/{repo}/structure")
def get_repository_structure(owner: str, repo: str):
    return repository_service.get_repository_structure(owner,repo)

@router.get("/repos/{owner}/{repo}/index")
def get_repository_index(owner: str, repo: str):
    return index_service.index_repository(owner,repo)

@router.post("/repos/{owner}/{repo}/chunks")
def create_repository_chunks(owner: str, repo: str):
    indexed_repository = index_service.index_repository(owner, repo)
    chunked_repository = chunk_service.create_chunks(indexed_repository)
    return chunked_repository


@router.post("/repos/{owner}/{repo}/embeddings")
def create_repository_embeddings(owner: str, repo: str):
    indexed_repository = index_service.index_repository(owner, repo)
    chunked_repository = chunk_service.create_chunks(indexed_repository)
    embedded_repository = embedding_service.create_embeddings(chunked_repository)
    return embedded_repository

@router.get("/vector/test")
def test_vector_database():
    return vector_service.check_connection()


@router.get("/vector/create")
def create_vector_collection():
    return vector_service.create_collection()

@router.get("/repos/{owner}/{repo}/store")
def store_repository(owner:str,repo:str):

    indexed_repository = index_service.index_repository(owner,repo)
    chunked_repository = chunk_service.create_chunks(indexed_repository)
    embedded_repository = embedding_service.create_embeddings(chunked_repository)
    vector_service.create_collection()
    result = vector_service.store_embeddings(embedded_repository)

    return result

@router.post("/search")
def search_repository(request: SearchRequest):
    result = search_service.search(request.question)
    return result


    
@router.post(
    "/ask",
    response_model=AskResponse
)
async def ask_repository(request: AskRequest):

    return rag_service.ask(request.question)