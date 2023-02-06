import os
import ffmpeg
def searchyt(yurl):
    try:
        os.system(f"yt-dlp -f 22 ytsearch:'{yurl}' -o 'videos/{yurl}.%(ext)s'")
        path=f"videos/{yurl}.mp4"
        rpath="./"+path
        path2=f"videos/{yurl}.mkv"
        rpath2="./"+path2
        path3=f"videos/{yurl}.webm"
        rpath3="./"+path3
        if os.path.isfile(path):
            path = open(path, 'rb')
            file_stats = os.stat(rpath)
            vsize=file_stats.st_size/(1024*1024)
            if vsize<50:
                text=0
                return path, rpath, text
            else:
                path.close()
                os.remove(rpath)
                os.system(f"yt-dlp -f 18 ytsearch:'{yurl}' -o 'videos/{yurl}.%(ext)s'")
                path=f"videos/{yurl}.mp4"
                rpath="./"+path
                path2=f"videos/{yurl}.mkv"
                rpath2="./"+path2
                path3=f"videos/{yurl}.webm"
                rpath3="./"+path3
                if os.path.isfile(path):
                    path = open(path, 'rb')
                    file_stats = os.stat(rpath)
                    vsize=file_stats.st_size/(1024*1024)
                    if vsize<50:
                        text=0
                        return path, rpath, text
                    else:
                        path.close()
                        os.remove(rpath)
                        r=0
                        text="File size exceeded limit(50MB)"
                        return r, r , text
                elif os.path.isfile(path2):
                    path = open(path2, 'rb')
                    file_stats = os.stat(rpath2)
                    vsize=file_stats.st_size/(1024*1024)
                    if vsize<50:
                        text=0
                        return path, rpath2, text
                    else:
                        path.close()
                        os.remove(rpath2)
                        text="File size exceeded limit(50MB)"
                        r=0
                        return r, r, text
                elif os.path.isfile(path3):
                    file_stats = os.stat(rpath3)
                    vsize=file_stats.st_size/(1024*1024)
                    if vsize<50:
                        stream=ffmpeg.input(path3)
                        stream=ffmpeg.output(stream, path)
                        ffmpeg.run(stream)
                        os.remove(rpath3)
                        path = open(path, 'rb')
                        text=0
                        return path , rpath, text
                    else:
                        os.remove(rpath3)
                        r=0
                        text="File size exceeded limit(50MB)"
                        return r, r , text
        elif os.path.isfile(path2):
            path = open(path2, 'rb')
            file_stats = os.stat(rpath2)
            vsize=file_stats.st_size/(1024*1024)
            if vsize<50:
                text=0
                return path, rpath2, text
            else:
                path.close()
                os.remove(rpath2)
                os.system(f"yt-dlp -f 18 ytsearch:'{yurl}' -o 'videos/{yurl}.%(ext)s'")
                path=f"videos/{yurl}.mp4"
                rpath="./"+path
                path2=f"videos/{yurl}.mkv"
                rpath2="./"+path2
                path3=f"videos/{yurl}.webm"
                rpath3="./"+path3
                if os.path.isfile(path):
                    path = open(path, 'rb')
                    file_stats = os.stat(rpath)
                    vsize=file_stats.st_size/(1024*1024)
                    if vsize<50:
                        text=0
                        return path, rpath, text
                    else:
                        path.close()
                        os.remove(rpath)
                        r=0
                        text="File size exceeded limit(50MB)"
                        return r, r , text
                elif os.path.isfile(path2):
                    path = open(path2, 'rb')
                    file_stats = os.stat(rpath2)
                    vsize=file_stats.st_size/(1024*1024)
                    if vsize<50:
                        text=0
                        return path, rpath2, text
                    else:
                        path.close()
                        os.remove(rpath2)
                        r=0
                        text="File size exceeded limit(50MB)"
                        return r, r , text
                elif os.path.isfile(path3):
                    file_stats = os.stat(rpath3)
                    vsize=file_stats.st_size/(1024*1024)
                    if vsize<50:
                        stream=ffmpeg.input(path3)
                        stream=ffmpeg.output(stream, path)
                        ffmpeg.run(stream)
                        os.remove(rpath3)
                        path = open(path, 'rb')
                        text=0
                        return path, rpath, text
                    else:
                        os.remove(rpath3)
                        r=0
                        text="Video not found"
                        return r, r , text

        
        elif os.path.isfile(path3):
            stream=ffmpeg.input(path3)
            stream=ffmpeg.output(stream, path)
            ffmpeg.run(stream)
            os.remove(rpath3)
            path = open(path, 'rb')
            file_stats = os.stat(rpath)
            vsize=file_stats.st_size/(1024*1024)
            if vsize<50:
                text=0
                return path , rpath, text
            else:
                path.close()
                os.remove(rpath2)
                os.system(f"yt-dlp -f 18 ytsearch:'{yurl}' -o 'videos/{yurl}.%(ext)s'")
                path=f"videos/{yurl}.mp4"
                rpath="./"+path
                path2=f"videos/{yurl}.mkv"
                rpath2="./"+path2
                path3=f"videos/{yurl}.webm"
                rpath3="./"+path3
                if os.path.isfile(path):
                    path = open(path, 'rb')
                    file_stats = os.stat(rpath)
                    vsize=file_stats.st_size/(1024*1024)
                    if vsize<50:
                        text=0
                        return path, rpath, text
                    else:
                        path.close()
                        os.remove(rpath)
                        text= "File not found"
                        r = 0
                        return r, r , text
                elif os.path.isfile(path2):
                    path = open(path2, 'rb')
                    file_stats = os.stat(rpath2)
                    vsize=file_stats.st_size/(1024*1024)
                    if vsize<50:
                        text = 0
                        return path, rpath2, text
                    else:
                        path.close()
                        os.remove(rpath2)
                        text="Video size exceeded limit!!(50MB)"
                        r = 0
                        return r, r, text
                elif os.path.isfile(path3):
                    file_stats = os.stat(rpath3)
                    vsize=file_stats.st_size/(1024*1024)
                    if vsize<50:
                        stream=ffmpeg.input(path3)
                        stream=ffmpeg.output(stream, path)
                        ffmpeg.run(stream)
                        os.remove(rpath3)
                        path = open(path, 'rb')
                        text = 0
                        return path , rpath, text
                    else:
                        os.remove(rpath3)
                        text="Video size exceeded limit!!(50MB)"
                        r = 0
                        return r, r, text
    except:
        try:
            os.system(f"yt-dlp -f 18 ytsearch:'{yurl}' -o 'videos/{yurl}.%(ext)s'")
            path=f"videos/{yurl}.mp4"
            rpath="./"+path
            path2=f"videos/{yurl}.mkv"
            rpath2="./"+path2
            path3=f"videos/{yurl}.webm"
            rpath3="./"+path3
            if os.path.isfile(path):
                path = open(path, 'rb')
                file_stats = os.stat(rpath)
                vsize=file_stats.st_size/(1024*1024)
                if vsize<50:
                    text=0
                    return path, rpath , text
                else:
                    path.close()
                    os.remove(rpath)
                    r=0
                    text = "File size exceeded limit(50MB)"
                    return r, r, text
            elif os.path.isfile(path2):
                path = open(path2, 'rb')
                file_stats = os.stat(rpath2)
                vsize=file_stats.st_size/(1024*1024)
                if vsize<50:
                    text=0
                    return path, rpath2, text
                else:
                    path.close()
                    os.remove(rpath2)
                    text="Video size exceeded limit!!(50MB)"
                    r= 0 
                    return r , r, text

            elif os.path.isfile(path3):
                file_stats = os.stat(rpath3)
                vsize=file_stats.st_size/(1024*1024)
                if vsize<50:
                    stream=ffmpeg.input(path3)
                    stream=ffmpeg.output(stream, path)
                    ffmpeg.run(stream)
                    os.remove(rpath3)
                    path = open(path, 'rb')
                    text=0
                    return path, rpath, text
                else:
                    os.remove(rpath3)
                    text = "Video not found"
                    r=0
                    return r , r, text
        except:
            text="File is private or not available"
            r=0
            return r, r, text


def searchaudio(yurl):
    try:
        os.system(f"yt-dlp -f bestaudio/best ytsearch:'{yurl}' -o 'videos/{yurl}.mp3'")
        path=f"videos/{yurl}.mp3"
        rpath="./"+path
        if os.path.isfile(path):
            path = open(path, 'rb')
            file_stats = os.stat(rpath)
            vsize=file_stats.st_size/(1024*1024)
            if vsize<50:
                text=0
                return path, rpath, text
            else:
                path.close()
                os.remove(rpath)
                text="File is private or not available"
                r=0
                return r, r, text
    except:
        text="File is private or not available"
        r=0
        return r, r, text