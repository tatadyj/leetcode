#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
from typing import List

def hourNeed(piles, speed):
    hour = 0
    for p in piles:
        hour += p // speed 
        if p % speed != 0:
            hour += 1
    return hour


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = max(sum(piles)//h,1), max(piles)
        while left < right - 1:
            mid = (left + right) // 2
            hour = hourNeed(piles, mid)
            if hour > h: # 吃的太慢， 需要提高速度
                left = mid
            elif hour < h: # 吃的太快， 需要降低速度
                right = mid
            else:
                right = mid # 最小值 需要进一步push右边界

        return left if hourNeed(piles, left) <= h else right 
        
#print(Solution().minEatingSpeed([30,11,23,4,20], 6))
        
# @lc code=end

