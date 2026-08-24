import requests
from app.core.config import GITHUB_TOKEN

class GitHubService:
    BASE_URL = "https://api.github.com"

    
    #using token to authenticate with GitHub API
    
    def __init__(self):
        self.headers ={
            "Authorization" : f"Bearer {GITHUB_TOKEN}",
            "Accept" : "application/vnd.github+json"

        }

    #Fetching user_data

    def get_authenticated_user(self):
        response = requests.get(
            f"{self.BASE_URL}/user",
            headers=self.headers
        )

        return response.json()
    
    def get_repositories(self):
        response = requests.get(
            f"{self.BASE_URL}/user/repos",
            headers=self.headers
        )

        response.raise_for_status()
        return response.json()

    def get_repository(self, owner: str, repo: str):
        response = requests.get(
            f"{self.BASE_URL}/repos/{owner}/{repo}",
            headers=self.headers
        )

        response.raise_for_status()
        repository = response.json()

        return {
            "id": repository["id"],
        "name": repository["name"],
        "full_name": repository["full_name"],
        "description": repository["description"],
        "language": repository["language"],
        "default_branch": repository["default_branch"],
        "private": repository["private"],
        "stars": repository["stargazers_count"],
        "forks": repository["forks_count"],
        "open_issues": repository["open_issues_count"],
        "size": repository["size"],
        "created_at": repository["created_at"],
        "updated_at": repository["updated_at"],
        "clone_url": repository["clone_url"]
        }

    def get_repository_tree(self,owner, repo):
        response = requests.get(
            f"{self.BASE_URL}/repos/{owner}/{repo}/git/trees/HEAD?recursive=1",
            headers=self.headers
        )

        response.raise_for_status()

        data = response.json()
        print(type(data))
        print(data)

        return data
    

    def get_file(self, owner:str, repo : str, path: str):

        response = requests.get(
            f"{self.BASE_URL}/repos/{owner}/{repo}/contents/{path}",
            headers=self.headers,
        )

        response.raise_for_status()
    
        return response.json()