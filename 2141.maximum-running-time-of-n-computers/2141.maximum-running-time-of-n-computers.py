#
# @lc app=leetcode id=2141 lang=python3
#
# [2141] Maximum Running Time of N Computers
#

# @lc code=start
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def is_ok(T):
            sum = 0
            for b in batteries:
                sum += min(b, T)
            return sum >= T*n


        left = 0
        right = sum(batteries)
        while left < right:
            mid = (left + right + 1) // 2
            if is_ok(mid):
                left = mid 
            else:
                right = mid - 1
        return left 

        
# @lc code=end

