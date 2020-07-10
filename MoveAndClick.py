import pyautogui
import time
import itertools 
import Action
width, height = pyautogui.size()

POSx = [4,2.2,1.5,1.17]
POSy = [3,1.6,1.1]

x = 0
y = 0

N = 5
Numth = list(itertools.product(POSy,POSx))
def Move(N):
  pyautogui.moveTo(width/Numth[N-1][1],height/Numth[N-1][0],duration=0.5)  

def MoveLoop():
  meol = ""
  while True:
    me = Action.listen(2)
    if "stop" in me:
      clickleft(None,None)
      break
    if "left" in me or "right" in me or "up" in me or "down" in me:
      meol = me
    if "left" in meol:
      pyautogui.moveRel(-100, 0, duration = 0.2)
    elif "right" in meol:
      pyautogui.moveRel(100, 0, duration = 0.2)
    elif "up" in meol:
      pyautogui.moveRel(0, -100, duration = 0.2)
    elif "down" in meol:
      pyautogui.moveRel(0, 100, duration = 0.2)


def clickleft(x,y):
  pyautogui.leftClick(x=x ,y = y)


def scroll(v):
    pyautogui.scroll(v)
    pyautogui.scroll(v)
    pyautogui.scroll(v)
    pyautogui.scroll(v)
    pyautogui.scroll(v)


def presskey(v):
    pyautogui.hotkey(v)
