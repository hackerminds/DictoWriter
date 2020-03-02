''' Speech synthesizer for ocr output '''
from PIL import Image
import pytesseract as ts
import requests
import os

from gtts import gTTS

url = "http://192.168.111.44:8080/shot.jpg" #ip address of the IP CAM App

def captureImg():
    img = requests.get(url).content
    with open("/home/pi/Pictures/hackgr9/shot.jpg",'wb') as shot:
        shot.write(img)
    
def img2txt():
    outText = ts.image_to_string(Image.open('/home/pi/Pictures/shot.jpg'), lang='eng')
    print(outText)
    return(outText)
    
def main():
    captureImg()
    tts = gTTS(img2txt())
    tts.save('ttsaud.mp3')
    os.system("omxplayer ttsaud.mp3")
    
main()
