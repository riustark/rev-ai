
import os
# pyrefly: ignore [missing-import]
from google import genai
from dotenv import load_dotenv

load_dotenv()


class LLMService:
    """
    Handles communication with Gemini.
    """

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")

        self.client = genai.Client(api_key=api_key)
        self.model_name = "gemini-3.5-flash"

    def generate_answer(self, prompt: str) -> str:
        """
        Generate an AI response from the prompt.
        """

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
        )

        return response.text


