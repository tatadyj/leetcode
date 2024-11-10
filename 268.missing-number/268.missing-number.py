#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        res = len(nums)        
        for i in range(len(nums)):
            res = res ^ nums[i] ^ i 
        return res
# @lc code=end

