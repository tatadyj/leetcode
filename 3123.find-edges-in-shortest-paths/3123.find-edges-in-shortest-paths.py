#
# @lc app=leetcode id=3123 lang=python3
#
# [3123] Find Edges in Shortest Paths
#

# @lc code=start
class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        adj_dict = defaultdict(list)
        for a, b, w in edges:
            adj_dict[a].append((b, w))
            adj_dict[b].append((a, w))

        def dijkstra(s):
            dist = [-1] * n
            pq = [(0, s)]

            while pq:
                w, curr = heapq.heappop(pq)
                if dist[curr] != -1: continue 
                dist[curr] = w 
                
                for nxt, nxt_w in adj_dict[curr]:
                    if dist[nxt] != -1: continue 
                    heapq.heappush(pq, (w + nxt_w, nxt))
            return dist

        dist_s = dijkstra(0)
        dist_d = dijkstra(n-1)

        ans = [False] * len(edges)
        for i, (a, b, w) in enumerate(edges):
            if (dist_s[a] != -1 and dist_d[b] != -1) and dist_s[a] + w + dist_d[b] == dist_s[n-1]:
                ans[i] = True 
            if  (dist_s[b] != -1 and dist_d[a] != -1) and dist_s[b] + w + dist_d[a] == dist_s[n-1]:
                ans[i] = True
           
        return ans   
# @lc code=end

