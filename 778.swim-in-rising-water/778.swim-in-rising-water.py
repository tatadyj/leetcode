#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#

# @lc code=start
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pq = [(grid[0][0], (0,0))]

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * n for _ in range(n)]
        level = 0
        while pq:
            h, (x,y) = heapq.heappop(pq)
            if visited[x][y]: continue # 必须要在出队列时skip
            visited[x][y] = True  # pq 一定要在出队列时标记
            level = max(level, h)
            if x == n-1 and y == n-1:
                return level

            for dx, dy in dir:
                nxt_x, nxt_y = x + dx, y + dy 
                if nxt_x < 0 or nxt_x >= n or nxt_y < 0 or nxt_y >= n: continue 
                if visited[nxt_x][nxt_y]: continue 
                heapq.heappush(pq, (grid[nxt_x][nxt_y], (nxt_x, nxt_y)))

      
# @lc code=end

