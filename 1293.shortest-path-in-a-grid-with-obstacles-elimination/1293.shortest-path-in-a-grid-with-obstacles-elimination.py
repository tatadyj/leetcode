#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#

# @lc code=start
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == n == 1: return 0

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[[False] * (k+1) for _ in range(n)] for _ in range(m)]
        visited[0][0][0]= True
        queue = deque()
        queue.append((0, 0, 0, 0)) # i, j, k, level
        
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y, c, l = queue.popleft()
                for dx, dy in dir:
                    nxt_x, nxt_y = x + dx, y + dy
                    if nxt_x < 0 or nxt_x >= m or nxt_y < 0 or nxt_y >= n: continue
                    if grid[nxt_x][nxt_y] == 1:
                        nxt_c = c + 1
                    else:
                        nxt_c = c
                    if nxt_c > k: continue
                    if visited[nxt_x][nxt_y][nxt_c]: continue
                    if nxt_x == m-1 and nxt_y == n-1:
                        return l + 1
                    queue.append((nxt_x, nxt_y, nxt_c, l+1))
                    visited[nxt_x][nxt_y][nxt_c]= True
        return -1

# @lc code=end

