from app.services.github_service import GitHubService

class RepositoryService:

    def __init__(self):
        self.github = GitHubService()

    
    def get_repository_structure(self,owner: str, repo : str):
        tree = self.github.get_repository_tree(owner,repo)

        files =[]

        for item in tree["tree"]:
            files.append({
                "path" : item["path"],
                "type": item["type"],
                "size": item.get("size")
            })
        
        return { "owner" : owner, "repo": repo, "total_files": len(files),"files": files}

    
repository_service = RepositoryService()