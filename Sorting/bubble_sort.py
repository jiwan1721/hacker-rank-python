def buble_sort(my_list):
    b = len(my_list)-1
    for x in range(b):
        for y in range(b-x):
            if my_list[y] > my_list[y+1]:
                my_list[y],my_list[y+1] = my_list[y+1],my_list[y]
    return my_list

my_list = [2,4,1,5,2,5]
print(buble_sort(my_list))

def insertion_sort(my_list):
    for x in range(1,len(my_list)):
        k = my_list[x]
        j = x -1
        while j >=0 and k < my_list[j]:
            my_list[j+1] = my_list[j]
            j-= 1
        my_list[j+1] = k
    return my_list

my_list = [2,4,1,5,3,5]
print(insertion_sort(my_list))