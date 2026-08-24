from app.services.llm_service import LLMService

llm = LLMService()

response = llm.generate_answer(
    """
You are an AI software engineer.

Explain FastAPI in one paragraph.
"""
)

print(response)