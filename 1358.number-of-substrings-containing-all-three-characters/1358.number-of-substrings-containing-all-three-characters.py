#
# @lc app=leetcode id=1358 lang=python3
#
# [1358] Number of Substrings Containing All Three Characters
#

# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        window = defaultdict(int)
        left = 0 
        for right in range(n):
            rval = s[right]
            window[rval] += 1

            while left < n and len(window) == 3:
                res += n - right
                lval = s[left]
                window[lval] -= 1
                if window[lval] == 0:
                    window.pop(lval)
                left += 1

        return res 

        
# @lc code=end

