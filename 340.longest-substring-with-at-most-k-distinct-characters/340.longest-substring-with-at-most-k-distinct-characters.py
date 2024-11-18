#
# @lc app=leetcode id=340 lang=python3
#
# [340] Longest Substring with At Most K Distinct Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res = 0 
        left = 0 
        window = defaultdict(int)

        for right in range(len(s)):
            rval = s[right]
            window[rval] += 1 

            while len(window) > k: 
                lval = s[left]
                window[lval] -= 1 
                if window[lval] == 0:
                    window.pop(lval)
                left += 1 

            res = max(res, right - left + 1)
        return res
        
# @lc code=end

