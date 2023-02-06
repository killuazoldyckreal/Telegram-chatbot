import random 

def helptext():
    helptxt="""
/start : <i>Start the bot</i>
/help : <i>Shows all bot commands</i>
/gpt : <i>Talk with me all day long</i>
/insult name : <i>To insult the user named</i>
/trans 'language_code' Your sentence : <i>Translate your sentence in any language</i>
/langcodes : <i>To get all language codes</i>
/anime : <i>Get the list of all worth watching anime</i>
/meme subreddit_name : <i>Get memes from your subreddit. If subreddit left empty, memes will be posted from <b>memes</b> subreddit</i>
/sv video_name : <i>To download YouTube video</i>
/sa video_name : <i>To download YouTube audio</i>
/v youtube_link : <i>To download YouTube video</i>
/a youtube_link : <i>To download YouTube audio</i>
/i post/reel_link : <i>To download Instagram post/reel</i>
/ia insta_video/reel_link : <i>To download Instagram audio</i>
/r reddit_image_link : <i>To download Reddit image</i>
/rv reddit_video_link : <i>To download Reddit video</i>
/ra reddit_video_link : <i>To download Reddit audio</i>
/a spotify_song_link : <i>To download song from Spotify</i>
/t youtube_link : <i>To download YouTube video thumbnail</i>
/tos : <i>To read the bot terms of service and privacy policy</i>"""
    return helptxt

def sanime():
    doc = open('./anime.txt','rb')
    cap = """
🤗Here are some of the best anime of all time and they are not ranked so that you don't watch all the epic ones first but don't worry cause all these are worth watching anime. 
✅Some of them are ongoing but you can watch the rest of them until the new ones get completed.

🎏Some of them have mutiple seasons. So make sure to search for them cause I have only included the anime name in the given file.
"""
    return doc, cap

def langcodes():
    doc = open('./languagecodes.txt','rb')
    cap= "for custom language translation use command\n\n/trans 'language_code' Your sentence"
    return doc, cap
def review():
    with open("review.txt", "r") as f:
        line=f.readlines()
        f.close()
    n=''.join(line)
    return n
def update(txt):
    with open("anime.txt", "a") as f:
        f.write(f"{txt}\n")
        f.close()
def check():
    with open("anime.txt", "r") as f:
        line=f.readlines()
        f.close()
    return line[-5:]

#with open("yourfile.txt", "r") as f:
    #lines = f.readlines()
#with open("yourfile.txt", "w") as f:
    #for line in lines:
        #if line.strip("\n") != "nickname_to_delete":
            #f.write(line)
def tos():
    text="""
<u><b>Terms of Service</b></u>

The bot provides the following services to its users:
<i>
1. Hindi-English one liner insult dialogues against whosoever named in the command
2. Translation of any language to any language
3. Download of YouTube videos, video thumbnails and audio of the videos
4. Download of Instagram reels/posts and audio of the videos
5. Download any spotify song
6. Get a list of best animes of all time
</i>
<u><b>Privacy Policy</b></u>
<i>
The bot doesn't collect any sort of data except the data provided by the user intentionally to use the bot's services. This includes the social media links, translation data and names(for insult command). The bot doesn't store this data and dump it after the execution of the command.
</i>"""
    return text
def welcome():
    text="👋Hi,\nI am typically an insulter bot, but I also provide other cool services😎\n\nType /help for more commands"
    return text

def insult(num):
    if num==0:
        text="_Sorry mate, this command doesn't work in private chats_"
        return text
    elif num==1:
        text="Idiot bina naam ke kiski insult krunga, agli baar se dhyan se use krna command.\nPta nhi kaise kaise log use krte hai mujhe"
        return text
    elif num==2:
        text="bhai phle ja ache se paida hoke aa, tere bas ka nhi hai mujhe use krna. Gadhe naam to daal command ke aage jiski insult krni hai"
        return text

def insultdoc():
    with open('insults.txt') as f:
        lines = f.readlines()
        lines = random.choice(lines)
    return f, lines