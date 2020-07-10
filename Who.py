import SearchGG

def Asw(me):
    FAS = ""
    if "is" in me or "are" in me:
        if "own" in me or "boss" in me:
            FAS = "Nguyen Phuc"
        elif "you" in me:
            FAS = "I'm Sunday"
        else:
            FAS = "I wil search on google" 
            SearchGG.Search(me)
    else: 
        FAS = "I am not programed for this case"
    return FAS
