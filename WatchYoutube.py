import MoveAndClick
import Action
import pyautogui
width, height = pyautogui.size()
def start():
    pyautogui.moveTo(width/2,height/2)
    while True:
        Action.ting('./AudioS/beep_open.wav')
        talk = Action.listen(3)
        if "stop"  in talk:
            break
        elif "tenth" in talk or talk == '10':
            MoveAndClick.Move(10)
        elif "eleventh" in talk or talk == '11':
            MoveAndClick.Move(11)
        elif "twelfth" in talk or talk == '12':
            MoveAndClick.Move(12)
        elif "first" in talk or "1" in talk:
            MoveAndClick.Move(1)
        elif "second" in talk or "2" in talk:
            MoveAndClick.Move(2)
        elif "third" in talk or "3" in talk:
            MoveAndClick.Move(3)
        elif "fourth" in talk or "4" in talk:
            MoveAndClick.Move(4)
        elif "fifth" in talk or "5" in talk:
            MoveAndClick.Move(5)
        elif "sixth" in talk or "6" in talk:
            MoveAndClick.Move(6)
        elif "seventh" in talk or "7" in talk:
            MoveAndClick.Move(7)
        elif "eighth" in talk or "8" in talk:
            MoveAndClick.Move(8)
        elif "ninth" in talk or "9" in talk:
            MoveAndClick.Move(9)
        elif "down" in talk:
            MoveAndClick.scroll(-100)
        elif "up" in talk:
            MoveAndClick.scroll(100)
        elif "header" in talk:
            MoveAndClick.scroll(9999)
        elif "pause" in talk or "play" in talk:
            MoveAndClick.presskey("k")
        elif "forward" in talk:
            MoveAndClick.presskey("l")
        elif "backward" in talk:
            MoveAndClick.presskey("j")
        elif "zoom" in talk:
            MoveAndClick.presskey("i")
        elif "full" in talk:
            MoveAndClick.presskey("f")
        elif "mute" in talk or "unmute" in talk:
            MoveAndClick.presskey("m")
        elif "back" in talk:
            MoveAndClick.clickleft(23,54)
            pyautogui.moveTo(width/2,height/2)
        elif "move" in talk:
            Action.speaker("Now you control")
            MoveAndClick.MoveLoop()
        elif "press" in talk or "click" in talk:
            Action.speaker("OK")
            MoveAndClick.clickleft(None,None)
        
