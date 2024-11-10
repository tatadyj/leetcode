#
# @lc app=leetcode id=1870 lang=python3
#
# [1870] Minimum Speed to Arrive on Time
#

# @lc code=start
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def is_ok(val):
            count = 0 
            for i,d in enumerate(dist):
                if i == len(dist)-1:
                    count += d/val
                else:
                    count += ceil(d/val)
            return count <= hour

        left = 1
        right = 10**7
        while left < right:
            mid = (left + right) // 2
            if is_ok(mid):
                right = mid 
            else:
                left = mid + 1

        if is_ok(left):
            return left
        else:
            return -1 
             
# @lc code=end

