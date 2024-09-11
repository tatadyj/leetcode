#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        word1 = list(word1)
        word2 = list(word2)
        i = j = 0
        while i < len(word1) and j < len(word2):
            ans.append(word1[i])
            ans.append(word2[j])
            i += 1
            j += 1

        if i < len(word1):
            ans.extend(word1[i:])
        if j < len(word2):
            ans.extend(word2[j:])
        return ''.join(ans)

Solution().mergeAlternately("abc", "pqr")
        
# @lc code=end

