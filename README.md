<p align="center">
  <img src="https://i.ibb.co/FxBt6zv/sans-github-2-70.png"/>
</p>

# discord-predb
discord-predb is a Python tool built for Discord servers, announcing new releases for Windows and Nintendo Switch. Its lightweight design optimizes storage usage by retaining only the latest information and has the minimum requirements by using Discord's webhook integration. The code is modifiable and leverages the xREL API to fetch release details.

## Features
- Customize the color for your embedded messages!
- Toggle between EU and US time formats!
- Adjust the interval for new release checks!
- No fancy dependencies, only one external dependency!
- Stay up-to-date with the newest games!

## Usage
- Install the requests module using pip or pip3.
- Add your discord webhooks to the the config.ini file
- Edit colors, time format and interval if needed.
- Set the description mode to "True" if you want a short description of the game added to the message (the language will be **German**)
- Run main.py


In case you are **not** interested in releases for the Windows or Nintendo Switch platform, simply remove the platform from "relevant_categories" in the config.ini file.
If you messed up the configuration file, simply run "create_default_config.py" to create a new one!

## Example
This is what a message would look like by default:
<p align="center">
  <img src="https://i.ibb.co/w66GgqG/eg.png"/>
</p>

## Documentation
[Discord API Reference](https://discordpy.readthedocs.io/en/stable/api.html)\
[xREL API](https://www.xrel.to/wiki/1681/API.html)
