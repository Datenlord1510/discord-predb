from xrelmedia import xRELMedia


class Game(xRELMedia):
    def __init__(self):
        super().__init__()
        self.game_title = None
        self.indie_flag = False

    @classmethod
    def from_json(cls, data):
        indie_game_names = ["Indie-Spiele", "Wimmelbild-Spiele",
                            "Solitär-Spiele", "Puzzlespiele"]
        instance = super().from_json(data)
        if instance.ext_info_title in indie_game_names:
            instance.indie_flag = True
            if "-" in instance.dirname:
                split_index = instance.dirname.find("-")
                instance.game_title = instance.dirname[:split_index].replace(
                    ".", " ").replace("_", " ")
        else:
            instance.game_title = instance.ext_info_title

        return instance

    def to_embed(self):
        embed = super().to_embed()
        embed.add_field("Title", self.game_title)
        return embed
