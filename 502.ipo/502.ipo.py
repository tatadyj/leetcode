#
# @lc app=leetcode id=502 lang=python3
#
# [502] IPO
#

# @lc code=start
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        arr = []
        for i in range(len(profits)):
            arr.append((capital[i], profits[i]))

        arr.sort()
        pq = [] # max heap

        count = 0 
        i = 0
        while count < k:
            while i < len(arr) and arr[i][0] <= w:
                heapq.heappush(pq, -arr[i][1])
                i += 1
            
            if not pq:
                break 
                
            if pq:
                top = heapq.heappop(pq)
                w += -top
                count += 1

        return w
         
# @lc code=end

