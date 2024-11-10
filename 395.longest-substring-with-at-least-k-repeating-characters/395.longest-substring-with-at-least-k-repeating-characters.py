#
# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#

# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        for m in range(1, 27):
            left, right = 0, 0 
            window = defaultdict(int)
            num_valid = 0
            while right < len(s):
                rval = s[right]
                window[rval] += 1 
                if window[rval] == k:
                    num_valid += 1

                # unique char > desired
                while len(window) > m:
                    lval = s[left]
                    if window[lval] == k: 
                        num_valid -= 1
                    window[lval] -= 1
                    if window[lval] == 0:
                        window.pop(lval)
                    left += 1

                if num_valid == m and len(window) == m:
                    res = max(res, right - left + 1)
                
                right += 1 
        return res 
        
# @lc code=end

