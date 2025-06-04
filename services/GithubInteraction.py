import os
from github import Github, GithubException
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

class GitHubService:
    def __init__(self, token=None):
        self.github = Github(GITHUB_TOKEN)

    def get_repo(self, repo_url):
        try:
            repo_path = repo_url.replace("https://github.com/", "")
            if repo_path.endswith(".git"):
                repo_path = repo_path[:-4]
            return self.github.get_repo(repo_path)
        except GithubException as e:
            raise ValueError(f"Invalid repo URL or access denied: {e}")

    def get_contributors(self, repo):
        return repo.get_contributors()

    def get_commits(self, repo, contributor):
        return repo.get_commits(author=contributor)
    
    def get_languages(self, repo):
        print(repo.get_languages())
        return repo.get_languages()