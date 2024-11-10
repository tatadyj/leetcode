#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def count_hours(piles, val):
            count = 0
            for pile in piles:
                count += ceil(pile / val)
            return count 

        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            count = count_hours(piles, mid)
            if count <= h:
                right = mid
            else:
                left = mid + 1 
        return left
       
           
        
# @lc code=end

