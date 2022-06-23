def bubbleSort(arr):
    array_length = len(arr)-1
    swapped = True
    for i in range(array_length):
        for j in range(0,array_length-i):
            if arr[j]>arr[j+1]:
                # swapped=True
                # arr[j],arr[j+1]=arr[j+1],arr[j]
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
        if not swapped:
            return
    return arr

arr=[12,23,34,23,31,11,24]
print(bubbleSort(arr))

#shortcut for bubble sort

for i in range(len(arr)):
    print('%d'%arr[i],end=" ")

# The %d operator is used as a placeholder to specify integer values, decimals or numbers.
# It allows us to print numbers within strings or other values.
# The %d operator is put where the integer is to be specified. Floating-point
# numbers are converted automatically to decimal values. 

