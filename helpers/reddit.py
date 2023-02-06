import yt_dlp
import re
import os
import subprocess
import requests
import random
def rvideo(yurl):
    if re.match(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)",yurl):
        if 'www.reddit.com/r' in yurl:
            try:
                ydl_opts_start = {
                        'format': 'bv+ba/b',
                        'outtmpl': f'videos/%(title)s.%(ext)s',
                        'no_warnings': False,
                        'logtostderr': False,
                        'ignoreerrors': False,
                        'noplaylist': True,
                        'writethumbnail': False
                    }
                ydl = yt_dlp.YoutubeDL(ydl_opts_start)
                with ydl:
                    result = ydl.extract_info(yurl, download=False)
                    title = ydl.prepare_filename(result)
                ydl.download([yurl])
                path = f'{title}'
                rpath = f'./{path}'
                if ".jpg" in path:
                    r=0
                    text="The file is an image, please send video URL to get the audio file."
                    os.remove(rpath)
                    return r, r, text
                if ".mp4" not in path:
                    path1=path
                    path=path.rsplit('.')[0]
                    try:
                        subprocess.call(['ffmpeg', '-i', f'{path1}', f'{path}.mp4'])
                        os.remove(f"./{path1}")
                        path=f"{path}.mp4"
                        rpath=f"./{path}.mp4"
                    except Exception as e:
                        print(e)
                        print('Error While Converting Vido')
                if os.path.isfile(rpath):
                    path = open(rpath, 'rb')
                    file_stats = os.stat(rpath)
                    vsize=file_stats.st_size/(1024*1024)
                    if vsize<50:
                        text = 0
                        return path, rpath, text
                    else:
                        path.close()
                        os.remove(rpath)
                        text="Video size exceeded limit!!(50MB)."
                        r=0
                        return r, r, text
            except:
                text="File is private or not available. Please check the URL and try again"
                r=0
                return r, r, text
        else:
            r=0
            text="Please provide a valid URL1"
            return r, r , text
    else:
        r=0
        text="Please input valid URL2"
        return r,r,text

def raudio(yurl):
    if re.match(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)",yurl):
        if 'www.reddit.com/r/' in yurl:
            try:
                ydl_opts_start = {'format': "ba/b",
                                  'outtmpl': f'videos/%(title)s.%(ext)s'}
                ydl = yt_dlp.YoutubeDL(ydl_opts_start)
                with ydl:
                    result = ydl.extract_info(yurl, download=False)
                    title = ydl.prepare_filename(result)
                ydl.download([yurl])
                path=f'{title}'
                rpath = f'./{path}'
                name=result['title']
                if '|' in name:
                    while name[0]=='|' or name[0]=='｜' or name[0]=='｜｜':
                        name=name.lstrip('|')
                        name=name.lstrip('｜')
                        name=name.lstrip('｜｜')
                    while name[0]==' ':
                        name=name.lstrip(" ")
                    name= name.split('|',1)
                    name=name[0]
                else:
                    if len(result['title'])>25:
                        name=result['title'][:25]
                    else:
                        name=result['title']
                if ".jpg" in path or ".jpeg" in path:
                    r=0
                    text="The file is an image, please send video URL to get the audio file."
                    os.remove(rpath)
                    return r, r, text
                if ".mp3" not in path:
                    path1=path
                    path=path.rsplit('.')[0]
                    try:
                        subprocess.call(['ffmpeg', '-i', f'{path1}', f'{path}.mp3'])
                        os.remove(f"./{path1}")
                        path=f"{path}.mp3"
                        rpath=f"./{path}.mp3"
                    except Exception as e:
                        print(e)
                        print('Error While Converting Audio')
                if os.path.isfile(path):
                    path = open(path, 'rb')
                    file_stats = os.stat(rpath)
                    vsize=file_stats.st_size/(1024*1024)
                    if vsize<50:
                        text = 0
                        return path, rpath, text
                    else:
                        text="Audio size exceeded limit!!."
                        path.close()
                        os.remove(rpath)
                        r=0
                        return r, r , text
            except:
                text="File is private or not available"
                r=0
                return r, r , text
        else:
            r=0
            text="Please provide a valid URL"
            return r, r , text
    else:
        r=0
        text="Please input valid URL"
        return r,r,text

def rimage(url):
    if re.match(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)",url):
        if 'www.reddit.com/r/' in url:
            try:
                regexp = '^(?:.*\/(comments)\/.*\/)([\d\w\-_]+)'
                code = re.search(regexp, url).group(2)
                ydl_opts_start = {'outtmpl': f'videos/%(title)s.%(ext)s'}
                ydl = yt_dlp.YoutubeDL(ydl_opts_start)
                with ydl:
                    result = ydl.extract_info(url, download=False)
                    title = ydl.prepare_filename(result)
                ydl.download([url])
                path=f"{title}"
                print("Path: ",path)
                rpath=f"./{path}"
                if ".jpg" not in path or ".mp3" in path or ".m4a" in path or ".mp4" in path:
                    r=0
                    text="The file is not an image, please send valid image URL"
                    os.remove(rpath)
                    return r, r, text
                if os.path.isfile(path):
                    path = open(path, 'rb')
                    text=0
                    return path, rpath, text
            except Exception as e:
                print(e)
                text="File is private or not available"
                r=0
                return r, r , text
        else:
            r=0
            text="Please provide a valid URL"
            return r, r , text
    else:
        r=0
        text="Please input valid URL"
        return r,r,text

def rmeme(url):
    try:
        ydl_opts_start = {
                'format': 'bv+ba/b',
                'outtmpl': f'videos/%(title)s.%(ext)s',
                'no_warnings': False,
                'logtostderr': False,
                'ignoreerrors': False,
                'noplaylist': True,
                'writethumbnail': False
            }
        ydl = yt_dlp.YoutubeDL(ydl_opts_start)
        with ydl:
            result = ydl.extract_info(url, download=False)
            title = ydl.prepare_filename(result)
        ydl.download([url])
        path = f'{title}'
        rpath = f'./{path}'
        if ".jpg" in path:
            if os.path.isfile(path):
                path = open(path, 'rb')
                text=1
                return path, rpath, text
        else:
            if ".mp4" not in path:
                path1=path
                path=path.rsplit('.')[0]
                try:
                    subprocess.call(['ffmpeg', '-i', f'{path1}', f'{path}.mp4'])
                    os.remove(f"./{path1}")
                    path=f"{path}.mp4"
                    rpath=f"./{path}.mp4"
                except Exception as e:
                    print(e)
                    print('Error While Converting Audio')
            if os.path.isfile(rpath):
                path = open(rpath, 'rb')
                file_stats = os.stat(rpath)
                vsize=file_stats.st_size/(1024*1024)
                if vsize<50:
                    text = 0
                    return path, rpath, text
                else:
                    path.close()
                    os.remove(rpath)
                    text="Video size exceeded limit!!(50MB)."
                    r=0
                    return r, r, text
    except:
        text="File is private or not available. Please check the URL and try again"
        r=0
        return r, r, text