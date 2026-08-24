from app.services import chunk_service
from app.services.github_service import GitHubService
from pathlib import Path
import base64
IGNORE_DIRS = {
    ".git",
    "node_modules",
    "dist",
    "build",
    ".next",
    "__pycache__",
    ".idea",
    ".vscode",
    "venv",
    ".venv"
}

SOURCE_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".html",
    ".css",
    ".scss",
    ".java",
    ".cpp",
    ".c",
    ".cs",
    ".go",
    ".rs",
    ".php",
    ".rb",
    ".swift",
    ".kt",
    ".json",
    ".yaml",
    ".yml",
    ".md",
    ".txt"
}

class IndexService:

    def __init__(self):
        self.github_service = GitHubService()

    def index_repository(self,owner: str, repo:str):
        tree = self.github_service.get_repository_tree(owner, repo)
        files = []
        for item in tree["tree"]:

            if item["type"] != "blob":
                continue
            path = item["path"]
            #skip ignored directories
            path_parts = path.split("/")

            if any(folder in IGNORE_DIRS for folder in path_parts):
                continue

            extension = Path(path).suffix.lower()

            if extension and extension not in SOURCE_EXTENSIONS:
                continue

            try:
                file_data = self.github_service.get_file(owner,repo,path)
                raw_content = file_data.get("content", "")
                encoding = file_data.get("encoding", "")
                if encoding == "base64":
                    # Remove linebreaks from base64 string and decode
                    decoded_content = base64.b64decode(raw_content.replace("\n", "")).decode("utf-8", errors="ignore")
                else:
                    decoded_content = raw_content

                files.append({
                    "name" : Path(path).name,
                    "path": path,
                    "extension": extension,
                    "size": file_data.get("size",0),
                    "content" : decoded_content
                })
            
            except Exception as e:
                print(f"Skipping {path} : {e}")

        return {
            "repository" :repo,
            "total_files": len(files),
            "files": files
        }

        



index_service = IndexService()

