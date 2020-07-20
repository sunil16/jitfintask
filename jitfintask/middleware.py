class CorsMiddleware(object):
    def process_response(self, req, resp):
        resp["Access-Control-Allow-Origin"] = "*"
        resp["Access-Control-Allow-Headers"] = "*"
        resp["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, DELETE"
        resp["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type, Origin, Authorization, Accept, Client-Security-Token, Accept-Encoding, X-Auth-Token, content-type"
        return resp
