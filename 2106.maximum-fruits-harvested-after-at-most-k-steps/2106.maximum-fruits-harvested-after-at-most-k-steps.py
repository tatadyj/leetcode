#
# @lc app=leetcode id=2106 lang=python3
#
# [2106] Maximum Fruits Harvested After at Most K Steps
#

# @lc code=start
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        pos = [p for p,_ in fruits]
        amt = [a for _,a in fruits]
        prefix = [0] + amt
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i-1] + prefix[i]

        res = 0
        # i<---s
        # i--->s-->j
        # first case 2x + y <= k
        idx = bisect.bisect_left(pos, startPos)
        i = 0
        for j in range(idx, n):
            while pos[i] <= startPos and 2 * (startPos - pos[i]) + pos[j] - startPos > k:
                i += 1
            if pos[i] <= startPos:
                res = max(res, prefix[j+1] - prefix[i])
            elif pos[j] - startPos <= k:
                res = max(res, prefix[j+1] - prefix[idx])
        #      s-->j
        # i<---s<--j
        # second case x + 2y <= k
        idx = bisect.bisect_right(pos, startPos) - 1
        j = n - 1 
        for i in range(idx, -1, -1):
            while pos[j] >= startPos and startPos - pos[i] + 2 * (pos[j] - startPos) > k:
                j -= 1
            if pos[j] >= startPos:
                res = max(res, prefix[j+1] - prefix[i])
            elif startPos - pos[i] <= k:
                res = max(res, prefix[idx+1] - prefix[i])
        return res 
# @lc code=end

