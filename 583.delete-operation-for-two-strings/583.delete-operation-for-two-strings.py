#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1)+1, len(word2)+1
        dp = [[0 for _ in range(len2)] for _ in range(len1)]

        for i in range(len1): dp[i][0] = i
        for j in range(len2): dp[0][j] = j

        for i in range(1, len1):
            for j in range(1, len2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] 
                else:
                    dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1]+2)
        return dp[-1][-1]
# @lc code=end

