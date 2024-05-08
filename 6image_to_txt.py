# copy this and paste into the terminal
# pip install pytesseract
# and download the exe file for the tesseract library from https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe
import os
import pytesseract
from PIL import Image

def convert(image):
    pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract.exe'
    text = pytesseract.image_to_string(image)
    print(text)

convert(Image.open('resume2.png'))