#
# @lc app=leetcode id=871 lang=python3
#
# [871] Minimum Number of Refueling Stops
#

# @lc code=start
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, float('inf')])

        pq = [] # max heap
        curr_fuel = startFuel 
        curr_pos = 0
        res = 0

        for i in range(len(stations)):
            pos, fuel = stations[i]
            curr_fuel -= pos - curr_pos
            curr_pos = pos

            while pq and curr_fuel < 0:
                top = heapq.heappop(pq)
                curr_fuel += -top
                res += 1
            
            if curr_fuel < 0:
                return -1

            heapq.heappush(pq, -fuel)

        return res
             
# @lc code=end

