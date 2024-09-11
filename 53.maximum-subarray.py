#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp_i = float('-inf')
        res = float('-inf')
        for i in range(len(nums)):
            dp_i = max(dp_i + nums[i], nums[i])
            res = max(res, dp_i)
        return res
        
# @lc code=end

