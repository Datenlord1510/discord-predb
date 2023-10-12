from .APIHelper import APIHelper


class ExtInfo(APIHelper):

    def __init__(self):
        self.ext_info_api = "https://api.xrel.to/v2/ext_info/"
        self.calendar_api = "https://api.xrel.to/v2/calendar/upcoming"

    def get_upcoming(self, country="de", response_format="json"):
        api = f"{self.calendar_api}.{response_format}"
        params = {"country": country}
        return self.send_request(api, params, response_format)

    def get_info(self, ext_info_id: str, response_format="json"):
        api = f"{self.ext_info_api}info.{response_format}"
        params = {"id": ext_info_id}
        return self.send_request(api, params, response_format)

    def get_media(self, ext_info_id: str, response_format="json"):
        api = f"{self.ext_info_api}media.{response_format}"
        params = {"id": ext_info_id}
        return self.send_request(api, params, response_format)

    def rate(self, ext_info_id: str, rating, response_format="json"):
        # TODO: Needs OAUTH!
        api = f"{self.ext_info_api}rate.{response_format}"
        params = {"id": ext_info_id,
                  "rating": rating}
        return self.send_request(api, params, response_format, post=True)
