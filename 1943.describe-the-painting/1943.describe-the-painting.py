#
# @lc app=leetcode id=1943 lang=python3
#
# [1943] Describe the Painting
#

# @lc code=start
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        diff = defaultdict(int)
        for start, end, color in segments:
            diff[start] += color 
            diff[end] -= color 

        ans = []
        start = -1
        end = -1
        sum = 0
        for pos in sorted(diff):
            if start == -1:
                start = pos
            else:
                end = pos
                ans.append([start, end, sum])
                start = end
            sum += diff[pos]

            if sum == 0:
                start = -1
        return ans
# @lc code=end

