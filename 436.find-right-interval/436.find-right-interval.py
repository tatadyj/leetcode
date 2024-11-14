#
# @lc app=leetcode id=436 lang=python3
#
# [436] Find Right Interval
#

# @lc code=start
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dct = {}
        for i, (s,e) in enumerate(intervals):
            dct[s] = i
            
        intervals.sort()
        starts = [i[0] for i in intervals]
        

        res = [-1] * len(intervals)
        for inter in intervals:
            idx = bisect.bisect_left(starts, inter[1])
            if idx < len(starts):
                res[dct[(inter[0])]] = dct[starts[idx]]

        return res
            

        
# @lc code=end

