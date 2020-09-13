import os
from langdetect import detect
from gtts import gTTS 

msg = "和歌山県大地町でググればいい"
lang = detect(msg)

tts = gTTS(msg, lang=lang)
print(tts.get_urls())
tts.save('temp.mp3')

