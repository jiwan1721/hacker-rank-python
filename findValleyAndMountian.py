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

findValley(valleys)