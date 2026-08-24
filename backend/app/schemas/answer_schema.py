from pydantic import BaseModel


class Source(BaseModel):
    repository: str
    file_name: str
    score: float


class AskResponse(BaseModel):
    question: str
    answer: str
    sources: list[Source]