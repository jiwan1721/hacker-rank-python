'''Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.'''
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
def merge(nums1, m: int, nums2, n: int) -> None:
    for i in range(m,m+n):
        nums1[i] = nums2[m-i]
    nums1.sort()
merge(nums1, m, nums2, n)

def merge1(nums1, m: int, nums2, n: int) -> None:
    i = m-1
    j=n-1
    k= m+n-1
    while j>=0:
        if i >=0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            k-=1
            i-=1
        else:
            nums1[k] = nums2[j]
            k-=1
            j-=1
    print(nums1)
    
merge1(nums1, m, nums2, n)