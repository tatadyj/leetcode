#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
def dfs(grid, m, n, i, j):
    if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 1: return 0
    
    grid[i][j] = -1
    right = dfs(grid, m, n, i, j+1)
    left = dfs(grid, m, n, i, j-1)
    up = dfs(grid, m, n, i+1, j)
    down = dfs(grid, m, n, i-1, j)
    return right+left+up+down+1
    
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0 
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curr = dfs(grid, m, n, i, j)
                    if curr > res:
                        res = curr

        return res
# @lc code=end

