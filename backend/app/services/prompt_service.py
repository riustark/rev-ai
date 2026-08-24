from typing import List

class PromptService:
    """
    Builds prompts for the LLM using retrived repository chunks
    """

    SYSTEM_PROMPT = """
You are Rev-AI, an expert AI Software Engineer and Codebase Assistant.

You answer questions ONLY using the provided repository context.

Guidelines:

- Never invent information.
- If the repository does not contain enough information, explicitly say so.
- Mention the relevant file names whenever possible.
- Explain code in a structured and easy-to-understand way.
- When appropriate, explain the execution flow step by step.
- If multiple files are involved, describe how they interact.
- Keep answers concise but technically accurate.
"""

    @classmethod
    def build_prompt(cls,question: str, search_results: List[dict]) -> str :
        """
        Build the final prompt for the LLM
        """

        context =""

        for index,chunk in enumerate(search_results, start=1):

            repository = chunk.get("repository","unknown Repository")
            file_name = chunk.get("file_name", "Unknown File")
            score = chunk.get("score", 0)
            content = chunk.get("content", "")

            context += f"""

========================+

Context {index}

Repository: {repository}
File  : {file_name}
Similarity : {score:.3f}

=============================

{content}


"""

        prompt = f"""
{cls.SYSTEM_PROMPT}

=============================
Repository Context
=============================

{context}

=============================
User Question
=============================

{question}

=============================
Answer
=============================

"""
        return prompt

