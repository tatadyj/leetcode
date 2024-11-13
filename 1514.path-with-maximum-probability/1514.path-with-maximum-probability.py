#
# @lc app=leetcode id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#

# @lc code=start
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_dict = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            if succProb[i] == 0:
                val = float('-inf')
            else:
                val = -log(succProb[i])
            adj_dict[a].append((b, val))
            adj_dict[b].append((a, val))

        visited = [False] * n # undirected needed 
        pq = [(0, start_node)]
        while pq:
            d, curr = heapq.heappop(pq)
            visited[curr] = True
            if curr == end_node:
                if d == float('-inf'):
                    return 0 
                else:
                    return exp(-d)
            for nxt, weight in adj_dict[curr]:
                if visited[nxt]: continue
                heapq.heappush(pq, (weight + d, nxt))
        return 0    
# @lc code=end

