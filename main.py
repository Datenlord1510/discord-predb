import logging
import sys
import os
import time
from PYxREL import xREL
from webhooks import Webhook, WebhookEmbed
from config import Config
from utils import write_games_file, read_games_file, timestamp_to_string

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('LOGS.log')
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - "
                              "%(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)


if __name__ == "__main__":

    if not os.path.exists("config.ini"):
        sys.exit("Could not find config.ini")

    config = Config()
    integrity = config.integrity_check()

    interval = config.get_interval()
    timeformat = config.get_time_format()
    description_mode = config.get_description_mode()

    windows_url = config.get_webhook_for_category("WINDOWS")
    nsw_url = config.get_webhook_for_category("NSW")

    if windows_url:
        windows_hook = Webhook(windows_url)
        windows_hook_color = config.get_color_for_category("WINDOWS")
    if nsw_url:
        nsw_hook = Webhook(nsw_url)
        nsw_hook_color = config.get_color_for_category("NSW")

    relevant_categories = config.get_relevant_categories()

    indie_game_names = ["Indie-Spiele", "Wimmelbild-Spiele"]
    xrel = xREL()
    logger.info("Started Discord PreDB.")

    while True:
        for cat in relevant_categories:
            response = None
            while not response:
                response = xrel.Release.browse_category(cat)
                if not response:
                    logger.warning("Did not receive a response from xREL.")
                    time.sleep(interval)

            response = response.get("list")
            cat_list = read_games_file(cat)
            if not cat_list:
                write_games_file(cat, response)
                logger.info(f"No game lists found for {cat}. "
                            "Assuming initial scan.")

            elif response != cat_list:
                write_games_file(cat, response)
                rls_id_list = [rls.get("id") for rls in cat_list]
                new_releases = [game for game in response if game.get("id")
                                not in rls_id_list]
                for rls in new_releases:
                    indie_flag = False
                    embed = WebhookEmbed()
                    rls_title = rls["dirname"]
                    embed.set_title(rls_title)
                    rls_time = timestamp_to_string(rls["time"], timeformat)
                    embed.set_footer(f"Released on {rls_time}")
                    game_title = rls["ext_info"]["title"]

                    if game_title in indie_game_names:
                        indie_flag = True
                        if "-" in rls_title:
                            split_index = rls_title.find("-")
                            game_title = rls_title[:split_index].replace(
                                ".", " ").replace("_", " ")

                    embed.add_field("Game title", game_title)
                    embed.add_field("Group", rls["group_name"])
                    embed.add_field("xREL", rls["link_href"])

                    try:
                        size = rls["size"]["number"]
                        unit = rls["size"]["unit"]
                        size_string = f"{size} {unit}"
                        embed.add_field("Size", f"{size_string}")
                    except KeyError:
                        pass

                    try:
                        embed.add_field("Rating", str(rls["ext_info"]
                                                      ["rating"]) + "/10")
                    except KeyError:
                        pass

                    if indie_flag is False:
                        ext_info_id = rls["ext_info"]["id"]
                        ext_response = xrel.ExtInfo.get_info(ext_info_id)

                        try:
                            embed.set_thumbnail(ext_response["cover_url"])
                        except KeyError:
                            pass

                        if description_mode is True:
                            try:
                                plot = ext_response["externals"][0]["plot"]
                                embed.add_field("Description", plot)
                            except KeyError:
                                pass

                    if windows_url and cat == "WINDOWS":
                        embed.set_color(windows_hook_color)
                        windows_hook.send_embed(embed)
                    elif nsw_url and cat == "NSW":
                        embed.set_color(nsw_hook_color)
                        nsw_hook.send_embed(embed)
                    logger.info(f"Sent message for new release: {rls_title}")
        time.sleep(interval)
