#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
def dp_solution(nums):
    if len(nums) <= 1:
        return len(nums)

    res = 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            dp[i] = dp[i-1] + 1
        res = max(res, dp[i])
    return res 


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        return dp_solution(nums)
# @lc code=end

