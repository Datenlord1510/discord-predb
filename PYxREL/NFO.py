from .APIHelper import APIHelper


class NFO(APIHelper):

    def __init__(self):
        self.nfo_api = "https://api.xrel.to/v2/nfo/"

    def get_release(self, release_id: str, response_format="json"):
        # TODO: Needs OAUTH!
        api = f"{self.nfo_api}release.{response_format}"
        params = {"id": release_id}
        return self.send_request(api, params)

    def get_p2p_rls(self, release_id: str, response_format="json"):
        # TODO: Needs OAUTH!
        api = f"{self.nfo_api}p2p_rls.{response_format}"
        params = {"id": release_id}
        return self.send_request(api, params, response_format)
