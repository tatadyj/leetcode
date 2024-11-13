#
# @lc app=leetcode id=1976 lang=python3
#
# [1976] Number of Ways to Arrive at Destination
#

# @lc code=start
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj_dict = defaultdict(list)
        for u, v, t in roads:
            adj_dict[u].append((v, t))
            adj_dict[v].append((u, t))

        pq = [(0, n-1)]

        min_t = inf
        dist =  [-1] * n
        while pq:
            time, curr = heapq.heappop(pq)
            if dist[curr] != -1: continue 
            dist[curr] = time

            if curr == 0:
                min_t = time
            
            for nxt, w in adj_dict[curr]:
                if dist[nxt] != -1: continue
                heapq.heappush(pq, (w+time, nxt))

        #print(min_t)

        memo = [None] * n
        def dfs(curr, curr_t):
            if curr == n-1:
                return 1 

            if memo[curr] is not None:
                return memo[curr]

            count = 0
            for nxt, nxt_t in adj_dict[curr]:
                if dist[nxt] + curr_t + nxt_t != min_t: continue 
                count += dfs(nxt, curr_t + nxt_t)
            
            memo[curr] = count
            return count

        return dfs(0, 0) % (10**9 + 7)
              
# @lc code=end

