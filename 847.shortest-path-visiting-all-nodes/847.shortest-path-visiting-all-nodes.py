#
# @lc app=leetcode id=847 lang=python3
#
# [847] Shortest Path Visiting All Nodes
#

# @lc code=start
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        final_state = 0
        for i in range(n):
            final_state = final_state | (1 << i)
        
        visited = [set() for _ in range(n)] # [set()] * n is incorrect, copy by reference
        queue = deque() # (i, state, level)
        for i in range(n):
            queue.append((i, 1<<i, 0))
            visited[i].add(1<<i) 

        while queue:
            size = len(queue)
            for _ in range(size):
                curr, state, level = queue.popleft()
                for nxt in graph[curr]:
                    nxt_state = state | (1 << nxt)
                    if nxt_state in visited[nxt]: continue
                    if nxt_state == final_state:
                        return level + 1 
                    queue.append((nxt, nxt_state, level+1))
                    visited[nxt].add(nxt_state)
        return 0

# @lc code=end

