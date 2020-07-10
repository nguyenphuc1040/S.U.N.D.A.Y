from datetime import date, datetime
today = date.today()
now = datetime.now()
import random
import SearchGG


A = [
    "I'm sure you know i'm Sunday",
    "Come on, I'm Sunday",
    "Sunday"
]
sizeA = len(A)-1

def Asw(me):
    FAS = ""
    if "is" in me:
        if "name" in me:
            if "your" in me:
                FAS = A[random.randint(0,sizeA)]
            elif "my" in me:
                FAS = "I'm sorry, I don't know your name"
        else :
            FAS = "I wil search on google" 
            SearchGG.Search(me)
    elif "do" in me:
        if "you do" in me:
            FAS = "I'm assisant virtual"
    elif "time" in me:
        FAS = now.strftime("%H:%M:%S")
    elif "today" in me:
        FAS = today.strftime("%B %d, %Y")
    elif "are" in me:
        if "you" in me:
            if "doing" in me:
                FAS = "I'm talking with you"
        else:
            FAS = "I wil search on google" 
            SearchGG.Search(me)        
    else:
        FAS = "I am not programed for this case"
    return FAS
                