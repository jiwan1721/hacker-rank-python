"""find valley using given strig"""

valleys = 'DDUUDDUUUUDD'
def findValley(valleys):
    up = 0
    down =0
    mountain=0
    valley =0
    for letter in valleys:
        if letter=="U":
            up+=1
            down-=1
            if down==0:
                valley+=1
            continue
        elif letter=="D":
            up-=1
            down+=1
            if up==0:
                mountain+=1
            continue
    print("print total number of valley: ",valley)
    print("print total number of mountain: ",mountain)

def againFindValley(valleys):
    altitude = 0
    valley=0
    mountain=0
    for letter in valleys:
        upward = letter.lower()=="u"
        if upward:
            altitude+=1
        else:
            altitude-=1
        if altitude==0 and upward:
            valley+=1
        elif altitude ==0 and not upward:
            mountain+=1
    return mountain,valley

print(againFindValley(valleys))


findValley(valleys)