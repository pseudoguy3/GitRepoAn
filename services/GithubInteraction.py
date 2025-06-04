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
    
    def get_issues(self, repo):
        issues = repo.get_issues(state='all')
        if issues:
            for issue in issues:
                print(f"Issue #{issue.number} - {issue.title}")
                print(f"State: {issue.state}")
                print(f"Author: {issue.user.login}")
                print(f"Created at: {issue.created_at}")
                print(f"Body: {issue.body}")
                print("-" * 50)
                print("-------------------------------")
        else:
            print("No issues found in the repository.")
        return repo.get_issues(state='all')
    

    def get_pulls_open(self, repo):
        return repo.get_pulls(state = 'open')
    
    def get_pulls_closed(self, repo):
        return repo.get_pulls(state = 'closed')