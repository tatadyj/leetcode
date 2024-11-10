#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp 
        dp_i_0, dp_i_1 = 0, float('-inf')
        dp_prev_0 = 0
        for i in range(len(prices)):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_prev_0 - prices[i])
            dp_prev_0 = tmp
        return dp_i_0
        
# @lc code=end

