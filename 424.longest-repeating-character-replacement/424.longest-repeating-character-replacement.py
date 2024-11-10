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
        left, right = 0, 0
        def num_changes(window):
            return (right - left + 1) - max(window.values())  

        while right < len(s):
            rval = s[right]
            window[rval] += 1
            while num_changes(window) > k:
                lval = s[left]
                window[lval] -= 1 
                left += 1

            res = max(res, right - left + 1)

            right += 1

        return res  

# @lc code=end

