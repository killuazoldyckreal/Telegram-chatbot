import re
import yt_dlp
import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials


def sendaudio(yurl):
    if re.match(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)",yurl):
        if 'youtu' in yurl:
            try:
                if 'https://www.youtube.com/c/' not in yurl:
                    ydl_opts_start = {'outtmpl': f'videos/%(title)s.mp3',
                                      'format': "ba/b"}
                    ydl = yt_dlp.YoutubeDL(ydl_opts_start)
                    with ydl:
                        result = ydl.extract_info(yurl, download=False)
                        title = ydl.prepare_filename(result)
                    ydl.download([yurl])
                    loc = title.replace('\\', '/')
                    rpath = f'./{loc}'
                    print(rpath)
                    path=f'{title}'
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
                    if os.path.isfile(path):
                        path = open(path, 'rb')
                        file_stats = os.stat(rpath)
                        vsize=file_stats.st_size/(1024*1024)
                        if vsize<50:
                            text = 0
                            return path, rpath, text
                        else:
                            text="Audio size exceeded limit!!\nUse the above link to download audio directly."
                            path.close()
                            os.remove(rpath)
                            r=0
                            return r, r , text
            except:
                text="File is private or not available"
                r=0
                return r, r , text
        elif 'https://open.spotify.com/track' in yurl:
            try:
                _id=yurl.replace("https://open.spotify.com/track/","").split("?")[0]
                sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.environ["YOUR_APP_CLIENT_ID"], client_secret=os.environ["YOUR_APP_CLIENT_SECRET"]))
                results = sp.track(track_id=_id)
                aname=results["artists"][0]["name"]
                sname=results["name"]
                songname=aname+" - "+sname
                if "'" in songname:
                    songname=songname.replace("'", "")
                elif '"' in songname:
                    songname=songname.replace('"', "")
                os.system(f"yt-dlp -f ba/b ytsearch:'{songname}' -o 'videos/{songname}.mp3'")
                path=f"videos/{songname}.mp3"
                rpath="./"+path
                if os.path.isfile(path):
                    path = open(path, 'rb')
                    file_stats = os.stat(rpath)
                    vsize=file_stats.st_size/(1024*1024)
                    if vsize<50:
                        text=0
                        return path, rpath, text, aname, sname
                    else:
                        text="Audio size exceeded limit!!"
                        path.close()
                        os.remove(rpath)
                        r=0
                        return r, r, text
            except:
                text="File is private or not available"
                r=0
                return r, r , text   
    else:
        r=0
        text="Please input valid URL"
        return r,r,text
        