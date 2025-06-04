from services.GithubInteraction import GitHubService

class RepoValidator:
    def __init__(self):
        self.github = GitHubService()

    def validate_repo(self, repo_url):
        repo = self.github.get_repo(repo_url)
        return {
            "creator": repo.owner.login,
            "contributors": self._get_contributor_stats(repo),
            "languages": self.github.get_languages(repo),
            "open_issues": self.github.get_issues_open(repo),
            "closed_issues": self.github.get_issues_closed(repo),
            "open_prs": self.github.get_pulls_open(repo),
            "closed_prs": self.github.get_pulls_closed(repo)
        }

    def _get_contributor_stats(self, repo):
        contributors = self.github.get_contributors(repo)
        return [
            {
                "username": c.login,
                "commits": self.github.get_commits(repo, c).totalCount,
                "commit_details": [commit.commit.message for commit in self.github.get_commits(repo, c)]
            }
            for c in contributors
        ]