import requests
from github import Github

class RequestHandler(object):
    """This class for handling all requests."""
    def __init__(self):
        self.top_follower = { 'followers': 0 }

    def get_repo_req(self, req_url=None):
        res = {}
        try:
            response = requests.request("GET", req_url, headers = {}, data = {})
            res['repository'] = {"repo": response.json(), "links": response.links}
            res["status"] = 200
            res['msg'] = 'success'
        except Exception as e:
            res["status"] = 500
            res['msg'] = 'Server error'
        finally:
            return res

    def get_follow_req(self, req_url=None):
        res = {}
        try:
            response = requests.request("GET", req_url, headers = {}, data = {})
            sorted_response = sorted(response.json(), key = lambda param: param['login'].lower()) # sorting followers by name
            self.get_highest_number_follower(sorted_response) # get top follower
            res['followers'] = {"followers": sorted_response, "links": response.links, "top_follower":self.top_follower}
            res["status"] = 200
            res['msg'] = 'success'

        except Exception as e:
            res["status"] = 500
            res['msg'] = 'Server error'
        finally:
            return res

    def get_total_followers(self,followers_url=None):
        try:
            if followers_url is not None:
                response = requests.request("GET", followers_url, headers = {}, data = {})
                current_follower = response.json()
                if current_follower.get('followers') > self.top_follower.get('followers'):
                    self.top_follower = current_follower
        except Exception as e:
            raise

    def get_highest_number_follower(self,total_followers=None):
        if len(total_followers):
            [self.get_total_followers(follower['url']) for follower in total_followers]

    def create_repos(self, repo_details=None):
        res ={}
        try:
            client_inst = self.login_github(repo_details.get('client_id'),repo_details.get('client_secret'))
            client_inst.get_user().create_repo(name=repo_details.get('name'), description=repo_details.get('description'), homepage= "https://github.com", private= False, has_issues= True, has_projects= True, has_wiki=True)
            res["status"] = 201
            res['msg'] = 'Repository {} successful created'.format(repo_details.get('name'))
        except Exception as e:
            res["status"] = 203
            res['msg'] = 'Error, repository {} not able to create'.format(repo_details.get('name'))
        finally:
            return res

    def login_github(self, client_id=None, client_secret=None):
        client_inst = None
        try:
            # using username and password
            client_inst = Github(client_id,client_secret)
        except Exception as e:
            raise
        finally:
            return client_inst
