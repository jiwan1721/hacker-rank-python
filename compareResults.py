def compareTriplets(a,b):
    x = 0
    y = 0
    for a,b in zip(a,b):
        if a ==b :
            continue
        elif a > b:
            x+=1
        elif a < b:
            y+=1
    return x, y
        

a = [1,3,4]
b=[4,2,1]
print(compareTriplets(a, b))

def aVeryBigSum(ar):
    total_sum = 0
    for number in ar:
        total_sum +=number
    return total_sum

ar = [1000000001,1000000002,1000000003,1000000004,1000000005]
print(aVeryBigSum(ar))


def diagonalDifference(arr):
    primary_diagonal = 0
    secondary_diagonal = 0
    len_of_arr = len(arr) -1
    for index,item in enumerate(arr):
        primary_diagonal += item[index]
        secondary_diagonal += item[len_of_arr]
        len_of_arr -= 1
    return abs(primary_diagonal-secondary_diagonal)
arr = [
    [11,2,4],
    [4, 5, 6],
    [10, 8, -12]
]
print(diagonalDifference(arr))

def plusMinus(arr):
    positive_num = 0
    negative_num =0
    zero = 0
    len_arr = len(arr)
    for number in arr:
        if number > 0:
            positive_num += 1
        elif number < 0:
            negative_num += 1
        else:
            zero+=1
    positive_round = "{0:4f}".format((positive_num/len_arr))
    negaive_nums = "{0:4f}".format((negative_num/len_arr))
    zero_num = "{0:4f}".format((zero/len_arr))
    print(positive_round)
    print(negaive_nums)
    print(zero_num)    
arr=[-4, 3, -9, 0, 4, 1]
print(plusMinus(arr))

def staircase(n):
    for i in range(1,n+1):
        space= n-i
        print(" "*space,end="")
        
from copy import deepcopy
def miniMaxSum(arr):
    all_sum=[]
    for index in range(len(arr)):
        x = deepcopy(arr)
        x.pop(index)
        all_sum.append(sum(x))
    max_num = max(all_sum)
    min_num = min(all_sum)
    return min_num,max_num

def miniMaxSum1(arr):
    all_sum=[]
    for value in arr:
        x = sum(arr)-value
        all_sum.append(x)
    max_num = max(all_sum)
    min_num = min(all_sum)
    return min_num,max_num


        

arr = [1,3,5,7,9]
print(miniMaxSum1(arr))

def birthdayCakeCandles(candles):
    # Write your code here
    x = sorted(candles,reverse=True)
    print(x.count(x[0]))
birthdayCakeCandles([2,4,5,5,6])