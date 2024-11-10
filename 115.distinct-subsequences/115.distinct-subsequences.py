#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        slen, tlen = len(s)+1, len(t)+1
        dp = [[0 for _ in range(tlen)] for _ in range(slen)]

        for j in range(1, tlen): dp[0][j] = 0
        for i in range(slen): dp[i][0] = 1
        
        for i in range(1, slen):
            for j in range(1, tlen):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
# @lc code=end

