#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

# @lc code=start
def getId(grid, m, n, i, j):
    if i >= 0 and i < m and j >= 0 and j < n:
        return grid[i][j]
    else:
        return 0

def dfs(grid, m, n, i, j, id):
    if i < 0 or j < 0 or i >= m or j >= m or grid[i][j] != 1: return 0

    grid[i][j] = id[0] 
    
    left = dfs(grid, m, n, i, j-1, id)
    right = dfs(grid, m, n, i, j+1, id)
    up = dfs(grid, m, n, i-1, j, id)
    down = dfs(grid, m, n, i+1, j, id)
    return 1+left+right+up+down 

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        id = [2]
        area = [0, 0]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area.append(dfs(grid, m, n, i, j, id))
                    id[0] += 1
        max_area = max(area)

        for i in range(m):
            for j in range(n):
                res = 1
                if grid[i][j] == 0:
                    for next_id in set([getId(grid, m, n, i, j-1), 
                                        getId(grid, m, n, i, j+1), 
                                        getId(grid, m, n, i-1, j), 
                                        getId(grid, m, n, i+1, j)]):
                        res += area[next_id]
                    max_area = max(max_area, res)

        return max_area

# @lc code=end

