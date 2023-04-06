nums = [-1,0,1,2,-1,-4]
import copy

output = [[-1,-1,2],[-1,0,1]]
def sums(nums):
    my_list = set()    
    list_len = len(nums)
    nums.sort()
    for i in range(0, list_len):
        for j in range(i+1, list_len):
            if i != j:
                for k in range(j, list_len):
                    if i !=k and j != k:
                        total_sum = nums[i]+nums[j]+nums[k]
                        if total_sum ==0:                            
                            my_list.add((nums[i],nums[j],nums[k]))
    return [list(i) for i in my_list]
                
print(sums(nums))
                