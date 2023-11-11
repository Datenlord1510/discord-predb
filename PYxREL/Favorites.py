from .APIHelper import APIHelper


class Favorites(APIHelper):

    def __init__(self):
        super().__init__()
        self.favorites_api = f"{self.base_api}favs/"

    def get_lists(self, response_format="json"):
        # TODO: Needs OAUTH
        api = f"{self.favorites_api}lists.{response_format}"
        return self.send_request(api, None, response_format)

    def get_list_entries(self, fav_list_id, get_releases=False,
                         response_format="json"):
        # TODO: Needs OAUTH
        api = f"{self.favorites_api}list_enties.{response_format}"
        params = {"id": fav_list_id,
                  "get_releases": get_releases}
        return self.send_request(api, params, response_format)

    def add_entry(self, fav_list_id, ext_info_id, response_format="json"):
        # TODO: Needs OAUTH
        api = f"{self.favorites_api}list_addentry.{response_format}"
        params = {"id": fav_list_id,
                  "ext_info_id": ext_info_id}
        return self.send_request(api, params, response_format, post=True)

    def del_entry(self, fav_list_id, ext_info_id, response_format="json"):
        # TODO: Needs OAUTH
        api = f"{self.favorites_api}list_delentry.{response_format}"
        params = {"id": fav_list_id,
                  "ext_info_id": ext_info_id}
        return self.send_request(api, params, response_format, post=True)

    def mark_read(self, fav_list_id, release_id, release_type="release",
                  response_format="json"):
        # TODO: Needs OAUTH
        # release_type defaults to the Scene. Optional: "p2p_rls".
        if release_type != "release" or release_type != "p2p_rls":
            print("Please use 'release' or 'p2p_rls' as release_type.")
            return

        api = f"{self.favorites_api}list_markread.{response_format}"
        params = {"id": fav_list_id,
                  "release_id": release_id,
                  "type": release_type}
        return self.send_request(api, params, response_format, post=True)
