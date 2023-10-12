from .APIHelper import APIHelper


class User(APIHelper):

    def __init__(self):
        self.user_api = "https://api.xrel.to/v2/user/"

    def get_info(self, response_format="json"):
        # TODO: Needs OAUTH
        api = f"{self.user_api}.{response_format}"
        return self.send_request(api, None, response_format)
