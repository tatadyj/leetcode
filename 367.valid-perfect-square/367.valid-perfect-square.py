#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num // 2
        while left < right:
            mid = (left + right) // 2
            if mid*mid >= num:
                right = mid 
            else:
                left = mid + 1 
        if left*left == num:
            return True 
        else:
            return False
        
# @lc code=end

