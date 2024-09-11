#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if len(intervals) == 0:
            return res 

        intervals = sorted(intervals, key = lambda x: x[0])
        l, r = intervals[0]
        for interval in intervals:
            start, end = interval 
            if start <= r:
                r = max(end, r)
            else:
                res.append([l, r])
                l = start 
                r = end 
        res.append([l, r])
        return res 

Solution().merge([[1,3],[2,6],[8,10],[15,18]])
# @lc code=end

