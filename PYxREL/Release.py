from .APIHelper import APIHelper


class Release(APIHelper):

    def __init__(self):
        self.release_api = "https://api.xrel.to/v2/release/"

    def get_info(self, release_id=None, dirname=None, response_format="json"):
        if not release_id and not dirname:
            print("You must provide either release_id or dirname.")
            return
        params = {"id": release_id,
                  "dirname": dirname}
        api = f"{self.release_api}info.{response_format}"
        return self.send_request(api, params, response_format)

    def get_latest(self, archive=None, per_page=25, page=1, filter_id=None,
                   response_format="json"):
        api = f"{self.release_api}latest.{response_format}"
        params = {"archive": archive,
                  "per_page": per_page,
                  "page": page,
                  "filter": filter_id}
        return self.send_request(api, params, response_format)

    def get_categories(self, response_format="json"):
        api = f"{self.release_api}categories.{response_format}"
        return self.send_request(api, None, response_format)

    def browse_category(self, category_name: str, ext_info_type=None,
                        per_page=25, page=1, response_format="json"):
        api = f"{self.release_api}browse_category.{response_format}"
        params = {"category_name": category_name,
                  "ext_info_type": ext_info_type,
                  "per_page": per_page,
                  "page": page}
        return self.send_request(api, params, response_format)

    def get_ext_info(self, ext_info_id: str, per_page=25,
                     response_format="json"):
        api = f"https://api.xrel.to/v2/release/ext_info.{response_format}"
        params = {"id": ext_info_id,
                  "per_page": per_page}
        return self.send_request(api, params, response_format)

    def get_filters(self, response_format="json"):
        api = f"https://api.xrel.to/v2/release/filters.{response_format}"
        return self.send_request(api, None, response_format)

    def addproof(self):
        doc_url = "https://www.xrel.to/wiki/6444/api-release-addproof.html"
        print("This method is currently NOT available.")
        print(f"Please see {doc_url} for further information.")
