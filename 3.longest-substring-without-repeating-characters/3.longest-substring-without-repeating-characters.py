#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        unique_char = defaultdict(int)
        left = 0 
        for right in range(len(s)):
            rval = s[right]
            unique_char[rval] += 1
            while unique_char[rval] > 1:
                lval = s[left]
                unique_char[lval] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
# @lc code=end

