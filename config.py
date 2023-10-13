import configparser
import sys


class Config:
    def __init__(self, config_file="config.ini"):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_relevant_categories(self) -> list:
        relevant_categories_str = self.config.get("categories",
                                                  "relevant_categories",
                                                  fallback="")
        relevant_categories = [category.strip() for category in
                               relevant_categories_str.split(",") if
                               category.strip()]
        return relevant_categories

    def get_webhook_for_category(self, category: str) -> str:
        return self.config.get("webhooks", category)

    def get_color_for_category(self, category: str) -> int:
        color_value = self.config.get("colors", category, fallback=None)
        return int(color_value) if color_value else 0

    def get_time_format(self) -> str:
        return self.config.get("timeformat", "timeformat")

    def get_interval(self) -> int:
        return int(self.config.get("interval", "interval"))

    def get_description_mode(self) -> str:
        return self.config.getboolean("modes", "description")

    def integrity_check(self) -> bool:
        sections = ["categories", "webhooks", "colors", "timeformat",
                    "interval", "modes"]

        for section in sections:
            if section not in self.config:
                sys.exit(f"Missing section {section}.")

        relevant_categories = self.get_relevant_categories()
        if not relevant_categories:
            sys.exit("You did not configure any relevant categories.")

        configured_webhooks = [self.get_webhook_for_category(category) for
                               category in relevant_categories]
        if not any(configured_webhooks):
            sys.exit("You did not configure any webhooks or forgot to "
                     "configure a webhook for a relevant category.")

        try:
            self.config.getboolean("modes", "description")
        except ValueError:
            sys.exit("Invalid error for description mode. Please use either "
                     "'True' or 'False'")
        return True
