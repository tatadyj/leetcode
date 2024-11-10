#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
def dfs(grid, m, n, i, j):
    #if i < 0 or j < 0 or i >= m or j >=n or grid[i][j] != "1":
    #    return 
    
    grid[i][j] = "*"
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direct in directions:
        next_i, next_j = i + direct[0], j + direct[1]
        if next_i < 0 or next_j < 0 or next_i >= m or next_j >=n or grid[next_i][next_j] != "1":
            continue 
        dfs(grid, m, n, next_i, next_j)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(grid, m, n, i, j)
                    res += 1
        return res 
        
        
# @lc code=end

