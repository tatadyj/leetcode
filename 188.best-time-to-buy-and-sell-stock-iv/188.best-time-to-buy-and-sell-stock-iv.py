#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
from typing import List 
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[[float('-inf') for _ in range(2)] for _ in range(k+1)] for _ in range(len(prices))]
        for i in range(len(prices)):
            dp[i][0][0] = 0
            dp[i][0][1] = float('-inf')

        for j in range(1, k):
            dp[0][j][0] = 0 
            dp[0][j][1] = - prices[0]

        for i in range(1, len(prices)):
            for j in range(k, 0, -1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

        return dp[-1][-1][0]

Solution().maxProfit(2, [2, 4, 1])
# @lc code=end

