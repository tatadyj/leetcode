#
# @lc app=leetcode id=759 lang=python3
#
# [759] Employee Free Time
#

# @lc code=start
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        diff = []
        for intervals in schedule:
            for interval in intervals:
                diff.append([interval.start, 1])
                diff.append([interval.end, -1])
        
        diff.sort(key=lambda x: (x[0], -x[1]))
        start = -1
        end = -1
        sum = 0 
        ans = []
        for i in range(len(diff)):
            if sum == 0 and sum + diff[i][1] > 0:
                end = diff[i][0]
                if start != -1:
                    ans.append(Interval(start, end))
            if sum > 0 and sum + diff[i][1] == 0:
                start = diff[i][0]
            sum += diff[i][1]
        return ans
# @lc code=end

