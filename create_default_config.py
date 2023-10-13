import os


config_content = """[categories]
# Values must match xREL categories.
relevant_categories = WINDOWS, NSW

[webhooks]
WINDOWS =
NSW =

[colors]
# Windows color defaults to blue and NSW to red. Please use decimal color codes.
WINDOWS = 3447003
NSW = 15548997

[timeformat]
# Timeformat can be "EU" or "US".
# EU example: Released on 12.10.2023 at 15:50:57
# US example: Released on 10/12/2023 at 05:47:28 PM
timeformat = EU

[interval]
# The interval is set in seconds. Please do not push the API too much.
interval = 1200

[modes]
# Set description to "True" in order to add a section with a game description in German.
# Use "False" to turn the description off.
description = False
"""

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, 'config.ini')

with open(config_path, 'w') as config_file:
    config_file.write(config_content)
