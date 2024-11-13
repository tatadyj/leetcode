#
# @lc app=leetcode id=2812 lang=python3
#
# [2812] Find the Safest Path in a Grid
#

# @lc code=start
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]

        queue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
                    dist[i][j] = 0
        
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y, l = queue.popleft()
                for dx, dy in dir:
                    nxt_x, nxt_y = x + dx, y + dy 
                    if nxt_x < 0 or nxt_x >= n or nxt_y < 0 or nxt_y >= n: continue
                    if dist[nxt_x][nxt_y] != -1: continue
                    dist[nxt_x][nxt_y] = l + 1
                    queue.append((nxt_x, nxt_y, l + 1))

        # print(dist)
        def is_ok(min_val):
            if dist[0][0] < min_val: 
                return False
            q = deque([(0,0)])
            visited = [[False]*n for _ in range(n)]
            visited[0][0] = True
            while q:
                x, y = q.popleft()
                for dx, dy in dir:
                    nxt_x, nxt_y = x + dx, y + dy 
                    if nxt_x < 0 or nxt_x >= n or nxt_y < 0 or nxt_y >= n: continue
                    if visited[nxt_x][nxt_y]: continue
                    if dist[nxt_x][nxt_y] < min_val: continue
                    q.append((nxt_x, nxt_y))
                    visited[nxt_x][nxt_y] = True
            return visited[n-1][n-1]   

        if n == 1: return dist[0][0]
        left, right = 0, n**2
        while left < right:
            mid = (left + right + 1) // 2
            if is_ok(mid):
                left = mid 
            else:
                right = mid - 1
        return left 
 
# @lc code=end

