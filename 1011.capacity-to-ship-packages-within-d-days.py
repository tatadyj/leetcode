#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
from typing import List 

# 计算所需要的最小天数
def requiredMinDays(weights, capacity):
    days = 0 
    total = 0 
    for w in weights:
        total += w 
        if total > capacity:
            days += 1 
            total = w 
    if total != 0:
        days += 1

    return days 

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right - 1:
            mid = (left + right) // 2
            minDays = requiredMinDays(weights, mid)
            if days < minDays: # capacity 太小 move 左界限
                left = mid 
            elif days > minDays: # capacity 太大 move 右界限
                right = mid 
            else:
                right = mid 

        if requiredMinDays(weights, left) <= days:
            return left 
        elif requiredMinDays(weights, right) <= days:
            return right
        else: 
            return -1 
            
if __name__ == '__main__':
    Solution().shipWithinDays([1,2,3,1,1], 4)
# @lc code=end

