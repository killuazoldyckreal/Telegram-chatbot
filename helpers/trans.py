from googletrans import Translator
translator = Translator()


def translates(txt):
    length=txt.split(" ")
    if len(length)<=2:
        text="Invalid Method used\nPlease mention both language code and sentence\ne.g.: /trans 'hi' How are you?"
        return text
    else:
        txt=txt.split(" ",2)
        sent=txt[2]
        lang=txt[1]
        if "'" in lang:
            lang=lang.replace("'","")
            with open(r'languagecodes.txt','r') as file:
                content = file.read()
            if lang in content:
                out = translator.translate(sent, dest=lang).text
                text=out
                file.close()
                return text
            else:
                text="Invalid language code please recheck and try again!"
                file.close()
                return text
            
        elif '"' in lang:
            lang=lang.replace('"',"")
            with open(r'languagecodes.txt','r') as file:
                content = file.read()
            if lang in content:
                out = translator.translate(text=sent, dest=lang).text
                text=out
                file.close()
                return text
            else:
                text="Invalid language code please recheck and try again!"
                file.close()
                return text
        else:
            text="Please mention language code under inverted commas\ne.g.: /trans 'hi' How are you?"
            return text