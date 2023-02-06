import instaloader
import re
import traceback
import os
from instaloader import Post
from moviepy.editor import VideoFileClip
USER=os.environ["USER"]
#PASSWORD=os.environ["PASSWORD"]
#L.login(USER, PASSWORD) 
#L.save_session_to_file(filename=".sessionid")

def ipost(text):
    url=text.replace("/i ","")
    if re.match(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)",url):
        regexp = '^(?:.*\/(p|tv|reel)\/)([\d\w\-_]+)'
        post_short_code = re.search(regexp, url).group(2)
        print(post_short_code)
        L = instaloader.Instaloader(filename_pattern=post_short_code)
        L.load_session_from_file(username=USER,filename=".sessionid")
        try:
            post = instaloader.Post.from_shortcode(L.context, post_short_code)
            L.download_post(post, target='videos')
            text=0
            if "reel" in url:
                path=f"videos/{post_short_code}.mp4"
                rpath=f"./{path}"
                if os.path.isfile(path):
                    path = open(path, 'rb')
                    if os.path.isfile(f"videos/{post_short_code}.jpg"):
                        os.remove(f"videos/{post_short_code}.jpg")
                    if os.path.isfile(f"videos/{post_short_code}.json.xz"):
                        os.remove(f"videos/{post_short_code}.json.xz")
                    if os.path.isfile(f"videos/{post_short_code}.txt"):
                        os.remove(f"videos/{post_short_code}.txt")
                    return path, rpath, text
                else:
                    r=0
                    text="File is private or invalid URL"
                    return r, r, text
            else:
                path=f"videos/{post_short_code}.jpg"
                path2=f"videos/{post_short_code}.mp4"
                rpath=f"./{path}"
                rpath2=f"./{path2}"
                if os.path.isfile(path2):
                    path2 = open(path2, 'rb')
                    if os.path.isfile(f"videos/{post_short_code}.jpg"):
                        os.remove(f"videos/{post_short_code}.jpg")
                    if os.path.isfile(f"videos/{post_short_code}.json.xz"):
                        os.remove(f"videos/{post_short_code}.json.xz")
                    if os.path.isfile(f"videos/{post_short_code}.txt"):
                        os.remove(f"videos/{post_short_code}.txt")
                    return path2, rpath2, text
                else:
                    path = open(path, 'rb')
                    if os.path.isfile(f"videos/{post_short_code}.json.xz"):
                        os.remove(f"videos/{post_short_code}.json.xz")
                    if os.path.isfile(f"videos/{post_short_code}.txt"):
                        os.remove(f"videos/{post_short_code}.txt")
                    return path, rpath, text
        except instaloader.exceptions.BadResponseException:
            r=0
            text="File is private or invalid URL"
            return r, r, text
    else:
        r=0
        text="File is private or invalid URL"
        return r, r, text

def iaudio(text):
    url=text.replace("/ia ","")
    if re.match(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)",url):
        regexp = '^(?:.*\/(p|tv|reel)\/)([\d\w\-_]+)'
        post_short_code = re.search(regexp, url).group(2)
        print(post_short_code)
        L = instaloader.Instaloader(filename_pattern=post_short_code)
        L.load_session_from_file(username=USER,filename=".sessionid")
        try:
            post = Post.from_shortcode(L.context, post_short_code)
            L.download_post(post, target='videos')
            text=0
            if "reel" in url:
                path=f"videos/{post_short_code}.mp4"
                rpath=f"./{path}"
                if os.path.isfile(path):
                    clip = VideoFileClip(r'{}'.format(path))
                    clip.audio.write_audiofile(r'{}mp3'.format(path[:-3]))
                    clip.close()
                    os.remove(rpath)
                    path=path.rpartition(".")[0]+".mp3"
                    rpath=f"./{path}"
                    path = open(path, 'rb')
                    if os.path.isfile(f"videos/{post_short_code}.jpg"):
                        os.remove(f"videos/{post_short_code}.jpg")
                    if os.path.isfile(f"videos/{post_short_code}.json.xz"):
                        os.remove(f"videos/{post_short_code}.json.xz")
                    if os.path.isfile(f"videos/{post_short_code}.txt"):
                        os.remove(f"videos/{post_short_code}.txt")
                    return path, rpath, text
                else:
                    r=0
                    text="File is private or invalid URL"
                    return r, r, text
            else:
                path=f"videos/{post_short_code}.jpg"
                path2=f"videos/{post_short_code}.mp4"
                rpath=f"./{path}"
                rpath2=f"./{path2}"
                if os.path.isfile(path2):
                    clip = VideoFileClip(r'{}'.format(path2))
                    clip.audio.write_audiofile(r'{}mp3'.format(path2[:-3]))
                    clip.close()
                    os.remove(rpath2)
                    path2=path2.rpartition(".")[0]+".mp3"
                    rpath=f"./{path2}"
                    path2 = open(path2, 'rb')
                    if os.path.isfile(f"videos/{post_short_code}.jpg"):
                        os.remove(f"videos/{post_short_code}.jpg")
                    if os.path.isfile(f"videos/{post_short_code}.json.xz"):
                        os.remove(f"videos/{post_short_code}.json.xz")
                    if os.path.isfile(f"videos/{post_short_code}.txt"):
                        os.remove(f"videos/{post_short_code}.txt")
                    return path2, rpath2, text
                else:
                    if os.path.isfile(f"videos/{post_short_code}.jpg"):
                        os.remove(f"videos/{post_short_code}.jpg")
                    if os.path.isfile(f"videos/{post_short_code}.json.xz"):
                        os.remove(f"videos/{post_short_code}.json.xz")
                    if os.path.isfile(f"videos/{post_short_code}.txt"):
                        os.remove(f"videos/{post_short_code}.txt")
                    r=0
                    text="Can't get the audio from the file"
                    return r, r, text
        except instaloader.exceptions.BadResponseException:
            r=0
            text="File is private or invalid URL"
            return r, r, text
        except:
            traceback.print_exc()
            r=0
            text="Unexpected error occured"
            return r, r, text
    else:
        r=0
        text="File is private or invalid URL"
        return r, r, text
                