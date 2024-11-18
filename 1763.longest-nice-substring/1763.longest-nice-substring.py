#
# @lc app=leetcode id=1763 lang=python3
#
# [1763] Longest Nice Substring
#

# @lc code=start
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        max_len = 0 
        ret = ""
        for k in range(1, 27):
            upper = defaultdict(int)
            lower = defaultdict(int)
            num_valid = 0
            left = 0 
            for right in range(len(s)):
                rval = s[right]
                if rval.lower() == rval:
                    lower[rval] += 1
                    if lower[rval] == 1 and rval.upper() in upper and upper[rval.upper()] > 0:
                        num_valid += 1
                else:
                    upper[rval] += 1
                    if upper[rval] == 1 and rval.lower() in lower and lower[rval.lower()] > 0:
                        num_valid += 1
                
                while left < len(s) and (len(lower) > k or len(upper) > k):
                    lval = s[left]
                    if lval.lower() == lval:
                        if lower[lval] == 1 and lval.upper() in upper and upper[lval.upper()] > 0:
                            num_valid -= 1
                        lower[lval] -= 1
                        if lower[lval] == 0:
                            lower.pop(lval)
                    else:
                        if upper[lval] == 1 and lval.lower() in lower and lower[lval.lower()] > 0:
                            num_valid -= 1
                        upper[lval] -= 1
                        if upper[lval] == 0:
                            upper.pop(lval)
                    left += 1

                if num_valid == k: 
                    #print(num_valid, s[left:right+1])
                    if right - left + 1 > max_len:
                        max_len = right - left + 1
                        ret = s[left:right+1]
        return ret
            
# @lc code=end

