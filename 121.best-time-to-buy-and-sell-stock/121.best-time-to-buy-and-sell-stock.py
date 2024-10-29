#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min_price = float('inf')
        # max_profit = 0
        # for i in range(len(prices)):
        #     if prices[i] < min_price:
        #         min_price = prices[i]
        #     elif prices[i] - min_price > max_profit:
        #         max_profit = prices[i] - min_price
                
        # return max_profit
        
        # dp
        dp_i_0, dp_i_1 = 0, float('-inf') 
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, - prices[i])
        return dp_i_0

# @lc code=end

