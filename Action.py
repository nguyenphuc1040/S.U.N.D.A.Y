import pyttsx3
import speech_recognition
import simpleaudio as sa
import threading

MSMARY = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\MSMary'
MSZIRA = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0'
#pyinstaller --hidden-import=pyttsx3.drivers --hidden-import=pyttsx3.drivers.dummy --hidden-import=pyttsx3.drivers.espeak --hidden-import=pyttsx3.drivers.nsss --hidden-import=pyttsx3.drivers.sapi5
SPK = pyttsx3.init(driverName='sapi5')
Ear = speech_recognition.Recognizer()
SPK.setProperty('voice',MSZIRA)
SPK.setProperty('rate',140)

def listen(timex):
    with speech_recognition.Microphone() as mic:
        audio = Ear.listen(mic, timeout = 0, phrase_time_limit = timex)
    try:
        return Ear.recognize_google(audio).lower()
    except:
        return ""

def speaker(x):
    SPK.say(x)
    SPK.runAndWait()


def ting(x):
    filename = x
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

