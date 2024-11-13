#
# @lc app=leetcode id=1568 lang=python3
#
# [1568] Minimum Number of Days to Disconnect Island
#

# @lc code=start
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs():
            visited = [[False] * n for _ in range(m)]
            num_island = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 0: continue 
                    if visited[i][j]: continue  
                    queue = deque()
                    queue.append((i, j))
                    visited[i][j] = True
                 
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in dir:
                            nxt_x, nxt_y = x + dx, y + dy 
                            if nxt_x < 0 or nxt_x >= m or nxt_y < 0 or nxt_y >= n: continue
                            if visited[nxt_x][nxt_y]: continue
                            if grid[nxt_x][nxt_y] == 0: continue
                            queue.append((nxt_x, nxt_y))
                            visited[nxt_x][nxt_y] = True
                    num_island += 1
                    if num_island > 1:
                        return num_island 
            return num_island

        num_island = bfs()
        if num_island != 1:
            return 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    count = bfs()
                    if count > 1 or count == 0: return 1
                    grid[i][j] = 1
        return 2
   
# @lc code=end

