#
# @lc app=leetcode id=1237 lang=python3
#
# [1237] Find Positive Integer Solution for a Given Equation
#

# @lc code=start
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        for x in range(1, 1001):
            left, right = 1, 1001
            while left < right:
                y = (left + right) // 2 
                if customfunction.f(x, y) >= z:
                    right = y 
                else:
                    left = y + 1 
            if customfunction.f(x, left) == z:
                ans.append([x, left])
        return ans
# @lc code=end

