import requests


class APIHelper:

    def __init__(self):
        self.base_api = "https://api.xrel.to/v2/"

    def send_request(self, api_url: str, parameters: dict, response_format: str,
                     post=False):
        try:
            if post is False:
                response = requests.get(api_url, params=parameters)
            elif post is True:
                response = requests.post(api_url, params=parameters)
            else:
                raise ValueError("Invalid value for the post flag.")

            try:
                if response_format == "json":
                    return response.json()
                elif response_format == "xml":
                    return response.content
            except Exception as val_error:
                print("Invalid response format: ", val_error)
                return None

        except requests.RequestException as req_error:
            print("Request failed: ", req_error)
            return None
