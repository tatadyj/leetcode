#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
def is_valid(val, weights, days):
    count = 1
    total = 0 
    for i in range(len(weights)):
        total += weights[i]
        if total > val:
            count += 1
            total = weights[i]
    return count <= days

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            if is_valid(mid, weights, days):
                right = mid
            else:
                left = mid + 1 
        return left

            
# @lc code=end

