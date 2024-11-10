#
# @lc app=leetcode id=1288 lang=python3
#
# [1288] Remove Covered Intervals
#

# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        count = 0 

        prev_end = 0
        for _, curr_end in intervals:
            if curr_end > prev_end:
                count += 1
                prev_end = curr_end

        return count
        
# @lc code=end

