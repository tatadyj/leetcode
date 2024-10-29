#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        left = 0 
        window = defaultdict(int)
        
        for right in range(len(s)):
            rval = s[right]
            window[rval] += 1

            while right - left + 1 - max(window.values()) > k:
                lval = s[left]
                left += 1 

                window[lval] -= 1

            res = max(res, right - left + 1)

        return res 

Solution().characterReplacement("AABABBA", 1)
# @lc code=end

