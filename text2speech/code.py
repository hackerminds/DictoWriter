from PIL import Image
import pytesseract as ts
inImg = Image.open('/home/pi/Pictures/sample.png')
outText = ts.image_to_string(inImg, lang='eng')
print(outText)