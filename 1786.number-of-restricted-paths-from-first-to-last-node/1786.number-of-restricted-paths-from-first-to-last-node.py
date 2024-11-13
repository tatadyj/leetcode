#
# @lc app=leetcode id=1786 lang=python3
#
# [1786] Number of Restricted Paths From First to Last Node
#

# @lc code=start
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        adj_dict = defaultdict(list)
        for u, v, w in edges:
            adj_dict[u-1].append((v-1, w))
            adj_dict[v-1].append((u-1, w))

        pq = [(0, n-1)]
        dist = [-1] * n
        while pq:
            d, curr = heapq.heappop(pq)
            if dist[curr] != -1: continue
            dist[curr] = d

            for nxt, w in adj_dict[curr]:
                if dist[nxt] != -1: continue 
                heapq.heappush(pq, (w + d, nxt))

        #print(dist)
        memo = [None] * n
        def dfs(curr):
            if curr == n-1:
                return 1
            
            if memo[curr] is not None:
                return memo[curr]
    
            count = 0
            for nxt, _ in adj_dict[curr]:
                if dist[nxt] >= dist[curr]: continue 
                count += dfs(nxt)
            memo[curr] = count
            return count 

        return dfs(0) % (10**9 + 7)   
# @lc code=end

