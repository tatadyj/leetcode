#
# @lc app=leetcode id=321 lang=python3
#
# [321] Create Maximum Number
#

# @lc code=start
def find_max(nums, k):
    num_removed = len(nums) - k
    stack = []
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i] and num_removed > 0:
            stack.pop()
            num_removed -=1
        stack.append(i)

    for _ in range(num_removed):
        stack.pop()

    return [nums[i] for i in stack]

def merge(arr1, arr2):
    res = []
    size = len(arr1) + len(arr2)
    for _ in range(size):
        if arr1 > arr2:
            res.append(arr1.pop(0))
        else:
            res.append(arr2.pop(0))
    return res 
        


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        ret = None
        for i in range(k+1):
            if len(nums1) >= i and len(nums2) >= (k-i):
                max1 = find_max(nums1, i)
                max2 = find_max(nums2, k-i)
                final = merge(max1, max2)
                if not ret:
                    ret = final 
                else:
                    ret = max(ret, final)

        return ret

        
# @lc code=end

