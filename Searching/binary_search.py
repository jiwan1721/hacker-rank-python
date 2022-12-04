def binary_search(my_list, key):
    left = 0
    right = len(my_list)-1
    matched = False
    while (left <= right and not matched):
        mid = (left+right)//2
        if my_list[mid]==key:
            matched = True
        else:
            if key < my_list[mid]:
                right = mid -1
            else:
                left = mid + 1
    return matched

my_list = [1,4,5,6,6]
print(binary_search(my_list, 2))
print(binary_search(my_list, 5))
