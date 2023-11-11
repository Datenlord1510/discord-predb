import json
from datetime import datetime as dt


def timestamp_to_string(timestamp: int, time_format="EU") -> str:
    dt_object = dt.fromtimestamp(timestamp)
    if time_format == "EU":
        formatted_date = dt_object.strftime("%d.%m.%Y at %H:%M:%S")
    else:
        formatted_date = dt_object.strftime("%m/%d/%Y at %I:%M:%S %p")
    return formatted_date


def read_cache_file(category: str) -> dict:
    try:
        with open(f"{category}.json", "r") as file:
            cache = json.load(file)
    except FileNotFoundError:
        with open(f"{category}.json", "w") as file:
            pass
        cache = {}
    return cache


def write_cache_file(category: str, json_data: dict) -> None:
    with open(f"{category}.json", "w") as file:
        json.dump(json_data, file, indent=4)
