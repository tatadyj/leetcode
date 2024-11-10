#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        q = [[-v, k] for k,v in Counter(s).items()]
        heapq.heapify(q)

        res = []
        while q:
            cnt, stack = 0, []
            for _ in range(2):
                if q:
                    v, k = heapq.heappop(q)
                    if not res or k != res[-1]:
                        res.append(k) 
                        if v < -1:
                            stack.append([v+1, k])

            for item in stack:
                heapq.heappush(q, item)
    

        if len(res) != len(s):
            return ''
        else: 
            return ''.join(res)

print(Solution().reorganizeString("vvvvlo"))



# @lc code=end

