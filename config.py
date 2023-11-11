import configparser
import sys


class Config:
    def __init__(self, config_file="config.ini"):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_webhooks(self):
        webhooks = []
        for category, url in self.config.items("webhooks"):
            if url != "":
                webhooks.append((category.strip(), url.strip()))
        return webhooks

    def get_webhook_for_category(self, category: str) -> str:
        return self.config.get("webhooks", category)

    def get_color_for_category(self, category: str) -> int:
        color_value = self.config.get("colors", category, fallback=None)
        return int(color_value) if color_value else 0

    def get_time_format(self) -> str:
        return self.config.get("timeformat", "timeformat")

    def get_interval(self) -> int:
        return int(self.config.get("interval", "interval"))

    def get_description_mode(self, category):
        return self.config.getboolean("modes", category)

    def get_description_modes(self):
        modes = {}
        for category, mode in self.config.items("modes"):
            modes[category] = self.get_description_mode(category)
        return modes

    def integrity_check(self):
        sections = ["webhooks", "colors", "timeformat", "interval", "modes"]

        for section in sections:
            if section not in self.config:
                sys.exit(f"Missing section {section}.")

        if not any(self.get_webhooks()):
            sys.exit("You did not configure any webhooks.")
