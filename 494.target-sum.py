#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for n in nums:
                if i - n >= 0 and i + n <= target:
                    dp[i] += dp[i - n] + dp[i + n]
        return dp[target]
        
# @lc code=end

