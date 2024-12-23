#
# @lc app=leetcode id=1353 lang=python3
#
# [1353] Maximum Number of Events That Can Be Attended
#

# @lc code=start
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        pq = []
        res = 0
        i = 0
        for day in range(1, 10**5+1):
            while i < len(events) and events[i][0] <= day:
                heapq.heappush(pq, events[i][1])
                i += 1

            while pq and pq[0] < day:
                heapq.heappop(pq)

            if pq:
                heapq.heappop(pq)
                res += 1
        return res  
# @lc code=end

