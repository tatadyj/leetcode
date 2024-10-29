#
# @lc app=leetcode id=1876 lang=python3
#
# [1876] Substrings of Size Three with Distinct Characters
#

# @lc code=start
from collections import defaultdict

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left, right = 0, 0 
        res = 0
        while right < len(s):
            right += 1

            print(f"window: [{left}, {right})\n")
            while right - left == 3:
                if len(set(list(s[left:right]))) == 3:
                    res += 1
                left += 1
        return res 
        
# @lc code=end

