import requests

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
