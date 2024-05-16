from .apihelper import APIHelper


class NFO(APIHelper):

    def __init__(self):
        super().__init__()
        self.nfo_api = f"{self.base_api}nfo/"

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
