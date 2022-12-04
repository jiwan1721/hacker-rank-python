
def merge_sort(ourlist, left, right):
    if right - left > 1:  # check if list length is greater than one
        middle = (left + right)//2
        merge_sort(ourlist, left, middle)
        merge_sort(ourlist, middle, right)
        merge_list1 = merge_list(ourlist, left, middle, right)
        return merge_list1

def merge_list(ourlist, left, middle, right):
    leftlist = ourlist[left:middle]
    rightlist = ourlist[middle:right]
    k = left
    i = 0
    j=0
    while(left +i<middle and middle+j <right):
        if (leftlist[i] <= rightlist[j]):
            ourlist[k] = leftlist[i]
            i = i+1
        else:
            ourlist[k] = rightlist[i]
            j = j+1
        k = k +1
    if left + i < middle:
        ourlist[k]=leftlist[i]
        i = i+1
        k = k+1
    else:
        while k <right:
            ourlist[k]=rightlist[j]
            j = j + 1
            k = k+1
    return ourlist
ourlist = [1,4,64,6,4]
print(merge_sort(ourlist, 0, len(ourlist)))

