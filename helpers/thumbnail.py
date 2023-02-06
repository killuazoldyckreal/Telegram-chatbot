import yt_dlp
import re

def sendimage(yurl):
    if 'youtu' in yurl:
        if 'https://www.youtube.com/c/' not in yurl:
            if re.match(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)",yurl):
                try:
                    ydl_opts_start = {
                        'format': 'best',
                        'outtmpl': f'%(id)s'
                    }
                    ydl = yt_dlp.YoutubeDL(ydl_opts_start)
                    with ydl:
                        result = ydl.extract_info(yurl, download=False)
                        _id = ydl.prepare_filename(result)
                    a = 'https://img.youtube.com/vi/' + _id + '/maxresdefault.jpg'
                    b = 'https://img.youtube.com/vi/' + _id + '/hqdefault.jpg'
                    c = 'https://img.youtube.com/vi/' + _id + '/mqdefault.jpg'
                    d = 'https://img.youtube.com/vi/' + _id + '/sddefault.jpg'
                    e = 'https://img.youtube.com/vi/' + _id + '/0.jpg'
                    f = 'https://img.youtube.com/vi/' + _id + '/1.jpg'
                    g = 'https://img.youtube.com/vi/' + _id + '/2.jpg'
                    h = 'https://img.youtube.com/vi/' + _id + '/3.jpg'
                    i = 'https://img.youtube.com/vi/' + _id + '/default.jpg'
                    images=[a,b,c,d,e,f,g,h,i]
                    return images
                except:
                    text="Thumbnail not found"
                    return text