#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
from collections import Counter
from typing import List
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [[-v,k] for k,v in Counter(tasks).items()]
        heapq.heapify(heap)
        res = 0 
        n += 1

        while heap:

            cnt, stack = 0, []
            for _ in range(n):
                if heap:
                    v,k = heapq.heappop(heap)
                    cnt += 1
                    if v < -1:
                        stack.append([v+1, k])
            for item in stack:
                heapq.heappush(heap, item)
            
            if heap:
                res += n 
            else:
                res += cnt
        return res 

Solution().leastInterval(["A","A","A","B","B","B"],2)
# @lc code=end

