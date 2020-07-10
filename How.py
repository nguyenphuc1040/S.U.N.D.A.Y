import random

A = [
    "I'm fine, thank you", 
    "I'm good", 
    "I feel so good, until i see you"
]
sizeA = len(A)-1

B = [
    "Sorry, I don't know your emotion",
    "Are you an idiot, Your emotion, how do I know ???"
]
sizeB = len(B)-1

def Asw(me):
    FAS =""
    if "are you" in me:
        FAS = A[random.randint(0,sizeA)] 
    elif "do" in me:
        if "feel" in me:
            if "I" in me or "my" in me:
                FAS = B[random.randint(0,sizeB)]
            elif "you" in me:
                FAS = A[random.randint(0,sizeA)]
    else:
        FAS = "I am not programed for this case"
    return FAS
        