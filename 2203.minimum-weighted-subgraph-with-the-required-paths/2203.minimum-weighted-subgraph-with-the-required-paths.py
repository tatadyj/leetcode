#
# @lc app=leetcode id=2203 lang=python3
#
# [2203] Minimum Weighted Subgraph With the Required Paths
#

# @lc code=start
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        adj_dict = defaultdict(list)
        pre_dict = defaultdict(list)
        for f, t, w in edges:
            adj_dict[f].append((t, w))
            pre_dict[t].append((f, w))

        def dijkstra(start, graph):
            pq = [(0, start)]
            dist = [-1] * n
            while pq:
                d, curr = heapq.heappop(pq)
                if dist[curr] != -1: continue 
                dist[curr] = d

                for nxt, w in graph[curr]:
                    if dist[nxt] != -1: continue
                    heapq.heappush(pq, (w+d, nxt))
            return dist

        dist_src1 = dijkstra(src1, adj_dict)
        dist_src2 = dijkstra(src2, adj_dict)
        dist_dest = dijkstra(dest, pre_dict)

        ans = inf
        for i in range(n):
            if dist_src1[i] == -1: continue 
            if dist_src2[i] == -1: continue 
            if dist_dest[i] == -1: continue 
            ans = min(ans, dist_src1[i]+dist_src2[i]+dist_dest[i])
        if ans == inf: return -1
        return ans
# @lc code=end

