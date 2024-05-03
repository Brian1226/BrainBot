# BrainBot

## About
BrainBot is a Discord bot designed to bring entertainment and fun to your server. With a variety of commands, BrainBot allows you to access different APIs to fetch advice, memes, activities, text overlays, pickup lines, translations, and many more! Programmed with Python, and utilized libraries like Discord.py and Requests.

## Getting Started
1. Install these (preferably the latest versions)
   ```bash
   python3
   pip3
   ```
2. Clone the repository
   ```bash
   https://github.com/Brian1226/BrainBot.git
   ```
3. Install all dependencies
   ```bash
   pip3 install -r requirements.txt
   ```
4. In `BrainBot.py`, replace "BOT_TOKEN" with your own
   ```python
   client.run(os.getenv("BOT_TOKEN"))
   ```
5. Run the application
   ```bash
   python3 BrainBot.py
   ```

## Commands

### Returning an Image
- !jail or !jail `member`
- !hue `degree` or !hue `degree` `member`
- !sadcat `text`
- !drake `text1` | `text2`
- !alert `text`
- !grave or !grave `member`
- !npc `text1` | `text2`
- !sign `text`
- !carreverse `text`

### Returning a Message
- !hello
- !pickuplines
- !dm `member` `message`
- !joke
- !wyr
- !translate `lang` `text`
- !_8ball `msg`
- !affirmation
- !advice
- !activity

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
