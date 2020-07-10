import subprocess
import os
import time
import random
 
import webbrowser

A = [
    "Yes sir",
    "OK I wil do",
    "OK",
    "Yep"
]

def Open(me):
    
    if "garena" in me:
        subprocess.Popen("C:\Program Files (x86)\Garena\Garena\Garena.exe")
    elif "code" in me:
        subprocess.Popen("C:\Program Files\Microsoft VS Code\Code.exe")
    else:
        webbrowser.open_new('http:/www.'+ me + '.com')
    return A[random.randint(0,len(A)-1)]