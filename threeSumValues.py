nums = [-1,0,1,2,-1,-4]
import copy

output = [[-1,-1,2],[-1,0,1]]
def sums(nums):
    my_list = []
    list_len = len(nums)
    for i in range(0, list_len):
        for j in range(i+1, list_len):
            if i != j:
                for k in range(j, list_len):
                    if i !=k and j != k:
                        lis = [nums[i],nums[j],nums[k]]
                        lis.sort()
                        if sum(lis)==0:
                            if lis not in my_list:
                                my_list.append(lis)
    return my_list
                
print(sums(nums))
                