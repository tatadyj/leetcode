#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        window = defaultdict(int)
        max_freq = 0
        left = 0
        for right in range(len(s)):
            rval = s[right]
            window[rval] += 1
            max_freq = max(max_freq, window[rval])
            while right - left + 1 - max_freq > k:
                lval = s[left]
                window[lval] -= 1 
                left += 1
            res = max(res, right - left + 1)
        return res  

# @lc code=end

