# copy this and paste into the terminal
# pip install pyttsx3
# pip install pywin32
# pip install SpeechRecognition
# pip install pyaudio

import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said: {}".format(text))
        return text
    except:
        print("Sorry could not recognize what you said")
        return None

listen()