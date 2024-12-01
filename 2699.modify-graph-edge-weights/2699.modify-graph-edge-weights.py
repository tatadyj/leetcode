#
# @lc app=leetcode id=2699 lang=python3
#
# [2699] Modify Graph Edge Weights
#

# @lc code=start
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:

        adj_dict = defaultdict(dict)
        flag = [[0]*n for _ in range(n)]
        for a, b, w in edges:
            if w != -1:
                adj_dict[a][b] = w
                adj_dict[b][a] = w
            else:
                adj_dict[a][b] = 1
                adj_dict[b][a] = 1
                flag[a][b] = 1
                flag[b][a] = 1

        dist_d = [-1] * n 
        pq = [(0, destination)]
        while pq:
            w, cur = heapq.heappop(pq)
            if dist_d[cur] != -1: continue 
            dist_d[cur] = w

            for nxt in adj_dict[cur]:
                nxt_w = adj_dict[cur][nxt]
                if dist_d[nxt] != -1: continue 
                heapq.heappush(pq, (w + nxt_w, nxt))

        # dijkstra 2nd time
        pq = [(0, source)]
        dist = [-1] * n 
        while pq:
            w, cur = heapq.heappop(pq)
            if dist[cur] != -1: continue 
            dist[cur] = w

            if cur == destination and w != target:
                return []

            for nxt in adj_dict[cur]:

                if dist[nxt] != -1: continue 
                if flag[cur][nxt] == 1:
                    if dist_d[nxt] + w + adj_dict[cur][nxt] < target:
                        adj_dict[cur][nxt] = target - dist_d[nxt] - w
                        adj_dict[nxt][cur] = target - dist_d[nxt] - w
                heapq.heappush(pq, (w + adj_dict[cur][nxt], nxt))

        ans = []
        for a, b, _ in edges:
            ans.append([a, b, adj_dict[a][b]])
        return ans  
# @lc code=end

