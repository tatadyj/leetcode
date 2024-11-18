#
# @lc app=leetcode id=3258 lang=python3
#
# [3258] Count Substrings That Satisfy K-Constraint I
#

# @lc code=start
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res = 0 
        count_zeros = 0
        left = 0 
        for right in range(len(s)):
            rval = s[right]
            if rval == '0':
                count_zeros += 1

            while count_zeros > k and right - left + 1 - count_zeros > k:
                lval = s[left]
                if lval == '0':
                    count_zeros -= 1
                left += 1
            res += right - left + 1
        return res  
# @lc code=end

