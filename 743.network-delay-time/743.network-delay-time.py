#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, k)]
        visited = [False] * (n + 1)
        ret = 0
        while pq:
            d, curr = heapq.heappop(pq)
            if visited[curr]: continue 
            visited[curr] = True 
            ret = max(ret, d)
            for nxt, weight in graph[curr]:
                if visited[nxt]: continue 
                heapq.heappush(pq, (d + weight, nxt))

        if sum(visited[1:]) == n:
            return ret 
        else: 
            return -1   
# @lc code=end

