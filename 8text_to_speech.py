# copy this and paste into the terminal
# pip install pyttsx3
# pip install pywin32

import pyttsx3
import os
data=input("Enter the text to convert into speech: ")
engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()
