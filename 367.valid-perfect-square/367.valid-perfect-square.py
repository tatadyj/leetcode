#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return num 

        l, r = 2, num // 2

        while l < r-1:
            mid = (l + r) // 2
            sq = mid * mid
            if sq < num:
                l = mid 
            elif sq > num:
                r = mid 
            else:
                return True 

        return (l*l == num) or (r*r == num) 
        
# @lc code=end

