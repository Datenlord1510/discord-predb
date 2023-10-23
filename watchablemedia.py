from xrelmedia import xRELMedia


class WatchableMedia(xRELMedia):
    def __init__(self):
        super().__init__()
        self.imdb_id = None
        self.imdb_link = None

    @classmethod
    def from_json(cls, data):
        instance = super().from_json(data)
        if "ext_info" in data:
            ext_info = data.get("ext_info")
            imdb = ext_info.get("uris", [None])[0]
            if imdb is not None:
                instance.imdb_id = imdb.split(":")[1]
                instance.imdb_link = f"https://www.imdb.com/title/{instance.imdb_id}/"

        return instance
