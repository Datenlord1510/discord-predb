from movie import Movie


class Show(Movie):
    def __init__(self):
        super().__init__()
        self.tv_season = None
        self.tv_episode = None

    @classmethod
    def from_json(cls, data):
        instance = super().from_json(data)
        instance.tv_season = data.get("tv_season")
        instance.tv_episode = data.get("tv_episode")
        return instance
