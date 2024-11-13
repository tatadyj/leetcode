#
# @lc app=leetcode id=1368 lang=python3
#
# [1368] Minimum Cost to Make at Least One Valid Path in a Grid
#

# @lc code=start
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        pq = [(0, 0, 0)]
        visited = [[False] * n for _ in range(m)]
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while pq:
            d, x, y = heapq.heappop(pq)
            if visited[x][y]: continue 
            visited[x][y] = True

            if x == m-1 and y == n-1:
                return d

            for i, (dx, dy) in enumerate(dir):
                nxt_x, nxt_y = x + dx, y + dy 
                if nxt_x < 0 or nxt_x >= m or nxt_y < 0 or nxt_y >= n: continue 
                if visited[nxt_x][nxt_y]: continue 
                if grid[x][y] == i+1:
                    weight = 0 
                else:
                    weight = 1
                heapq.heappush(pq, (d + weight, nxt_x, nxt_y))

# @lc code=end

