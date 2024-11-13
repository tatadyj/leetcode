#
# @lc app=leetcode id=1559 lang=python3
#
# [1559] Detect Cycles in 2D Grid
#

# @lc code=start
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(i, j):
            queue = deque()
            queue.append(((i, j), (-1, -1)))
            visited[i][j] = True 

            while queue:
                (i, j), prev = queue.popleft()
                for di, dj in dir:
                    nxt_i, nxt_j = i + di, j + dj
                    if nxt_i < 0 or nxt_i >= m or nxt_j < 0 or nxt_j >= n: continue 
                    if (nxt_i, nxt_j) == prev: continue
                    if grid[nxt_i][nxt_j] != grid[i][j]: continue 
                    if visited[nxt_i][nxt_j]: 
                        return True
                    queue.append(((nxt_i, nxt_j), (i, j)))
                    visited[nxt_i][nxt_j] = True 
            return False

        for i in range(m):
            for j in range(n):
                if visited[i][j]: continue 
                if bfs(i, j):
                    return True 
        return False 
                 
# @lc code=end

