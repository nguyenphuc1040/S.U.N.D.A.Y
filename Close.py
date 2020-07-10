import subprocess
import os

def Close(me):
    FAS = ""
    if "chrome" in me or "google" in me:
        FAS = "OK"
        os.system("TASKKILL /F /IM chrome.exe")
    elif "garena" in me:
        FAS = "Yepp"
        os.system("TASKKILL /F /IM garena.exe")
    elif "code" in me:
        FAS = "OK"
        os.system("TASKKILL /F /IM code.exe")
    return FAS