#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n <= -1:
            n = -n 
            x = 1/x 

        res = 1 
        while n > 0:
            if n % 2 == 1:
                res = res * x 
                n = n - 1
            
            x = x**2 
            n = n / 2

        return res 
        
# @lc code=end

