import requests

class RequestHandler(object):
    """This class for handling all requests."""
    def __init__(self):
        pass

    def get_repo_req(self, req_url=None):
        res = {}
        try:
            response = requests.request("GET", req_url, headers = {}, data = {})
            res['data'] = {"repo": response.json(), "links": response.links}
            res["status"] = 200
            res['msg'] = 'success'
        except Exception as e:
            res["status"] = 500
            res['msg'] = 'Server error'
        finally:
            return res
