#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
     
        # [1, 2, 3, 4]
        # [1, 1, 2, 6]
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        # [24, 12, 4, 1] right 
        # [1, 1, 2, 6]   left 
        # [24, 12, 8, 6] 
        right = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * right 
            right = right * nums[i]
        return res 
       

        
        
# @lc code=end

