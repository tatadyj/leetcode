#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for i in range(n-1, -1, -1): #[0, n-1]
            for j in range(i+1, n, 1): # [i+1, n-1]
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2 
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        #print(dp)
        return dp[0][n-1]

# @lc code=end

