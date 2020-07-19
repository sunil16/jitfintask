from .requests_handler import RequestHandler

class GitUtility(RequestHandler):
    """This class for handling git Api's ."""

    def get_repo_url(self, github_username = None):
        return "https://api.github.com/users/{}/repos?sort=created&direction=desc".format(github_username)

    def get_repo(self,github_username=None):
        if github_username is not None:
            return super().get_repo_req(self.get_repo_url(github_username))

    def get_next_repo(self, paging_url=None):
        if paging_url is not None:
            return super().get_repo_req(paging_url)
