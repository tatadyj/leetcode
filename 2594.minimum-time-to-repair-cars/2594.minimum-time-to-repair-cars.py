#
# @lc app=leetcode id=2594 lang=python3
#
# [2594] Minimum Time to Repair Cars
#

# @lc code=start
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def is_ok(t):
            count = 0 
            for r in ranks:
                count += int(sqrt(t / r))
                if count >= cars:
                    return True 
            return False 

        left = 1
        right = max(ranks) * cars * cars
        while left < right:
            mid = (left + right) //2 
            if is_ok(mid):
                right = mid 
            else:
                left = mid + 1
        return left 
# @lc code=end

