from helpers.helper import helptext, sanime, langcodes, tos, welcome
from helpers.trans import translates
from helpers.dyoutube import sendvideo
from helpers.ytsearch import searchyt, searchaudio
from helpers.reddit import rvideo, raudio, rimage, rmeme
from helpers.daudio import sendaudio
from helpers.thumbnail import sendimage
from helpers.dinsta import ipost, iaudio
import os, keep_alive
import telebot
import traceback
import requests
import json
import random
import helpers.revopenai
from dotenv import load_dotenv
load_dotenv()
# Set a minimum time between API requests
MIN_REQUEST_INTERVAL = 5
last_request_time = 0
keep_alive.keep_alive()

def main():
    token = os.getenv("Token")                              #Enter your telegram bot token which you got from father bot in telegram
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['tos'])
    def termsofservice(message):
        text = tos()
        print(message.chat.id)
        bot.send_message(message.chat.id, text=text, parse_mode='HTML')

    @bot.message_handler(commands=['i'])
    def sendinstaphoto(message):
        try:
            path, rpath, text = ipost(message.text)
            if text == 0:
                if ".mp4" in rpath:
                    bot.send_chat_action(chat_id=message.chat.id,
                                         action='upload_video')
                    bot.send_video(message.chat.id, path, supports_streaming=True)
                    path.close()
                    if os.path.isfile(rpath):
                        os.remove(rpath)
                else:
                    bot.send_chat_action(chat_id=message.chat.id,
                                         action='upload_photo')
                    bot.send_photo(message.chat.id, photo=path)
                    path.close()
                    if os.path.isfile(rpath):
                        os.remove(rpath)
            else:
                bot.send_message(message.chat.id, text=text)
        except:
            traceback.print_exc()
            bot.send_message(message.chat.id, text="Sorry, this command isn't working right now!")
    @bot.message_handler(commands=['ia'])
    def instaaudio(message):
        path, rpath, text = iaudio(message.text)
        if text == 0:
            bot.send_chat_action(chat_id=message.chat.id,
                                 action='upload_audio')
            bot.send_audio(message.chat.id, path)
            path.close()
            if os.path.isfile(rpath):
                os.remove(rpath)
        else:
            bot.send_message(message.chat.id, text=text)

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        text = welcome()
        bot.reply_to(message, text=text, parse_mode='markdownv2')

    @bot.message_handler(commands=['help'])
    def sendhelp(message):
        helptxt = helptext()
        bot.reply_to(message, helptxt, parse_mode='HTML')

    @bot.message_handler(commands=['anime'])
    def sendanime(message):
        doc, cap = sanime()
        bot.send_document(message.chat.id, doc, caption=cap)
        doc.close()

    @bot.message_handler(commands=['langcodes'])
    def langcode(message):
        doc, cap = langcodes()
        bot.send_document(message.chat.id, doc, caption=cap)
        doc.close()

    @bot.message_handler(commands=['trans'])
    def translats(message):
        text = translates(message.text)
        bot.send_message(message.chat.id, text=text)

    @bot.message_handler(commands=['rv'])
    def redditvideo(message):
        try:
            data = message.text
            data = data.split(" ", 1)
            yurl = data[1]
            path, rpath, text = rvideo(yurl)
            if text == 0:
                bot.send_chat_action(chat_id=message.chat.id,
                                     action='upload_video')
                bot.send_video(message.chat.id, path, supports_streaming=True)
                path.close()
                if os.path.isfile(rpath):
                    os.remove(rpath)
            else:
                bot.send_message(message.chat.id, text=text)
        except:
            traceback.print_exc()
    @bot.message_handler(commands=['meme'])
    def redditmeme(message):
        try:
            data = message.text
            data = data.split(" ", 1)
            if len(data)==1:
                subreddit="memes"
            else:
                subreddit = data[1].replace(" ", "")
            if subreddit!="":
                url = f"https://www.reddit.com/r/{subreddit}/random/.json"
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
                response = requests.get(url, headers=headers)
                try:
                    data = json.loads(response.text)
                    if data[0]["kind"] == "Listing":
                        if data[0]["data"]["children"]==[]:
                            bot.send_message(message.chat.id, text="No posts found!")
                        else:
                            random_post = data[0]["data"]["children"][0]["data"]
                            url = random_post["url"]
                            caption = random_post["title"]
                            try:
                                path, rpath, text = rmeme(url)
                                if text == 0:
                                    bot.send_chat_action(chat_id=message.chat.id,
                                                         action='upload_video')
                                    bot.send_video(message.chat.id, path, supports_streaming=True,caption=caption)
                                    path.close()
                                    if os.path.isfile(rpath):
                                        os.remove(rpath)
                                elif text == 1:
                                    try:
                                        bot.send_chat_action(chat_id=message.chat.id,
                                                             action='upload_photo')
                                        bot.send_photo(message.chat.id, path,caption=caption)
                                        path.close()
                                        if os.path.isfile(rpath):
                                            os.remove(rpath)
                                    except Exception as e:
                                        print(e)
                                        bot.send_message(message.chat.id,
                                                         text="File size exceeded!")
                                else:
                                    bot.send_message(message.chat.id, text=text)
                            except KeyError:
                                bot.send_message(message.chat.id, text="No posts found!")
                            except:
                                traceback.print_exc()
                                bot.send_message(message.chat.id, text="Some error occured while fetching post!")
                    else:
                        bot.send_message(message.chat.id, text="Subreddit doesn't exist!")
                except:
                    traceback.print_exc()
                    bot.send_message(message.chat.id, text="Subreddit doesn't exist!")
            else:
                path, rpath, text = rmeme('memes')
                if text == 0:
                    bot.send_chat_action(chat_id=message.chat.id,
                                         action='upload_video')
                    bot.send_video(message.chat.id, path, supports_streaming=True)
                    path.close()
                    if os.path.isfile(rpath):
                        os.remove(rpath)
                elif text == 1:
                    try:
                        bot.send_chat_action(chat_id=message.chat.id,
                                             action='upload_photo')
                        bot.send_photo(message.chat.id, path)
                        path.close()
                        if os.path.isfile(rpath):
                            os.remove(rpath)
                    except Exception as e:
                        print(e)
                        bot.send_message(message.chat.id,
                                         text="File size exceeded!")
                else:
                    bot.send_message(message.chat.id, text=text)
        except:
            traceback.print_exc()
    @bot.message_handler(commands=['r'])
    def redditpost(message):
        try:
            data = message.text
            data = data.split(" ", 1)
            yurl = data[1]
            path, rpath, text = rimage(yurl)
            if text == 0:
                try:
                    bot.send_chat_action(chat_id=message.chat.id,
                                         action='upload_photo')
                    bot.send_photo(message.chat.id, path)
                    path.close()
                    if os.path.isfile(rpath):
                        os.remove(rpath)
                except Exception as e:
                    print(e)
                    bot.send_message(message.chat.id, text="File size exceeded!")
            else:
                bot.send_message(message.chat.id, text=text)
        except:
            traceback.print_exc()
            
    @bot.message_handler(commands=['v'])
    def sendvideos(message):
        data = message.text
        data = data.split(" ", 1)
        yurl = data[1]
        path, rpath, text = sendvideo(yurl)
        if text == 0:
            try:
                bot.send_chat_action(chat_id=message.chat.id,
                                     action='upload_video')
                bot.send_video(message.chat.id, path, supports_streaming=True)
                path.close()
                if os.path.isfile(rpath):
                    os.remove(rpath)
            except Exception as e:
                print(e)
                bot.send_message(message.chat.id, text="File size exceeded!")
        else:
            bot.send_message(message.chat.id, text=text)

    @bot.message_handler(commands=['sv'])
    def searchvideos(message):
        try:
            data = message.text
            data = data.split(" ", 1)
            yurl = data[1]
            path, rpath, text = searchyt(yurl)
            print("Path: ", path)
            print("Rpath: ", rpath)
            if text == 0:
                bot.send_chat_action(chat_id=message.chat.id,
                                     action='upload_video')
                bot.send_video(message.chat.id, path, supports_streaming=True)
                path.close()
                if os.path.isfile(rpath):
                    os.remove(rpath)
            else:
                bot.send_message(message.chat.id, text=text)
        except TypeError:
            bot.send_message(message.chat.id, "Sorry video not Found")

    @bot.message_handler(commands=['sa'])
    def searchaudios(message):
        try:
            data = message.text
            data = data.split(" ", 1)
            yurl = data[1]
            path, rpath, text = searchaudio(yurl)
            print("Path: ", path)
            print("Rpath: ", rpath)
            if text == 0:
                bot.send_chat_action(chat_id=message.chat.id,
                                     action='upload_audio')
                bot.send_audio(
                    message.chat.id,
                    audio=path,
                    title=yurl,
                )
                path.close()
                if os.path.isfile(rpath):
                    os.remove(rpath)
            else:
                bot.send_message(message.chat.id, text=text)
        except TypeError:
            bot.send_message(message.chat.id, "Sorry audio not Found")

    @bot.message_handler(commands=['ra'])
    def redditaudio(message):
        data = message.text
        data = data.split(" ", 1)
        yurl = data[1]
        path, rpath, text = raudio(yurl)
        if text == 0:
            bot.send_chat_action(chat_id=message.chat.id,
                                 action='upload_audio')
            bot.send_audio(message.chat.id, path)
            path.close()
            if os.path.isfile(rpath):
                os.remove(rpath)
        else:
            bot.send_message(message.chat.id, text=text)

    @bot.message_handler(commands=['a'])
    def sendaudios(message):
        data = message.text
        data = data.split(" ", 1)
        yurl = data[1]
        if 'https://open.spotify.com/track' in yurl:
            path, rpath, text, artist, title = sendaudio(yurl)
        else:
            path, rpath, text = sendaudio(yurl)
            artist = 0
        if artist == 0:
            if text == 0:
                bot.send_chat_action(chat_id=message.chat.id,
                                     action='upload_audio')
                bot.send_audio(message.chat.id, path)
                path.close()
                if os.path.isfile(rpath):
                    os.remove(rpath)
            else:
                bot.send_message(message.chat.id, text=text)
        else:
            if text == 0:
                bot.send_chat_action(chat_id=message.chat.id,
                                     action='upload_audio')
                bot.send_audio(message.chat.id,
                               audio=path,
                               title=title,
                               performer=artist)
                path.close()
                if os.path.isfile(rpath):
                    os.remove(rpath)
            else:
                bot.send_message(message.chat.id, text=text)

    @bot.message_handler(commands=['t'])
    def sendimages(message):
        data = message.text
        data = data.split(" ", 1)
        yurl = data[1]
        image = sendimage(yurl)
        if isinstance(image, list):
            try:
                bot.send_photo(message.chat.id, photo=image[0])
            except:
                try:
                    bot.send_photo(message.chat.id, photo=image[1])
                except:
                    try:
                        bot.send_photo(message.chat.id, photo=image[2])
                    except:
                        try:
                            bot.send_photo(message.chat.id, photo=image[3])
                        except:
                            try:
                                bot.send_photo(message.chat.id, photo=image[4])
                            except:
                                try:
                                    bot.send_photo(message.chat.id,
                                                   photo=image[5])
                                except:
                                    try:
                                        bot.send_photo(message.chat.id,
                                                       photo=image[6])
                                    except:
                                        try:
                                            bot.send_photo(message.chat.id,
                                                           photo=image[7])
                                        except:
                                            try:
                                                bot.send_photo(message.chat.id,
                                                               photo=image[8])
                                            except:
                                                bot.send_message(
                                                    message.chat.id,
                                                    text=
                                                    "Please send a valid youtube video url"
                                                )
        else:
            bot.send_message(message.chat.id, image)

    @bot.message_handler(commands=['gpt'])
    def chatgpt(message):
        data = message.text
        data = data.split(" ", 1)
        if len(data)==1:
            bot.send_message(message.chat.id,"Ask me anything")
            return
        elif data[1].strip()=="":
            bot.send_message(message.chat.id,"Ask me anything")
            return
        query = data[1]
        response = revopenai.make_request(query)
        bot.send_message(message.chat.id, text=response)
    
    bot.polling()


if __name__ == '__main__':
    main()
