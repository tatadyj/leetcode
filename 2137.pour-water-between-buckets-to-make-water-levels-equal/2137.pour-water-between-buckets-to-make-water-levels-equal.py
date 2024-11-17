#
# @lc app=leetcode id=2137 lang=python3
#
# [2137] Pour Water Between Buckets to Make Water Levels Equal
#

# @lc code=start
class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        def is_ok(v):
            incr = 0
            decr = 0
            for b in buckets:
                if b > v:
                    decr += b - v 
                if b < v:
                    incr += v - b
            return decr * (100 - loss)/100 >= incr

        left = 0
        right = max(buckets)

        while right - left > 10**-5:
            mid = (left + right) / 2
            if is_ok(mid):
                left = mid 
            else:
                right = mid
        return left  
# @lc code=end

