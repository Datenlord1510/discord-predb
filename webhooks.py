import requests
import logging

logger = logging.getLogger(__name__)


class Webhook:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send(self, message: str) -> bool:
        data = {"content": message}
        headers = {"Content-Type": "application/json"}

        response = requests.post(self.webhook_url, json=data, headers=headers)

        if response.status_code == 204:
            return True
        else:
            logger.warning("Failed to send message. Status code: "
                           f"{response.status_code}")
            return False

    def send_embed(self, embed) -> bool:
        data = {"embeds": [embed.data]}
        headers = {"Content-Type": "application/json"}

        response = requests.post(self.webhook_url, json=data, headers=headers)

        if response.status_code == 204:
            return True
        else:
            logger.warning("Failed to send embed. Status code: "
                           f"{response.status_code}")
            return False


class WebhookEmbed:
    def __init__(self):
        self.data = {}

    def set_title(self, title):
        self.data["title"] = title

    def set_description(self, description):
        self.data["description"] = description

    def set_url(self, url):
        self.data["url"] = url

    def set_color(self, color):
        self.data["color"] = color

    def set_thumbnail(self, url):
        self.data["thumbnail"] = {"url": url}

    def set_author(self, name, url=None, icon_url=None):
        author = {"name": name}
        if url:
            author["url"] = url
        if icon_url:
            author["icon_url"] = icon_url
        self.data["author"] = author

    def set_footer(self, text, icon_url=None):
        footer = {"text": text}
        if icon_url:
            footer["icon_url"] = icon_url
        self.data["footer"] = footer

    def add_field(self, name, value, inline=False):
        if "fields" not in self.data:
            self.data["fields"] = []
        field = {"name": name, "value": value, "inline": inline}
        self.data["fields"].append(field)
