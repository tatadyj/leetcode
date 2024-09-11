#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n 

        f0, f1 = 0, 1
        f2 = 0
        for i in range(n-1):
            f2 = f1 + f0 
            f0 = f1 
            f1 = f2
        return f2
        
# @lc code=end

