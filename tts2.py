""" Custom tts code from google api """

import requests
import os
def get_speech(msg):
    ttsurl = "http://translate.google.com.vn/translate_tts?ie=UTF-8&tl=bn&client=tw-ob&q="
    ttsaud = requests.get(ttsurl+msg)
    with open("ttsout.mp3",'wb') as af:
            af.write(ttsaud.content)

def play():
    os.system("omxplayer ttsaud.mp3")
