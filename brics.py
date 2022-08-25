from itertools import combinations


def makeBricks():
    small= int(input("enter number of small brics: "))
    big = int(input("enter number of big brics: "))
    goal= int(input("enter the goal: "))
    b_brics = big*5
    if small==goal or b_brics ==goal:
        print("from here")
        return True
    if b_brics<goal:
        print("bric goal")
        if small>(goal-b_brics):
            return True
        return False
    if small<goal:
        print("heooo")
        if (goal-small)%5==0:
            return True    
    else:
        return False

"""using combinations """
def make_bricks_using_combinations():
    small= int(input("enter number of small brics: "))
    big = int(input("enter number of big brics: "))
    goal= int(input("enter the goal: "))
    b_brics = big*5
    if (small+b_brics)<goal:
        return False
    my_list = [1]*small+[5]*big
    for index,y in enumerate(my_list,1):
        for combo in combinations(my_list,index):
            print(combo)
            if sum(combo)==goal:
                return True
    return False


