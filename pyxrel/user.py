from .apihelper import APIHelper


class User(APIHelper):

    def __init__(self):
        super().__init__()
        self.user_api = f"{self.base_api}user/"

    def get_info(self, response_format="json"):
        # TODO: Needs OAUTH
        api = f"{self.user_api}.{response_format}"
        return self.send_request(api, None, response_format)
