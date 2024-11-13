#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_dict = defaultdict(list)
        for fr, to, p in flights:
            adj_dict[fr].append((to, p))

        pq = [(0, src, 0)] # price, city, stop
        memo = [[False]*(k+2) for _ in range(n)] # memo[city][stop] 最多k+1次飞机

        while pq:
            price, curr, stop = heapq.heappop(pq)
            if memo[curr][stop]: continue 
            memo[curr][stop] = True 
            if curr == dst:
                return price

            for nxt, w in adj_dict[curr]:
                if stop + 1 > k + 1: continue
                if memo[nxt][stop+1]: continue 
                heapq.heappush(pq, (price + w, nxt, stop+1))
        return -1    
# @lc code=end

