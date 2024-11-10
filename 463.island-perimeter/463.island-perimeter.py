#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4
                    if i-1 >= 0 and grid[i-1][j] == 1:
                        res -= 1
                    if i+1 < m and grid[i+1][j] == 1:
                        res -= 1
                    if j-1 >= 0 and grid[i][j-1] == 1:
                        res -= 1
                    if j+1 < n and grid[i][j+1] == 1:
                        res -= 1
        return res
        
Solution().islandPerimeter([[1,1]])
# @lc code=end

