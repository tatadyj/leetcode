#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slen, tlen = len(s)+1, len(t)+1
        dp =[[0 for _ in range(tlen)] for _ in range(slen)]

        for i in range(1, slen):
            for j in range(1, tlen):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]

        return dp[-1][-1] == slen-1 
        
# @lc code=end

