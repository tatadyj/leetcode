#
# @lc app=leetcode id=1928 lang=python3
#
# [1928] Minimum Cost to Reach Destination in Time
#

# @lc code=start
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        unique = defaultdict(int)
        for x, y, t in edges:
            if (x, y) not in unique:
                unique[(x, y)] = t 
            else:
                unique[(x, y)] = min(t, unique[(x, y)])

        adj_dict = defaultdict(list)
        for x, y in unique:
            adj_dict[x].append((y, unique[(x, y)]))
            adj_dict[y].append((x, unique[(x, y)]))

        n = len(passingFees)
        pq = [(passingFees[0], 0, 0)] #cost, city, time
        memo = [[False] * (maxTime + 1) for _ in range(n)]

        while pq:
            cost, curr, time = heapq.heappop(pq)
            if memo[curr][time]: continue 
            memo[curr][time] = True 

            if curr == n-1:
                return cost 

            for nxt, t in adj_dict[curr]:
                if time + t > maxTime: continue
                if memo[nxt][time + t]: continue 
                heapq.heappush(pq, (cost + passingFees[nxt], nxt, time + t))
        return -1
         
# @lc code=end

