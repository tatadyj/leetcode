#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
def dfs(grid, m, n, i, j):
    if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1': return 

    grid[i][j] = '*'
    dfs(grid, m, n, i, j+1)
    dfs(grid, m, n, i, j-1)
    dfs(grid, m, n, i+1, j)
    dfs(grid, m, n, i-1, j) 


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(grid, m, n, i, j)
                    res += 1 
        return res 

        
# @lc code=end

