import re
import yt_dlp
import os
import subprocess
import traceback
def sendvideo(yurl):
    if re.match(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)",yurl):
        if 'youtu' in yurl:
            if 'https://www.youtube.com/c/' not in yurl:
                try:
                    ydl_opts_start = {
                            'format': '22',
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
                    try:
                        size=result['filesize_approx']/1000000
                    except KeyError:
                        size=result['filesize']/1000000
                    if size <50:
                        ydl.download([yurl])
                        title = title.replace('\\', '/')
                        ntitle=title.lstrip('|')
                        ntitle=ntitle.lstrip('｜')
                        ntitle=ntitle.lstrip('｜｜')
                        ntitle=ntitle.replace("'","")
                        ntitle=ntitle.replace('"','')
                        if "'" in title or '"' in title or '|' in title or '｜' in title or '｜｜' in title:
                            os.rename(f"{title}", f'{ntitle}')
                        title = ntitle
                        path = title
                        rpath=f"./{path}"
                        if os.path.isfile(path):
                            path = open(path, 'rb')
                            text = 0
                            return path, rpath, text
                    else:
                        try:
                            ydl_opts_start = {
                                    'format': '18',
                                    'outtmpl': f'{title}',
                                    'no_warnings': False,
                                    'logtostderr': False,
                                    'ignoreerrors': False,
                                    'noplaylist': True,
                                    'writethumbnail': False
                                }
                            ydl = yt_dlp.YoutubeDL(ydl_opts_start)
                            with ydl:
                                result = ydl.extract_info(yurl, download=False)
                            try:
                                size=result['filesize_approx']/1000000
                            except KeyError:
                                size=result['filesize']/1000000
                            if size <50:
                                ydl.download([yurl])
                                path = title
                                rpath=f"./{path}"
                                if os.path.isfile(path):
                                    path = open(path, 'rb')
                                    text = 0
                                    return path, rpath, text
                            else:
                                try:
                                    try:
                                        size=subprocess.check_output(f"yt-dlp -f 397 {yurl} --print filesize_approx", shell=True)
                                        size = ''.join(filter(lambda i: i.isdigit(), str(size)))
                                        if size=="":
                                            size=subprocess.check_output(f"yt-dlp -f 397 {yurl} --print filesize", shell=True)
                                            size = ''.join(filter(lambda i: i.isdigit(), str(size)))
                                    except:
                                        try:
                                            size=subprocess.check_output(f"yt-dlp -f 397 {yurl} --print filesize", shell=True)
                                            size = ''.join(filter(lambda i: i.isdigit(), str(size)))
                                        except:
                                            try:
                                                size=subprocess.check_output(f"yt-dlp -f 135 {yurl} --print filesize_approx", shell=True)
                                                size = ''.join(filter(lambda i: i.isdigit(), str(size)))
                                                if size=="":
                                                    size=subprocess.check_output(f"yt-dlp -f 135 {yurl} --print filesize", shell=True)
                                                    size = ''.join(filter(lambda i: i.isdigit(), str(size)))
                                            except FileNotFoundError:
                                                size=subprocess.check_output(f"yt-dlp -f 135 {yurl} --print filesize", shell=True)
                                                size = ''.join(filter(lambda i: i.isdigit(), str(size)))
                                            except:
                                                print("Exception 00")
                                                traceback.print_exc()
                                                text="Some error occurred at bot's end."
                                                r=0
                                                return r, r, text
                                    size=int(size)
                                    if size/1000000 <50 :
                                        os.system(f"yt-dlp -f 397+139/135+139 {yurl} --merge-output-format mp4 -o '{title}'")
                                        path = title
                                        rpath=f"./{path}"
                                        if os.path.isfile(path):
                                            path = open(path, 'rb')
                                            text = 0
                                            return path, rpath, text
                                    else:
                                        try:
                                            try:
                                                size=subprocess.check_output(f"yt-dlp -f 134 {yurl} --print filesize_approx", shell=True)
                                                size = ''.join(filter(lambda i: i.isdigit(), str(size)))
                                                if size=="":
                                                    size=subprocess.check_output(f"yt-dlp -f 134 {yurl} --print filesize", shell=True)
                                                    size = ''.join(filter(lambda i: i.isdigit(), str(size)))
                                            except FileNotFoundError:
                                                size=subprocess.check_output(f"yt-dlp -f 134 {yurl} --print filesize", shell=True)
                                                size = ''.join(filter(lambda i: i.isdigit(), str(size)))
                                            except:
                                                print("Exception 0")
                                                traceback.print_exc()
                                                text="Some error occurred at bot's end."
                                                r=0
                                                return r, r, text
                                            size=int(size)
                                            if size/1000000 <50:
                                                os.system(f"yt-dlp -f 134+139/134+599 {yurl} --merge-output-format mp4 -o '{title}'")
                                                path = title
                                                rpath=f"./{path}"
                                                if os.path.isfile(path):
                                                    path = open(path, 'rb')
                                                    text = 0
                                                    return path, rpath, text
                                                else:
                                                    text="File not found"
                                                    r=0
                                                    return r, r, text
                                            else:
                                                text="Video size exceeded limit!!(50MB)."
                                                r=0
                                                return r, r, text
                                        except:
                                            print("Exception 1")
                                            traceback.print_exc()
                                            text="Some error occurred at bot's end."
                                            r=0
                                            return r, r, text
                                except:
                                    print("Exception 2")
                                    traceback.print_exc()
                                    text="Some error occurred at bot's end."
                                    r=0
                                    return r, r, text
                        except:
                            print("Exception 3")
                            traceback.print_exc()
                            text="Some error occurred at bot's end."
                            r=0
                            return r, r, text
                except:
                    print("Exception 4")
                    traceback.print_exc()
                    text="Some error occurred at bot's end."
                    r=0
                    return r, r, text
            else:
                r=0
                text="Please provide a valid URL"
                return r, r , text
        else:
            r=0
            text="Please provide a valid URL"
            return r, r , text
    else:
        r=0
        text="Please input valid URL"
        return r,r,text