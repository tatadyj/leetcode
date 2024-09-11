#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp 
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins: # 先coin 后amount 避免重复计数
            for i in range(1, amount + 1):
                if i - coin >= 0:
                    dp[i] += dp[i - coin]
        return dp[amount]
# @lc code=end

