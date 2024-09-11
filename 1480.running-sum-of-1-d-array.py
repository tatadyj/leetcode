#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        res[0] = nums[0]
        for i in range(1, len(nums)):
            res[i] = res[i-1] + nums[i]
        return res 
# @lc code=end

