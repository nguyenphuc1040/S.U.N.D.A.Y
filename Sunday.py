import threading
import random
import speech_recognition
import UI
#import Dectect
import What,Why,How,Open,Close,Who
import webbrowser
import SearchGG,Action
import WatchYoutube
import webbrowser

#pyinstaller --hidden-import=pyttsx3.drivers --hidden-import=pyttsx3.drivers.dummy --hidden-import=pyttsx3.drivers.espeak --hidden-import=pyttsx3.drivers.nsss --hidden-import=pyttsx3.drivers.sapi5

Ear = speech_recognition.Recognizer()

FrBr = ""
me = ""
talk = ""
dout = 0
StartTalk = "sunday"
A = [
    "Hello",
    "I'm here",
    "Hi there",
    "I'm listen",
]

B = [
    "OK ,see you later",
    "Goodbye, call me if you need"
]


import socket
import SOpen,FaceBook


def is_connected():
    try:
        # connect to the Host -- tells us if the Host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


def daemon():
    Action.ting("./AudioS/r2d2.wav")
    Action.speaker("welcome to the laptop")
    Action.speaker("I'm sunday. Say sunday to call me")
    dout = 0
    while True:
    
        while StartTalk in Action.listen(2):
            Action.speaker(A[random.randint(0,len(A)-1)])
            while True:
                with speech_recognition.Microphone() as mic:
                    Action.ting("./AudioS/beep_open.wav")
                    audio = Ear.listen(mic, timeout = 0, phrase_time_limit = 5)
                    Action.ting("./AudioS/beep_close.wav")
                try:
                    me = Ear.recognize_google(audio)
                except:
                    me = ""

                me = me.lower()
                if is_connected()==False:
                    Action.speaker("Please connect to the internet")
                if me == "":
                    if dout == 1:
                        dout = 0
                        FrBr = "I can hear you , see you later"
                        Action.speaker(FrBr)
                        break
                    FrBr = "Sorry I can't hear you, try again"
                    Action.speaker(FrBr)
                    dout = dout + 1
                    continue

                elif "bye" in me or "goodbye" in me or "thanks" in me or "thank you" in me or "see you later" in me or "no thanks" in me or "thank" in me or "no thank" in me:
                    FrBr = B[random.randint(0,len(B)-1)]
                    Action.speaker(FrBr)
                    break
                elif "what" in me or "what's" in me:
                    FrBr = What.Asw(me)
                elif "how" in me:
                    FrBr = How.Asw(me)
                elif "open" in me:
                    me = SOpen.process_string(me)
                    FrBr = Open.Open(me)
                elif "close" in me:
                    FrBr = Close.Close(me)
                elif "who" in me:
                    FrBr = Who.Asw(me)
                elif "search" in me:
                    FrBr = "I wil search on google"
                    me = SOpen.process_string(me)
                    SearchGG.Search(me)
                elif "hello youtube" in me:
                    Action.speaker("OK")
                    webbrowser.open_new('https://www.youtube.com')
                    WatchYoutube.start()
                    FrBr = "I'm done, do you want to say something more"
                elif "hello facebook" in me:
                    Action.speaker("OK now")
                    webbrowser.open_new('https://www.facebook.com')
                    FaceBook.surf()
                    FrBr = "I'm done, do you want to say something more"
                else: 
                    FrBr = "I'm sorry, I'm not program for this case, I wil search google for you"
                    SearchGG.Search(me)
                
                dout = 0
                Action.speaker(FrBr)
                FrBr = ""


d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)
d.start()


