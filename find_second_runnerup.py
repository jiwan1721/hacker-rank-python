''' Given the participants' score sheet for your University 
Sports Day, you are required to find the runner-up score. 
You are given scores.Store them in a list and find the score 
of the runner-up. '''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_arr = []
    for i in arr:
        new_arr.append(i)
    new_arr.sort()
    x = set(new_arr)
    x.remove(max(x))
    print(max(x))


#different approach
# Python program to find second largest
# number in a list
 
# list of numbers - length of
# list should be at least 2
list1 = [10, 20, 4, 45, 99]
 
mx=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
n =len(list1)
for i in range(2,n):
    if list1[i]>mx:
        secondmax=mx
        mx=list1[i]
    elif list1[i]>secondmax and \
        mx != list1[i]:
        secondmax=list1[i]
 
print("Second highest number is : ",\
      str(secondmax))

#different approach but it wont work if we give same value twice or more
# so we have use set functio  as first program