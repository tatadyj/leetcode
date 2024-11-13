#
# @lc app=leetcode id=882 lang=python3
#
# [882] Reachable Nodes In Subdivided Graph
#

# @lc code=start
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        adj_dict = defaultdict(list)
        for u, v, cnt in edges:
            adj_dict[u].append((v, cnt+1))
            adj_dict[v].append((u, cnt+1))

        pq = [(0, 0)]
        dist = [-1] * n
        while pq:
            d, curr = heapq.heappop(pq)
            if dist[curr] != -1: continue 
            dist[curr] = d 

            for nxt, cnt in adj_dict[curr]:
                if dist[nxt] != -1: continue
                if d + cnt > maxMoves: continue
                heapq.heappush(pq, (d+cnt, nxt))
        
        ans = 0
        for u, v, cnt in edges:
            sum = 0
            if dist[u] != -1 and dist[u] < maxMoves:
                sum += maxMoves - dist[u]
            if dist[v] != -1 and dist[v] < maxMoves:
                sum += maxMoves - dist[v]
            sum = min(sum, cnt)
            ans += sum

        for i in range(n):
            if dist[i] != -1:
                ans += 1 
        return ans     
# @lc code=end

