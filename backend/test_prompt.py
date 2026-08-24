from app.services.prompt_service import PromptService

results = [
        {
            "repository" : "REV-AI",
            "file_name" : "github_service.py",
            "score" : 0.95,
            "content" : "Authenticate GitHub user using PAT"
        },
        {
            "repository" : "Rev-AI",
            "file_name" : "repository_service.py",
            "score" : 0.92,
            "content": "Fetch repositories after authentication"
        }
    ]

prompt = PromptService.build_prompt(
    question = " How does Github auth works?",
    search_results = results
)

print(prompt)