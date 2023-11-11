from watchablemedia import WatchableMedia


class Show(WatchableMedia):
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

    def to_embed(self):
        embed = super().to_embed()
        if self.tv_season is not None and self.tv_episode is not None:
            embed.add_field("Season", self.tv_season)
            embed.add_field("Episode", self.tv_episode)
        return embed
