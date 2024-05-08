import tkinter as tk
import webbrowser
import pyttsx3
import os
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"

    return query

def wiki():
    speak("What do you want me to search for?")
    search = takeCommand()
    if search != "None":
        url = 'https://www.google.com/search?q=' + search
        speak("Here is what I found for " + search)
        webbrowser.open(url)

root = tk.Tk()
root.title("Personal Assistant")

label = tk.Label(root, text="Hello, I am your personal assistant.")
label.pack()

time_button = tk.Button(root, text="Tell Time", command=time)
time_button.pack()

wiki_button = tk.Button(root, text="Search Wikipedia", command=wiki)
wiki_button.pack()

root.mainloop()