#
# @lc app=leetcode id=1446 lang=python3
#
# [1446] Consecutive Characters
#

# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:
        left = 0 
        res = 0 
      
        for right in range(len(s)):
            if s[right] != s[left]:
                left = right 
            res = max(res, right-left+1)
        return res

        
# @lc code=end

