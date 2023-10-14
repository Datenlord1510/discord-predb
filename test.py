from PYxREL import xREL
from webhooks import Webhook, WebhookEmbed
from config import Config
import sys
from utils import timestamp_to_string
from logger import setup_logger

logger = setup_logger(__name__, "test.log")


if __name__ == "__main__":

    config = Config()
    config.integrity_check()
    logger.info("Integrity check successful. Config file should be "
                "configured correctly.")

    relevant_categories = config.get_relevant_categories()

    interval = config.get_interval()
    timeformat = config.get_time_format()
    description_mode = config.get_description_mode()

    windows_url = config.get_webhook_for_category("WINDOWS")
    nsw_url = config.get_webhook_for_category("NSW")

    if windows_url:
        windows_hook = Webhook(windows_url)
        windows_hook_color = config.get_color_for_category("WINDOWS")
        logger.info("Found webhook for Windows.")
    if nsw_url:
        nsw_hook = Webhook(nsw_url)
        nsw_hook_color = config.get_color_for_category("NSW")
        logger.info("Found webhook for Nintendo Switch.")

    indie_game_names = ["Indie-Spiele", "Wimmelbild-Spiele"]
    xrel = xREL()

    for category in relevant_categories:
        response = xrel.Release.browse_category(category)
        if response is None:
            logger.warning("Could not get a response from xREL.")
            sys.exit("Could not get a response from xREL. Please check "
                     "your internet connection or xREL's status.")

        example = response.get("list")[0]
        indie_flag = False
        embed = WebhookEmbed()
        rls_title = example["dirname"]
        embed.set_title(rls_title)
        rls_time = timestamp_to_string(example["time"], timeformat)
        embed.set_footer(f"Released on {rls_time}")
        game_title = example["ext_info"]["title"]

        if game_title in indie_game_names:
            indie_flag = True
            if "-" in rls_title:
                split_index = rls_title.find("-")
                game_title = rls_title[:split_index].replace(
                    ".", " ").replace("_", " ")

        embed.add_field("Game title", game_title)
        embed.add_field("Group", example["group_name"])
        embed.add_field("xREL", example["link_href"])

        try:
            size = example["size"]["number"]
            unit = example["size"]["unit"]
            size_string = f"{size} {unit}"
            embed.add_field("Size", f"{size_string}")
        except KeyError:
            pass

        try:
            embed.add_field("Rating", str(example["ext_info"]
                                          ["rating"]) + "/10")
        except KeyError:
            pass

        if indie_flag is False:
            ext_info_id = example["ext_info"]["id"]
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

        if windows_url and category == "WINDOWS":
            embed.set_color(windows_hook_color)
            windows_hook.send_embed(embed)
            logger.info("Sent test message for new release: "
                        f"{rls_title}")
        elif nsw_url and category == "NSW":
            embed.set_color(nsw_hook_color)
            nsw_hook.send_embed(embed)
            logger.info("Sent test message for new release: "
                        f"{rls_title}")

        logger.info("Test passed. You should have received a message on your "
                    "configured webhooks.")
