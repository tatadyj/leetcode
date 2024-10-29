#
# @lc app=leetcode id=475 lang=python3
#
# [475] Heaters
#

# @lc code=start
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        res = 0
        for h in houses:
            idx = bisect_left(heaters, h)
            if idx == 0:
                radius = heaters[idx] - h 
            elif idx == len(heaters):
                radius = h - heaters[idx - 1] 
            else:
                radius = min(heaters[idx] - h, h - heaters[idx - 1])
            res = max(res, radius)
        return res        
# @lc code=end

