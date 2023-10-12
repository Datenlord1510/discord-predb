from .APIHelper import APIHelper


class Comments(APIHelper):

    def __init__(self):
        self.comments_api = "https://api.xrel.to/v2/comments/"

    def get_comments(self, release_id, release_type="release", per_page=25,
                     page=1, response_format="json"):
        # release_type defaults to the Scene. Optional: "p2p_rls"
        if release_type != "release" or release_type != "p2p_rls":
            raise ValueError("Please use 'release' or 'p2p_rls' as "
                             "release_type.")
            return None

        api = f"{self.comments_api}get.{response_format}"
        params = {"id": release_id,
                  "type": release_type,
                  "per_page": per_page,
                  "page": page}
        return self.send_request(api, params, response_format)

    def add_comment(self, release_id, release_type, text="", ratings=None,
                    response_format="json"):
        # TODO: Needs OAUTH
        print("Currently NOT available!")
        return
        api = f"{self.comments_api}add.{response_format}"
        params = {"id": release_id,
                  "type": release_type,
                  "text": text,
                  "video_rating": ratings["video_rating"],
                  "audio_rating": ratings["audio_rating"]}
        return self.send_request(api, params, response_format, post=True)
