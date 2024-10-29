#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #ans = 0
        #for i in range(1, len(prices)):
        #    ans += max(prices[i] - prices[i-1], 0)
        #return ans

        # dp
        dp_i_0, dp_i_1 = 0, float('-inf') 
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
        return dp_i_0
# @lc code=end

