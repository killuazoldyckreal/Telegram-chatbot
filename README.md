# Telegram-chatbot
Telegram bot with some awesome commands

## Installation
**Python 3.8 or higher is required**

To install the required library, you can just run the following command:

```sh
pip install -r requirements.txt
```

## Usage
> create a file and rename it to `.env` and add your telegram bot token and openai token inside it like this:

```
Token = "Your Telegram bot token here"
otoken = "Your openai API key here"
```

## Available Commands

- `/start` : Start the bot
- `/help` : Shows all bot commands
- `/gpt` : Talk with me all day long
- `/trans 'language_code' your_sentence` : Translate your sentence in any language
- `/langcodes` : To get all language codes
- `/anime` : Get the list of all worth watching anime
- `/meme subreddit_name` : Get memes from your subreddit. If subreddit left empty, memes will be posted from memes subreddit
- `/sv video_name` : To download YouTube video
- `/sa video_name` : To download YouTube audio
- `/v youtube_link` : To download YouTube video
- `/a youtube_link` : To download YouTube audio
- `/i post/reel_link` : To download Instagram post/reel
- `/ia insta_video/reel_link` : To download Instagram audio
- `/r reddit_image_link` : To download Reddit image
- `/rv reddit_video_link` : To download Reddit video
- `/ra reddit_video_link` : To download Reddit audio
- `/a spotify_song_link` : To download song from Spotify
- `/t youtube_link` : To download YouTube video thumbnail
- `/tos` : To read the bot terms of service and privacy policy
