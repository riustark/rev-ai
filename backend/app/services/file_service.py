import base64

from app.services.github_service import GitHubService

class FileService:

    def __init__(self):
        self.github_service = GitHubService()

    def get_file_content(self,owner,repo,path):

        file_data =self.github_service.get_file(owner,repo,path,)
        content = base64.b64decode(file_data["content"]).decode("utf-8")

        return{
            "path" : path,
            "content": content,
        }
    


file_service=FileService()