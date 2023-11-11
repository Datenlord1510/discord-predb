from .APIHelper import APIHelper


class P2P(APIHelper):

    def __init__(self):
        super().__init__()
        self.p2p_api = f"{self.base_api}p2p/"

    def get_releases(self, per_page=25, page=1, category_id=None,
                     group_id=None, ext_info_id=None, response_format="json"):
        api = f"{self.p2p_api}releases.{response_format}"
        params = {"category_id": category_id,
                  "group_id": group_id,
                  "ext_info_id": ext_info_id,
                  "per_page": per_page,
                  "page": page}
        return self.send_request(api, params, response_format)

    def get_categories(self, response_format="json"):
        api = f"{self.p2p_api}categories.{response_format}"
        return self.send_request(api, None, response_format)

    def get_rls_info(self, release_id=None, dirname=None,
                     response_format="json"):
        if not release_id and not dirname:
            print("You must provide either release_id or dirname.")
            return
        api = f"https://api.xrel.to/v2/p2p/rls_info.{response_format}"
        params = {"id": release_id,
                  "dirname": dirname}
        return self.send_request(api, params, response_format)
