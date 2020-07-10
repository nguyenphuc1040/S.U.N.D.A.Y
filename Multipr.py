import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import requests, json
import Action,threading

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        audio = r.listen(source,timeout = 1, phrase_time_limit = 1.5)
    data = ""
    try:
        data = r.recognize_google(audio)
    except:
        data = listen()
    if data == "sunday": return data
    else: data = listen()

print(listen())
d = threading.Thread(name='listen', target=listen)
d.setDaemon(True)
d.join()
