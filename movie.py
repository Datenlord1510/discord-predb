
class Movie:
    def __init__(self):
        self.xrel_id = None
        self.dirname = None
        self.rls_link_href = None
        self.time_unix = None
        self.group_name = None
        self.size_number = None
        self.size_unit = None
        self.video_type = None
        self.audio_type = None
        self.type = None
        self.ext_info_id = None
        self.ext_info_title = None
        self.ext_info_href = None
        self.imdb_id = None
        self.imdb_link = None
        self.rating = None
        self.num_ratings = None

    @classmethod
    def from_json(cls, data):
        instance = cls()
        instance.xrel_id = data["id"]
        instance.dirname = data["dirname"]
        instance.rls_link_href = data["link_href"]
        instance.time_unix = data["time"]
        instance.group_name = data["group_name"]
        instance.size_number = data["size"]["number"]
        instance.size_unit = data["size"]["unit"]
        instance.video_type = data["video_type"]
        instance.audio_type = data["audio_type"]

        if "ext_info" in data:
            ext_info = data.get("ext_info")
            instance.type = ext_info.get("type")
            instance.ext_info_id = ext_info.get("id")
            instance.ext_info_title = ext_info.get("title")
            instance.ext_info_href = ext_info.get("link_href")
            imdb = ext_info.get("uris", [None])[0]
            if imdb is not None:
                instance.imdb_id = imdb.split(":")[1]
                instance.imdb_link = f"https://www.imdb.com/title/{instance.imdb_id}/"
            instance.rating = ext_info.get("rating")
            instance.num_ratings = ext_info.get("num_ratings")

        return instance
