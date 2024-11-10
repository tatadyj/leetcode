#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        end, cnt = float('-inf'), 0 

        for point in sorted(points, key=lambda x:x[1]):
            if end < point[0]:
                cnt += 1
                end = point[1]
        return cnt 

        
# @lc code=end

