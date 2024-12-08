#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(grid, m, n, i, j):
            #if i < 0 or j < 0 or i >= m or j >=n or grid[i][j] != 1:
            #    return 0
            
            grid[i][j] = 0
            count = 1
            for direct in directions:
                next_i, next_j = i + direct[0], j + direct[1]
                if next_i < 0 or next_j < 0 or next_i >= m or next_j >=n or grid[next_i][next_j] != 1:
                    continue 
                count += dfs(grid, m, n, next_i, next_j)
            return count

        res = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = dfs(grid, m, n, i, j)
                    res = max(res, count)
        return res 
# @lc code=end

