#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: 
            return x
        
        left, right = 2, x // 2
        
        while left < right-1:
            mid = (left + right) // 2
            if mid*mid > x:
                right = mid
            elif mid*mid < x:
                left = mid
            else:
                return mid 
            
        return right if right*right <= x else left 

# @lc code=end

