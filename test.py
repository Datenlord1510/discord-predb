import sys
import os
import time
from PYxREL import xREL
from discord_webhooks import Webhook
from config import Config
from utils import timestamp_to_string
from logger import setup_logger
from game import Game
from movies import Movies
from show import Show

logger = setup_logger(__name__, "test.log")


if __name__ == "__main__":

    if not os.path.exists("config.ini"):
        sys.exit("Could not find config.ini. You can run the "
                 "create_default_config.py and configure it.")

    config = Config()
    config.integrity_check()
    logger.info("Integrity check successful. Config file should be "
                "configured correctly.")

    interval = config.get_interval()
    timeformat = config.get_time_format()
    description_modes = config.get_description_modes()

    webhooks = {}
    for category, url in config.get_webhooks():
        webhooks[category] = Webhook(url)

    xrel = xREL()
    logger.info("Started test run.")

    for category in webhooks:
        response = None
        while not response:
            response = xrel.Release.browse_category(category)
            if not response:
                logger.warning("Did not receive a response from xREL.")
                time.sleep(interval)

        response = response.get("list")
        test_rls = response[0]

        if category == "windows" or category == "nsw":
            instance = Game.from_json(test_rls)
        elif category == "movies":
            instance = Movies.from_json(test_rls)
        elif category == "tv" or category == "anime":
            instance = Show.from_json(test_rls)
        else:
            logger.info(f"Found unknown category: {category}")
            continue

        formatted_time = timestamp_to_string(instance.time_unix,
                                             time_format=timeformat)
        embed_msg = instance.to_embed()
        embed_msg.set_color(config.get_color_for_category(category))
        embed_msg.set_footer(formatted_time)

        try:
            ext_response = xrel.ExtInfo.get_info(instance.ext_info_id)
            embed_msg.set_thumbnail(ext_response["cover_url"])
        except KeyError:
            pass

        if description_modes[category] is True:
            try:
                plot = ext_response["externals"][0]["plot"]
                embed_msg.add_field("Description", plot)
            except KeyError:
                pass

        webhooks[category].send_embed(embed_msg)
        logger.info("Test passed. You should have received a message on your "
                    "configured webhooks.")
