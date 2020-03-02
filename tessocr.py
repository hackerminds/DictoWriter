''' image to text and text to voice '''
from PIL import Image
import pytesseract as ts
import requests
import os

from gtts import gTTS

url = "http://192.168.137.44:8080/shot.jpg"

def captureImg():
    img = requests.get(url).content
    with open("/home/pi/Pictures/hackgr9/shot.jpg",'wb') as shot:
        shot.write(img)
    
def img2txt():
    outText = ts.image_to_string(Image.open('/home/pi/Pictures/hackgr9/shot.jpg'), lang='eng')
    print(outText)
    return(outText)
    
def main():
    captureImg()
    tts = gTTS(img2txt())
    tts.save('ttsaud.mp3')
    os.system("omxplayer ttsaud.mp3")
    
main()
