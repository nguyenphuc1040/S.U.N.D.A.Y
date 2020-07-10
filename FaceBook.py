import MoveAndClick
import Action
import pyautogui

width , height = pyautogui.size()

def surf():
    meol = ""
    while True:
        me = Action.listen(3)
        if "stop" in me or "begin" in me: 
            meol = me
        if "stop" in meol:
            meol = ""
            Action.speaker('ok')
        elif "begin" in meol:
            MoveAndClick.presskey('j')
        if "show" in me:
            pyautogui.moveTo(width/2,height/2)
            MoveAndClick.clickleft(None,None)
        elif "back" in me:
            MoveAndClick.clickleft(23,54)
            pyautogui.moveTo(width/2,height/2)
        elif "cancel" in me:
            break