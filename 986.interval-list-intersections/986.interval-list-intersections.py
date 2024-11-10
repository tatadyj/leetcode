#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#

# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []

        i, j = 0, 0
        l, r = 0, 0 
        while i < len(firstList) and j < len(secondList):
            a1, a2 = firstList[i]
            b1, b2 = secondList[j]

            if a2 < b1 or b2 < a1: # no overlap
                if a2 < b1:
                    i += 1
                if b2 < a1: 
                    j += 1
            else:
                l = max(a1, b1)
                r = min(a2, b2)

                res.append([l, r])
                if a2 < b2:
                    i += 1
                elif b2 < a2:
                    j += 1
                else:
                    i += 1
                    j += 1 
        return res 

# @lc code=end

