from .APIHelper import APIHelper


class Search(APIHelper):

    def __init__(self):
        super().__init__()
        self.search_api = f"{self.base_api}search/"

    def get_releases(self, keyword, scene=True, p2p=False, limit=25,
                     response_format="json"):
        api = f"{self.search_api}releases.{response_format}"
        if scene is False and p2p is False:
            p2p = True
        params = {"q": keyword,
                  "scene": scene,
                  "p2p": p2p,
                  "limit": limit}
        return self.send_request(api, params, response_format)

    def get_ext_info(self, keyword, category=None, limit=25,
                     response_format="json"):
        api = f"{self.search_api}ext_info.{response_format}"
        params = {"q": keyword,
                  "type": category,
                  "limit": limit}
        return self.send_request(api, params, response_format)
