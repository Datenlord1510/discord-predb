from watchablemedia import WatchableMedia


class Movie(WatchableMedia):
    def __init__(self):
        super().__init__()
        self.video_type = None
        self.audio_type = None

    @classmethod
    def from_json(cls, data):
        instance = super().from_json(data)
        instance.video_type = data.get("video_type")
        instance.audio_type = data.get("audio_type")

        return instance
