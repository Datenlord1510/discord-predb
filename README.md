<p align="center">
<p align="center">
  <img src="https://i.ibb.co/cLH004G/523525354235.png"/>
</p>

# discord-predb
discord-predb is a Python tool built for Discord servers, announcing new releases for several release types. Its lightweight design optimizes storage usage by retaining only the latest information and has the minimum requirements by using Discord's webhook integration. The code leverages the xREL API to fetch release details.

## Update!
discord-predb now supports more release types!
- Windows
- Nintendo Switch
- Movies (*new*)
- TV shows (*new*)
- Anime (*new*)

## Features
- Customize the colors for your embedded messages!
- Toggle between EU and US time formats!
- Adjust the interval for new release checks!
- No fancy dependencies, only one external module!
- Stay up-to-date with the newest releases!

## Usage
- If needed, install the requests module using pip or pip3
- Add your Discord webhooks to the config.ini file
- Edit colors, time format and interval if needed
- Set the description mode to "True" if you want a short description of the release added to the message (the language will be **German**)
- Run test.py to check if everything is working. You should get a message to your configured webhooks.
- Run main.py


If you messed up the configuration file, simply run "create_default_config.py" to create a new one!

## Example
This is what a message looks like by default:
<p align="center">
  <img src="https://i.ibb.co/w66GgqG/eg.png"/>
</p>

## Disclaimer
This repo **does not** provide or link to pirated content. It only **informs** about such releases.
Some people asked if you risk your Discord server and acccount by running this repo.
Please read Discord's [Community Guidlines](https://discord.com/terms/guidelines-march-2022) and [Terms of Service](https://discord.com/terms) and decide for yourself.

## Documentation
[Discord API Reference](https://discordpy.readthedocs.io/en/stable/api.html)\
[xREL API](https://www.xrel.to/wiki/1681/API.html)
