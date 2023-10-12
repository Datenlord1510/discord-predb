import json
from datetime import datetime as dt


def timestamp_to_string(timestamp: int, time_format="EU") -> str:
    dt_object = dt.fromtimestamp(timestamp)
    if time_format == "EU":
        formatted_date = dt_object.strftime("%d.%m.%Y at %H:%M:%S")
    else:
        formatted_date = dt_object.strftime("%m/%d/%Y at %I:%M:%S %p")
    return formatted_date


def read_games_file(game_type: str) -> dict:
    try:
        with open(f"{game_type}.json", "r") as file:
            games_list = json.load(file)
    except FileNotFoundError:
        with open(f"{game_type}.json", "w") as file:
            pass
        games_list = {}
    return games_list


def write_games_file(game_type: str, json_data: dict) -> None:
    with open(f"{game_type}.json", "w") as file:
        json.dump(json_data, file, indent=4)
